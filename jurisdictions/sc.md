# South Carolina (SC) — free legal sources

_Generated from `data/sc.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes, constitution, regulations and the State Register all come from scstatehouse.gov (unofficial, robots-permitted, script and fetch tool both work): the Code is one HTML page per chapter (t{TT}c{CCC}.php, no section anchors, long chapters truncate in the fetch tool) current through the 2025 Session; the Constitution is per-article PDFs; regulations are chapter PDFs (some 1.5M chars). The judiciary site www.sccourts.org disallows all robots, so official opinions and ALL court rules (SCRCP, SCRE, SCACR/RPC) are link-only with no tier-2 copy of the rules. Case text comes from Justia (constructible by Opinion No., incl. unpublished YYYY-UP-NNN; fetch tool only, script refused); subsequent history from the robots-free C-Track docket portal by a plain GET search.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of South Carolina | `sc (unverified)` | S.C. | S.C., S.E.2d, S.E., S.E.3d | — |
| South Carolina Court of Appeals | `scctapp (unverified)` | S.C. Ct. App. | S.C., S.E.2d, S.E.3d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| SC Appellate Court Rules (SCACR) incl. Rule 407 RPC | `Rule 407, SCACR`; `Rule 268(d)(2), SCACR`; `Rule 208(b)(1)(B), SCACR`; `Rule 8.4(e), RPC, Rule 407, SCACR`; `Rule 242 of the South Carolina Appellate Court Rules` | `sc-rules-sccourts` |
| SC Rules of Civil Procedure (SCRCP) | `Rule 12(b)(6), SCRCP`; `Rule 56(c), SCRCP`; `S.C. R. Civ. P. 12(b)(6)`; `Rule 12(b)(6) of the South Carolina Rules of Civil Procedure` | `sc-rules-sccourts` |
| SC Rules of Evidence (SCRE) | `Rule 702, SCRE`; `Rule 404(b), SCRE`; `S.C. R. Evid. 403`; `Rule 702 of the South Carolina Rules of Evidence` | `sc-rules-sccourts` |
| SC Rules of Criminal Procedure, Family Court, Magistrates Court, ADR | `Rule 5, SCRCrimP`; `Rule 7(b)(1), SCRCrimP`; `Rule 2, SCRFC`; `Rule 3, SCADR`; `Rule 4, SCRMC` | `sc-rules-sccourts` |
| SC Code of Regulations | `S.C. Code Ann. Regs. 61-62.5`; `S.C. Code Regs. 61-62`; `24A S.C. Code Ann. Regs. 61-62.1`; `S.C. Code Ann. Regs. 10-1`; `Regulation 61-62.5 of the South Carolina Code of Regulations` | `sc-regs-scstatehouse` |
| SC Code of Laws | `S.C. Code Ann. § 15-3-530`; `S.C. Code Ann. § 15-3-530(5) (Supp. 2025)`; `S.C. Code § 16-3-20`; `S.C. Code Ann. §§ 15-3-530 to -535`; `S.C. Code Ann. § 36-2A-103`; `S.C. Code Ann. § 12-6-510 (2014)`; `section 15-3-530 of the South Carolina Code`; `Section 1-23-380 of the South Carolina Code of Laws`; `Section 39-5-20 of the S.C. Code` | `sc-code-scstatehouse` → `sc-code-justia` |
| SC Code bare section (generic) *(only once this jurisdiction is known)* | `§ 15-3-530`; `Section 15-3-535`; `section 16-3-20(C)` | `sc-code-scstatehouse` → `sc-code-justia` |
| SC Acts (session laws) | `1988 S.C. Acts 494`; `2016 S.C. Acts No. 133`; `Act No. 133 of 2016 (S.C.)` | `sc-acts-scstatehouse` |
| SC Acts, Code-history form (generic) *(only once this jurisdiction is known)* | `1988 Act No. 494`; `2016 Act No. 133 (H.3145)` | `sc-acts-scstatehouse` |
| SC Constitution | `S.C. Const. art. I, § 10`; `S.C. Const. art. V, § 5`; `S.C. Const. art. VIII-A, § 1`; `Article I, Section 10 of the South Carolina Constitution` | `sc-constitution-scstatehouse` → `sc-constitution-justia` |
| SC State Register | `50 S.C. Reg. 123`; `S.C. State Register Vol. 50, Issue 9`; `South Carolina State Register, Volume 50, Issue No. 3` | `sc-register-scstatehouse` |
| Reported SC cases (S.C. Reports; S.E.2d with S.C. parenthetical) | `Huskins v. Mungo Homes, LLC, 439 S.C. 356, 887 S.E.2d 534 (Ct. App. 2023)`; `887 S.E.2d 534 (S.C. Ct. App. 2023)`; `Bodman v. State, 403 S.C. 60, 742 S.E.2d 363 (2013)`; `742 S.E.2d 363 (S.C. 2013)` | `sc-cases-justia` → `sc-opinions-sccourts` |
| SC opinion numbers, unpublished and memorandum opinions, advance sheets | `Op. No. 28245 (S.C. Sup. Ct. filed Dec. 11, 2024)`; `Op. No. 2024-UP-425 (S.C. Ct. App. filed Dec. 30, 2024)`; `2024-UP-425`; `Mem. Op. No. 2024-MO-012`; `(S.C. Sup. Ct. filed Dec. 11, 2024) (Howard Adv. Sh. No. 49 at 12)`; `(Shearouse Adv. Sh. No. 12 at 20)` | `sc-cases-justia` → `sc-ctrack-appellate-dockets` → `sc-opinions-sccourts` |
| SC Westlaw / Lexis cites | `2024 WL 4567890 (S.C. Ct. App. Jan. 3, 2024)`; `2023 S.C. App. LEXIS 12`; `2022 S.C. LEXIS 45` | `sc-cases-justia` |
| SC Appellate Case No. (generic) *(only once this jurisdiction is known)* | `Appellate Case No. 2023-000452`; `2018-000889` | `sc-ctrack-appellate-dockets` |
| Regional reporter without court (generic) *(only once this jurisdiction is known)* | `887 S.E.2d 534`; `742 S.E.2d 363, 365` | `sc-cases-justia` |
| Subsequent history phrases (generic) *(only once this jurisdiction is known)* | `cert. denied`; `cert. granted`; `cert. dismissed as improvidently granted`; `reh'g denied` | `sc-ctrack-appellate-dockets` |

