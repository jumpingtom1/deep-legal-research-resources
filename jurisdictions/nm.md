# New Mexico (NM) — free legal sources

_Generated from `data/nm.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes, constitution, court rules and official opinions are all on NMOneSource (New Mexico Compilation Commission, official publisher; Lexum platform): listings are iframe shells (add ?iframe=true), every chapter / rule set / constitution is one long PDF at {id}/1/document.do, and a plain GET search by official citation (ref=2019-NMSC-021) finds opinions. fetch_doc.py reads those PDFs, but nmonesource.com intermittently answers HTTP 403 and WebFetch on built URLs is gated, so Justia (per-section statutes and constitution, docket-slug cases) is the practical WebFetch second source. NMAC is constructible on srca.nm.gov (official), the NM Register is per-issue PDFs, Court of Appeals slip opinions are on coa.nmcourts.gov, and cert status appears in the header of published NMCA opinions.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of New Mexico | `nm (unverified)` | N.M. | N.M., P.3d, P.2d, P. | YYYY-NMSC-NNN (e.g. 2019-NMSC-021, ¶ 5) |
| Court of Appeals of New Mexico | `nmctapp (unverified)` | N.M. Ct. App. | N.M., P.3d, P.2d | YYYY-NMCA-NNN (e.g. 2018-NMCA-064, ¶ 1) |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| New Mexico Statutes Annotated 1978 | `NMSA 1978, § 37-1-8`; `NMSA 1978, §§ 57-12-1 to -26`; `N.M. Stat. Ann. § 41-4-4`; `Section 37-1-8 NMSA 1978`; `37-1-8 NMSA 1978`; `N.M.S.A. 1978, § 22-10A-3`; `section 41-4-4 of the NMSA`; `section 30-16-1 of the New Mexico Statutes Annotated` | `nm-nmsa-nmonesource` → `nm-nmsa-justia` → `nm-nmsa-unanno-nmonesource` |
| New Mexico session laws (Laws YYYY, ch. N) *(only once this jurisdiction is known)* | `Laws 2019, ch. 202, § 1`; `Laws 1880, ch. 5, § 1` | `nm-session-laws-nmonesource` |
| New Mexico Constitution | `N.M. Const. art. II, § 10`; `N.M. Const. art. II, § 18`; `Article II, Section 18 of the New Mexico Constitution`; `Article II, § 14 of the New Mexico Constitution` | `nm-constitution-nmonesource` → `nm-constitution-justia` |
| New Mexico Rules Annotated (Rule N-NNN NMRA, UJI) | `Rule 1-012(B)(6) NMRA`; `Rule 11-702 NMRA`; `Rule 12-502 NMRA`; `UJI 14-5050 NMRA`; `Rule 16-107 NMRA`; `NMRA, Rule 1-056`; `SCRA 1986, 1-012` | `nm-rules-unanno-nmonesource` → `nm-rules-annotated-nmonesource` → `nm-rules-supremecourt` |
| Bare New Mexico rule number (Rule N-NNN) *(only once this jurisdiction is known)* | `Rule 1-012(B)(6)`; `Rule 5-805` | `nm-rules-unanno-nmonesource` → `nm-rules-annotated-nmonesource` |
| New Mexico Administrative Code | `16.10.8.9 NMAC`; `1.24.1.7 NMAC`; `16.10.8 NMAC`; `N.M. Admin. Code § 21.16.9.1`; `N.M. Code R. § 16.10.8.8` | `nm-nmac-srca` → `nm-nmac-lii` |
| New Mexico Register | `New Mexico Register, Volume XXXVII, Issue 19`; `N.M. Reg. Vol. XXXVII, No. 19`; `37 N.M. Reg. 1234` | `nm-register-srca` |
| Public-domain citations (YYYY-NMSC / NMCA / NMCERT-NNN) | `2019-NMSC-021, ¶ 5`; `2018-NMCA-064`; `2020-NMCA-034, ¶ 12`; `1990-NMSC-063, ¶ 22, 110 N.M. 206`; `2009-NMCERT-008` | `nm-opinions-nmonesource` → `nm-cases-justia` |
| New Mexico Reports and Pacific Reporter with (N.M.) parenthetical | `110 N.M. 206`; `794 P.2d 349 (N.M. 1990)`; `429 P.3d 338 (N.M. Ct. App. 2018)` | `nm-opinions-nmonesource` → `nm-cases-justia` |
| New Mexico appellate docket numbers (S-1-SC / A-1-CA), incl. memorandum opinions | `No. S-1-SC-37201`; `No. A-1-CA-41857`; `State v. Soto, No. A-1-CA-42452, mem. op. (N.M. Ct. App. Jan. 26, 2026) (nonprecedential)` | `nm-opinions-nmonesource` → `nm-opinions-coa-nmcourts` → `nm-cases-justia` |
| Pre-2010 comma docket numbers (No. 27,270) *(only once this jurisdiction is known)* | `No. 27,270` | `nm-opinions-nmonesource` → `nm-cases-justia` |

Regexes (case-insensitive):

- New Mexico Statutes Annotated 1978: `(?:NMSA(?:\s*1978)?,?\s*|N\.\s*M\.\s*S\.\s*A\.(?:\s*1978)?,?\s*|N\.\s*M\.\s*Stat\.\s*Ann\.\s*)(?:§+|[Ss]ec(?:tion|\.)s?)\s*(?P<chapter>\d{1,2}[A-Z]?)-(?P<article>\d{1,3}[A-Z]?)-(?P<section>\d{1,4}(?:\.\d+)?)|(?:(?:[Ss]ection|§+)\s*)?(?P<chapter2>\d{1,2}[A-Z]?)-(?P<article2>\d{1,3}[A-Z]?)-(?P<section2>\d{1,4}(?:\.\d+)?)(?:\([A-Za-z0-9]+\))*,?\s+(?:of\s+the\s+)?(?:NMSA|N\.M\.S\.A\.|New\s+Mexico\s+Statutes\s+Annotated)`
- New Mexico session laws (Laws YYYY, ch. N): `Laws\s+(?P<year>(?:18|19|20)\d\d),?\s*\(?(?:\d+(?:st|nd|rd|th)\s+S\.S\.\)?,?\s*)?ch\.\s*(?P<chapter>\d+)`
- New Mexico Constitution: `N\.\s*M\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*§+\s*(?P<section>\d+[A-Za-z]?)|Article\s+(?P<article2>[IVXL]+),?\s+(?:Section|§)\s*(?P<section2>\d+[A-Za-z]?)\s+of\s+the\s+(?:New\s+Mexico|N\.\s*M\.)\s+Constitution`
- New Mexico Rules Annotated (Rule N-NNN NMRA, UJI): `(?:(?:Rule|UJI)\s+)?(?P<set>\d{1,2}[A-Z]?)-(?P<rule>\d{3,4}(?:\.\d+)?)(?:\s*\([A-Za-z0-9]+\))*,?\s+(?:NMRA|SCRA)|(?:NMRA|SCRA\s+1986),?\s+(?:Rule\s+)?(?P<set2>\d{1,2}[A-Z]?)-(?P<rule2>\d{3,4}(?:\.\d+)?)`
- Bare New Mexico rule number (Rule N-NNN): `Rule\s+(?P<set>\d{1,2}[A-Z]?)-(?P<rule>\d{3})(?!\d)`
- New Mexico Administrative Code: `(?P<title>\d{1,2})\.(?P<chapter>\d{1,3})\.(?P<part>\d{1,4})(?:\.(?P<section>\d{1,4}))?\s+NMAC|N\.\s*M\.\s*(?:Admin\.\s*Code|Code\s+R\.)\s*(?:r\.|§+)?\s*(?P<title2>\d{1,2})\.(?P<chapter2>\d{1,3})\.(?P<part2>\d{1,4})(?:\.(?P<section2>\d{1,4}))?`
- New Mexico Register: `(?:New\s+Mexico|N\.\s*M\.)\s+Reg(?:ister|\.)\s*,?\s*Vol(?:ume|\.)\s*(?P<volume>[IVXL]+),?\s*(?:Issue|No\.)\s*(?P<issue>\d+)|(?P<volume2>\d{1,2})\s+N\.\s*M\.\s*Reg\.\s+(?P<page>\d+)`
- Public-domain citations (YYYY-NMSC / NMCA / NMCERT-NNN): `(?P<year>(?:19|20)\d\d)-NM(?P<court>SC|CA|CERT)-(?P<number>\d{1,3})(?:,\s*¶+\s*(?P<para>\d+))?`
- New Mexico Reports and Pacific Reporter with (N.M.) parenthetical: `(?P<volume>\d{1,3})\s+N\.\s*M\.\s+(?P<page>\d{1,4})(?!\d)|(?P<pvolume>\d{1,4})\s+P\.(?:\s*(?P<series>[23])d)?\s+(?P<ppage>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>N\.\s*M\.(?:\s*Ct\.\s*App\.)?)\s*(?P<year>\d{4})\)`
- New Mexico appellate docket numbers (S-1-SC / A-1-CA), incl. memorandum opinions: `(?:No\.\s*)?(?P<docket>[AS]-1-(?:CA|SC)-\d{4,6})`
- Pre-2010 comma docket numbers (No. 27,270): `No\.\s*(?P<number>\d{1,2},\d{3})`

Short forms → URL key:

NMSA → `nmsa`; NMSA 1978 → `nmsa`; N.M.S.A. → `nmsa`; N.M. Stat. Ann. → `nmsa`; NM Stat → `nmsa`; NMRA → `nmra`; SCRA → `nmra`; SCRA 1986 → `nmra`; UJI → `nmra`; NMAC → `nmac`; N.M. Admin. Code → `nmac`; N.M. Code R. → `nmac`

Rule 23-112 NMRA (and its Appendix) governs citation form. Public-domain opinion citations YYYY-NMSC-NNN / YYYY-NMCA-NNN with ¶ pinpoints apply from 1996 (memory; NMOneSource 2019-NMSC-021 and 1990-NMSC-063 cites seen); the PDF text marks paragraphs as {1}. NMSA statute numbers are chapter-article-section ('37-1-8'); ranges are written '§§ 57-12-1 to -26' - take the first section; the regex never reads 'to -26' as a section. A bare 'N-N-N' or 'Section 37-1-8' without NMSA/N.M. is NOT routed here (Colorado C.R.S., Wyoming and others use the same shape). Bare 'Rule 1-012' / 'Rule 5-805' and 'Laws YYYY, ch. N' are generic (context_required). Older rule cites 'SCRA 1986, 1-012' map to the same NMRA rule numbers. Docket forms: Supreme Court S-1-SC-NNNNN, Court of Appeals A-1-CA-NNNNN (since c. 2010; earlier 'No. 27,270' comma form). Memorandum opinions are cited by docket with 'mem. op.' and are nonprecedential (Rule 12-405 NMRA). law_aliases values are collection keys on nmonesource.com (nmsa, nmra) and the NMAC key; URL building for NMSA/NMRA still needs the chapter/rule-set redirect. CourtListener ids nm / nmctapp from memory. Justia case URLs: see nm-cases-justia (filing year, old comma-docket slugs).

## A. Statutes / code

### `nm-nmsa-nmonesource` — NMSA 1978, annotated (NMOneSource, current NMSA collection)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · New Mexico Compilation Commission (NMOneSource, Lexum Norma platform) · text: **fetch-and-quote** · official: official
- **Coverage:** All NMSA 1978 chapters (1-77 incl. 22A, 24A, 32A, 42A, 46A, 46B, 59A), one annotated PDF per chapter; historical archives from 1989 in a separate collection (nmsa-historical).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://laws.nmonesource.com/w/nmos/Chapter-{chapter}-NMSA-1978  (redirects to https://nmonesource.com/nmos/nmsa/en/item/{id}/index.do; text at https://nmonesource.com/nmos/nmsa/en/{id}/1/document.do)`
  - Placeholders: chapter = the first hyphen group of the section number (37-1-8 -> 37; 22A-... -> 22A). The laws.nmonesource.com friendly URL is constructible and 302-redirects to the item page; take {id} from the redirect (Chapter-37 -> 4366, Chapter-41 -> 4382) and read https://nmonesource.com/nmos/nmsa/en/{id}/1/document.do (a PDF of the whole chapter). Inside the PDF, sections begin with the bare number and a period: '37-1-8. ' (search with flexible whitespace: regex '37-1-8\.\s+\S'); cross-references also contain the number, so match the heading form. Item ids are not derivable from chapter numbers. Further verified id: Chapter-30 -> 4371 (ch. 30 PDF 1,139 pp, 2.98M chars).
  - Index: `https://nmonesource.com/nmos/nmsa/en/nav_date.do?iframe=true`
  - Navigation: Listing (iframe=true variant; the plain nav_date.do is an empty shell that loads it in an iframe) shows 'Chapter N - Title' rows, 4 pages (?page=2&iframe=true …), each with item/{id}/index.do and {id}/1/document.do links. No section ranges are shown; the chapter number is enough because each chapter is one document. Shortcut: laws.nmonesource.com/w/nmos/Chapter-{N}-NMSA-1978 redirect.
