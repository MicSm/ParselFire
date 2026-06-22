# Universal Lifecycle Leaf

## KERNELS

```text
UNI-K20|stage=3|scope=narrow-init-window|kernel=make the window between construction and fully valid state as small as possible so callers cannot observe a half-wired object
UNI-K21|stage=3|scope=ownership-state-centralization|kernel=place lifecycle-sensitive mutable state and teardown responsibility under a clear owner instead of scattering them across globals frees and scratch state
UNI-K22|stage=3|scope=rebuild-then-swap|kernel=build replacement state in an owned temporary and publish it only after successful completion
UNI-K23|stage=3|scope=explicit-lifecycle-state|kernel=model cross-thread or cross-process lifecycle with explicit states and transitions
UNI-K49|stage=3|scope=durable-recovery-policy|kernel=express recovery as explicit policy owned by the failing unit and durably record the transition into that policy so restart resumes recovery instead of replaying the failed step
UNI-K52|stage=3|scope=latched-degradation|kernel=when failover activates record degraded mode under the owner so later calls reuse the fallback path instead of reprobing the failed primary on every invocation
```

## EXCLUDES

```text
UNI-X20|stage=3|scope=half-configured-publication|violation=do not expose objects while setup still allows callers to observe a partially configured intermediate state
UNI-X21|stage=3|scope=scattered-lifecycle-state|violation=do not spread lifecycle-sensitive state ownership and cleanup across globals ad-hoc frees and scratch buffers with no clear owner
UNI-X22|stage=3|scope=partial-live-mutation|violation=do not mutate live structures through half-built intermediate states when rebuild-then-swap is available
UNI-X23|stage=3|scope=sticky-lifecycle-flags|violation=do not model lifecycle with sticky global bools detached threads or destructor side effects when explicit states and transitions are required
UNI-X49|stage=3|scope=hidden-ephemeral-recovery|violation=do not choose recovery through transient in-memory decisions or hidden topology that vanish on crash and send restart back through the failed step
UNI-X52|stage=3|scope=stateless-primary-reprobe|violation=do not activate failover without recording degraded mode under the owner because later calls will reprobe the failed primary on every invocation
```
