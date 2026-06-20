# C++ State-Outcome Modeling Leaf

## KERNELS
CPP-K19|stage=2|scope=explicit-result-channels|kernel=model identifiers metadata and auxiliary outputs as explicit return or callback data instead of globals or side-band registers
CPP-K20|stage=2|scope=check-only-load-mode|kernel=give untrusted persistence formats a check-only load mode for validation without instantiating live runtime state
CPP-K21|stage=2|scope=category-indexed-quantities|kernel=represent per-category quantities as arrays or maps keyed by category instead of fixed numbered slots when the category set can grow
CPP-K49|stage=2|scope=probe-result-channel|kernel=for best-effort metadata or diagnostics probes return explicit value-or-error results so callers can handle one probe failure locally and continue the wider scan
CPP-K50|stage=2|scope=nullable-observation-fields|kernel=when diagnostic or probe fields can be unavailable represent that state explicitly with nullable or unknown outputs instead of coercing it to false zero or empty values
CPP-K51|stage=2|scope=exclusive-payload-variant|kernel=model mutually exclusive payload shapes as a tagged union with per-case visitors instead of one record that stores inactive branches and manual skip bookkeeping
CPP-K52|stage=2|scope=state-tag-equality|kernel=when one abstraction has multiple internal state representations carry the representation tag through equality hashing and cache keys so distinct states cannot alias

## EXCLUDES
CPP-X19|stage=2|scope=global-result-sidechannels|violation=do not hide secondary results in globals or out-of-band registers when they can be explicit return or callback data
CPP-X20|stage=2|scope=validation-through-full-load|violation=do not require a full runtime load or crash on malformed data just to verify whether persisted state is readable
CPP-X21|stage=2|scope=fixed-multislot-acceptance|violation=do not model extensible category data as hardcoded fields or numbered slots that require special cases for each new type
CPP-X49|stage=2|scope=throwing-probe-control-flow|violation=do not make optional metadata or diagnostics probes signal routine unavailability only by throwing and abort a wider scan that could continue with partial results
CPP-X50|stage=2|scope=defaulted-unknown-fields|violation=do not collapse unavailable diagnostic fields into ordinary false zero or empty values that look like real observations
CPP-X51|stage=2|scope=baggy-payload-struct|violation=do not pack mutually exclusive payload layouts into one struct with inactive fields skip counters or branch-specific bookkeeping
CPP-X52|stage=2|scope=variant-blind-equality|violation=do not treat distinct state representations as equal just because their function name parameters or payload types match