Regexes (case-insensitive):

- SC Appellate Court Rules (SCACR) incl. Rule 407 RPC: `(?:Rule\s+(?P<rpc>\d+\.\d+)(?:\s*\([a-z0-9]+\))*,\s*RPC,\s*)?Rule\s+(?P<rule>\d+)(?:\s*\([a-z0-9]+\))*,?\s+SCACR|Rule\s+(?P<rule2>\d+)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+South\s+Carolina\s+Appellate\s+Court\s+Rules`
- SC Rules of Civil Procedure (SCRCP): `Rule\s+(?P<rule>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*,?\s+SCRCP|S\.\s*C\.\s*R\.\s*Civ\.\s*P\.\s*(?P<rule2>\d+(?:\.\d+)?)|Rule\s+(?P<rule3>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+South\s+Carolina\s+Rules\s+of\s+Civil\s+Procedure`
- SC Rules of Evidence (SCRE): `Rule\s+(?P<rule>\d{3,4})(?:\s*\([a-z0-9]+\))*,?\s+SCRE\b|S\.\s*C\.\s*R\.\s*Evid\.\s*(?P<rule2>\d{3,4})|Rule\s+(?P<rule3>\d{3,4})(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+South\s+Carolina\s+Rules\s+of\s+Evidence`
- SC Rules of Criminal Procedure, Family Court, Magistrates Court, ADR: `Rule\s+(?P<rule>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*,?\s+(?P<set>SCRCrimP|SCRFC|SCRMC|SCADR)\b`
- SC Code of Regulations: `S\.\s*C\.\s*Code(?:\s+Ann\.)?\s+Regs?\.\s*(?:§\s*)?(?P<chapter>\d{1,3})-(?P<reg>\d+(?:\.\d+)*[A-Z]?)|Regulation\s+(?P<chapter2>\d{1,3})-(?P<reg2>\d+(?:\.\d+)*)\s+of\s+the\s+South\s+Carolina\s+Code\s+of\s+(?:State\s+)?Regulations`
- SC Code of Laws: `S\.\s*C\.\s*Code(?:\s+(?:Ann\.|of\s+Laws))?\s*§§?\s*(?P<title>\d{1,2})-(?P<chapter>\d{1,3}[A-Z]?)-(?P<section>\d+(?:\.\d+)?)|(?:sec(?:tion|\.)|§)\s*(?P<title2>\d{1,2})-(?P<chapter2>\d{1,3}[A-Z]?)-(?P<section2>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:South\s+Carolina|S\.\s*C\.)\s+Code`
- SC Code bare section (generic): `(?:§|sec(?:tion|\.))\s*(?P<title>\d{1,2})-(?P<chapter>\d{1,3}[A-Z]?)-(?P<section>\d{1,5}(?:\.\d+)?)\b`
- SC Acts (session laws): `(?P<year>(?:19|20)\d\d)\s+S\.\s*C\.\s*Acts\s+(?:No\.\s*)?(?P<number>\d+)|Act\s+No\.\s*(?P<number2>\d+)\s+of\s+(?P<year2>(?:19|20)\d\d)\s+\(S\.\s*C\.\)`
- SC Acts, Code-history form (generic): `(?P<year>(?:19|20)\d\d)\s+Act\s+No\.\s*(?P<number>\d+)`
- SC Constitution: `S\.\s*C\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+(?:-A)?),?\s*§\s*(?P<section>\d+)|Article\s+(?P<article2>[IVXL]+(?:-A)?),?\s+Section\s+(?P<section2>\d+)\s+of\s+the\s+(?:South\s+Carolina|S\.\s*C\.)\s+Constitution`
- SC State Register: `(?P<volume>\d{1,2})\s+S\.\s*C\.\s*(?:State\s+)?Reg\.\s+(?P<page>\d+)|(?:S\.\s*C\.|South\s+Carolina)\s+State\s+Register,?\s+Vol(?:ume|\.)\s*(?P<volume2>\d+),?\s+Issue\s*(?:No\.\s*)?(?P<issue>\d+)`
- Reported SC cases (S.C. Reports; S.E.2d with S.C. parenthetical): `(?<![\w.])(?P<volume>\d{1,3})\s+S\.\s*C\.\s+(?P<page>\d{1,4})\b|(?P<sevol>\d{1,3})\s+S\.E\.(?:\s*(?P<series>[23])d)?\s+(?P<sepage>\d{1,4})(?:,\s*\d+)?\s*\((?P<court>S\.\s*C\.(?:\s*Ct\.\s*App\.)?)\s*(?P<year>\d{4})\)`
- SC opinion numbers, unpublished and memorandum opinions, advance sheets: `\b(?P<year>(?:19|20)\d\d)-(?P<kind>UP|MO)-(?P<number>\d{1,4})\b|Op\.\s*No\.\s*(?P<opno>\d{4,5})\s*\(S\.\s*C\.|(?P<sheet>Howard|Shearouse|Davis)\s+Adv\.\s*Sh\.\s*No\.\s*(?P<advsh>\d+)`
- SC Westlaw / Lexis cites: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(S\.\s*C\.|S\.\s*C\.(?:\s*App\.)?\s*LEXIS\s+(?P<lexis>\d+))`
- SC Appellate Case No. (generic): `(?:Appellate\s+Case\s+No\.\s*)?\b(?P<year>(?:19|20)\d\d)-(?P<number>\d{6})\b`
- Regional reporter without court (generic): `(?P<volume>\d{1,3})\s+S\.E\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,4})`
- Subsequent history phrases (generic): `\bcert\.\s*(?:denied|granted|dismissed)|\breh'?g\s+denied`

