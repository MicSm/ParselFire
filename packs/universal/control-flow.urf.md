# Universal Control-Flow Leaf

## KERNELS
UNI-K08|stage=1|scope=exceptional-path-retention|kernel=keep genuinely special or protocol-specific paths explicit when a generic handler would erase distinct state or sequencing rules
UNI-K09|stage=1|scope=completion-marker|kernel=preserve stream or protocol completion semantics under partial failure by emitting an explicit terminator instead of treating silence as success
UNI-K10|stage=1|scope=helper-surface-tightening|kernel=narrow related helper types and mutable surfaces when that makes a lifecycle or ownership invariant obvious without widening the change
UNI-K11|stage=1|scope=monotonic-elapsed-time|kernel=use a monotonic clock for elapsed-time and liveness logic and handle drift or desync explicitly
UNI-K12|stage=1|scope=shadow-free-outputs|kernel=assign directly into the output variable that must survive a guard and avoid same-named locals inside the guarded block
UNI-K16|stage=2|scope=explicit-init-outcomes|kernel=model unavailable already-active retryable and failed states explicitly instead of letting initialization report them as defaults or implicit success
UNI-K17|stage=2|scope=typed-lookup-result|kernel=return a structured lookup result when not-found unchanged remapped and out-of-range are all meaningful outcomes
UNI-K18|stage=2|scope=retry-terminal-separation|kernel=separate retryable continuation from terminal failure as distinct outcomes
UNI-K19|stage=2|scope=success-first-loop|kernel=shape retry loops around an explicit success branch and normalize final output only after success actually happened

## EXCLUDES
UNI-X08|stage=1|scope=special-case-flattening|violation=do not flatten real special cases or protocol-specific branches into generic code that erases their distinct rules
UNI-X09|stage=1|scope=implicit-stream-end|violation=do not treat absence of further output as an implicit completion signal because partial failure then becomes indistinguishable from success
UNI-X10|stage=1|scope=loose-helper-surface|violation=do not leave helper types and mutable surfaces broader than the real invariant when narrowing them would make the contract obvious
UNI-X11|stage=1|scope=wall-clock-elapsed|violation=do not use wall-clock APIs for elapsed-time or liveness checks because clock jumps create false timeouts and false freshness
UNI-X12|stage=1|scope=shadowed-output-local|violation=do not redeclare a same-named local inside a guarded block when an outer output variable must carry the result afterward
UNI-X16|stage=2|scope=false-success-defaults|violation=do not report initialization or transport failure as a default-constructed domain value or as implicit success
UNI-X17|stage=2|scope=lookup-sentinel-collapse|violation=do not collapse distinct lookup outcomes into one bool null or numeric sentinel
UNI-X18|stage=2|scope=generic-retry-collapse|violation=do not route transient retryable conditions and terminal failures through one generic retry path that erases the real outcome contract
UNI-X19|stage=2|scope=interleaved-retry-flow|violation=do not mix success normalization retry continuation and terminal recovery into one undifferentiated control flow
