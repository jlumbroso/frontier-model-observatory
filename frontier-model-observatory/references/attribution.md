# Conversation attribution protocol

## Goal

Estimate which model or deployment could have produced a conversation while
keeping model identity, timestamp integrity, product routing, and stylistic
evidence separate.

## Procedure

1. Preserve the supplied transcript and metadata unchanged.
2. Identify all explicit model names, API identifiers, product surfaces,
   timestamps, tools, modalities, and self-descriptions.
3. Build candidates from models actually available through the stated product
   and date.
4. Apply hard constraints:
   - release and availability interval;
   - endpoint existence;
   - supported modalities and tools;
   - product naming used at that time;
   - documented routing or model substitution.
5. Test metadata corruption separately:
   - wrong model label;
   - wrong conversation date;
   - migration/export rewrite;
   - per-message model changes;
   - product alias replacing the underlying model.
6. Apply softer evidence only after hard constraints:
   - disclosed knowledge cutoff;
   - system-prompt phrases;
   - refusal and formatting behavior;
   - characteristic capabilities;
   - prose style.
7. Return candidates, exclusions, evidence weights, and residual uncertainty.

## Evidence weights

- **Very strong**: model did not exist; endpoint unavailable; impossible
  modality; cryptographically or platform-authenticated per-message model ID.
- **Strong**: official product availability, exact system-prompt phrase,
  contemporaneous API model identifier.
- **Moderate**: feature behavior unique during a bounded interval, disclosed
  knowledge cutoff, routing documentation.
- **Weak**: prose style, tone, formatting preference, self-reported identity
  without corroboration.

Never turn style into certainty. A chronological impossibility may indicate a
bad timestamp rather than a bad model label; evaluate both hypotheses.

## Output

For each candidate report:

- temporal viability;
- product/endpoint viability;
- supporting and conflicting evidence;
- confidence as an observatory inference;
- falsifier or evidence that would change the ranking.

Use "indeterminate" when surviving candidates cannot be separated responsibly.