Short forms → URL key:

SCUTPA → `39-5`; South Carolina Unfair Trade Practices Act → `39-5`; Unfair Trade Practices Act → `39-5`; SCTCA → `15-78`; Tort Claims Act → `15-78`; South Carolina Tort Claims Act → `15-78`; SCAPA → `1-23`; Administrative Procedures Act → `1-23`; SCFOIA → `30-4`; Freedom of Information Act → `30-4`; Probate Code → `62`; South Carolina Probate Code → `62`; Children's Code → `63`; South Carolina Children's Code → `63`; Workers' Compensation Act → `42`; Uniform Commercial Code → `36`; Payment of Wages Act → `41-10`; Frivolous Civil Proceedings Sanctions Act → `15-36`

The statute URL needs no code key: title and chapter come straight from 'T-C-S' (pad title to 2, chapter to 3 digits). law_aliases map act names to their title or title-chapter so a named act can be routed to the chapter page. Bare '§ 15-3-530' / 'Section 15-3-530' is shared in form with other three-part codes (Tennessee, Georgia, Indiana, etc.) and is context_required. SC rule cites put the rule set AFTER the number ('Rule 12(b)(6), SCRCP'; RPC as 'Rule 8.4(e), RPC, Rule 407, SCACR'); bare 'Rule 12(b)(6)' or 'Rules of Civil Procedure' route here only with S.C. context. The '(?<![\w.])' guard keeps '42 U.S.C. 1983' from reading as an S.C. Reports cite. S.C. has no public-domain citation; the court's Opinion No. (5-digit Supreme Court, 4-digit published COA) and 'YYYY-UP-NNN' (unpublished COA) / 'YYYY-MO-NNN' (Supreme Court memorandum) numbers are the opinion keys and also the Justia URL key. Unpublished opinions have no precedential value (Rule 268(d)(2), SCACR). Advance-sheet cites ('Howard Adv. Sh.', earlier 'Shearouse'/'Davis') are pre-reporter cites. The Appellate Case No. 'YYYY-NNNNNN' is the docket key for C-Track. Cert dispositions (S.C. Supreme Court cert to the COA, and U.S. Supreme Court notices) are found on the C-Track docket; from a COA decision search the Supreme Court by party name. CourtListener ids from memory, unverified.

## A. Statutes / code

### `sc-acts-scstatehouse` — Ratifications and Acts (session laws)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · South Carolina Legislative Services Agency · text: **link-only** · official: unofficial
- **Coverage:** Current-session ratification sheets, ratifications/acts log and act lists; earlier sessions moved to the Archives.
- **Access:** `index-anchored` · format html
  - Index: `https://www.scstatehouse.gov/newlaws.php`
  - Navigation: newlaws.php -> '2025-2026 Ratifications/Acts Log' or 'Act Lists' -> bill page (act text). Earlier sessions: /archives.php.
- **Automation:** WebFetch untested · shell ok · robots: User-agent * - Disallow /images/, /jpeg/, /gif/, /dashboard/, /sys/ (AhrefsBot, Riddler: Disallow /); /code/, /coderegs/, /scconstitution/, /state_register.php allowed
  - Only the index page was read (script 200). Act text pages not probed.
- **Currency:** page heading — observed: "2025-2026 Legislative Session"
- **Official status:** General site disclaimer; acts are cited by the Code disclaimer as part of the official law but the web copies are not stated to be official.
- **Hazard:** needed because the online Code is only current through the 2025 Session
- **Probe:**  → `https://www.scstatehouse.gov/newlaws.php` — expect: "Ratification Sheets & Act Lists"
- **Evidence (2026-10-17):** Script: newlaws.php 200, 'Ratification Sheets & Act Lists', '2025-2026 Legislative Session'. No act text fetched.

