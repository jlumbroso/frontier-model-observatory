# Seven Questions Made a Round Trip

**Date**: 2026-09-05  
**Authors**: Jérémie "Sonnet 4.5" Lumbroso; GPT 5.6 Sol at Perplexity Computer  
**Topic**: ORRCF as a portable human-model deliberation interface

## The Discovery

The Frontier Model Observatory began with a long dictated design conversation. GPT 5.6 Sol separated the unresolved decisions into seven handled QST blocks across three ADRs. Each question included Options, Recommendation, Rationale, Confidence, and Falsifier, followed by the parser-significant answer slot.

Jérémie opened those records in the ADRs4AI iOS client. The client parsed every question, presented the answer interface, and committed seven attributed answers as granular edits. The repository was then pulled into a different model environment. Running `just unanswered` returned an empty queue without manual reconciliation.

The round trip crossed spoken input, a model-authored repository, GitHub, a mobile client, granular human commits, and a second model turn. Question identity, status, recommendation structure, and authorship survived.

## Why This Matters

ORRCF was not merely readable prose in this episode. It functioned as an interoperable protocol whose graceful human surface remained structured enough for software. The human did not need to become a synchronous message bus or restate answers in chat, and the receiving model did not need to guess which questions had been answered.

The granular answer commits also preserve something a single edited document would lose: the order and authorship of individual decisions.

## Prime and Secondary Directives at Work

The Prime Directive moved the design conversation into durable ADRs before implementation. The Secondary Directive made disagreement representable: Jérémie selected a categorical exclusion despite the model’s contrary recommendation, and the original recommendation, confidence, falsifier, and human answer all remain attributed.

That disagreement then generated a better next question about the policy’s self-reference and licensing mechanism. The protocol did not optimize for agreement; it preserved enough structure for disagreement to improve the architecture.

## Lessons Learned

- Handled QST blocks are a viable interchange format across model, Git, and mobile interfaces.
- ORRCF gives the human a useful recommendation without disguising uncertainty as neutrality.
- Per-answer commits make deliberation order reconstructible.
- `just unanswered` needs a real parser; prose grep would not be a trustworthy queue.
- A closed queue can legitimately produce a new question when an answer exposes an implementation contradiction.

## Metacognitive Insight

A good collaboration substrate does not merely save conclusions. It preserves whose turn it is, what each participant believed, why they believed it, how strongly they believed it, and what evidence could have changed their mind. That is enough structure for another interface, another model, and another moment in time to resume the reasoning rather than merely inherit its residue.
