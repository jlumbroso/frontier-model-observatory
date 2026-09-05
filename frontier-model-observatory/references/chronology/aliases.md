# Aliases and endpoint identifiers

Generated from the official-source chronology observed 2026-09-05.
These are research projections, not canonical records. Preserve typed
gaps, date precision, and competing provider values.

Rows: **29**.

## Anthropic

- Source report line: `313`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Anthropic
- **Alias / endpoint identifier**: `claude-sonnet-4-5`
- **Kind**: convenience alias
- **Resolves to**: most recent dated snapshot of Sonnet 4.5, i.e. `claude-sonnet-4-5-20250929`
- **Valid from**: not_reported (exists for pre-4.6 models)
- **Valid to**: → present
- **Source of the mapping**: [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
- **Notes**: "On the Claude API, these models also have shorter aliases … that point to the most recent dated snapshot for that minor version."
- **Typed absences**: `not_reported`

## Anthropic

- Source report line: `314`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Anthropic
- **Alias / endpoint identifier**: `claude-haiku-4-5`
- **Kind**: convenience alias
- **Resolves to**: `claude-haiku-4-5-20251001`
- **Valid from**: [Oct 15, 2025](https://www.anthropic.com/news/claude-haiku-4-5) (used in the launch post)
- **Valid to**: → present
- **Source of the mapping**: [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
- **Notes**: The announcement cites the alias, the docs cite the pinned ID.

## Anthropic

- Source report line: `315`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Anthropic
- **Alias / endpoint identifier**: `claude-opus-4-6`, `claude-sonnet-4-6`, `claude-opus-4-7`, `claude-opus-4-8`, `claude-sonnet-5`, `claude-opus-5`, `claude-fable-5`, `claude-fable-5-1`, `claude-mythos-5`, `claude-mythos-5-1`
- **Kind**: **not aliases** — pinned snapshots
- **Resolves to**: themselves
- **Valid from**: per-model release date (§2a)
- **Valid to**: → present
- **Source of the mapping**: [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
- **Notes**: "A 4.6-generation ID such as `claude-sonnet-4-6` is not an alias. It is the snapshot."

## Anthropic

- Source report line: `316`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Anthropic
- **Alias / endpoint identifier**: `anthropic.claude-opus-4-6-v1`
- **Kind**: Bedrock endpoint ID
- **Resolves to**: Claude Opus 4.6
- **Valid from**: Opus 4.6 release ([Feb 5, 2026](https://platform.claude.com/docs/en/release-notes/overview))
- **Valid to**: → present
- **Source of the mapping**: [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
- **Notes**: "the last Bedrock model ID to include the `-v1` suffix".

## Anthropic

- Source report line: `317`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Anthropic
- **Alias / endpoint identifier**: `anthropic.claude-sonnet-4-6`, `anthropic.claude-opus-4-7`, `anthropic.claude-opus-4-8`, `anthropic.claude-sonnet-5`, `anthropic.claude-opus-5`
- **Kind**: Bedrock endpoint IDs
- **Resolves to**: corresponding models
- **Valid from**: per-model release date
- **Valid to**: → present
- **Source of the mapping**: [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
- **Notes**: Suffix dropped starting with Sonnet 4.6.

## Anthropic

- Source report line: `318`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Anthropic
- **Alias / endpoint identifier**: `claude-haiku-4-5@20251001`
- **Kind**: Google Cloud endpoint ID
- **Resolves to**: `claude-haiku-4-5-20251001`
- **Valid from**: [Oct 15, 2025](https://platform.claude.com/docs/en/release-notes/overview)
- **Valid to**: → present
- **Source of the mapping**: [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
- **Notes**: Google Cloud separates the snapshot date with `@`.

## OpenAI

- Source report line: `319`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `gpt-5.6`
- **Kind**: alias
- **Resolves to**: `gpt-5.6-sol`
- **Valid from**: [Jul 9, 2026](https://platform.openai.com/docs/changelog)
- **Valid to**: → present
- **Source of the mapping**: [Models](https://platform.openai.com/docs/models) · [changelog](https://platform.openai.com/docs/changelog)
- **Notes**: "The `gpt-5.6` alias routes requests to `gpt-5.6-sol`."

## OpenAI

- Source report line: `320`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `gpt-daybreak-blue-latest`
- **Kind**: access-tier alias
- **Resolves to**: default snapshot `gpt-5.6-sol`
- **Valid from**: [Aug 7, 2026](https://platform.openai.com/docs/changelog)
- **Valid to**: → present
- **Source of the mapping**: [Model page](https://platform.openai.com/docs/models/gpt-daybreak-blue-latest)
- **Notes**: Approval-gated alias, not a distinct model.

## OpenAI

- Source report line: `321`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `gpt-daybreak-red-latest`
- **Kind**: access-tier alias
- **Resolves to**: default snapshot `gpt-5.6-cyber`
- **Valid from**: [Aug 7, 2026](https://platform.openai.com/docs/changelog)
- **Valid to**: → present
- **Source of the mapping**: [Model page](https://platform.openai.com/docs/models/gpt-daybreak-red-latest)
- **Notes**: —

## OpenAI

- Source report line: `322`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `chat-latest`
- **Kind**: mutable pointer
- **Resolves to**: ChatGPT's current Plus/Pro model; earlier the Instant model
- **Valid from**: [May 5, 2026](https://platform.openai.com/docs/changelog)
- **Valid to**: → present, repointed [May 28, 2026](https://platform.openai.com/docs/changelog), [Jun 24, 2026](https://platform.openai.com/docs/changelog), [Aug 6, 2026](https://platform.openai.com/docs/changelog)
- **Source of the mapping**: [Model page](https://platform.openai.com/docs/models/chat-latest)
- **Notes**: "The underlying model snapshot will be regularly updated."

## OpenAI

- Source report line: `323`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `chatgpt-4o-latest`
- **Kind**: mutable pointer
- **Resolves to**: latest ChatGPT GPT-4o model
- **Valid from**: [Aug 15, 2024](https://platform.openai.com/docs/changelog)
- **Valid to**: [Feb 17, 2026](https://platform.openai.com/docs/deprecations)
- **Source of the mapping**: [Model page](https://platform.openai.com/docs/models/chatgpt-4o-latest)
- **Notes**: Retired alias.

## OpenAI

- Source report line: `324`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `gpt-5-chat-latest`, `gpt-5.1-chat-latest`, `gpt-5.2-chat-latest`, `gpt-5.3-chat-latest`
- **Kind**: ChatGPT-tracking aliases
- **Resolves to**: the ChatGPT snapshot of each generation
- **Valid from**: [Aug 7, 2025](https://platform.openai.com/docs/changelog) / [Nov 13, 2025](https://platform.openai.com/docs/changelog) / [Dec 11, 2025](https://platform.openai.com/docs/changelog) / [Mar 3, 2026](https://platform.openai.com/docs/changelog)
- **Valid to**: [Jul 23, 2026](https://platform.openai.com/docs/deprecations) / [Jul 23, 2026](https://platform.openai.com/docs/deprecations) / [Aug 10, 2026](https://platform.openai.com/docs/deprecations) / [Aug 10, 2026](https://platform.openai.com/docs/deprecations)
- **Source of the mapping**: [Deprecations](https://platform.openai.com/docs/deprecations)
- **Notes**: `gpt-5.3-chat-latest` was itself repointed on [Mar 16, 2026](https://platform.openai.com/docs/changelog).

## OpenAI

- Source report line: `325`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `gpt-realtime-mini`
- **Kind**: family alias
- **Resolves to**: `gpt-realtime-mini-2025-10-06`, then `gpt-realtime-mini-2025-12-15`
- **Valid from**: [Oct 6, 2025](https://platform.openai.com/docs/changelog)
- **Valid to**: repointed [Jan 13, 2026](https://platform.openai.com/docs/changelog); family shutdown [Jan 20, 2027](https://platform.openai.com/docs/deprecations)
- **Source of the mapping**: [Model page](https://platform.openai.com/docs/models/gpt-realtime-mini)
- **Notes**: —

## OpenAI

- Source report line: `326`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `gpt-audio-mini`
- **Kind**: family alias
- **Resolves to**: `gpt-audio-mini-2025-10-06`, then `-2025-12-15`
- **Valid from**: [Oct 6, 2025](https://platform.openai.com/docs/changelog)
- **Valid to**: repointed [Jan 13, 2026](https://platform.openai.com/docs/changelog); shutdown [Jan 20, 2027](https://platform.openai.com/docs/deprecations)
- **Source of the mapping**: [Model page](https://platform.openai.com/docs/models/gpt-audio-mini)
- **Notes**: —

## OpenAI

- Source report line: `327`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `gpt-4o-mini-transcribe`, `gpt-4o-mini-tts`
- **Kind**: family aliases
- **Resolves to**: `-2025-03-20`, then `-2025-12-15`
- **Valid from**: [Mar 20, 2025](https://platform.openai.com/docs/changelog)
- **Valid to**: repointed [Jan 13, 2026](https://platform.openai.com/docs/changelog); transcribe shutdown [Feb 26, 2027](https://platform.openai.com/docs/deprecations)
- **Source of the mapping**: [Changelog](https://platform.openai.com/docs/changelog)
- **Notes**: —

## OpenAI

- Source report line: `328`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `sora-2`
- **Kind**: family alias
- **Resolves to**: `sora-2-2025-10-06`, then `sora-2-2025-12-08`
- **Valid from**: [Oct 6, 2025](https://platform.openai.com/docs/changelog)
- **Valid to**: repointed [Jan 13, 2026](https://platform.openai.com/docs/changelog); shutdown [Sep 24, 2026](https://platform.openai.com/docs/deprecations)
- **Source of the mapping**: [Model page](https://platform.openai.com/docs/models/sora-2)
- **Notes**: —

## OpenAI

- Source report line: `329`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `gpt-4o`
- **Kind**: family alias
- **Resolves to**: default `gpt-4o-2024-08-06` (snapshots 2024-05-13, 2024-08-06, 2024-11-20)
- **Valid from**: [May 13, 2024](https://platform.openai.com/docs/changelog)
- **Valid to**: → present
- **Source of the mapping**: [Model page](https://platform.openai.com/docs/models/gpt-4o)
- **Notes**: One snapshot deprecated while the alias stays active.

## OpenAI

- Source report line: `330`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `gpt-4-turbo-preview`, `gpt-4-turbo-preview-completions`
- **Kind**: aliases
- **Resolves to**: `gpt-4-0125-preview`
- **Valid from**: [Nov 6, 2023](https://platform.openai.com/docs/changelog)
- **Valid to**: [Mar 26, 2026](https://platform.openai.com/docs/deprecations)
- **Source of the mapping**: [Deprecations](https://platform.openai.com/docs/deprecations)
- **Notes**: Alias and target retired together.

## OpenAI

- Source report line: `331`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `text-moderation-latest`, `text-moderation-stable`
- **Kind**: aliases
- **Resolves to**: `text-moderation-007`
- **Valid from**: not_reported
- **Valid to**: [Oct 27, 2025](https://platform.openai.com/docs/deprecations)
- **Source of the mapping**: [Model page](https://platform.openai.com/docs/models/text-moderation-latest)
- **Notes**: Two aliases, one snapshot.
- **Typed absences**: `not_reported`

## OpenAI

- Source report line: `332`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `omni-moderation-latest`
- **Kind**: alias
- **Resolves to**: `omni-moderation-2024-09-26`
- **Valid from**: [Sep 26, 2024](https://platform.openai.com/docs/changelog)
- **Valid to**: → present
- **Source of the mapping**: [Model page](https://platform.openai.com/docs/models/omni-moderation-latest)
- **Notes**: —

## OpenAI

- Source report line: `333`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: OpenAI
- **Alias / endpoint identifier**: `o1`, `o3-mini`, `o4-mini`, `o1-pro`, `computer-use-preview`, `gpt-3.5-turbo`, `gpt-4`
- **Kind**: aliases with pipe-listed equivalents in the deprecation table (e.g. "`o1-2024-12-17` \| `o1`")
- **Resolves to**: their dated snapshots
- **Valid from**: per model
- **Valid to**: [Oct 23, 2026](https://platform.openai.com/docs/deprecations) / [Jul 23, 2026](https://platform.openai.com/docs/deprecations)
- **Source of the mapping**: [Deprecations](https://platform.openai.com/docs/deprecations)
- **Notes**: The pipe notation is OpenAI's own alias-grouping syntax.

## Google

- Source report line: `334`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Google
- **Alias / endpoint identifier**: `gemini-flash-latest`
- **Kind**: hot-swapped alias
- **Resolves to**: `gemini-3-flash-preview` from [Jan 21, 2026](https://ai.google.dev/gemini-api/docs/changelog); `gemini-3.5-flash` from [May 19, 2026](https://ai.google.dev/gemini-api/docs/changelog)
- **Valid from**: [Jan 21, 2026](https://ai.google.dev/gemini-api/docs/changelog)
- **Valid to**: → present
- **Source of the mapping**: [Models](https://ai.google.dev/gemini-api/docs/models) · [changelog](https://ai.google.dev/gemini-api/docs/changelog)
- **Notes**: "This alias will get hot-swapped with every new release … For breaking changes, a 2-week notice will be provided through email."

## Google

- Source report line: `335`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Google
- **Alias / endpoint identifier**: `gemini-pro-latest`
- **Kind**: hot-swapped alias
- **Resolves to**: `gemini-3-pro-preview`
- **Valid from**: [Jan 21, 2026](https://ai.google.dev/gemini-api/docs/changelog)
- **Valid to**: → present (target itself repointed, see next row)
- **Source of the mapping**: [Changelog](https://ai.google.dev/gemini-api/docs/changelog)
- **Notes**: —

## Google

- Source report line: `336`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Google
- **Alias / endpoint identifier**: `gemini-3-pro-preview`
- **Kind**: endpoint name reused as an alias after shutdown
- **Resolves to**: Gemini 3 Pro until [Mar 9, 2026](https://ai.google.dev/gemini-api/docs/deprecations); thereafter "`gemini-3-pro-preview` now points to `gemini-3.1-pro-preview`" ([changelog](https://ai.google.dev/gemini-api/docs/changelog))
- **Valid from**: [Nov 18, 2025](https://ai.google.dev/gemini-api/docs/deprecations)
- **Valid to**: identity change [Mar 9, 2026](https://ai.google.dev/gemini-api/docs/changelog)
- **Source of the mapping**: [Changelog](https://ai.google.dev/gemini-api/docs/changelog)
- **Notes**: **Highest-risk identity trap in this report:** one string, two models, boundary 2026-03-09.

## Google

- Source report line: `337`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Google
- **Alias / endpoint identifier**: `gemini-3.1-pro-preview-customtools`
- **Kind**: second endpoint on one model
- **Resolves to**: Gemini 3.1 Pro, tuned to prioritize custom tools
- **Valid from**: [Feb 19, 2026](https://ai.google.dev/gemini-api/docs/changelog)
- **Valid to**: → present
- **Source of the mapping**: [Model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview)
- **Notes**: Endpoint-level variation without a new model.

## Google

- Source report line: `338`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Google
- **Alias / endpoint identifier**: `gemini-3.1-flash-image` ↔ "Nano Banana 2"; `gemini-3.1-flash-lite-image` ↔ "Nano Banana 2 Lite"; `gemini-3-pro-image` ↔ "Nano Banana Pro"; `gemini-2.5-flash-image` ↔ "Nano Banana"
- **Kind**: marketing-name ↔ endpoint aliases
- **Resolves to**: as shown
- **Valid from**: GA dates in §2c
- **Valid to**: → present
- **Source of the mapping**: [Models](https://ai.google.dev/gemini-api/docs/models)
- **Notes**: Marketing version numbers and endpoint version numbers deliberately differ.

## Google

- Source report line: `339`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Google
- **Alias / endpoint identifier**: `gemini-live-2.5-flash-native-audio` (Cloud) ↔ `gemini-2.5-flash-native-audio-preview-12-2025` (Gemini API)
- **Kind**: cross-surface endpoint names for one model
- **Resolves to**: Gemini 2.5 Flash native audio
- **Valid from**: [Dec 12, 2025](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions)
- **Valid to**: Cloud retirement [Dec 13, 2026](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions)
- **Source of the mapping**: [Cloud lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions) · [Models](https://ai.google.dev/gemini-api/docs/models)
- **Notes**: Same model, two identifier namespaces.

## Google

- Source report line: `340`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Google
- **Alias / endpoint identifier**: `veo-3.1-generate-preview` (Gemini API) ↔ `veo-3.1-generate-001` (Cloud)
- **Kind**: cross-surface identifiers
- **Resolves to**: Veo 3.1
- **Valid from**: [Oct 15, 2025](https://ai.google.dev/gemini-api/docs/deprecations) / [Nov 17, 2025](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions)
- **Valid to**: Cloud "November 17, 2026 or later"
- **Source of the mapping**: [Cloud lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions)
- **Notes**: Preview vs GA status differs by surface.

## Google

- Source report line: `341`
- Research section: 3. Alias and endpoint-identifier table, with validity intervals
- **Provider**: Google
- **Alias / endpoint identifier**: `imagen-4.0-generate`
- **Kind**: catalog alias
- **Resolves to**: Imagen 4 generate family
- **Valid from**: not_reported
- **Valid to**: GA IDs shut down [Aug 17, 2026](https://ai.google.dev/gemini-api/docs/deprecations)
- **Source of the mapping**: [Models](https://ai.google.dev/gemini-api/docs/models)
- **Notes**: Listed in the catalog as "Imagen 4 (Deprecated)".
- **Typed absences**: `not_reported`