### `sc-code-scstatehouse` — South Carolina Code of Laws, unannotated (scstatehouse.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Carolina Legislative Council / Legislative Services Agency · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All 63 titles, one HTML page per chapter (text, numbering, history, editor's notes); per-chapter Word downloads. Historical snapshots under /Archives/CodeofLaws{YYYY}/ (seen in search results for 2000-2013, not fetched).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.scstatehouse.gov/code/t{title}c{chapter}.php`
  - Placeholders: Citation S.C. Code Ann. § {T}-{C}-{S}: title = T zero-padded to 2 digits; chapter = C zero-padded to 3 digits with any letter suffix kept upper-case (15-3-530 -> t15c003.php; 1-23-380 -> t01c023.php; 36-2A-103 -> t36c002A.php). The page holds the WHOLE chapter; there are no section anchors (no id/name attributes), so locate the section by the literal text 'SECTION {T}-{C}-{S}.' (script: fetch_doc.py grep/section). Chapters ending 'R' (t40c021R.php) are RESERVED stubs. Word file of a chapter: /getfile.php?TYPE=CODEOFLAWS&TITLE={T}&CHAPTER={C} (unpadded). Title index /code/title{T}.php (unpadded) lists chapter names only, no section ranges; not needed because the chapter is in the citation.
  - Index: `https://www.scstatehouse.gov/code/statmast.php`
  - Navigation: statmast.php -> title{T}.php -> t{TT}c{CCC}.php (HTML) or getfile.php (Word)
- **Automation:** WebFetch ok (truncated) · shell ok · robots: User-agent * - Disallow /images/, /jpeg/, /gif/, /dashboard/, /sys/ (AhrefsBot, Riddler: Disallow /); /code/, /coderegs/, /scconstitution/, /state_register.php allowed
  - WebFetch read built URLs on this host without an approval prompt. Long chapters exceed the WebFetch window: t16c003.php is 124,663 chars of text and WebFetch stopped inside § 16-3-740 (continue with offset 100000). Script sizes (raw text incl. whitespace): t15c003 45,604; t01c023 140,304; t16c003 333,507; t63c007 314,879; t12c006 508,386 chars. Prefer fetch_doc.py grep/section on long chapters. Full-text search (query.php) needs a JavaScript auto-submit; a hand-built GET returned 'found 0 times'/'Submitting...' - not usable.
- **Currency:** https://www.scstatehouse.gov/code/statmast.php DISCLAIMER paragraph (not on chapter pages) — observed: "now current through the 2025 Session of the General Assembly"
- **Official status:** https://www.scstatehouse.gov/code/statmast.php DISCLAIMER: this version 'is not official'; only the published volumes of the S.C. Code of Laws Annotated and the acts are official.
- **Hazard:** one page per chapter, no section anchors: search the text for 'SECTION T-C-S.'
- **Hazard:** long chapters truncate in WebFetch at 100K chars (use offset or the script)
- **Hazard:** currency is the 2025 Session as of 2026-10-17: 2026 acts may not be in the text yet; check Ratifications & Acts
- **Hazard:** no currency line on chapter pages
- **Hazard:** Word/HTML only; no PDF of the Code
- **Probe:** S.C. Code Ann. § 15-3-530 → `https://www.scstatehouse.gov/code/t15c003.php` — expect: "SECTION 15-3-530. Three years. Within three years:"
- **Evidence (2026-10-17):** Script: t15c003.php 45,604 chars; grep 'SECTION 15-3-530. Three years. Within three years: (1) an action upon a contract'. Second title: t16c003.php 'SECTION 16-3-20. Punishment for murder'; t01c023.php 'SECTION 1-23-380. Judicial review upon exhaustion'; t12c006.php 'SECTION 12-6-510. Tax rates'; t36c002A.php 'SECTION 36-2A-103.'. WebFetch t15c003: YES 'Within three years: (1) an action upon a contract', ends § 15-3-700, not truncated; WebFetch t16c003: truncated at 100,000 of 124,663 chars.
- **Notes:** 1,371 chapter links enumerated from title1-63.php: all fit t{2 digits}c{3 digits}[A|R].php; only 36-2A, 36-4A carry a letter (plus reserved 40-21R, 40-73R).

### `sc-code-justia` — South Carolina Code of Laws (Justia, 2025 edition)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-section pages of the S.C. Code; edition '2025 South Carolina Code of Laws'.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/south-carolina/title-{title}/chapter-{chapter}/section-{title}-{chapter}-{section}/`
  - Placeholders: No zero-padding (title-15/chapter-3/section-15-3-530). Letter-suffix chapters (36-2A) untested: likely lower-case 'chapter-2a', verify before use.
  - Index: `https://law.justia.com/codes/south-carolina/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com/robots.txt answered with a Cloudflare challenge; fetch_doc.py REFUSED the host for the day (robots.txt challenge, 2026-10-17T09:44)
  - WebFetch read built Justia URLs. Per-section pages, so no truncation.
- **Currency:** page heading — observed: "2025 South Carolina Code of Laws"
- **Official status:** Page states 'These codes may not be the most recent version' and refers users to official sources.
- **Hazard:** one edition behind the print code possible; disclose currency
- **Hazard:** script route refused (challenge)
- **Probe:** S.C. Code Ann. § 15-3-530 → `https://law.justia.com/codes/south-carolina/title-15/chapter-3/section-15-3-530/` — expect: "Within three years: (1) an action upon a contract, obligation,"
- **Evidence (2026-10-17):** WebFetch: YES 'Within three years: (1) an action upon a contract, obligation,'; '2025 South Carolina Code of Laws'. Second: title-16/chapter-3/section-16-3-20/ YES 'A person who is convicted of or pleads guilty to'. Script: REFUSED (law.justia.com challenge).

