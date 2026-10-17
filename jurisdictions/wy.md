# Wyoming (WY) — free legal sources

_Generated from `data/wy.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: the Legislative Service Office publishes the whole Wyoming Statutes as one PDF per title at wyoleg.gov/statutes/compress/TitleNN.pdf (constructible from the citation; fetch_doc.py reads them in full; the fetch tool is gated for these built URLs); wyoleg.gov itself is an Angular app whose HTML pages are empty to both tools, and the LSO disclaims official status. Justia (2025) is a constructible tier-2 fallback per section. Constitution: Title97.pdf on the same path, Justia one-page fallback. Court rules: full-set PDFs on wyocourts.gov (Civil Procedure, Criminal Procedure and Appellate Procedure are large annotated LexisNexis-produced pamphlets: corpus candidates). Case law: the Supreme Court is the only appellate court and has used public-domain citations ('2024 WY 138') since 2001; the official opinions list (2006 on) is a JavaScript table neither tool can read, so Justia (1870-2026, cases.justia.com PDFs readable by script) is the practical route. Admin code: rules.wyo.gov is an ASP.NET search with no permalinks; Cornell LII mirrors it per section.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Wyoming Supreme Court | `wyo (unverified)` | Wyo. | P.3d, P.2d, P., Wyo. | 2024 WY 138 (YYYY WY N, paragraphs cited as ¶ N; used since 2001) |
| Wyoming Chancery Court | `— (unverified)` | Wyo. Ch. Ct. | — | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Wyoming Statutes | `Wyo. Stat. Ann. § 1-3-105`; `Wyo. Stat. Ann. § 6-2-101(a) (2025)`; `W.S. 1-3-105(a)(iv)(C)`; `W.S. 1977 § 27-14-102`; `Wyo. Stat. § 16-3-101`; `section 1-3-105 of the Wyoming Statutes` | `wy-statutes-lso-pdf` → `wy-statutes-justia` |
| Wyoming Session Laws | `2011 Wyo. Sess. Laws ch. 1`; `1977 Wyo. Sess. Laws 456` | `wy-session-laws-lso` |
| Wyoming Constitution | `Wyo. Const. art. 1, § 8`; `Wyo. Const. art. I, § 8`; `Article 1, Section 8 of the Wyoming Constitution`; `Wyo. Const. art. 5, § 2` | `wy-constitution-lso-pdf` → `wy-constitution-justia` |
| Wyoming Rules of Civil Procedure | `W.R.C.P. 56`; `Wyo. R. Civ. P. 12(b)(6)`; `Rule 56 of the Wyoming Rules of Civil Procedure` | `wy-rules-civil` |
| Wyoming Rules of Criminal Procedure | `W.R.Cr.P. 35`; `Wyo. R. Crim. P. 35(b)`; `Rule 35 of the Wyoming Rules of Criminal Procedure` | `wy-rules-criminal` |
| Wyoming Rules of Appellate Procedure | `W.R.A.P. 1.03`; `Wyo. R. App. P. 2.07`; `Rule 9.08 of the Wyoming Rules of Appellate Procedure` | `wy-rules-appellate` |
| Wyoming Rules of Evidence | `W.R.E. 702`; `Wyo. R. Evid. 404(b)`; `Rule 702 of the Wyoming Rules of Evidence` | `wy-rules-evidence` |
| Uniform Rules for District Courts | `U.R.D.C. 802`; `Rule 802 of the Uniform Rules for District Courts of the State of Wyoming` | `wy-rules-district-uniform` |
| Wyoming Administrative Code (LII 'Wyo. Code R.' form) | `053-1 Wyo. Code R. § 1-1`; `020-2 Wyo. Code R. §§ 2-1` | `wy-admincode-lii` → `wy-admincode-sos` |
| Wyoming Administrative Code (agency.program.chapter form) | `Wyo. Admin. Code 053.0021.1`; `Wyo. Admin. Code 020.0002.2 § 2` | `wy-admincode-sos` → `wy-admincode-lii` |
| Wyoming public-domain citation | `2024 WY 138`; `Rader v. Sugarland Enters., Inc., 2006 WY 160, ¶ 12, 149 P.3d 702 (Wyo. 2006)`; `Kinstler v. RTB South Greeley, LTD., LLC, 2007 WY 98, 160 P.3d 1125` | `wy-opinions-wyocourts` → `wy-cases-justia` |
| Pacific Reporter with Wyoming parenthetical | `149 P.3d 702 (Wyo. 2006)`; `Doidge v. State Board of Charities and Reform, 789 P.2d 880, 883 (Wyo. 1990)`; `Yeager v. Forbes, 2003 WY 134, 78 P.3d 241, 2003 Wyo. LEXIS 164 (Wyo. 2003)` | `wy-cases-justia` → `wy-opinions-wyocourts` |
| Wyoming Reports (official, to 1959) and Wyo. LEXIS | `75 Wyo. 1`; `2007 Wyo. LEXIS 108` | `wy-cases-justia` |
| Wyoming Supreme Court docket number *(only once this jurisdiction is known)* | `S-24-0162`; `Docket Nos. S-24-0004, S-24-0003`; `D-24-0005` | `wy-cases-justia` → `wy-opinions-wyocourts` |

Regexes (case-insensitive):

- Wyoming Statutes: `(?:(?:Wyo(?:ming)?\.?\s*Stat(?:utes|\.)?(?:\s*Ann\.?)?|(?<![A-Za-z.])W\.\s*S\.(?:\s*1977)?),?\s*(?:§+\s*)?(?P<title>\d{1,2})-(?P<chapter>\d{1,2}[A-Za-z]?)-(?P<section>\d{3,4}[A-Za-z]?)(?!\d)|(?:sec(?:tion|\.)|§)\s*(?P<title2>\d{1,2})-(?P<chapter2>\d{1,2}[A-Za-z]?)-(?P<section2>\d{3,4}[A-Za-z]?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Wyoming\s+Statutes)`
- Wyoming Session Laws: `(?P<year>(?:18|19|20)\d\d)\s+Wyo\.\s*Sess\.\s*Laws,?\s*(?:ch\.\s*(?P<chapter>\d+)|(?P<page>\d+))`
- Wyoming Constitution: `Wyo(?:ming)?\.?\s*Const(?:itution|\.)?\s*art(?:icle|\.)?\s*(?P<article>\d{1,2}|[IVXL]+),?\s*(?:§|sec(?:tion|\.)?)\s*(?P<section>\d+[A-Za-z]?)|Article\s+(?P<article2>\d{1,2}|[IVXL]+),?\s+Section\s+(?P<section2>\d+[A-Za-z]?)\s+of\s+the\s+Wyoming\s+Constitution`
- Wyoming Rules of Civil Procedure: `(?:(?<![A-Za-z.])W\.\s*R\.\s*C\.\s*P\.|Wyo\.\s*R\.\s*Civ\.\s*P\.)\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Wyoming\s+Rules\s+of\s+Civil\s+Procedure(?!\s+for)`
- Wyoming Rules of Criminal Procedure: `(?:(?<![A-Za-z.])W\.\s*R\.\s*Cr\.\s*P\.|Wyo\.\s*R\.\s*Crim\.\s*P\.)\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Wyoming\s+Rules\s+of\s+Criminal\s+Procedure`
- Wyoming Rules of Appellate Procedure: `(?:(?<![A-Za-z.])W\.\s*R\.\s*A\.\s*P\.|Wyo\.\s*R\.\s*App\.\s*P\.)\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)\s+of\s+the\s+Wyoming\s+Rules\s+of\s+Appellate\s+Procedure`
- Wyoming Rules of Evidence: `(?:(?<![A-Za-z.])W\.\s*R\.\s*E\.|Wyo\.\s*R\.\s*Evid\.)\s*(?P<rule>\d{3,4})|Rule\s+(?P<rule2>\d{3,4})(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Wyoming\s+Rules\s+of\s+Evidence`
- Uniform Rules for District Courts: `(?<![A-Za-z.])U\.\s*R\.\s*D\.\s*C\.\s*(?P<rule>\d{3,4})|Rule\s+(?P<rule2>\d{3,4})\s+of\s+the\s+Uniform\s+Rules\s+for\s+District\s+Courts\s+of\s+the\s+State\s+of\s+Wyoming`
- Wyoming Administrative Code (LII 'Wyo. Code R.' form): `(?P<agency>\d{3})-(?P<chapter>\d{1,3})\s+Wyo\.\s*Code\s*R\.\s*§+\s*(?P<section>\d+-\d+)`
- Wyoming Administrative Code (agency.program.chapter form): `Wyo(?:ming)?\.?\s*Admin(?:istrative|\.)?\s*Code\s+(?P<agency>\d{3})\.(?P<program>\d{4})\.(?P<chapter>\d{1,3})(?:\.(?P<effective>\d{8}))?(?:\s*§\s*(?P<section>\d+))?`
- Wyoming public-domain citation: `(?P<year>(?:19|20)\d\d)\s+WY\s+(?P<number>\d{1,3})(?!\d)`
- Pacific Reporter with Wyoming parenthetical: `(?P<volume>\d{1,4})\s+P\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?(?:,\s*(?:19|20)\d\d\s+Wyo\.\s*LEXIS\s+\d+)?\s*\(Wyo\.\s*(?P<year>\d{4})\)`
- Wyoming Reports (official, to 1959) and Wyo. LEXIS: `(?<!\d)(?P<volume>\d{1,2})\s+Wyo\.\s+(?P<page>\d{1,4})(?!\d)|(?P<lexyear>(?:19|20)\d\d)\s+Wyo\.\s*LEXIS\s+(?P<lexis>\d+)`
- Wyoming Supreme Court docket number: `(?<![A-Za-z0-9-])(?P<docket>[SD]-\d{2}-\d{4})(?!\d)`

Short forms → URL key:

Wyo. Stat. Ann. → `statutes`; Wyo. Stat. → `statutes`; W.S. → `statutes`; W.S. 1977 → `statutes`; WS → `statutes`; Wyo. Const. → `Title97`; W.R.C.P. → `wy-rules-civil`; Wyo. R. Civ. P. → `wy-rules-civil`; W.R.Cr.P. → `wy-rules-criminal`; Wyo. R. Crim. P. → `wy-rules-criminal`; W.R.A.P. → `wy-rules-appellate`; Wyo. R. App. P. → `wy-rules-appellate`; W.R.E. → `wy-rules-evidence`; Wyo. R. Evid. → `wy-rules-evidence`; U.R.D.C. → `wy-rules-district-uniform`

Statute numbers are TITLE-CHAPTER-SECTION (1-3-105, 6-2-101); the title number alone picks the PDF (Title01.pdf … Title42.pdf; constitution = Title97.pdf). The hundreds digit of the section is the article within a chapter that has articles (6-2-101 = ch. 2, art. 1); Justia inserts /article-N/ only for such chapters. A range 'W.S. 16-3-101 through 115' or '§§ 1-1-101 - 1-1-105' is a span: the regex takes the first section only. 'W.S.' is the LSO's own short form (often 'W.S. 1977'); it is guarded so it does not fire inside other abbreviations. Constitution articles are Arabic in the official text ('Article 1, Section 8'); Roman numerals also accepted. Wyoming has had a public-domain citation since 2001 ('YYYY WY N', paragraph pinpoints '¶ N'); Bluebook form adds P.3d and '(Wyo. YYYY)'. The official Wyoming Reports ended in 1959 (vol. 80, from memory); bare 'NN Wyo. NNN' is that reporter. Docket numbers: S-YY-NNNN (civil/criminal appeals), D-YY-NNNN (attorney discipline); before about 2010 dockets were bare 'NN-NNN' (e.g. 06-20), too generic to route. There is no intermediate appellate court. Court-rule abbreviations follow the courts' own annotated pamphlets (W.R.C.P., W.R.Cr.P., W.R.A.P., W.R.E., U.R.D.C.); circuit-court civil rules (W.R.C.P.C.C.) are deliberately NOT matched by the W.R.C.P. pattern. The agency.program.chapter admin-code form is inferred from the Secretary of State's description of its numbering (agency, program, chapter, effective date) and was not seen in a real citation: treat as unverified. CourtListener id 'wyo' from memory, unverified. law_aliases map short forms to the source id or PDF key that serves them.

## A. Statutes / code

### `wy-session-laws-lso` — Session Laws of Wyoming (annual volume PDFs)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Wyoming Legislative Service Office · text: **fetch-and-quote** · official: unknown
- **Coverage:** Annual session laws volume; 2011 volume probed (624 pp).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://wyoleg.gov/{year}/Session%20Laws.pdf`
  - Placeholders: Verified only for 2011 (found by web search). The same pattern for 2024, 2025 and 2026 returns the app shell (soft 404), so recent volumes live elsewhere; per-act enrolled PDFs are listed on the JavaScript session pages.
  - Index: `https://wyoleg.gov/Legislation`
  - Navigation: Legislation / Session pages are JavaScript (empty to both tools); no static index of volumes found.
- **Automation:** WebFetch untested · shell ok · robots: none (404)
  - 2011 volume: 1,570,300 chars — script only.
- **Currency:** none stated
- **Official status:** Volume PDF on wyoleg.gov; no authentication statement seen; site disclaimer applies.
- **Hazard:** soft 404 on guessed years
- **Hazard:** very large PDFs
- **Probe:** 2011 Wyo. Sess. Laws ch. 1 → `https://wyoleg.gov/2011/Session%20Laws.pdf` — expect: "OMNIBUS WATER BILL-PLANNING"
- **Evidence (2026-10-17):** fetch_doc.py: pdf 624 pp, 1,570,300 chars; table of chapters '1 HB0061 OMNIBUS WATER BILL-PLANNING'. 2024-2026 same pattern: 0-char html (soft 404).
- **Notes:** Low priority; navigation for current volumes unresolved (open question).

### `wy-statutes-lso-pdf` — Wyoming Statutes — per-title PDFs (Legislative Service Office)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Wyoming Legislative Service Office · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All titles 1-42 of the Wyoming Statutes, text only (no annotations), one PDF per title; Title97 = Wyoming Constitution.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://wyoleg.gov/statutes/compress/Title{title:02d}.pdf`
  - Placeholders: title = the first number of the citation, zero-padded to 2 digits (W.S. 1-3-105 → Title01.pdf; 6-2-101 → Title06.pdf; 27-14-102 → Title27.pdf). The path is case-insensitive (IIS): /Statutes/compress/title01.pdf returns the same file. Inside the PDF each section starts with a heading line '{title}-{chapter}-{section}.   Catchline.' (e.g. '1-3-105. Actions other than recovery of real property.'); grep for '{cite}. ' (number, full stop, space) to land on the heading rather than on cross-references. Missing files do NOT 404: wyoleg.gov returns the Angular app shell (HTTP 200, 0 text chars) for unknown paths — treat a 0-char 'html' result as not found.
  - Index: `https://wyoleg.gov/stateStatutes/StatutesDownload`
  - Navigation: The StatutesDownload page is a JavaScript app (empty to both tools); its list of 43 links (Constitution + Titles 1-42) is the url_pattern above.
- **Automation:** WebFetch gated · shell ok · robots: none (404 on wyoleg.gov and www.wyoleg.gov)
  - WebFetch on Title01.pdf returned PROVENANCE_REQUIRED (built URL, permission not answered); not retried. fetch_doc.py reads whole titles (Title01: 366 pp, 730,731 chars; Title06: 210 pp, 407,091 chars) — far beyond the fetch tool's ~100K window, so the script or a corpus is the only full-text route. Section headings are indented with multiple spaces; fetch_doc.py grep normalises whitespace, so search '1-3-105. ' with ONE space.
- **Currency:** StatutesDownload page (JavaScript-rendered; read from the app bundle); the PDFs carry no currency line. HTTP Last-Modified on the PDFs: 8 May 2026. — observed: "reflects the contents of the statutes as they exist as of July 1, 2026."
- **Official status:** LSO disclaimer (wyoleg.gov/Legislature/disclaimer, JavaScript-rendered; text read from the site's app bundle): site information 'is not the official record' of the Legislature and is subject to revision. The annotated Wyoming Statutes are published by LexisNexis.
- **Hazard:** whole-title PDFs (up to ~730K chars) exceed the fetch tool window
- **Hazard:** soft 404: unknown wyoleg.gov paths return the app shell with HTTP 200
- **Hazard:** fetch tool gated on built wyoleg.gov URLs
- **Hazard:** site-wide disclaimer: not the official record
- **Probe:** Wyo. Stat. Ann. § 1-3-105 → `https://wyoleg.gov/statutes/compress/Title01.pdf` — expect: "Civil actions other than for the recovery of real property can only be brought"
- **Evidence (2026-10-17):** fetch_doc.py grep '1-3-105. ': 1 match p. 35, '(a) Civil actions other than for the recovery of real property'. Second citation W.S. 6-2-101 in Title06.pdf p. 14: 'Whoever purposely and with premeditated malice'. Title01 starts 'TITLE 1 - CODE OF CIVIL PROCEDURE'.
- **Notes:** A Folio 'text only' statutes database is also linked (wyoleg.gov/NXT/gateway.dll) — see wy-statutes-nxt. LexisNexis hosts the free annotated statutes (lexisnexis.com/hottopics/wystatutes) — not an allowed tier, not recorded as a source.

### `wy-statutes-nxt` — Wyoming Statutes — Folio NXT 'text only' database

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Wyoming Legislative Service Office · text: **link-only** · official: unofficial
- **Coverage:** Statutes and constitution as a searchable Folio infobase (per LSO statutes page).
- **Access:** `link-only` · format html
  - Index: `https://wyoleg.gov/NXT/gateway.dll?f=templates&fn=default.htm`
  - Navigation: Frame-based search forms only; no per-section URL established.
- **Automation:** WebFetch untested · shell ok · robots: none (404)
  - fetch_doc.py returns 466 chars of search-form labels ('Simple Search … <Not initialized yet>') and no links.
- **Currency:** none seen
- **Official status:** Same LSO site disclaimer as wy-statutes-lso-pdf.
- **Hazard:** frames / search forms, no deep links
- **Probe:** landing page → `https://wyoleg.gov/NXT/gateway.dll?f=templates&fn=default.htm`
- **Evidence (2026-10-17):** fetch_doc.py: 466 chars, search-form labels only, 0 links.
- **Notes:** Use the per-title PDFs instead.

### `wy-statutes-justia` — Justia — Wyoming Statutes (2025)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Wyoming Statutes, unversioned URL = 2025 edition; earlier years under /codes/wyoming/{year}/.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/wyoming/title-{title}/chapter-{chapter}/[article-{article}/]section-{title}-{chapter}-{section}/`
  - Placeholders: title and chapter unpadded. Include /article-{N}/ only when the chapter is divided into articles; N = the hundreds digit of the section (6-2-101 → article-1; 6-2-202 → article-2). Chapters without articles have none (1-3-105 → /title-1/chapter-3/section-1-3-105/). Whether a chapter has articles is not visible from the citation: if unsure, fetch https://law.justia.com/codes/wyoming/title-{title}/chapter-{chapter}/ and follow the real link.
  - Index: `https://law.justia.com/codes/wyoming/`
  - Navigation: chapter page lists section links (no body text)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable to the script (law.justia.com robots.txt challenge; host refused for the day)
  - Use WebFetch only. Even a built article URL (6-2-101) went through WebFetch without a permission prompt.
- **Currency:** page header and Universal Citation line — observed: "2025 Wyoming Statutes; WY Stat § 1-3-105 (2025)"
- **Official status:** Page says 'These codes may not be the most recent version' and disclaims warranties.
- **Hazard:** edition lags the LSO text (2025 vs. July 1, 2026)
- **Hazard:** article level present only in some chapters
- **Hazard:** shell blocked by challenge
- **Probe:** Wyo. Stat. Ann. § 1-3-105 → `https://law.justia.com/codes/wyoming/title-1/chapter-3/section-1-3-105/` — expect: "(a) Civil actions other than for the recovery of real"
- **Evidence (2026-10-17):** WebFetch YES, '(a) Civil actions other than for the recovery of real'; '2025 Wyoming Statutes'. Second: /title-6/chapter-2/article-1/section-6-2-101/ YES, '(a) Whoever purposely and with premeditated malice, or in the'. Chapter page /title-1/chapter-3/ lists section links, no body.

## B. Constitution

### `wy-constitution-lso-pdf` — Wyoming Constitution — Title 97 PDF (Legislative Service Office)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Wyoming Legislative Service Office · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole constitution as amended, 81 pp.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://wyoleg.gov/statutes/compress/Title97.pdf`
  - Placeholders: Single PDF. Sections are headed 'Article {N}, Section {M}   Catchline.' with Arabic article numbers; grep 'Article 5, Section 2 ' (trailing space) to avoid Section 20-29.
  - Index: `https://wyoleg.gov/stateStatutes/StatutesDownload`
- **Automation:** WebFetch gated · shell ok · robots: none (404)
  - 166,570 chars: beyond the fetch tool window (later articles would need offset). Not WebFetched: the same host's built PDF URL was gated.
- **Currency:** as wy-statutes-lso-pdf (StatutesDownload page) — observed: "as they exist as of July 1, 2026"
- **Official status:** Same LSO site disclaimer ('not the official record').
- **Hazard:** 166K chars: truncated in the fetch tool
- **Hazard:** fetch tool gated
- **Probe:** Wyo. Const. art. 1, § 8 → `https://wyoleg.gov/statutes/compress/Title97.pdf` — expect: "All courts shall be open and every person for an injury done"
- **Evidence (2026-10-17):** fetch_doc.py: 'TITLE 97 - WYOMING CONSTITUTION'; Art. 1 § 8 'All courts shall be open and every person for an injury' (p. 2). Second: Art. 5 § 2 'The supreme court shall have general appellate jurisdiction' (p. 25).

### `wy-constitution-justia` — Justia — Wyoming Constitution

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole constitution on one page (~137K chars).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/wyoming/`
  - Placeholders: Single page, no per-article URLs; later articles need WebFetch offset=100000.
  - Index: `https://law.justia.com/constitution/wyoming/`
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: unreadable (law.justia.com challenge)
  - 136,973 chars; WebFetch read 0-100,000.
- **Currency:** none stated
- **Official status:** Third-party compilation; no currency statement on the page.
- **Hazard:** page exceeds the fetch tool window
- **Hazard:** no currency date
- **Probe:** Wyo. Const. art. 1, § 8 → `https://law.justia.com/constitution/wyoming/` — expect: "All courts shall be open and every person for an"
- **Evidence (2026-10-17):** WebFetch YES 'All courts shall be open and every person for an'; single page; edition NOT PRESENT; 136,973 chars (window 0-100,000).

## C. Court rules

### `wy-rules-appellate` — Wyoming Rules of Appellate Procedure (annotated PDF)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Wyoming Supreme Court / Wyoming Judicial Branch · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full W.R.A.P. with annotations; 125 pp; appendices I-III separate PDFs.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.wyocourts.gov/app/uploads/2025/01/WRAP-eff-Dec-1.pdf`
  - Placeholders: Re-read from the rule page.
  - Index: `https://www.wyocourts.gov/court-rules/wyoming-rules-of-appellate-procedure/`
  - Navigation: court-rules index → rule page → 'Download Rule' link
- **Automation:** WebFetch gated · shell ok · robots: see wy-rules-civil
  - 552,805 chars.
- **Currency:** file name / rule page order table — observed: "WRAP-eff-Dec-1.pdf (Last-Modified 10 May 2026)"
- **Official status:** Published on wyocourts.gov; annotated pamphlet; no statement.
- **Hazard:** annotated two-column text
- **Hazard:** script or corpus only
- **Probe:** W.R.A.P. 9.08 → `https://www.wyocourts.gov/app/uploads/2025/01/WRAP-eff-Dec-1.pdf` — expect: "A petition for rehearing of a case in the appellate court may be filed"
- **Evidence (2026-10-17):** fetch_doc.py: 125 pp, 552,805 chars; 'Rule 9.08. Petition for Rehearing. (a) A petition for rehearing' p. 66.
- **Notes:** Annotations show the courts' own citation style, e.g. '2007 WY 98, 160 P.3d 1125, 2007 Wyo. LEXIS 108 (Wyo. 2007)'.

### `wy-rules-civil` — Wyoming Rules of Civil Procedure (annotated PDF)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Wyoming Supreme Court / Wyoming Judicial Branch · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full W.R.C.P. with history notes and case annotations; file name says effective 9-21-26; 228 pp.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.wyocourts.gov/app/uploads/2025/01/WY-Rules-of-Civ.-Procedure-Eff.-9-21-26.pdf`
  - Placeholders: File name and upload folder change with each amendment; re-read the rule page's 'Download Rule' link.
  - Index: `https://www.wyocourts.gov/court-rules/wyoming-rules-of-civil-procedure/`
  - Navigation: court-rules index → 'Wyoming Rules of Civil Procedure' page → 'Download Rule' PDF link (fetch_doc.py links … uploads).
- **Automation:** WebFetch gated · shell ok · robots: www.wyocourts.gov: User-agent * disallows /app/uploads/protected/, /protected-files/, /search and any path containing 'search' (/*search*) — which also blocks '/legal-research-resources/…'; /court-rules/ and /app/uploads/ allowed
  - 1,162,284 chars, two-column layout with interleaved annotations: grep for 'Rule 56. Summary Judgment' (heading) rather than 'Rule 56.' (cross-references). Ligatures (ﬁ) in the text layer. Plain curl gets HTTP 403 'Access denied: Automated access detected' (x-blocked-by: Fruition-Cloud-Bot-Protection) while fetch_doc.py is served — never use curl here.
- **Currency:** file name and rule page 'Order / Date Signed / Effective Date' table — observed: "WY-Rules-of-Civ.-Procedure-Eff.-9-21-26.pdf (Last-Modified 14 Aug 2026)"
- **Official status:** Published on wyocourts.gov court-rules page; the PDF is a LexisNexis-produced annotated pamphlet with case notes; no official/unofficial statement.
- **Hazard:** two-column annotated text: case notes interleave with rule text
- **Hazard:** PDF URL changes on amendment
- **Hazard:** 1.16M chars: script or corpus only
- **Hazard:** bot protection blocks generic clients
- **Probe:** W.R.C.P. 56 → `https://www.wyocourts.gov/app/uploads/2025/01/WY-Rules-of-Civ.-Procedure-Eff.-9-21-26.pdf` — expect: "A party may move for summary judgment, identifying each claim or defense"
- **Evidence (2026-10-17):** fetch_doc.py: pdf 228 pp, 1,162,284 chars; 'Rule 56. Summary Judgment. (a) … A party may move for summary judgment' at p. 169. WebFetch on the sibling evidence PDF: PROVENANCE_REQUIRED.
- **Notes:** Circuit-court civil rules, chancery rules, Uniform Rules for Circuit Courts and small-claims rules each have their own page on the same index.

### `wy-rules-criminal` — Wyoming Rules of Criminal Procedure (annotated PDF, with bond schedule)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Wyoming Supreme Court / Wyoming Judicial Branch · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full W.R.Cr.P. with annotations and bail schedule; 190 pp.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.wyocourts.gov/app/uploads/2026/06/WRCrP-with-bond-schedule.pdf`
  - Placeholders: Re-read from the rule page; URL changes on amendment.
  - Index: `https://www.wyocourts.gov/court-rules/wyoming-rules-of-criminal-procedure/`
  - Navigation: court-rules index → rule page → 'Download Rule' link
- **Automation:** WebFetch gated · shell ok · robots: see wy-rules-civil
  - 761,741 chars; grep the heading 'Rule 35\. Correction' with --regex.
- **Currency:** rule page order table; HTTP Last-Modified — observed: "Last-Modified 8 Jul 2026"
- **Official status:** Published on wyocourts.gov; annotated pamphlet; no statement.
- **Hazard:** annotated two-column text
- **Hazard:** script or corpus only (761K chars)
- **Probe:** W.R.Cr.P. 35 → `https://www.wyocourts.gov/app/uploads/2026/06/WRCrP-with-bond-schedule.pdf` — expect: "The court may correct an illegal sentence at any time."
- **Evidence (2026-10-17):** fetch_doc.py: pdf 190 pp; 'Rule 35. Correction or Reduction of Sentence. (a) Correction. — The court may correct an illegal sentence' p. 93.

### `wy-rules-district-uniform` — Uniform Rules for District Courts of the State of Wyoming (PDF)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Wyoming Supreme Court / Wyoming Judicial Branch · text: **fetch-and-quote** · official: unknown
- **Coverage:** U.R.D.C., effective August 2026; 23 pp.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.wyocourts.gov/app/uploads/2026/06/Uniform-Rules-for-District-Courts-of-Wyomingeff-August-2026.pdf`
  - Placeholders: Re-read from the rule page.
  - Index: `https://www.wyocourts.gov/court-rules/uniform-rules-for-district-courts-of-the-state-of-wyoming-2/`
  - Navigation: court-rules index → rule page → 'Download Rule' link
- **Automation:** WebFetch untested · shell ok · robots: see wy-rules-civil
  - 115,304 chars. Carries LexisNexis page-furniture strings (e.g. 'WYOMING COURT RULES 18') mid-text.
- **Currency:** file name — observed: "eff-August-2026"
- **Official status:** Published on wyocourts.gov; no statement.
- **Hazard:** page headers interleaved with rule text
- **Probe:** U.R.D.C. 802 → `https://www.wyocourts.gov/app/uploads/2026/06/Uniform-Rules-for-District-Courts-of-Wyomingeff-August-2026.pdf` — expect: "Rule 802"
- **Evidence (2026-10-17):** fetch_doc.py: 23 pp, 115,304 chars; 'Rule 802' heading found p. 16.
- **Notes:** Rules of Professional Conduct for Attorneys at Law: https://www.wyocourts.gov/app/uploads/2026/06/WY-Rules-Prof-Conduct-Eff.-9-21-26.pdf (140 pp, 569,634 chars; script info only).

### `wy-rules-evidence` — Wyoming Rules of Evidence (PDF)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Wyoming Supreme Court / Wyoming Judicial Branch · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full W.R.E.; 26 pp.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.wyocourts.gov/app/uploads/2025/01/WYOMING-RULES-OF-EVIDENCE-1.pdf`
  - Placeholders: Re-read from the rule page.
  - Index: `https://www.wyocourts.gov/court-rules/wyoming-rules-of-evidence/`
  - Navigation: court-rules index → rule page → 'Download Rule' link
- **Automation:** WebFetch gated · shell ok · robots: see wy-rules-civil
  - 92,805 chars — would fit in one fetch-tool window, but WebFetch returned PROVENANCE_REQUIRED. Superseded versions are kept beside current ones ('Effective until August 1, 2019' / 'Effective August 1, 2019'): quote the current one.
- **Currency:** per-rule '(Effective …)' labels; HTTP Last-Modified — observed: "Rule 702. Testimony by experts (Effective August 1, 2019.)"
- **Official status:** Published on wyocourts.gov; no statement.
- **Hazard:** old and new versions of the same rule both present
- **Probe:** W.R.E. 702 → `https://www.wyocourts.gov/app/uploads/2025/01/WYOMING-RULES-OF-EVIDENCE-1.pdf` — expect: "A witness who is qualified as an expert by knowledge, skill, experience"
- **Evidence (2026-10-17):** fetch_doc.py: 26 pp, 92,805 chars; Rule 702 (Effective August 1, 2019) p. 10; verify 'Rule 1008.' VERIFIED p. 25. WebFetch: PROVENANCE_REQUIRED.

## D. Administrative code

### `wy-admincode-sos` — Wyoming Administrative Rules (Code) — Secretary of State rules system

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Wyoming Secretary of State · text: **link-only** · official: unknown
- **Coverage:** Current, proposed, emergency, superseded and repealed rules, indexed by agency number, program number, chapter number and effective date.
- **Access:** `search-only` · format html
  - Index: `https://rules.wyo.gov/Search.aspx?mode=7`
  - Navigation: Administrative Code search (ASP.NET postback form: agency, program, keyword) → chapter row → document download. No GET permalink for a chapter was found; the Agencies.aspx listing gives agency names only.
- **Automation:** WebFetch gated · shell ok · robots: none (404)
  - fetch_doc.py reads the landing and search pages (7,650 / 5,221 chars) but the search is a POST form; WebFetch on https://rules.wyo.gov/ returned PROVENANCE_REQUIRED.
- **Currency:** per-rule effective date in the search results (not reached)
- **Official status:** rules.wyo.gov: the SOS is 'the repository for rules and regulations'; agencies are responsible for content. No official-text statement seen.
- **Hazard:** POST-only search, no permalinks
- **Hazard:** fetch tool gated
- **Probe:** Administrative Code search page → `https://rules.wyo.gov/Search.aspx?mode=7` — expect: "ADMINISTRATIVE RULES (CODE)"
- **Evidence (2026-10-17):** fetch_doc.py: page text 'ADMINISTRATIVE RULES (CODE) This includes all Current and Repealed rules.'; no rule text reachable by GET.
- **Notes:** Use wy-admincode-lii for text; cite the SOS system as the official repository.

### `wy-admincode-lii` — Cornell LII — Wyoming Administrative Code

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Cornell Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All agencies, per section, with version numbers and 'Amended, Eff.' notes.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/wyoming/agency-{agency:03d}/subagency-{program:04d}/chapter-{chapter}`
  - Placeholders: Agency/subagency/chapter pages are constructible from agency number (3 digits), program (4 digits) and chapter. Section URLs are NOT uniform: one chapter links sections under the chapter path (…/chapter-1/053-1-Wyo-Code-R-SSSS-1-1), another links them flat (…/regulations/wyoming/020-2-Wyo-Code-R-SSSS-2-1). Always take the section link from the chapter page.
  - Index: `https://www.law.cornell.edu/regulations/wyoming`
  - Navigation: agency list → agency-NNN → subagency-NNNN → chapter-N → section link
- **Automation:** WebFetch untested · shell ok · robots: law.cornell.edu permits these paths (script not refused)
- **Currency:** page footer 'updated quarterly'; Last-Modified header — observed: "State regulations are updated quarterly (Last-Modified 8 Aug 2025)"
- **Official status:** Third-party mirror; 'State regulations are updated quarterly'.
- **Hazard:** quarterly lag; Last-Modified Aug 2025 suggests older snapshot
- **Hazard:** inconsistent section URL shapes
- **Probe:** 053-1 Wyo. Code R. § 1-1 → `https://www.law.cornell.edu/regulations/wyoming/agency-053/subagency-0021/chapter-1/053-1-Wyo-Code-R-SSSS-1-1` — expect: "These rules, regulations and fee schedules are adopted by the"
- **Evidence (2026-10-17):** fetch_doc.py: '053-1 Wyo. Code R. §§ 1-1 - Authority'; body 'These rules, regulations and fee schedules are adopted by the'; 'Amended, Eff. 8/24/2017'. Second: 020-2 Wyo. Code R. § 2-1 (DEQ Air Quality ch. 2) page present.

## D. Administrative register

### `wy-register-sos-proposed` — Proposed Rules Open for Comment (Secretary of State rules system)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Wyoming Secretary of State · text: **link-only** · official: unknown
- **Coverage:** Proposed and emergency rule filings with comment periods; Wyoming publishes no separate register volume (none found).
- **Access:** `search-only` · format html
  - Index: `https://rules.wyo.gov/Search.aspx?mode=5`
  - Navigation: ASP.NET listing/search; no permalinks found.
- **Automation:** WebFetch untested · shell untested · robots: none (404)
  - Link found on rules.wyo.gov home page; not probed for content.
- **Currency:** 
- **Hazard:** POST search
- **Probe:**  → `https://rules.wyo.gov/Search.aspx?mode=5`
- **Evidence (2026-10-17):** Linked from rules.wyo.gov ('Proposed Rules Open for Comment'); not fetched.
- **Notes:** Legislative Service Office rule-review copies of filed rules also exist at wyoleg.gov/arules/{year}/rules/ARRyy-nnnP.pdf (seen in search results only).

## E. Case law

### `wy-chancery-decisions` — Wyoming Chancery Court Orders and Decisions

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Wyoming Chancery Court · text: **link-only** · official: unknown
- **Coverage:** Chancery Court (business and trust matters, created 2023) orders and decisions.
- **Access:** `link-only` · format pdf
  - Index: `https://www.wyocourts.gov/chancery-court-orders-and-decisions/`
  - Navigation: JavaScript database; no document links visible to the script.
- **Automation:** WebFetch untested · shell ok · robots: see wy-rules-civil
  - fetch_doc.py: 8,048 chars, 0 upload links.
- **Currency:** 
- **Official status:** Page says orders and decisions are published in a searchable electronic database pursuant to Wyo. Stat. Ann. § 5-13-104(f).
- **Hazard:** JavaScript-only database
- **Probe:** page → `https://www.wyocourts.gov/chancery-court-orders-and-decisions/` — expect: "published in a searchable electronic database pursuant to Wyo. Stat. Ann. § 5-13-104(f)"
- **Evidence (2026-10-17):** fetch_doc.py: description text present, no decision links.

### `wy-opinions-wyocourts` — Wyoming Supreme Court Opinions (official search)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Wyoming Supreme Court · text: **link-only** · official: unknown
- **Coverage:** Opinions and orders from 2006 ('Opinions and orders published prior to 2006 are not available in this search').
- **Access:** `link-only` · format pdf
  - Index: `https://www.wyocourts.gov/wy-supreme-court-opinions/`
  - Navigation: The table (Opinion ID, Publish Date, Appellant, Appellee, Docket Number) and its search (date range, appellant, appellee) are filled by JavaScript; neither tool sees rows or document links. The data endpoint was not identified (the site's /wp-json/api/v1/dynamictable route returns HTTP 400 without parameters).
- **Automation:** WebFetch fail · shell ok · robots: see wy-rules-civil; note any URL containing 'search' is disallowed
  - WebFetch: headers only, no rows. fetch_doc.py: 7,739 chars of page chrome, no opinion links. curl: HTTP 403 bot protection.
- **Currency:** none
- **Official status:** Court's own opinion list; no statement on official status.
- **Hazard:** JavaScript-only table
- **Hazard:** robots disallows any path containing 'search'
- **Hazard:** bot protection on generic clients
- **Probe:** 2024 WY 138 → `https://www.wyocourts.gov/wy-supreme-court-opinions/` — expect: "Opinions and orders published prior to 2006 are not available in this search."
- **Evidence (2026-10-17):** WebFetch: table headers, 'NO' rows; coverage note 'published prior to 2006 are not available'. fetch_doc.py links: 81 site links, none to opinions.
- **Notes:** Opinion PDFs carry the public-domain cite and [¶N] paragraphs (seen in Justia copies of the court's PDFs). Supreme Court Opinion Summaries page exists (https://www.wyocourts.gov/supreme-court-opinion-summaries/) with no per-opinion links visible.

### `wy-cases-justia` — Justia — Wyoming Supreme Court decisions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** 1870-2026 year listings.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/cases/wyoming/supreme-court/{year}/{docket_lower}.html`
  - Placeholders: Recent years: case page = /{year}/{docket lower-case}.html (S-24-0162 → s-24-0162.html; discipline D-24-0005 → d-24-0005.html) and PDF = https://cases.justia.com/wyoming/supreme-court/{year}-{docket_lower}.pdf (the ?ts= query is optional). With several dockets the first-listed docket is used (2024 WY 138, Nos. S-24-0004, S-24-0003 → s-24-0004). Older years (e.g. 2006) use numeric ids (/2006/448386.html) — take them from the year listing. The public-domain number is NOT in the URL: map 'YYYY WY N' to a docket via the year listing.
  - Index: `https://law.justia.com/cases/wyoming/supreme-court/{year}/`
  - Navigation: year listing (shows name, date, docket, YYYY WY N and P.3d) → case page; PDF link on the case page
  - Read via: cases.justia.com PDFs are readable by fetch_doc.py (robots disallows only /static/pdf-js/web/); law.justia.com pages by WebFetch only.
- **Automation:** WebFetch ok (truncated) · shell ok · robots: law.justia.com: challenge (script refused); cases.justia.com: Disallow /static/pdf-js/web/ only
  - shell 'ok' applies to cases.justia.com PDFs only; law.justia.com is blocked-challenge for the script. WebFetch cut 2024 WY 138 (112,583 chars) at ¶101 — read the PDF by script for long opinions.
- **Currency:** year listing — observed: "latest year listed 2026"
- **Official status:** Third-party; PDFs at cases.justia.com are copies of the court's slip opinions (caption 'IN THE SUPREME COURT, STATE OF WYOMING 2024 WY 138').
- **Hazard:** long opinions truncated in WebFetch
- **Hazard:** older years use numeric ids
- **Hazard:** public-domain cite not in URL
- **Hazard:** only slip pagination (¶ numbers); no P.3d page breaks
- **Probe:** Hogan & Assocs. Builders, LLC v. Eiden Constr., LLC, 2024 WY 138 → `https://law.justia.com/cases/wyoming/supreme-court/2024/s-24-0004.html` — expect: "Eiden Construction, LLC (Eiden) entered into an earthwork and utilities"
- **Evidence (2026-10-17):** WebFetch: body to ¶101 then truncated (112,583 chars). fetch_doc.py on cases.justia.com/…/2024-s-24-0004.pdf: 41 pp, '2024 WY 138 OCTOBER TERM, A.D. 2024'; 2024-s-24-0162.pdf (no ts): '2024 WY 139'. Older: /2006/448386.html (2006 WY 160) full body, ¶1-¶26.
- **Notes:** Justia year listing gives P.3d parallels for older years (e.g. 2006 WY 160 = 149 P.3d 702).

## F. Subsequent history

### `wy-subsequent-history` — Wyoming Supreme Court — rehearing orders and public docket

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Wyoming Supreme Court · text: **link-only** · official: unknown
- **Coverage:** No intermediate appellate court: district-court and chancery decisions go straight to the Supreme Court; its decisions are reviewed only on petition for rehearing (W.R.A.P. 9.08, within 15 days) or by U.S. Supreme Court certiorari.
- **Access:** `link-only` · format html
  - Index: `https://ctefiling.wyocourts.gov/portal/home`
  - Navigation: Public docket portal (JavaScript app; linked from the Supreme Court page as 'Public Docket'). Without it: find the appeal on Justia's year listing by PARTY NAME (the listing shows docket and lower court only in the opinion caption); trial-court case numbers are not indexed.
- **Automation:** WebFetch untested · shell ok · robots: ctefiling.wyocourts.gov/robots.txt returns the app shell (0 chars) — no rules
  - fetch_doc.py: 0-char JavaScript shell.
- **Currency:** 
- **Hazard:** JavaScript-only docket
- **Hazard:** in practice findable only by party name
- **Probe:** docket portal → `https://ctefiling.wyocourts.gov/portal/home`
- **Evidence (2026-10-17):** fetch_doc.py 0 chars (app shell); rehearing rule W.R.A.P. 9.08 read in wy-rules-appellate.

## Not available (do not look for these again)

- **statutes** — public.law edition of the Wyoming Statutes: wyoming.public.law: proxy 'Tunnel connection failed: 502' (no such host). (2026-10-17)
- **statutes** — Official HTML per-section statute pages on wyoleg.gov: wyoleg.gov is an Angular app (0-char shell to the script); statutes are offered only as per-title PDFs, the Folio NXT search, and LexisNexis's annotated site. (2026-10-17)
- **case_law** — Official opinions before 2006 on wyocourts.gov: Opinions page: 'Opinions and orders published prior to 2006 are not available in this search.' (2026-10-17)
- **case_law** — Free official reporter (P.3d) pagination: Slip PDFs carry 'YYYY WY N' and ¶ numbers only; P.3d is West's. Wyoming Reports ceased long ago. (2026-10-17)
- **case_law** — Intermediate appellate court: Wyoming has none; Wyo. Const. art. 5, § 2 gives the supreme court general appellate jurisdiction. (2026-10-17)
- **admin_register** — A published Wyoming administrative register volume: rules.wyo.gov offers only proposed/emergency rule listings; no register publication linked from the rules system home page. (2026-10-17)

## Corpus candidates (maintainers)

- `wy-statutes-lso-pdf` — Each title PDF exceeds the fetch tool window (Title01 730,731 chars; Title06 407,091 chars); 42 titles in all. · bulk: https://wyoleg.gov/statutes/compress/Title{01..42}.pdf (no zip; Word set on USB sold by LSO)
- `wy-constitution-lso-pdf` — 166,570 chars; fetch tool gated and would truncate.
- `wy-rules-civil` — 1,162,284 chars, two-column, annotations interleaved.
- `wy-rules-criminal` — 761,741 chars, annotated.
- `wy-rules-appellate` — 552,805 chars, annotated.

## Open questions

- Where the official Supreme Court opinion PDFs (2006 on) are served and what the JavaScript table calls; documents.wyocourts.gov did not resolve through the proxy.
- URL or index for Session Laws volumes after 2011 (the 2011 pattern soft-404s for 2024-2026).
- Whether any GET permalink exists for a rules.wyo.gov chapter document.
- Real-world form of the agency.program.chapter admin-code citation (pattern inferred from the SOS numbering description).
- Folio NXT statutes database: per-section deep links not established.
- CourtListener id 'wyo' unverified.
- WebFetch untested on wyocourts.gov rule PDFs beyond one gated attempt; independent verifier should retry from a provenance-carrying link.
