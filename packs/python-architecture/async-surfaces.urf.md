# Python Async-Surfaces Leaf

## KERNELS
PY-K01|stage=1|scope=async-unsafe-guards|kernel=mark blocking or thread-bound operations async-unsafe and fail fast in coroutine contexts so callers must bridge them explicitly
PY-K12|stage=4|scope=ast-contract-lints|kernel=encode framework-visible import call and module-structure rules as repo-local AST lints instead of review-only conventions
PY-K13|stage=4|scope=native-sync-async-paths|kernel=share neutral mechanics in a base layer but keep distinct sync and async entry points or engines
PY-K14|stage=4|scope=lifecycle-entrypoint-tests|kernel=exercise setup migration and unload through public lifecycle entrypoints in tests and checks rather than calling component internals directly
PY-K15|stage=5|scope=explicit-context-propagation|kernel=capture the required ambient context explicitly when Python crosses thread-pool process or engine boundaries and rehydrate it in the target runtime
PY-K16|stage=5|scope=thread-sensitive-bridges|kernel=route connection-bound sync hooks through thread-sensitive bridges owned by the current request rather than a shared generic executor

## EXCLUDES
PY-X01|stage=1|scope=unguarded-sync-in-async|violation=do not let coroutine code call sync-only resource methods directly and fail later through hidden blocking or thread misuse
PY-X12|stage=4|scope=review-only-framework-rules|violation=do not rely on reviewer memory or out-of-band checks for architecture contracts that a custom Python AST lint can detect at author time
PY-X13|stage=4|scope=mixed-mode-engines|violation=do not force sync and async execution through one path that mixes blocking and awaitable lifecycle logic or fakes async with wrappers over sync internals
PY-X14|stage=4|scope=internal-lifecycle-test-calls|violation=do not test setup migration or unload by calling component internals directly and bypassing the public lifecycle entrypoints
PY-X15|stage=5|scope=assumed-context-propagation|violation=do not launch thread-pool subprocess or remote engine work assuming in-memory context objects or contextvars will propagate automatically
PY-X16|stage=5|scope=generic-sync-bridges|violation=do not schedule connection-bound sync middleware or lifecycle hooks on arbitrary worker threads or a global sync lane
