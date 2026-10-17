# Nebraska (NE) — free legal sources

_Generated from `data/ne.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes and Constitution: nebraskalegislature.gov serves one constructible page per section (statutes.php?statute=25-207; articles.php?article=I-3) that fetch_doc.py reads (WebFetch is gated for built URLs); the printed Reissue volumes and Supplements are free PDFs, and Justia 2025 is the constructible tier-2 fallback. Court rules: nebraskajudicial.gov per-rule pages and whole-article print exports, index-anchored. Case law: the Nebraska Appellate Courts Online Library serves advance-sheet PDFs with official Neb./Neb. App. pagination, located by a plain-GET search on docket or cite; further-review dispositions are in per-volume PFR lists. The Administrative Code site (rules.nebraska.gov) is JavaScript-only with a 401 API, so Cornell LII is the only readable text; Nebraska has no register.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Nebraska Supreme Court | `neb (unverified)` | Neb. | Neb., N.W.3d, N.W.2d, N.W. | — |
| Nebraska Court of Appeals | `nebctapp (unverified)` | Neb. Ct. App. | Neb. App., N.W.3d, N.W.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Nebraska Revised Statutes | `Neb. Rev. Stat. § 25-207 (Reissue 2016)`; `Neb. Rev. Stat. § 77-2701.10 (Cum. Supp. 2024)`; `Neb. Rev. Stat. §§ 25-207 to 25-212`; `R.R.S. Neb. § 27-702`; `Neb. Rev. Stat. Ann. § 25-222`; `section 25-207 of the Nebraska Revised Statutes`; `Neb. U.C.C. § 2-207`; `Neb. Rev. Stat. UCC § 2-207` | `ne-statutes-leg` → `ne-statutes-justia` → `ne-statutes-pdf-volumes` |
| Nebraska statutes (bare section, Nebraska context) *(only once this jurisdiction is known)* | `§ 25-207`; `section 25-1912`; `sections 25-207 and 25-222` | `ne-statutes-leg` → `ne-statutes-justia` |
| Nebraska Evidence Rules (codified at Neb. Rev. Stat. ch. 27) | `Neb. Evid. R. 702`; `Rule 702 of the Nebraska Evidence Rules`; `Neb. R. Evid. 803(1)` | `ne-statutes-leg` → `ne-statutes-justia` |
| Nebraska Constitution | `Neb. Const. art. I, § 3`; `Neb. Const. art. VIII, § 1A`; `Article V, section 2, of the Nebraska Constitution`; `Neb. Const. art. I, § 7` | `ne-constitution-leg` → `ne-constitution-justia` |
| Nebraska Court Rules (Neb. Ct. R.) | `Neb. Ct. R. § 6-1112`; `Neb. Ct. R. Pldg. § 6-1112(b)(6)`; `Neb. Ct. R. App. P. § 2-109(D)(1)`; `Neb. Ct. R. of Prof. Cond. § 3-501.7`; `Neb. Ct. R. Disc. § 6-326`; `§ 6-1112 of the Nebraska Court Rules of Pleading in Civil Cases` | `ne-rules-judicial` |
| Nebraska Administrative Code | `53 Neb. Admin. Code, ch. 2, § 002`; `471 Neb. Admin. Code ch. 23, § 007`; `Title 92 NAC Chapter 51`; `92 NAC 51-003.01`; `Neb. Admin. Code tit. 471, ch. 23, § 007` | `ne-admincode-lii` → `ne-admincode-rules` |
| Nebraska Reports / Nebraska Appellate Reports | `State v. Evans, 321 Neb. 841, ___ N.W.3d ___ (2026)`; `Martinez v. Amerigreen, 34 Neb. App. 347 (2026)`; `Lee v. Brodbeck, 196 Neb. 393, 243 N.W.2d 331 (1976)`; `Anonymous v. St. John Lutheran Church, 14 Neb. App. 42, 703 N.W.2d 918 (2005)` | `ne-opinions-library` → `ne-cases-justia` → `ne-opinions-judicial` |
| North Western Reporter with a Nebraska parenthetical | `243 N.W.2d 331 (Neb. 1976)`; `703 N.W.2d 918 (Neb. App. 2005)`; `12 N.W.3d 345 (Neb. Ct. App. 2024)` | `ne-opinions-library` → `ne-cases-justia` |
| Nebraska appellate docket numbers (S- / A- dockets) *(only once this jurisdiction is known)* | `No. S-25-209`; `No. A-25-855`; `State v. Spencer, No. A-25-855, 2026 WL 1234567 (Neb. App. Oct. 13, 2026)` | `ne-opinions-library` → `ne-opinions-judicial` → `ne-cases-justia` |
| Westlaw / Lexis unreported Nebraska cites | `2026 WL 1234567 (Neb. App. Oct. 13, 2026)`; `2021 Neb. App. LEXIS 112` | `ne-opinions-library` → `ne-cases-justia` |
| Further review dispositions (Nebraska parenthetical) | `further review denied (Neb. Oct. 9, 2026)`; `petition for further review granted (Neb. Aug. 24, 2026)` | `ne-pfr-lists` |
| Generic 'further review denied' history *(only once this jurisdiction is known)* | `further review denied`; `petition for further review denied` | `ne-pfr-lists` |

Regexes (case-insensitive):

- Nebraska Revised Statutes: `(?:Neb\.\s*Rev\.\s*Stat\.(?:\s*Ann\.)?|R\.\s*R\.\s*S\.\s*Neb\.|Neb\.\s*Rev\.\s*St\.)\s*(?:U\.?C\.?C\.?\s*)?§+\s*(?P<section>\d{1,3}[A-Z]?-\d{1,4}(?:\.\d{1,3})?)(?![\d.]*\d)|(?:sec(?:tion|\.)|§)\s*(?P<section2>\d{1,3}[A-Z]?-\d{1,4}(?:\.\d{1,3})?)(?:\([a-z0-9]+\))*,?\s+of\s+the\s+(?:Nebraska\s+Revised\s+Statutes|Revised\s+Statutes\s+of\s+Nebraska)|Neb\.\s*U\.\s*C\.\s*C\.\s*§+\s*(?P<ucc>\d{1,2}[A-Z]?-\d{3}(?:\.\d+)?)`
- Nebraska statutes (bare section, Nebraska context): `(?:sec(?:tion|\.)s?|§+)\s*(?P<section>\d{1,3}[A-Z]?-\d{1,4}(?:\.\d{1,3})?)(?![\d.]*\d)`
- Nebraska Evidence Rules (codified at Neb. Rev. Stat. ch. 27): `Neb\.\s*(?:Evid\.\s*R\.|R\.\s*Evid\.)\s*(?P<rule>\d{3,4})|Rule\s+(?P<rule2>\d{3,4})(?:\([a-z0-9]+\))*\s+of\s+the\s+Nebraska\s+(?:Evidence\s+Rules|Rules\s+of\s+Evidence)`
- Nebraska Constitution: `Neb\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*§\s*(?P<section>\d+[A-Z]?)|Article\s+(?P<article2>[IVXL]+),?\s+(?:section|§)\s*(?P<section2>\d+[A-Z]?),?\s+of\s+the\s+(?:Nebraska\s+Constitution|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Nebraska)`
- Nebraska Court Rules (Neb. Ct. R.): `Neb\.\s*Ct\.\s*R\.(?:\s+(?:of\s+)?[A-Z][A-Za-z]*\.?){0,4}\s*§+\s*(?P<rule>(?P<chapter>[1-6])-\d{3,4}(?:\.\d{1,2})?)|§+\s*(?P<rule2>[1-6]-\d{3,4}(?:\.\d{1,2})?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Nebraska\s+(?:Court\s+Rules|Rules\s+of\s+Professional\s+Conduct|Supreme\s+Court\s+Rules)`
- Nebraska Administrative Code: `(?P<title>\d{1,3})\s+Neb\.\s*Admin\.\s*Code,?\s*(?:ch\.|Chapter)\s*(?P<chapter>\d{1,3}[A-Z]?)(?:,?\s*§+\s*(?P<section>\d{3}(?:\.\d+)*))?|Neb\.\s*Admin\.\s*Code\s+tit\.\s*(?P<title2>\d{1,3}),?\s*ch\.\s*(?P<chapter2>\d{1,3}[A-Z]?)(?:,?\s*§+\s*(?P<section2>\d{3}(?:\.\d+)*))?|Title\s+(?P<title3>\d{1,3})\s+(?:Neb\.\s*Admin\.\s*Code|NAC),?\s*(?:ch\.|Chapter)\s*(?P<chapter3>\d{1,3}[A-Z]?)|(?P<title4>\d{1,3})\s+NAC\s+(?P<chapter4>\d{1,3}[A-Z]?)-(?P<section4>\d{3}(?:\.\d+)*)`
- Nebraska Reports / Nebraska Appellate Reports: `(?P<volume>\d{1,3}|_{2,})\s+Neb\.(?:\s*(?P<app>App)\.)?\s+(?P<page>\d{1,4}|_{2,})(?![\d.])`
- North Western Reporter with a Nebraska parenthetical: `(?P<volume>\d{1,4})\s+N\.\s*W\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>Neb\.(?:\s*(?:Ct\.\s*)?App\.)?)\s*(?P<year>\d{4})\)`
- Nebraska appellate docket numbers (S- / A- dockets): `\b(?P<court>[SA])-(?P<yy>\d{2})-(?P<num>\d{3,4})\b`
- Westlaw / Lexis unreported Nebraska cites: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Neb\.|Neb\.\s*(?:App\.\s*)?LEXIS\s+(?P<lexis>\d+))`
- Further review dispositions (Nebraska parenthetical): `(?:petition\s+for\s+)?further\s+review\s+(?P<disposition>denied|granted|dismissed)\s*\(Neb\.\s*(?P<date>[A-Z][a-z]{2,4}\.?\s+\d{1,2},\s*(?P<year>\d{4}))\)`
- Generic 'further review denied' history: `(?:petition\s+for\s+)?further\s+review\s+(?P<disposition>denied|granted|dismissed)`

