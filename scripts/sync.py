#!/usr/bin/env python3
"""Rebuild the security-skills database from the vendored/ upstreams.

Reads sources.yaml + categories.yaml, scans every vendored SKILL.md, then writes:
  - catalog.json               machine-readable index of all skills
  - README.md                  the human "database" (starter set + category tables)
  - .claude-plugin/marketplace.json   one installable marketplace of all plugins

Run from the repo root:  python scripts/sync.py
No network access — it only reads what is already vendored. To pull upstream
changes, re-clone at a new SHA (see sources.yaml) into vendored/, then run this.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
DROP_SEGMENTS = {"plugins", "skills", "SKILL.md"}


def load_yaml(name: str) -> dict:
    return yaml.safe_load((ROOT / name).read_text(encoding="utf-8"))


def parse_frontmatter(text: str) -> dict:
    """Tolerant frontmatter reader: pulls `name` and `description` even when the
    description is unquoted and contains colons (real Claude Code handles this;
    a strict YAML load does not)."""
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    block = m.group(1) if m else text[:2000]
    lines = block.splitlines()
    out: dict[str, str] = {}
    key = None
    buf: list[str] = []
    for ln in lines:
        km = re.match(r"^([A-Za-z_][\w-]*):\s?(.*)$", ln)
        if km:
            if key:
                out[key] = " ".join(buf).strip()
            key, first = km.group(1), km.group(2)
            buf = [first] if first else []
        elif key and (ln.startswith((" ", "\t")) or ln.strip()):
            buf.append(ln.strip())
    if key:
        out[key] = " ".join(buf).strip()
    for k, v in out.items():
        if len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]:
            out[k] = v[1:-1].strip()
    return out


def skill_id(rel_parts: list[str]) -> str:
    return "/".join(p for p in rel_parts if p not in DROP_SEGMENTS)


def classify(skill: dict, cats: dict) -> str:
    sid = skill["id"]
    if sid in cats.get("overrides", {}):
        return cats["overrides"][sid]
    leaf = sid.rsplit("/", 1)[-1].lower()
    for pref in cats.get("offensive_name_prefixes", []):
        if leaf.startswith(pref):
            return "offensive"
    hay = f"{skill['path']} {skill['name']} {skill['description']}".lower()
    for cat in cats["categories"]:
        for kw in cat["match"]:
            if kw.lower() in hay:
                return cat["id"]
    return "uncategorized"


def find_plugins() -> dict[str, dict]:
    """Every vendored dir holding .claude-plugin/plugin.json becomes an installable
    plugin. Returns {plugin_dir_relposix: plugin.json-ish}."""
    plugins = {}
    for pj in (ROOT / "vendored").rglob(".claude-plugin/plugin.json"):
        pdir = pj.parent.parent
        try:
            data = json.loads(pj.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = {}
        plugins[pdir.relative_to(ROOT).as_posix()] = {
            "dir": pdir,
            "name": data.get("name") or pdir.name,
            "description": data.get("description", ""),
        }
    return plugins


def main() -> None:
    sources = load_yaml("sources.yaml")["sources"]
    cats = load_yaml("categories.yaml")
    src_by_key = {s["key"]: s for s in sources}
    exclude_paths = cats.get("exclude_paths", [])
    exclude_ids = set(cats.get("exclude_ids", []))

    skills: list[dict] = []
    for s in sources:
        scan_root = ROOT / s["scan_root"]
        for skill_md in sorted(scan_root.rglob("SKILL.md")):
            rel = skill_md.relative_to(ROOT).as_posix()
            if any(x in f"/{rel}" for x in exclude_paths):
                continue
            fm = parse_frontmatter(skill_md.read_text(encoding="utf-8", errors="replace"))
            parts = skill_md.relative_to(ROOT / "vendored").as_posix().split("/")
            parts = [s["key"]] + parts[1:]  # normalise source dir -> source key
            sid = skill_id(parts)
            if sid in exclude_ids:
                continue
            skills.append({
                "id": sid,
                "name": fm.get("name") or parts[-2],
                "description": re.sub(r"\s+", " ", fm.get("description", "")).strip(),
                "source": s["key"],
                "license": s["license"],
                "path": rel,
            })

    for sk in skills:
        sk["category"] = classify(sk, cats)

    plugins = find_plugins()
    write_catalog(skills, src_by_key, plugins)
    write_marketplace(plugins, src_by_key)
    write_readme(skills, cats, src_by_key, plugins)
    by_cat: dict[str, int] = {}
    for sk in skills:
        by_cat[sk["category"]] = by_cat.get(sk["category"], 0) + 1
    print(f"{len(skills)} skills, {len(plugins)} plugins")
    for cid, n in sorted(by_cat.items(), key=lambda x: -x[1]):
        print(f"  {n:3d}  {cid}")


def write_catalog(skills, src_by_key, plugins) -> None:
    payload = {
        "generated_by": "scripts/sync.py",
        "sources": [
            {"key": k, "repo": s["repo"], "sha": s["sha"], "license": s["license"],
             "homepage": s["homepage"]}
            for k, s in src_by_key.items()
        ],
        "counts": {"skills": len(skills), "plugins": len(plugins)},
        "skills": sorted(skills, key=lambda x: (x["category"], x["id"])),
    }
    (ROOT / "catalog.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def marketplace_name(prefix, name) -> str:
    return f"{prefix}-{name}".replace("_", "-")


def write_marketplace(plugins, src_by_key) -> None:
    prefix = {"vendored/trailofbits": "tob", "vendored/masriyan": "masriyan",
              "vendored/trilwu": "trilwu"}
    entries = []
    for reldir, p in sorted(plugins.items()):
        src_prefix = next((v for k, v in prefix.items() if reldir.startswith(k)), "sec")
        entries.append({
            "name": marketplace_name(src_prefix, p["name"]),
            "source": f"./{reldir}",
            "description": p["description"][:300],
        })
    doc = {
        "name": "security-skills",
        "owner": {"name": "gztes", "url": "https://github.com/gztes"},
        "metadata": {
            "version": "1.0.0",
            "description": "Aggregated security skills for Claude Code from Trail of Bits, "
                           "Masriyan, and trilwu — categorised for securing apps, sites, and "
                           "companies. See README.md for the full index.",
        },
        "plugins": entries,
    }
    (ROOT / ".claude-plugin" / "marketplace.json").write_text(
        json.dumps(doc, indent=2) + "\n", encoding="utf-8")


def esc(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ")


def write_readme(skills, cats, src_by_key, plugins) -> None:
    by_id = {sk["id"]: sk for sk in skills}
    by_cat: dict[str, list] = {}
    for sk in skills:
        by_cat.setdefault(sk["category"], []).append(sk)
    total = len(skills)

    L = []
    L.append("# security\n")
    L.append("> A categorised database of **security skills for Claude Code**, aggregated "
             "from three open-source collections and organised around what you actually "
             "secure: apps, websites, APIs, cloud, and companies.\n")
    L.append(f"**{total} skills** across **{len(by_cat)} categories**, vendored from "
             f"{len(src_by_key)} upstream repositories. Every skill keeps its original "
             "folder, license, and attribution.\n")
    intro = ROOT / "INTRO.md"
    if intro.exists():
        L.append(intro.read_text(encoding="utf-8").strip() + "\n")
    L.append("Each skill is a folder of instructions (and sometimes scripts) that Claude "
             "Code loads on demand. This repo does three things: **collects** them, "
             "**categorises** them, and packages them as **one installable marketplace**.\n")

    # Sources
    L.append("## Sources\n")
    L.append("| Upstream | Skills | License | Pinned commit |")
    L.append("|---|--:|---|---|")
    counts = {k: 0 for k in src_by_key}
    for sk in skills:
        counts[sk["source"]] += 1
    for k, s in src_by_key.items():
        L.append(f"| [{s['repo']}]({s['homepage']}) | {counts[k]} | {s['license']} | "
                 f"`{s['sha'][:10]}` |")
    L.append("")

    # Install
    L.append("## Install\n")
    L.append("```bash\n/plugin marketplace add gztes/security\n```\n")
    L.append("Then install any plugin listed by the marketplace, e.g.:\n")
    L.append("```bash\n/plugin install tob-insecure-defaults@security-skills\n"
             "/plugin install trilwu-secskills-core@security-skills\n"
             "/plugin install masriyan-cybersecurity@security-skills\n```\n")
    L.append("> Install a few plugins for the job in front of you, not all of them at "
             "once — a smaller, relevant skill set makes Claude better at picking the "
             "right one. Skills are prompts Claude executes and some ship runnable "
             "scripts; only add what you trust.\n")

    # Starter
    starter_ids = [i for i in cats.get("starter", []) if i in by_id]
    if starter_ids:
        L.append("## Start here\n")
        L.append("If you have vibe-coded an app or site and want the highest-signal checks first:\n")
        L.append("> Also install **`tob-insecure-defaults`** — a command-based plugin (hardcoded "
                 "credentials, fallback secrets, dangerous defaults) that ships as a `/audit` "
                 "command rather than a skill, so it is not in the table below.\n")
        L.append("| Skill | Source | What it does |")
        L.append("|---|---|---|")
        for sid in starter_ids:
            sk = by_id[sid]
            L.append(f"| [`{sk['name']}`]({sk['path']}) | {sk['source']} | "
                     f"{esc(sk['description'])[:150]} |")
        L.append("")

    # Categories
    L.append("## Categories\n")
    order = [c["id"] for c in cats["categories"]] + ["uncategorized"]
    titles = {c["id"]: c["title"] for c in cats["categories"]}
    blurbs = {c["id"]: c["blurb"] for c in cats["categories"]}
    titles["uncategorized"] = "Uncategorized (needs triage)"
    blurbs["uncategorized"] = "New or unmatched upstream skills — edit categories.yaml to place them."
    # table of contents
    for cid in order:
        if by_cat.get(cid):
            anchor = titles[cid].lower().replace(" ", "-").replace("&", "").replace("/", "").replace("(", "").replace(")", "").replace(",", "").replace("--", "-")
            L.append(f"- [{titles[cid]}](#{anchor}) ({len(by_cat[cid])})")
    L.append("")
    for cid in order:
        group = by_cat.get(cid)
        if not group:
            continue
        L.append(f"### {titles[cid]}\n")
        L.append(f"_{blurbs[cid]}_\n")
        L.append("| Skill | Source | What it does |")
        L.append("|---|---|---|")
        for sk in sorted(group, key=lambda x: x["name"]):
            L.append(f"| [`{sk['name']}`]({sk['path']}) | {sk['source']} | "
                     f"{esc(sk['description'])[:160]} |")
        L.append("")

    # Attribution / license
    L.append("## Licensing & attribution\n")
    L.append("This is an **aggregation**. Copyright stays with the original authors and "
             "each skill remains under its upstream license:\n")
    for k, s in src_by_key.items():
        L.append(f"- **{s['repo']}** — {s['license']} "
                 f"([license](LICENSES/{Path(s['license_file']).name}))")
    L.append("")
    L.append("Trail of Bits' skills are **CC-BY-SA-4.0**: they are redistributed here with "
             "attribution and a link to the license; any modified versions must stay under "
             "CC-BY-SA-4.0. The only change made to upstream content is **relocation** into "
             "`vendored/` — skill contents are unmodified. See `NOTICE.md`.\n")
    L.append("## Rebuilding\n")
    L.append("`README.md`, `catalog.json`, and `.claude-plugin/marketplace.json` are "
             "generated. Edit `categories.yaml` (curation) or bump a SHA in `sources.yaml` "
             "and re-vendor, then run:\n")
    L.append("```bash\npython scripts/sync.py\n```\n")

    (ROOT / "README.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
