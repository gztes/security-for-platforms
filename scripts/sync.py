#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCES_FILE = ROOT / "sources.yaml"
CATEGORIES_FILE = ROOT / "categories.yaml"
CATALOG_FILE = ROOT / "catalog.json"
README_FILE = ROOT / "README.md"
SKILLS_DIR = ROOT / "skills"
PLUGINS_DIR = ROOT / "plugins"
MARKETPLACE_FILE = ROOT / ".claude-plugin" / "marketplace.json"


@dataclass
class SkillRecord:
    source: str
    source_url: str
    license: str
    name: str
    slug: str
    description: str
    category_id: str
    category_name: str
    path: str
    key: str


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-")


def run(cmd: List[str], cwd: Optional[Path] = None) -> None:
    subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=True)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def parse_frontmatter(skill_md: Path) -> tuple[str, str]:
    text = skill_md.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        fallback = skill_md.parent.name
        return fallback, ""

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, flags=re.DOTALL)
    if not match:
        fallback = skill_md.parent.name
        return fallback, ""

    frontmatter_text = match.group(1)
    name = skill_md.parent.name
    description = ""
    try:
        parsed = yaml.safe_load(frontmatter_text) or {}
        name = str(parsed.get("name") or name).strip()
        description = str(parsed.get("description") or "").strip()
    except yaml.YAMLError:
        for line in frontmatter_text.splitlines():
            if line.startswith("name:"):
                name = line.split(":", 1)[1].strip().strip("'\"")
            elif line.startswith("description:"):
                description = line.split(":", 1)[1].strip().strip("'\"")

    description = description.replace("\n", " ").strip()
    return name, description


def clone_at_sha(repo: str, sha: str, dest: Path) -> None:
    run(["git", "clone", "--depth", "1", f"https://github.com/{repo}.git", str(dest)])
    run(["git", "fetch", "--depth", "1", "origin", sha], cwd=dest)
    run(["git", "checkout", "--detach", sha], cwd=dest)


def iter_skills(source_root: Path) -> Iterable[Path]:
    for skill_md in source_root.rglob("SKILL.md"):
        path_str = skill_md.as_posix()
        if "/tests/" in path_str:
            continue
        yield skill_md


def category_for(
    source_id: str,
    slug: str,
    by_source: Dict[str, Dict[str, str]],
    default_prefixes: Dict[str, Dict[str, str]],
    source_relative_path: str,
) -> str:
    explicit = by_source.get(source_id, {}).get(slug)
    if explicit:
        return explicit
    for prefix, category in default_prefixes.get(source_id, {}).items():
        if source_relative_path.startswith(prefix):
            return category
    return "uncategorized"


def ensure_empty_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def build_readme(
    records: List[SkillRecord],
    categories: Dict[str, str],
    starter_keys: List[str],
) -> str:
    by_key = {r.key: r for r in records}

    lines: List[str] = []
    lines.append("# vibe-sec-skills")
    lines.append("")
    lines.append("Curated security skill catalog aggregated from Masriyan, trilwu, and Trail of Bits.")
    lines.append("")
    lines.append("## Starter 15")
    lines.append("")
    lines.append("These are the highest-signal skills for common vibe-coding security failures: insecure defaults, hardcoded secrets, auth/session flaws, dependency risk, and XSS/injection review.")
    lines.append("")

    for key in starter_keys:
        rec = by_key.get(key)
        if not rec:
            continue
        lines.append(f"- **{rec.name}** ({rec.category_name}) — {rec.description}")

    lines.append("")
    lines.append("## Full catalog")
    lines.append("")
    lines.append("| Category | Skill | Description | Source | License | Path |")
    lines.append("|---|---|---|---|---|---|")

    for rec in sorted(records, key=lambda r: (r.category_name, r.source, r.slug)):
        source_md = f"[{rec.source}]({rec.source_url})"
        lines.append(
            "| "
            f"{rec.category_name} | "
            f"`{rec.name}` | "
            f"{rec.description.replace('|', '\\|')} | "
            f"{source_md} | "
            f"{rec.license} | "
            f"`{rec.path}` |"
        )

    lines.append("")
    lines.append("## Sources")
    lines.append("")
    lines.append("Pinned source commits are recorded in `sources.yaml`.")
    return "\n".join(lines) + "\n"


