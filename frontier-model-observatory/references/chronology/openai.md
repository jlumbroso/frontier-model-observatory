# OpenAI chronology

Generated from the official-source chronology observed 2026-09-05.
These are research projections, not canonical records. Preserve typed
gaps, date precision, and competing provider values.

Rows: **101**.

## **GPT-6 Astra**

- Source report line: `81`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-6
- **Exact name**: **GPT-6 Astra**
- **Kind**: model
- **Native kind wording**: "Our most capable model, built for the hardest end-to-end work" ([model page](https://platform.openai.com/docs/models/gpt-6-astra))
- **API ID / default snapshot**: `gpt-6-astra`; default snapshot `gpt-6-astra` ([model page](https://platform.openai.com/docs/models/gpt-6-astra))
- **Announcement**: [Sep 3, 2026](https://deploymentsafety.openai.com/) — "Sep 03, 2026 · GPT-6 Astra System Card"
- **Release / API availability**: [Sep 3, 2026](https://platform.openai.com/docs/changelog) — "Released GPT-6 Astra … Use GPT-6 Astra for reasoning, coding, computer use, research, and document creation"
- **GA**: **Not yet GA:** "Access is rolling out to a limited set of organizations. Astra is not yet generally available. Broader availability is planned over the coming days." ([ChatGPT release notes, Sep 3, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses API + Chat Completions ([changelog](https://platform.openai.com/docs/changelog)); ChatGPT limited rollout ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-6-astra))
- **Knowledge cutoff**: "Apr 30, 2026 knowledge cutoff" ([model page](https://platform.openai.com/docs/models/gpt-6-astra)) — applies to the API model
- **Relations**: "significantly more robust than its predecessors"; compared throughout with GPT-5.6 Sol ([system card](https://deploymentsafety.openai.com/gpt-6-astra))
- **Card**: [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra)
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-6-astra)
- **Lifecycle 2026-09-05**: Released / limited availability
- **Notes / typed gaps**: Breaking constraints at launch: no `none` reasoning effort, no custom `temperature`/`top_p`/`logprobs`, tool calling requires Responses API ([changelog](https://platform.openai.com/docs/changelog)). The catalog's HTML "Choosing a model" text still recommends GPT-5.6 Sol as flagship while [models.md](https://platform.openai.com/docs/models.md) recommends GPT-6 Astra — see §7.

## **GPT-5.6 Sol**

- Source report line: `82`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.6
- **Exact name**: **GPT-5.6 Sol**
- **Kind**: model
- **Native kind wording**: "Frontier model for complex professional work" ([model page](https://platform.openai.com/docs/models/gpt-5.6-sol))
- **API ID / default snapshot**: `gpt-5.6-sol`, alias `gpt-5.6` ([Models](https://platform.openai.com/docs/models))
- **Announcement**: preview card [Jun 26, 2026](https://deploymentsafety.openai.com/); private red-team access "beginning June 3rd, 2026" ([preview card](https://deploymentsafety.openai.com/gpt-5-6-preview))
- **Release / API availability**: [Jul 9, 2026](https://platform.openai.com/docs/changelog) — "Released the GPT-5.6 model family … The `gpt-5.6` alias routes requests to `gpt-5.6-sol`"; ChatGPT rollout began the same day ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **GA**: "The GPT-5.6 models are now broadly available" ([system card](https://deploymentsafety.openai.com/gpt-5-6)); no calendar date stated → `not_reported`
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses, Chat Completions, Batch ([changelog](https://platform.openai.com/docs/changelog)); ChatGPT paid plans, not Free/Go/logged-out at launch ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes)); Codex and ChatGPT Work ([August update card](https://deploymentsafety.openai.com/gpt-5-6-august-update)); Daybreak Blue tier ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.6-sol))
- **Knowledge cutoff**: "Feb 16, 2026 knowledge cutoff" ([model page](https://platform.openai.com/docs/models/gpt-5.6-sol))
- **Relations**: family sibling of Terra and Luna; "GPT-5.6 is a new family of three models: Sol, our new flagship model; Terra, a capable lower-cost option; and Luna, our fastest and most cost-efficient model" ([system card](https://deploymentsafety.openai.com/gpt-5-6))
- **Card**: [GPT-5.6 System Card](https://deploymentsafety.openai.com/gpt-5-6) · [preview card](https://deploymentsafety.openai.com/gpt-5-6-preview) · [August update](https://deploymentsafety.openai.com/gpt-5-6-august-update)
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.6-sol)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: Price cut to $4/$20 per 1M on [Aug 21, 2026](https://platform.openai.com/docs/changelog), "promotional pricing … at least through November 21, 2026". Ultrafast mode announced [Aug 13, 2026](https://platform.openai.com/docs/changelog) (limited preview).
- **Typed absences**: `not_reported`

## **GPT-5.6 Sol (August)**

- Source report line: `83`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.6
- **Exact name**: **GPT-5.6 Sol (August)**
- **Kind**: configuration
- **Native kind wording**: month-distinguished deployment version — "we distinguish these models by their month of release: August for the versions released today, and July for the versions that remain in use in Codex and Work" ([August update card](https://deploymentsafety.openai.com/gpt-5-6-august-update))
- **API ID / default snapshot**: no separate API ID (`not_applicable`)
- **Announcement**: [Aug 6, 2026](https://deploymentsafety.openai.com/) — "Aug 06, 2026 · GPT-5.6 — August Updates"
- **Release / API availability**: [Aug 6, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — "Plus and Pro users can now use an updated GPT-5.6 Sol in ChatGPT"
- **GA**: not_applicable
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: ChatGPT chat experience only — "Work and Codex are not changing as part of this release" ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Modalities**: text, image → text
- **Knowledge cutoff**: not_reported on the card
- **Relations**: "deployed with the respective safeguards developed for the previous models" ([August update card](https://deploymentsafety.openai.com/gpt-5-6-august-update))
- **Card**: [GPT-5.6 August update card](https://deploymentsafety.openai.com/gpt-5-6-august-update)
- **Docs**: [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **Lifecycle 2026-09-05**: Active in ChatGPT
- **Notes / typed gaps**: Two live configurations of one API model, separated only by deployment surface — the clearest OpenAI case for configuration-level modeling.
- **Typed absences**: `not_applicable`, `not_reported`

## **GPT-5.6 Terra**

- Source report line: `84`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.6
- **Exact name**: **GPT-5.6 Terra**
- **Kind**: model
- **Native kind wording**: "GPT-5.6 model that balances intelligence and cost" ([model page](https://platform.openai.com/docs/models/gpt-5.6-terra))
- **API ID / default snapshot**: `gpt-5.6-terra` ([model page](https://platform.openai.com/docs/models/gpt-5.6-terra))
- **Announcement**: [Jun 26, 2026](https://deploymentsafety.openai.com/gpt-5-6-preview) (preview card)
- **Release / API availability**: [Jul 9, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported (family "broadly available", no date)
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses, Chat Completions, Batch; "Availability for other GPT-5.6 family models varies by product and plan" ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.6-terra))
- **Knowledge cutoff**: "Feb 16, 2026" ([model page](https://platform.openai.com/docs/models/gpt-5.6-terra))
- **Relations**: GPT-5.6 family ([system card](https://deploymentsafety.openai.com/gpt-5-6))
- **Card**: [GPT-5.6 System Card](https://deploymentsafety.openai.com/gpt-5-6)
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.6-terra)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: 20% price reduction [Jul 30, 2026](https://platform.openai.com/docs/changelog). Recommended replacement for many retired legacy models ([deprecations](https://platform.openai.com/docs/deprecations)).
- **Typed absences**: `not_reported`

## **GPT-5.6 Luna**

- Source report line: `85`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.6
- **Exact name**: **GPT-5.6 Luna**
- **Kind**: model
- **Native kind wording**: "GPT-5.6 model optimized for cost-sensitive workloads" ([model page](https://platform.openai.com/docs/models/gpt-5.6-luna))
- **API ID / default snapshot**: `gpt-5.6-luna` ([model page](https://platform.openai.com/docs/models/gpt-5.6-luna))
- **Announcement**: [Jun 26, 2026](https://deploymentsafety.openai.com/gpt-5-6-preview)
- **Release / API availability**: [Jul 9, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: API; ChatGPT — "GPT-5.6 Luna will become the default model for Free and Go users this week" ([ChatGPT release notes, Aug 6, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.6-luna))
- **Knowledge cutoff**: "Feb 16, 2026" ([model page](https://platform.openai.com/docs/models/gpt-5.6-luna))
- **Relations**: GPT-5.6 family
- **Card**: [GPT-5.6 System Card](https://deploymentsafety.openai.com/gpt-5-6) · [August update](https://deploymentsafety.openai.com/gpt-5-6-august-update)
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.6-luna)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: 80% price reduction [Jul 30, 2026](https://platform.openai.com/docs/changelog). An August ChatGPT configuration exists alongside the July version ([August update card](https://deploymentsafety.openai.com/gpt-5-6-august-update)).
- **Typed absences**: `not_reported`

## **GPT-5.6 Cyber**

- Source report line: `86`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.6
- **Exact name**: **GPT-5.6 Cyber**
- **Kind**: model
- **Native kind wording**: "Our most advanced cybersecurity model for authorized vulnerability research and security testing" ([Models](https://platform.openai.com/docs/models))
- **API ID / default snapshot**: `gpt-5.6-cyber` ([model page](https://platform.openai.com/docs/models/gpt-5.6-cyber))
- **Announcement**: [Aug 7, 2026](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Aug 7, 2026](https://platform.openai.com/docs/changelog) — "Daybreak now offers two access tiers for approved defenders: Daybreak Blue and Daybreak Red"
- **GA**: not_applicable — approved defenders only ([changelog](https://platform.openai.com/docs/changelog))
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses API, gated behind Daybreak Red approval ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.6-cyber))
- **Knowledge cutoff**: "Feb 16, 2026" ([model page](https://platform.openai.com/docs/models/gpt-5.6-cyber))
- **Relations**: default snapshot behind the `gpt-daybreak-red-latest` alias ([model page](https://platform.openai.com/docs/models/gpt-daybreak-red-latest))
- **Card**: not_found (no separate Cyber system card on the [Deployment Safety Hub](https://deploymentsafety.openai.com/) index)
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.6-cyber)
- **Lifecycle 2026-09-05**: Active, access-gated
- **Notes / typed gaps**: —
- **Typed absences**: `not_applicable`, `not_found`

## **GPT-5.5**

- Source report line: `87`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.5
- **Exact name**: **GPT-5.5**
- **Kind**: model
- **Native kind wording**: "A new class of intelligence for coding and professional work" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5.5`, default snapshot `gpt-5.5-2026-04-23` ([model page](https://platform.openai.com/docs/models/gpt-5.5))
- **Announcement**: [Apr 23, 2026](https://deploymentsafety.openai.com/) — "Apr 23, 2026 · GPT-5.5 System Card"
- **Release / API availability**: [Apr 24, 2026](https://platform.openai.com/docs/changelog) — "Released GPT-5.5, a new frontier model for complex professional work, to the Chat Completions and Responses API"
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Chat Completions, Responses, Batch ([changelog](https://platform.openai.com/docs/changelog)); available in Amazon Bedrock through an OpenAI-compatible Responses endpoint from [Jun 1, 2026](https://platform.openai.com/docs/changelog); ChatGPT ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.5))
- **Knowledge cutoff**: "Dec 01, 2025 knowledge cutoff" ([model page](https://platform.openai.com/docs/models/gpt-5.5))
- **Relations**: base model of GPT-Rosalind-5.5 and of GPT-5.5 Pro ([GPT-5.5 card](https://deploymentsafety.openai.com/gpt-5-5), [Rosalind card](https://deploymentsafety.openai.com/gpt-rosalind-5-5))
- **Card**: [GPT-5.5 System Card](https://deploymentsafety.openai.com/gpt-5-5) (card "updated on April 24, 2026 to include additional information about safeguards for the deployment of GPT-5.5 and GPT-5.5 Pro in the API")
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.5)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: Card date and API release date differ by one day (Apr 23 vs Apr 24) — both retained.
- **Typed absences**: `not_reported`

## **GPT-5.5 Pro**

- Source report line: `88`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.5
- **Exact name**: **GPT-5.5 Pro**
- **Kind**: configuration
- **Native kind wording**: "Version of GPT-5.5 that produces smarter and more precise responses" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5.5-pro`, default snapshot `gpt-5.5-pro-2026-04-23` ([model page](https://platform.openai.com/docs/models/gpt-5.5-pro))
- **Announcement**: [Apr 23, 2026](https://deploymentsafety.openai.com/gpt-5-5)
- **Release / API availability**: [Apr 24, 2026](https://platform.openai.com/docs/changelog) — "released GPT-5.5 Pro for Responses API requests for tougher problems that benefit from more compute"
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses API only ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.5-pro))
- **Knowledge cutoff**: "Dec 01, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.5-pro))
- **Relations**: "the same underlying model using a setting that makes use of parallel test time compute" ([system card](https://deploymentsafety.openai.com/gpt-5-5))
- **Card**: [GPT-5.5 System Card](https://deploymentsafety.openai.com/gpt-5-5)
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.5-pro)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: Provider-stated shared-weights configuration with its own API ID — model vs configuration must be recorded from the card, not the catalog.
- **Typed absences**: `not_reported`

## **GPT-Rosalind-5.5**

- Source report line: `89`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-Rosalind
- **Exact name**: **GPT-Rosalind-5.5**
- **Kind**: model (derived)
- **Native kind wording**: "a new model in the GPT-Rosalind series, our frontier reasoning model built to support research" ([Deployment Safety Hub](https://deploymentsafety.openai.com/))
- **API ID / default snapshot**: not_reported (no API ID published)
- **Announcement**: [Jun 3, 2026](https://deploymentsafety.openai.com/) — "Jun 03, 2026 · GPT-Rosalind-5.5 System Card"
- **Release / API availability**: "We are deploying it in research preview to trusted organizations" ([card](https://deploymentsafety.openai.com/gpt-rosalind-5-5)); calendar date `not_reported`
- **GA**: not_applicable — "available only to approved customers" ([card](https://deploymentsafety.openai.com/gpt-rosalind-5-5))
- **Deprecated**: not_reported
- **Shutdown**: not_reported
- **Surfaces**: Trusted-access deployment structure; separate government pathway ([card](https://deploymentsafety.openai.com/gpt-rosalind-5-5))
- **Modalities**: not_reported
- **Knowledge cutoff**: not_reported
- **Relations**: "GPT-Rosalind-5.5 is incrementally trained from GPT-5.5, our flagship reasoning model"; "Unlike GPT-5.5, it is trained not to refuse sophisticated biology queries"; "inherits the model-level cyber safeguards of the GPT-5.5 base model" ([card](https://deploymentsafety.openai.com/gpt-rosalind-5-5))
- **Card**: [GPT-Rosalind-5.5 System Card](https://deploymentsafety.openai.com/gpt-rosalind-5-5)
- **Docs**: [Deployment Safety Hub](https://deploymentsafety.openai.com/)
- **Lifecycle 2026-09-05**: Research preview, approved customers only
- **Notes / typed gaps**: Never appears in the API catalog → an archive mention of "GPT-Rosalind" is card-surface evidence only.
- **Typed absences**: `not_applicable`, `not_reported`

## **GPT-5.4**

- Source report line: `90`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.4
- **Exact name**: **GPT-5.4**
- **Kind**: model
- **Native kind wording**: "A more affordable model for coding and professional work" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5.4`, default snapshot `gpt-5.4-2026-03-05` ([model page](https://platform.openai.com/docs/models/gpt-5.4))
- **Announcement**: not_reported separately
- **Release / API availability**: [Mar 5, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Chat Completions, Responses ([changelog](https://platform.openai.com/docs/changelog)); Amazon Bedrock from [Jun 1, 2026](https://platform.openai.com/docs/changelog); ChatGPT as "GPT-5.4 Thinking" from [Mar 5, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.4))
- **Knowledge cutoff**: "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.4))
- **Relations**: successor context: replacement target for retired GPT-5.1 ChatGPT models ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Card**: not_found (no GPT-5.4 card on the [hub index](https://deploymentsafety.openai.com/))
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.4)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: Image-encoder fix on [Mar 13, 2026](https://platform.openai.com/docs/changelog) — a silent behavior change under a fixed snapshot ID.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.4 Pro**

- Source report line: `91`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.4
- **Exact name**: **GPT-5.4 Pro**
- **Kind**: configuration
- **Native kind wording**: "Version of GPT-5.4 that produces smarter and more precise responses" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5.4-pro`, snapshot `gpt-5.4-pro-2026-03-05` ([model page](https://platform.openai.com/docs/models/gpt-5.4-pro))
- **Announcement**: not_reported
- **Release / API availability**: [Mar 5, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses API ([changelog](https://platform.openai.com/docs/changelog)); ChatGPT "GPT-5.4 Pro" ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.4-pro))
- **Knowledge cutoff**: "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.4-pro))
- **Relations**: Pro variant of GPT-5.4
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.4-pro)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.4 Mini**

- Source report line: `92`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.4
- **Exact name**: **GPT-5.4 Mini**
- **Kind**: model
- **Native kind wording**: "Our strongest mini model yet for coding, computer use, and subagents" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5.4-mini`, snapshot `gpt-5.4-mini-2026-03-17` ([model page](https://platform.openai.com/docs/models/gpt-5.4-mini))
- **Announcement**: not_reported
- **Release / API availability**: [Mar 17, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Chat Completions, Responses ([changelog](https://platform.openai.com/docs/changelog)); ChatGPT from [Mar 18, 2026](https://help.openai.com/en/articles/9624314-model-release-notes) — "available to Free and Go users via the 'Thinking' feature in the + menu … will not appear as a selectable model in the model picker"
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.4-mini))
- **Knowledge cutoff**: "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.4-mini))
- **Relations**: rate-limit fallback for GPT-5.4 Thinking ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.4-mini)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: A model that is deliberately *not* a product label — important for archive attribution.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.4 nano**

- Source report line: `93`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.4
- **Exact name**: **GPT-5.4 nano**
- **Kind**: model
- **Native kind wording**: "Our cheapest GPT-5.4-class model for simple high-volume tasks" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5.4-nano`, snapshot `gpt-5.4-nano-2026-03-17` ([model page](https://platform.openai.com/docs/models/gpt-5.4-nano))
- **Announcement**: not_reported
- **Release / API availability**: [Mar 17, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Chat Completions, Responses ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.4-nano))
- **Knowledge cutoff**: "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.4-nano))
- **Relations**: GPT-5.4 family
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.4-nano)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.2**

- Source report line: `94`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.2
- **Exact name**: **GPT-5.2**
- **Kind**: model
- **Native kind wording**: "Previous flagship model for professional work with configurable reasoning effort" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5.2`, snapshot `gpt-5.2-2025-12-11` ([model page](https://platform.openai.com/docs/models/gpt-5.2))
- **Announcement**: not_reported
- **Release / API availability**: [Dec 11, 2025](https://platform.openai.com/docs/changelog) — "Released GPT-5.2, the newest flagship model in the GPT-5 model family"
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses, Chat Completions ([changelog](https://platform.openai.com/docs/changelog)); ChatGPT until [Jun 12, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — "As of June 12, 2026, GPT-5.2 models are no longer available in ChatGPT"
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.2))
- **Knowledge cutoff**: "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.2))
- **Relations**: GPT-5 family; ChatGPT successor GPT-5.5 ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.2)
- **Lifecycle 2026-09-05**: Active in API, withdrawn from ChatGPT
- **Notes / typed gaps**: Product retirement without API retirement — must be modeled as a deployment-scoped event.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.2 Pro**

- Source report line: `95`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.2
- **Exact name**: **GPT-5.2 Pro**
- **Kind**: configuration
- **Native kind wording**: "Previous pro model for professional work" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5.2-pro`, snapshot `gpt-5.2-pro-2025-12-11` ([model page](https://platform.openai.com/docs/models/gpt-5.2-pro))
- **Announcement**: not_reported
- **Release / API availability**: [Dec 11, 2025](https://platform.openai.com/docs/changelog) (same release as GPT-5.2)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses API; ChatGPT "GPT-5.2 Pro" removed [Jun 12, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.2-pro))
- **Knowledge cutoff**: "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.2-pro))
- **Relations**: Pro variant of GPT-5.2
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.2-pro)
- **Lifecycle 2026-09-05**: Active in API
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.1**

- Source report line: `96`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5.1
- **Exact name**: **GPT-5.1**
- **Kind**: model
- **Native kind wording**: "The best model for coding and agentic tasks with configurable reasoning effort" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5.1`, snapshot `gpt-5.1-2025-11-13` ([model page](https://platform.openai.com/docs/models/gpt-5.1))
- **Announcement**: not_reported
- **Release / API availability**: [Nov 13, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses, Chat Completions; ChatGPT labels retired [Mar 11, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.1))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-5.1))
- **Relations**: "GPT-5.1 defaults to a new `none` reasoning setting" ([changelog](https://platform.openai.com/docs/changelog))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.1)
- **Lifecycle 2026-09-05**: Active in API
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5**

- Source report line: `97`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5
- **Exact name**: **GPT-5**
- **Kind**: model
- **Native kind wording**: "Previous intelligent reasoning model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5`, snapshot `gpt-5-2025-08-07` ([model page](https://platform.openai.com/docs/models/gpt-5))
- **Announcement**: not_reported
- **Release / API availability**: [Aug 7, 2025](https://platform.openai.com/docs/changelog) — "Released GPT-5 family of models in the API, including `gpt-5`, `gpt-5-mini`, and `gpt-5-nano`"
- **GA**: not_reported
- **Deprecated**: [Jun 11, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Dec 11, 2026](https://platform.openai.com/docs/deprecations) (scheduled)
- **Surfaces**: API; ChatGPT "GPT-5 Instant/Thinking" retired [Feb 13, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-5))
- **Relations**: replacement `gpt-5.6-sol` ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found on the current hub index (older cards not listed)
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5)
- **Lifecycle 2026-09-05**: Deprecated, shutdown scheduled
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5 Mini**

- Source report line: `98`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5
- **Exact name**: **GPT-5 Mini**
- **Kind**: model
- **Native kind wording**: "Strong intelligence for cost sensitive … workloads" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5-mini`, snapshot `gpt-5-mini-2025-08-07` ([model page](https://platform.openai.com/docs/models/gpt-5-mini))
- **Announcement**: not_reported
- **Release / API availability**: [Aug 7, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Jun 11, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Dec 11, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: API
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5-mini))
- **Knowledge cutoff**: "May 31, 2024" ([model page](https://platform.openai.com/docs/models/gpt-5-mini))
- **Relations**: replacement `gpt-5.6-terra`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5-mini)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: Cutoff differs from `gpt-5` in the same launch (May 31, 2024 vs Sep 30, 2024) — per-model, not per-family.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5 nano**

- Source report line: `99`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5
- **Exact name**: **GPT-5 nano**
- **Kind**: model
- **Native kind wording**: "Fastest, most cost-efficient version of GPT-5" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5-nano`, snapshot `gpt-5-nano-2025-08-07` ([model page](https://platform.openai.com/docs/models/gpt-5-nano))
- **Announcement**: not_reported
- **Release / API availability**: [Aug 7, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Jun 11, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Dec 11, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: API
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5-nano))
- **Knowledge cutoff**: "May 31, 2024" ([model page](https://platform.openai.com/docs/models/gpt-5-nano))
- **Relations**: replacement `gpt-5.6-luna`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5-nano)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5 Pro**

- Source report line: `100`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-5
- **Exact name**: **GPT-5 Pro**
- **Kind**: configuration
- **Native kind wording**: "Version of GPT-5 that produces smarter and more precise responses" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-5-pro`, snapshot `gpt-5-pro-2025-10-06` ([model page](https://platform.openai.com/docs/models/gpt-5-pro))
- **Announcement**: [Oct 6, 2025](https://platform.openai.com/docs/changelog) (DevDay)
- **Release / API availability**: [Oct 6, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Jun 11, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Dec 11, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Responses, Batch, Chat Completions ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5-pro))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-5-pro))
- **Relations**: replacement is `gpt-5.6-sol` with `reasoning.mode: pro` ([deprecations](https://platform.openai.com/docs/deprecations)) — a configuration replacing a model ID
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5-pro)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **o3**

- Source report line: `101`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: o-series
- **Exact name**: **o3**
- **Kind**: model
- **Native kind wording**: "Reasoning model for complex tasks, succeeded by GPT-5" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `o3`, snapshot `o3-2025-04-16` ([model page](https://platform.openai.com/docs/models/o3))
- **Announcement**: [Apr 16, 2025](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Apr 16, 2025](https://platform.openai.com/docs/changelog) — "Added two new o-series reasoning models, `o3` and `o4-mini`"
- **GA**: not_reported
- **Deprecated**: [Jun 11, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Dec 11, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: API; ChatGPT retirement announced [May 28, 2026](https://help.openai.com/en/articles/9624314-model-release-notes) — "retired from ChatGPT on August 26, 2026 following a 90-day sunset period"
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/o3))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/o3))
- **Relations**: "succeeded by GPT-5" ([models.md](https://platform.openai.com/docs/models.md))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/o3)
- **Lifecycle 2026-09-05**: Deprecated in API; retired from ChatGPT 2026-08-26
- **Notes / typed gaps**: Two different retirement dates for two deployments of one model.
- **Typed absences**: `not_found`, `not_reported`

## **o3-pro**

- Source report line: `102`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: o-series
- **Exact name**: **o3-pro**
- **Kind**: configuration
- **Native kind wording**: "Version of o3 with more compute for better responses" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `o3-pro`, snapshot `o3-pro-2025-06-10` ([model page](https://platform.openai.com/docs/models/o3-pro))
- **Announcement**: [Jun 10, 2025](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Jun 10, 2025](https://platform.openai.com/docs/changelog); ChatGPT "available in the model picker for Pro and Team users starting today, replacing o1-pro" ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **GA**: not_reported
- **Deprecated**: [Jun 11, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Dec 11, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Responses, Batch; ChatGPT Pro/Team
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/o3-pro))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/o3-pro))
- **Relations**: replaced o1-pro in ChatGPT ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/o3-pro)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **o3-mini**

- Source report line: `103`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: o-series
- **Exact name**: **o3-mini**
- **Kind**: model
- **Native kind wording**: "A small model alternative to o3" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `o3-mini`, snapshot `o3-mini-2025-01-31` ([model page](https://platform.openai.com/docs/models/o3-mini))
- **Announcement**: [Jan 31, 2025](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Jan 31, 2025](https://platform.openai.com/docs/changelog); ChatGPT same day ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Oct 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions; ChatGPT
- **Modalities**: text → text ([model page](https://platform.openai.com/docs/models/o3-mini))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/o3-mini))
- **Relations**: replacement `gpt-5.6-sol`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/o3-mini)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **o4-mini**

- Source report line: `104`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: o-series
- **Exact name**: **o4-mini**
- **Kind**: model
- **Native kind wording**: "Fast, cost-efficient reasoning model, succeeded by GPT-5 Mini" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `o4-mini`, snapshot `o4-mini-2025-04-16` ([model page](https://platform.openai.com/docs/models/o4-mini))
- **Announcement**: [Apr 16, 2025](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Apr 16, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Oct 23, 2026](https://platform.openai.com/docs/deprecations); ChatGPT retirement [Feb 13, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Surfaces**: API; ChatGPT until Feb 13, 2026
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/o4-mini))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/o4-mini))
- **Relations**: "succeeded by GPT-5 Mini" ([models.md](https://platform.openai.com/docs/models.md))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/o4-mini)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: A snapshot rollback occurred on [Jun 6, 2025](https://help.openai.com/en/articles/9624314-model-release-notes) — behavior changed under one label.
- **Typed absences**: `not_found`, `not_reported`

## **o4-mini-deep-research**

- Source report line: `105`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: o-series
- **Exact name**: **o4-mini-deep-research**
- **Kind**: model
- **Native kind wording**: "Faster, more affordable deep research model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `o4-mini-deep-research`, snapshot `o4-mini-deep-research-2025-06-26` ([model page](https://platform.openai.com/docs/models/o4-mini-deep-research))
- **Announcement**: [Jun 24, 2025](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Jun 24, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations) — already shut down
- **Surfaces**: Responses API
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/o4-mini-deep-research))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/o4-mini-deep-research))
- **Relations**: deep-research variant of o4-mini
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/o4-mini-deep-research)
- **Lifecycle 2026-09-05**: Retired (shut down 2026-07-23)
- **Notes / typed gaps**: Still listed in the catalog after shutdown — catalogs are not lifecycle sources.
- **Typed absences**: `not_found`, `not_reported`

## **o3-deep-research**

- Source report line: `106`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: o-series
- **Exact name**: **o3-deep-research**
- **Kind**: model
- **Native kind wording**: "Our most powerful deep research model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `o3-deep-research`, snapshot `o3-deep-research-2025-06-26` ([model page](https://platform.openai.com/docs/models/o3-deep-research))
- **Announcement**: [Jun 24, 2025](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Jun 24, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Responses API
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/o3-deep-research))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/o3-deep-research))
- **Relations**: cited as an example of a "deep research variant" subject to the 3-month notice class ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/o3-deep-research)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **o1**

- Source report line: `107`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: o-series
- **Exact name**: **o1**
- **Kind**: model
- **Native kind wording**: "Previous full o-series reasoning model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `o1`, snapshot `o1-2024-12-17` ([model page](https://platform.openai.com/docs/models/o1))
- **Announcement**: [Dec 17, 2024](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Dec 17, 2024](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Oct 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions, Responses
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/o1))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/o1))
- **Relations**: replacement `gpt-5.6-sol`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/o1)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **o1-pro**

- Source report line: `108`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: o-series
- **Exact name**: **o1-pro**
- **Kind**: configuration
- **Native kind wording**: "Version of o1 with more compute" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `o1-pro`, snapshot `o1-pro-2025-03-19` ([model page](https://platform.openai.com/docs/models/o1-pro))
- **Announcement**: [Mar 19, 2025](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Mar 19, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Oct 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Responses, Batch
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/o1-pro))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/o1-pro))
- **Relations**: replaced in ChatGPT by o3-pro on [Jun 10, 2025](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/o1-pro)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **o1-preview**

- Source report line: `109`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: o-series
- **Exact name**: **o1-preview**
- **Kind**: model
- **Native kind wording**: "Preview of our first o-series reasoning model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `o1-preview`, snapshot `o1-preview-2024-09-12` ([model page](https://platform.openai.com/docs/models/o1-preview))
- **Announcement**: [Sep 12, 2024](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Sep 12, 2024](https://platform.openai.com/docs/changelog) — "Released o1-preview and o1-mini"
- **GA**: not_applicable (preview)
- **Deprecated**: [Apr 28, 2025](https://platform.openai.com/docs/deprecations)
- **Shutdown**: see deprecations entry "2025-04-28: o1-preview and o1-mini" ([deprecations](https://platform.openai.com/docs/deprecations))
- **Surfaces**: Chat Completions
- **Modalities**: text → text ([model page](https://platform.openai.com/docs/models/o1-preview))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/o1-preview))
- **Relations**: first o-series model
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/o1-preview)
- **Lifecycle 2026-09-05**: Deprecated / retired
- **Notes / typed gaps**: —
- **Typed absences**: `not_applicable`, `not_found`

## **o1-mini**

- Source report line: `110`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: o-series
- **Exact name**: **o1-mini**
- **Kind**: model
- **Native kind wording**: "A small model alternative to o1" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `o1-mini`, snapshot `o1-mini-2024-09-12` ([model page](https://platform.openai.com/docs/models/o1-mini))
- **Announcement**: [Sep 12, 2024](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Sep 12, 2024](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 28, 2025](https://platform.openai.com/docs/deprecations)
- **Shutdown**: see "2025-04-28: o1-preview and o1-mini" ([deprecations](https://platform.openai.com/docs/deprecations))
- **Surfaces**: Chat Completions
- **Modalities**: text → text ([model page](https://platform.openai.com/docs/models/o1-mini))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/o1-mini))
- **Relations**: superseded by o3-mini in ChatGPT ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/o1-mini)
- **Lifecycle 2026-09-05**: Deprecated / retired
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4.5 Preview**

- Source report line: `111`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-4.5
- **Exact name**: **GPT-4.5 Preview**
- **Kind**: model
- **Native kind wording**: "Deprecated large model." ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-4.5-preview`, snapshot `gpt-4.5-preview-2025-02-27` ([model page](https://platform.openai.com/docs/models/gpt-4.5-preview))
- **Announcement**: [Feb 27, 2025](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Feb 27, 2025](https://platform.openai.com/docs/changelog) — "Released a research preview of GPT-4.5"
- **GA**: not_applicable (research preview)
- **Deprecated**: [Apr 14, 2025](https://platform.openai.com/docs/deprecations) ("2025-04-14: GPT-4.5-preview")
- **Shutdown**: API per [deprecations](https://platform.openai.com/docs/deprecations); ChatGPT retirement [Jun 26, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — "As of June 26, 2026, GPT-4.5 is no longer available in ChatGPT, including for custom GPTs"
- **Surfaces**: Chat Completions, Assistants, Batch ([changelog](https://platform.openai.com/docs/changelog)); ChatGPT until Jun 26, 2026
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-4.5-preview))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-4.5-preview))
- **Relations**: ChatGPT successor GPT-5.5 ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4.5-preview)
- **Lifecycle 2026-09-05**: Deprecated in API; retired from ChatGPT
- **Notes / typed gaps**: API deprecation (2025) preceded product retirement (2026) by 14 months.
- **Typed absences**: `not_applicable`, `not_found`

## **GPT-4.1**

- Source report line: `112`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-4.1
- **Exact name**: **GPT-4.1**
- **Kind**: model
- **Native kind wording**: "Smartest non-reasoning model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-4.1`, snapshot `gpt-4.1-2025-04-14` ([model page](https://platform.openai.com/docs/models/gpt-4.1))
- **Announcement**: [Apr 14, 2025](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Apr 14, 2025](https://platform.openai.com/docs/changelog); ChatGPT for paid users [May 14, 2025](https://help.openai.com/en/articles/9624314-model-release-notes)
- **GA**: not_reported
- **Deprecated**: not listed in current upcoming-deprecation tables → `not_reported`
- **Shutdown**: ChatGPT retirement [Feb 13, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Surfaces**: Responses, Chat Completions, fine-tuning ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-4.1))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/gpt-4.1))
- **Relations**: GPT-4.1 family
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4.1)
- **Lifecycle 2026-09-05**: Active in API; retired from ChatGPT
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4.1 Mini**

- Source report line: `113`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-4.1
- **Exact name**: **GPT-4.1 Mini**
- **Kind**: model
- **Native kind wording**: "Smaller, faster version of GPT-4.1" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-4.1-mini`, snapshot `gpt-4.1-mini-2025-04-14` ([model page](https://platform.openai.com/docs/models/gpt-4.1-mini))
- **Announcement**: [Apr 14, 2025](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Apr 14, 2025](https://platform.openai.com/docs/changelog); ChatGPT [May 14, 2025](https://help.openai.com/en/articles/9624314-model-release-notes) — "replaces GPT-4o mini in the model picker under 'more models'"
- **GA**: not_reported
- **Deprecated**: not_reported
- **Shutdown**: ChatGPT retirement [Feb 13, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Surfaces**: API; ChatGPT
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-4.1-mini))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/gpt-4.1-mini))
- **Relations**: replaced GPT-4o mini as ChatGPT fallback ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4.1-mini)
- **Lifecycle 2026-09-05**: Active in API
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4.1 nano**

- Source report line: `114`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-4.1
- **Exact name**: **GPT-4.1 nano**
- **Kind**: model
- **Native kind wording**: "Fastest, most cost-efficient version of GPT-4.1" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-4.1-nano`, snapshot `gpt-4.1-nano-2025-04-14` ([model page](https://platform.openai.com/docs/models/gpt-4.1-nano))
- **Announcement**: [Apr 14, 2025](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Apr 14, 2025](https://platform.openai.com/docs/changelog); fine-tuning [May 7, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Oct 23, 2026](https://platform.openai.com/docs/deprecations) (also `ft-gpt-4.1-nano-2025-04-14`)
- **Surfaces**: API
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-4.1-nano))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/gpt-4.1-nano))
- **Relations**: replacement `gpt-5.6-luna`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4.1-nano)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: Fine-tuned derivatives get their own shutdown rows ([deprecations](https://platform.openai.com/docs/deprecations)).
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4o**

- Source report line: `115`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-4o
- **Exact name**: **GPT-4o**
- **Kind**: model
- **Native kind wording**: "Fast, intelligent, flexible GPT model" ([model page](https://platform.openai.com/docs/models/gpt-4o))
- **API ID / default snapshot**: `gpt-4o`; default snapshot `gpt-4o-2024-08-06`; snapshots `gpt-4o-2024-11-20`, `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13` ([model page](https://platform.openai.com/docs/models/gpt-4o))
- **Announcement**: [May 13, 2024](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [May 13, 2024](https://platform.openai.com/docs/changelog) — "Released GPT-4o in the API"; later snapshots [Aug 6, 2024](https://platform.openai.com/docs/changelog) and [Nov 20, 2024](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: `gpt-4o-2024-05-13` deprecated [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: `gpt-4o-2024-05-13` shutdown [Oct 23, 2026](https://platform.openai.com/docs/deprecations); ChatGPT retirement of GPT-4o [Feb 13, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Surfaces**: API; ChatGPT until Feb 13, 2026; Advanced Voice upgrade [Jun 7, 2025](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-4o))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-4o))
- **Relations**: ChatGPT behavior revisions [Mar 27, 2025](https://help.openai.com/en/articles/9624314-model-release-notes), [Apr 25, 2025](https://help.openai.com/en/articles/9624314-model-release-notes), reverted [Apr 29, 2025](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4o)
- **Lifecycle 2026-09-05**: Active (one snapshot deprecated)
- **Notes / typed gaps**: Three snapshots under one alias; one deprecated while the alias remains active — alias/checkpoint separation is mandatory here.
- **Typed absences**: `not_found`, `not_reported`

## **ChatGPT-4o**

- Source report line: `116`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-4o
- **Exact name**: **ChatGPT-4o**
- **Kind**: endpoint_alias
- **Native kind wording**: "GPT-4o model used in ChatGPT" ([model page](https://platform.openai.com/docs/models/chatgpt-4o-latest))
- **API ID / default snapshot**: `chatgpt-4o-latest` (default snapshot = itself, i.e. a mutable pointer) ([model page](https://platform.openai.com/docs/models/chatgpt-4o-latest))
- **Announcement**: [Aug 15, 2024](https://platform.openai.com/docs/changelog) — "Released dynamic model for `chatgpt-4o-latest` — this model will point to the latest GPT-4o model used by ChatGPT"
- **Release / API availability**: [Aug 15, 2024](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Nov 18, 2025](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Feb 17, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/chatgpt-4o-latest))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/chatgpt-4o-latest))
- **Relations**: replacement `gpt-5.1-chat-latest` ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/chatgpt-4o-latest)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: Validity interval of the alias: 2024-08-15 → 2026-02-17.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4o Mini**

- Source report line: `117`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-4o
- **Exact name**: **GPT-4o Mini**
- **Kind**: model
- **Native kind wording**: "Fast, affordable small model for focused tasks" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-4o-mini`, snapshot `gpt-4o-mini-2024-07-18` ([model page](https://platform.openai.com/docs/models/gpt-4o-mini))
- **Announcement**: [Jul 18, 2024](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Jul 18, 2024](https://platform.openai.com/docs/changelog); fine-tuning [Jul 23, 2024](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: not_reported
- **Shutdown**: replaced in ChatGPT by GPT-4.1 mini [May 14, 2025](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Surfaces**: API; ChatGPT
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-4o-mini))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-4o-mini))
- **Relations**: —
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4o-mini)
- **Lifecycle 2026-09-05**: Active in API
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4**

- Source report line: `118`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-4
- **Exact name**: **GPT-4**
- **Kind**: model
- **Native kind wording**: "An older high-intelligence GPT model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-4`, default snapshot `gpt-4-0613`; snapshots `gpt-4-0613`, `gpt-4-0314` ([model page](https://platform.openai.com/docs/models/gpt-4))
- **Announcement**: not_reported (predates the changelog's earliest entry, [Oct 6, 2023](https://platform.openai.com/docs/changelog))
- **Release / API availability**: not_reported
- **GA**: not_reported
- **Deprecated**: `gpt-4-0314` deprecated [Sep 26, 2025](https://platform.openai.com/docs/deprecations); `gpt-4-0613` family deprecated [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: `gpt-4-0314` shut down [Mar 26, 2026](https://platform.openai.com/docs/deprecations); `gpt-4`/`gpt-4-0613`/completions variants [Oct 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions + `-completions` endpoint variants ([deprecations](https://platform.openai.com/docs/deprecations))
- **Modalities**: text → text ([model page](https://platform.openai.com/docs/models/gpt-4))
- **Knowledge cutoff**: "Dec 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-4)) — note: later than some GPT-4o cutoffs
- **Relations**: replacement `gpt-5.6-sol`; also `ft-gpt-4` shutdown [Oct 23, 2026](https://platform.openai.com/docs/deprecations)
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: No official release date is recoverable from the fetched surfaces → `not_found`, flagged in §8.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4 Turbo**

- Source report line: `119`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-4
- **Exact name**: **GPT-4 Turbo**
- **Kind**: model
- **Native kind wording**: "An older high-intelligence GPT model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-4-turbo`, snapshot `gpt-4-turbo-2024-04-09` ([model page](https://platform.openai.com/docs/models/gpt-4-turbo))
- **Announcement**: [Nov 6, 2023](https://platform.openai.com/docs/changelog) (GPT-4 Turbo Preview)
- **Release / API availability**: GA with vision [Apr 9, 2024](https://platform.openai.com/docs/changelog) — "Released GPT-4 Turbo with Vision in general availability in the API"
- **GA**: [Apr 9, 2024](https://platform.openai.com/docs/changelog)
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Oct 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions, completions variant
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-4-turbo))
- **Knowledge cutoff**: "Dec 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-4-turbo))
- **Relations**: replacement `gpt-5.6-sol`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4-turbo)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: Distinct announcement (preview) and GA dates — both preserved.
- **Typed absences**: `not_found`

## **GPT-4 Turbo Preview**

- Source report line: `120`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-4
- **Exact name**: **GPT-4 Turbo Preview**
- **Kind**: model
- **Native kind wording**: "An older fast GPT model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-4-turbo-preview`, default snapshot `gpt-4-0125-preview`; also lists `gpt-4-1106-vision-preview` ([model page](https://platform.openai.com/docs/models/gpt-4-turbo-preview))
- **Announcement**: [Nov 6, 2023](https://platform.openai.com/docs/changelog); updated preview [Jan 25, 2024](https://platform.openai.com/docs/changelog)
- **Release / API availability**: [Nov 6, 2023](https://platform.openai.com/docs/changelog)
- **GA**: not_applicable (preview)
- **Deprecated**: `gpt-4-0125-preview` deprecated [Sep 26, 2025](https://platform.openai.com/docs/deprecations); `gpt-4-1106-preview` also listed [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: `gpt-4-0125-preview` shut down [Mar 26, 2026](https://platform.openai.com/docs/deprecations); `gpt-4-1106-preview` [Oct 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions
- **Modalities**: text → text ([model page](https://platform.openai.com/docs/models/gpt-4-turbo-preview))
- **Knowledge cutoff**: "Dec 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-4-turbo-preview))
- **Relations**: `gpt-4-turbo-preview` and `gpt-4-turbo-preview-completions` "point to this snapshot" ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4-turbo-preview)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: `gpt-4-1106-preview` appears in **two** deprecation announcements with different shutdown dates — contradiction, §7.
- **Typed absences**: `not_applicable`, `not_found`

## **GPT-3.5 Turbo**

- Source report line: `121`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT-3.5
- **Exact name**: **GPT-3.5 Turbo**
- **Kind**: model
- **Native kind wording**: "Legacy GPT model for cheaper chat and non-chat tasks" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `gpt-3.5-turbo`, default snapshot `gpt-3.5-turbo-0125`; snapshots `gpt-3.5-turbo-0125`, `gpt-3.5-turbo-1106`, `gpt-3.5-turbo-instruct` ([model page](https://platform.openai.com/docs/models/gpt-3.5-turbo))
- **Announcement**: `gpt-3.5-turbo-1106` [Nov 6, 2023](https://platform.openai.com/docs/changelog); `gpt-3.5-turbo-0125` [Feb 1, 2024](https://platform.openai.com/docs/changelog)
- **Release / API availability**: as above
- **GA**: not_reported
- **Deprecated**: `gpt-3.5-turbo-0125` [Apr 22, 2026](https://platform.openai.com/docs/deprecations); `gpt-3.5-turbo-1106`/`-instruct` [Sep 26, 2025](https://platform.openai.com/docs/deprecations)
- **Shutdown**: `gpt-3.5-turbo-0125` [Oct 23, 2026](https://platform.openai.com/docs/deprecations); `gpt-3.5-turbo-instruct`, `gpt-3.5-turbo-1106` [Sep 28, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions, completions
- **Modalities**: text → text ([model page](https://platform.openai.com/docs/models/gpt-3.5-turbo))
- **Knowledge cutoff**: "Sep 01, 2021" ([model page](https://platform.openai.com/docs/models/gpt-3.5-turbo))
- **Relations**: `ft-gpt-3.5-turbo` shutdown [Oct 23, 2026](https://platform.openai.com/docs/deprecations)
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-3.5-turbo)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: Different snapshots of one family have different shutdown dates — checkpoint-level lifecycle required.
- **Typed absences**: `not_found`, `not_reported`

## **babbage-002**

- Source report line: `122`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT base
- **Exact name**: **babbage-002**
- **Kind**: model
- **Native kind wording**: "Replacement for the GPT-3 ada and babbage base models" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `babbage-002` ([model page](https://platform.openai.com/docs/models/babbage-002))
- **Announcement**: not_reported
- **Release / API availability**: not_reported
- **GA**: not_reported
- **Deprecated**: [Sep 26, 2025](https://platform.openai.com/docs/deprecations); fine-tuning training deprecated earlier, "2024-08-29: Fine-tuning training on babbage-002 and davinci-002 models" ([deprecations](https://platform.openai.com/docs/deprecations))
- **Shutdown**: [Sep 28, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Completions, fine-tuning
- **Modalities**: text → text ([model page](https://platform.openai.com/docs/models/babbage-002))
- **Knowledge cutoff**: "Sep 01, 2021" ([model page](https://platform.openai.com/docs/models/babbage-002))
- **Relations**: `ft-babbage-002` shutdown [Oct 23, 2026](https://platform.openai.com/docs/deprecations)
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/babbage-002)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: Oldest documented OpenAI knowledge cutoff (2021-09-01).
- **Typed absences**: `not_found`, `not_reported`

## **davinci-002**

- Source report line: `123`
- Research section: 2b-i. Frontier and reasoning models (text)
- **Family**: GPT base
- **Exact name**: **davinci-002**
- **Kind**: model
- **Native kind wording**: "Replacement for the GPT-3 curie and davinci base models" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / default snapshot**: `davinci-002` ([model page](https://platform.openai.com/docs/models/davinci-002))
- **Announcement**: not_reported
- **Release / API availability**: not_reported
- **GA**: not_reported
- **Deprecated**: [Sep 26, 2025](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Sep 28, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Completions, fine-tuning
- **Modalities**: text → text ([model page](https://platform.openai.com/docs/models/davinci-002))
- **Knowledge cutoff**: "Sep 01, 2021" ([model page](https://platform.openai.com/docs/models/davinci-002))
- **Relations**: `ft-davinci-002` shutdown [Oct 23, 2026](https://platform.openai.com/docs/deprecations)
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/davinci-002)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5-Codex**

- Source report line: `173`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: Codex
- **Exact name**: **GPT-5-Codex**
- **Kind**: configuration
- **Native kind wording**: "A version of GPT-5 optimized for agentic coding in Codex" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-5-codex` ([model page](https://platform.openai.com/docs/models/gpt-5-codex))
- **Announcement**: [Sep 15, 2025](https://help.openai.com/en/articles/9624314-model-release-notes) — "We're adding GPT-5-codex, a GPT-5 variant optimized for agentic coding in Codex"
- **Release**: Codex surfaces [Sep 15, 2025](https://help.openai.com/en/articles/9624314-model-release-notes); Responses API [Sep 23, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations) — already shut down
- **Surfaces**: Codex, then Responses API ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5-codex))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-5-codex))
- **Relations**: GPT-5 variant ([help center](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5-codex)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: Two distinct availability dates for two surfaces of one model ID.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.1-Codex**

- Source report line: `174`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: Codex
- **Exact name**: **GPT-5.1-Codex**
- **Kind**: configuration
- **Native kind wording**: "A version of GPT-5.1 optimized for agentic coding in Codex." ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-5.1-codex` ([model page](https://platform.openai.com/docs/models/gpt-5.1-codex))
- **Announcement**: [Nov 13, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Nov 13, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Responses API, Codex
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.1-codex))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-5.1-codex))
- **Relations**: GPT-5.1 variant
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.1-codex)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: "Codex variants such as `gpt-5.3-codex`" are named in the 3-month notice class ([deprecations](https://platform.openai.com/docs/deprecations)).
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.1-Codex Mini**

- Source report line: `175`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: Codex
- **Exact name**: **GPT-5.1-Codex Mini**
- **Kind**: configuration
- **Native kind wording**: "Smaller, more cost-effective, less-capable version of GPT-5.1-Codex" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-5.1-codex-mini` ([model page](https://platform.openai.com/docs/models/gpt-5.1-codex-mini))
- **Announcement**: [Nov 13, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Nov 13, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Responses API
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.1-codex-mini))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-5.1-codex-mini))
- **Relations**: mini variant of GPT-5.1-Codex
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.1-codex-mini)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.1-Codex-Max**

- Source report line: `176`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: Codex
- **Exact name**: **GPT-5.1-Codex-Max**
- **Kind**: configuration
- **Native kind wording**: "A version of GPT-5.1-codex optimized for long running tasks." ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-5.1-codex-max` ([model page](https://platform.openai.com/docs/models/gpt-5.1-codex-max))
- **Announcement**: [Nov 19, 2025](https://help.openai.com/en/articles/9624314-model-release-notes) — "Introducing GPT-5-Codex-Max … GPT-5.1-Codex-Max is our new frontier agentic coding model built for long-running, project-scale work"
- **Release**: Responses API [Dec 4, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Responses API, Codex
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.1-codex-max))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-5.1-codex-max))
- **Relations**: "a version of GPT-5.1-codex"
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.1-codex-max)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: The help-center headline says "GPT-5-Codex-Max" while the body and the API say "GPT-5.1-Codex-Max" — naming contradiction, §7.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.2-Codex**

- Source report line: `177`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: Codex
- **Exact name**: **GPT-5.2-Codex**
- **Kind**: configuration
- **Native kind wording**: "Our most intelligent coding model optimized for long-horizon, agentic coding tasks." ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-5.2-codex` ([model page](https://platform.openai.com/docs/models/gpt-5.2-codex))
- **Announcement**: [Jan 14, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [Jan 14, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Responses API
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.2-codex))
- **Knowledge cutoff**: "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.2-codex))
- **Relations**: GPT-5.2 variant
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.2-codex)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.3-Codex**

- Source report line: `178`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: Codex
- **Exact name**: **GPT-5.3-Codex**
- **Kind**: configuration
- **Native kind wording**: "The most capable agentic coding model to date." ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-5.3-codex` ([model page](https://platform.openai.com/docs/models/gpt-5.3-codex))
- **Announcement**: [Feb 5, 2026](https://help.openai.com/en/articles/9624314-model-release-notes) — "Today, we launched GPT-5.3-Codex, our most capable agentic coding model yet"
- **Release**: Responses API [Feb 24, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses API, Codex
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.3-codex))
- **Knowledge cutoff**: "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.3-codex))
- **Relations**: replaced GPT-5.1-Codex in Codex ([help center](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.3-codex)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: Product launch (Feb 5) precedes API availability (Feb 24) by 19 days — both preserved.
- **Typed absences**: `not_found`, `not_reported`

## **codex-mini-latest**

- Source report line: `179`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: Codex
- **Exact name**: **codex-mini-latest**
- **Kind**: model
- **Native kind wording**: "Fast reasoning model optimized for the Codex CLI" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `codex-mini-latest` ([model page](https://platform.openai.com/docs/models/codex-mini-latest))
- **Announcement**: [May 15, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [May 15, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Nov 17, 2025](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Feb 12, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Responses, Chat Completions, Codex CLI
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/codex-mini-latest))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/codex-mini-latest))
- **Relations**: replacement `gpt-5-codex-mini` ([deprecations](https://platform.openai.com/docs/deprecations)) — **a replacement ID that does not appear in the current catalog** (`not_found`)
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/codex-mini-latest)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: Its retirement also removed "our legacy local shell tool" ([deprecations](https://platform.openai.com/docs/deprecations)).
- **Typed absences**: `not_found`, `not_reported`

## **Chat Latest**

- Source report line: `180`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: chat pointers
- **Exact name**: **Chat Latest**
- **Kind**: endpoint_alias
- **Native kind wording**: "Latest Instant model used in ChatGPT" ([models.md](https://platform.openai.com/docs/models.md)); "points to the latest model available in ChatGPT for Plus and Pro users … The underlying model snapshot will be regularly updated" ([changelog](https://platform.openai.com/docs/changelog))
- **API ID / snapshot**: `chat-latest` ([model page](https://platform.openai.com/docs/models/chat-latest))
- **Announcement**: [May 5, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [May 5, 2026](https://platform.openai.com/docs/changelog); re-released/announced [May 28, 2026](https://platform.openai.com/docs/changelog); repointed [Jun 24, 2026](https://platform.openai.com/docs/changelog) and [Aug 6, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_applicable
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Chat Completions / Responses
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/chat-latest))
- **Knowledge cutoff**: "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/chat-latest)) — cutoff of whatever snapshot it currently points to
- **Relations**: tracked GPT-5.5 Instant, then the ChatGPT Plus/Pro model ([changelog](https://platform.openai.com/docs/changelog))
- **Card**: not_applicable
- **Docs**: [Model page](https://platform.openai.com/docs/models/chat-latest)
- **Lifecycle 2026-09-05**: Active mutable alias
- **Notes / typed gaps**: Deliberately unstable pointer: repointings on 2026-05-05, 2026-05-28, 2026-06-24, 2026-08-06 are the alias's valid-time boundaries.
- **Typed absences**: `not_applicable`

## **GPT-5 Chat**

- Source report line: `181`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: chat pointers
- **Exact name**: **GPT-5 Chat**
- **Kind**: endpoint_alias
- **Native kind wording**: "GPT-5 model used in ChatGPT" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-5-chat-latest` ([model page](https://platform.openai.com/docs/models/gpt-5-chat-latest))
- **Announcement**: not_reported
- **Release**: with the GPT-5 family, [Aug 7, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5-chat-latest))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-5-chat-latest))
- **Relations**: replacement `gpt-5.6-sol`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5-chat-latest)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.1 Chat**

- Source report line: `182`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: chat pointers
- **Exact name**: **GPT-5.1 Chat**
- **Kind**: endpoint_alias
- **Native kind wording**: "GPT-5.1 model used in ChatGPT" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-5.1-chat-latest` ([model page](https://platform.openai.com/docs/models/gpt-5.1-chat-latest))
- **Announcement**: [Nov 13, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Nov 13, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.1-chat-latest))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-5.1-chat-latest))
- **Relations**: named as the archetype "chat variant" in the 3-month notice class ([deprecations](https://platform.openai.com/docs/deprecations)); was the replacement for `chatgpt-4o-latest`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.1-chat-latest)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: An alias that was itself the migration target of another retired alias.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.2 Chat**

- Source report line: `183`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: chat pointers
- **Exact name**: **GPT-5.2 Chat**
- **Kind**: endpoint_alias
- **Native kind wording**: "GPT-5.2 model used in ChatGPT" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-5.2-chat-latest` ([model page](https://platform.openai.com/docs/models/gpt-5.2-chat-latest))
- **Announcement**: [Dec 11, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Dec 11, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [May 8, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Aug 10, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions, Responses
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.2-chat-latest))
- **Knowledge cutoff**: "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.2-chat-latest))
- **Relations**: replacement `gpt-5.6-sol`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.2-chat-latest)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.3 Chat**

- Source report line: `184`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: chat pointers
- **Exact name**: **GPT-5.3 Chat**
- **Kind**: endpoint_alias
- **Native kind wording**: "GPT-5.3 Instant model used in ChatGPT" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-5.3-chat-latest` ([model page](https://platform.openai.com/docs/models/gpt-5.3-chat-latest))
- **Announcement**: [Mar 3, 2026](https://platform.openai.com/docs/changelog) — "points to the GPT-5.3 Instant snapshot currently used in ChatGPT"
- **Release**: [Mar 3, 2026](https://platform.openai.com/docs/changelog); repointed [Mar 16, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [May 8, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Aug 10, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions, Responses
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-5.3-chat-latest))
- **Knowledge cutoff**: "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.3-chat-latest))
- **Relations**: tracks the ChatGPT "GPT-5.3 Instant" product label
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-5.3-chat-latest)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: Alias lived 2026-03-03 → 2026-08-10 and was repointed once inside that interval.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Live-1** and **GPT-Live-1 mini**

- Source report line: `185`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: ChatGPT labels
- **Exact name**: **GPT-Live-1** and **GPT-Live-1 mini**
- **Kind**: model
- **Native kind wording**: "a new generation of voice models" / "the models that power Advanced Voice Mode (AVM)" ([system card](https://deploymentsafety.openai.com/gpt-live))
- **API ID / snapshot**: not_reported (no API IDs published; the API's realtime line is a separate `gpt-realtime-*` series)
- **Announcement**: [Jul 8, 2026](https://deploymentsafety.openai.com/) — "Jul 08, 2026 · GPT-Live System Card"
- **Release**: [Jul 8, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — "ChatGPT Voice is now powered by GPT-Live-1 for paid users"; mini for Free users
- **GA**: "rolling out across consumer plans, including Free, on chatgpt.com and the ChatGPT iOS and Android apps in supported regions. It is not available in ChatGPT Business, Enterprise, or Edu workspaces at launch" ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: ChatGPT Voice only ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Modalities**: audio ↔ audio with delegation to text models ([system card](https://deploymentsafety.openai.com/gpt-live))
- **Knowledge cutoff**: not_reported
- **Relations**: "They can also delegate more complex work to our other models, and when they do, the resulting work will reflect the safety training of the underlying model that is doing that work" ([system card](https://deploymentsafety.openai.com/gpt-live))
- **Card**: [GPT-Live System Card](https://deploymentsafety.openai.com/gpt-live) (card carries a correction dated "August 4, 2026")
- **Docs**: [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **Lifecycle 2026-09-05**: Active in ChatGPT
- **Notes / typed gaps**: Product-only models with no API identifier; the card documents a *safety-evaluation configuration mismatch* later corrected — evidence that card numbers can be revised after release.
- **Typed absences**: `not_reported`

## **GPT-5.5 Instant**

- Source report line: `186`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: ChatGPT labels
- **Exact name**: **GPT-5.5 Instant**
- **Kind**: product_model_label
- **Native kind wording**: "our latest Instant model … deployed at a low reasoning effort" ([system card](https://deploymentsafety.openai.com/gpt-5-5-instant))
- **API ID / snapshot**: `gpt-5.5-instant` identifier appears in the card ([system card](https://deploymentsafety.openai.com/gpt-5-5-instant)); not present in the API catalog → API exposure `not_found`
- **Announcement**: [May 5, 2026](https://deploymentsafety.openai.com/) — "May 05, 2026 · GPT-5.5 Instant System Card"
- **Release**: ChatGPT; updated [May 28, 2026](https://help.openai.com/en/articles/9624314-model-release-notes) and [Jun 24, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — "our most-used model in ChatGPT"
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: replaced by the August GPT-5.6 models — "These models will replace GPT-5.5 Instant" ([August update card](https://deploymentsafety.openai.com/gpt-5-6-august-update))
- **Surfaces**: ChatGPT; the May 28 update also covered the API ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Modalities**: text, image → text
- **Knowledge cutoff**: not_reported
- **Relations**: "the main model to baseline against is GPT-5.3 Instant" ([system card](https://deploymentsafety.openai.com/gpt-5-5-instant))
- **Card**: [GPT-5.5 Instant System Card](https://deploymentsafety.openai.com/gpt-5-5-instant)
- **Docs**: [Model release notes](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Lifecycle 2026-09-05**: Superseded in ChatGPT
- **Notes / typed gaps**: The card explicitly states "there is not a model named GPT-5.4 Instant" — a documented naming gap in the Instant series, useful for refuting invented labels.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-5.5 Instant Mini**

- Source report line: `187`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: ChatGPT labels
- **Exact name**: **GPT-5.5 Instant Mini**
- **Kind**: product_model_label
- **Native kind wording**: fallback model — "Because it serves as a fallback, it won't appear in the model picker" ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **API ID / snapshot**: not_reported
- **Announcement**: [Jul 6, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **Release**: [Jul 6, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — "It replaces GPT-5.3 Instant Mini as the fallback model users reach after hitting their GPT-5.5 Instant or Auto rate limits"
- **GA**: not_applicable
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: ChatGPT only — "This update does not affect the API or Codex" ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Modalities**: text → text
- **Knowledge cutoff**: not_reported
- **Relations**: replaced GPT-5.3 Instant Mini ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Card**: not_found
- **Docs**: [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **Lifecycle 2026-09-05**: Active in ChatGPT
- **Notes / typed gaps**: —
- **Typed absences**: `not_applicable`, `not_found`, `not_reported`

## **GPT-5.3 Instant**, **GPT-5.3 Instant Mini**

- Source report line: `188`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: ChatGPT labels
- **Exact name**: **GPT-5.3 Instant**, **GPT-5.3 Instant Mini**
- **Kind**: product_model_label
- **Native kind wording**: ChatGPT Instant tier labels ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **API ID / snapshot**: `gpt-5.3-instant` appears in the GPT-5.5 Instant card's comparison set ([card](https://deploymentsafety.openai.com/gpt-5-5-instant))
- **Announcement**: [Mar 3, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Release**: [Mar 3, 2026](https://help.openai.com/en/articles/9624314-model-release-notes); updated [Mar 16, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **GA**: not_applicable
- **Deprecated**: N/A
- **Shutdown**: Instant Mini replaced [Jul 6, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **Surfaces**: ChatGPT
- **Modalities**: text, image → text
- **Knowledge cutoff**: not_reported
- **Relations**: exposed to the API through the `gpt-5.3-chat-latest` alias ([changelog](https://platform.openai.com/docs/changelog))
- **Card**: not_found
- **Docs**: [Model release notes](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Lifecycle 2026-09-05**: Superseded
- **Notes / typed gaps**: Product label ↔ alias ↔ snapshot triad; there is no `gpt-5.3` base model page in the catalog (`not_found`).
- **Typed absences**: `not_applicable`, `not_found`, `not_reported`

## **GPT-5.4 Thinking**, **GPT-5.4 Pro**

- Source report line: `189`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: ChatGPT labels
- **Exact name**: **GPT-5.4 Thinking**, **GPT-5.4 Pro**
- **Kind**: product_model_label
- **Native kind wording**: ChatGPT reasoning-tier labels ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **API ID / snapshot**: back onto `gpt-5.4` / `gpt-5.4-pro` ([changelog](https://platform.openai.com/docs/changelog))
- **Announcement**: [Mar 5, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Release**: [Mar 5, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **GA**: not_applicable
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: ChatGPT paid tiers
- **Modalities**: text, image → text
- **Knowledge cutoff**: as `gpt-5.4` — "Aug 31, 2025" ([model page](https://platform.openai.com/docs/models/gpt-5.4))
- **Relations**: migration destination for retired GPT-5.1 conversations ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Card**: not_found
- **Docs**: [Model release notes](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: —
- **Typed absences**: `not_applicable`, `not_found`

## **GPT-5.2 Instant / Thinking / Pro**

- Source report line: `190`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: ChatGPT labels
- **Exact name**: **GPT-5.2 Instant / Thinking / Pro**
- **Kind**: product_model_label
- **Native kind wording**: ChatGPT labels ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **API ID / snapshot**: `gpt-5.2`, `gpt-5.2-pro`, `gpt-5.2-chat-latest`
- **Announcement**: [Dec 11, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Dec 11, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_applicable
- **Deprecated**: N/A
- **Shutdown**: [Jun 12, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) — "no longer available in ChatGPT"
- **Surfaces**: ChatGPT until 2026-06-12
- **Modalities**: text, image → text
- **Knowledge cutoff**: as underlying models
- **Relations**: "Existing conversations that used GPT-5.2 will automatically continue on the corresponding GPT-5.5 model" ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Card**: not_found
- **Docs**: [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **Lifecycle 2026-09-05**: Retired from ChatGPT
- **Notes / typed gaps**: Thinking-time setting changed and was restored on [Feb 4, 2026](https://help.openai.com/en/articles/9624314-model-release-notes) — a product-configuration event with no model change.
- **Typed absences**: `not_applicable`, `not_found`

## **GPT-5.1 Instant / Thinking / Pro**

- Source report line: `191`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: ChatGPT labels
- **Exact name**: **GPT-5.1 Instant / Thinking / Pro**
- **Kind**: product_model_label
- **Native kind wording**: ChatGPT labels ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **API ID / snapshot**: `gpt-5.1`, `gpt-5.1-chat-latest` (Pro label ID `not_found`)
- **Announcement**: [Nov 13, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Nov 13, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_applicable
- **Deprecated**: N/A
- **Shutdown**: [Mar 11, 2026](https://help.openai.com/en/articles/9624314-model-release-notes) — "As of March 11, 2026, GPT-5.1 models are no longer available in ChatGPT"
- **Surfaces**: ChatGPT until 2026-03-11
- **Modalities**: text, image → text
- **Knowledge cutoff**: as underlying models
- **Relations**: conversations migrated to "GPT-5.3 Instant, GPT-5.4 Thinking, or GPT-5.4 Pro" ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Card**: not_found
- **Docs**: [Model release notes](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Lifecycle 2026-09-05**: Retired from ChatGPT
- **Notes / typed gaps**: A "GPT-5.1 Pro" product label exists with no corresponding catalog entry (`not_found`).
- **Typed absences**: `not_applicable`, `not_found`

## **GPT-5 Instant / GPT-5 Thinking / GPT-5 Auto / GPT-5 Thinking mini**

- Source report line: `192`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: ChatGPT labels
- **Exact name**: **GPT-5 Instant / GPT-5 Thinking / GPT-5 Auto / GPT-5 Thinking mini**
- **Kind**: product_model_label
- **Native kind wording**: ChatGPT labels and router ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **API ID / snapshot**: `gpt-5` family; Auto and Thinking-mini IDs `not_found`
- **Announcement**: [Aug 7, 2025](https://platform.openai.com/docs/changelog) (API family)
- **Release**: ChatGPT behavior update [Oct 3, 2025](https://help.openai.com/en/articles/9624314-model-release-notes) — "We're updating GPT-5 Instant to better recognize and support people in moments of distress"
- **GA**: not_applicable
- **Deprecated**: N/A
- **Shutdown**: GPT-5 Instant/Thinking retired from ChatGPT [Feb 13, 2026](https://help.openai.com/en/articles/9624314-model-release-notes); GPT-5 Thinking mini "will be retired as a selectable option in 30 days" from [Mar 18, 2026](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Surfaces**: ChatGPT
- **Modalities**: text, image → text
- **Knowledge cutoff**: as `gpt-5`
- **Relations**: Auto routing is a product-level router, not a model ([model release notes](https://help.openai.com/en/articles/9624314-model-release-notes))
- **Card**: not_found
- **Docs**: [Model release notes](https://help.openai.com/en/articles/9624314-model-release-notes)
- **Lifecycle 2026-09-05**: Retired from ChatGPT
- **Notes / typed gaps**: "30 days" wording gives a derived, not stated, retirement date → recorded as `not_reported` exact date.
- **Typed absences**: `not_applicable`, `not_found`, `not_reported`

## **Model-picker options "Instant", "Medium", "High", "Extra High", "Pro Standard"**

- Source report line: `193`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: ChatGPT labels
- **Exact name**: **Model-picker options "Instant", "Medium", "High", "Extra High", "Pro Standard"**
- **Kind**: product_model_label
- **Native kind wording**: "The model picker now has the following simplified options" ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **API ID / snapshot**: not_applicable — effort tiers, not model IDs
- **Announcement**: [Jun 10, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **Release**: [Jun 10, 2026](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **GA**: not_applicable
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: ChatGPT; "Extra High *[Pro plans only]*" ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **Modalities**: not_applicable
- **Knowledge cutoff**: not_applicable
- **Relations**: replaced per-model naming in the picker
- **Card**: not_applicable
- **Docs**: [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: After 2026-06-10 a ChatGPT transcript may name an *effort tier* rather than a model — critical for archive attribution.
- **Typed absences**: `not_applicable`

## **GPT-4o Search Preview** / **GPT-4o Mini Search Preview**

- Source report line: `194`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: search variants
- **Exact name**: **GPT-4o Search Preview** / **GPT-4o Mini Search Preview**
- **Kind**: model
- **Native kind wording**: "GPT model for web search in Chat Completions" / "Fast, affordable small model for web search" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-4o-search-preview` (snapshot `gpt-4o-search-preview-2025-03-11`), `gpt-4o-mini-search-preview` (snapshot `gpt-4o-mini-search-preview-2025-03-11`) ([model pages](https://platform.openai.com/docs/models/gpt-4o-search-preview))
- **Announcement**: [Mar 11, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Mar 11, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_applicable (preview)
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions
- **Modalities**: text → text ([model pages](https://platform.openai.com/docs/models/gpt-4o-mini-search-preview))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-4o-search-preview))
- **Relations**: replacement `gpt-5.6-terra`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4o-search-preview)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: —
- **Typed absences**: `not_applicable`, `not_found`

## **computer-use-preview**

- Source report line: `195`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: computer use
- **Exact name**: **computer-use-preview**
- **Kind**: model
- **Native kind wording**: "Specialized model for computer use tool" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `computer-use-preview`, snapshot `computer-use-preview-2025-03-11` ([model page](https://platform.openai.com/docs/models/computer-use-preview))
- **Announcement**: [Mar 11, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Mar 11, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_applicable — cited as the archetype preview model that "may be retired with much shorter notice, such as 2 weeks" ([deprecations](https://platform.openai.com/docs/deprecations))
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Responses API computer-use tool
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/computer-use-preview))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/computer-use-preview))
- **Relations**: replacement `gpt-5.6-terra`; built-in computer use later folded into GPT-5.4/5.5 ([changelog](https://platform.openai.com/docs/changelog))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/computer-use-preview)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: Agentic/computer-use capability migrated from a dedicated model to a tool on general models.
- **Typed absences**: `not_applicable`, `not_found`

## **Daybreak Blue**

- Source report line: `196`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: Daybreak
- **Exact name**: **Daybreak Blue**
- **Kind**: endpoint_alias
- **Native kind wording**: "An alias for flagship general-purpose models with safeguards for defensive cybersecurity work." ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-daybreak-blue-latest`; default snapshot `gpt-5.6-sol` ([model page](https://platform.openai.com/docs/models/gpt-daybreak-blue-latest))
- **Announcement**: [Aug 7, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [Aug 7, 2026](https://platform.openai.com/docs/changelog) — "Start with Daybreak Blue for most defensive security work"
- **GA**: not_applicable — approved defenders
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses API, approval-gated ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-daybreak-blue-latest))
- **Knowledge cutoff**: "Feb 16, 2026" (inherited from the snapshot) ([model page](https://platform.openai.com/docs/models/gpt-daybreak-blue-latest))
- **Relations**: alias → `gpt-5.6-sol`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-daybreak-blue-latest)
- **Lifecycle 2026-09-05**: Active alias
- **Notes / typed gaps**: An access-tier alias, not a model: safeguard/entitlement wrapper over a general model.
- **Typed absences**: `not_applicable`, `not_found`

## **Daybreak Red**

- Source report line: `197`
- Research section: 2b-ii. OpenAI — Codex variants, chat-latest pointers, ChatGPT product labels, search/computer-use, Daybreak aliases
- **Family**: Daybreak
- **Exact name**: **Daybreak Red**
- **Kind**: endpoint_alias
- **Native kind wording**: "An alias for advanced cybersecurity models for authorized vulnerability research and security testing." ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshot**: `gpt-daybreak-red-latest`; default snapshot `gpt-5.6-cyber` ([model page](https://platform.openai.com/docs/models/gpt-daybreak-red-latest))
- **Announcement**: [Aug 7, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [Aug 7, 2026](https://platform.openai.com/docs/changelog) — "Daybreak Red provides separately approved access"
- **GA**: not_applicable
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Responses API, separately approved ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/gpt-daybreak-red-latest))
- **Knowledge cutoff**: "Feb 16, 2026" ([model page](https://platform.openai.com/docs/models/gpt-daybreak-red-latest))
- **Relations**: alias → `gpt-5.6-cyber`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-daybreak-red-latest)
- **Lifecycle 2026-09-05**: Active alias
- **Notes / typed gaps**: —
- **Typed absences**: `not_applicable`, `not_found`

## **GPT-Image-2**

- Source report line: `203`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: GPT Image
- **Exact name**: **GPT-Image-2**
- **Kind**: model
- **Native kind wording**: "State-of-the-art image generation model" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-image-2`; default snapshot `gpt-image-2-2026-04-21` ([model page](https://platform.openai.com/docs/models/gpt-image-2))
- **Announcement**: [Apr 21, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [Apr 21, 2026](https://platform.openai.com/docs/changelog) — "Released GPT Image 2, a state-of-the-art image generation model for image generation and editing"
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Images generations + edits, Batch (50% discount), Responses image tool ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: text, image → image ([model page](https://platform.openai.com/docs/models/gpt-image-2))
- **Knowledge cutoff**: not_reported (image models list no cutoff)
- **Relations**: replacement for `gpt-image-1`, `gpt-image-1-mini`, `gpt-image-1.5`, `chatgpt-image-latest`, `dall-e-2`, `dall-e-3` ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-image-2)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: Transparent backgrounds added in preview [Aug 20, 2026](https://platform.openai.com/docs/changelog) for both `gpt-image-2` and its dated snapshot.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Image-1.5**

- Source report line: `204`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: GPT Image
- **Exact name**: **GPT-Image-1.5**
- **Kind**: model
- **Native kind wording**: "Our previous image generation model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `gpt-image-1.5`, snapshot `gpt-image-1.5-2025-12-16` ([model page](https://platform.openai.com/docs/models/gpt-image-1.5))
- **Announcement**: [Dec 16, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Dec 16, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Jun 2, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Dec 1, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Images API; Responses image tool from [Dec 19, 2025](https://platform.openai.com/docs/changelog); Batch from [Feb 10, 2026](https://platform.openai.com/docs/changelog)
- **Modalities**: text, image → image, text ([model page](https://platform.openai.com/docs/models/gpt-image-1.5))
- **Knowledge cutoff**: not_reported
- **Relations**: replacement `gpt-image-2`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-image-1.5)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: A fidelity bug affecting this ID was fixed [Jan 9, 2026](https://platform.openai.com/docs/changelog) — behavior change under a fixed snapshot.
- **Typed absences**: `not_found`, `not_reported`

## **chatgpt-image-latest**

- Source report line: `205`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: GPT Image
- **Exact name**: **chatgpt-image-latest**
- **Kind**: endpoint_alias
- **Native kind wording**: "Previous image model used in ChatGPT." ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `chatgpt-image-latest` ([model page](https://platform.openai.com/docs/models/chatgpt-image-latest))
- **Announcement**: [Dec 16, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Dec 16, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Jun 2, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Dec 1, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Images API, Responses image tool, Batch
- **Modalities**: text, image → image, text ([model page](https://platform.openai.com/docs/models/chatgpt-image-latest))
- **Knowledge cutoff**: not_reported
- **Relations**: replacement `gpt-image-2`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/chatgpt-image-latest)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: Alias whose target is the ChatGPT image model — product↔API bridge.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Image-1**

- Source report line: `206`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: GPT Image
- **Exact name**: **GPT-Image-1**
- **Kind**: model
- **Native kind wording**: "Our previous image generation model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `gpt-image-1` ([model page](https://platform.openai.com/docs/models/gpt-image-1))
- **Announcement**: [Apr 23, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Apr 23, 2025](https://platform.openai.com/docs/changelog) — "Added a new image generation model, `gpt-image-1`"
- **GA**: not_reported
- **Deprecated**: [Apr 22, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Oct 23, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Images generations + edits, Batch
- **Modalities**: text, image → image ([model page](https://platform.openai.com/docs/models/gpt-image-1))
- **Knowledge cutoff**: not_reported
- **Relations**: replacement `gpt-image-2`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-image-1)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Image-1 Mini**

- Source report line: `207`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: GPT Image
- **Exact name**: **GPT-Image-1 Mini**
- **Kind**: model
- **Native kind wording**: "A cost-efficient version of GPT Image 1" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `gpt-image-1-mini` ([model page](https://platform.openai.com/docs/models/gpt-image-1-mini))
- **Announcement**: [Oct 6, 2025](https://platform.openai.com/docs/changelog) (DevDay)
- **Release**: [Oct 6, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Jun 2, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Dec 1, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Images API, Batch
- **Modalities**: text, image → image ([model page](https://platform.openai.com/docs/models/gpt-image-1-mini))
- **Knowledge cutoff**: not_reported
- **Relations**: replacement `gpt-image-2`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-image-1-mini)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **dall-e-3** and **dall-e-2**

- Source report line: `208`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: DALL·E
- **Exact name**: **dall-e-3** and **dall-e-2**
- **Kind**: models
- **Native kind wording**: "DALL·E model snapshots" ([deprecations](https://platform.openai.com/docs/deprecations))
- **API ID / snapshots**: `dall-e-3`, `dall-e-2` ([deprecations](https://platform.openai.com/docs/deprecations))
- **Announcement**: `dall-e-3` in the API [Nov 6, 2023](https://platform.openai.com/docs/changelog); `dall-e-2` release date `not_found` (predates the changelog)
- **Release**: [Nov 6, 2023](https://platform.openai.com/docs/changelog) for DALL·E 3
- **GA**: not_reported
- **Deprecated**: [Nov 14, 2025](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [May 12, 2026](https://platform.openai.com/docs/changelog) — "deprecated and removed from the API on May 12, 2026"
- **Surfaces**: Images API
- **Modalities**: text → image (per family; not_reported on fetched pages)
- **Knowledge cutoff**: not_applicable
- **Relations**: replacements `gpt-image-2`, `gpt-image-1`, `gpt-image-1-mini` ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found
- **Docs**: [Deprecations](https://platform.openai.com/docs/deprecations)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: Both models are absent from the current catalog while still listed in deprecations — catalog absence ≠ nonexistence.
- **Typed absences**: `not_applicable`, `not_found`, `not_reported`

## **Sora 2**

- Source report line: `209`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Sora
- **Exact name**: **Sora 2**
- **Kind**: model
- **Native kind wording**: "Flagship video generation with synced audio" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `sora-2`; default snapshot `sora-2-2025-12-08`; snapshots `sora-2-2025-12-08`, `sora-2-2025-10-06`, `sora-2` ([model page](https://platform.openai.com/docs/models/sora-2))
- **Announcement**: [Oct 6, 2025](https://platform.openai.com/docs/changelog) (DevDay release in the API)
- **Release**: [Oct 6, 2025](https://platform.openai.com/docs/changelog); alias repointed to `sora-2-2025-12-08` on [Jan 13, 2026](https://platform.openai.com/docs/changelog); capability expansion [Mar 12, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Mar 24, 2026](https://platform.openai.com/docs/deprecations) — "Sora 2 video generation models and Videos API"
- **Shutdown**: [Sep 24, 2026](https://platform.openai.com/docs/deprecations) (`2026-09-24`, together with the Videos API)
- **Surfaces**: `v1/videos`, `v1/videos/characters`, `v1/videos/extensions`, Batch ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: text, image → video, audio ([model page](https://platform.openai.com/docs/models/sora-2))
- **Knowledge cutoff**: not_applicable
- **Relations**: recommended replacement column is "---" (none) ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found on the current [hub index](https://deploymentsafety.openai.com/)
- **Docs**: [Model page](https://platform.openai.com/docs/models/sora-2)
- **Lifecycle 2026-09-05**: Deprecated; shutdown in 19 days
- **Notes / typed gaps**: Rare case: an entire modality endpoint retired with **no** recommended replacement.
- **Typed absences**: `not_applicable`, `not_found`, `not_reported`

## **Sora 2 Pro**

- Source report line: `210`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Sora
- **Exact name**: **Sora 2 Pro**
- **Kind**: configuration
- **Native kind wording**: "Most advanced synced-audio video generation" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `sora-2-pro`; default snapshot `sora-2-pro-2025-10-06` ([model page](https://platform.openai.com/docs/models/sora-2-pro))
- **Announcement**: [Oct 6, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Oct 6, 2025](https://platform.openai.com/docs/changelog); 1080p output added [Mar 12, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Mar 24, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Sep 24, 2026](https://platform.openai.com/docs/deprecations)
- **Surfaces**: `v1/videos`
- **Modalities**: text, image → video, audio ([model page](https://platform.openai.com/docs/models/sora-2-pro))
- **Knowledge cutoff**: not_applicable
- **Relations**: pro configuration of Sora 2
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/sora-2-pro)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_applicable`, `not_found`, `not_reported`

## **GPT-Realtime-2.1** / **GPT-Realtime-2.1 Mini**

- Source report line: `211`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Realtime
- **Exact name**: **GPT-Realtime-2.1** / **GPT-Realtime-2.1 Mini**
- **Kind**: models
- **Native kind wording**: "Reasoning model with tool use" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-realtime-2.1`, `gpt-realtime-2.1-mini` ([model pages](https://platform.openai.com/docs/models/gpt-realtime-2.1))
- **Announcement**: [Jul 6, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [Jul 6, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Realtime API (`v1/realtime`)
- **Modalities**: text, audio, image → text, audio ([model page](https://platform.openai.com/docs/models/gpt-realtime-2.1))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-realtime-2.1))
- **Relations**: replacements for `gpt-realtime` and `gpt-realtime-mini` ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-realtime-2.1)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: The mini is described as "a faster, lower-cost distilled reasoning model" ([changelog](https://platform.openai.com/docs/changelog)) — distillation stated but the teacher model is `not_reported`.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Realtime-2**

- Source report line: `212`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Realtime
- **Exact name**: **GPT-Realtime-2**
- **Kind**: model
- **Native kind wording**: "Reasoning model with tool use" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-realtime-2` ([model page](https://platform.openai.com/docs/models/gpt-realtime-2))
- **Announcement**: [May 7, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [May 7, 2026](https://platform.openai.com/docs/changelog) — "a new realtime voice model with configurable reasoning for speech-to-speech agents"
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Realtime API
- **Modalities**: text, audio, image → text, audio ([model page](https://platform.openai.com/docs/models/gpt-realtime-2))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-realtime-2))
- **Relations**: predecessor of 2.1
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-realtime-2)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Realtime-Translate**

- Source report line: `213`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Realtime
- **Exact name**: **GPT-Realtime-Translate**
- **Kind**: model
- **Native kind wording**: "Streaming speech-to-speech translation model" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-realtime-translate` ([model page](https://platform.openai.com/docs/models/gpt-realtime-translate))
- **Announcement**: [May 7, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [May 7, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: `v1/realtime/translations` ([changelog](https://platform.openai.com/docs/changelog))
- **Modalities**: audio → audio, text ([model page](https://platform.openai.com/docs/models/gpt-realtime-translate))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-realtime-translate))
- **Relations**: —
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-realtime-translate)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Realtime-Whisper**

- Source report line: `214`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Realtime
- **Exact name**: **GPT-Realtime-Whisper**
- **Kind**: model
- **Native kind wording**: "Streaming speech-to-text model for realtime transcription" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-realtime-whisper` ([model page](https://platform.openai.com/docs/models/gpt-realtime-whisper))
- **Announcement**: [May 7, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [May 7, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: `v1/realtime/transcription_sessions`
- **Modalities**: audio, text → text ([model page](https://platform.openai.com/docs/models/gpt-realtime-whisper))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-realtime-whisper))
- **Relations**: name reuses "Whisper" but is a distinct model from `whisper-1`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-realtime-whisper)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: Name collision hazard: `gpt-realtime-whisper` (2026) vs `whisper-1` (legacy).
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Realtime-1.5**

- Source report line: `215`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Realtime
- **Exact name**: **GPT-Realtime-1.5**
- **Kind**: model
- **Native kind wording**: "The best voice model for audio in, audio out" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-realtime-1.5` ([model page](https://platform.openai.com/docs/models/gpt-realtime-1.5))
- **Announcement**: [Feb 23, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [Feb 23, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Realtime API
- **Modalities**: text, audio, image → text, audio ([model page](https://platform.openai.com/docs/models/gpt-realtime-1.5))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-realtime-1.5))
- **Relations**: migration target for retired `gpt-4o-realtime-preview` snapshots ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-realtime-1.5)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Realtime**

- Source report line: `216`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Realtime
- **Exact name**: **GPT-Realtime**
- **Kind**: model
- **Native kind wording**: "Model capable of realtime text and audio inputs and outputs" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `gpt-realtime`, snapshot `gpt-realtime-2025-08-28` ([model page](https://platform.openai.com/docs/models/gpt-realtime))
- **Announcement**: [Aug 28, 2025](https://platform.openai.com/docs/changelog) — "The OpenAI Realtime API is now generally available"
- **Release**: [Aug 28, 2025](https://platform.openai.com/docs/changelog)
- **GA**: [Aug 28, 2025](https://platform.openai.com/docs/changelog) (API GA)
- **Deprecated**: [Jul 20, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jan 20, 2027](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Realtime API
- **Modalities**: text, audio, image → text, audio ([model page](https://platform.openai.com/docs/models/gpt-realtime))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-realtime))
- **Relations**: replacement `gpt-realtime-2.1`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-realtime)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`

## **GPT-Realtime Mini**

- Source report line: `217`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Realtime
- **Exact name**: **GPT-Realtime Mini**
- **Kind**: model
- **Native kind wording**: "A cost-efficient version of GPT-Realtime"; catalog badge "Deprecated" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-realtime-mini`; default snapshot `gpt-realtime-mini-2025-12-15`; snapshots `-2025-10-06`, `-2025-12-15` ([model page](https://platform.openai.com/docs/models/gpt-realtime-mini))
- **Announcement**: [Oct 6, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Oct 6, 2025](https://platform.openai.com/docs/changelog); new snapshot [Dec 15, 2025](https://platform.openai.com/docs/changelog); slug repointed [Jan 13, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: `-2025-10-06` [Apr 22, 2026](https://platform.openai.com/docs/deprecations); family [Jul 20, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: `-2025-10-06` [Jul 23, 2026](https://platform.openai.com/docs/deprecations); family [Jan 20, 2027](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Realtime API
- **Modalities**: text, image, audio → text, audio ([model page](https://platform.openai.com/docs/models/gpt-realtime-mini))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-realtime-mini))
- **Relations**: replacement `gpt-realtime-2.1-mini`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-realtime-mini)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: Alias validity: `gpt-realtime-mini` → `-2025-10-06` (2025-10-06 → 2026-01-13), then → `-2025-12-15`.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Audio-1.5**

- Source report line: `218`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Audio (Chat)
- **Exact name**: **GPT-Audio-1.5**
- **Kind**: model
- **Native kind wording**: "The best voice model for audio in, audio out with Chat Completions." ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `gpt-audio-1.5` ([model page](https://platform.openai.com/docs/models/gpt-audio-1.5))
- **Announcement**: [Feb 23, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [Feb 23, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: Chat Completions
- **Modalities**: text, audio → text, audio ([model page](https://platform.openai.com/docs/models/gpt-audio-1.5))
- **Knowledge cutoff**: "Sep 30, 2024" ([model page](https://platform.openai.com/docs/models/gpt-audio-1.5))
- **Relations**: replacement for `gpt-audio`, `gpt-4o-audio`, `gpt-audio-mini`, `gpt-4o-mini-audio` ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-audio-1.5)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Audio**

- Source report line: `219`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Audio (Chat)
- **Exact name**: **GPT-Audio**
- **Kind**: model
- **Native kind wording**: "For audio inputs and outputs with Chat Completions API" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `gpt-audio`, snapshot `gpt-audio-2025-08-28` ([model page](https://platform.openai.com/docs/models/gpt-audio))
- **Announcement**: [Aug 28, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Aug 28, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: [Jul 20, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Jan 20, 2027](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions
- **Modalities**: text, audio → text, audio ([model page](https://platform.openai.com/docs/models/gpt-audio))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-audio))
- **Relations**: replacement `gpt-audio-1.5`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-audio)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Audio Mini**

- Source report line: `220`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Audio (Chat)
- **Exact name**: **GPT-Audio Mini**
- **Kind**: model
- **Native kind wording**: "A cost-efficient version of GPT Audio" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `gpt-audio-mini`; default `gpt-audio-mini-2025-12-15`; snapshots `-2025-10-06`, `-2025-12-15` ([model page](https://platform.openai.com/docs/models/gpt-audio-mini))
- **Announcement**: [Oct 6, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Oct 6, 2025](https://platform.openai.com/docs/changelog); new snapshot [Dec 15, 2025](https://platform.openai.com/docs/changelog); repointed [Jan 13, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: `-2025-10-06` [Apr 22, 2026](https://platform.openai.com/docs/deprecations); family [Jul 20, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: `-2025-10-06` [Jul 23, 2026](https://platform.openai.com/docs/deprecations); family [Jan 20, 2027](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions
- **Modalities**: text, audio → text, audio ([model page](https://platform.openai.com/docs/models/gpt-audio-mini))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-audio-mini))
- **Relations**: replacement `gpt-audio-1.5`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-audio-mini)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4o Audio**, **GPT-4o Mini Audio**, **GPT-4o Realtime**, **GPT-4o Mini Realtime**

- Source report line: `221`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: GPT-4o audio
- **Exact name**: **GPT-4o Audio**, **GPT-4o Mini Audio**, **GPT-4o Realtime**, **GPT-4o Mini Realtime**
- **Kind**: models
- **Native kind wording**: preview models ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `gpt-4o-audio-preview` (snapshots `-2025-06-03`, `-2024-12-17`, `-2024-10-01`), `gpt-4o-mini-audio-preview` (`-2024-12-17`), `gpt-4o-realtime-preview` (snapshots `-2025-06-03`, `-2024-12-17`, `-2024-10-01`), `gpt-4o-mini-realtime-preview` (`-2024-12-17`) ([model pages](https://platform.openai.com/docs/models/gpt-4o-audio-preview))
- **Announcement**: audio preview [Oct 17, 2024](https://platform.openai.com/docs/changelog); Realtime API [Oct 1, 2024](https://platform.openai.com/docs/changelog); Dec snapshots [Dec 17, 2024](https://platform.openai.com/docs/changelog); Jun snapshots [Jun 3, 2025](https://platform.openai.com/docs/changelog)
- **Release**: as announced
- **GA**: not_applicable (preview; "identified by `preview` in the model name") ([deprecations](https://platform.openai.com/docs/deprecations))
- **Deprecated**: `-2024-10-01` snapshots [Jun 10, 2025](https://platform.openai.com/docs/deprecations); family [Sep 15, 2025](https://platform.openai.com/docs/deprecations) and [Jul 20, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: `-2024-10-01` [Oct 10, 2025](https://platform.openai.com/docs/deprecations); preview families [May 7, 2026](https://platform.openai.com/docs/deprecations); remaining families [Jan 20, 2027](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Chat Completions, Realtime API
- **Modalities**: text, audio → text, audio ([model pages](https://platform.openai.com/docs/models/gpt-4o-realtime-preview))
- **Knowledge cutoff**: "Oct 01, 2023" ([model page](https://platform.openai.com/docs/models/gpt-4o-audio-preview))
- **Relations**: "Uses the same underlying model as the Realtime API" ([changelog](https://platform.openai.com/docs/changelog)) — an officially stated shared-model relation across two endpoints
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4o-audio-preview)
- **Lifecycle 2026-09-05**: Deprecated / partly retired
- **Notes / typed gaps**: Same underlying model exposed as two endpoint families with independent lifecycles.
- **Typed absences**: `not_applicable`, `not_found`

## **GPT-Transcribe**

- Source report line: `222`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Transcription
- **Exact name**: **GPT-Transcribe**
- **Kind**: model
- **Native kind wording**: "High-accuracy speech-to-text model for file and Realtime input transcription" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-transcribe` ([model page](https://platform.openai.com/docs/models/gpt-transcribe))
- **Announcement**: [Jul 28, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [Jul 28, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: `v1/audio/transcriptions`, `v1/realtime`
- **Modalities**: audio, text → text ([model page](https://platform.openai.com/docs/models/gpt-transcribe))
- **Knowledge cutoff**: not_reported
- **Relations**: replacement for `whisper-1`, `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe-diarize` ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-transcribe)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-Live-Transcribe**

- Source report line: `223`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Transcription
- **Exact name**: **GPT-Live-Transcribe**
- **Kind**: model
- **Native kind wording**: "Low-latency speech-to-text model for realtime transcription" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-live-transcribe` ([model page](https://platform.openai.com/docs/models/gpt-live-transcribe))
- **Announcement**: [Jul 28, 2026](https://platform.openai.com/docs/changelog)
- **Release**: [Jul 28, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: `v1/realtime`, `v1/audio/transcriptions`
- **Modalities**: audio, text → text ([model page](https://platform.openai.com/docs/models/gpt-live-transcribe))
- **Knowledge cutoff**: not_reported
- **Relations**: co-replacement with `gpt-transcribe` ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-live-transcribe)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: Naming overlaps the ChatGPT-only "GPT-Live-1" voice models but they are different entities.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4o Transcribe**

- Source report line: `224`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Transcription
- **Exact name**: **GPT-4o Transcribe**
- **Kind**: model
- **Native kind wording**: "Speech-to-text model powered by GPT-4o" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-4o-transcribe` ([model page](https://platform.openai.com/docs/models/gpt-4o-transcribe))
- **Announcement**: [Mar 20, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Mar 20, 2025](https://platform.openai.com/docs/changelog) — "Added `gpt-4o-mini-tts`, `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, and `whisper-1` models to the Audio API"
- **GA**: not_reported
- **Deprecated**: [Aug 26, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Feb 26, 2027](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Audio API
- **Modalities**: audio, text → text ([model page](https://platform.openai.com/docs/models/gpt-4o-transcribe))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/gpt-4o-transcribe))
- **Relations**: "powered by GPT-4o" — officially stated derivation
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4o-transcribe)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4o Mini Transcribe**

- Source report line: `225`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Transcription
- **Exact name**: **GPT-4o Mini Transcribe**
- **Kind**: model
- **Native kind wording**: "Speech-to-text model powered by GPT-4o mini" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-4o-mini-transcribe`; default `gpt-4o-mini-transcribe-2025-12-15`; snapshots `-2025-03-20`, `-2025-12-15` ([model page](https://platform.openai.com/docs/models/gpt-4o-mini-transcribe))
- **Announcement**: [Mar 20, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Mar 20, 2025](https://platform.openai.com/docs/changelog); new snapshot [Dec 15, 2025](https://platform.openai.com/docs/changelog); repointed [Jan 13, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: `-2025-03-20` [Jul 20, 2026](https://platform.openai.com/docs/deprecations); family [Aug 26, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: `-2025-03-20` [Jan 20, 2027](https://platform.openai.com/docs/deprecations); family [Feb 26, 2027](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Audio API
- **Modalities**: audio, text → text ([model page](https://platform.openai.com/docs/models/gpt-4o-mini-transcribe))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/gpt-4o-mini-transcribe))
- **Relations**: "powered by GPT-4o mini"
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4o-mini-transcribe)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: Snapshot-level and family-level deprecations coexist with different dates.
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4o Transcribe Diarize**

- Source report line: `226`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Transcription
- **Exact name**: **GPT-4o Transcribe Diarize**
- **Kind**: model
- **Native kind wording**: "Transcription model that identifies who's speaking when" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `gpt-4o-transcribe-diarize` ([model page](https://platform.openai.com/docs/models/gpt-4o-transcribe-diarize))
- **Announcement**: not_reported (no changelog entry located → `not_found`)
- **Release**: not_found
- **GA**: not_reported
- **Deprecated**: [Aug 26, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Feb 26, 2027](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Audio API
- **Modalities**: text, audio → text ([model page](https://platform.openai.com/docs/models/gpt-4o-transcribe-diarize))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/gpt-4o-transcribe-diarize))
- **Relations**: replacement `gpt-live-transcribe` or `gpt-transcribe`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4o-transcribe-diarize)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: A model with a documented deprecation but no documented release — flagged in §8.
- **Typed absences**: `not_found`, `not_reported`

## **Whisper**

- Source report line: `227`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Transcription
- **Exact name**: **Whisper**
- **Kind**: model
- **Native kind wording**: "General-purpose speech recognition model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `whisper-1` ([model page](https://platform.openai.com/docs/models/whisper-1))
- **Announcement**: not_found (added to the Audio API list on [Mar 20, 2025](https://platform.openai.com/docs/changelog), which is not a release date for the model)
- **Release**: not_found
- **GA**: not_reported
- **Deprecated**: [Aug 26, 2026](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Feb 26, 2027](https://platform.openai.com/docs/deprecations)
- **Surfaces**: Audio API
- **Modalities**: audio → text ([model page](https://platform.openai.com/docs/models/whisper-1))
- **Knowledge cutoff**: not_reported
- **Relations**: replacement `gpt-live-transcribe` or `gpt-transcribe`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/whisper-1)
- **Lifecycle 2026-09-05**: Deprecated
- **Notes / typed gaps**: —
- **Typed absences**: `not_found`, `not_reported`

## **GPT-4o mini TTS**

- Source report line: `228`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Speech
- **Exact name**: **GPT-4o mini TTS**
- **Kind**: model
- **Native kind wording**: "Text-to-speech model powered by GPT-4o mini" ([Models](https://platform.openai.com/docs/models))
- **API ID / snapshots**: `gpt-4o-mini-tts`; default `gpt-4o-mini-tts-2025-12-15`; snapshots `-2025-03-20`, `-2025-12-15` ([model page](https://platform.openai.com/docs/models/gpt-4o-mini-tts))
- **Announcement**: [Mar 20, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Mar 20, 2025](https://platform.openai.com/docs/changelog); new snapshot [Dec 15, 2025](https://platform.openai.com/docs/changelog) with Custom voices; repointed [Jan 13, 2026](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: not_reported
- **Shutdown**: not_reported
- **Surfaces**: `v1/audio/speech`
- **Modalities**: text → audio ([model page](https://platform.openai.com/docs/models/gpt-4o-mini-tts))
- **Knowledge cutoff**: not_reported
- **Relations**: "powered by GPT-4o mini"
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-4o-mini-tts)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: Still listed as a current speech model in the catalog ([Models](https://platform.openai.com/docs/models)).
- **Typed absences**: `not_found`, `not_reported`

## **TTS-1** / **TTS-1 HD**

- Source report line: `229`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Speech
- **Exact name**: **TTS-1** / **TTS-1 HD**
- **Kind**: models
- **Native kind wording**: "Text-to-speech model optimized for speed" / "…for quality" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `tts-1`, `tts-1-hd` ([model pages](https://platform.openai.com/docs/models/tts-1))
- **Announcement**: text-to-speech API launched [Nov 6, 2023](https://platform.openai.com/docs/changelog); per-model release dates `not_found`
- **Release**: not_found
- **GA**: not_reported
- **Deprecated**: not_reported
- **Shutdown**: not_reported
- **Surfaces**: `v1/audio/speech`
- **Modalities**: text → audio ([model pages](https://platform.openai.com/docs/models/tts-1-hd))
- **Knowledge cutoff**: not_applicable
- **Relations**: —
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/tts-1)
- **Lifecycle 2026-09-05**: Legacy, still catalogued
- **Notes / typed gaps**: —
- **Typed absences**: `not_applicable`, `not_found`, `not_reported`

## **text-embedding-3-large** / **text-embedding-3-small**

- Source report line: `230`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Embeddings
- **Exact name**: **text-embedding-3-large** / **text-embedding-3-small**
- **Kind**: models
- **Native kind wording**: embedding models ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `text-embedding-3-large`, `text-embedding-3-small` ([model pages](https://platform.openai.com/docs/models/text-embedding-3-large))
- **Announcement**: [Jan 25, 2024](https://platform.openai.com/docs/changelog) — "Released embedding V3 models"
- **Release**: [Jan 25, 2024](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: not_reported
- **Shutdown**: not_reported
- **Surfaces**: `v1/embeddings`, Batch (from [Apr 29, 2024](https://platform.openai.com/docs/changelog))
- **Modalities**: text → embedding vectors ([model pages](https://platform.openai.com/docs/models/text-embedding-3-small))
- **Knowledge cutoff**: not_applicable
- **Relations**: `dimensions` parameter added at release ([changelog](https://platform.openai.com/docs/changelog))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/text-embedding-3-large)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: Longest-lived unchanged OpenAI models in the current catalog.
- **Typed absences**: `not_applicable`, `not_found`, `not_reported`

## **text-embedding-ada-002**

- Source report line: `231`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Embeddings
- **Exact name**: **text-embedding-ada-002**
- **Kind**: model
- **Native kind wording**: "Older embedding model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `text-embedding-ada-002` ([model page](https://platform.openai.com/docs/models/text-embedding-ada-002))
- **Announcement**: not_found
- **Release**: not_found
- **GA**: not_reported
- **Deprecated**: not_reported
- **Shutdown**: not_reported
- **Surfaces**: `v1/embeddings`
- **Modalities**: text → embedding vectors ([model page](https://platform.openai.com/docs/models/text-embedding-ada-002))
- **Knowledge cutoff**: not_applicable
- **Relations**: —
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/text-embedding-ada-002)
- **Lifecycle 2026-09-05**: Legacy, still catalogued
- **Notes / typed gaps**: —
- **Typed absences**: `not_applicable`, `not_found`, `not_reported`

## **omni-moderation**

- Source report line: `232`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Moderation
- **Exact name**: **omni-moderation**
- **Kind**: model
- **Native kind wording**: "Identify potentially harmful content in text and images" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `omni-moderation-latest`, default snapshot `omni-moderation-2024-09-26` ([model page](https://platform.openai.com/docs/models/omni-moderation-latest))
- **Announcement**: [Sep 26, 2024](https://platform.openai.com/docs/changelog)
- **Release**: [Sep 26, 2024](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: `v1/moderations`; moderation scores added to Responses/Chat Completions [Jun 4, 2026](https://platform.openai.com/docs/changelog)
- **Modalities**: text, image → text ([model page](https://platform.openai.com/docs/models/omni-moderation-latest))
- **Knowledge cutoff**: not_applicable
- **Relations**: replacement for the `text-moderation` line ([deprecations](https://platform.openai.com/docs/deprecations))
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/omni-moderation-latest)
- **Lifecycle 2026-09-05**: Active
- **Notes / typed gaps**: `-latest` alias with one dated snapshot behind it since 2024-09-26.
- **Typed absences**: `not_applicable`, `not_found`, `not_reported`

## **text-moderation** / **text-moderation-stable**

- Source report line: `233`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Moderation
- **Exact name**: **text-moderation** / **text-moderation-stable**
- **Kind**: endpoint_alias
- **Native kind wording**: "Previous generation text-only moderation model" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `text-moderation-latest`, `text-moderation-stable`, both with default snapshot `text-moderation-007` ([model pages](https://platform.openai.com/docs/models/text-moderation-latest))
- **Announcement**: not_found
- **Release**: not_found
- **GA**: not_reported
- **Deprecated**: [Apr 28, 2025](https://platform.openai.com/docs/deprecations)
- **Shutdown**: [Oct 27, 2025](https://platform.openai.com/docs/deprecations)
- **Surfaces**: `v1/moderations`
- **Modalities**: text → text ([model page](https://platform.openai.com/docs/models/text-moderation-stable))
- **Knowledge cutoff**: "Sep 01, 2021" ([model page](https://platform.openai.com/docs/models/text-moderation-latest))
- **Relations**: replacement `omni-moderation`
- **Card**: not_found
- **Docs**: [Model page](https://platform.openai.com/docs/models/text-moderation-latest)
- **Lifecycle 2026-09-05**: Retired
- **Notes / typed gaps**: Two aliases resolving to one snapshot — a clean alias-vs-checkpoint test case.
- **Typed absences**: `not_found`, `not_reported`

## **gpt-oss-120b** / **gpt-oss-20b**

- Source report line: `234`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Open weights
- **Exact name**: **gpt-oss-120b** / **gpt-oss-20b**
- **Kind**: models (open weights)
- **Native kind wording**: "Most powerful open-weight model, fits into an H100 GPU" / "Medium-sized open-weight model for low latency" ([models.md](https://platform.openai.com/docs/models.md))
- **API ID / snapshots**: `gpt-oss-120b`, `gpt-oss-20b` ([model pages](https://platform.openai.com/docs/models/gpt-oss-120b))
- **Announcement**: [Aug 5, 2025](https://help.openai.com/en/articles/9624314-model-release-notes) — "Introducing two open-weight models: gpt-oss-120b and gpt-oss-20b"
- **Release**: [Aug 5, 2025](https://help.openai.com/en/articles/9624314-model-release-notes)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: **Not OpenAI-hosted:** "These models are not served through the OpenAI API and are not available in ChatGPT" ([help center](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss))
- **Modalities**: text → text ([model page](https://platform.openai.com/docs/models/gpt-oss-120b))
- **Knowledge cutoff**: "Jun 01, 2024" ([model page](https://platform.openai.com/docs/models/gpt-oss-120b))
- **Relations**: base of the `gpt-oss-safeguard` models ([changelog](https://platform.openai.com/docs/changelog))
- **Card**: not_found on the current [hub index](https://deploymentsafety.openai.com/)
- **Docs**: [Model page](https://platform.openai.com/docs/models/gpt-oss-120b)
- **Lifecycle 2026-09-05**: Released weights; not a hosted deployment
- **Notes / typed gaps**: Catalogued models with **no** endpoint — the catalog documents weights, not availability.
- **Typed absences**: `not_found`, `not_reported`

## **gpt-oss-safeguard-120b** / **gpt-oss-safeguard-20b**

- Source report line: `235`
- Research section: 2b-iii. OpenAI — image, video, audio, realtime, transcription, speech, embeddings, moderation, open weights
- **Family**: Open weights
- **Exact name**: **gpt-oss-safeguard-120b** / **gpt-oss-safeguard-20b**
- **Kind**: models (open weights)
- **Native kind wording**: "safety reasoning models built-upon gpt-oss" ([changelog](https://platform.openai.com/docs/changelog))
- **API ID / snapshots**: `gpt-oss-safeguard-120b`, `gpt-oss-safeguard-20b` ([changelog](https://platform.openai.com/docs/changelog))
- **Announcement**: [Oct 29, 2025](https://platform.openai.com/docs/changelog)
- **Release**: [Oct 29, 2025](https://platform.openai.com/docs/changelog)
- **GA**: not_reported
- **Deprecated**: N/A
- **Shutdown**: N/A
- **Surfaces**: "Like other gpt-oss models, these weights are not served through the OpenAI API or ChatGPT" ([help center](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss))
- **Modalities**: text → text (per family)
- **Knowledge cutoff**: not_reported
- **Relations**: "built-upon gpt-oss" ([changelog](https://platform.openai.com/docs/changelog))
- **Card**: not_found
- **Docs**: [Changelog](https://platform.openai.com/docs/changelog)
- **Lifecycle 2026-09-05**: Released weights
- **Notes / typed gaps**: Not present in the model catalog → an archive mention resolves only via changelog + help center.
- **Typed absences**: `not_found`, `not_reported`