- **Automation:** WebFetch gated · shell ok · robots: nmonesource.com: User-agent * disallows only two /icm/ items; BUbiNG fully disallowed. laws.nmonesource.com: robots permits.
  - Intermittent HTTP 403 from nmonesource.com to the script: about half of requests on 2026-10-17 were refused (listing iframes, document.do PDFs, search URLs) while identical URL shapes succeeded seconds earlier; fetch_doc.py then marks that exact URL refused for the day. Never retry a refused URL; use the tier-2 row or another day. WebFetch on built nmonesource.com / laws.nmonesource.com URLs hit PROVENANCE_REQUIRED (permission prompt unanswered) - gated. A document.do PDF that came from a search result (nmsl/en/18777/1/document.do) was read by WebFetch, so WebFetch can read these PDFs when the URL is approved. Chapter PDFs are long (ch. 37: 160 pp / 430,719 chars; ch. 41: 322 pp / 874,366 chars) - WebFetch's ~100K window cannot reach most sections; use fetch_doc.py grep/section.
- **Currency:** nmcompcomm.us Scope of Coverage page; PDF filename carries edition date — observed: "current through the Second Session of the Fifty-Seventh Legislature (2026)"
- **Official status:** The Compilation Commission is the State's official legal publisher (supremecourt.nmcourts.gov/rules-forms-files/opinions/ calls it 'the official legal publisher for the Supreme Court'); NMSA 1978 is the official compilation it publishes. No per-page authentication statement on the chapter PDFs (opinion PDFs carry a digital attestation).
- **Hazard:** nav_date.do without ?iframe=true is an empty shell (text in iframe)
- **Hazard:** item ids not derivable; resolve via laws.nmonesource.com redirect or listing
- **Hazard:** one PDF per chapter, 400K-900K chars: WebFetch truncation
- **Hazard:** annotations interleaved; cross-references repeat section numbers - match the 'N-N-N. ' heading
- **Hazard:** WebFetch gated on built URLs
- **Hazard:** sporadic HTTP 403; a refused URL is off for the day in fetch_doc — fall back to the fetch tool on a search-surfaced URL or to Justia; never retry by another route
- **Hazard:** PDF filename date is a per-chapter edition date (ch. 30 '10-13-26_…', ch. 37 '8-11-26_…'), not a whole-code currency date
- **Hazard:** the probe URL itself (4366) was refused HTTP 403 at the independent check; the route was proven on ch. 30
- **Probe:** NMSA 1978, § 37-1-8 → `https://nmonesource.com/nmos/nmsa/en/4366/1/document.do` — expect: "Actions must be brought against sureties on official bonds and"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 160 pp, 430,719 chars, filename '8-11-26_chapter-37-limitation-of-actions-abatement-and-revivor-2026.pdf'; '37-1-8. Actions against sureties on fiduciary bonds; injuries to person or reputation.' at offset 137,932 (p. 51). Second: ch. 41 (id 4382, 322 pp) '41-4-4. Granting immunity from tort liability' at p. 106. | Independent check 2026-10-17: probe 4366 script REFUSED HTTP 403, WebFetch PROVENANCE_REQUIRED; route proven on ch. 30 ('30-16-1. Larceny.' p. 510); second citation NMSA 1978, § 30-16-1 ok
- **Notes:** Unannotated chapters (collection nmsa-unanno, ids 18502-18580 per the Scope page) are much shorter; their document.do returned 403 to the script on test (2026-10-17), so recorded as nm-nmsa-unanno-nmonesource (reported).

