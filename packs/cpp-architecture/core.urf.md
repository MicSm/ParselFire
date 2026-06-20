# C++ Core Leaf

## KERNELS
CPP-K01|stage=1|scope=nodiscard-side-effect-ops|kernel=reserve nodiscard for results that genuinely must be consumed and not for exchange-style operations whose old value is often discarded on purpose
CPP-K03|stage=1|scope=array-destroy-direction|kernel=derive reverse-destruction end from the base pointer and element count rather than a separately supplied end pointer
CPP-K04|stage=1|scope=explicit-bool-propagation|kernel=when a type exposes explicit operator bool convert explicitly at every bool-producing site
CPP-K05|stage=1|scope=pack-expansion-ellipsis|kernel=when forwarding a variadic pack through nested template arguments include the expansion ellipsis so the whole pack propagates
CPP-K06|stage=1|scope=forward-in-universal-ref|kernel=every use of a forwarding-reference parameter must pass through forward so the original value category survives delegation
CPP-K07|stage=1|scope=assignment-self-return|kernel=when move construction or move assignment delegates to a void helper return the target object explicitly

## EXCLUDES
CPP-X01|stage=1|scope=nodiscard-exchange-clear|violation=do not mark exchange-style operations nodiscard when their normal use includes discarding the previous value
CPP-X03|stage=1|scope=end-ptr-assumption|violation=do not let reverse-destruction logic depend on a separately tracked end pointer when base plus count is the authoritative range description
CPP-X04|stage=1|scope=implicit-explicit-bool|violation=do not rely on implicit conversion from a type with explicit operator bool at bool-producing sites
CPP-X05|stage=1|scope=missing-pack-expansion|violation=do not pass a variadic pack through nested template arguments without the expansion ellipsis
CPP-X06|stage=1|scope=dropped-forward|violation=do not pass a forwarding-reference parameter onward by name alone and silently collapse the value category
CPP-X07|stage=1|scope=void-return-chain|violation=do not try to return the result of a void helper from move construction or move assignment that must yield the target object
