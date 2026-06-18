# URF Profile for Kernel Packs

This document freezes the minimal URF-flavored profile used by ParselFire family indexes and leaf packs.

## Goals

- human-readable in plain markdown
- cheap to diff and review
- deterministic to parse with zero third-party dependencies
- compact enough that readers and tooling can inspect an index before opening leaf content

## File Shapes

ParselFire uses three compatible file shapes.

### Universal index (`packs/universal/pack.urf.md`)

The universal index carries the shared stage model plus compact routing records.

```text
## STAGES
S00|name=scope-and-need|question=should this be built at all and what is the smallest correct move

## ROUTING
R01|leaf=foundations.urf.md|signals=smallest,stdlib,dependency,contract,test

## LEAVES
L01|file=foundations.urf.md|theme=scope-contracts
```

### Family index (`*/pack.urf.md` outside `universal`)

A family index is the compact entry surface for one pack family.

```text
## ROUTING
R01|leaf=core.urf.md|signals=nodiscard,forward,pack,bool,assignment,ellipsis

## LEAVES
L01|file=core.urf.md|theme=language-mechanics
```

When a family index needs to hand off into another family, it uses the same `R##|pack=...|signals=...` record shape.

### Leaf pack (`*.urf.md` other than `pack.urf.md`)

Leaf packs contain the actual K/X records.

```text
## KERNELS
UNI-K01|stage=0|scope=build-ladder|kernel=before writing code walk the build ladder: not-needed > stdlib > platform > dependency > one-liner > minimum new code

## EXCLUDES
UNI-X01|stage=0|scope=premature-custom-code|violation=do not write new code when an existing primitive or standard mechanism already covers the need
```

## Parsing Rules

- lines starting with `#` define section boundaries and are not records
- lines starting with `<!--` or `-->` are comments and should be ignored
- blank lines are ignored
- record lines are split on `|`
- the first token is `S00`, `R01`, `L01`, or a bare K/X id such as `UNI-K01`
- remaining tokens are `key=value` pairs
- unknown sections may exist, but tooling should consume `STAGES`, `ROUTING`, `LEAVES`, `KERNELS`, and `EXCLUDES` only when relevant to that file shape

## Normalization Rules

- preserve original field order when rewriting leaf record lines
- preserve leading id tokens exactly
- trim surrounding whitespace around section headings and tokens
- do not wrap record lines across multiple lines
- prefer ASCII punctuation for portability
- keep `signals=` as a comma-separated selector list with no spaces
- keep exact `signals=` tokens unique within one family index surface

## Public v0 Constraints

- entries must reference public architectural guidance only
- no non-public infrastructure names or undistributable implementation details
- no literal reuse from non-public source surfaces
- family indexes should stay small enough to review quickly
- `## ROUTING` should use short literal selectors instead of sentence prose
- exact `signals=` tokens should not repeat across `R` records in the same family index
- `## LEAVES` should remain a small registry surface
- leaf packs should stay compact enough to keep guidance focused and readable

## Validation

Run the repository validator after editing pack surfaces:

```text
python scripts/pack_lint.py
```

The validator is zero-dependency and checks family-index signal collisions, universal stage definitions, route and leaf references, K/X mirror numbering, and stage/id ordering. It also emits warnings when route signals drift away from their target leaf content.