### `nm-nmsa-unanno-nmonesource` — NMSA 1978, unannotated (NMOneSource)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · New Mexico Compilation Commission · text: **fetch-and-quote** · official: official
- **Coverage:** All chapters, statute text and history only, one PDF per chapter.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://nmonesource.com/nmos/nmsa-unanno/en/{id}/1/document.do`
  - Placeholders: ids from the Scope of Coverage page or listing (ch. 1-4: 18502-18505; ch. 5: 18447; ch. 6-24: 18506-18524; ch. 33-42: 18533-18542, so ch. 37 = 18537; ch. 60-77: 18563-18580). Not derivable by arithmetic across the letter-suffixed chapters.
  - Index: `https://nmonesource.com/nmos/nmsa-unanno/en/nav_date.do?iframe=true`
  - Navigation: listing (iframe) -> 'Chapter N - Title' -> {id}/1/document.do
- **Automation:** WebFetch gated · shell ok · robots: nmonesource.com: User-agent * disallows only two /icm/ items; BUbiNG fully disallowed. laws.nmonesource.com: robots permits.
  - Listing page 1 read by script; page 2 listing and ch. 37 document (18537) returned HTTP 403 on 2026-10-17. Intermittent HTTP 403 from nmonesource.com to the script: about half of requests on 2026-10-17 were refused (listing iframes, document.do PDFs, search URLs) while identical URL shapes succeeded seconds earlier; fetch_doc.py then marks that exact URL refused for the day. Never retry a refused URL; use the tier-2 row or another day.
- **Currency:** Scope of Coverage page — observed: "current through the Second Session of the Fifty-Seventh Legislature (2026)"
- **Official status:** Same publisher as nm-nmsa-nmonesource.
- **Hazard:** WebFetch gated
- **Hazard:** sporadic HTTP 403; a refused URL is off for the day in fetch_doc — fall back to the fetch tool on a search-surfaced URL or to Justia; never retry by another route
- **Probe:** NMSA 1978, § 37-1-8 → `https://nmonesource.com/nmos/nmsa-unanno/en/18537/1/document.do`
- **Evidence (2026-10-17):** Listing (iframe) returned chapter rows with ids; document 18537 refused HTTP 403 to the script. | Independent check 2026-10-17: listing served (ch. 3 -> 18504, matches); doc 18504 REFUSED 403; no unannotated chapter text read by any route.

### `nm-session-laws-nmonesource` — Session Laws of New Mexico (NMOneSource)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · New Mexico Compilation Commission · text: **link-only** · official: unknown
- **Coverage:** Laws 2026 (Second Session, 57th Legislature); historical archives from 1993.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: item ids not derivable.
  - Index: `https://nmonesource.com/nmos/nmsl/en/nav_date.do?iframe=true`
  - Navigation: listing (iframe) -> session -> document.do
- **Automation:** WebFetch ok · shell untested · robots: nmonesource.com: User-agent * disallows only two /icm/ items; BUbiNG fully disallowed. laws.nmonesource.com: robots permits.
  - WebFetch read https://nmonesource.com/nmos/nmsl/en/18777/1/document.do (a 2023 'Newly Enacted NMSA 1978 Section Numbers' table, from a search result).
- **Currency:** Scope of Coverage page — observed: "Second Session, Fifty-Seventh Legislature - Laws 2026"
- **Official status:** Listed on the Scope of Coverage page; no statement seen on a document.
- **Hazard:** not probed on a session-law chapter
- **Hazard:** sporadic HTTP 403; a refused URL is off for the day in fetch_doc — fall back to the fetch tool on a search-surfaced URL or to Justia; never retry by another route
- **Probe:** Laws 2023 (section-number table) → `https://nmonesource.com/nmos/nmsl/en/18777/1/document.do`
- **Evidence (2026-10-17):** Only a finding-aid table in the collection was fetched (WebFetch); no session-law chapter text probed. | Independent check 2026-10-17: same finding-aid table only; no session-law chapter text shown.
- **Notes:** The Legislature (nmlegis.gov) also posts bills and chaptered acts per session; not probed.

