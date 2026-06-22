# Universal Pack Guide

This file is NOT intended for LLM consumption. Human-readable guide only.

The universal family defines the shared stage pipeline that every other pack family plugs into.

Legend: `id | stage | scope | rule` means a stable record id, stage number, short scope label, and the kernel or violation text carried by that record.

## Files

- `pack.urf.md`: the shared S00-S06 stage pipeline, route signals, and leaf registry
- `foundations.urf.md`: S00-S01 scope control, contracts, and proof obligations
- `control-flow.urf.md`: S01-S02 outcomes, retries, completion, and control-flow constraints
- `lifecycle.urf.md`: S03 ownership, publication, teardown, and rebuild invariants
- `shared-abstractions.urf.md`: S04 DRY and shared-invariant refactors after semantics are clear
- `boundaries.urf.md`: S05 subsystem boundaries, transport, logging, and migration behavior
- `convergence.urf.md`: S06 cleanup, retirement, and displaced-layer removal

## Reading Tip

Start at `pack.urf.md` when you want the stage order. Open a leaf file when you want the concrete `K` and `X` records behind one stage or seam.
