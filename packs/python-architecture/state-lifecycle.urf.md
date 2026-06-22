# Python State-Lifecycle Leaf

## KERNELS

```text
PY-K03|stage=2|scope=typed-runtime-carriers|kernel=model runtime state and cached API snapshots with typed dataclasses and typed keys so state shape is explicit and refactors stay local
PY-K04|stage=2|scope=setup-exception-taxonomy|kernel=model async setup with distinct retryable not-ready fatal and reauth-required failures so the orchestrator can recover correctly
PY-K05|stage=3|scope=typed-entry-runtime|kernel=store per-instance live clients coordinators and listeners on a typed entry-owned runtime object instead of shared nested registries
PY-K09|stage=3|scope=task-local-context|kernel=store ambient execution context in task-aware locals and reserve plain thread locals for resources that are truly thread-bound
PY-K10|stage=3|scope=structured-request-cleanup|kernel=run disconnect watchers and response work inside one cancellation domain with a guaranteed cleanup exit path
PY-K11|stage=3|scope=refresh-domain-sharding|kernel=give resources with different cadence freshness or failure isolation their own coordinators or refresh loops even when they share a client
```

## EXCLUDES

```text
PY-X03|stage=2|scope=string-key-runtime-state|violation=do not shuttle loosely shaped dicts or parallel string-key entries through integration code when a typed carrier can express the real state
PY-X04|stage=2|scope=collapsed-setup-failures|violation=do not collapse transient fatal and reauthable setup failures into one generic exception or boolean result
PY-X05|stage=3|scope=global-dict-entry-state|violation=do not scatter per-entry runtime objects across global dicts keyed by domain and id and recover them through string lookups
PY-X09|stage=3|scope=thread-local-async-context|violation=do not keep request locale URL or similar ambient context in plain thread locals once code can cross await boundaries
PY-X10|stage=3|scope=cancellation-leak-lifecycle|violation=do not let disconnect or cancellation bypass response cleanup or final lifecycle signaling through ad hoc task management
PY-X11|stage=3|scope=multi-domain-single-coordinator|violation=do not make one coordinator own resources with different cadence freshness rules or failure domains just because they share a client
```