Nebraska style: 'Name, 321 Neb. 841, ___ N.W.3d ___ (2026)'; statutes cite the print volume, e.g. 'Neb. Rev. Stat. § 25-207 (Reissue 2016)' or '(Cum. Supp. 2024)' / '(Supp. 2025)' - the volume tag is not part of the URL. Nebraska courts write '(Neb. App. 2021)' while Bluebook uses '(Neb. Ct. App. 2021)'; both match. Court of Appeals memorandum opinions are 'not designated for permanent publication' and cite only as § 2-102(E) allows. Court rules: 'Neb. Ct. R.' plus an optional set tag (Pldg., App. P., Disc., of Prof. Cond.) and '§ c-nnnn'; former pleading rule N = § 6-11NN. Evidence rules are statutes: Neb. Evid. R. N = Neb. Rev. Stat. § 27-N. 'NAC' alone is also Nevada's code: the Nebraska pattern requires the title number before 'NAC' and a hyphenated chapter-section ('92 NAC 51-003'). Bare '§ 25-207', bare S-/A- docket numbers and bare 'further review denied' (Iowa also uses 'further review') are context_required. A '§§ a to b' range is two sections: take the first. CourtListener ids from memory, unverified.

## A. Statutes / code

### `ne-statutes-leg` — Nebraska Revised Statutes (nebraskalegislature.gov)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Nebraska Legislature / Revisor of Statutes · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All chapters of the Nebraska Revised Statutes, one page per section with source (session-law history), cross references and annotations; Uniform Commercial Code on a separate endpoint (ucc.php?code=); Appendix via browse-appendix.php.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://nebraskalegislature.gov/laws/statutes.php?statute={chapter}-{section}`
  - Placeholders: {chapter}-{section} exactly as cited (25-207, 27-702, 77-2701.10; lettered chapters such as 81-1505.04 or 2-4004 likewise as printed). Drop subsection parentheticals ('25-207(1)' -> 25-207). UCC (cited 'Neb. U.C.C. § 2-207' or 'Neb. Rev. Stat. UCC § 2-207') -> https://nebraskalegislature.gov/laws/ucc.php?code={article}-{section}. Chapter listing: /laws/browse-chapters.php?chapter={chapter} lists every section in one flat table (no article headings or ranges). Print view: append &print=true.
  - Index: `https://nebraskalegislature.gov/laws/browse-statutes.php`
