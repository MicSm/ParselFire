# Universal Shared-Abstractions Leaf

## KERNELS
UNI-K24|stage=4|scope=shared-invariant-extraction|kernel=when multiple paths repeat the same conversion normalization or validation rule extract the shared invariant into one implementation while keeping truly distinct cases explicit
UNI-K25|stage=4|scope=trampoline-elimination|kernel=remove pass-through layers that only forward calls and add no lifecycle ownership or error-boundary semantics
UNI-K26|stage=4|scope=foundation-first-upgrade|kernel=when a subsystem needs stronger ownership or value semantics improve the shared utility or foundation layer first
UNI-K27|stage=4|scope=explicit-context-threading|kernel=when the caller already has the owning context pass it through helpers and factories explicitly instead of re-fetching it from a global inside callees
UNI-K28|stage=4|scope=parameterized-duplicates|kernel=collapse copy-pasted workflow variants into one parameterized implementation when their differences are stable inputs or policies
UNI-K36|stage=4|scope=divergent-contract-resistance|kernel=when related types share surface structure but diverge in error handling ownership or lifecycle resist unifying them under one base and keep separate implementations until a genuinely shared contract emerges
UNI-K37|stage=4|scope=hook-locality|kernel=despite surface similarity in surrounding setup keep variant-specific collaborator selection on the owning type behind overridable hooks so downstream variants can customize one step without forking the shared initialization

## EXCLUDES
UNI-X24|stage=4|scope=repeated-invariant-inline|violation=do not keep duplicating the same conversion normalization validation or pointer-shape rule once the shared invariant is understood
UNI-X25|stage=4|scope=vestigial-delegation|violation=do not keep thin trampoline layers that only forward calls and add no ownership lifecycle or error-boundary semantics
UNI-X26|stage=4|scope=local-workaround-foundations|violation=do not encode local workarounds where the missing fix belongs in shared utility or foundation code
UNI-X27|stage=4|scope=implicit-context-global|violation=do not reach into globals from helpers to recover an owning context that could have been passed explicitly
UNI-X28|stage=4|scope=copy-paste-variants|violation=do not keep copy-pasted workflow variants once their differences can be expressed as parameters or bounded hooks
UNI-X36|stage=4|scope=forced-common-base|violation=do not unify types under one base when their contracts diverge in error handling ownership or lifecycle because the resulting hierarchy will require brittle overrides or fake support from non-conforming members
UNI-X37|stage=4|scope=override-bypassing-hoist|violation=do not hoist variant extension points into module-level helpers or hard-wired collaborators despite similar surrounding setup when it forces downstream variants to fork the shared initialization just to customize one step
