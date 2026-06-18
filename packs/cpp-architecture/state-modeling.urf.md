# C++ State-Outcome Modeling Leaf

## KERNELS
CPP-K19|stage=2|scope=explicit-result-channels|kernel=model identifiers metadata and auxiliary outputs as explicit return or callback data instead of globals or side-band registers
CPP-K20|stage=2|scope=check-only-load-mode|kernel=give untrusted persistence formats a check-only load mode for validation without instantiating live runtime state
CPP-K21|stage=2|scope=category-indexed-quantities|kernel=represent per-category quantities as arrays or maps keyed by category instead of fixed numbered slots when the category set can grow

## EXCLUDES
CPP-X19|stage=2|scope=global-result-sidechannels|violation=do not hide secondary results in globals or out-of-band registers when they can be explicit return or callback data
CPP-X20|stage=2|scope=validation-through-full-load|violation=do not require a full runtime load or crash on malformed data just to verify whether persisted state is readable
CPP-X21|stage=2|scope=fixed-multislot-acceptance|violation=do not model extensible category data as hardcoded fields or numbered slots that require special cases for each new type
