# Using this repo from the deep-legal-research skill

Federal, Oregon and Washington stay bundled in the skill. For every other
jurisdiction the skill reads this repo at run time, pinned to a release tag.

## Run-time flow

1. **Phase 1 — pick jurisdictions.** Fetch `index.json` and match the query and
   any cited authorities against each jurisdiction's `citation_patterns`.
   Fetch `jurisdictions/<xx>.md` for each hit and check its sha256 against
   `index.json`. A failed fetch or a mismatch means that jurisdiction has no
   approved source this run: cite by number only, and say so in the banner.
2. **Get the scripts once:** `lsnet.py`, `lstext.py`, `fetch_doc.py`,
   `corpus.py`, plus `hosts.json` and `corpus/index.json`, all from the same
   tag. They are stdlib-only and need `pdftotext`, which the skill already
   requires. Set `LEGAL_SOURCES_BASE=https://raw.githubusercontent.com/jumpingtom1/deep-legal-research-resources/<tag>`.
3. **Statutes and rules:** try `corpus.py resolve "<citation>"` first. A hit
   returns exact official text, its capture date and a freshness verdict.
   Otherwise follow the row's routes: `fetch_doc.py` on the live official page
   or PDF, then the fetch tool to locate and link.
4. **Opinions:** locate the case with the row's search or listing, then use
   `fetch_doc.py read|grep|verify <pdf-url>`. Exact text, every page.
5. **Quotes:**
   - `corpus.py verify` and `fetch_doc.py verify` are exact matches against
     the official text. Either one stands in for the two-fetch rule's second
     fetch.
   - Text read through the fetch tool still needs two fetches that agree.
6. **Refusals:** exit code 3 means refused (blocked host, robots.txt, bot
   challenge). That source is off for the run. Never try another route to it.

## Network setup to tell users and admins

The **script** route needs the official hosts to be reachable from the
code-execution sandbox. The corpus route needs only GitHub.

- **Team / Enterprise.** An owner sets Organization settings → Capabilities →
  network access to *Package managers plus specific domains* and adds:
  - `raw.githubusercontent.com`, for the corpus and the instruction files;
  - each `allowed` host in `hosts.json`, currently:
    - courts.delaware.gov, delcode.delaware.gov, legis.delaware.gov, regulations.delaware.gov
    - www.nysenate.gov, legislation.nysenate.gov, www.nycourts.gov, nycourts.gov, dos.ny.gov
    - courts.ca.gov, www.courts.ca.gov, supreme.courts.ca.gov, oal.ca.gov
    - www.law.cornell.edu, law.justia.com, california.public.law, newyork.public.law
- **Free / Pro / Max.** Turn on network egress under Settings → Capabilities.
- **Without access to a host**, `fetch_doc.py` fails with exit 4 (network) or
  exit 3 (refused). The skill then falls back to the next route the row lists.

Some hosts block scripts but let the fetch tool through (law.justia.com and,
at times, www.nycourts.gov). `fetch_doc.py` reports those as refused, so the
fetch tool remains their only route.

## Maintenance

- **Release checklist:**
  - `python3 scripts/build.py`, which must show no errors;
  - `corpus.py check <collection>` for every collection;
  - re-ingest anything SOURCE CHANGED or STALE;
  - tag a release.

  Then bump the skill's pinned tag.
- **Adding a collection:** write `corpus-config/<xx>-<name>.json`, run
  `ingest.py --dry-run` until every quality gate passes, ingest, then build.
- **Adding a jurisdiction:** follow `research/BRIEF.md`, then
  `research/VERIFY-BRIEF.md`, then build.
