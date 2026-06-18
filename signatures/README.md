# Signatures

ParselFire reserves a detached GPG signing surface for its public pack files.
For now, release numbering is tracked manually in the root `VERSION` file, and
signatures are prepared manually during release packaging. CI-side signing is
intentionally deferred until after the initial OSS release.

`signatures/pubkeys/` is the canonical location for maintainer and contributor
public keys.

## Planned Signed Surface

The intended signed surface is every shipped `*.urf.md` file under the public
core families in `packs/`:

- `packs/universal/`
- `packs/python-architecture/`
- `packs/cpp-architecture/`

Each signed file should have a neighboring detached signature with the same
name plus `.sig`.

## Release-Time Checklist

1. Update the root `VERSION` file to the release or release-candidate number.
2. Make sure the released `*.urf.md` contents are final.
3. Create or refresh the detached `.sig` file beside each released `*.urf.md`
   surface.
4. Publish or update the matching public key under `signatures/pubkeys/`.

## Verify A Single File

Once signatures exist:

```text
gpg --verify packs/universal/pack.urf.md.sig packs/universal/pack.urf.md
```

## Verify The Repository Surface

For routine verification, check the public key first and then verify each
shipped pack file against its detached signature.

On Windows PowerShell, a simple loop looks like:

```powershell
Get-ChildItem packs -Recurse -Filter *.urf.md | ForEach-Object {
  gpg --verify "$($_.FullName).sig" $_.FullName
}
```

## Contributor Requirements

- external contributors must publish their public key under `signatures/pubkeys/`
- external shipped pack files must include detached `.sig` files
- unsigned pack surfaces should be treated as review material, not as released
  artifacts
