# C++ Shared-Abstractions Leaf

## KERNELS
CPP-K31|stage=4|scope=alloc-wrapper-abstraction|kernel=once alignment or tagging invariants live in a shared allocation wrapper route relevant allocations through it
CPP-K32|stage=4|scope=raii-wrapper-vocabulary|kernel=prefer a small shared vocabulary of RAII wrappers over bespoke cleanup helpers
CPP-K33|stage=4|scope=view-input-owned-output|kernel=favor view-based inputs and owned outputs over shared scratch state and bool-plus-out-param contracts
CPP-K34|stage=4|scope=trailing-payload-accessor|kernel=factor shared trailing-payload byte-range logic into one constrained helper
CPP-K35|stage=4|scope=handle-validity-trait|kernel=encode handle-validity rules in shared wrapper traits so callers test wrapper validity centrally
CPP-K36|stage=4|scope=owner-direct-access|kernel=inside an owning class use direct member access instead of re-fetching its own published accessor

## EXCLUDES
CPP-X31|stage=4|scope=raw-alloc-bypass|violation=do not bypass a shared allocation wrapper where alignment or tagging policy is supposed to be centralized
CPP-X32|stage=4|scope=bespoke-cleanup-scatter|violation=do not invent one-off cleanup helpers or scattered scope-exit patterns when shared RAII wrappers can encode the policy once
CPP-X33|stage=4|scope=shared-scratch-outparams|violation=do not keep enrichment helpers on shared mutable scratch state with bool-plus-out-params when view-based input and owned output semantics are available
CPP-X34|stage=4|scope=repeated-trailing-arithmetic|violation=do not repeat pointer arithmetic for similar trailing-payload layouts once the byte-range contract is understood
CPP-X35|stage=4|scope=scattered-handle-validity|violation=do not scatter raw invalid-handle sentinel checks through call sites when wrapper traits can encode validity centrally
CPP-X36|stage=4|scope=self-canonical-relookup|violation=do not re-fetch a class's own published accessor from inside the owning class when direct member access already exists