def write_plugin(plugin_root: Path, name: str, description: str, records: List[SkillRecord]) -> None:
    ensure_empty_dir(plugin_root)
    (plugin_root / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (plugin_root / "skills").mkdir(parents=True, exist_ok=True)

    plugin_json = {
        "name": name,
        "version": "1.0.0",
        "description": description,
        "author": {
            "name": "gztes",
            "url": "https://github.com/gztes/vibe-sec-skills",
        },
        "license": "MIXED (MIT, CC-BY-SA-4.0)",
        "homepage": "https://github.com/gztes/vibe-sec-skills",
        "repository": "https://github.com/gztes/vibe-sec-skills",
    }
    (plugin_root / ".claude-plugin" / "plugin.json").write_text(
        json.dumps(plugin_json, indent=2) + "\n", encoding="utf-8"
    )

    for rec in records:
        src = ROOT / rec.path
        dst = plugin_root / "skills" / f"{rec.source}--{rec.slug}"
        shutil.copytree(src, dst)


def main() -> None:
    sources_cfg = load_yaml(SOURCES_FILE)
    categories_cfg = load_yaml(CATEGORIES_FILE)

    categories: Dict[str, str] = categories_cfg.get("categories", {})
    by_source: Dict[str, Dict[str, str]] = categories_cfg.get("by_source", {})
    default_prefixes: Dict[str, Dict[str, str]] = categories_cfg.get("defaults", {})
    starter_15: List[str] = categories_cfg.get("starter_15", [])

    ensure_empty_dir(SKILLS_DIR)
    PLUGINS_DIR.mkdir(parents=True, exist_ok=True)

    records: List[SkillRecord] = []

    with tempfile.TemporaryDirectory(prefix="vibe-sec-sync-") as tmp:
        tmp_root = Path(tmp)

        for source in sources_cfg.get("sources", []):
            source_id = source["id"]
            repo = source["repo"]
            sha = source["sha"]
            source_url = source["source_url"]
            license_name = source["license"]
            denylist = set(source.get("denylist", []))

            clone_dir = tmp_root / source_id
            clone_at_sha(repo, sha, clone_dir)

            for skill_md in iter_skills(clone_dir):
                name, description = parse_frontmatter(skill_md)
                slug = slugify(name)
                if not slug or slug in denylist:
                    continue

                source_relative = skill_md.relative_to(clone_dir).as_posix()
                category_id = category_for(
                    source_id=source_id,
                    slug=slug,
                    by_source=by_source,
                    default_prefixes=default_prefixes,
                    source_relative_path=source_relative,
                )
                category_name = categories.get(category_id, categories.get("uncategorized", "Uncategorized"))

                relative_skill_dir = skill_md.parent
                dest_rel = Path("skills") / category_id / f"{source_id}--{slug}"
                dest_abs = ROOT / dest_rel
                dest_abs.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(relative_skill_dir, dest_abs)

                records.append(
                    SkillRecord(
                        source=source_id,
                        source_url=source_url,
                        license=license_name,
                        name=name,
                        slug=slug,
                        description=description,
                        category_id=category_id,
                        category_name=category_name,
                        path=dest_rel.as_posix(),
                        key=f"{source_id}/{slug}",
                    )
                )

    records.sort(key=lambda r: (r.category_name, r.source, r.slug))

    CATALOG_FILE.write_text(
        json.dumps(
            [
                {
                    "name": r.name,
                    "description": r.description,
                    "category": r.category_name,
                    "category_id": r.category_id,
                    "source": r.source,
                    "source_url": r.source_url,
                    "license": r.license,
                    "path": r.path,
                    "key": r.key,
                }
                for r in records
            ],
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    README_FILE.write_text(build_readme(records, categories, starter_15), encoding="utf-8")

    # Build plugin bundles.
    starter_records = [r for r in records if r.key in set(starter_15)]
    offense_records = [r for r in records if r.category_id == "offensive-authorized-testing"]
    full_records = [r for r in records if r.category_id != "uncategorized"]

    write_plugin(
        PLUGINS_DIR / "vibe-sec-starter",
        "vibe-sec-starter",
        "Starter 15 security skills for common vibe-coding vulnerabilities.",
        starter_records,
    )
    write_plugin(
        PLUGINS_DIR / "vibe-sec-offense",
        "vibe-sec-offense",
        "Offensive security skills for authorized penetration testing only.",
        offense_records,
    )
    write_plugin(
        PLUGINS_DIR / "vibe-sec-full",
        "vibe-sec-full",
        "Full curated security catalog (excluding uncategorized).",
        full_records,
    )

    marketplace = {
        "name": "vibe-sec-skills",
        "owner": {
            "name": "gztes",
            "url": "https://github.com/gztes",
        },
        "metadata": {
            "version": "1.0.0",
            "description": "Curated security skills split into starter, full, and offensive packs.",
        },
        "plugins": [
            {
                "name": "vibe-sec-starter",
                "version": "1.0.0",
                "description": "Starter 15: insecure defaults, secrets, auth, dependency risk, and XSS/injection checks.",
                "author": {
                    "name": "gztes",
                    "url": "https://github.com/gztes",
                },
                "source": "./plugins/vibe-sec-starter",
            },
            {
                "name": "vibe-sec-full",
                "version": "1.0.0",
                "description": "Full curated catalog for broad security engineering and review workflows.",
                "author": {
                    "name": "gztes",
                    "url": "https://github.com/gztes",
                },
                "source": "./plugins/vibe-sec-full",
            },
            {
                "name": "vibe-sec-offense",
                "version": "1.0.0",
                "description": "Offensive skills for authorized testing only.",
                "author": {
                    "name": "gztes",
                    "url": "https://github.com/gztes",
                },
                "source": "./plugins/vibe-sec-offense",
            },
        ],
    }
    MARKETPLACE_FILE.parent.mkdir(parents=True, exist_ok=True)
    MARKETPLACE_FILE.write_text(json.dumps(marketplace, indent=2) + "\n", encoding="utf-8")

    missing_starter = sorted(set(starter_15) - {r.key for r in records})
    if missing_starter:
        print(f"Warning: missing starter keys: {', '.join(missing_starter)}")

    print(f"Generated {len(records)} skills")


if __name__ == "__main__":
    main()
