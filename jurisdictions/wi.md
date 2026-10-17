# Wisconsin (WI) — free legal sources

_Generated from `data/wi.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes, constitution, session laws, Administrative Code and Register all sit on docs.legis.wisconsin.gov (Legislative Reference Bureau), and each is constructible from a citation through the /document/... redirector (e.g. /document/statutes/802.06(2)(a)6., /document/administrativecode/DHS%20110.04, /document/wisconsinconstitution/I,9); the statutes are certified under s. 35.18. Civil procedure, evidence and appellate procedure are statutes (chs. 801-847, 901-911, 809); Supreme Court Rules (SCR, incl. ch. 20 professional conduct) are per-chapter PDFs on wicourts.gov. Case law: wicourts.gov serves Supreme Court and Court of Appeals slip opinions (published and unpublished) from 1995 as PDFs, found by plain GET searches that accept a public-domain citation (pdcNo=2024 WI 13), docket number, party name or date range. Petition-for-review dispositions are findable by docket number (scorder.jsp order PDFs and the bimonthly disposition tables); WebFetch is gated on built wicourts URLs, so use fetch_doc.py.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Wisconsin Supreme Court | `wis (unverified)` | Wis. | Wis. 2d, N.W.2d, N.W.3d, Wis. | 2024 WI 13, ¶ 22 |
| Wisconsin Court of Appeals | `wisctapp (unverified)` | Wis. Ct. App. | Wis. 2d, N.W.2d, N.W.3d | 2020 WI App 34, ¶ 12 |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Wisconsin Statutes | `Wis. Stat. § 893.54`; `Wis. Stat. § 802.06(2)(a)6.`; `Wis. Stats. § 940.01(1)(a)`; `Wis. Stat. § (Rule) 809.62`; `WIS. STAT. § 908.03(6)`; `s. 893.54, Stats.`; `section 802.06 of the Wisconsin Statutes`; `Wis. Stat. §§ 893.52-893.55`; `Wis. Stat. ch. 893`; `Wis. Stats. ch. 802` | `wi-statutes-legis` → `wi-statutes-pdf` → `wi-statutes-justia` |
| Prose 'section 893.54 of the statutes' (generic, no state marker) *(only once this jurisdiction is known)* | `section 893.54 of the statutes`; `sec. 802.06(2) of the statutes` | `wi-statutes-legis` → `wi-statutes-justia` |
| Wisconsin appellate procedure cited as a rule (ch. 809) | `Wis. Stat. Rule 809.23(3)(b)`; `WIS. STAT. RULE 809.62`; `Rule 809.19(1)(e), Stats.` | `wi-statutes-legis` → `wi-statutes-justia` |
| Bare 'Rule 809.62' (Wisconsin appellate rule without a state marker) *(only once this jurisdiction is known)* | `Rule 809.62`; `RULE 809.23(3)` | `wi-statutes-legis` |
| Wisconsin session laws (Acts) | `2025 Wis. Act 247`; `2011 Wisconsin Act 10`; `1995 Wis. Act 27, § 9126` | `wi-acts-legis` |
| Wisconsin Constitution | `Wis. Const. art. I, § 9`; `Wis. Const. art. VII, § 3(1)`; `Article I, Section 9 of the Wisconsin Constitution`; `art. I, sec. 9, Wis. Const.` | `wi-constitution-legis` → `wi-constitution-justia` |
| Wisconsin Supreme Court Rules (SCR) | `SCR 20:1.7`; `Wis. Sup. Ct. R. 20:1.7`; `Supreme Court Rule 20:8.4(c)`; `Wis. Sup. Ct. R. 22.03(2)`; `Wis. Sup. Ct. R. 60.04(1)(g)`; `SCR 20:8.4(c)` | `wi-scr-wicourts` |
| Wisconsin Supreme Court Rules (bare "SCR NN.NN", shared with Nevada) *(only once this jurisdiction is known)* | `SCR 22.03`; `SCR 60.04`; `SCR 22.03(2)`; `SCR 60.04(1)(g)` | `wi-scr-wicourts` |
| Wisconsin Administrative Code | `Wis. Admin. Code § DHS 110.04`; `Wis. Admin. Code DHS § 110.04(1g)`; `Wis. Admin. Code § NR 115.05(1)(b)`; `s. DHS 110.04, Wis. Adm. Code`; `Wis. Admin. Code ch. ATCP 134` | `wi-admincode-legis` → `wi-admincode-lii` |
| Wisconsin Administrative Register | `Register, September 2021, No. 789`; `Register December 2010 No. 660`; `EmR2609` | `wi-register-legis` |
| Wisconsin Supreme Court public-domain citation | `2024 WI 13`; `2024 WI 13, ¶ 22`; `2019 WI 12, ¶¶ 20-24` | `wi-opinions-supreme` → `wi-cases-justia` |
| Wisconsin Court of Appeals public-domain citation | `2020 WI App 34`; `2020 WI App 34, ¶ 12` | `wi-opinions-appeals` → `wi-cases-justia` |
| Wisconsin Reports (Wis. / Wis. 2d) | `406 Wis. 2d 586`; `385 Wis. 2d 1, 922 N.W.2d 1`; `177 Wis. 2d 1` | `wi-opinions-supreme` → `wi-opinions-appeals` → `wi-cases-justia` |
| North Western Reporter with a Wisconsin parenthetical | `987 N.W.2d 778 (Wis. Ct. App. 2023)`; `922 N.W.2d 1 (Wis. 2019)` | `wi-opinions-supreme` → `wi-opinions-appeals` → `wi-cases-justia` |
| Wisconsin appeal number / unpublished opinion form (Wis. Stat. § 809.23(3)(c)) | `No. 2025AP1919, unpublished slip op. ¶ 12 (WI App Oct. 15, 2026)`; `2018AP2220-CR`; `2023AP000301` | `wi-opinions-appeals` → `wi-opinions-supreme` → `wi-cases-justia` |
| Generic 'review denied' / 'review granted' history *(only once this jurisdiction is known)* | `review denied, 2026 WI 33`; `review granted`; `petition for review denied` | `wi-pfr-orders` → `wi-pfr-disposition-tables` |

Regexes (case-insensitive):

- Wisconsin Statutes: `(?:Wis(?:consin)?\.?\s*Stats?\.?(?:\s*Ann\.)?\s*(?:§+|ss?\.)\s*(?:\(Rule\)\s*)?(?P<section>\d{1,3}\.\d{2,4}[a-z]?)(?!\d)(?P<sub>(?:\s*\([0-9a-z]+\))*(?:\s*\d+\.)?(?:\s*[a-z]\.)?)|(?:s|ss|sec(?:tion)?)\.?\s+(?P<section2>\d{1,3}\.\d{2,4}[a-z]?)(?!\d)(?:\s*\([0-9a-z]+\))*(?:\s*\d+\.)?,?\s+(?:Wis\.\s*)?Stats\.|section\s+(?P<section3>\d{1,3}\.\d{2,4}[a-z]?)(?!\d)(?:\s*\([0-9a-z]+\))*\s+of\s+the\s+Wisconsin\s+Statutes|Wis(?:consin)?\.?\s*Stats?\.?\s*chs?\.\s*(?P<chapter>\d{1,3})(?![\d.]))`
- Prose 'section 893.54 of the statutes' (generic, no state marker): `sec(?:tion|\.)\s+(?P<section>\d{1,3}\.\d{2,4}[a-z]?)(?!\d)(?:\s*\([0-9a-z]+\))*\s+of\s+the\s+statutes`
- Wisconsin appellate procedure cited as a rule (ch. 809): `(?:Wis\.?\s*Stats?\.?\s*Rule\s*(?P<rule>8\d\d\.\d{2,3})|Rule\s+(?P<rule2>8\d\d\.\d{2,3})(?:\s*\([0-9a-z]+\))*,\s*Stats\.)`
- Bare 'Rule 809.62' (Wisconsin appellate rule without a state marker): `\bRule\s+(?P<rule>809\.\d{2,3})`
- Wisconsin session laws (Acts): `(?P<year>(?:19|20)\d\d)\s+Wis(?:consin|\.)\s+Act\s+(?P<act>\d{1,4})`
- Wisconsin Constitution: `(?:Wis\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*(?:§|sec\.)\s*(?P<section>\d+[a-z]?)|Article\s+(?P<article2>[IVXL]+),?\s+Section\s+(?P<section2>\d+[a-z]?)\s+of\s+the\s+Wisconsin\s+Constitution|art\.\s*(?P<article3>[IVXL]+),\s*(?:sec\.|§)\s*(?P<section3>\d+[a-z]?)(?:\s*\([0-9a-z]+\))*,\s*Wis\.\s*Const\.)`
- Wisconsin Supreme Court Rules (SCR): `(?:(?:Wis\.\s*)?S\.?C\.?R\.?|Wis\.\s*Sup\.\s*Ct\.\s*R\.|Supreme\s+Court\s+Rule)\s*(?P<chapter>\d{2}):(?P<rule>\d\.\d{1,2})|(?:Wis\.\s*SCR|Wis\.\s*Sup\.\s*Ct\.\s*R\.)\s*(?P<chapter2>\d{2})\.(?P<rule2>\d{2,3})`
- Wisconsin Supreme Court Rules (bare "SCR NN.NN", shared with Nevada): `\bSCR\s+(?P<chapter3>(?:1[0-4]|2[0-3]|3[0-6]|40|50|6[0-3]|7[0-2]|8[01]))\.(?P<rule3>\d{2,3})`
- Wisconsin Administrative Code: `(?:Wis\.?\s*Adm(?:in)?\.?\s*Code\s*(?:§+|ch\.)?\s*(?P<agency>[A-Z][A-Za-z]{1,5})\s*(?:§+\s*)?(?P<section>\d{1,4}(?:\.\d{2,4}[a-z]?)?)|s\.\s*(?P<agency2>[A-Z][A-Za-z]{1,5})\s+(?P<section2>\d{1,4}\.\d{2,4}[a-z]?)(?:\s*\([0-9a-z]+\))*,\s*Wis\.\s*Adm(?:in)?\.\s*Code)`
- Wisconsin Administrative Register: `Register,?\s+(?P<month>January|February|March|April|May|June|July|August|September|October|November|December),?\s+(?P<year>(?:19|20)\d\d),?\s+No\.\s*(?P<number>\d{3})(?P<part>[AB]\d?)?|\bEmR\s?(?P<emr>\d{4})\b`
- Wisconsin Supreme Court public-domain citation: `(?P<year>(?:199[5-9]|20\d\d))\s+WI\s+(?!App\b)(?P<number>\d{1,3})(?!\d)(?:,\s*¶+\s*(?P<para>\d+))?`
- Wisconsin Court of Appeals public-domain citation: `(?P<year>(?:199[5-9]|20\d\d))\s+WI\s+App\s+(?P<number>\d{1,3})(?!\d)(?:,\s*¶+\s*(?P<para>\d+))?`
- Wisconsin Reports (Wis. / Wis. 2d): `(?P<volume>\d{1,3})\s+Wis\.\s*(?P<series>2d\s+)?(?P<page>\d{1,4})(?!\d)`
- North Western Reporter with a Wisconsin parenthetical: `(?P<volume>\d{1,4})\s+N\.W\.\s*(?P<series>[23]d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\(Wis\.(?:\s*Ct\.\s*App\.)?\s*(?P<year>\d{4})\)`
- Wisconsin appeal number / unpublished opinion form (Wis. Stat. § 809.23(3)(c)): `(?P<year>(?:19|20)\d\d)AP0*(?P<seq>\d{1,6})(?:-(?P<suffix>[A-Z]{1,4}))?`
- Generic 'review denied' / 'review granted' history: `(?:petition\s+for\s+)?review\s+(?P<disposition>denied|granted|dismissed)`

Short forms → URL key:

Wis. Stat. → `statutes`; Wis. Stats. → `statutes`; Stats. → `statutes`; Wis. Admin. Code → `administrativecode`; Wis. Adm. Code → `administrativecode`; Wis. Const. → `wisconsinconstitution`; Wis. Act → `acts`; SCR → `scr`; SCR 20 (Preamble-20:1.18) → `chap20a`; SCR 20 (20:2.1-20:8.5) → `chap20b`

Wisconsin style (SCR 80.02, Wis. Stat. § 809.19) cites cases in public-domain form first: '2024 WI 13, ¶ 22, 4xx Wis. 2d ___, ___ N.W.3d ___'; public-domain citations exist for decisions from 1994/1995 onward (wicourts listings start 1995). Court of Appeals opinions are 'WI App'. The bimonthly Supreme Court disposition tables are themselves assigned a 'YYYY WI N' number (e.g. 2026 WI 33), so a 'review denied, YYYY WI N' cite resolves to a table, not an opinion. Statute sections are always CHAPTER.SECTION (no hyphens); 'Wis. Stat. §§ 893.52-893.55' is a range — the regex takes the first section. Wisconsin writes subunits with spaces ('802.06 (2) (a) 6.'); strip spaces for the URL. Appellate procedure (ch. 809) is cited as 'Wis. Stat. § (Rule) 809.62' or 'Wis. Stat. Rule 809.62'; civil procedure (chs. 801-847) and evidence (chs. 901-911) are ordinary statutes. Bare 'Rule 809.xx' and bare 'review denied' are context_required. SCR ch. 20 (professional conduct) uses a colon ('SCR 20:1.7'), which is distinctive; other SCR chapters use a dot ('SCR 22.03(2)') and route here bare only with a subunit parenthetical and a known Wisconsin SCR chapter number (Nevada also has 'SCR' rules). 'Register, Month YYYY, No. NNN' history notes cite the Administrative Register. Unpublished Court of Appeals opinions authored after July 1, 2009 may be cited for persuasive value with the form 'No. 2025AP1919, unpublished slip op. ¶ 12 (WI App Oct. 15, 2026)' (Wis. Stat. § 809.23(3)). CourtListener ids 'wis' and 'wisctapp' are from memory, unverified. Cross-routing caution: Nevada's record has a bare 'SCR \d+' pattern that also matches Wisconsin's practitioner form 'SCR 20:1.7' / 'SCR 22.03'; the colon form ('20:1.7') is uniquely Wisconsin, so route 'SCR NN:N.N' here. The colon form 'SCR 20:1.7' identifies Wisconsin; bare 'SCR NN.NN' is shared with Nevada's Supreme Court Rules and routes here only once Wisconsin is established. 'Wis. Stat. ch. 893' (chapter cite) is captured by the statutes pattern's chapter group and routes to the chapter PDF/page. The prose form 'section 893.54 of the statutes' (Wisconsin acts' drafting style) has no state marker and is context_required.

## A. Statutes / code

### `wi-acts-legis` — Wisconsin Acts (session laws)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Wisconsin Legislative Reference Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** Acts by legislative session.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://docs.legis.wisconsin.gov/document/acts/{year}/{act}[.pdf]`
  - Placeholders: year = the session year printed in the cite ('2025 Wis. Act 247' → 2025/247). Redirects to /{year}/related/acts/{act}; .pdf gives the enrolled act text.
- **Automation:** WebFetch untested · shell ok · robots: allowed
- **Currency:** act PDF header — observed: "Date of enactment: April 9, 2026"
- **Official status:** Act PDFs show date of enactment and publication; no certification statement seen online (the printed Laws of Wisconsin carry the s. 35.15 certificate).
- **Hazard:** long acts exceed the fetch tool window (2011 Wis. Act 10: 46 pp, 301,914 chars) — use fetch_doc.py
- **Probe:** 2025 Wis. Act 247 → `https://docs.legis.wisconsin.gov/document/acts/2025/247.pdf` — expect: "2025 WISCONSIN ACT 247"
- **Evidence (2026-10-17):** fetch_doc.py: → /2025/related/acts/247.pdf, 1 page, 1,803 chars; '2025 WISCONSIN ACT 247'; 'AN ACT to create 945.01 (1) (h) of the statutes'. | Independent check 2026-10-17: fetch_doc.py: /2025/related/acts/247.pdf, 1 p; 'Date of enactment: April 9, 2026 ... 2025 WISCONSIN ACT 247'; second citation 2011 Wis. Act 10 ok
- **Notes:** 2011 Wis. Act 10 → /2011/related/acts/10.pdf verified by the independent check.

### `wi-statutes-legis` — Wisconsin Statutes & Annotations (docs.legis.wisconsin.gov)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Wisconsin Legislative Reference Bureau · text: **fetch-and-quote** · official: official
- **Coverage:** Current 2023-24 Wisconsin Statutes with annotations, updated continuously; prior biennial editions under /statutes/prior/.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://docs.legis.wisconsin.gov/document/statutes/{section}{subunits}`
  - Placeholders: section = CHAPTER.SECTION exactly as cited (893.54, 940.01, 180.0302, 802.06). Optional subunits appended with spaces removed, keeping the trailing period on numbered subdivisions: Wis. Stat. § 802.06(2)(a)6. → /document/statutes/802.06(2)(a)6. The /document/ URL 302-redirects to the canonical path /statutes/statutes/{chapter}/{subchapter_roman_lower}/{section_suffix}[/{sub}/...] (893.54 → /statutes/statutes/893/v/54; 940.01 → /940/i/01; 180.0302 → /180/iii/0302; 802.06(2)(a)6. → /802/06/2/a/6). Do NOT build the canonical path yourself: chapters with subchapters need the Roman subchapter segment (/893/54 returns 404). The page is a scrolling window holding the target section plus neighbouring sections (893.54 page holds 893.52-893.55, ~31K chars).
  - Index: `https://docs.legis.wisconsin.gov/statutes/statutes`
  - Navigation: Index lists every chapter with title (no section ranges, but section numbers encode the chapter, so no hop is needed).
- **Automation:** WebFetch ok (truncated) · shell ok · robots: User-agent * Disallow: /frame, /frame/, /scroll/, /feed/, /doc/feed/, /breadcrumbs/, /preferences, /search, one LRB PDF. /document/, /statutes/, /code/, /constitution/ allowed.
  - WebFetch on a built /document/ URL was gated once (PROVENANCE_REQUIRED) and worked in the independent check, returning the section text but not the currency footer; the search-surfaced canonical URL /statutes/statutes/893/V/54 was cut mid-893.55 ('Loading...') and showed an older snapshot (Act 170, May 22, 2026) than the live page read by the script (Act 247, Oct. 1, 2026). Take the currency footer from fetch_doc.py only. /search is robots-disallowed: never use the site search.
- **Currency:** Footer of every statute page — observed: "2023-24 Wisconsin Statutes updated through 2025 Wis. Act 247 ... October 1, 2026"
- **Official status:** Every page footer: 'Published and certified under s. 35.18.' Wis. Stat. § 35.18(1)(b) requires the LRB to publish an updated electronic version with a notice that it is certified under sub. (2)(b). Not a UELMA authentication.
- **Hazard:** canonical path needs the subchapter Roman numeral: always enter via /document/statutes/{section}
- **Hazard:** page is a window of neighbouring sections; WebFetch view ends with 'Loading...'
- **Hazard:** WebFetch may serve an older cached snapshot (observed May 22, 2026 vs live Oct. 1, 2026)
- **Hazard:** section headings are concatenated with numbers in extracted text ('893.54893.54 Injury to the person.')
- **Probe:** Wis. Stat. § 893.54 → `https://docs.legis.wisconsin.gov/document/statutes/893.54` — expect: "An action to recover damages for injuries to the person"
- **Evidence (2026-10-17):** fetch_doc.py: → /statutes/statutes/893/v/54, html 31,362 chars; verify 'An action to recover damages for injuries to the person' VERIFIED. Second cite Wis. Stat. § 802.06(2)(a)6. → /802/06/2/a/6, 34,314 chars; 'Failure to state a claim upon which relief can be granted' VERIFIED. Also 940.01 → /940/i/01, 180.0302 → /180/iii/0302. WebFetch (search URL /893/V/54): YES, 'Except as provided in sub. (2m), the following actions shall'. | Independent check 2026-10-17: fetch_doc.py: /893/v/54, 31,362 chars; quote found; footer 'updated through 2025 Wis. Act 247'; second citation Wis. Stat. § 908.03(6); Wis. Stat. § 101.11 ok
- **Notes:** Per-section PDF: /document/statutes/{section}.pdf redirects to the whole-chapter PDF (see wi-statutes-pdf). Chapter-only cites ('Wis. Stat. ch. 893') route to wi-statutes-pdf or the chapter page /statutes/statutes/{chapter}.

### `wi-statutes-pdf` — Wisconsin Statutes — per-chapter PDFs

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Wisconsin Legislative Reference Bureau · text: **fetch-and-quote** · official: official
- **Coverage:** One PDF per statute chapter, current edition.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://docs.legis.wisconsin.gov/statutes/statutes/{chapter}.pdf`
  - Placeholders: chapter = integer part of the section number (893.54 → 893.pdf). /document/statutes/{section}.pdf also redirects here (with #page=0).
- **Automation:** WebFetch untested · shell ok · robots: allowed (see wi-statutes-legis)
  - Large chapters exceed the fetch tool's ~100K-character window (ch. 893: 34 pages, 448,171 extracted chars); read with fetch_doc.py grep/section.
- **Currency:** page headers/footers of the PDF — observed: "not separately recorded; same edition as HTML"
- **Official status:** Same certified publication as the HTML (s. 35.18 footer).
- **Hazard:** long chapters truncated by the fetch tool
- **Hazard:** two-column layout in chapter tables of contents
- **Probe:** Wis. Stat. ch. 893 → `https://docs.legis.wisconsin.gov/statutes/statutes/893.pdf` — expect: "893.54 Injury to the person."
- **Evidence (2026-10-17):** fetch_doc.py info: pdf, 34 pages, 448,171 chars; grep finds '893.54 Injury to the person.' in chapter TOC. /document/statutes/893.54.pdf → same file. | Independent check 2026-10-17: fetch_doc.py: 893.pdf 34 pp, 448,171 chars; '893.54 Injury to the person.' in TOC; second citation Wis. Stat. ch. 802 (802.06) ok
- **Notes:** 802.pdf: 15 pp, 195,766 chars ('802.06 Defenses and objection; when and how presented' pp. 1 and 8).

### `wi-statutes-justia` — Justia — Wisconsin Statutes & Annotations (2025)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Wisconsin Statutes; unversioned URL serves the 2025 edition; older year editions exist (e.g. /2011/).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/wisconsin/chapter-{chapter}/section-{chapter}-{section_suffix}/`
  - Placeholders: 893.54 → chapter-893/section-893-54 (dot becomes hyphen); 908.03 → chapter-908/section-908-03.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: robots.txt answers the shell with a Cloudflare challenge
  - fetch_doc.py: 'law.justia.com refused automated access earlier (robots.txt challenge)'. WebFetch only.
- **Currency:** Universal Citation line — observed: "WI Stat § 893.54 (2025)"
- **Official status:** Page states 'These codes may not be the most recent version.'
- **Hazard:** Cloudflare challenge for the shell
- **Hazard:** may lag the official text
- **Probe:** Wis. Stat. § 893.54 → `https://law.justia.com/codes/wisconsin/chapter-893/section-893-54` — expect: "Except as provided in sub. (2m), the following actions"
- **Evidence (2026-10-17):** WebFetch: YES, '(1m) Except as provided in sub. (2m), the following actions'; 'WI Stat § 893.54 (2025)'; not truncated. | Independent check 2026-10-17: WebFetch: YES '(1m) Except as provided in sub. (2m)'; 'WI Stat § 893.54 (2025)'; not truncated; second citation Wis. Stat. § 908.03 ok
- **Notes:** Pattern proven on two citations (893.54; 908.03 → 'WI Stat § 908.03 (2025)').

## B. Constitution

### `wi-constitution-legis` — Wisconsin Constitution (annotated), docs.legis.wisconsin.gov

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Wisconsin Legislative Reference Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full constitution with annotations; whole-document PDF at /constitution/wi.pdf.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://docs.legis.wisconsin.gov/document/wisconsinconstitution/{article_roman},{section}`
  - Placeholders: article as upper-case Roman numeral, section as cited (I,9; VII,3). Redirects to an opaque canonical path (/constitution/wi/000230/000020) — never build that path. Page is a window of neighbouring sections with annotations.
  - Index: `https://docs.legis.wisconsin.gov/constitution/wi`
- **Automation:** WebFetch untested · shell ok · robots: allowed
  - Whole PDF (https://docs.legis.wisconsin.gov/constitution/wi.pdf, 95 pages, 1,375,500 chars) is two-column: verbatim quote checks fail across column breaks; use the HTML.
- **Currency:** page footer — observed: "Published August 5, 2026"
- **Official status:** Footer: 'Wisconsin Constitution updated by the Legislative Reference Bureau. Published August 5, 2026.' No certification statement.
- **Hazard:** opaque canonical URLs (use /document/ redirector)
- **Hazard:** two-column whole PDF breaks exact quoting
- **Hazard:** window pages hold neighbouring articles and Roman numerals nest: the X,3 page (/000239/000004) also holds IX,3, and a plain grep for 'X,3' first hits 'IX,3 Ultimate property in lands'. Match the heading with a boundary, e.g. regex (?<![IVX])X,3, not the first hit
- **Probe:** Wis. Const. art. I, § 9 → `https://docs.legis.wisconsin.gov/document/wisconsinconstitution/I,9` — expect: "Every person is entitled to a certain remedy in the laws"
- **Evidence (2026-10-17):** fetch_doc.py: → /constitution/wi/000230/000020, 27,554 chars; quote VERIFIED. Second: VII,3 → /000236/000004, 'VII,3 Supreme court: jurisdiction. Section 3.' | Independent check 2026-10-17: fetch_doc.py: /constitution/wi/000230/000020; 'I,9 Remedy for wrongs. Section 9. Every person is entitled'; 'Published August 5, 2026'; second citation Wis. Const. art. X, § 3 ok

### `wi-constitution-justia` — Justia — Wisconsin Constitution

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Articles and sections.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/wisconsin/article-{article_roman_lower}/section-{section}/`
  - Placeholders: article-i/section-9; letter suffixes kept (section-9m). Links taken from the article page.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: Cloudflare challenge to the shell
  - WebFetch only.
- **Currency:** page notice — observed: "This Constitution may not be the most recent version."
- **Official status:** 'This Constitution may not be the most recent version.'
- **Hazard:** Cloudflare challenge for the shell
- **Probe:** Wis. Const. art. I, § 9 → `https://law.justia.com/constitution/wisconsin/article-i/section-9/` — expect: "Every person is entitled to a certain remedy in the"
- **Evidence (2026-10-17):** WebFetch: YES, 'Every person is entitled to a certain remedy in the'. Article page lists Sections 1-26. | Independent check 2026-10-17: WebFetch: YES 'Every person is entitled to a certain remedy in the'; 'may not be the most recent version'; second citation Wis. Const. art. X, § 3 ok

## C. Court rules

### `wi-scr-wicourts` — Wisconsin Supreme Court Rules (SCR) — per-chapter PDFs

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Wisconsin Supreme Court / Wisconsin Court System · text: **fetch-and-quote** · official: unknown
- **Coverage:** SCR chapters 10-14, 20 (split 20A Preamble-20:1.18 and 20B 20:2.1-20:8.5), 21-23, 30-36, 40, 50, 60-63, 70-72, 80-81 etc., each with a release date.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.wicourts.gov/sc/rules/chap{chapter}.pdf`
  - Placeholders: chapter as cited (10, 22, 60). Chapter 20 is split: SCR 20:1.x and Preamble/Terminology → chap20a.pdf; SCR 20:2.1-20:8.5 → chap20b.pdf. The index also links each chapter as a plain href (about 35 PDF links: /sc/scrule/DisplayDocument.pdf?content=pdf&seqNo={n}, e.g. 20A → seqNo=1121029; fetch_doc.py links <index> DisplayDocument lists them in row order). Index rows read: release date, then description, then the 'Chapter' link.
  - Index: `https://www.wicourts.gov/supreme/sc_rules.jsp`
- **Automation:** WebFetch gated · shell ok · robots: none (www.wicourts.gov/robots.txt returns the site's HTML 404 page)
  - chap20a.pdf is 107 pages / 298,902 chars, chap20b 64 pages / 214,011 chars: beyond the fetch tool's window. Read with fetch_doc.py.
- **Currency:** PDF Last-Modified header (the index's release-date column can lag the file: ch. 20A shows Jul 01, 2023) — observed: "chap20a.pdf Last-Modified: Tue, 19 May 2026"
- **Official status:** Index says rules 'are updated as changes are approved by the Wisconsin Supreme Court'; no official/certified statement.
- **Hazard:** long PDFs truncated by the fetch tool
- **Hazard:** chapter 20 split across two files
- **Hazard:** index release dates may lag the PDFs: ch. 20A listed Jul 01, 2023 but the file is dated May 19, 2026
- **Probe:** SCR 20:1.7 → `https://www.wicourts.gov/sc/rules/chap20a.pdf` — expect: "a lawyer shall not represent a client if the representation involves a concurrent conflict of interest"
- **Evidence (2026-10-17):** fetch_doc.py: chap20a.pdf 107 pp; SCR 20:1.7 at page 38, quote VERIFIED; SCR 20:1.18 on p. 105. Also chap10.pdf (56 pp) and chap60.pdf (40 pp) HTTP 200. | Independent check 2026-10-17: fetch_doc.py: chap20a.pdf 107 pp; p.38 'involves a concurrent conflict of interest'; Last-Modified May 19, 2026; second citation SCR 22.03 ok
- **Notes:** Civil procedure (Wis. Stat. chs. 801-847), evidence (chs. 901-911), appellate procedure (ch. 809) and criminal procedure (chs. 967-980) are statutes: use wi-statutes-legis. Uniform circuit-court rules: https://www.wicourts.gov/scrules/docs/circuitrules.pdf (not probed).

## D. Administrative code

### `wi-admincode-legis` — Wisconsin Administrative Code (docs.legis.wisconsin.gov)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Wisconsin Legislative Reference Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** Entire current Administrative Code; per-chapter PDFs.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://docs.legis.wisconsin.gov/document/administrativecode/{AGENCY}%20{section}`
  - Placeholders: AGENCY = upper-case prefix as cited (DHS, NR, ATCP, SPS, Trans); the space MUST be percent-encoded (%20). Redirects to /code/admin_code/{agency_lower}/{range}/{chapter}/[{subchapter}/]{section_suffix} (DHS 110.04 → /dhs/110/110/i/04; NR 115.05 → /nr/100/115/05); never build that path. Chapter PDF: /document/administrativecode/ch.%20{AGENCY}%20{chapter}.pdf → /code/admin_code/{agency}/{range}/{chapter}.pdf.
  - Index: `https://docs.legis.wisconsin.gov/code/admin_code`
- **Automation:** WebFetch untested · shell ok · robots: allowed
  - /code/admin_code/dhs/110/110_04 (guessed form) is 404.
- **Currency:** page footer — observed: "Updated on the first day of each month. Entire code is always current."
- **Official status:** Footer: 'Published under s. 35.93, Stats. Updated on the first day of each month.' s. 35.93 text read did not use the word 'official'.
- **Hazard:** space in URL must be encoded
- **Hazard:** window page includes neighbouring sections
- **Probe:** Wis. Admin. Code § DHS 110.04 → `https://docs.legis.wisconsin.gov/document/administrativecode/DHS%20110.04` — expect: "has the meaning given in s. 256.01"
- **Evidence (2026-10-17):** fetch_doc.py: → /code/admin_code/dhs/110/110/i/04, 19,763 chars; 'DHS 110.04 Definitions. In this chapter:'; quote VERIFIED. NR 115.05 → /nr/100/115/05 (30,031 chars). ch. DHS 110 PDF: 25 pp. | Independent check 2026-10-17: fetch_doc.py: /dhs/110/110/i/04, 19,763 chars; 'has the meaning given in s. 256.01 (1k)'; second citation Wis. Admin. Code § ATCP 134.06 ok
- **Notes:** ATCP 134.06 → /code/admin_code/atcp/090/134/06 ('ATCP 134.06 Security deposits'), independent check.

### `wi-admincode-lii` — Cornell LII — Wisconsin Administrative Code

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Wisconsin Administrative Code by agency/chapter/section.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/wisconsin/Wis-Admin-Code-SS-{AGENCY}-{chapter}-{section_suffix}`
  - Placeholders: DHS 110.04 → Wis-Admin-Code-SS-DHS-110-04; NR 115.05 → Wis-Admin-Code-SS-NR-115-05. 'Wis-Adm-Code' (no 'in') silently returns the index page — check the heading.
  - Index: `https://www.law.cornell.edu/regulations/wisconsin`
- **Automation:** WebFetch untested · shell ok · robots: 200; Crawl-delay 10
- **Currency:** bottom of section page — observed: "State regulations are updated quarterly"
- **Official status:** LII: 'State regulations are updated quarterly'.
- **Hazard:** wrong slug returns the index with HTTP 200
- **Hazard:** LII pages Last-Modified Aug 8, 2025: may lag the monthly official update
- **Probe:** Wis. Admin. Code § DHS 110.04 → `https://www.law.cornell.edu/regulations/wisconsin/Wis-Admin-Code-SS-DHS-110-04` — expect: "In this chapter"
- **Evidence (2026-10-17):** fetch_doc.py: 'DHS 110.04 - Definitions ... In this chapter: (1g) "Advanced emergency medical technician"'; NR 115.05 page heading 'NR 115.05 - Minimum zoning standards for shorelands'. | Independent check 2026-10-17: fetch_doc.py: 'In this chapter: (1g) "Advanced emergency medical technician"'; Last-Modified Aug 8, 2025; second citation Wis. Admin. Code § ATCP 134.06 ok

## D. Administrative register

### `wi-register-legis` — Wisconsin Administrative Register

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Wisconsin Legislative Reference Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** Weekly issues (e.g. 850A1, 850A2, 849B) with emergency rules, final rules, notices.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Index: `https://docs.legis.wisconsin.gov/code/register/{year}/`
  - Navigation: year page /code/register/{year}/ lists issues newest first ('850A1 Register (10/5/2026)' → /document/register/850/A1/toc → /code/register/{year}/{issue_lower}). The issue page exposes no 'Register' link to the link extractor: append '/register' to the issue URL (/code/register/2026/850a1/register) to get the item list, which links each item (e.g. EmR2609 → …/emr_effect/emr2609/emr2609). History notes cite 'Register Month YYYY No. NNN': find that issue number on the year page (issues in a month carry suffixes A1, A2, B). A bare 'EmRNNNN' cite gives no issue number: scan the year's issues' /register pages newest-first for the EmR (EmR26xx → year 2026).
- **Automation:** WebFetch untested · shell ok · robots: allowed (/feed/ and /frame/ disallowed — do not follow 'Show tree' links)
- **Currency:** year page issue list — observed: "850A2 Register (10/12/2026)"
- **Official status:** Published under s. 35.93(2)(b); no certification statement seen.
- **Hazard:** 'Show tree' links go to robots-disallowed /frame/
- **Hazard:** issue item list reached only by appending /register to the issue URL
- **Probe:** EmR2609 (Register 850A1, Oct. 5, 2026) → `https://docs.legis.wisconsin.gov/code/register/2026/850A1/register/emr_effect/emr2609/emr2609`
- **Evidence (2026-10-17):** fetch_doc.py: year page 46 links (850A2 10/12/2026 … 847A1 7/6/2026); 850A1 register page lists EmR2609…EmR2602; EmR2609 link → /code/register/2026/849a3/register/emr/emr2609_rule_text/emr2609_rule_text, 12,292 chars. | Independent check 2026-10-17: fetch_doc.py: probe redirects to /2026/849a3/.../emr2609_rule_text, 12,292 chars; 'EmR2609 Rule Text'; second citation Register December 2025 No. 840 (EmR2517) ok
- **Notes:** Independent check reached Register December 2025 No. 840 (EmR2517) via /code/register/2025/840A2/register/emr_effect/emr2517/emr2517.

## E. Case law

### `wi-opinions-appeals` — Wisconsin Court of Appeals opinions (wicourts.gov), published and unpublished

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Wisconsin Court System · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Published and unpublished opinions, per curiam and one-judge decisions, from 1995 (1995: 22 result pages) to date; listing shows district, county and '[Final publication on YYYY-MM-DD]'.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.wicourts.gov/other/appeals/caopin.jsp?range=None&pdcNo={year}+WI+App+{number}&sortBy=date`
  - Placeholders: Same GET parameters as the Supreme Court search (pdcNo, docket_number, party_name, begin_date/end_date, page). Rows link to https://www.wicourts.gov/ca/opinion/DisplayDocument.pdf?content=pdf&seqNo={n}. Unpublished opinions have no pdcNo: search by docket_number.
  - Index: `https://www.wicourts.gov/opinions/appeals.jsp`
- **Automation:** WebFetch gated · shell ok · robots: none (HTML 404 page)
  - Not tried with WebFetch after the Supreme Court PDF was gated; use fetch_doc.py.
- **Currency:** listing results — observed: "Oct 15, 2026 2026AP001629 Rock County Human Services Department v. T. S."
- **Official status:** Unpublished PDFs: 'If published, the official version will appear in the bound volume of the Official Reports.'
- **Hazard:** slip pagination only
- **Hazard:** first page flags '†Petition for Review filed'
- **Probe:** State v. Vice, 2020 WI App 34 → `https://www.wicourts.gov/ca/opinion/DisplayDocument.pdf?content=pdf&seqNo=261630` — expect: "2020 WI App 34 COURT OF APPEALS OF WISCONSIN PUBLISHED OPINION"
- **Evidence (2026-10-17):** caopin.jsp?range=None&pdcNo=2020+WI+App+34 → 2018AP002220-CR State v. Adam W. Vice, seqNo=261630; PDF 45 pp, p.1 '2020 WI App 34 ... PUBLISHED OPINION', '¶1 STARK, P.J.'. Unpublished 2025AP1919 (Oct. 15, 2026) PDF 22 pp read. | Independent check 2026-10-17: fetch_doc.py: seqNo=261630, 45 pp; '2020 WI App 34 COURT OF APPEALS OF WISCONSIN PUBLISHED OPINION'; second citation Fleming v. AAU, 2022 WI App 46; unpublished No. 2026AP929 (Oct. 14, 2026) ok
- **Notes:** Independent check: 2022 WI App 46 → seqNo=542819 (22 pp, '†Petition for Review filed'); docket_number=2026AP000929 → seqNo=1189261 (unpublished, 17 pp).

### `wi-opinions-supreme` — Wisconsin Supreme Court opinions (wicourts.gov)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Wisconsin Court System · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Slip opinions (PDF) from 1995 (1995: one results page; 1994: no records) to date, including attorney-discipline (-D) and original actions (-OA).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.wicourts.gov/supreme/scopin.jsp?range=None&pdcNo={year}+WI+{number}&sortBy=date`
  - Placeholders: Plain GET search. pdcNo = public-domain cite with '+' for spaces (2024+WI+13). Alternatives: docket_number={yyyy}AP{nnnnnn}[-suffix] (zero-pad to 6: 2020AP002007), party_name={name}, begin_date/end_date=MM/DD/YYYY (paged: &page=2). range=None is needed with pdcNo. Result rows link to https://www.wicourts.gov/sc/opinion/DisplayDocument.pdf?content=pdf&seqNo={n} — take seqNo from the result, never guess it. cite_type (N.W.2d / Wis. 2d) + volume/page search returned 'no records' when tried with value Wis2D (the form value is 'Wis. 2d'; untested).
  - Index: `https://www.wicourts.gov/opinions/supreme.jsp`
- **Automation:** WebFetch gated · shell ok · robots: none (robots.txt returns the site's HTML 404 page)
  - WebFetch on the built PDF URL: PROVENANCE_REQUIRED. Long opinions exceed the fetch tool window (2024 WI 13: 129 pp, 275,298 chars). content=html variant returns 0 chars.
- **Currency:** listing results — observed: "Mar 14, 2024 2020AP002007 Catholic Charities Bureau, Inc. v. ..."
- **Official status:** Listing: 'Published opinions are subject to further editing ... final version will appear in the bound volume of the official reports.'
- **Hazard:** slip pagination only; ¶ numbers are the pinpoint
- **Hazard:** long PDFs
- **Hazard:** seqNo not derivable from the citation
- **Probe:** Catholic Charities Bureau, Inc. v. LIRC, 2024 WI 13, ¶ 22 → `https://www.wicourts.gov/sc/opinion/DisplayDocument.pdf?content=pdf&seqNo=777152` — expect: "In an appeal from a LIRC determination, we review"
- **Evidence (2026-10-17):** scopin.jsp?range=None&pdcNo=2024+WI+13 → one row, 2020AP002007, PDF seqNo=777152; PDF p.1 '2024 WI 13 SUPREME COURT OF WISCONSIN'; '¶22 In an appeal from a LIRC determination' VERIFIED p.14. docket_number and party_name GETs also returned rows. | Independent check 2026-10-17: fetch_doc.py: seqNo=777152, 129 pp; p.14 '¶22 In an appeal from a LIRC determination, we review'; second citation Fleming v. Amateur Athletic Union, 2023 WI 40 ok
- **Notes:** Page 1 of a Supreme Court opinion states where the decision below is reported ('Reported at 406 Wis. 2d 586, 987 N.W.2d 778'). Independent check: 2023 WI 40 → seqNo=657604 (51 pp, p.1 'Reported at 404 Wis. 2d 377, 979 N.W.2d 614').

### `wi-cases-justia` — Justia — Wisconsin Supreme Court and Court of Appeals opinions

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1878-2026 (year list); Court of Appeals.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/cases/wisconsin/{supreme-court|court-of-appeals}/{year}/{docket_lower}.html`
  - Placeholders: Observed slug {docket_lower}.html (2022ap000431.html, 2021ap001054.html), but slugs can carry suffixes (2023ap001399-oa-1.html; -d, -1). Do not build the URL: open the year page and match by docket number. The year index does not show the WI citation, so resolve citation → docket on wicourts first.
  - Index: `https://law.justia.com/cases/wisconsin/supreme-court/{year}/`
  - Navigation: court index → year page → case link
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: Cloudflare challenge to the shell
  - 2026 WI 28 page is 109,178 chars: WebFetch stopped mid-¶75; continue with offset=100000.
- **Currency:** none stated
- **Official status:** Third-party copy of slip opinions.
- **Hazard:** truncation of long opinions
- **Hazard:** Cloudflare challenge for the shell
- **Hazard:** suffixed slugs (-oa-1): navigate from the year list, never construct
- **Probe:** Wisconsin State Legislature v. Kaul, 2026 WI 28 → `https://law.justia.com/cases/wisconsin/supreme-court/2026/2022ap000431.html` — expect: "The attorney general represents the state in legal matters, including"
- **Evidence (2026-10-17):** WebFetch: 2026 WI 28, ¶1 'The attorney general represents the state in legal matters, including'; ¶ numbers present; truncated at 100,000 of 109,178 chars. | Independent check 2026-10-17: WebFetch: YES ¶1 'The attorney general represents the state in legal matters'; truncated at 100,000/109,178; second citation 2023 WI 40 ok

## F. Subsequent history

### `wi-pfr-disposition-tables` — Wisconsin Supreme Court disposition tables (petitions for review, bypass, certification)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Wisconsin Court System · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Bimonthly tables, about six per year; listing shows recent tables (6 PDFs linked on 2026-10-17).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.wicourts.gov/supreme/sc_disptab.jsp`
  - Navigation: index → table PDF (/sc/DisplayDocument.pdf?content=pdf&seqNo={n}) → grep the docket number; rows give case number, caption, Granted/Denied and date.
- **Automation:** WebFetch untested · shell ok · robots: none (HTML 404 page)
- **Currency:** index release-date column — observed: "Oct 15, 2026 Disposition table - July & August 2026"
- **Official status:** Page: 'These tables will be printed in the official reports.' Each table carries a public-domain number (July & August 2026 table = 2026 WI 33).
- **Hazard:** only recent tables listed online
- **Probe:** 2026 WI 33 (July & August 2026 dispositions) → `https://www.wicourts.gov/sc/DisplayDocument.pdf?content=pdf&seqNo=1192383` — expect: "2023AP000301 Milwaukee Police Association v. City of Milwaukee Denied 8/18/2026"
- **Evidence (2026-10-17):** fetch_doc.py: 8 pp, 32,061 chars; p.1 '2026 WI 33 DISPOSITION OF PETITIONS TO THE WISCONSIN SUPREME COURT July & August 2026'; row '2023AP000301 Milwaukee Police Association v. City of Milwaukee Denied 8/18/2026'. | Independent check 2026-10-17: fetch_doc.py: 8 pp; '2023AP000301 Milwaukee Police Association v. City of Milwaukee Denied 8/18/2026'; second citation index listing ok

### `wi-pfr-orders` — Wisconsin Supreme Court orders search (petition-for-review orders by docket)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Wisconsin Court System · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court dispositional orders, including orders granting/denying petitions for review; start year not determined.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.wicourts.gov/supreme/scorder.jsp?range=None&docket_number={yyyy}AP{nnnnnn}`
  - Placeholders: Use the Court of Appeals docket number of the decision below (same number carries to the Supreme Court), zero-padded to 6 digits. Then run 'fetch_doc.py links <scorder url> DocImage': it lists the /sc/order/DisplayDocImage.pdf?docId={n} links in result-row order (the result text itself carries no docIds). Also accepts party_name and begin_date/end_date.
  - Index: `https://www.wicourts.gov/opinions/sorders.htm`
- **Automation:** WebFetch untested · shell ok · robots: none (HTML 404 page)
  - Find-by-docket works, so no party-name search is needed. A Court of Appeals opinion's p.1 '†Petition for Review filed' flag shows a petition was filed.
- **Currency:** result row — observed: "Aug 18, 2026 2023AP000301 Milwaukee Police Association v. City of Milwaukee"
- **Official status:** Court orders as filed (clerk-signed PDF).
- **Hazard:** several orders per docket: pair each docId with its row by order (e.g. 2021AP001054: 8 orders, Nov 16, 2022 row → docId=592385 'petition for review is granted')
- **Probe:** Milwaukee Police Ass'n v. City of Milwaukee, No. 2023AP301, review denied (Wis. Aug. 18, 2026) → `https://www.wicourts.gov/sc/order/DisplayDocImage.pdf?docId=1163207` — expect: "IT IS ORDERED that the petition for review is denied, without costs."
- **Evidence (2026-10-17):** scorder.jsp?range=None&docket_number=2023AP000301 → 1 row (Aug 18, 2026) linking docId=1163207; PDF 1 p: 'IT IS ORDERED that the petition for review is denied, without costs.' | Independent check 2026-10-17: fetch_doc.py: docId=1163207, 1 p; 'IT IS ORDERED that the petition for review is denied, without costs.'; second citation Fleming v. AAU, No. 2021AP1054, review granted (Wis. Nov. 16, 2022) ok
- **Notes:** Independent check: Fleming v. AAU, 2021AP001054, review granted Nov. 16, 2022 (docId=592385).

### `wi-wscca` — Wisconsin Supreme Court and Court of Appeals Case Access (WSCCA)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Wisconsin Court System · text: **link-only** · official: unofficial
- **Coverage:** Appellate dockets, including petition-for-review events.
- **Access:** `link-only` · format html
  - Index: `https://wscca.wicourts.gov/`
  - Navigation: JavaScript application; link the user to it, do not fetch.
- **Automation:** WebFetch untested · shell http-error · robots: none (404)
  - fetch_doc.py: root returns HTML with 0 extractable chars (JS shell); guessed /caseDetails.do?caseNo= and /appealHistory.xsl paths 404. Not tried further.
- **Currency:** none
- **Official status:** Docket system.
- **Hazard:** JavaScript-only
- **Probe:**  → `https://wscca.wicourts.gov/`
- **Evidence (2026-10-17):** fetch_doc.py info: html, 0 chars.
- **Notes:** Use wi-pfr-orders instead.

## Not available (do not look for these again)

- **case_law** — Free official Wisconsin Reports (Wis. 2d) pagination: wicourts listing: final version appears in the bound official reports; PDFs carry slip pagination and ¶ numbers only (2024 WI 13 PDF). (2026-10-17)
- **case_law** — wicourts.gov opinions before 1995: scopin.jsp and caopin.jsp with begin_date 01/01/1994-12/31/1994: 'Sorry, no records found'; 1995 returns rows. (2026-10-17)
- **statutes** — Site search on docs.legis.wisconsin.gov: robots.txt: Disallow: /search (2026-10-17)

## Corpus candidates (maintainers)

- `wi-scr-wicourts` — SCR ch. 20 Preamble-20:1.18: 107 pages, 298,902 chars; beyond the fetch tool's window.
- `wi-scr-wicourts` — SCR 20:2.1-20:8.5: 64 pages, 214,011 chars.
- `wi-statutes-pdf` — Chapter PDFs of the certified statutes run to 448K chars (ch. 893); HTML per-section route already works, so ingest only chapters heavily used (801-847, 809, 901-911).

## Open questions

- Bulk statute/admin-code download (XML/zip) from the LRB not found; not searched exhaustively.
- WebFetch is gated on built docs.legis and wicourts URLs; the docs.legis HTML route was confirmed only through a search-surfaced URL, and it served an older snapshot than the live page.
- Official status of the online Administrative Code (s. 35.93) and Constitution not confirmed; Wisconsin UELMA status not checked.
- Opinion search by reporter cite (cite_type='Wis. 2d' / 'N.W.2d' with cite_volume/cite_page) not confirmed working.
- Start year of scorder.jsp order coverage and of the online disposition-table archive not determined.
- Justia statute and case URL patterns each proven on one citation only.
- Circuit court local rules location not researched.
- Bare 'EmRNNNN' cites have no deterministic issue lookup in the Administrative Register; the only route is scanning that year's issues.
