# NOTICE — attribution & licensing

This repository is an **aggregation** of security skills for Claude Code created by
other people. It does not claim authorship of any vendored skill. Copyright remains
with the original authors, and each skill stays under its upstream license.

## Vendored sources

| Source | Location here | License | Upstream |
|---|---|---|---|
| Trail of Bits — `trailofbits/skills` | `vendored/trailofbits/` | **CC-BY-SA-4.0** | https://github.com/trailofbits/skills |
| Masriyan (sudo3rs) — `Claude-Code-CyberSecurity-Skill` | `vendored/masriyan/` | MIT | https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill |
| trilwu — `secskills` | `vendored/trilwu/` | MIT | https://github.com/trilwu/secskills |

The exact commit each source was taken from is pinned in `sources.yaml`. Full
license texts are in `LICENSES/`.

## What was changed

Skill **contents are unmodified**. The only change is **relocation**: each upstream
repository was copied whole into a subfolder of `vendored/`, and this repo adds its
own index (`README.md`, `catalog.json`), curation (`categories.yaml`), a combined
`.claude-plugin/marketplace.json`, and a rebuild script (`scripts/sync.py`).

## CC-BY-SA-4.0 (Trail of Bits) compliance

The Trail of Bits skills in `vendored/trailofbits/` are licensed **CC-BY-SA-4.0**.
As required by that license:

- **Attribution** — credited above, with a link to the source and to the license
  (`LICENSES/trailofbits-CC-BY-SA-4.0.txt`).
- **Indicate changes** — see "What was changed" above (relocation only).
- **ShareAlike** — any adapted/modified version of that content must be distributed
  under CC-BY-SA-4.0.

The aggregation as a whole is a **collection**: combining these works alongside the
MIT-licensed sources does not relicense any of them. Each subtree keeps its own terms.

## Repository's own additions

The files original to this repository — `README.md`, `catalog.json`,
`categories.yaml`, `sources.yaml`, `scripts/`, and `.claude-plugin/marketplace.json`
— are provided under CC-BY-SA-4.0 to stay compatible with the strongest upstream
license. They contain no upstream skill content beyond names and descriptions quoted
for indexing.

## Removing your work

If you are an upstream author and want your skills removed from this aggregation,
open an issue and they will be taken down.
