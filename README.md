# deep-legal-research-resources

Free, verified sources for US state (and DC) statutes, constitutions, court
rules, administrative codes, case law and subsequent history. This is the
jurisdiction allowlist and text library for the `deep-legal-research` skill.
Federal, Oregon and Washington stay bundled in the skill; everything else
lives here.

## Layout

| Path | What |
|---|---|
| `SCHEMA.md` | Record format, tier policy, verification vocabulary, read routes, corpus format |
| `INTEGRATION.md` | How the skill uses this repo at run time; network setup for users and admins |
| `data/<xx>.json` | Jurisdiction records (source of truth) |
| `jurisdictions/<xx>.md` | Generated instructions the skill reads. Never hand-edit |
| `index.json` · `hosts.json` | Generated: jurisdiction index with sha256s and citation regexes · live-fetch host allowlist |
| `corpus/` | Pre-built official text, one file per rule or section, plus `corpus/index.json` |
| `corpus-config/` | One ingest config per corpus collection |
| `scripts/build.py` | Validates records, self-tests the regexes, renders the `.md` files, writes the indexes |
| `scripts/fetch_doc.py` | **Script route:** exact text from a live allowlisted page or PDF (read, grep, section, verify) |
| `scripts/corpus.py` | **Corpus route:** list, resolve, get, search, verify, check. Stdlib only; local or raw GitHub |
| `scripts/ingest.py` | Builds a corpus collection, with quality gates. Maintainer-only; needs PyMuPDF |
| `scripts/lsnet.py` · `lstext.py` | Shared code: allowlist, robots, refusals, politeness, cache · extraction and exact quote matching |
| `skill/` | The newest skill release (`deep-legal-research.zip`, without the GovInfo key) and `latest.json`, which the skill's update check reads. See `skill/UPGRADE.md` |
| `scripts/release_skill.py` | Publishes a release into `skill/`, leaving local-only secrets out |
| `research/` | Briefs for the research and verification agents, probe logs, independent-check results |

## Status

See `PRIORITY.md` for the build order and per-jurisdiction status. Done (49 — all): California, Delaware, New York, Texas, Florida, Illinois, Pennsylvania, New Jersey, Massachusetts, Nevada, Idaho, Arizona, Colorado, Georgia, North Carolina, Ohio, Virginia, Maryland, District of Columbia, Minnesota, Michigan, Utah, Montana, Alaska, Hawaii, New Mexico, Wisconsin, Tennessee, Indiana, Missouri, Connecticut, South Carolina, Louisiana, Alabama, Oklahoma, Kentucky, Kansas, Iowa, Nebraska, Arkansas, Mississippi, Maine, New Hampshire, Vermont, Rhode Island, West Virginia, Wyoming, South Dakota, North Dakota. Oregon and Washington stay bundled in the skill.
