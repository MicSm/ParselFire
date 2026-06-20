# C++ Architecture Pack Index

Portable C++ runtime routing surface for language mechanics, state modeling, concurrency, lifecycle, shared abstractions, and subsystem boundaries.

## ROUTING
R01|leaf=core.urf.md|signals=nodiscard,forward,pack,bool,assignment,ellipsis
R02|leaf=contracts.urf.md|signals=contract,identity,width,accessor,encoding,fallback
R03|leaf=state-modeling.urf.md|signals=result,callback,category,metadata,load,validation,probe,variant,equality
R04|leaf=concurrency.urf.md|signals=barrier,memory,thread,stream,writer,ordering
R05|leaf=lifecycle.urf.md|signals=raii,start,stop,teardown,publication,worker,transition,scratch
R06|leaf=shared.urf.md|signals=wrapper,trait,helper,allocation,view,owned
R07|leaf=boundaries.urf.md|signals=lto,macro,namespace,snapshot,abi,transport

## LEAVES
L01|file=core.urf.md|theme=language-mechanics
L02|file=contracts.urf.md|theme=contracts-typed-boundaries
L03|file=state-modeling.urf.md|theme=state-outcome-modeling
L04|file=concurrency.urf.md|theme=concurrency-publication
L05|file=lifecycle.urf.md|theme=ownership-lifecycle
L06|file=shared.urf.md|theme=shared-abstractions
L07|file=boundaries.urf.md|theme=boundaries-convergence