### `nm-nmsa-justia` — Justia - New Mexico Statutes (2025)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** NMSA editions incl. 2019 and 2025; unversioned URL serves 2025.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/new-mexico/chapter-{chapter}/article-{article}/section-{section}/`
  - Placeholders: From N-A-S: chapter = N, article = A, section = whole number 'N-A-S' (37-1-8 -> chapter-37/article-1/section-37-1-8/). Year edition: insert /{year}/ after /new-mexico/ (2019 verified). Letter-suffixed chapters are lower-case (verified: 59A-16-20 -> chapter-59a/article-16/section-59a-16-20/).
  - Index: `https://law.justia.com/codes/new-mexico/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable to the script (Cloudflare challenge on law.justia.com, per other records)
  - Shell blocked by Cloudflare across law.justia.com (see other jurisdictions' records); WebFetch only. Not re-tested by script for NM.
- **Currency:** page header and Universal Citation line — observed: "2025 New Mexico Statutes; 'NM Stat § 37-1-8 (2025)'"
- **Official status:** Third-party copy; Justia disclaims currency.
- **Hazard:** lags official edition (2025 vs 2026)
- **Hazard:** shell blocked
- **Probe:** NMSA 1978, § 37-1-8 → `https://law.justia.com/codes/new-mexico/chapter-37/article-1/section-37-1-8/` — expect: "Actions must be brought against sureties on official bonds and"
- **Evidence (2026-10-17):** WebFetch: body present, '2025 New Mexico Statutes', not truncated. Built URL chapter-41/article-4/section-41-4-4/ also body present ('A governmental entity and any public employee while acting within'). 2019 edition URL also OK. | Independent check 2026-10-17: WebFetch YES 'Actions must be brought against sureties on official bonds and'; '2025 New Mexico Statutes'; second citation NMSA 1978, § 59A-16-20 ok
- **Notes:** Per-section pages make Justia the practical WebFetch second source, since the official chapter PDFs exceed the WebFetch window.

## B. Constitution

### `nm-constitution-nmonesource` — Constitution of New Mexico, annotated (NMOneSource)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · New Mexico Compilation Commission · text: **fetch-and-quote** · official: official
- **Coverage:** Whole constitution with annotations in one PDF (1,422 pp, 4,024,971 chars); also the U.S. Constitution (item 5812).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://nmonesource.com/nmos/c/en/5916/1/document.do`
  - Placeholders: Single document (item 5916). Locate the article by its heading anchored to its title, e.g. regex 'ARTICLE VII\s+Elective Franchise' (a bare 'ARTICLE VII' grep hits ~17 annotation references such as 'Article VII of the New Probate Code'); alternatively take the first 'Section 1. [' after the heading. Then match the section with regex '(?:Sec\.|Section) N\. \[' — the first section of each article reads 'Section 1. [', later ones 'Sec. N. ['. Section numbers restart in every article, so always search forward from the article heading (fetch_doc.py section --start '<heading regex>').
  - Index: `https://nmonesource.com/nmos/c/en/nav_date.do?iframe=true`
  - Navigation: listing (iframe) -> 'Constitution of New Mexico' -> 5916/1/document.do
- **Automation:** WebFetch gated · shell ok · robots: nmonesource.com: User-agent * disallows only two /icm/ items; BUbiNG fully disallowed. laws.nmonesource.com: robots permits.
  - 4M chars: WebFetch cannot reach beyond Article I/early Article II. Intermittent HTTP 403 from nmonesource.com to the script: about half of requests on 2026-10-17 were refused (listing iframes, document.do PDFs, search URLs) while identical URL shapes succeeded seconds earlier; fetch_doc.py then marks that exact URL refused for the day. Never retry a refused URL; use the tier-2 row or another day.
- **Currency:** PDF filename — observed: "nm_const_2026.pdf"
- **Official status:** Published by the State's official legal publisher in the NMSA 1978 compilation (filename nm_const_2026.pdf); no authentication statement in the PDF text.
- **Hazard:** 4M-character single PDF
- **Hazard:** section numbers repeat per article
- **Hazard:** WebFetch gated
- **Hazard:** sporadic HTTP 403; a refused URL is off for the day in fetch_doc — fall back to the fetch tool on a search-surfaced URL or to Justia; never retry by another route
- **Hazard:** article heading text also appears in annotations — anchor on heading + article title
- **Hazard:** first section of each article is 'Section 1. [' not 'Sec. 1. ['
- **Probe:** N.M. Const. art. II, § 18 → `https://nmonesource.com/nmos/c/en/5916/1/document.do` — expect: "No person shall be deprived of life, liberty or property without due process"
- **Evidence (2026-10-17):** fetch_doc.py: 1,422 pp; 'Sec. 18. [Due process; equal protection; sex discrimination.]' at p. 511; 'Sec. 10. [Searches and seizures.]' at p. 25 ('The people shall be secure in their persons, papers, homes'). | Independent check 2026-10-17: script 1,422 pp, 'Sec. 18. [Due process; equal protection' p. 511; second citation N.M. Const. art. VII, § 1 ok

### `nm-constitution-justia` — Justia - New Mexico Constitution

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Preamble and Articles I-XXII, XXIV (index omits XXIII); one page per section.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/new-mexico/article-{article_roman_lower}/section-{section}/`
  - Placeholders: article as lower-case Roman numeral (article-ii); article pages list section links only (no text).
  - Index: `https://law.justia.com/constitution/new-mexico/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare)
  - WebFetch only.
- **Currency:** none stated
- **Official status:** 'This Constitution may not be the most recent version.'
- **Hazard:** no currency date
- **Hazard:** index and article pages have no body text
- **Probe:** N.M. Const. art. II, § 10 → `https://law.justia.com/constitution/new-mexico/article-ii/section-10/` — expect: "The people shall be secure in their persons, papers, homes"
- **Evidence (2026-10-17):** WebFetch: section page body present, not truncated; /article-ii/ is a section list (NOT PRESENT); index lists articles. | Independent check 2026-10-17: WebFetch YES 'The people shall be secure in their persons, papers, homes'; second citation N.M. Const. art. VII, § 1 ok

## C. Court rules

### `nm-rules-annotated-nmonesource` — New Mexico Rules Annotated - annotated rule sets (NMOneSource)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · New Mexico Compilation Commission · text: **fetch-and-quote** · official: official
- **Coverage:** Rule sets with annotations; local district rules; federal NM rules (items 17760-17763). Historical archives from 1989 (nmra-historical).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://laws.nmonesource.com/w/nmos/Rule-Set-{set}-NMRA  (redirects to /nmos/nmra/en/item/{id}/index.do; text at /nmos/nmra/en/{id}/1/document.do)`
  - Placeholders: Redirect verified: Rule-Set-1-NMRA -> item 5687; Rule-Set-11-NMRA -> item 5665. District rules: /w/nmos/District-{1-13}-NMRA; Judicial Standards Commission: Rule-Set-JSC-NMRA.
  - Index: `https://nmonesource.com/nmos/nmra/en/nav_date.do?iframe=true`
  - Navigation: laws.nmonesource.com redirect -> item id -> {id}/1/document.do