- **Automation:** WebFetch gated · shell ok · robots: User-agent: * Disallow /trans/search.php, /bills/search_by_date.php, /bills/search_by_introducer.php; Crawl-delay: 3. /laws/ not disallowed.
  - Built section URL (statutes.php?statute=25-207) hit the WebFetch provenance gate; use fetch_doc.py. The chapter listing (from a WebSearch hit) did read in WebFetch but is truncated: chapter 25 listing (224K chars) stopped at 25-1013. Section pages include long annotation lists after the text (25-207: 26.6K chars) - quote only from the block between the heading and 'Source'.
- **Currency:** none on section pages; /laws/laws.php 'Reissue and Supplement publication dates' table — observed: "Supplement 2025; Cumulative Supplement 2024"
- **Official status:** Site disclaimer (https://nebraskalegislature.gov/contact/disclaimer.php): no warranty on content; for matters affecting legal rights refer to the printed version of the official publication. No UELMA authentication statement seen.
- **Hazard:** no currency line on section pages
- **Hazard:** annotations follow the section text on the same page - do not quote annotation text as statute
- **Hazard:** chapter listing pages exceed WebFetch's window (chapter 25 cut at 25-1013); use fetch_doc.py links
- **Hazard:** UCC sections use a different endpoint (ucc.php?code=) than statutes.php
- **Hazard:** Bluebook/Nebraska cites carry the print volume ('Reissue 2016', 'Cum. Supp. 2024'); the web page shows only the current text
- **Probe:** Neb. Rev. Stat. § 25-207 → `https://nebraskalegislature.gov/laws/statutes.php?statute=25-207` — expect: "The following actions can only be brought within four years"
- **Evidence (2026-10-17):** fetch_doc.py: html 26,651 chars; '25-207. Actions for trespass, conversion, other torts, and frauds; exceptions.' Also 27-702 ('a witness qualified as an expert by knowledge, skill'), 77-2701.10, UCC 2-207 (ucc.php) OK. WebFetch on built URL: PROVENANCE_REQUIRED.
- **Notes:** Section heading line format '25-207.' then catchline; history in 'Source' paragraph (e.g. 'R.S.1867, Code § 12, p. 395').

### `ne-statutes-pdf-volumes` — Nebraska Revised Statutes - Reissue volumes and Supplements (PDF)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Nebraska Revisor of Statutes · text: **fetch-and-quote** · official: unknown
- **Coverage:** Reissue volumes 1-6 (dates vary by volume: 2016-2024; UCC Reissue 2020), 2025 Supplement (2 vols), 2024 Cumulative Supplement (3 vols), older supplements, General Index 2025, Cross Reference Tables 1943-2026.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://nebraskalegislature.gov/pdf/revisor/{year}reissue_v{volume}.pdf`
  - Placeholders: Volume -> chapter span and reissue year are listed on /laws/laws.php (e.g. Vol. 2 = ch. 24-28, Reissue 2016 -> 2016reissue_v2.pdf; Vol. 5 = ch. 78-80 -> 2024reissue_v5.pdf). Supplements: {year}suppv{n}.pdf (2025suppv1.pdf = ch. 1-59). Always pick from the index list; do not build.
  - Index: `https://nebraskalegislature.gov/laws/laws.php`
  - Navigation: laws.php 'Books for Download' -> Reissue volume or Supplement PDF covering the chapter -> fetch_doc.py grep for '{chapter}-{section}.'
- **Automation:** WebFetch untested · shell ok · robots: /pdf/revisor/ not disallowed
  - Very large: 2016reissue_v2.pdf = 1,297 pages, 6.19M chars (Last-Modified Oct 3 2016). Use to quote the text as printed in the volume a citation names (e.g. 'Reissue 2016').
- **Currency:** laws.php publication-date table and file names — observed: "Volume 2 (chapters 24 through 28) 2016; Supplement 2025"
- **Official status:** PDFs of the printed Reissue volumes and Supplements, offered 'for purposes of downloading and printing' on /laws/laws.php; same site-wide disclaimer referring users to the printed official publication.
- **Hazard:** multi-thousand-page PDFs (fetch tool useless)
- **Hazard:** reissue text may be superseded by a later Supplement - check both
- **Probe:** Neb. Rev. Stat. § 25-207 (Reissue 2016) → `https://nebraskalegislature.gov/pdf/revisor/2016reissue_v2.pdf` — expect: "Actions for trespass, conversion, other torts, and frauds"
- **Evidence (2026-10-17):** fetch_doc.py info: pdf, 1,297 pages, 6,189,605 chars; text search for 25-207 not run (size).
- **Notes:** Bulk route for the whole code (all volumes + current Supplement).

### `ne-statutes-justia` — Justia - Nebraska Revised Statutes (2025)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** 2025 Nebraska Revised Statutes per section; prior years (2009-2024) under /codes/nebraska/{year}/.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/nebraska/chapter-{chapter}/statute-{chapter}-{section}/`
  - Placeholders: 25-207 -> chapter-25/statute-25-207/ ; 27-702 -> chapter-27/statute-27-702/. Note 'statute-' not 'section-' (chapter-25/section-25-207/ errored). Chapter page lists every section; year index /codes/nebraska/2025/ lists chapters without ranges.
  - Index: `https://law.justia.com/codes/nebraska/2025/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com answers robots.txt with a bot check (fetch_doc.py REFUSED)
  - Built section URLs were not gated for WebFetch.
- **Currency:** page heading — observed: "2025 Nebraska Revised Statutes"
- **Official status:** Page disclaimer: 'These codes may not be the most recent version.'
- **Hazard:** tier 2: disclose with '2025' edition string
- **Hazard:** may lag Supplement updates
- **Probe:** Neb. Rev. Stat. § 25-207 → `https://law.justia.com/codes/nebraska/chapter-25/statute-25-207/` — expect: "The following actions can only be brought within four years"
- **Evidence (2026-10-17):** WebFetch: YES, 'The following actions can only be brought within four years:'; '2025 Nebraska Revised Statutes'; complete. Second: statute-27-702 YES 'If scientific, technical, or other specialized knowledge will assist the'.

## B. Constitution

### `ne-constitution-leg` — Nebraska State Constitution (nebraskalegislature.gov, per section)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Nebraska Legislature · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Constitution of 1875 as amended: Preamble and every section, with source/amendment history.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://nebraskalegislature.gov/laws/articles.php?article={article}-{section}`
  - Placeholders: {article} = upper-case Roman numeral, {section} = section number with any upper-case letter suffix: art. I, § 3 -> I-3 ; art. V, § 2 -> V-2 ; art. VIII, § 1A -> VIII-1A. Preamble -> article=Preamble. Whole document: /laws/display-fullconst.php?print=false; certified PDF: /FloorDocs/Current/PDF/Constitution/constitution.pdf (91 pages, 235,777 chars).
  - Index: `https://nebraskalegislature.gov/laws/browse-constitution.php`
- **Automation:** WebFetch gated · shell ok · robots: /laws/ and /FloorDocs/ not disallowed
  - Not tried in WebFetch (same host as ne-statutes-leg, whose built URLs are gated). Section pages carry annotations after the text (I-3 page 60K chars).
- **Currency:** constitution.pdf cover page — observed: "Certified by Secretary of State's Office ... December 2, 2024"
- **Official status:** Same site disclaimer as the statutes (refer to the printed official publication). The PDF edition's cover says 'Certified by Secretary of State's Office' (see notes).
- **Hazard:** annotations follow the section text
- **Hazard:** lettered sections (VIII-1A) keep upper-case suffix
- **Probe:** Neb. Const. art. I, § 3 → `https://nebraskalegislature.gov/laws/articles.php?article=I-3` — expect: "No person shall be deprived of life, liberty, or property"
- **Evidence (2026-10-17):** fetch_doc.py: 60,660 chars; 'I-3. Due process of law; equal protection. No person shall be deprived'. Second: article=V-2 'The Supreme Court shall consist of seven judges'. Index lists VIII-1A, VIII-1B, VIII-2A.
- **Notes:** constitution.pdf Last-Modified Jun 4 2025; cover 'Certified by Secretary of State's Office and Distributed by Clerk of the Legislature's Office'.

### `ne-constitution-justia` — Justia - Nebraska Constitution

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Nebraska Constitution per section.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/nebraska/c01{article_num:02d}{section:03d}000.html`
  - Placeholders: {article_num} = Arabic number of the Roman article, two digits; {section} three digits: art. I § 3 -> c0101003000.html ; art. V § 2 -> c0105002000.html ; Preamble -> c0100000000.html. Lettered sections (VIII-1A) slug unknown: use the index /constitution/nebraska/.
  - Index: `https://law.justia.com/constitution/nebraska/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot check on robots.txt (fetch_doc.py)
- **Currency:** disclaimer only — observed: "This Constitution may not be the most recent version."
- **Official status:** Page note: 'This Constitution may not be the most recent version.'
- **Hazard:** tier 2
- **Hazard:** opaque numeric slugs; lettered sections unverified
- **Probe:** Neb. Const. art. I, § 3 → `https://law.justia.com/constitution/nebraska/c0101003000.html` — expect: "No person shall be deprived of life, liberty, or property"
- **Evidence (2026-10-17):** WebFetch: YES 'No person shall be deprived of life, liberty, or property,'. Second: c0105002000.html = Section V-2, 'The Supreme Court shall consist of seven judges, one of whom'.

## C. Court rules

### `ne-rules-judicial` — Nebraska Supreme Court Rules (nebraskajudicial.gov, per-rule pages)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Nebraska Supreme Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** All Neb. Ct. R. chapters 1-6: ch. 2 Appeals (Art. 1 Appellate Practice, §§ 2-101 ff.), ch. 3 Attorneys (Art. 5 Rules of Professional Conduct §§ 3-501.0 ff.; Art. 3 discipline), ch. 4 Children and Families, ch. 5 Judges (Code of Judicial Conduct), ch. 6 Trial Courts (Art. 11 Pleading in Civil Cases §§ 6-1101 ff.; Art. 3 discovery; uniform district/county court rules). Prior versions kept on separate pages. Evidence rules are statutes (Neb. Rev. Stat. ch. 27), not here.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format html
  - Index: `https://nebraskajudicial.gov/supreme-court-rules`
  - Navigation: index lists /supreme-court-rules/chapter-{n}-{slug} -> chapter page lists article pages -> article page lists one link per section (slug = '%C2%A7-' + section without hyphen-dots + heading words, e.g. %C2%A7-6-1112-defenses-and-objections-...; § 3-501.7 sits on a group page %C2%A7%C2%A7-3-5011-3-50118-client-lawyer-relationship). Faster: each article page links a 'Printer-Friendly Version' https://nebraskajudicial.gov/book/export/html/{node} with the whole article's text and amendment notes (Art. 11 Pleading = 9131; ch. 2 Art. 1 Appellate = 8671; ch. 3 Art. 5 Prof. Cond. = 8800). Article slugs may carry an edition suffix ('-effective-january-1-2025'); old article URLs redirect there.
- **Automation:** WebFetch ok · shell ok · robots: Drupal default: Disallow /core/ /profiles/ /admin/ /search/ /user/* etc.; /supreme-court-rules/ and /book/export/ not disallowed
  - fetch_doc.py 'links' crashes on these pages (a malformed href 'site:url-brief' raises ValueError in urljoin) - read hrefs another way or use grep on the book export. supremecourt.nebraska.gov and supremecourt.ne.gov redirect (301) to nebraskajudicial.gov. Book exports: Prof. Cond. 367,510 chars, Appellate 136,868 - beyond WebFetch's window; Art. 11 (64,852) read whole in WebFetch.
- **Currency:** amendment note after each section; article title may carry an edition ('Effective January 1, 2025') — observed: "§ 6-1115 amended September 3, 2025."
- **Official status:** Published by the Supreme Court on its own site with amendment history lines ('§ 6-1112 amended ...'); no official-status statement seen. Rule amendment orders: /rules/rule-amendments.
- **Hazard:** per-rule URLs contain heading-word slugs: not constructible
- **Hazard:** current and 'Prior Version' articles coexist - check the article title's effective date
- **Hazard:** large book exports truncate in WebFetch (Prof. Cond. 367K chars)
- **Hazard:** fetch_doc.py links crashes on these pages
- **Probe:** Neb. Ct. R. Pldg. § 6-1112(b)(6) → `https://nebraskajudicial.gov/supreme-court-rules/chapter-6-trial-courts/article-11-nebraska-court-rules-pleading-civil-cases-effective-january-1-2025/%C2%A7-6-1112-defenses-and-objections-when-and-how-presented-pleading-or-motion-motion-judgment-pleadings` — expect: "(6) failure to state a claim upon which relief can be granted"
- **Evidence (2026-10-17):** fetch_doc.py: 30,609 chars; '(6) failure to state a claim upon which relief can be granted'. § 2-109 page: '(A) Time for Filing.'; § 3-501.7 in export 8800: '(a) Except as provided in paragraphs (b) and (c)'. WebFetch export 9131: YES, complete through § 6-1116.
- **Notes:** Revisor's note on Art. 11: former rule 12 is now Neb. Ct. R. Pldg. § 6-1112 - the last two digits match the federal rule number.

## D. Administrative code

### `ne-admincode-rules` — Nebraska Administrative Code - rules.nebraska.gov (Secretary of State Rules and Regulations)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Nebraska Secretary of State · text: **link-only** · official: unknown
- **Coverage:** Nebraska Administrative Code by agency -> title -> chapter (chapter documents), rulemaking docket.
- **Access:** `link-only` · format html
  - Index: `https://rules.nebraska.gov/browse-rules`
  - Navigation: React app: /browse-rules?agencyId=... ; content loads from /api/agency/filtered, /api/title/GetByAgencyId/{id}, /api/chapter/GetByTitleId/{id}, /api/ChapterImage/GetByChapterId/{id} (found in the public JS bundle). The API answered HTTP 401 to fetch_doc.py: not usable. Legacy URLs (www.nebraska.gov/rules-and-regs/regsearch/..., nebraska.gov/nesos/rules-and-regs/regtrack/...) redirect to this app.
- **Automation:** WebFetch gated · shell unreadable-format · robots: User-agent: * Disallow: (empty - allows all)
  - fetch_doc.py gets an empty JavaScript shell (0 chars) for /, /browse-rules and /about; /api/agency/filtered REFUSED HTTP 401 (not retried). WebFetch on /browse-rules: PROVENANCE_REQUIRED.
- **Currency:** n/a (not readable) — observed: "n/a"
- **Official status:** Linked from sos.nebraska.gov as the Rules and Regulations site; content not readable, no statement seen.
- **Hazard:** JavaScript-only app
- **Hazard:** API refuses (401)
- **Hazard:** agency PDFs on agency sites (e.g. dhhs.ne.gov) not probed
- **Probe:** 53 Neb. Admin. Code ch. 2, § 002 → `https://rules.nebraska.gov/browse-rules` — expect: "Title 53"
- **Evidence (2026-10-17):** fetch_doc.py: html 0 chars (JS shell); API /api/agency/filtered HTTP 401; WebFetch gated.
- **Notes:** Use ne-admincode-lii for text; link users here.

### `ne-admincode-lii` — Cornell LII - Nebraska Administrative Code

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-section pages by agency -> title -> chapter, including repealed-section stubs.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/nebraska/{title}-Neb-Admin-Code-ch-{chapter}-SS-{section}`
  - Placeholders: {section} keeps its three-digit zero padding: 53 NAC 2-002 -> 53-Neb-Admin-Code-ch-2-SS-002 ; 471 NAC 23-007 -> 471-Neb-Admin-Code-ch-23-SS-007. Subsections (002.01) are inside the section page. A malformed URL (53-Neb-Admin-Code-SS-2-001) returns HTTP 200 with the Nebraska index page, so confirm the heading '{title} Neb. Admin. Code, ch. {chapter}, § {section}' appears. Chapter index: /regulations/nebraska/{agency-slug}/title-{title}/chapter-{chapter}.
  - Index: `https://www.law.cornell.edu/regulations/nebraska`
- **Automation:** WebFetch untested · shell ok · robots: permits; crawl-delay 10 (fetch_doc.py check)
  - Last-Modified headers Aug 3 2025.
- **Currency:** none on page; HTTP Last-Modified only — observed: "Last-Modified: Sun, 03 Aug 2025"
- **Official status:** Third-party compilation; page says state regulations are updated quarterly.
- **Hazard:** tier 2; possibly stale (Aug 2025)
- **Hazard:** bad slugs return the index page with HTTP 200
- **Hazard:** repealed sections still have pages
- **Probe:** 53 Neb. Admin. Code ch. 2, § 002 → `https://www.law.cornell.edu/regulations/nebraska/53-Neb-Admin-Code-ch-2-SS-002` — expect: "Any person may petition an agency requesting the promulgation, amendment, or repeal"
- **Evidence (2026-10-17):** fetch_doc.py: 3,194 chars; '53 Neb. Admin. Code, ch. 2, § 002 - Rule Making Petition ... 002.01 Petition Any person may petition'. Second: 471-...-ch-23-SS-007 '[REPEALED] ... Repealed effective 12/26/2021'.

## E. Case law

### `ne-opinions-judicial` — Nebraska Judicial Branch opinion pages (last ~90 days) and Court of Appeals memorandum web opinions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Nebraska Supreme Court / Court of Appeals · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court and Court of Appeals releases of the last ~90 days, grouped by release date with docket, 'Cite As', title; Court of Appeals memorandum (unpublished) web opinions as PDFs on nebraskajudicial.gov; weekly 'NonWeblist' PDFs naming memorandum opinions not posted (viewable only via subscription SCCALES).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Index: `https://nebraskajudicial.gov/courts/court-appeals/opinions`
  - Navigation: Supreme Court: /courts/supreme-court/opinions; Court of Appeals: /courts/court-appeals/opinions -> release date -> row (docket, cite, title) -> published: www.nebraska.gov/apps-courts-epub/public/viewOpinion?docId=...; memorandum: /sites/default/files/memorandums/a{yy}-{nnn}m.pdf (a25-855m.pdf; consolidated cases may use 'mm', e.g. a25-928mm.pdf) - take the link from the page, do not build.
- **Automation:** WebFetch ok · shell ok · robots: Drupal default (see ne-rules-judicial); /courts/ and /sites/default/files/ not disallowed
  - WebFetch read the Supreme Court listing but mis-associated rows (paired S-25-084 with other cases' titles): take docket/title/link pairs from fetch_doc.py output or the raw HTML, not WebFetch summaries.
- **Currency:** release-date headings — observed: "October 16, 2026 (Supreme Court); October 13, 2026 (Court of Appeals)"
- **Official status:** Release listings; published opinions link to the Online Library PDFs. Memorandum opinions are headed 'NOT DESIGNATED FOR PERMANENT PUBLICATION' (citable only per Neb. Ct. R. App. P. § 2-102(E)).
- **Hazard:** listing holds only ~90 days
- **Hazard:** WebFetch scrambles the listing table
- **Hazard:** memorandum opinions not selected for posting are not free online (subscription SCCALES)
- **Probe:** State v. Spencer, No. A-25-855 (Neb. App. Oct. 13, 2026) (memorandum web opinion) → `https://nebraskajudicial.gov/sites/default/files/memorandums/a25-855m.pdf` — expect: "MEMORANDUM OPINION AND JUDGMENT ON APPEAL (Memorandum Web Opinion) STATE V. SPENCER"
- **Evidence (2026-10-17):** fetch_doc.py: pdf 4 pages, 11,903 chars; 'MEMORANDUM OPINION AND JUDGMENT ON APPEAL (Memorandum Web Opinion)', 'Filed October 13, 2026. No. A-25-855.'
- **Notes:** Older memorandum web opinions: whether they stay at /sites/default/files/memorandums/ after the 90-day window was not tested.

### `ne-opinions-library` — Nebraska Appellate Courts Online Library (advance-sheet opinions, bound volumes, minutes lists)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Nebraska Supreme Court Reporter of Decisions (hosted by Nebraska.gov) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court published opinions in advance-sheet form (Neb. Reports vol. 275 ff. as advance sheets; current vol. 322) and scanned bound volumes Neb. Reports vol. 1 (1871) - 274 (2012); Court of Appeals published opinions (Neb. App. advance sheets, current vol. 34) and bound Neb. App. vol. 1 (1994) - 15 (2011); per-volume Memo / DWO / PFR minutes lists. Released Fridays 8 a.m. (Supreme Court) and Tuesdays 8 a.m. (Court of Appeals).
- **Read via (in order):** **script**
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.nebraska.gov/apps-courts-epub/public/search?searchText={query}`
  - Placeholders: {query} = docket number (S-25-209, A-25-197) or citation ('321 Neb. 841', URL-encoded). The site's JavaScript POSTs this form, but a plain GET works and returns an HTML table: volume, caption, filed date, docket, 'NNN Neb. NNN' cite, link /viewAdvanced?docId=N000NNNNPUB (same PDF as /viewOpinion?docId=). Full-text search also matches older volumes that mention the term. Listings: /supreme and /appeals (25 per page, ?offset=&max=).
  - Index: `https://www.nebraska.gov/apps-courts-epub/public/supreme`
- **Automation:** WebFetch gated · shell ok · robots: www.nebraska.gov: Disallow /demo/billtrack/ and /app-fsp/ only; Allow /
  - viewOpinion PDFs (links from nebraskajudicial.gov pages) hit the WebFetch provenance gate twice; fetch_doc.py reads them in full. Long opinions exceed WebFetch's window anyway (S-25-209: 102,805 chars). PDFs carry a library header (download timestamp) on page 1.
- **Currency:** Supreme Court listing: minutes-list 'Date' column — observed: "322 Neb. 08/14/2026 - ; Memo/DWO/PFR updated 10/16/2026"
- **Official status:** Library page: the printed bound volumes contain the final, official opinions; scanned volumes online are unofficial copies. Advance-sheet PDFs carry official Neb./Neb. App. pagination ('Cite as 321 Neb. 841').
- **Hazard:** docId is opaque: locate via GET search or listing
- **Hazard:** advance-sheet N.W.3d cite blank ('___ N.W.3d ___') until published
- **Hazard:** full-text search returns unrelated older volumes mentioning the term
- **Hazard:** scanned bound volumes are OCR of whole volumes, split in two parts
- **Probe:** State v. Evans, 321 Neb. 841 (2026) (No. S-25-209) → `https://www.nebraska.gov/apps-courts-epub/public/viewOpinion?docId=N00013369PUB` — expect: "Nebraska Supreme Court Advance Sheets 321 Nebraska Reports STATE v. EVANS Cite as 321 Neb. 841"
- **Evidence (2026-10-17):** fetch_doc.py: pdf 45 pages, 102,805 chars; 'Cite as 321 Neb. 841', 'Filed July 24, 2026. No. S-25-209.' GET search S-25-209 and '321 Neb. 841' both list it. CoA: N00013358PUB 'Cite as 34 Neb. App. 384', No. A-25-413.
- **Notes:** Official page numbers appear as '- 841 -' markers at the top of each page: pin cites can be taken from the advance sheet.

### `ne-cases-justia` — Justia - Nebraska Supreme Court and Court of Appeals opinions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Year listings for Supreme Court and Court of Appeals; modern pages reproduce official advance-sheet pagination.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/nebraska/{court}/{year}/{docket_lower}.html`
  - Placeholders: {court} = supreme-court | court-of-appeals; {docket_lower} = s-25-209, a-25-197; {year} = decision year. Year listing https://law.justia.com/cases/nebraska/{court}/{year}/ to confirm. Whether memorandum opinions are included was not tested.
  - Index: `https://law.justia.com/cases/nebraska/supreme-court/2026/`
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: bot check on robots.txt (fetch_doc.py)
  - S-25-209 page 110,604 chars: WebFetch cut at 100,000 (continue with offset).
- **Currency:** listing heading — observed: "Nebraska Supreme Court Decisions 2026"
- **Official status:** Third-party copy of the advance-sheet opinions (keeps 'Cite as' headers and '- NNN -' page markers).
- **Hazard:** tier 2
- **Hazard:** long opinions truncated in WebFetch
- **Hazard:** decision year needed in URL
- **Hazard:** listing showed newest entry Sept. 25, 2026 - may lag the court by weeks
- **Probe:** State v. Evans, 321 Neb. 841 (2026) → `https://law.justia.com/cases/nebraska/supreme-court/2026/s-25-209.html` — expect: "Raymond Evans was convicted by a jury of first degree"
- **Evidence (2026-10-17):** WebFetch: YES; 'Raymond Evans was convicted by a jury of first degree'; 'Cite as 321 Neb. 841'; '- 841 -' markers; truncated at 100K. Second: court-of-appeals/2026/a-25-197.html 'Cite as 34 Neb. App. 347', complete.

## F. Subsequent history

### `ne-pfr-lists` — Petitions for Further Review lists (Online Library, per volume) and daily minutes

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Nebraska Supreme Court · text: **fetch-and-quote** · official: official
- **Coverage:** For each Neb. Reports volume: a PFR list naming every Court of Appeals case (by A- docket, with Neb. App. cite when published) and the date further review was denied or granted; Memo (disposed by memorandum) and DWO (without opinion) lists. Daily minutes of both courts kept 60 days on nebraskajudicial.gov.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.nebraska.gov/apps-courts-epub/public/supreme`
  - Navigation: Library /supreme -> volume row whose Opening-Closing dates cover the likely ruling date (petitions are decided ~1-3 months after the Court of Appeals decision) -> 'PFR' link (/viewPFR?docId=...) -> grep the PDF for the A- docket. The GET search does NOT index PFR lists (A-25-197 search found only the opinion). Recent rulings: https://nebraskajudicial.gov/courts/appellate-courts-offices/daily-minutes ('Minutes for MM.DD.YYYY' PDFs, 60 days).
- **Automation:** WebFetch gated · shell ok · robots: as ne-opinions-library
  - Not tried in WebFetch (same gated viewer). PFR list for vol. 322: 2 pages, 3,808 chars.
- **Currency:** Library 'Date - Date Minutes List was last updated' — observed: "PFR 10/16/2026"
- **Official status:** Court's own lists, printed in the Nebraska Supreme Court Advance Sheets front matter ('PETITIONS FOR FURTHER REVIEW').
- **Hazard:** per-volume lists only: pick the volume by date
- **Hazard:** not searchable by docket through the library search
- **Probe:** Martinez v. Amerigreen, 34 Neb. App. 347 (2026), further review denied → `https://www.nebraska.gov/apps-courts-epub/public/viewPFR?docId=N00013533PUB` — expect: "Petition of appellant for further review denied on October 9, 2026."
- **Evidence (2026-10-17):** fetch_doc.py: pdf 2 pages; '*No. A-25-197: Martinez v. Amerigreen, 34 Neb. App. 347 (2026). Petition of appellant for further review denied on October 9, 2026.'
- **Notes:** U.S. Supreme Court certiorari dispositions are not recorded here.

## Not available (do not look for these again)

- **admin_register** — Nebraska administrative register: Nebraska publishes no register; proposed rules and hearing notices live in the rules.nebraska.gov docket (/docket, same unreadable React app; legacy regtrack URLs redirect there). (2026-10-17)
- **case_law** — Public-domain (vendor-neutral) citation format: Opinions cite as 'NNN Neb. NNN' / 'NN Neb. App. NNN' with N.W.2d/N.W.3d parallel; no medium-neutral form on the advance sheets. (2026-10-17)
- **case_law** — Free text of Court of Appeals memorandum opinions not selected for web posting: NonWeblist10-13-26.pdf: such opinions 'can be viewed online through the appellate court case search available by subscription' (SCCALES). (2026-10-17)
- **statutes** — Structured bulk statute data (XML/JSON/API): laws.php offers only PDF Reissue volumes and Supplements for download; no XML/JSON seen. (2026-10-17)

## Corpus candidates (maintainers)

- `ne-rules-judicial` — Rules of Professional Conduct whole-article export, 367,510 chars - beyond WebFetch's window
- `ne-rules-judicial` — Appellate Practice rules (ch. 2 art. 1) export, 136,868 chars
- `ne-constitution-leg` — Certified PDF (91 pages, 235,777 chars); per-section HTML exists, so low priority
- `ne-statutes-pdf-volumes` — Reissue volume (ch. 24-28, 1,297 pages, 6.19M chars); with the 2025 Supplement PDFs this is the whole printed code · bulk: https://nebraskalegislature.gov/laws/laws.php (all Reissue volumes + Supplements as PDF)
- `ne-opinions-library` — Long opinions exceed WebFetch's window (45 pages, 102,805 chars)

## Open questions

- rules.nebraska.gov (Nebraska Administrative Code) is JavaScript-only and its API answers 401: find an official readable route (agency-hosted chapter PDFs, e.g. dhhs.ne.gov) or confirm none exists.
- ne-statutes-pdf-volumes: text search inside a Reissue PDF not run (size); confirm section lines extract cleanly.
- Whether Court of Appeals memorandum web opinions stay at /sites/default/files/memorandums/ after the 90-day listing window.
- Justia: whether memorandum (unpublished) Court of Appeals opinions are included; pre-2000 case slugs; lettered constitution sections (VIII-1A).
- Session laws (Laws of Nebraska) and slip laws on nebraskalegislature.gov not probed.
- Free tier-2 court-rule copies (Justia/LII) not checked.
