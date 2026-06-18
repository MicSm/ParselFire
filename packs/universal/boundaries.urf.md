# Universal Boundaries Leaf

## KERNELS
UNI-K29|stage=5|scope=first-class-capability|kernel=when adding a capability thread it through real config transport persistence cache and runtime-control paths so it becomes first-class rather than a side channel
UNI-K30|stage=5|scope=stable-lookup-strategy|kernel=when artifact locations or names vary across versions match them through a stable runtime rule instead of hardcoding brittle version-shaped paths
UNI-K31|stage=5|scope=boundary-key-normalization|kernel=normalize keys at subsystem boundaries so hashing comparison and lookup all operate on one canonical representation
UNI-K32|stage=5|scope=single-responsibility-path|kernel=keep each coordinator or hot path focused on one concern and push transport policy enrichment recovery and mode switching into bounded subsystems

## EXCLUDES
UNI-X29|stage=5|scope=side-band-semantics|violation=do not bolt important behavior onto side channels when it should flow through real config transport cache or runtime-control boundaries
UNI-X30|stage=5|scope=brittle-path-matching|violation=do not hardcode unstable artifact paths or version-specific names when a stable runtime matching rule exists
UNI-X31|stage=5|scope=unnormalized-boundary-keys|violation=do not let callers cross a subsystem boundary with multiple key representations that hash compare and look up differently
UNI-X32|stage=5|scope=boundary-smearing|violation=do not let one coordinator mix transport policy enrichment recovery and mode switching so thoroughly that failures and ownership stop being local
