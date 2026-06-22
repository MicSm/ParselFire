# Python Boundaries-Cleanup Leaf

## KERNELS

```text
PY-K17|stage=5|scope=inert-cross-process-payloads|kernel=across Python process boundaries pass inert metadata or type-tag-plus-kwargs and reconstruct behavior in the owning runtime
PY-K18|stage=5|scope=dedicated-schema-definitions|kernel=represent serialized payloads with dedicated low-level schema classes and keep them separate from live runtime classes
PY-K19|stage=5|scope=typed-protocol-frames|kernel=model protocol frames as strict discriminated schemas with validators for version capability and payload invariants
PY-K20|stage=5|scope=stable-sdk-import-surface|kernel=keep author-facing constructs on stable public SDK paths and hide implementation-only helpers under _internal
PY-K29|stage=5|scope=registry-backed-extension-resolution|kernel=for serialized extension points resolve custom classes through an explicit plugin registry instead of importing dotted class paths from payloads at deserialization time
PY-K21|stage=6|scope=post-convergence-cleanup|kernel=after moving a runtime concern to a new owner delete mirrored policy bridges and fallback serializers from the old owner
PY-K22|stage=6|scope=legacy-surface-retirement|kernel=after shipping a replacement API, config, or CLI surface remove legacy entrypoints, flags, and tests on schedule
```

## EXCLUDES

```text
PY-X17|stage=5|scope=pickled-live-objects|violation=do not pickle live runtime objects or invoke plugin methods inside passive services to recover cross-process behavior
PY-X18|stage=5|scope=shared-layer-hierarchies|violation=do not make client, server, or serialized models share live runtime classes or one mutable schema hierarchy
PY-X19|stage=5|scope=dict-shaped-protocol|violation=do not represent protocol messages as loose dicts that leave version capability and payload invariants to scattered handler code
PY-X20|stage=5|scope=accidental-public-internals|violation=do not leak internal helpers onto public import paths or require extensions to depend on concrete runtime context classes
PY-X29|stage=5|scope=payload-driven-class-import|violation=do not let serialized payloads drive direct dotted-class imports for custom extension resolution and assume whatever is importable is registered and supported
PY-X21|stage=6|scope=post-convergence-residuals|violation=do not leave compatibility bridges or fallback serializers in superseded owners after convergence
PY-X22|stage=6|scope=permanent-dual-surface|violation=do not keep legacy and replacement APIs settings or CLI surfaces alive indefinitely once one can become canonical
```
