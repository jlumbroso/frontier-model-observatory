# Canonical Repository Exclusion Policy

## Policy

The canonical Frontier Model Observatory does not collect, describe, index,
summarize, compare, quote, or archive Meta Platforms, Meta AI, Llama, or their
related models, weights, products, releases, and events.

This is a repository-governance choice grounded in the project owner’s ethical
judgment. It is not an additional condition on the MIT License.

## Narrow Governance Exception

The excluded subject may appear only where necessary to define, preserve,
test, or audit this policy:

- this policy;
- ADR-0002 and its originating human answer;
- the machine-readable exclusion configuration;
- regression tests for the exclusion checker;
- immutable Git history that predates or records adoption of the policy.

The exception does not permit ordinary corpus records, source quotations,
comparisons, chronology entries, attribution candidates, prompts, artifacts,
generated views, examples, or marketing references.

## Enforcement

`just check-exclusions` scans candidate repository text and filenames using
the patterns in `policy/exclusions.json`. `just verify` includes that check and
is the required local and CI gate.

The checker is a backstop, not a complete semantic oracle. Reviewers must also
reject indirect or newly named excluded material that a finite term list does
not yet recognize. When the checker misses a real case, add a regression test
and extend the configuration.

## Forks

Downstream forks are requested to preserve this exclusion. The project does
not represent that request as a restriction imposed by the MIT License.
