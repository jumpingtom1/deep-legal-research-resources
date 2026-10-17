#!/usr/bin/env python3
"""release_skill.py — publish a deep-legal-research release into skill/.

    python3 scripts/release_skill.py <skill-folder-or-zip> [--summary "one line"] [--dry-run]

Builds  skill/deep-legal-research.zip  (one root folder deep-legal-research/,
deterministic order and timestamps) and  skill/latest.json  — the manifest the
skill's own scripts/update_check.py reads to decide whether a newer release
exists.

Secrets never reach the public repo: scripts/govinfo.key (the bundled
api.data.gov key, which the skill says may be shared with colleagues but
never posted publicly) and any *.key / *.pem / .env file are left out, and
listed in `preserve_local` so update_check.py copies them from the user's
current installation into the zip it hands over. The script refuses to write
if a remaining text file looks like it holds a credential.

Checks before writing: SKILL.md frontmatter name == folder name; VERSION
parses; the new version is higher than the published one; every file of the
previous release is still present (or listed with --allow-removed); no
__pycache__.
"""
import argparse
import hashlib
import io
import json
import re
import sys
import zipfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "skill"
NAME = "deep-legal-research"
RAW = "https://raw.githubusercontent.com/jumpingtom1/deep-legal-research-resources/main/skill/"
EXCLUDE_NAMES = {"govinfo.key", ".DS_Store"}
EXCLUDE_SUFFIX = (".key", ".pem", ".pyc")
EXCLUDE_DIRS = {"__pycache__", ".git"}
PRESERVE_LOCAL = ["scripts/govinfo.key"]
SECRET_RX = re.compile(rb"(api[_-]?key\s*[=:]\s*['\"]?[A-Za-z0-9]{32,})|(-----BEGIN [A-Z ]*PRIVATE KEY-----)"
                       rb"|(\bghp_[A-Za-z0-9]{30,})|(\bsk-[A-Za-z0-9]{20,})", re.I)
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def load_tree(src):
    """Return {relative path: bytes} for the skill, from a folder or a zip."""
    src = Path(src)
    files = {}
    if src.is_dir():
        base = src
        for p in sorted(src.rglob("*")):
            if p.is_file():
                files[p.relative_to(base).as_posix()] = p.read_bytes()
        return files
    with zipfile.ZipFile(src) as z:
        roots = {n.split("/", 1)[0] for n in z.namelist()}
        if len(roots) != 1:
            sys.exit(f"zip must contain exactly one root folder, found {sorted(roots)}")
        root = roots.pop()
        for n in z.namelist():
            if not n.endswith("/"):
                files[n[len(root) + 1:]] = z.read(n)
    return files


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("--summary", default="")
    ap.add_argument("--allow-removed", nargs="*", default=[])
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    files = load_tree(a.source)
    if "SKILL.md" not in files or "VERSION" not in files:
        sys.exit("source has no SKILL.md or VERSION at its root")
    fm = re.match(rb"---\s*\n(.*?)\n---", files["SKILL.md"], re.S)
    m = fm and re.search(rb"^name:\s*(\S+)", fm.group(1), re.M)
    if not m or m.group(1).decode() != NAME:
        sys.exit(f"SKILL.md frontmatter name must be {NAME!r}")
    vm = re.search(rb"version:\s*([\d.]+)", files["VERSION"])
    dm = re.search(rb"last_modified:\s*([\d-]+)", files["VERSION"])
    if not vm:
        sys.exit("VERSION has no version: line")
    version = vm.group(1).decode()

    kept, dropped = {}, []
    for rel, data in files.items():
        parts = rel.split("/")
        if (set(parts) & EXCLUDE_DIRS) or parts[-1] in EXCLUDE_NAMES or rel.endswith(EXCLUDE_SUFFIX) \
                or parts[-1].startswith(".env"):
            dropped.append(rel)
            continue
        if SECRET_RX.search(data):
            sys.exit(f"{rel} looks like it contains a credential — remove it before publishing")
        kept[rel] = data

    prev = {}
    if (OUT / "latest.json").exists():
        prev = json.loads((OUT / "latest.json").read_text())
        pv = tuple(int(x) for x in prev["version"].split("."))
        if tuple(int(x) for x in version.split(".")) <= pv:
            sys.exit(f"version {version} is not higher than the published {prev['version']}")
        gone = [f for f in prev.get("files", []) if f not in kept and f not in a.allow_removed]
        if gone:
            sys.exit(f"files in the previous release are missing: {gone} (use --allow-removed)")

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for d in sorted({"/".join(r.split("/")[:i]) for r in kept for i in range(1, r.count("/") + 1)}):
            zi = zipfile.ZipInfo(f"{NAME}/{d}/", date_time=FIXED_TIME)
            zi.external_attr = 0o40755 << 16
            z.writestr(zi, b"")
        for rel in sorted(kept):
            zi = zipfile.ZipInfo(f"{NAME}/{rel}", date_time=FIXED_TIME)
            zi.external_attr = (0o755 if rel.endswith(".py") else 0o644) << 16
            z.writestr(zi, kept[rel], zipfile.ZIP_DEFLATED)
    blob = buf.getvalue()
    manifest = {
        "name": NAME,
        "version": version,
        "released": dm.group(1).decode() if dm else date.today().isoformat(),
        "published": date.today().isoformat(),
        "summary": a.summary,
        "zip_url": RAW + "deep-legal-research.zip",
        "sha256": hashlib.sha256(blob).hexdigest(),
        "bytes": len(blob),
        "files": sorted(kept),
        "preserve_local": [p for p in PRESERVE_LOCAL if p in files or p in dropped],
        "excluded_from_public_zip": sorted(dropped),
    }
    print(f"{NAME} v{version}: {len(kept)} files, {len(blob):,} bytes, sha256 {manifest['sha256'][:16]}")
    print(f"  left out (local-only): {', '.join(sorted(dropped)) or '—'}")
    if a.dry_run:
        print("  dry run — nothing written")
        return
    OUT.mkdir(exist_ok=True)
    (OUT / "deep-legal-research.zip").write_bytes(blob)
    (OUT / "latest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    print(f"  wrote {OUT.relative_to(ROOT)}/deep-legal-research.zip and latest.json")


if __name__ == "__main__":
    main()
