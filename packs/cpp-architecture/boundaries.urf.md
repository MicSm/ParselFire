# C++ Boundaries Leaf

## KERNELS
CPP-K37|stage=5|scope=lto-cross-boundary-refs|kernel=when LTO can discard metadata-only or special-entrypoint symbols force explicit retention
CPP-K38|stage=5|scope=canonical-platform-macro|kernel=drive conditional compilation from the platform's canonical version macro rather than a shadow project-local copy
CPP-K39|stage=5|scope=domain-namespace-entry|kernel=replace vague legacy wrappers with domain-named namespaces and direct entrypoints
CPP-K40|stage=5|scope=producer-side-snapshot|kernel=when snapshot fidelity depends on producer-local state enumerate at the producer and carry an explicit snapshot marker
CPP-K41|stage=5|scope=abi-boundary-catch|kernel=at shared-library and C ABI boundaries contain C++ exceptions, log them, and convert failure into explicit status
CPP-K42|stage=5|scope=static-link-internals|kernel=when all consumers are built together prefer static link-time dependencies over internal runtime-loaded boundaries
CPP-K43|stage=5|scope=producer-output-negotiation|kernel=when a producer's output depends on consumer capabilities expose an explicit negotiation step before first consumption
CPP-K44|stage=5|scope=nested-scope-wrapping|kernel=materialize nested-scope modifiers at the exact scope boundary they affect
CPP-K45|stage=5|scope=local-global-identity|kernel=separate local instance identity from broader shared identity with distinct compare and hash modes
CPP-K46|stage=5|scope=command-payload-serialization|kernel=serialize command arguments into length-delimited schema-owned payloads so commands can evolve independently
CPP-K47|stage=5|scope=composable-stream-filters|kernel=build serialization and compression as composable filter stages reusable across files memory buffers and network sinks
CPP-K48|stage=6|scope=redundant-build-target|kernel=once a support library is always part of a parent runtime merge it into the parent and delete the standalone target

## EXCLUDES
CPP-X37|stage=5|scope=lto-silent-elimination|violation=do not assume LTO will keep metadata-only or special-entrypoint symbols
CPP-X38|stage=5|scope=shadow-version-macro|violation=do not drive platform-dependent compilation from a shadow project-local version macro that can drift from the actual target
CPP-X39|stage=5|scope=legacy-wrapper-boundary|violation=do not hide subsystem boundaries behind vague legacy wrapper layers
CPP-X40|stage=5|scope=snapshot-consumer-synthesis|violation=do not synthesize producer-local snapshot semantics in a consumer layer when fidelity depends on producer-side state
CPP-X41|stage=5|scope=abi-exception-leak|violation=do not let C++ exceptions cross a shared-library or C ABI boundary
CPP-X42|stage=5|scope=internal-dynamic-boundary|violation=do not keep a runtime-loaded boundary when all consumers build together and it only adds loader and deployment friction
CPP-X43|stage=5|scope=hidden-output-defaults|violation=do not bury output-format selection in global defaults or late caller-side conversions
CPP-X44|stage=5|scope=flattened-scope-semantics|violation=do not flatten nested-scope configuration into one global context or ad hoc arithmetic that loses scope boundaries
CPP-X45|stage=5|scope=one-identity-for-all-contexts|violation=do not reuse one equality or hash scheme for both local instance identity and broader shared or cross-process identity
CPP-X46|stage=5|scope=fixed-command-layout|violation=do not force every command through one fixed transport field layout or bolt extra meaning onto shared packet slots as schemas evolve
CPP-X47|stage=5|scope=tempfile-bound-codecs|violation=do not hard-wire codecs to one file-based sink when composable filter stages can serve memory or network too
CPP-X48|stage=6|scope=zombie-build-target|violation=do not leave a standalone build target after the code has converged into its parent runtime