- **Automation:** WebFetch gated · shell ok · robots: nmonesource.com: User-agent * disallows only two /icm/ items; BUbiNG fully disallowed. laws.nmonesource.com: robots permits.
  - Redirects resolved by script; both document.do probes (5687, 5665) and the listing iframe returned HTTP 403 on 2026-10-17. Intermittent HTTP 403 from nmonesource.com to the script: about half of requests on 2026-10-17 were refused (listing iframes, document.do PDFs, search URLs) while identical URL shapes succeeded seconds earlier; fetch_doc.py then marks that exact URL refused for the day. Never retry a refused URL; use the tier-2 row or another day.
- **Currency:** Scope of Coverage page — observed: "New Mexico Rules Annotated - current through March 13, 2026"
- **Official status:** As nm-rules-unanno-nmonesource.
- **Hazard:** text not yet read by any route
- **Hazard:** sporadic HTTP 403; a refused URL is off for the day in fetch_doc — fall back to the fetch tool on a search-surfaced URL or to Justia; never retry by another route
- **Probe:** Rule 1-012(B)(6) NMRA → `https://nmonesource.com/nmos/nmra/en/5687/1/document.do`
- **Evidence (2026-10-17):** Redirect Rule-Set-1-NMRA -> item 5687 OK; document.do HTTP 403 to the script; WebFetch PROVENANCE_REQUIRED. | Independent check 2026-10-17: not testable — 5687 and the nmra listing were on fetch_doc's refusal list for the day.
- **Notes:** Annotated sets are larger than the unannotated ones; prefer nm-rules-unanno-nmonesource for quoting.

### `nm-rules-supremecourt` — Supreme Court of New Mexico - Rules & Forms / rule-amendment orders

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Supreme Court of New Mexico · text: **link-only** · official: unknown
- **Coverage:** Recently approved and proposed rule amendments; not a full compilation.
- **Access:** `link-only` · format pdf
  - Index: `https://supremecourt.nmcourts.gov/rules-forms-files/approved-amendments-to-rules-and-forms/`
  - Navigation: /rules-forms-files/rules-forms/ is a menu hub with no PDFs; amendment PDFs are one hop deeper on /rules-forms-files/approved-amendments-to-rules-and-forms/ and /rules-forms-files/proposed-amendments-to-rules-and-forms/
- **Automation:** WebFetch untested · shell ok · robots: robots.txt present but empty (0 chars)
- **Currency:** none stated
- **Official status:** Court site; posts newly approved rule amendments as PDFs (e.g. UJI 14-5050 NMRA PDF found by search).
- **Hazard:** amendments only
- **Probe:**  → `https://supremecourt.nmcourts.gov/rules-forms-files/rules-forms/`
- **Evidence (2026-10-17):** Link seen on the court home page via script; page not read. | Independent check 2026-10-17: hub page 'Rules & Forms' -> 'Approved Amendments to Rules and Forms'.
- **Notes:** Use to check amendments newer than the NMRA PDFs' edition date.

### `nm-rules-unanno-nmonesource` — New Mexico Rules Annotated - unannotated rule sets (NMOneSource)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · New Mexico Compilation Commission (rules promulgated by the Supreme Court) · text: **fetch-and-quote** · official: official
- **Coverage:** Rule Sets 1-28 incl. 1B, 4A, 4B, 17A, 17B, JSC (ids 18468-18501 in list order; JSC 18500) and the 13 local district rule sets (18455-18467); one PDF per rule set.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://nmonesource.com/nmos/nmra-unanno/en/{id}/1/document.do`
  - Placeholders: Rule N-NNN belongs to Rule Set N (Rule 1-012 -> Set 1; 11-702 -> Set 11; 12-502 -> Set 12; UJI 14-xxxx -> Set 14). ids: Set 1 = 18468, 1B = 18469, 2 = 18470, 3 = 18471, 4 = 18472, 4A = 18473, 4B = 18474, 5 = 18475 ... 9 = 18479, 11 = 18481, 12 = 18482, 16 = 18486 (verified from the listing). Rules start with 'N-NNN. Title.' - grep regex '12-502\.\s+\S'.
  - Index: `https://nmonesource.com/nmos/nmra-unanno/en/nav_date.do?iframe=true`
  - Navigation: listing (iframe) -> 'Rule Set N - Title' -> {id}/1/document.do
- **Automation:** WebFetch gated · shell ok · robots: nmonesource.com: User-agent * disallows only two /icm/ items; BUbiNG fully disallowed. laws.nmonesource.com: robots permits.
  - Set 11 (evidence) 67 pp / 151,784 chars; Set 12 (appellate) 127 pp / 346,651 chars: beyond WebFetch's window. Sets 1 (18468) and 16 (18486) returned 403 on test. Intermittent HTTP 403 from nmonesource.com to the script: about half of requests on 2026-10-17 were refused (listing iframes, document.do PDFs, search URLs) while identical URL shapes succeeded seconds earlier; fetch_doc.py then marks that exact URL refused for the day. Never retry a refused URL; use the tier-2 row or another day.
