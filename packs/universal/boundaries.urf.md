# Universal Boundaries Leaf

## KERNELS

```text
UNI-K29|stage=5|scope=first-class-capability|kernel=when adding a capability thread it through real config transport persistence cache and runtime-control paths so it becomes first-class rather than a side channel
UNI-K30|stage=5|scope=stable-lookup-strategy|kernel=when artifact locations or names vary across versions match them through a stable runtime rule instead of hardcoding brittle version-shaped paths
UNI-K31|stage=5|scope=boundary-key-normalization|kernel=normalize keys at subsystem boundaries so hashing comparison and lookup all operate on one canonical representation
UNI-K32|stage=5|scope=single-responsibility-path|kernel=keep each coordinator or hot path focused on one concern and push transport policy enrichment recovery and mode switching into bounded subsystems
UNI-K35|stage=5|scope=wrapped-future-contract|kernel=when a wrapper future transforms payloads preserve its normal result and completion contract so decode failures surface through the same exception channel as underlying execution errors
UNI-K39|stage=5|scope=standard-log-surface|kernel=when a subsystem becomes a first-class peer route its logs through the platform's standard logger handlers and output surface instead of maintaining bespoke per-subsystem sinks and config knobs
UNI-K40|stage=5|scope=artifact-log-factory|kernel=when a coordinator launches per-item workers construct each worker logger at the coordinator boundary with shared formatting and a deterministic name derived from work identity so logs stay structured and discoverable
UNI-K41|stage=5|scope=boundary-granular-logs|kernel=emit control-loop logs at the same boundary unit the loop actually refreshes or skips so each message names the concrete unit and avoids aggregate status noise
UNI-K45|stage=5|scope=boundary-default-access-policy|kernel=when most entry points share one access policy enforce it once at the dispatch boundary and let exceptional entries opt out through explicit metadata instead of stacking the same policy guard on every entry point
UNI-K50|stage=5|scope=versioned-state-migration|kernel=evolve persisted state through explicit versioned migrations that are idempotent and rerunnable so older data is upgraded before reuse rather than patched in place
```

## EXCLUDES

```text
UNI-X29|stage=5|scope=side-band-semantics|violation=do not bolt important behavior onto side channels when it should flow through real config transport cache or runtime-control boundaries
UNI-X30|stage=5|scope=brittle-path-matching|violation=do not hardcode unstable artifact paths or version-specific names when a stable runtime matching rule exists
UNI-X31|stage=5|scope=unnormalized-boundary-keys|violation=do not let callers cross a subsystem boundary with multiple key representations that hash compare and look up differently
UNI-X32|stage=5|scope=boundary-smearing|violation=do not let one coordinator mix transport policy enrichment recovery and mode switching so thoroughly that failures and ownership stop being local
UNI-X35|stage=5|scope=hidden-decode-failure|violation=do not decode payloads inside adapter callbacks in a way that hides failures outside the wrapper future's normal exception channel
UNI-X39|stage=5|scope=bespoke-log-sidepath|violation=do not keep special log handlers files or config switches for one subsystem once it can share the same logging surface as its peer components
UNI-X40|stage=5|scope=ad-hoc-worker-logging|violation=do not let child workers invent their own logger setup path conventions or formatting when the system needs consistent structured logs per work item
UNI-X41|stage=5|scope=aggregate-refresh-noise|violation=do not log aggregate refresh activity without naming the boundary unit when operators need to tell which concrete inputs were checked skipped or updated
UNI-X45|stage=5|scope=decorator-pileup-policy|violation=do not repeat the same access-policy guard across nearly every entry point and discover exceptions only by guard absence instead of giving the dispatch boundary an explicit opt-out surface
UNI-X50|stage=5|scope=ad-hoc-schema-upgrade|violation=do not change persisted state schemas or serialization layouts in place and assume older data will upgrade itself or survive repeated runs without explicit versioned migration
```
