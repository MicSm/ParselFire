# Python Runtime-Bootstrap Leaf

## KERNELS
PY-K02|stage=1|scope=serialize-init-symmetry|kernel=for type-tag-plus-kwargs rehydration make serialize() a complete JSON-safe mirror of reconstructable __init__ parameters
PY-K06|stage=3|scope=import-safe-bootstrap|kernel=centralize configuration-dependent bootstrap in explicit setup or lazy first use so module import never mutates global runtime state
PY-K07|stage=3|scope=global-vs-entry-setup|kernel=put process-wide services and handlers in one-time async setup and reserve per-entry setup for independently owned resources
PY-K08|stage=3|scope=borrowed-async-resources|kernel=when async helpers may receive loop-bound resources from callers separate acquisition from ownership and only context-manage instances created locally

## EXCLUDES
PY-X02|stage=1|scope=lossy-rehydration-contract|violation=do not add constructor parameters that serialize() omits or emit partial values and assume re-instantiation will preserve behavior
PY-X06|stage=3|scope=import-side-effect-bootstrap|violation=do not populate registries bind settings-driven singletons or perform network and filesystem work as a side effect of import
PY-X07|stage=3|scope=entry-scoped-global-registration|violation=do not register global services or process-wide handlers from per-entry setup hooks where retries duplicates or unload ordering can leave partial state
PY-X08|stage=3|scope=nested-resource-ownership|violation=do not have nested helpers unconditionally create or context-manage async clients or runners that a longer-lived caller already owns
