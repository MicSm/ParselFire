# Universal Lifecycle Leaf

## KERNELS
UNI-K20|stage=3|scope=narrow-init-window|kernel=make the window between construction and fully valid state as small as possible so callers cannot observe a half-wired object
UNI-K21|stage=3|scope=ownership-state-centralization|kernel=place lifecycle-sensitive mutable state and teardown responsibility under a clear owner instead of scattering them across globals frees and scratch state
UNI-K22|stage=3|scope=rebuild-then-swap|kernel=build replacement state in an owned temporary and publish it only after successful completion
UNI-K23|stage=3|scope=explicit-lifecycle-state|kernel=model cross-thread or cross-process lifecycle with explicit states and transitions

## EXCLUDES
UNI-X20|stage=3|scope=half-configured-publication|violation=do not expose objects while setup still allows callers to observe a partially configured intermediate state
UNI-X21|stage=3|scope=scattered-lifecycle-state|violation=do not spread lifecycle-sensitive state ownership and cleanup across globals ad-hoc frees and scratch buffers with no clear owner
UNI-X22|stage=3|scope=partial-live-mutation|violation=do not mutate live structures through half-built intermediate states when rebuild-then-swap is available
UNI-X23|stage=3|scope=sticky-lifecycle-flags|violation=do not model lifecycle with sticky global bools detached threads or destructor side effects when explicit states and transitions are required