## B. Constitution

### `sc-constitution-scstatehouse` — South Carolina Constitution, unannotated (per-article PDFs)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Carolina Legislative Council / Legislative Services Agency · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Preamble, Articles I-XVII (incl. VIII-A), amendments list; whole text SCConstitution.pdf (99 pp).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.scstatehouse.gov/scconstitution/A{article}.pdf`
  - Placeholders: article = Arabic number of the Roman article, zero-padded to 2 digits (art. I -> A01.pdf, art. V -> A05.pdf); Article VIII-A -> A08A.pdf. Locate the section by 'SECTION {n}.' inside the PDF. Whole document: /scconstitution/SCConstitution.pdf.
  - Index: `https://www.scstatehouse.gov/scconstitution/scconst.php`
- **Automation:** WebFetch ok · shell ok · robots: User-agent * - Disallow /images/, /jpeg/, /gif/, /dashboard/, /sys/ (AhrefsBot, Riddler: Disallow /); /code/, /coderegs/, /scconstitution/, /state_register.php allowed
  - Article PDFs are small (A01 7 pp, 20,313 chars). SCConstitution.pdf is 99 pp / 244,257 chars - too long for WebFetch.
- **Currency:** scconst.php page body — observed: "updated through the 2025 Session of the General Assembly is now available"
- **Official status:** https://www.scstatehouse.gov/scconstitution/scconst.php DISCLAIMER: the unannotated Constitution online 'is not official'.
- **Hazard:** no currency line inside the PDFs (Last-Modified 14 Oct 2025)
- **Hazard:** whole-text PDF exceeds the WebFetch window
- **Probe:** S.C. Const. art. I, § 10 → `https://www.scstatehouse.gov/scconstitution/A01.pdf` — expect: "The right of the people to be secure in their persons"
- **Evidence (2026-10-17):** Script: A01.pdf 7 pp, grep 'SECTION 10. Searches and seizures; invasions of privacy.'; A05.pdf 'SECTION 5. Jurisdiction of Supreme Court.' WebFetch A01.pdf: YES 'The right of the people to be secure in their', last § 25, not truncated.

### `sc-constitution-justia` — South Carolina Constitution (Justia)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-article pages (introduction, preamble, a01 ...). Out of date: Article I page ends at § 24 (the official text has § 25).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/south-carolina/a{article}.html`
  - Placeholders: article = 2-digit Arabic number (a01.html). Article VIII-A untested.
  - Index: `https://law.justia.com/constitution/south-carolina/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com/robots.txt answered with a Cloudflare challenge; fetch_doc.py REFUSED the host for the day (robots.txt challenge, 2026-10-17T09:44)
- **Currency:** none stated — observed: "This Constitution may not be the most recent version."
- **Official status:** Page states 'This Constitution may not be the most recent version.'
- **Hazard:** stale: lacks Art. I § 25 (hunting and fishing) present on scstatehouse.gov
- **Hazard:** no edition date
- **Probe:** S.C. Const. art. I, § 10 → `https://law.justia.com/constitution/south-carolina/a01.html` — expect: "The right of the people to be secure in their"
- **Evidence (2026-10-17):** WebFetch a01.html: YES 'The right of the people to be secure in their'; last section 24. Index lists introduction.html, preamble.html, a01.html.
- **Notes:** Use only when scstatehouse.gov fails, and check the section exists in the current text.

## C. Court rules

### `sc-rules-sccourts` — South Carolina Court Rules (SCACR incl. Rule 407 RPC, SCRCP, SCRE, SCRCrimP, SCRFC, SCRMC, SCADR)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · South Carolina Judicial Branch · text: **link-only** · official: unknown
- **Coverage:** All court rules issued by the Supreme Court of South Carolina (per-rule pages on the court site).
- **Access:** `link-only` · format html
  - Index: `https://www.sccourts.org/court-rules/`
  - Navigation: Not navigated (robots). Link the court-rules page in reports; do not fetch.
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.sccourts.org: 'User-agent: *' 'Disallow: /' 'Crawl-delay: 120000' (named Google/Bing bots get path rules only)
  - fetch_doc.py check: REFUSED 'robots.txt on www.sccourts.org disallows /court-rules/ (rule: Disallow: /)'. WebFetch not used (policy). The lead host 'sccourts.gov' does not serve the court: WebFetch ROBOTS_DISALLOWED on https://www.sccourts.gov/ and /robots.txt; proxy CONNECT 502; http DNS does not resolve.
- **Currency:** n/a
- **Official status:** Not readable: host refuses all crawlers in robots.txt.
- **Hazard:** robots Disallow: / for every agent
- **Hazard:** no tier-2 copy of S.C. court rules on Justia, LII or public.law
- **Probe:** Rule 12(b)(6), SCRCP → `https://www.sccourts.org/court-rules/`
- **Evidence (2026-10-17):** robots.txt 'User-agent: *' 'Disallow: /'; fetch_doc.py REFUSED for /court-rules/ and /opinions/.
- **Notes:** index_url path is a guess from the site structure and was never fetched; treat as the court site's home www.sccourts.org when linking.