- **Currency:** Scope of Coverage page; PDF filename — observed: "New Mexico Rules Unannotated - current through March 13, 2026; file '12-31-25_unannotated_rule-set-11…'"
- **Official status:** NMRA is the official compilation of Supreme Court rules published by the Compilation Commission (Supreme Court site calls it the Court's official legal publisher).
- **Hazard:** PDF filename date (12-31-25) older than the Scope page's March 13, 2026 claim - check amendments
- **Hazard:** long PDFs
- **Hazard:** WebFetch gated
- **Hazard:** sporadic HTTP 403; a refused URL is off for the day in fetch_doc — fall back to the fetch tool on a search-surfaced URL or to Justia; never retry by another route
- **Hazard:** probe URL 18481 refused HTTP 403 at the independent check; route proven on Set 5 (18475, 265 pp, 728,935 chars)
- **Probe:** Rule 11-702 NMRA → `https://nmonesource.com/nmos/nmra-unanno/en/18481/1/document.do` — expect: "A witness who is qualified as an expert by knowledge, skill, experience"
- **Evidence (2026-10-17):** fetch_doc.py: 67 pp; '11-702. Testimony by expert witnesses.' at p. 40; '11-401. Test for relevant evidence.' p. 7. Second: Set 12 (18482) '12-502. Certiorari from the Supreme Court to the Court of Appeals.' p. 100. | Independent check 2026-10-17: probe 18481 script REFUSED HTTP 403; Set 5 '5-604. Time of commencement of trial' p. 201; second citation Rule 5-604 NMRA ok
- **Notes:** Rule 23-112 NMRA and its Appendix set New Mexico citation form (referenced in Rules 12-305/12-318).

## D. Administrative code

### `nm-nmac-srca` — New Mexico Administrative Code (State Records Center and Archives)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · New Mexico Commission of Public Records, Administrative Law Division · text: **fetch-and-quote** · official: official
- **Coverage:** All 22 NMAC titles; one HTML page per part.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.srca.nm.gov/parts/title{title:02d}/{title:02d}.{chapter:03d}.{part:04d}.html`
  - Placeholders: From T.C.P.S NMAC: title zero-padded to 2, chapter to 3, part to 4 (16.10.8.8 NMAC -> /parts/title16/16.010.0008.html; 1.24.1.7 NMAC -> /parts/title01/01.024.0001.html). The section is on the part page; locate '16.10.8.8' heading.
  - Index: `https://www.srca.nm.gov/nmac-home/nmac-titles/`
- **Automation:** WebFetch gated · shell ok · robots: script check: robots.txt permits /parts/ and /nmac-home/
  - WebFetch on the built part URL hit PROVENANCE_REQUIRED (unanswered). Part pages are small (6,764 and 17,099 chars).
- **Currency:** NMAC home page (https://www.srca.nm.gov/nmac-home/) — observed: "Last Update: September 18, 2026 including all new rules, amendments, and repeals"
- **Official status:** NMAC home page: 'The Official site of the New Mexico Administrative Code (NMAC) and the New Mexico Register'.
- **Hazard:** part pages carry no currency line; use only the NMAC home-page 'Last Update' line (Last-Modified is a bulk date, 21 Apr 2025, on every part page)
- **Probe:** 16.10.8.8 NMAC → `https://www.srca.nm.gov/parts/title16/16.010.0008.html` — expect: "UNPROFESSIONAL OR DISHONORABLE CONDUCT"
- **Evidence (2026-10-17):** fetch_doc.py: 6,764 chars, sections 16.10.8.1-16.10.8.8 present ('ISSUING AGENCY: New Mexico Medical Board'); Last-Modified 21 Apr 2025. Second: 01.024.0001.html, '1.24.1.7 DEFINITIONS' present. | Independent check 2026-10-17: script 6,764 chars, '16.10.8.8 UNPROFESSIONAL OR DISHONORABLE CONDUCT' present; second citation 8.200.400.10 NMAC ok
- **Notes:** NMOneSource also carries NMAC (collection nmac, title items 18046-18067) - not probed.

### `nm-nmac-lii` — Cornell LII - New Mexico Administrative Code

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** NMAC per section.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/new-mexico/N-M-Admin-Code-SS-{title}.{chapter}.{part}.{section}`
  - Placeholders: Unpadded T.C.P.S as cited (21.16.9.1).
  - Index: `https://www.law.cornell.edu/regulations/new-mexico`
- **Automation:** WebFetch ok · shell untested · robots: Crawl-delay 10 (per other records); /regulations allowed
- **Currency:** page header — observed: "State regulations are updated quarterly; we currently have two versions available."
- **Official status:** 'State regulations are updated quarterly'.
- **Hazard:** quarterly lag
- **Probe:** 21.16.9.1 NMAC → `https://www.law.cornell.edu/regulations/new-mexico/N-M-Admin-Code-SS-21.16.9.1` — expect: "New Mexico State University, New Mexico Department of Agriculture"
- **Evidence (2026-10-17):** WebFetch (URL from search): issuing-agency section body present; Notes '21.16.9.1 NMAC - Rn & A, 21 NMAC 16.9.1, 05/29/09'. | Independent check 2026-10-17: WebFetch body present; 'State regulations are updated quarterly'; second citation 16.10.8.8 NMAC ok
- **Notes:** Only one citation probed.

## D. Administrative register

### `nm-register-srca` — New Mexico Register

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Commission of Public Records, Administrative Law Division · text: **fetch-and-quote** · official: official
- **Coverage:** Current volume issues (twice monthly); previous issues 2022-2025; archived single issues 2001-2021; cumulative indexes.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.srca.nm.gov/nmac-home/new-mexico-register/volume-{volume_roman_lower}-issue-{issue}/`
  - Placeholders: Issue page slug uses lower-case Roman volume (volume-xxxvii-issue-19). The whole-issue PDF is on prod-rf-lambda.rtssaas.com with an opaque GUID path - take it from the issue page ('PDF Version of Entire Issue').
  - Index: `https://www.srca.nm.gov/nmac-home/new-mexico-register/`
  - Navigation: Register page lists only the latest 3 issues -> for older issues of the current volume follow 'Previous Issues 1 - 24 : Volume XXXVII - 2026' (https://www.srca.nm.gov/nmac-home/new-mexico-register/all-volumes/volume-xxxvii-2026-2/); 2022-2025 at https://www.srca.nm.gov/all-volumes/; 2001-2021 at https://www.srca.nm.gov/new-mexico-register/archived-issues/ -> issue page -> 'PDF Version of Entire Issue' (rtssaas.com PDF; names vary, e.g. xxxvii19c.pdf vs xxxvii17.pdf)
- **Automation:** WebFetch untested · shell ok · robots: srca.nm.gov permits; rtssaas.com PDF fetched by script (robots permitted)
  - Issue PDFs are long (Vol. XXXVII Issue 19: 42 pp, 231,267 chars).
- **Currency:** issue PDF cover — observed: "Volume XXXVII - Issue 19 - October 6, 2026"
- **Official status:** Issue cover: 'The official publication for all official notices of rulemaking'.
- **Hazard:** PDF host is a third-party CMS (rtssaas.com) with GUID paths
- **Hazard:** long PDFs
- **Hazard:** Register index shows only the latest 3 issues; use the Previous Issues / archive pages
- **Hazard:** issue PDFs can exceed 1M chars (Issue 17: 201 pp)
- **Probe:** N.M. Register, Vol. XXXVII, Issue 19 (Oct. 6, 2026) → `https://prod-rf-lambda.rtssaas.com/PublicFiles/d89c47bd0d70402dba89b03a22bda6d1/efb63e06-9632-4c97-b6c7-a706777a9933/xxxvii19c.pdf` — expect: "The official publication for all official notices of rulemaking"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 42 pp, 231,267 chars, Last-Modified 6 Oct 2026; cover text matches. | Independent check 2026-10-17: script 42 pp, 'Volume XXXVII - Issue 19 - October 6, 2026'; second citation N.M. Reg. Vol. XXXVII, No. 17 (Sept. 9, 2026) ok

## E. Case law

### `nm-opinions-coa-nmcourts` — Court of Appeals of New Mexico - formal and memorandum slip opinions

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · New Mexico Court of Appeals · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Formal (precedential) slip opinions 2009-2026; memorandum (nonprecedential) opinions 2018-2026 (sealed cases omitted).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://coa.nmcourts.gov/wp-content/uploads/sites/43/{YYYY}/{MM}/{Month}-{D}-{YYYY}-{Case-Name}-No.-{docket}.pdf`
  - Placeholders: File names are built from the date and case name and are not reliably derivable (suffixes like '-1' occur); take the link from the listing. Listing rows read 'January 29, 2026- State of New Mexico v. …, No. A-1-CA-41857'.
  - Index: `https://coa.nmcourts.gov/opinions-oral-arguments/formal-opinions/`
  - Navigation: formal-opinions/ or memorandum-opinions/ page (all years on one page, grouped by year/month; 1,634 and 3,779 links) -> find docket A-1-CA-NNNNN -> PDF; listing order is not newest-first — find the row by docket, not position
- **Automation:** WebFetch untested · shell ok · robots: robots.txt present but empty (0 chars)
  - Slip PDFs have pleading-paper line numbers (1-25) at line starts, which break exact-quote matching across lines.
- **Currency:** listing page grouped by month — observed: "Opinions Filed in 2026"
- **Official status:** Formal Opinions page: slip opinions 'may contain computer-generated errors or other deviations from the official opinion' and are replaced when formally released for publication.
- **Hazard:** slip text, no Opinion Number until publication
- **Hazard:** line numbers in PDF text
- **Hazard:** very large listing pages
- **Probe:** State v. Crawford, No. A-1-CA-41857 (N.M. Ct. App. Jan. 29, 2026) → `https://coa.nmcourts.gov/wp-content/uploads/sites/43/2026/01/January-29-2026-State-of-New-Mexico-v.-Bobby-Charles-Crawford-No.-A-1-CA-41857.pdf` — expect: "IN THE COURT OF APPEALS OF THE STATE OF NEW MEXICO"
- **Evidence (2026-10-17):** fetch_doc.py: 29 pp, 49,493 chars; 'Opinion Number: __________', 'Filing Date: January 29, 2026'. Memorandum: Mottola v. Triad Nat'l Sec., No. A-1-CA-41722, 19 pp OK. | Independent check 2026-10-17: script 29 pp, 'IN THE COURT OF APPEALS OF THE STATE OF NEW MEXICO'; second citation State v. Chavez, No. A-1-CA-41405 (N.M. Ct. App. July 29, 2026) ok
- **Notes:** The Supreme Court's own site has no opinion database; its Opinions page sends readers to NMOneSource.

### `nm-opinions-nmonesource` — NMOneSource - Supreme Court and Court of Appeals opinions (official)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · New Mexico Compilation Commission · text: **fetch-and-quote** · official: official
- **Coverage:** Supreme Court (listing years 1852-2026) and Court of Appeals formal opinions 'from 1852' (NM Appellate Reports); slip opinions; unreported decisions/memorandum opinions from January 2009 (Scope page).
- **Read via (in order):** **script**
- **Access:** `search-only` · format pdf
  - Pattern: `https://nmonesource.com/nmos/en/d/s/index.do?cont=&ref={citation}&d1=&d2=&p=&col=&or=date&iframe=true`
  - Placeholders: Plain GET search by official citation works: ref=2019-NMSC-021 -> one row, nmsc/en/item/454344/index.do; ref=2020-NMCA-034 -> nmca/en/item/483661; ref=2018-NMCA-064 -> nmca/en/item/392375 (an extra 'AI Generated Opinion Summaries' row also appears - ignore it). Text: https://nmonesource.com/nmos/{nmsc|nmca}/en/{id}/1/document.do (PDF). By date: https://nmonesource.com/nmos/{nmsc|nmca}/en/{YYYY}/nav_date.do?iframe=true lists the year's decisions (25 per page). Other listings: nav_neu.do (by official citation), nav_re.do (by N.M. Reports citation), nav_alpha.do (by name). Full-text search: cont={words}.
  - Index: `https://nmonesource.com/nmos/nmsc/en/nav_date.do?iframe=true`
  - Navigation: GET search by ref (or year listing) -> item/{id}/index.do -> {id}/1/document.do
- **Automation:** WebFetch gated · shell ok · robots: nmonesource.com: User-agent * disallows only two /icm/ items; BUbiNG fully disallowed. laws.nmonesource.com: robots permits.
  - item/{id}/index.do is a shell (256 chars) and its ?iframe=true variant returned 403; read document.do. Intermittent HTTP 403 from nmonesource.com to the script: about half of requests on 2026-10-17 were refused (listing iframes, document.do PDFs, search URLs) while identical URL shapes succeeded seconds earlier; fetch_doc.py then marks that exact URL refused for the day. Never retry a refused URL; use the tier-2 row or another day. WebFetch on built nmonesource.com / laws.nmonesource.com URLs hit PROVENANCE_REQUIRED (permission prompt unanswered) - gated. A document.do PDF that came from a search result (nmsl/en/18777/1/document.do) was read by WebFetch, so WebFetch can read these PDFs when the URL is approved.
- **Currency:** site footer — observed: "Website last modified: 10/16/2026"
- **Official status:** Supreme Court opinions page: Compilation Commission is 'the official legal publisher for the Supreme Court'. Final opinion PDFs carry a digital attestation by the Commission ('I attest to the accuracy and integrity of this document').
- **Hazard:** listing and item pages are iframe shells
- **Hazard:** WebFetch gated
- **Hazard:** paragraph numbers appear as {1}, {2} in the PDF text - cite as ¶ 1
- **Hazard:** 'AI Generated Opinion Summaries' rows mixed into search results - never quote them
- **Hazard:** sporadic HTTP 403; a refused URL is off for the day in fetch_doc — fall back to the fetch tool on a search-surfaced URL or to Justia; never retry by another route
- **Hazard:** the citation year can differ from the filing year (2017-NMSC-007 filed June 16, 2016)
- **Hazard:** probe URL 454344 refused HTTP 403 to the script at the independent check (WebFetch read it)
- **Probe:** GandyDancer, LLC v. Rock House CGM, LLC, 2019-NMSC-021 → `https://nmonesource.com/nmos/nmsc/en/454344/1/document.do` — expect: "The district court certified for interlocutory review whether the New Mexico"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 13 pp, 37,099 chars, '19sc-021_auth.pdf'; 'Opinion Number: 2019-NMSC-021', 'No. S-1-SC-37201', '{1}' paragraphs. Second: 2018-NMCA-064 (id 392375) 10 pp, header 'Certiorari Granted, October 15, 2018, No. S-1-SC-37201'. | Independent check 2026-10-17: script on 454344 REFUSED 403; WebFetch YES 'The district court certified for interlocutory review'; second citation Hamaatsa, Inc. v. Pueblo of San Felipe, 2017-NMSC-007 ok
- **Notes:** State v. Jackson 2020-NMCA-034 document (483661) returned 403 to the script; Romero v. Lovelace (459534) likewise.

### `nm-cases-justia` — Justia - New Mexico case law

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court and Court of Appeals (ranges not checked); labels 'Published Opinion' / 'Unpublished Opinion'.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/new-mexico/{court-slug}/{year}/{docket-slug}.html`
  - Placeholders: court-slug: supreme-court | court-of-appeals. year = year of the FILING date, not the citation year (2017-NMSC-007 was filed 2016 -> /2016/). Recent opinions: docket-slug = lower-cased S-1-SC / A-1-CA docket (No. S-1-SC-37201 -> /supreme-court/2019/s-1-sc-37201.html; A-1-CA-41405 -> /court-of-appeals/2026/a-1-ca-41405.html). Older opinions use the comma-style docket hyphenated with no prefix (No. 34,287 / S-1-SC-34287 -> /supreme-court/2016/34-287.html); the cutover is unknown (2016 old style, 2019 new style). When unsure, or on any miss, fetch the year listing /cases/new-mexico/{court-slug}/{filing-year}/ and follow the link.
  - Index: `https://law.justia.com/cases/new-mexico/`
  - Navigation: year listing (filing year) lists every decision with its link — use it whenever the slug is uncertain
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare)
  - WebFetch only.
- **Currency:** none
- **Official status:** Third-party copy.
- **Hazard:** no N.M./P.3d pagination for the case itself
- **Hazard:** shell blocked
- **Hazard:** built slug s-1-sc-34287 failed for Hamaatsa (2016/2017): older cases use '34-287' slugs and the filing year
- **Hazard:** citation year != filing year
- **Probe:** GandyDancer, LLC v. Rock House CGM, LLC, 2019-NMSC-021 → `https://law.justia.com/cases/new-mexico/supreme-court/2019/s-1-sc-37201.html` — expect: "The district court certified for interlocutory review"
- **Evidence (2026-10-17):** WebFetch: full opinion, {1}-{43}, '2019-NMSC-021' in header, not truncated. COA 2020 listing gave /court-of-appeals/2020/a-1-ca-39058.html (listing only). | Independent check 2026-10-17: WebFetch YES 'The district court certified for interlocutory review whether the New Mexico'; 2019-NMSC-021

## F. Subsequent history

### `nm-subsequent-history` — Certiorari status in NMOneSource opinion headers; Supreme Court decision on the cert docket

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · New Mexico Compilation Commission · text: **fetch-and-quote** · official: official
- **Coverage:** Published (NMCA) opinions: header line 'Certiorari Granted/Denied, {date}, No. S-1-SC-NNNNN'. The Supreme Court decision on that docket is a separate NMSC opinion or order.
- **Read via (in order):** **script**
- **Access:** `search-only` · format pdf
  - Pattern: `https://nmonesource.com/nmos/en/d/s/index.do?cont=&ref={citation}&d1=&d2=&p=&col=&or=date&iframe=true`
  - Placeholders: 1) GET search the NMCA citation (ref=) -> document.do -> read the first line for 'Certiorari Granted|Denied, date, No. S-1-SC-NNNNN'. 2) Find the Supreme Court decision: search the NMSC year listing(s) after the cert date by party name, or full-text search cont={S-1-SC docket} (untested: returned 403). Justia's Supreme Court slug is the docket (s-1-sc-37201.html) - a deterministic tier-2 check.
  - Index: `https://nmonesource.com/nmos/nmsc/en/nav_date.do?iframe=true`
  - Navigation: NMCA opinion header -> S-1-SC docket -> Justia /supreme-court/{year}/s-1-sc-{n}.html or NMSC listing by party name
