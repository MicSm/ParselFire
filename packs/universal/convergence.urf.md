# Universal Convergence Leaf

## KERNELS

```text
UNI-K42|stage=6|scope=canonical-surface-cutover|kernel=once a replacement registry or keyed configuration surface is established stop translating legacy singleton knobs and helper entrypoints into it and make the canonical surface the only runtime source of truth
UNI-K43|stage=6|scope=canonical-entrypoint-retirement|kernel=once one discovery or implementation entrypoint is canonical remove deprecated alternate entrypoints instead of keeping aliases or override hooks that only preserve legacy selection
UNI-K44|stage=6|scope=baseline-shim-retirement|kernel=when the supported runtime floor now guarantees the replacement primitive delete feature flags compatibility branches and shim exceptions so every caller runs through the same baseline path
```

## EXCLUDES

```text
UNI-X42|stage=6|scope=legacy-surface-dual-read|violation=do not keep legacy settings names helper factories or translation glue alive after the replacement registry already owns the runtime contract
UNI-X43|stage=6|scope=alternate-entrypoint-retention|violation=do not keep alias entrypoints or override escape hatches after the system has converged on one canonical discovery or implementation path
UNI-X44|stage=6|scope=post-floor-compat-branch|violation=do not keep legacy-mode switches version-floor shims or compatibility exceptions after the supported runtime already guarantees the replacement behavior
```
