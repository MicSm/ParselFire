# Universal Pack Index

Language-agnostic runtime entry surface for ParselFire.

## STAGES
S00|name=scope-and-need|question=should this be built at all and what is the smallest correct move
S01|name=contracts-and-invariants|question=what exact contract invariant or special case must not be violated
S02|name=state-and-outcome-modeling|question=are all meaningful states outcomes and retries represented explicitly
S03|name=ownership-and-lifecycle|question=who owns this state resource or registration and how is start stop teardown modeled
S04|name=shared-abstractions|question=is a shared invariant now clear enough to extract into a reusable abstraction or boundary normalizer
S05|name=boundaries-and-plumbing|question=are subsystem boundaries explicit and are first-class semantics threaded end to end
S06|name=convergence-and-deletion|question=once the replacement model is proven has the old path been fully removed from runtime and build surfaces

## ROUTING
R01|leaf=foundations.urf.md|signals=smallest,stdlib,dependency,contract,test
R02|leaf=control-flow.urf.md|signals=special-case,outcome,retry,lookup,completion,clock
R03|leaf=lifecycle.urf.md|signals=owner,lifecycle,publish,rebuild,transition,teardown
R04|leaf=shared-abstractions.urf.md|signals=shared,extract,duplicate,trampoline,context,parameterize
R05|leaf=boundaries.urf.md|signals=boundary,capability,artifact,normalize,transport,plumbing

## LEAVES
L01|file=foundations.urf.md|theme=scope-contracts
L02|file=control-flow.urf.md|theme=control-flow-outcomes
L03|file=lifecycle.urf.md|theme=ownership-lifecycle
L04|file=shared-abstractions.urf.md|theme=shared-invariants
L05|file=boundaries.urf.md|theme=boundaries-plumbing