- **Automation:** WebFetch gated · shell ok · robots: nmonesource.com: User-agent * disallows only two /icm/ items; BUbiNG fully disallowed. laws.nmonesource.com: robots permits.
  - Intermittent HTTP 403 from nmonesource.com to the script: about half of requests on 2026-10-17 were refused (listing iframes, document.do PDFs, search URLs) while identical URL shapes succeeded seconds earlier; fetch_doc.py then marks that exact URL refused for the day. Never retry a refused URL; use the tier-2 row or another day.
- **Currency:** none stated
- **Official status:** Published Court of Appeals opinions carry the cert disposition line in the Commission's authenticated PDF.
- **Hazard:** cert denials of unpublished/memorandum opinions not shown this way
- **Hazard:** slip (coa.nmcourts.gov) versions lack the cert line
- **Hazard:** docket full-text search unverified (403)
- **Hazard:** sporadic HTTP 403; a refused URL is off for the day in fetch_doc — fall back to the fetch tool on a search-surfaced URL or to Justia; never retry by another route
- **Hazard:** second probe (2015-NMCA-030, item 371480) found by search but document refused HTTP 403 at the independent check
- **Probe:** Gandydancer LLC v. Rock House CGM, LLC, 2018-NMCA-064 -> 2019-NMSC-021 → `https://nmonesource.com/nmos/nmca/en/392375/1/document.do` — expect: "Certiorari Granted, October 15, 2018, No. S-1-SC-37201"
- **Evidence (2026-10-17):** fetch_doc.py: NMCA PDF header 'Certiorari Granted, October 15, 2018, No. S-1-SC-37201'; NMSC opinion 454344 shows 'No. S-1-SC-37201' and reverses ('We reverse'); Justia s-1-sc-37201.html matches. | Independent check 2026-10-17: script 18ca-064_auth.pdf 'Certiorari Granted, October 15, 2018, No. S-1-SC-37201'
- **Notes:** Before 2013 cert dispositions also received vendor-neutral citations of the form YYYY-NMCERT-NNN (from memory; unverified). Case lookup (caselookup.nmcourts.gov) robots.txt unreachable to the script (connection closed) - not used.

