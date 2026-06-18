# ParselFire

ParselFire is a portable runtime surface and pack format for giving AI coding
agents architectural guidance at the moment they make design decisions.

On large or long-lived codebases, raw search and larger context windows are not
enough. Agents still miss local invariants, flatten special cases, and drift
away from the system's intended shape. ParselFire keeps that guidance small,
explicit, inspectable, and loadable on demand.

This repository focuses on one practical layer of that problem:

1. thin routing surfaces in `packs/*/pack.urf.md`
2. dense leaf packs with the actual K/X guidance records
3. local validation and evidence that keep the surfaces reviewable and
   falsifiable

Viewed more broadly, ParselFire is a public step toward persistent
architectural guidance for codebases: guidance that should survive across
repeated agent sessions instead of being rediscovered from scratch each time.

## Why This Exists

ParselFire is built for codebases where architecture matters more than one-file
completion speed:

- long-lived repositories
- repeated agent sessions against the same system
- boundaries and lifecycle rules that should survive across tasks
- guidance that should stay portable, reviewable, and usable with local
  workflows

Current integration is Cursor-first, but the pack format is plain markdown and
the surface is intentionally inspectable and runtime-agnostic.

## What ParselFire Is

- a compact format for architectural guidance
- a routed pack layout that keeps runtime reads smaller than repository storage
- a local surface you can review, diff, validate, and sign
- a public starter set of universal, Python, and C++ guidance packs

## What ParselFire Is Not

- not a coding model
- not a hosted service
- not a giant always-on rules dump
- not tied to one language family or one agent environment

## What Ships In v0

- public format docs in [spec/kernel-schema.md](spec/kernel-schema.md) and
  [spec/urf-profile-kernels.md](spec/urf-profile-kernels.md)
- shipped pack families in `packs/universal/`, `packs/python-architecture/`,
  and `packs/cpp-architecture/`
- Cursor routing rules in `.cursor/rules/`
- a zero-dependency validator in [scripts/pack_lint.py](scripts/pack_lint.py)
- real before/after evidence in
  [examples/before-after-python.md](examples/before-after-python.md)
- a manual release marker in `VERSION`
- signature scaffolding in [signatures/README.md](signatures/README.md)

v0 stays deliberately small: routed public pack surfaces, local validation, and
reproducible evidence. That keeps the repository usable today while leaving
room for broader guidance coverage, stronger verification surfaces, and more
runtime integrations over time.

## Pack Ecosystem

ParselFire ships the open format, starter packs, and validation surfaces in
this repository.

Additional maintained packs for other languages, frameworks, and
organization-specific workflows may be published separately under their own
licenses, while continuing to follow the same public format.

This keeps the core surface open and portable while allowing the pack
ecosystem to grow beyond what is shipped here.

## 5 Minutes To Working Routing

The fastest way to try ParselFire is to use this repository as the workspace
root and clone a target repository under `.repos/`.

```text
git clone <parselfire-repo-url>
cd parselfire
git clone <target-repo-url> .repos/target
```

Then:

1. Open `parselfire` in Cursor.
2. Ask the agent to work inside `.repos/target/...`.
3. Let the rules load the relevant pack surfaces automatically.

For a typical Python task, the runtime flow is:

1. `.cursor/rules/parselfire-pack-routing.mdc` loads
   `packs/universal/pack.urf.md`.
2. `.cursor/rules/parselfire-python-routing.mdc` adds
   `packs/python-architecture/pack.urf.md`.
3. The agent matches `signals=` in `## ROUTING` and reads one relevant leaf per
   family.
4. The agent selects a small set of K/X entries from those loaded leaves.
5. `.cursor/rules/post-change-audit.mdc` forces a re-read of the loaded leaves
   against the actual diff after editing.

For C++ sources, `.cursor/rules/parselfire-cpp-routing.mdc` swaps in the
portable C++ family instead of the Python family.

## Runtime Model

ParselFire keeps runtime reads selective:

1. Load the family index surfaces relevant to the task.
2. Follow `## ROUTING` into matching leaf files when needed.
3. Work from a small relevant set of K/X entries rather than the whole
   repository at once.
4. Apply the guidance semantically rather than copying pack text into code.

For many tasks this means:

- `packs/universal/pack.urf.md`
- one matching universal leaf
- zero or one language-family index
- zero or one matching language leaf

This keeps reads focused while leaving the wider repository surface available
when needed.

## Repository Layout

```text
.cursor/rules/      Cursor activation and post-change audit rules
.repos/             Local target repositories to test ParselFire against
examples/           Before/after evidence and related notes
external/           Third-party pack contribution area
packs/              Family indexes plus leaf packs in URF-flavored markdown
scripts/            Zero-dependency validation helpers
signatures/         Signing docs and public-key/signature scaffolding
spec/               Public format specification
VERSION             Manual release version marker
```

## Proof

The best starting point is the Python evidence doc:

- [examples/before-after-python.md](examples/before-after-python.md)

The evidence doc shows two real refactors against external open-source
repositories with project-local test verification and diff-based review.

## Validate Pack Surfaces

Run the repository validator before committing pack-surface edits:

```text
python scripts/pack_lint.py
```

It checks:

- exact `signals=` token uniqueness within each family index
- universal `## STAGES` completeness and ordering
- broken `R.leaf`, `R.pack`, and `L.file` references
- family-wide K/X mirror numbering
- stage-first, id-second ordering inside leaf sections
- warning-level drift where route signals drift away from their target leaf
  content

## Versioning For Now

ParselFire currently versions releases manually through the root `VERSION`
file.

When you cut a release or release candidate, bump `VERSION` first and then
produce matching detached signatures for the shipped `*.urf.md` files.

CI automation is intentionally deferred until after the initial OSS release.
Until then, validation and release packaging stay local and explicit.

## Contributing And Verification

- Format and field rules live in
  [spec/kernel-schema.md](spec/kernel-schema.md) and
  [spec/urf-profile-kernels.md](spec/urf-profile-kernels.md).
- Pack contribution workflow lives in [CONTRIBUTING.md](CONTRIBUTING.md).
- External pack expectations live in [external/README.md](external/README.md).
- Signature and key verification lives in [signatures/README.md](signatures/README.md).

## Design Rules

- Keep family indexes compact; move K/X density into leaf files.
- Use namespaced ids such as `UNI-K03`, `CPP-K17`, and `PY-X08`.
- Keep exact `signals=` tokens unique within one family index.
- Keep one distinct idea per kernel line when possible.
- Treat positive kernels and mirrored exclusions as first-class guidance.
- Keep public pack surfaces self-contained, reviewable, and public-safe.
