# Universal Foundations Leaf

## KERNELS
UNI-K01|stage=0|scope=build-ladder|kernel=before writing code walk the build ladder: not-needed > stdlib > platform > dependency > one-liner > minimum new code
UNI-K02|stage=0|scope=metadata-stable-identity|kernel=when the need is stable correlation prefer a cheaper metadata-derived identity over runtime content hashing
UNI-K03|stage=0|scope=minimal-change-surface|kernel=when new code is necessary minimize change surface and prefer deletion, direct code, and few new files or dependencies
UNI-K04|stage=0|scope=minimal-test-proof|kernel=for non-trivial logic leave the smallest runnable check that fails when the behavior breaks
UNI-K05|stage=1|scope=guard-comparison-direction|kernel=write early-return guards against the invalid domain so protection cannot silently invert
UNI-K06|stage=1|scope=positional-param-threading|kernel=propagate positional control parameters through every delegating layer to the implementation that applies the modification
UNI-K07|stage=1|scope=builder-domain-separation|kernel=separate same-width values from different semantic domains by type or naming
UNI-K13|stage=1|scope=api-contract-verification|kernel=verify external API contracts against authoritative sources before integrating them
UNI-K14|stage=1|scope=correctness-floor|kernel=preserve validation safety and explicitly requested behavior even while minimizing code
UNI-K15|stage=1|scope=behavioral-test-contract|kernel=write tests against observable behavior and architectural intent
UNI-K38|stage=1|scope=public-contract-audit|kernel=before changing a public interface map all caller and extension touchpoints and preserve or adapt every caller-visible contract facet including argument binding return shape side effects and override hooks

## EXCLUDES
UNI-X01|stage=0|scope=premature-custom-code|violation=do not write new code when an existing primitive or standard mechanism already covers the need
UNI-X02|stage=0|scope=content-hash-overreach|violation=do not pay for runtime content hashing when the real requirement is stable correlation
UNI-X03|stage=0|scope=speculative-surface-growth|violation=do not widen a solution with speculative abstractions, indirection, extra files, or new dependencies when a smaller change already satisfies the need
UNI-X04|stage=0|scope=test-scaffolding-overreach|violation=do not build fixture-heavy test scaffolding when one small runnable check already gives the needed protection
UNI-X05|stage=1|scope=inverted-guard-filter|violation=do not invert an early-return validation guard and reject valid input while letting invalid input continue
UNI-X06|stage=1|scope=dropped-positional-arg|violation=do not drop a positional parameter during delegation when it controls where the underlying modification must occur
UNI-X07|stage=1|scope=numeric-domain-conflation|violation=do not pass one semantic numeric domain where another is expected just because the widths match
UNI-X13|stage=1|scope=unverified-api-contract|violation=do not assume signatures calling conventions or completion semantics without checking authoritative documentation or runtime evidence
UNI-X14|stage=1|scope=brevity-over-obligations|violation=do not save code by removing validation safety or explicitly requested behavior or by choosing a shorter but less correct path
UNI-X15|stage=1|scope=implementation-coupled-tests|violation=do not anchor tests to incidental structure when the stable obligation is the touched behavior contract
UNI-X38|stage=1|scope=unmapped-interface-swap|violation=do not replace a public interface with a new implementation based only on matching names or happy-path behavior while leaving positional calls return contracts side effects or override seams unmapped