## D. Administrative code

### `sc-regs-scstatehouse` — South Carolina Code of State Regulations, unannotated (chapter PDFs)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Carolina Legislative Council / Legislative Services Agency · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All agency chapters as PDF (and Word); Chapter 61 (Dept. of Environmental Services / DHEC) split into per-regulation PDFs.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.scstatehouse.gov/coderegs/Chapter%20{chapter}.pdf`
  - Placeholders: Regulation {C}-{N}: chapter PDF is 'Chapter {C}.pdf' (space encoded %20; the script rejects a raw space). Chapter 61 is NOT one file: use the Chapter61.php page, which links 'Chapter 61-1 through 61-17.pdf', 'Chapter 61-18 through 61-58.17.pdf', 'Chapter 61-62.pdf', 'Chapter 61-63.pdf' ... (ranges shown in the link text). Word: /getfile.php?TYPE=CODEOFREGS&CHAPTER={C}. Inside PDFs numbers use EN DASHES ('10–1.', '61–62.1') and also hyphens in cross-references; grep both.
  - Index: `https://www.scstatehouse.gov/coderegs/statmast.php`
  - Navigation: statmast.php -> chapter 'PDF' link (or, for chapter 61, Chapter61.php -> per-regulation PDF) -> search the PDF for the regulation number
- **Automation:** WebFetch ok (truncated) · shell ok · robots: User-agent * - Disallow /images/, /jpeg/, /gif/, /dashboard/, /sys/ (AhrefsBot, Riddler: Disallow /); /code/, /coderegs/, /scconstitution/, /state_register.php allowed
  - Chapter 61-62.pdf (air pollution control) is 397 pp / 1,570,629 chars; WebFetch stopped inside Reg. 61-62.1 § II.L. Chapter 10.pdf 23 pp / 82,785 chars.
- **Currency:** coderegs/statmast.php, top of page and DISCLAIMER — observed: "Files are current through State Register Volume 50, Issue 3, effective March 27, 2026."
- **Official status:** https://www.scstatehouse.gov/coderegs/statmast.php DISCLAIMER: the online Code of Regulations 'is not official'; the print volumes are.
- **Hazard:** en-dash numbering in PDFs
- **Hazard:** very large chapter PDFs truncate in WebFetch
- **Hazard:** space in file names
- **Hazard:** HTML version not offered; tables best in PDF per the site
- **Probe:** S.C. Code Ann. Regs. 61-62.1 → `https://www.scstatehouse.gov/coderegs/Chapter%2061-62.pdf` — expect: "Department approved malfunction plan"
- **Evidence (2026-10-17):** Script: Chapter%2061-62.pdf 397 pp, 1,570,629 chars, Last-Modified 23 Feb 2026; grep '61-62.1' found at p. 60. Chapter%2010.pdf 23 pp, starts 'CHAPTER 10 Department of Labor, Licensing and Regulation'. WebFetch 61-62.pdf: 61-62.5 NOT PRESENT; truncated in 61-62.1.

## D. Administrative register

### `sc-register-scstatehouse` — South Carolina State Register (monthly issue PDFs)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Carolina Legislative Council · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Volume 29 (2005) to current; annual index PDFs.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.scstatehouse.gov/state_register.php?first=FILE&pdf=1&file=Sr{volume}-{issue}.pdf`
  - Placeholders: volume = calendar year - 1976 (2026 -> 50); issue = month number 1-12 (Sept. 25, 2026 -> Sr50-9.pdf). Annual index: file=index{YYYY}.pdf. The listing page groups issues by fiscal year (July-June), but the file names follow the calendar volume.
  - Index: `https://www.scstatehouse.gov/state_register.php`
- **Automation:** WebFetch untested · shell ok · robots: User-agent * - Disallow /images/, /jpeg/, /gif/, /dashboard/, /sys/ (AhrefsBot, Riddler: Disallow /); /code/, /coderegs/, /scconstitution/, /state_register.php allowed
  - Issue PDFs 20-60 pp (Sr50-9 153,818 chars).
- **Currency:** state_register.php list; issue cover page — observed: "Published September 25, 2026 Volume 50 Issue No. 9"
- **Official status:** Each issue's first page: 'the printed version of the State Register, not the online version, is the official version.'
- **Hazard:** issues >100K chars truncate in WebFetch
- **Hazard:** page numbers continue through the volume
- **Probe:** 50 S.C. Reg. (Sept. 25, 2026) → `https://www.scstatehouse.gov/state_register.php?first=FILE&pdf=1&file=Sr50-9.pdf` — expect: "Published September 25, 2026 Volume 50 Issue No. 9"
- **Evidence (2026-10-17):** Script: Sr50-9.pdf 53 pp, 153,818 chars; 'SOUTH CAROLINA STATE REGISTER DISCLAIMER'; 'Published September 25, 2026 Volume 50 Issue No. 9'. Sr50-3.pdf 22 pp.

## E. Case law

