#!/usr/bin/env python3
"""Fetch remaining ADR-0006 calibration bytes into a review cache.

The supported Perplexity content fetcher is used first for HTML captures.
Direct HTTPS is used only to preserve exact PDF bytes, which the cleaned-content
interface can read but does not return as a downloadable byte stream.

Outputs are outside the repository until hashes, media types, and policy checks
pass. Promotion into `artifacts/` is a separate explicit step.

Outcome:
    Successfully used on 2026-09-05. The managed fetcher returned raw HTML for
    all three pages without fallback. Direct HTTPS preserved three official
    PDFs. The resulting cache contains six captures plus a hash/transport
    manifest. Policy review allowed two HTML captures to be materialized and
    required the third to remain hash-addressed but remote-only.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pplx_sdk
from urllib.request import Request, urlopen


OUT = Path("/home/user/workspace/fmo-remaining-20260905")
OUT.mkdir(parents=True, exist_ok=True)

HTML_URLS = {
    "anthropic-claude-opus-5-system-prompt.html":
        "https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-5",
    "openai-sora-2-system-card.html":
        "https://deploymentsafety.openai.com/sora-2",
    "google-gemma-4-model-card.html":
        "https://ai.google.dev/gemma/docs/core/model_card_4",
}
PDF_URLS = {
    "anthropic-claude-4-system-card-current.pdf":
        "https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf",
    "anthropic-claude-4-system-card-earlier.pdf":
        "https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47.pdf",
    "openai-gpt-5-2-system-card-update.pdf":
        "https://cdn.openai.com/pdf/3a4153c8-c748-4b71-8e31-aecbde944f8d/oai_5_2_system-card.pdf",
}


manifest = []
pages = pplx_sdk.content.fetch(
    list(HTML_URLS.values()), cache_enabled=False, return_html=True
)
by_url = {page.url: page for page in pages}

for filename, url in HTML_URLS.items():
    page = by_url.get(url)
    if page is None or page.error:
        raise RuntimeError(f"managed fetch failed for {url}: {page and page.error}")
    raw = page.raw_html
    method = "managed_fetch_raw_html"
    if not raw:
        request = Request(url, headers={"User-Agent": "FrontierModelObservatory/0"})
        with urlopen(request, timeout=60) as response:
            raw = response.read().decode("utf-8")
        method = "direct_https_fallback_no_raw_html"
    data = raw.encode("utf-8")
    path = OUT / filename
    path.write_bytes(data)
    manifest.append(
        {
            "filename": filename,
            "requested_url": url,
            "method": method,
            "sha256": hashlib.sha256(data).hexdigest(),
            "byte_length": len(data),
            "media_type_detected": "text/html",
        }
    )

for filename, url in PDF_URLS.items():
    request = Request(url, headers={"User-Agent": "FrontierModelObservatory/0"})
    with urlopen(request, timeout=120) as response:
        data = response.read()
        if not data.startswith(b"%PDF-"):
            raise RuntimeError(f"{url} did not return PDF bytes")
        path = OUT / filename
        path.write_bytes(data)
        manifest.append(
            {
                "filename": filename,
                "requested_url": url,
                "final_url": response.geturl(),
                "method": "direct_https_pdf_bytes",
                "status_code": response.status,
                "content_type": response.headers.get("content-type"),
                "last_modified": response.headers.get("last-modified"),
                "etag": response.headers.get("etag"),
                "sha256": hashlib.sha256(data).hexdigest(),
                "byte_length": len(data),
                "media_type_detected": "application/pdf",
            }
        )

(OUT / "manifest.json").write_text(
    json.dumps(sorted(manifest, key=lambda item: item["filename"]), indent=2)
    + "\n",
    encoding="utf-8",
)
print(json.dumps(manifest, indent=2))
