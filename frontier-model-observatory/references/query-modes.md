# Progressive query modes

## Locator

Use when the user wants a URL, card, prompt, API identifier, or quick identity.
Return the smallest resolvable entity and official locator. If several records
match, expose the ambiguity rather than selecting silently.

## Orientation

Use for an unfamiliar model name. Include:

- provider and family;
- entity kind;
- aliases or endpoint identifiers;
- release/lifecycle evidence;
- artifact availability;
- snapshot boundary and typed gaps.

## Chronology

Use for "when," "what existed," or model-generation questions. Keep date roles
separate. For historical availability, require product/deployment evidence
instead of treating an announcement as availability everywhere.

## Dossier

Use when one subject needs deep treatment. Assemble:

- identity graph;
- release and deployment events;
- artifacts and versions;
- URL/byte topology;
- prompts and governing specifications;
- claims, evaluations, corrections, and typed absences.

Read `epistemic-protocol.md`.

## Comparison

Use only after writing the comparison contract. Prefer a matrix with provider-
native values and immediate official citations. Report non-comparability as a
finding rather than forcing a winner.

## Attribution

Read `attribution.md`. Begin with hard chronology and platform constraints,
then product features and self-identification. Style is weak corroboration.

## Audit

Declare the intended universe before measuring coverage. Distinguish excluded,
out of scope, not yet collected, not found, and confirmed absent. Include the
retrieval/as-of date and next scheduled checks.

## Depth selection

Choose the shallowest mode that can resolve the user's decision. Escalate when:

- identity ambiguity affects the answer;
- revision history could change the fact;
- a quantitative comparison is requested;
- attribution has more than one chronologically viable candidate;
- a coverage claim depends on an unbounded search.
