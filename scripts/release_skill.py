#!/usr/bin/env python3
"""release_skill.py — publish a deep-legal-research release into skill/.

    python3 scripts/release_skill.py <skill-folder-or-zip> --notes NOTES.md
            [--summary "one line"] [--feedback CONTACT] [--private-out DIR] [--dry-run]

--notes      REQUIRED. A short file of user-facing "- " bullets (1-8, each
             <= 200 characters): what upgrading gets the user. Shown by
             update_check.py for every release newer than the installed one.
--feedback   Where users send suggested improvements (default: the previous
             manifest's value, else the author e-mail in VERSION).
--private-out DIR
             Also write deep-legal-research-v<X.Y>-with-key.zip — the same
             release WITH scripts/govinfo.key — for handing to colleagues.
             DIR must be outside this repository; that zip is never committed.

Builds  skill/deep-legal-research.zip  (one root folder deep-legal-research/,
deterministic order and timestamps) and  skill/latest.json  — the manifest the
skill's own scripts/update_check.py reads to decide whether a newer release
exists and what it brings.

Secrets never reach the public repo: scripts/govinfo.key (the bundled
api.data.gov key, which the skill says may be shared with colleagues but
never posted publicly) and any *.key / *.pem / .env file are left out, and
listed in `preserve_local` so update_check.py copies them from the user's
current installation into the zip it hands over. The script refuses to write
if a remaining text file looks like it holds a credential.

Every zip carries MANIFEST.sha256 (sha256 of every other file; local-only
files excluded) so update_check.py can tell a user when their copy has been
changed since release.

Checks before writing: SKILL.md frontmatter name == folder name; VERSION
parses; the new version is higher than the published one; every file of the
previous release is still present (or listed with --allow-removed); no
__pycache__; release notes present and short.
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
MANIFEST_NAME = "MANIFEST.sha256"
MAX_NOTES, MAX_NOTE_LEN, MAX_HISTORY = 8, 200, 30


def vt(v):
    return tuple(int(x) for x in v.split("."))


def load_tree(src):
    """Return {relative path: bytes} for the skill, from a folder or a zip."""
    src = Path(src)
    files = {}
    if src.is_dir():
        for p in sorted(src.rglob("*")):
            if p.is_file():
                files[p.relative_to(src).as_posix()] = p.read_bytes()
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


def read_notes(path):
    bullets = [ln[2:].strip() for ln in Path(path).read_text().splitlines() if ln.startswith("- ")]
    bullets = [b for b in bullets if b]
    if not 1 <= len(bullets) <= MAX_NOTES:
        sys.exit(f"--notes must hold 1-{MAX_NOTES} '- ' bullets; found {len(bullets)}")
    long_ = [b for b in bullets if len(b) > MAX_NOTE_LEN]
    if long_:
        sys.exit(f"release-note bullets must be <= {MAX_NOTE_LEN} characters: {long_[0][:60]}...")
    return bullets


def build_zip(files):
    """Deterministic zip: one root folder, sorted entries, fixed timestamps."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for d in sorted({"/".join(r.split("/")[:i]) for r in files for i in range(1, r.count("/") + 1)}):
            zi = zipfile.ZipInfo(f"{NAME}/{d}/", date_time=FIXED_TIME)
            zi.external_attr = 0o40755 << 16
            z.writestr(zi, b"")
        for rel in sorted(files):
            zi = zipfile.ZipInfo(f"{NAME}/{rel}", date_time=FIXED_TIME)
            zi.external_attr = (0o755 if rel.endswith(".py") else 0o644) << 16
            z.writestr(zi, files[rel], zipfile.ZIP_DEFLATED)
    return buf.getvalue()


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("--notes", required=True)
    ap.add_argument("--summary", default="")
    ap.add_argument("--feedback", default=None)
    ap.add_argument("--private-out", type=Path, default=None)
    ap.add_argument("--allow-removed", nargs="*", default=[])
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    notes = read_notes(a.notes)
    if a.private_out:
        po = a.private_out.resolve()
        if po == ROOT or ROOT in po.parents:
            sys.exit("--private-out must be outside this repository (the keyed zip is never committed)")

    files = load_tree(a.source)
    if "SKILL.md" not in files or "VERSION" not in files:
        sys.exit("source has no SKILL.md or VERSION at its root")
    fm = re.match(rb"---\s*\n(.*?)\n---", files["SKILL.md"], re.S)
    m = fm and re.search(rb"^name:\s*(\S+)", fm.group(1), re.M)
    if not m or m.group(1).decode() != NAME:
        sys.exit(f"SKILL.md frontmatter name must be {NAME!r}")
    vm = re.search(rb"version:\s*([\d.]+)", files["VERSION"])
    dm = re.search(rb"last_modified:\s*([\d-]+)", files["VERSION"])
    am = re.search(rb"author:.*?([\w.+-]+@[\w-]+\.[\w.]+)", files["VERSION"])
    if not vm:
        sys.exit("VERSION has no version: line")
    version = vm.group(1).decode()
    released = dm.group(1).decode() if dm else date.today().isoformat()

    kept, dropped = {}, []
    for rel, data in files.items():
        parts = rel.split("/")
        if (set(parts) & EXCLUDE_DIRS) or parts[-1] in EXCLUDE_NAMES or rel.endswith(EXCLUDE_SUFFIX) \
                or parts[-1].startswith(".env"):
            dropped.append(rel)
            continue
        if rel == MANIFEST_NAME:
            continue                      # regenerated below
        if SECRET_RX.search(data):
            sys.exit(f"{rel} looks like it contains a credential — remove it before publishing")
        kept[rel] = data

    prev = {}
    if (OUT / "latest.json").exists():
        prev = json.loads((OUT / "latest.json").read_text())
        if vt(version) <= vt(prev["version"]):
            sys.exit(f"version {version} is not higher than the published {prev['version']}")
        gone = [f for f in prev.get("files", []) if f != MANIFEST_NAME
                and f not in kept and f not in a.allow_removed]
        if gone:
            sys.exit(f"files in the previous release are missing: {gone} (use --allow-removed)")

    # Fingerprint of every shipped file, so update_check can spot local edits.
    kept[MANIFEST_NAME] = "".join(f"{hashlib.sha256(kept[r]).hexdigest()}  {r}\n"
                                  for r in sorted(kept)).encode()
    blob = build_zip(kept)

    history = list(prev.get("history", []))
    if prev and not history:          # seed from a pre-history manifest (v10.4)
        history = [{"version": prev["version"], "released": prev.get("released", ""),
                    "notes": [prev["summary"]] if prev.get("summary") else []}]
    history = [h for h in history if h.get("version") != version]
    history.append({"version": version, "released": released, "notes": notes})
    history = sorted(history, key=lambda h: vt(h["version"]))[-MAX_HISTORY:]
    feedback = a.feedback or prev.get("feedback") or (am.group(1).decode() if am else "")

    manifest = {
        "name": NAME,
        "version": version,
        "released": released,
        "published": date.today().isoformat(),
        "summary": a.summary or notes[0],
        "notes": notes,
        "history": history,
        "feedback": feedback,
        "zip_url": RAW + "deep-legal-research.zip",
        "sha256": hashlib.sha256(blob).hexdigest(),
        "bytes": len(blob),
        "files": sorted(kept),
        "preserve_local": [p for p in PRESERVE_LOCAL if p in files or p in dropped],
        "excluded_from_public_zip": sorted(dropped),
    }
    print(f"{NAME} v{version}: {len(kept)} files, {len(blob):,} bytes, sha256 {manifest['sha256'][:16]}")
    print(f"  left out (local-only): {', '.join(sorted(dropped)) or '—'}")
    print(f"  feedback contact: {feedback or '—'}")
    print("  what's new:")
    for n in notes:
        print(f"    - {n}")
    if a.dry_run:
        print("  dry run — nothing written")
        return
    OUT.mkdir(exist_ok=True)
    (OUT / "deep-legal-research.zip").write_bytes(blob)
    (OUT / "latest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    print(f"  wrote {OUT.relative_to(ROOT)}/deep-legal-research.zip and latest.json")
    if a.private_out:
        priv = dict(kept)
        for rel in manifest["preserve_local"]:
            if rel in files:
                priv[rel] = files[rel]
        a.private_out.mkdir(parents=True, exist_ok=True)
        pz = a.private_out / f"{NAME}-v{version}-with-key.zip"
        pz.write_bytes(build_zip(priv))
        print(f"  wrote colleague zip WITH key: {pz}  (never commit or post it)")


if __name__ == "__main__":
    main()