### `sc-advance-sheets-statelibrary` — Advance Sheets: Opinions of the Supreme Court and Court of Appeals (State Library depository)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · South Carolina State Library (State Documents Depository, Judicial Department) · text: **link-only** · official: unknown
- **Coverage:** Advance sheets deposited by the Judicial Department (range not checked).
- **Access:** `link-only` · format pdf
  - Pattern: `https://dc.statelibrary.sc.gov/entities/publication/{uuid}`
  - Placeholders: uuid only from search results; Discovery search (/search) and /browse are robots-disallowed.
  - Index: `https://dc.statelibrary.sc.gov/`
  - Navigation: Found only through web search results; item page -> bitstream (not followed).
- **Automation:** WebFetch untested · shell ok · robots: User-agent * - Disallow /search, /browse, /entities/*?f, /entities/*/full, /items/*/full, login/admin paths; Crawl-delay 10
  - Script read one item page (Angular DSpace; 1,751 chars, title 'advance sheet no. 26'). PDFs not fetched: whether a depository copy of a robots-blocked court publication is an acceptable source is an open question.
- **Currency:** n/a
- **Official status:** Depository copies of the courts' advance sheets; no statement seen.
- **Hazard:** policy question: possible alternate host for robots-blocked court documents
- **Hazard:** no search route (robots)
- **Probe:**  → `https://dc.statelibrary.sc.gov/entities/publication/518f38c4-71bd-403f-920d-600dc17e2ae5` — expect: "advance sheet no. 26"
- **Evidence (2026-10-17):** Script: item page 200, 'Opinions of the Supreme Court and Court of Appeals of South Carolina advance sheet no. 26'. Not read further.
- **Notes:** Do not quote from it until the alternate-host question is settled.

### `sc-opinions-sccourts` — Supreme Court and Court of Appeals opinions (www.sccourts.org)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · South Carolina Judicial Branch · text: **link-only** · official: unofficial
- **Coverage:** Published and unpublished opinions, advance sheets, orders (not inspected).
- **Access:** `link-only` · format pdf
  - Index: `https://www.sccourts.org/opinions/`
  - Navigation: Not navigated (robots).
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.sccourts.org: 'User-agent: *' 'Disallow: /' 'Crawl-delay: 120000' (named Google/Bing bots get path rules only)
  - fetch_doc.py check REFUSED '/opinions/ (rule: Disallow: /)'. WebFetch not used. www.sccourts.gov (the lead's host) is not the court site: WebFetch ROBOTS_DISALLOWED, proxy 502.
- **Currency:** n/a
- **Official status:** Slip opinions and advance sheets; official reports are the South Carolina Reports (print).
- **Hazard:** robots Disallow: / for every agent
- **Probe:** Op. No. 28245 → `https://www.sccourts.org/opinions/`
- **Evidence (2026-10-17):** robots.txt 'User-agent: *' 'Disallow: /'; fetch_doc.py REFUSED.
- **Notes:** Read opinion text from sc-cases-justia; link the court site.

### `sc-cases-justia` — South Carolina Supreme Court and Court of Appeals opinions (Justia)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1883-2026 (some years skipped); Court of Appeals incl. unpublished (YYYY-UP-NNN) opinions. Latest Supreme Court item seen: Aug. 12, 2026 (about two months behind on 2026-10-17).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/south-carolina/{court}/{year}/{opinion}.html`
  - Placeholders: court = supreme-court | court-of-appeals; year = filing year; opinion = the court's Opinion No. (Supreme Court 28245; published COA 6093) or lower-case unpublished number (2024-up-425). Not the Appellate Case No. (2023-000452). Year listing: /cases/south-carolina/{court}/{year}/ gives name, number, date. PDF: cases.justia.com/south-carolina/{court}/{year}-{opinion}.pdf?ts=... (from the page's Download PDF link).
  - Index: `https://law.justia.com/cases/south-carolina/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com/robots.txt answered with a Cloudflare challenge; fetch_doc.py REFUSED the host for the day (robots.txt challenge, 2026-10-17T09:44)
  - WebFetch read listing and case pages built from the pattern. Script route refused for the day.
- **Currency:** year listing — observed: "latest Supreme Court entry Aug. 12, 2026 (No. 28348)"
- **Official status:** Third-party copy of slip opinions; no official reporter pagination.
- **Hazard:** slip pagination only; S.C./S.E.2d pages not shown
- **Hazard:** lags the court by weeks
- **Hazard:** Supreme Court memorandum opinions (YYYY-MO-NNN) coverage untested
- **Probe:** Huskins v. Mungo Homes, LLC, Op. No. 28245 (S.C. Dec. 11, 2024) → `https://law.justia.com/cases/south-carolina/supreme-court/2024/28245.html` — expect: "When Petitioners Amanda Leigh Huskins and Jay R. Huskins decided to buy"
- **Evidence (2026-10-17):** WebFetch 2024/28245.html: YES full text 'When Petitioners Amanda Leigh Huskins and Jay R. Huskins decided to buy', ends 'REVERSED AND REMANDED'; Opinion No. 28245, Appellate Case No. 2023-000452. COA 2024 listing: 2024-UP-425 (Dec. 30, 2024) -> 2024-up-425.html; published No. 6093. Supreme Court index: years 1883-2026.

## F. Subsequent history

### `sc-ctrack-appellate-dockets` — South Carolina Appellate Case Management System (C-Track public portal)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · South Carolina Judicial Branch (Clerks of the Supreme Court and Court of Appeals) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court and Court of Appeals dockets, cases filed from about 2012 (csIID 1043 = 2012-206608): classification (e.g. 'Certiorari - COA'), lower court and its number, disposition date/type, remittitur, event list incl. rehearing and U.S. Supreme Court cert notices.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://ctrack.sccourts.org/public/caseSearch.do?courtID={court}&csNumber={appellate_case_no}&shortTitle={title}&submitValue=Search&action=Search&startRow=1&displayRows=50&orderBy=FileDt&orderDir=DESC&href=/public/caseView.do`
  - Placeholders: court = 10001 (Supreme Court) | 10002 (Court of Appeals); csNumber = Appellate Case No. 'YYYY-NNNNNN'; or shortTitle = a party name. Omit 'exclude=on' (that excludes closed cases and returned 'No records were found.'). A single hit redirects straight to caseView.do?csIID={id}. From the decision below to cert: search courtID=10001 by party name (shortTitle) and match 'Lower Court or Tribunal' (same trial-court number on both records) - there is no search by lower-court number.
  - Index: `https://ctrack.sccourts.org/public/caseSearch.do`
- **Automation:** WebFetch gated · shell ok · robots: none (404)
  - Form is method=post but GET works. WebFetch on a built caseView URL: PROVENANCE_REQUIRED (approval not answered) - not a site refusal. Linked from the court site as sccourts.org/ACMS (seen in search results; the court site itself is robots-blocked so the link was not fetched).
- **Currency:** live docket — observed: "events through 10/14/2025 on 2023-000452"
- **Official status:** Page banner: information 'should not be relied upon as an official record of action.'
- **Hazard:** cert-to-COA linkage by party name only
- **Hazard:** documents column: links not exposed to the script
- **Hazard:** pre-2012 cases absent
- **Probe:** Appellate Case No. 2023-000452 (Huskins v. Mungo Homes) → `https://ctrack.sccourts.org/public/caseSearch.do?courtID=10001&csNumber=2023-000452&submitValue=Search&action=Search&startRow=1&displayRows=50&orderBy=FileDt&orderDir=DESC&href=/public/caseView.do` — expect: "Supreme Court of the United States - Notice that Certiorari Denied"
- **Evidence (2026-10-17):** Script GET -> caseView.do?csIID=78122: 'Case Information: 2023-000452', 'Certiorari - COA', disposition 12/11/2024 Opinion; events '01/16/2025 Rehearing - Denied', '10/14/2025 Supreme Court of the United States - Notice that Certiorari Denied'. COA search shortTitle=Huskins -> 2018-000889, same lower court 2017CP4003697.
- **Notes:** Script candidate: deterministic subsequent-history lookup.

## Not available (do not look for these again)

- **court_rules** — Tier-2 (Justia, Cornell LII, public.law) text of S.C. court rules (SCRCP, SCRE, SCACR): Web search for SCRCP Rule 12 text returned only non-vetted third parties (courtrules.net, rulesofcivilprocedure.com, vlex); Justia/LII do not list S.C. rules; public.law has no S.C. edition (DE/NC records). (2026-10-17)
- **statutes** — Official bulk download / API of the S.C. Code: None on code/statmast.php; per-chapter Word files via getfile.php are the closest substitute. (2026-10-17)
- **case_law** — Public-domain / vendor-neutral citation format: S.C. uses Opinion Nos. and S.C./S.E.2d only; none seen on Justia pages or C-Track. (2026-10-17)
- **case_law** — Court site at sccourts.gov (the host named in the leads): WebFetch ROBOTS_DISALLOWED on https://www.sccourts.gov/ and /robots.txt; proxy CONNECT 502; plain http DNS failure. The court's site is www.sccourts.org. (2026-10-17)

## Corpus candidates (maintainers)

- `sc-regs-scstatehouse` — 397 pp / 1.57M chars; WebFetch stops inside Reg. 61-62.1 (61-62.5 NOT PRESENT).
- `sc-code-scstatehouse` — Chapter pages up to 508K chars (t12c006); WebFetch stops at 100K (t16c003 inside § 16-3-740). Script reads in full, so ingest is optional. · bulk: https://www.scstatehouse.gov/getfile.php?TYPE=CODEOFLAWS&TITLE={T}&CHAPTER={C}
- `sc-constitution-scstatehouse` — Whole text 99 pp / 244K chars exceeds WebFetch; per-article PDFs are the read route.

## Open questions

- Is the State Library depository copy of the courts' advance sheets (dc.statelibrary.sc.gov) an acceptable source while www.sccourts.org disallows all robots, or is it an alternate host that the policy excludes? Not fetched beyond one item page.
- S.C. court rules have no reachable official or tier-2 text: needs a policy decision (e.g. ask the court, or a manual capture route).
- C-Track is linked from the court site as sccourts.org/ACMS only per search results; the link could not be read on the robots-blocked court site.
- Justia letter-suffix chapters (36-2A) and Article VIII-A URL forms untested; Justia coverage of Supreme Court memorandum opinions (YYYY-MO-NNN) untested.
- The online Code is 'current through the 2025 Session' on 2026-10-17; recheck for the 2026 update.
- Act text pages (session laws) not probed; sc-acts-scstatehouse is reported only.
