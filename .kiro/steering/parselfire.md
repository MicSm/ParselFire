---
title: ParselFire portable routing contract
inclusion: always
---

# ParselFire Portable Routing Contract

ParselFire gives AI coding agents a small routed set of architectural guardrails
instead of one large always-on rules dump.

When a task touches code:

1. Load `packs/universal/pack.urf.md`.
2. Detect the active source family from the file being changed:
   - Python: also load `packs/python-architecture/pack.urf.md`
   - C++: also load `packs/cpp-architecture/pack.urf.md`
   - Plain C: stay on universal only
   - Ambiguous `.h`: use the C++ family only when the file contains C++
     constructs
3. Treat each loaded `pack.urf.md` as a routing index, not as the dense
   guidance body.
4. From each loaded `## ROUTING`, match `signals=` against the active code
   context and read exactly one matching leaf per family unless the change
   truly crosses themes.
5. From the loaded leaves, select 3-5 total K/X entries with stage-aligned
   preference.
6. Apply the guidance semantically. Never paste pack text verbatim into code or
   comments.

After any code edit:

- Re-read the relevant loaded leaf pack(s); do not rely on memory.
- Inspect the actual diff against both `## KERNELS` and `## EXCLUDES`.
- Verify that every selected or claimed kernel is demonstrably satisfied by the
  diff, and that no loaded exclusion pattern was introduced.
- Fix any mismatch immediately or report the violated `pack/scope` and the
  exact trade-off explicitly.
- If a loaded kernel was not materially relevant, omit it rather than citing it
  aspirationally.

Keep runtime reads focused:

- default read set = `packs/universal/pack.urf.md` + one matching universal
  leaf + zero or one language-family index + zero or one language leaf
- only widen the read surface when the change truly spans multiple themes or
  families

This file is the canonical portable instruction surface. Thin host adapters
should mirror it without adding host-specific routing semantics.
