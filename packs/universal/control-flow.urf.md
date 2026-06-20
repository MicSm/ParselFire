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
UNI-K33|stage=2|scope=bounded-retry-hint|kernel=derive retry delays from live contention but cap the reported interval so burst debt or one slow holder cannot turn transient throttling into effectively permanent backoff
UNI-K34|stage=2|scope=fresh-visibility-retry|kernel=when a read-then-write decision can lose a race against concurrent writers rerun the whole decision in a fresh transaction before treating a uniqueness conflict as terminal
UNI-K46|stage=2|scope=deterministic-concurrent-merge|kernel=when concurrent writers update shared state through a merge operation make the merge semantics explicit and deterministic using either a commutative reducer or a stable merge order so live execution and recovery replay produce the same result
UNI-K47|stage=2|scope=retryable-timeout-type|kernel=represent retryable operational timeouts as a distinct failure type so retry policies can discriminate them from terminal failures without inspecting error messages
UNI-K48|stage=2|scope=return-vs-continuation|kernel=when a unit of work persists continuation state separate the caller-visible result from the saved continuation state so callers and recovery logic operate on independent contracts
UNI-K51|stage=2|scope=stable-retry-identity|kernel=when retrying a partial batch track each item by its original input identity and rebuild outputs from that stable mapping instead of indexing by position in the shrinking retry subset

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
UNI-X33|stage=2|scope=unbounded-retry-hint|violation=do not let aggregate contention metrics emit unbounded retry delays that strand callers in excessive backoff after a brief burst or one long-running holder
UNI-X34|stage=2|scope=stale-view-conflict-finalization|violation=do not classify a uniqueness conflict as final when the failing write was based on pre-commit reads that may be stale relative to concurrent writers
UNI-X46|stage=2|scope=order-dependent-concurrent-merge|violation=do not let concurrent state merges depend on incidental writer ordering or opaque merge sequencing that differs between live execution and recovery replay
UNI-X47|stage=2|scope=terminalized-timeout|violation=do not classify retryable operational timeouts under broad terminal failure hierarchies that retry policies cannot distinguish without inspecting error content
UNI-X48|stage=2|scope=conflated-return-state|violation=do not use one object as both the caller-visible return value and the persisted continuation state
UNI-X51|stage=2|scope=shrinking-retry-index|violation=do not track retry results by their position in the current shrinking attempt subset because position shifts as items succeed and the output ordering corrupts
