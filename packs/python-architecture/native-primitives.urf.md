# Python Native-Primitives Leaf

## KERNELS
PY-K23|stage=0|scope=native-cache-decorators|kernel=for stable in-process Python lookups prefer the standard callable-cache decorators over project-local memoize wrappers or parallel cache dicts so invalidation and introspection stay on the callable itself
PY-K24|stage=0|scope=standard-replace-protocol|kernel=when Python objects are conceptually immutable records expose the standard replace protocol so call sites can express updates as structural replacement instead of replaying constructors
PY-K25|stage=0|scope=explicit-hotpath-dunders|kernel=for hot-path proxy or value classes spell out the small comparison dunders explicitly instead of using class decorators that synthesize them during class construction
PY-K26|stage=0|scope=targeted-wrapper-metadata|kernel=when generating framework entry callables copy only the metadata and decorator flags the runtime actually needs instead of applying full wrapper emulation that rewrites callable identity
PY-K27|stage=0|scope=format-boundary-sanitizers|kernel=when a stdlib date or datetime type is correct except for a platform formatting edge sanitize the format string at the boundary instead of wrapping the value in a shadow type

## EXCLUDES
PY-X23|stage=0|scope=project-local-cache-shims|violation=do not build custom memoize decorators or side cache registries for stable Python lookups when the standard cache decorators already provide the needed semantics and cache-clear hooks
PY-X24|stage=0|scope=constructor-replay-updates|violation=do not scatter constructor replays or bespoke clone helpers across call sites when the real model is an immutable record with a few field substitutions
PY-X25|stage=0|scope=decorator-generated-dunders|violation=do not put convenience decorators on hot-path proxy types when they generate comparison dunders you could define directly and add hidden class-construction cost
PY-X26|stage=0|scope=wrapper-identity-spoofing|violation=do not apply wrapper helpers to synthetic entry callables that are not true wrappers and thereby inherit signature or __wrapped__ semantics from a different callable
PY-X27|stage=0|scope=shadow-type-format-fixes|violation=do not introduce shadow date or datetime wrappers just to paper over platform strftime quirks when a boundary format sanitizer preserves the native type
