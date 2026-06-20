# Python Architecture Pack Index

Portable Python runtime routing surface for imports, async lifecycle, runtime ownership, schema boundaries, and cleanup.

## ROUTING
R01|leaf=runtime-bootstrap.urf.md|signals=import,bootstrap,serialize,global,entry,setup,borrowed
R02|leaf=state-lifecycle.urf.md|signals=state,runtime,typed,reauth,tasklocal,cancellation,coordinator,refresh
R03|leaf=async-surfaces.urf.md|signals=async,await,guard,lint,bridge,context,thread
R04|leaf=boundaries-cleanup.urf.md|signals=payload,schema,protocol,sdk,cleanup,retire

## LEAVES
L01|file=runtime-bootstrap.urf.md|theme=bootstrap-imports
L02|file=state-lifecycle.urf.md|theme=state-lifecycle
L03|file=async-surfaces.urf.md|theme=async-surfaces
L04|file=boundaries-cleanup.urf.md|theme=boundaries-cleanup