## Not available (do not look for these again)

- **statutes** — Official bulk download / API of NMSA 1978: None linked from nmcompcomm.us Scope page or NMOneSource; content is per-chapter PDF only. (2026-10-17)
- **statutes** — public.law edition of NM statutes: public.law covers only CA, CO, FL, NV, NY, OR, TX (per de record). (2026-10-17)
- **case_law** — Opinion database on supremecourt.nmcourts.gov: Opinions page says to read Supreme Court opinions on the Compilation Commission website (link to nmonesource.com). (2026-10-17)

## Corpus candidates (maintainers)

- `nm-nmsa-nmonesource` — Chapter PDFs 430K-874K chars (ch. 37, ch. 41); WebFetch window ~100K and gated.
- `nm-constitution-nmonesource` — One 1,422-page, 4M-char annotated PDF.
- `nm-rules-unanno-nmonesource` — Rule set PDFs 150K-350K chars (Sets 11, 12); also Set 1 (18468) and Set 16 (18486).

## Open questions

- NMOneSource intermittently answers HTTP 403 to the script (about half of requests on 2026-10-17); is it rate-based (WAF) - would a slower crawl succeed consistently?
- Annotated NMRA (nm-rules-annotated-nmonesource) and unannotated NMSA chapters never read (403); Rule 1-012 NMRA text not verified by any route.
- WebFetch on nmonesource.com and srca.nm.gov built URLs was gated (PROVENANCE_REQUIRED); WebFetch behaviour on those hosts untested beyond one search-sourced document.do.
- Full-text search by Supreme Court docket (cont=S-1-SC-NNNNN) untested (403).
- YYYY-NMCERT-NNN cert citation form and the end of the official N.M. Reports (vendor-neutral citations from 1996; N.M. Reports ceased c. 2013?) from memory, unverified.
- Justia NM case coverage years not checked; State v. Jackson 2020-NMCA-034 not located on Justia's 2020 COA listing (page 1 only).
- CourtListener ids nm / nmctapp unverified.
- Probe an actual Laws 2026 session-law chapter on NMOneSource (nmsl) before relying on nm-session-laws-nmonesource.
- Justia NM case-slug cutover year (comma-docket '34-287' style vs 's-1-sc-NNNNN') unknown.
