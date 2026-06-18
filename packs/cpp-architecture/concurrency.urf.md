# C++ Concurrency Leaf

## KERNELS
CPP-K02|stage=1|scope=barrier-semantic-level|kernel=express cross-thread visibility through C++ memory ordering at the weakest strength that preserves the invariant
CPP-K14|stage=1|scope=ordered-stream-preservation|kernel=preserve per-stream ordering when downstream stages depend on each input stream remaining individually ordered
CPP-K27|stage=3|scope=single-writer-claim|kernel=gate shared metadata mutation and one-time publication behind an explicit single-writer claim and keep followers read-only until ownership is established

## EXCLUDES
CPP-X02|stage=1|scope=compiler-barrier-as-fence|violation=do not substitute compiler-specific fences or volatile for C++ memory-model ordering when cross-thread visibility matters
CPP-X14|stage=1|scope=order-breaking-narrowing|violation=do not narrow or concatenate individually sorted streams when later stages depend on per-stream ordering being preserved
CPP-X27|stage=3|scope=implicit-writer-ownership|violation=do not rely on implicit ordering or role assumptions to let multiple writers touch shared state before exclusive ownership is confirmed
