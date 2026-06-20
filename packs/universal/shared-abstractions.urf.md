# Universal Shared-Abstractions Leaf

## KERNELS
UNI-K24|stage=4|scope=shared-invariant-extraction|kernel=when multiple paths repeat the same conversion normalization or validation rule extract the shared invariant into one implementation while keeping truly distinct cases explicit
UNI-K25|stage=4|scope=trampoline-elimination|kernel=remove pass-through layers that only forward calls and add no lifecycle ownership or error-boundary semantics
UNI-K26|stage=4|scope=foundation-first-upgrade|kernel=when a subsystem needs stronger ownership or value semantics improve the shared utility or foundation layer first
UNI-K27|stage=4|scope=explicit-context-threading|kernel=when the caller already has the owning context pass it through helpers and factories explicitly instead of re-fetching it from a global inside callees
UNI-K28|stage=4|scope=parameterized-duplicates|kernel=collapse copy-pasted workflow variants into one parameterized implementation when their differences are stable inputs or policies

## EXCLUDES
UNI-X24|stage=4|scope=repeated-invariant-inline|violation=do not keep duplicating the same conversion normalization validation or pointer-shape rule once the shared invariant is understood
UNI-X25|stage=4|scope=vestigial-delegation|violation=do not keep thin trampoline layers that only forward calls and add no ownership lifecycle or error-boundary semantics
UNI-X26|stage=4|scope=local-workaround-foundations|violation=do not encode local workarounds where the missing fix belongs in shared utility or foundation code
UNI-X27|stage=4|scope=implicit-context-global|violation=do not reach into globals from helpers to recover an owning context that could have been passed explicitly
UNI-X28|stage=4|scope=copy-paste-variants|violation=do not keep copy-pasted workflow variants once their differences can be expressed as parameters or bounded hooks
