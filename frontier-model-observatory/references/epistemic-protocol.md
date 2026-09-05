# Epistemic protocol

## Evidence-bearing claims

For every load-bearing statement preserve:

- exact subject identity and kind;
- who made the claim;
- artifact and artifact-version identity;
- page, section, table, anchor, quote, or other locator;
- valid time and observed time;
- epistemic status;
- correction, supersession, dispute, or derivation relationships.

Provider publication proves that the provider made a statement. It does not
independently prove the statement's truth.

## Source order

Prefer:

1. provider-issued artifact bytes or provider-rendered page;
2. provider artifact/index surface;
3. provider release or technical documentation;
4. independent primary evaluator report;
5. third-party archive only to locate or preserve a missing primary artifact;
6. commentary only for discovery or clearly attributed interpretation.

Never promote a mirror into the provenance root while an official artifact is
available.

## Temporal discipline

Maintain at least:

- valid time: when a model, deployment, alias, claim, or event applied;
- observed time: when the evidence was encountered;
- artifact date role: publication, cover, revision, index, platform, metadata,
  or transport;
- Git history: when the repository representation changed.

Do not manufacture day precision from a month or year. Do not use an HTTP
`Last-Modified` header as a provider-authored revision statement.

## Typed negative findings

- `not_reported`: the artifact does not state the requested field.
- `not_found`: a bounded search did not locate it; schedule a recheck.
- `not_evaluated`: evidence says the evaluation was not performed.
- `withheld`: evidence says information exists but was not disclosed.
- `not_applicable`: evidence establishes the field does not apply.
- `not_retrieved`: a known artifact was not downloaded.
- `confirmed_absent`: authoritative or exhaustive evidence proves absence.
- `excluded_by_policy`: collection or materialization is intentionally barred.

Unknown is not zero, false, or absent.

## Comparison contract

Before ranking or computing a difference, verify:

- same subject level;
- same model/checkpoint/configuration;
- same benchmark and version;
- same metric and units;
- compatible prompt, harness, tools, and attempt count;
- same pre/post-mitigation state;
- compatible publication or as-of boundary.

If any decisive dimension differs, juxtapose with caveats. Do not normalize
away provider-native artifact terms or risk taxonomies.

## Confidence

Use confidence only for observatory inference, not provider statements or
measured results. Name:

- the inference;
- supporting evidence;
- plausible alternatives;
- what would falsify or materially change it.
