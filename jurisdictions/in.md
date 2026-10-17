# Indiana (IN) — free legal sources

_Generated from `data/in.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Court rules are the strongest family: rules.incourts.gov serves every statewide rule set as static per-rule HTML (constructible) plus whole-set PDFs, both script-readable. Opinions since mid-2005 come from a plain-GET JSON API behind public.courts.in.gov/decisions, with PDFs on the same host; transfer dispositions are weekly clerk PDFs on in.gov. The official Code, Constitution, Administrative Code and Register (iga.in.gov, iar.iga.in.gov) are JavaScript-only apps that neither route can read, so statutes and the Constitution fall back to Justia (fetch tool only) and the IAC to Cornell LII. MyCase dockets are robots-disallowed.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Indiana Supreme Court | `ind (unverified)` | Ind. | N.E.3d, N.E.2d, N.E., Ind. | — |
| Indiana Court of Appeals | `indctapp (unverified)` | Ind. Ct. App. | N.E.3d, N.E.2d, N.E., Ind. App. | — |
| Indiana Tax Court | `indtc (unverified)` | Ind. T.C. | N.E.3d, N.E.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Indiana Code | `Ind. Code § 34-11-2-4`; `Ind. Code Ann. § 35-42-1-1`; `I.C. § 34-11-2-4`; `IC 6-1.1-10-16`; `Indiana Code section 34-11-2-4`; `section 35-38-1-7.1 of the Indiana Code`; `Ind. Code §§ 34-11-2-4 to -7` | `in-code-justia` → `in-code-iga` |
| Indiana Constitution | `Ind. Const. art. 1, § 12`; `Ind. Const. art. 7, § 4`; `Article 1, Section 12 of the Indiana Constitution`; `Indiana Constitution Article 1, Section 23` | `in-constitution-justia` → `in-constitution-iga` |
| Indiana court rules (with Ind./Indiana marker) | `Ind. Trial Rule 12(B)(6)`; `Ind. T.R. 56(C)`; `Ind. Evidence Rule 702`; `Ind. Appellate Rule 65(D)`; `Ind. App. R. 65(D)`; `Ind. Crim. Rule 4(C)`; `Ind. Professional Conduct Rule 1.7`; `Ind. Admission and Discipline Rule 23`; `Indiana Trial Rule 56` | `in-rules-incourts` → `in-rules-pdf` |
| Indiana court rules (prose: 'of the Indiana Rules of ...') | `Rule 12(B)(6) of the Indiana Rules of Trial Procedure`; `Rule 702 of the Indiana Rules of Evidence`; `Rule 1.7 of the Indiana Rules of Professional Conduct` | `in-rules-incourts` → `in-rules-pdf` |
| Indiana court rules, bare short forms (T.R., Trial Rule, Evid. R., App. R., Crim. R., Prof. Cond. R., Admis. Disc. R.) *(only once this jurisdiction is known)* | `T.R. 56(C)`; `Trial Rule 12(B)(6)`; `Evidence Rule 702`; `Appellate Rule 65(D)`; `Criminal Rule 4(C)`; `Admis. Disc. R. 23` | `in-rules-incourts` → `in-rules-pdf` |
| Indiana Administrative Code | `410 IAC 1-1-1`; `312 IAC 9-2-2`; `170 IAC 1-1.1-1`; `410 Ind. Admin. Code 1-1-1` | `in-admincode-lii` → `in-admincode-iar` |
| Indiana Register document IDs | `20211208-IR-410210385RFA`; `20241204-IR-170240381RNA` | `in-register-iar` |
| Reporter citations with Indiana parenthetical (N.E., Ind., Ind. App.) | `275 N.E.3d 505 (Ind. 2026)`; `141 N.E.3d 384, 386 (Ind. 2020)`; `247 N.E.3d 1 (Ind. Ct. App. 2024)`; `33 N.E.3d 1 (Ind. T.C. 2015)`; `260 Ind. 123`; `150 Ind. App. 61` | `in-opinions-decisions-api` → `in-cases-justia` |
| Bare North Eastern Reporter citation (no court parenthetical) *(only once this jurisdiction is known)* | `275 N.E.3d 505`; `141 N.E.3d 384, 386` | `in-opinions-decisions-api` → `in-cases-justia` |
| Indiana appellate docket numbers (old and post-2021 styles) | `No. 26A-DC-221`; `No. 25S-PL-103`; `No. 49S02-1608-CT-00431`; `26A-DC-00221` | `in-opinions-decisions-api` → `in-transfer-dispositions` |
| Memorandum decisions / Westlaw cites with Indiana parenthetical | `No. 23A-CR-1234, 2023 WL 6453411 (Ind. Ct. App. Oct. 4, 2023) (mem.)`; `2024 WL 112233 (Ind. Ct. App. 2024)` | `in-opinions-decisions-api` → `in-cases-justia` |
| Indiana transfer history (trans. denied / trans. granted / trans. not sought) *(only once this jurisdiction is known)* | `trans. denied`; `trans. not sought`; `trans. granted` | `in-transfer-dispositions` |

Regexes (case-insensitive):

- Indiana Code: `(?:Ind(?:\.|iana)\s*Code(?:\s+Ann\.)?\s*(?:§§?|sec(?:tion|\.)s?)?\s*|\bI\.\s?C\.\s*§§?\s*|\bIC\s+)(?P<title>\d{1,2})-(?P<article>\d{1,2}(?:\.\d{1,2})?)-(?P<chapter>\d{1,2}(?:\.\d{1,2})?)-(?P<section>\d{1,3}(?:\.\d{1,2})?)(?![\d])|(?:sec(?:tion|\.)|§)\s*(?P<title2>\d{1,2})-(?P<article2>\d{1,2}(?:\.\d{1,2})?)-(?P<chapter2>\d{1,2}(?:\.\d{1,2})?)-(?P<section2>\d{1,3}(?:\.\d{1,2})?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Indiana\s+Code`
- Indiana Constitution: `Ind(?:\.|iana)\s*Const(?:\.|itution)\s*,?\s*art(?:\.|icle)\s*(?P<article>\d{1,2}|[IVX]+),?\s*(?:§|sec(?:tion|\.))\s*(?P<section>\d{1,2})|Article\s+(?P<article2>\d{1,2}|[IVX]+),?\s+Section\s+(?P<section2>\d{1,2})\s+of\s+the\s+Indiana\s+Constitution|Indiana\s+Constitution,?\s+Article\s+(?P<article3>\d{1,2}|[IVX]+),?\s+Section\s+(?P<section3>\d{1,2})`
- Indiana court rules (with Ind./Indiana marker): `Ind(?:\.|iana)\s+(?P<set>Trial|T\.\s?R\.|Evid(?:ence|\.)|App(?:ellate|\.)|Crim(?:inal|\.)|Prof(?:essional|\.)\s*Cond(?:uct|\.)|Admis(?:sion|\.)\s*(?:and\s+|&\s*)?Disc(?:ipline|\.)|Small\s+Claims|Post-Conviction|Jury|Tax\s+Court)\s*(?:Rule|R\.)?\s*(?P<rule>\d{1,3}(?:\.\d{1,2})?)`
- Indiana court rules (prose: 'of the Indiana Rules of ...'): `Rule\s+(?P<rule>\d{1,3}(?:\.\d{1,2})?)(?:\s*\([A-Za-z0-9]+\))*\s+of\s+the\s+Indiana\s+Rules\s+(?:of|for)\s+(?P<set>(?:Trial\s+Procedure|Evidence|Appellate\s+Procedure|Criminal\s+Procedure|Professional\s+Conduct|Admission\s+and\s+Discipline|Small\s+Claims|Post-Conviction\s+Remedies|Jury\s+Rules|Tax\s+Court|Court))`
- Indiana court rules, bare short forms (T.R., Trial Rule, Evid. R., App. R., Crim. R., Prof. Cond. R., Admis. Disc. R.): `(?<![\w.])(?P<set>T\.\s?R\.|Trial\s+Rule|Evid(?:\.\s?R\.|ence\s+Rule)|App(?:\.\s?R\.|ellate\s+Rule)|Crim(?:\.\s?R\.|inal\s+Rule)|Prof\.\s*Cond\.\s*R\.|Admis\.\s*Disc\.\s*R\.)\s*(?P<rule>\d{1,3}(?:\.\d{1,2})?)`
- Indiana Administrative Code: `(?P<title>\d{1,3})\s+(?:IAC|Ind\.\s*Admin\.\s*Code)\s+(?P<article>\d{1,3}(?:\.\d{1,2})?)-(?P<rule>\d{1,3}(?:\.\d{1,2})?)(?:-(?P<section>\d{1,3}(?:\.\d{1,2})?))?`
- Indiana Register document IDs: `(?P<date>(?:19|20)\d{6})-IR-(?P<docid>\d{9}[A-Z]{2,4})`
- Reporter citations with Indiana parenthetical (N.E., Ind., Ind. App.): `(?P<volume>\d{1,4})\s+N\.E\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+(?:[-–]\d+)?)?\s*\((?P<court>Ind\.(?:\s*(?:Ct\.\s*)?App\.|\s*T\.\s?C\.|\s*Tax)?)\s*(?:[A-Z][a-z]{2,3}\.?\s+\d{1,2},\s+)?(?P<year>\d{4})\)|(?P<volume2>\d{1,3})\s+Ind\.(?:\s*(?P<app>App)\.)?\s+(?P<page2>\d{1,4})(?![\d.])`
- Bare North Eastern Reporter citation (no court parenthetical): `(?P<volume>\d{1,4})\s+N\.E\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})`
- Indiana appellate docket numbers (old and post-2021 styles): `\b(?P<yy>\d{2})(?P<court>[AST])-(?P<ctype>[A-Z]{2})-(?P<num>\d{1,5})\b|\b(?P<county>\d{2})(?P<court2>[AST])(?P<dist>\d{2})-(?P<yymm>\d{4})-(?P<ctype2>[A-Z]{2})-(?P<num2>\d{1,5})\b`
- Memorandum decisions / Westlaw cites with Indiana parenthetical: `(?P<year>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\((?P<court>Ind\.(?:\s*(?:Ct\.\s*)?App\.|\s*T\.\s?C\.)?)`
- Indiana transfer history (trans. denied / trans. granted / trans. not sought): `\btrans\.\s+(?P<disp>denied|granted|not\s+sought|dismissed|vacated)`

Short forms → URL key:

T.R. → `trial`; Tr. R. → `trial`; Trial Rule → `trial`; Ind. Trial Rule → `trial`; Ind. T.R. → `trial`; Rules of Trial Procedure → `trial`; Evid. R. → `evidence`; Ind. Evid. R. → `evidence`; Evidence Rule → `evidence`; Ind. Evidence Rule → `evidence`; Rules of Evidence → `evidence`; App. R. → `appellate`; Ind. App. R. → `appellate`; Appellate Rule → `appellate`; Ind. Appellate Rule → `appellate`; Rules of Appellate Procedure → `appellate`; Crim. R. → `criminal`; Ind. Crim. Rule → `criminal`; Criminal Rule → `criminal`; Rules of Criminal Procedure → `criminal`; Prof. Cond. R. → `prof-conduct`; Professional Conduct Rule → `prof-conduct`; Rules of Professional Conduct → `prof-conduct`; Admis. Disc. R. → `admission-discipline`; Admission and Discipline Rule → `admission-discipline`; Rules for Admission to the Bar and the Discipline of Attorneys → `admission-discipline`; S.C.R. → `small-claims`; Small Claims Rule → `small-claims`; P-C.R. → `post-conviction`; Post-Conviction Rule → `post-conviction`; Jury Rule → `jury`; Tax Court Rule → `tax`; Admin. R. → `admin`; Administrative Rule → `admin`; A.R. → `admin`; Original Action Rule → `original-actions`; A.D.R. → `adr`; ADR Rule → `adr`; Judicial Conduct Rule → `judicial-conduct`

Statute forms require the four-part Indiana number (title-article-chapter-section) after 'Ind. Code', 'I.C. §' or 'IC'; Idaho's 'I.C. § 5-219' (two parts) must not route here. Bare rule short forms (T.R., Trial Rule, Evid. R., App. R., Crim. R., Prof. Cond. R.) are context_required; the abbreviated 'Evid. R.', 'App. R.', 'Crim. R.', 'Prof. Cond. R.' forms (even after 'Ind.') are also matched by Ohio's patterns, so examples use the spelled-out Indiana forms. Old-style dockets like 49A02-1509-CT-1234 are matched by this regex but also overlap D.C./N.C. docket patterns — route them only with Indiana context. law_aliases map rule-set short forms to the rules.incourts.gov {set} key. Indiana has no public-domain citation; App. R. 65(D): memorandum decisions issued on or after Jan. 1, 2023 may be cited for persuasive value. 'trans. denied' is Indiana usage but kept context_required as a bare history phrase.

## A. Statutes / code

### `in-code-iga` — Indiana Code (iga.in.gov)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Indiana General Assembly / Legislative Services Agency · text: **link-only** · official: unknown
- **Coverage:** Current and prior-year Indiana Code by title (reported), Constitution, Acts of Indiana, bill PDFs; IC downloads page reported at /laws/ic/downloads.
- **Access:** `link-only` · format html
  - Placeholders: Reported pattern https://iga.in.gov/laws/{year}/ic/titles/{title} (title unpadded in 2025 links seen in search results; '021' zero-padded in a 2020 link). Not usable: JS-only.
  - Index: `https://iga.in.gov/laws/ic/downloads`
  - Navigation: JS single-page app; no server-rendered links.
  - Read via: in-code-justia (tier 2) for text
- **Automation:** WebFetch fail · shell http-error · robots: /robots.txt returns the same HTML app shell (sha256 61d9d1265c828684), i.e. no robots rules
  - Script: every path (titles/34, /api/…, …/Title_34.pdf, /static/js bundle) returns the identical 0-char shell, served from S3/CloudFront catch-all. WebFetch of /laws/ic/downloads (search-result URL) returned 'You need to enable JavaScript to run this app.'; WebFetch of built /laws/2025/ic/titles/34 was gated (permission timeout).
- **Currency:** none readable
- **Official status:** Not determined: every iga.in.gov path returns the same 691-byte React shell to both routes, so no disclaimer or authentication statement could be read.
- **Hazard:** JavaScript-only app: neither route sees statute text
- **Hazard:** the shell is returned with HTTP 200 for every path, so a 200 does not mean the document exists
- **Probe:** Ind. Code § 34-11-2-4 → `https://iga.in.gov/laws/2025/ic/titles/34` — expect: "An action for: (1) injury to person or character"
- **Evidence (2026-10-17):** fetch_doc --research info: kind=html chars=0 sha256=61d9d1265c828684 (same as /robots.txt and /); WebFetch /laws/ic/downloads: JS shell only.
- **Notes:** Official publisher of the Code; keep as the link target. Text must come from in-code-justia until an IGA endpoint that serves text is found.

### `in-code-justia` — Indiana Code (Justia)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Indiana Code by edition year (2025 is current default; prior years under /codes/indiana/{year}/).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/indiana/title-{title}/article-{article}/chapter-{chapter}/section-{title}-{article}-{chapter}-{section}/`
  - Placeholders: IC t-a-c-s maps directly; dots in a component become hyphens in the path segment (article 34.1 -> article-34-1, seen as /2023/title-25/article-34-1/chapter-1); the section slug keeps the full number. Unversioned URLs serve the latest edition (2025 heading); prefix /{year}/ after /indiana/ for an older edition.
  - Index: `https://law.justia.com/codes/indiana/`
  - Navigation: title page lists articles; article page lists chapters; chapter page lists sections (no text).
- **Automation:** WebFetch ok · shell blocked-challenge · robots: script refused law.justia.com for the day (robots.txt challenge 2026-10-17 09:44)
  - Built per-section URLs went through WebFetch without a gate. Use the fetch tool only (bot wall policy).
- **Currency:** edition heading and universal citation at top of section page; disclaimer at foot — observed: "2025 Indiana Code ... IN Code § 34-11-2-4 (2025)"
- **Official status:** Page states 'These codes may not be the most recent version.' and points to the official state site.
- **Hazard:** edition lags the official code by a session
- **Hazard:** tier 2: disclose with currency string
- **Probe:** Ind. Code § 34-11-2-4 → `https://law.justia.com/codes/indiana/title-34/article-11/chapter-2/section-34-11-2-4/` — expect: "An action for: (1) injury to person or character"
- **Evidence (2026-10-17):** WebFetch: body present 'Sec. 4. (a) An action for: (1) injury to person', complete (a)-(d). Second citation IC 35-42-1-1 at /title-35/article-42/chapter-1/section-35-42-1-1/: 'Sec. 1. A person who: (1) knowingly or intentionally kills', 2025 edition.

## B. Constitution

### `in-constitution-iga` — Constitution of the State of Indiana (iga.in.gov)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Indiana General Assembly · text: **link-only** · official: unknown
- **Coverage:** Current amended Constitution (reported, published with the Indiana Code).
- **Access:** `link-only` · format html
  - Index: `https://iga.in.gov/`
  - Navigation: JS-only app; no static route found.
  - Read via: in-constitution-justia
- **Automation:** WebFetch fail · shell http-error · robots: none (HTML shell)
  - Same 0-char shell as in-code-iga.
- **Currency:** none readable
- **Official status:** Not readable (JS app).
- **Hazard:** JS-only
- **Probe:** Ind. Const. art. 1, § 12 → `https://iga.in.gov/` — expect: "All courts shall be open"
- **Evidence (2026-10-17):** fetch_doc: chars=0 shell for every iga.in.gov path.
- **Notes:** www.in.gov/history '/constitution-of-1851/' pages are the 1851 text 'as originally written' (historical, not current); do not cite them for current text.

### `in-constitution-justia` — Indiana Constitution (Justia)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Articles 1-16, one page per article, section history notes.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/indiana/art{article}.html`
  - Placeholders: article in Arabic numerals, unpadded (art1.html). Sections are on the article page.
  - Index: `https://law.justia.com/constitution/indiana/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com robots challenge to script 2026-10-17
  - fetch tool only
- **Currency:** history note after each section; disclaimer at foot — observed: "(History: As Amended November 6, 1984)."
- **Official status:** Page: 'This Constitution may not be the most recent version.'
- **Hazard:** the fetch tool reported Article 1 running through Section 37; Art. 1 § 39 (2016 amendment) may be missing — check currency before relying on recent amendments
- **Probe:** Ind. Const. art. 1, § 12 → `https://law.justia.com/constitution/indiana/art1.html` — expect: "All courts shall be open; and every person, for injury"
- **Evidence (2026-10-17):** WebFetch: § 12 body present 'All courts shall be open; and every person, for injury', not truncated.

## C. Court rules

### `in-rules-incourts` — Indiana Rules of Court (rules.incourts.gov, per-rule HTML)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Indiana Supreme Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** All statewide rule sets: Trial Procedure, Evidence, Appellate, Criminal (restyled numbering 1.1… effective Jan. 1, 2024), Professional Conduct, Admission & Discipline, Small Claims, Post-Conviction, Jury, Tax Court, Administrative, Access to Court Records, Original Actions, ADR, Judicial Conduct, Child Support, Parenting Time, etc. Prior versions linked as dated pages ({MM-DD-YYYY}.htm). Local rules: https://www.in.gov/courts/publications/local-rules/ (not probed).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://rules.incourts.gov/Content/{set}/rule{rule}/current.htm`
  - Placeholders: set keys (law_aliases): trial, evidence, appellate, criminal, prof-conduct, admission-discipline, small-claims, post-conviction, jury, tax, admin, records, original-actions, adr, judicial-conduct, child-support, parenting, commercial, problem-solving, trial-denovo. rule = number with '.' replaced by '-' (T.R. 3.1 -> rule3-1; Prof. Cond. 1.7 -> rule1-7; Crim. 1.1 -> rule1-1). Subdivisions ((B)(6)) are on the rule page. Preamble/scope pages: /prof-conduct/preamble/current.htm.
  - Index: `https://rules.incourts.gov/Content/index.htm`
  - Navigation: index.htm lists sets -> /Content/{set}/default.htm lists every rule with links.
- **Automation:** WebFetch ok · shell ok · robots: none (404)
  - The bare host root https://rules.incourts.gov/ is a JS shell (0 chars); /Content/… pages are static HTML. rulesqa.incourts.gov is a QA mirror — never use.
- **Currency:** line under the rule heading — observed: "Effective July 1, 2026 (T.R. 12)"
- **Official status:** No official/unofficial statement on rule pages (WebFetch: 'no disclaimer about official status'). Amendment orders are at https://www.in.gov/courts/public-records/orders/rules/.
- **Hazard:** rule pages include ~1.5K chars of navigation before the heading
- **Hazard:** Criminal Rules renumbered 2024: old 'Crim. R. 4(C)' is now Rule 4 in the restyled set — check the effective-date line
- **Probe:** Ind. Trial Rule 12(B)(6) → `https://rules.incourts.gov/Content/trial/rule12/current.htm` — expect: "Failure to state a claim upon which relief can be granted"
- **Evidence (2026-10-17):** fetch_doc grep: T.R. 12 'Effective July 1, 2026 (A) When presented'; Evid. R. 702 'A witness who is qualified as an expert by knowledge'; App. R. 65 'memorandum decision issued on or after January 1, 2023, may be cited for persuasive value'; Prof. Cond. 1.7, Crim. 1.1 OK. WebFetch T.R. 1 (search-result URL): body present, 'Effective January 1, 2026'.

### `in-rules-pdf` — Indiana Rules of Court — whole-set PDFs

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Indiana Supreme Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** One PDF per rule set, with TOC and 'Effective' line per rule.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://rules.incourts.gov/pdf/PDF%20-%20{Set}/{set}.pdf`
  - Placeholders: Trial/trial.pdf (216 pp), Evidence/evidence.pdf (50 pp), Appellate/appellate.pdf (116 pp), Criminal/criminal.pdf (36 pp), 'Professional Conduct'/professional-conduct.pdf (170 pp), 'Admission Discipline'/admission-discipline.pdf (194 pp). Take others from the set's default.htm.
  - Index: `https://rules.incourts.gov/Content/index.htm`
  - Navigation: /Content/{set}/default.htm carries the PDF link.
- **Automation:** WebFetch untested · shell ok · robots: none (404)
  - Space in directory name must be %20-encoded.
- **Currency:** Last-Modified header; per-rule 'Effective' line — observed: "Last-Modified 31 Jul 2026; T.R. 12 'Effective July 1, 2026'"
- **Official status:** As in-rules-incourts.
- **Hazard:** long PDFs exceed the fetch tool's ~100K-char window (trial.pdf 462K chars)
- **Probe:** Ind. Trial Rule 12 → `https://rules.incourts.gov/pdf/PDF%20-%20Trial/trial.pdf` — expect: "Rule 12. Defenses, objections, and motions on the pleadings"
- **Evidence (2026-10-17):** fetch_doc info: pdf 216 pages 462,254 chars; grep found 'Rule 12. Defenses, objections…' at page 51 with 'Effective July 1, 2026'.

## D. Administrative code

### `in-admincode-iar` — Indiana Administrative Code (iar.iga.in.gov)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Legislative Services Agency · text: **link-only** · official: unknown
- **Coverage:** Current IAC by title/article (reported).
- **Access:** `link-only` · format html
  - Index: `https://iar.iga.in.gov/`
  - Navigation: JS single-page app; every path returns the same shell.
  - Read via: in-admincode-lii (tier 2)
- **Automation:** WebFetch untested · shell http-error · robots: /robots.txt returns the app shell (sha256 f91bd4e755d1cdd9) — no rules
  - fetch_doc: '/', '/code/current/410' identical 0-char shell. Legacy host iac.iga.in.gov (linked from rules.incourts.gov) failed TLS handshake (UNEXPECTED_EOF) on robots.txt.
- **Currency:** none readable
- **Official status:** Not readable (JS app).
- **Hazard:** JS-only
- **Probe:** 410 IAC 1-1-1 → `https://iar.iga.in.gov/code/current/410` — expect: "Every child less than nineteen (19) years of age"
- **Evidence (2026-10-17):** kind=html chars=0 sha256=f91bd4e755d1cdd9 for every path.

### `in-admincode-lii` — Indiana Administrative Code (Cornell LII)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All IAC titles, one page per section with Authority/Affected lines and Indiana Register history notes.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/indiana/{title}-IAC-{article}-{rule}-{section}`
  - Placeholders: Section number verbatim incl. dots (170-IAC-1-1.1-1). Rule-level index URLs are irregular (title-410/article-1/rule-410-IAC-1-1 vs rule-2) — navigate if needed.
  - Index: `https://www.law.cornell.edu/regulations/indiana`
  - Navigation: title-{t} -> article-{a} -> rule page -> section
- **Automation:** WebFetch untested · shell ok · robots: permits (script check OK)
- **Currency:** foot of section page — observed: "State regulations are updated quarterly; we currently have two versions available."
- **Official status:** Third-party; 'State regulations are updated quarterly'.
- **Hazard:** LII mislabels Title 410 as 'INDIANA UTILITY REGULATORY COMMISSION' (410 is the Department of Health) — ignore its title captions
- **Hazard:** quarterly lag
- **Probe:** 410 IAC 1-1-1 → `https://www.law.cornell.edu/regulations/indiana/410-IAC-1-1-1` — expect: "Every child less than nineteen (19) years of age residing in Indiana"
- **Evidence (2026-10-17):** fetch_doc grep: 410-IAC-1-1-1 'Sec. 1. Every child less than nineteen (19) years of age'; 170-IAC-1-1.1-1 'This rule shall govern the practice and procedure'; 312-IAC-9-2-2 'An individual must not take or chase a wild mammal'.

## D. Administrative register

### `in-register-iar` — Indiana Register (iar.iga.in.gov)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Legislative Services Agency · text: **link-only** · official: unknown
- **Coverage:** Indiana Register documents, IDs like 20211208-IR-410210385RFA (date-IR-title+year+LSA no.+type).
- **Access:** `link-only` · format html
  - Index: `https://iar.iga.in.gov/`
  - Navigation: JS app.
- **Automation:** WebFetch untested · shell http-error · robots: app shell, no rules
  - Agencies sometimes host their own copies (e.g. secure.in.gov/iurc/files/20241204-IR-170240381RNA.pdf, seen in search, not fetched).
- **Currency:** none readable
- **Official status:** Not readable (JS app).
- **Hazard:** JS-only
- **Probe:** 20211208-IR-410210385RFA → `https://iar.iga.in.gov/`
- **Evidence (2026-10-17):** 0-char shell.

## E. Case law

### `in-opinions-decisions-api` — Indiana Appellate Decisions (public.courts.in.gov/decisions + JSON API)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Indiana Supreme Court / Clerk of the Courts · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court, Court of Appeals and Tax Court opinions, memorandum decisions (isMemorandum flag) and some orders, from mid-2005 (earliest Supreme Court row 6/23/2005; help page says collection dates back to 2005). Up to 250 results per query.
- **Read via (in order):** **script**
- **Access:** `search-only` · format json
  - Pattern: `https://public.courts.in.gov/Decisions/api/Search?courtId={court}&fromDate={MM/DD/YYYY}&toDate={MM/DD/YYYY}&caseParty={word}&showMemorandum=true`
  - Placeholders: Plain GET returning JSON. courtId: 9510 Supreme Court, 9530 Court of Appeals, 9550 Tax Court (from /Decisions/api/Dropdown/Court). Other params: caseCategoryId, judgeId, countyId (dropdowns at /Decisions/api/Dropdown/{CaseCategory|Judge|County}). Without showMemorandum=true memorandum decisions are omitted (Sept 1-5 2026 COA: 7 vs 30 rows). Each row: style, caseNumber (e.g. 26A-DC-00221), date, decision, isMemorandum, courts[] with trial-court cause numbers, opinionUrl (relative: prefix https://public.courts.in.gov/Decisions/). There is no docket-number parameter: search by party word + date range, then match caseNumber.
  - Index: `https://public.courts.in.gov/decisions`
  - Navigation: API row -> opinionUrl 'api/Document/Opinion?Id=…' returns the PDF (filename Opinion.pdf).
  - Read via: opinion PDFs on the same host (script ok)
- **Automation:** WebFetch untested · shell ok · robots: Disallows /MyCase/ca…, /Appellate, /Docket, /*.pdf etc.; /Decisions/ and /Decisions/api/… not covered (script check OK)
  - The /decisions page itself is a Vue app (no rows server-side). Opinion document URLs have no .pdf suffix, so the /*.pdf disallow does not apply. detailsUrl links into MyCase (/mycase/#/vw/CaseSummary/…), whose data calls are robots-disallowed.
- **Currency:** date field per row — observed: "newest row 10/16/2026"
- **Official status:** Footer: information on this site 'is not to be considered or used as an official court record'.
- **Hazard:** slip pagination only ('Page 1 of 29'); N.E.3d pages must come from elsewhere
- **Hazard:** Id tokens in opinionUrl are opaque; take them from the API
- **Hazard:** 250-row cap per query: narrow by date
- **Probe:** Walls v. Walls, No. 26A-DC-221 (Ind. Ct. App. Oct. 16, 2026) → `https://public.courts.in.gov/Decisions/api/Search?caseParty=Walls&fromDate=10/01/2026&toDate=10/17/2026` — expect: ""caseNumber":"26A-DC-00221""
- **Evidence (2026-10-17):** fetch_doc: Search JSON 1 row 26A-DC-00221; opinionUrl -> pdf 29 pages 54,398 chars, footer 'Court of Appeals of Indiana | Opinion 26A-DC-221 | October 16, 2026 Page 1 of 29'. Year probes: Supreme Court 2008 101 rows, 2005 earliest 6/23/2005, 2004 0 rows.
- **Notes:** Docket formats: since 2021 'YYA-CT-NNNNN' (COA), 'YYS-CT-NNNNN' (Supreme), 'YYT-TA-…' (Tax); API zero-pads to 5 digits, opinions print unpadded (26A-DC-221). Older: '49A02-1509-CT-1234' / '49S02-1608-CT-00431' (county, court, district, yymm, type, number).

### `in-cases-justia` — Indiana case law (Justia)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court, Court of Appeals, Tax Court by year; full opinion text.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/cases/indiana/supreme-court/{year}/{docket-lowercase}.html`
  - Placeholders: observed for post-2021 dockets: 25S-PL-00103 -> 25s-pl-00103.html (5-digit zero-padded). Other courts: /cases/indiana/court-of-appeals/{year}/, /cases/indiana/tax-court/{year}/ (reported, not fetched).
  - Index: `https://law.justia.com/cases/indiana/supreme-court/2025/`
  - Navigation: year page lists cases with docket numbers -> case page.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: script refused (robots challenge) 2026-10-17
  - fetch tool only
- **Currency:** none stated
- **Official status:** Third-party compilation.
- **Hazard:** no N.E.3d cite for the opinion itself
- **Hazard:** text-extraction artifacts (footnotes, attorney lists)
- **Probe:** Brooks v. USA Track & Field, Inc., No. 25S-PL-00103 (Ind. 2025) → `https://law.justia.com/cases/indiana/supreme-court/2025/25s-pl-00103.html` — expect: "This case concerns application of the final judgment rule"
- **Evidence (2026-10-17):** WebFetch: full opinion with dissent, 'Massa, Justice. This case concerns application of the final judgment rule', ends 'Page 6 of 6'.

## F. Subsequent history

### `in-mycase` — MyCase / appellate docket (public.courts.in.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Indiana Office of Judicial Administration · text: **link-only** · official: unofficial
- **Coverage:** Trial and appellate dockets incl. transfer filings and orders.
- **Access:** `link-only` · format html
  - Index: `https://public.courts.in.gov/mycase/`
  - Navigation: JS app; case summaries reachable only via data calls under /mycase/Case… which robots disallows.
- **Automation:** WebFetch blocked · shell blocked-robots · robots: Disallow: /MYCASE/ca (+case variants), /Appellate, /AppellateDocket, /Docket, /*.pdf …
  - fetch_doc check: /mycase/Case/CaseSummary REFUSED (rule Disallow: /MYCASE/ca); /Appellate/ REFUSED. Give users the decisions API detailsUrl as a link only.
- **Currency:** n/a
- **Official status:** Footer: 'not to be considered or used as an official court record'.
- **Hazard:** robots-disallowed
- **Probe:** 26A-DC-221 docket → `https://public.courts.in.gov/mycase/Case/CaseSummary`
- **Evidence (2026-10-17):** REFUSED: robots.txt on public.courts.in.gov disallows /mycase/Case/CaseSummary (rule: Disallow: /MYCASE/ca).

### `in-transfer-dispositions` — Indiana Supreme Court transfer dispositions (weekly lists)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Clerk of the Indiana Supreme Court, Court of Appeals, and Tax Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** Weekly lists of petitions to transfer granted/denied, 2024-2026 in the archive selector; each row: COA docket, style, petitioner, Granted/Denied, vote, date, COA panel, FP / mem. dec., COA decision date.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Placeholders: File names are irregular (transfer-2026-1009.pdf, transfer-list-2026-1002.xlsx, /dA/{hash}/transfer-2026-0109.pdf) — take links from the index.
  - Index: `https://www.in.gov/courts/clerk/transfer/`
  - Navigation: index (week ending, totals, PDF/XLSX links; year archive selector) -> weekly PDF -> grep the COA docket number (e.g. 25A-CR-338).
- **Automation:** WebFetch untested · shell ok · robots: www.in.gov: 'User-agent: *' with no Disallow
  - Weekly PDFs are small (2 pp, ~6K chars). Granted transfers also appear as Supreme Court opinions in the decisions API (new S docket).
- **Currency:** index table 'Week Ending' — observed: "10/09/2026 21 0 21"
- **Official status:** Clerk publication; no official-status statement.
- **Hazard:** finding a disposition from the COA decision needs the week: scan lists after the COA decision date, or use the XLSX
- **Probe:** Nour v. State, No. 25A-CR-338 (trans. denied Feb. 10, 2026) → `https://www.in.gov/courts/clerk/files/transfer-2026-0213.pdf` — expect: "25A-CR-338 Kamal Nour v. State of Indiana Appellant Denied"
- **Evidence (2026-10-17):** fetch_doc: pdf 2 pages 6,104 chars; rows '25A-CR-338 Kamal Nour v. State of Indiana Appellant Denied All Justices concur. 2/10/26'. Index lists weekly PDF+XLSX links back to 2026-01-09 with 2024/2025 archive.

## Not available (do not look for these again)

- **case_law** — Opinions before mid-2005 on any official Indiana host: Decisions API: Supreme Court 2004 range returns 0 rows, earliest 2005 row 6/23/2005; legacy www.in.gov/judiciary/opinions/pdf/11250901.pdf returns HTTP 404. (2026-10-17)
- **case_law** — Free official reporter pagination: Opinion PDFs carry slip pagination only ('Page 1 of 29'); Indiana Reports/Ind. App. Reports ceased; N.E.3d is West's. (2026-10-17)
- **case_law** — Public-domain (vendor-neutral) citation format: Opinions are identified by docket number only (e.g. 26A-DC-221); App. R. 65 prescribes no neutral citation. (2026-10-17)
- **constitution** — Current Constitution text on www.in.gov: in.gov/history '/constitution-of-1851/' pages are titled 'Constitution of 1851 as originally written'. (2026-10-17)

## Corpus candidates (maintainers)

- `in-rules-pdf` — 216 pp / 462K chars; fetch tool stops near 100K chars
- `in-rules-pdf` — 116 pp / 206K chars
- `in-rules-pdf` — 50 pp / 77K chars (fits, but a corpus avoids per-rule fetches)
- `in-rules-pdf` — 36 pp / 67K chars; restyled 2024 numbering
- `in-rules-pdf` — 170 pp / 415K chars
- `in-rules-pdf` — 194 pp / 447K chars
- `in-code-iga` — Official IC download page (reported via search); JS-only, not reachable by either route — would give an official statute corpus if a static file URL is found · bulk: https://iga.in.gov/laws/ic/downloads (unverified)

## Open questions

- Find a static/API endpoint behind iga.in.gov (Code, Constitution, Acts) and iar.iga.in.gov (IAC, Register): every path, including /static/js bundles, returned the same HTML shell through the agent proxy; a browser session may reveal the real API host.
- Justia Indiana Constitution: confirm whether Art. 1 § 39 (2016) and other recent amendments are present.
- Justia court-of-appeals / tax-court case URL slugs not fetched; older (pre-2021) docket slug format unverified.
- Local court rules index https://www.in.gov/courts/publications/local-rules/ not probed.
