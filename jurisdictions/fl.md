# Florida (FL) — free legal sources

_Generated from `data/fl.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: Online Sunshine (leg.state.fl.us) per-section pages are constructible from the section number and read cleanly by both tools; flsenate.gov is the second official fetch (crawl-delay 10, 429s under load); Justia (2025) and public.law (stale 2024 text) are tier-2. Constitution: one huge page on flsenate/Online Sunshine — WebFetch cannot reach Articles VI-XII, the script can. Court rules: only Florida Bar PDFs, shell-blocked by Cloudflare and cut off by WebFetch after ~100K chars, so most rules (e.g. Civ. P. 1.510) are unreachable. Case law: every flcourts.gov host (Supreme Court, six DCAs) is robots-disallowed and ACIS is a JS app; use Justia (1848-2026, PCAs included) and the FSU archive of Supreme Court opinions. Admin code: flrules.org metadata is fine but rule text is a binary .doc; LII has text but lags (2023 vs 2026 amendments).

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Florida | `fla (unverified)` | Fla. | So. 3d, So. 2d, So., Fla. L. Weekly | — |
| Florida First District Court of Appeal | `fladistctapp (unverified)` | Fla. 1st DCA | So. 3d, So. 2d, Fla. L. Weekly | — |
| Florida Second District Court of Appeal | `fladistctapp (unverified)` | Fla. 2d DCA | So. 3d, So. 2d, Fla. L. Weekly | — |
| Florida Third District Court of Appeal | `fladistctapp (unverified)` | Fla. 3d DCA | So. 3d, So. 2d, Fla. L. Weekly | — |
| Florida Fourth District Court of Appeal | `fladistctapp (unverified)` | Fla. 4th DCA | So. 3d, So. 2d, Fla. L. Weekly | — |
| Florida Fifth District Court of Appeal | `fladistctapp (unverified)` | Fla. 5th DCA | So. 3d, So. 2d, Fla. L. Weekly | — |
| Florida Sixth District Court of Appeal | `fladistctapp (unverified)` | Fla. 6th DCA | So. 3d, So. 2d, Fla. L. Weekly | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Florida Statutes | `Fla. Stat. § 768.81 (2024)`; `§ 57.105, Fla. Stat.`; `section 768.81, Florida Statutes`; `s. 768.81, F.S.`; `Fla. Stat. Ann. § 90.803`; `§ 768.81(3), Fla. Stat. (2023)`; `§§ 768.71-768.81, Fla. Stat.`; `section 1001.42 of the Florida Statutes`; `Fla. Stat. section 83.56` | `fl-statutes-online-sunshine` → `fl-statutes-flsenate` → `fl-statutes-justia` → `fl-statutes-publiclaw` |
| Florida Evidence Code (Fla. Stat. ch. 90) | `section 90.404(2)(a) of the Florida Evidence Code`; `§ 90.803(6), Fla. Stat.`; `Fla. Stat. § 90.702` | `fl-statutes-online-sunshine` → `fl-statutes-flsenate` → `fl-statutes-justia` |
| Laws of Florida (session laws) | `Ch. 2023-15, Laws of Fla.`; `ch. 2023-15, § 9, Laws of Fla.`; `Chapter 2023-15, Laws of Florida` | `fl-laws-of-florida` |
| Florida Constitution | `Art. V, § 3(b)(3), Fla. Const.`; `Fla. Const. art. I, § 9`; `Article I, Section 9 of the Florida Constitution`; `article V, section 3(b)(3) of the Florida Constitution` | `fl-constitution-online-sunshine` → `fl-constitution-flsenate` → `fl-constitution-justia` |
| Florida Rules of Civil Procedure | `Fla. R. Civ. P. 1.510`; `Florida Rule of Civil Procedure 1.510(a)`; `rule 1.510, Florida Rules of Civil Procedure`; `Rule 1.442 of the Florida Rules of Civil Procedure` | `fl-rules-civil-floridabar` |
| Florida Rules of Criminal Procedure | `Fla. R. Crim. P. 3.850`; `Florida Rule of Criminal Procedure 3.191(a)`; `rule 3.800(a), Florida Rules of Criminal Procedure`; `Rule 3.850 of the Florida Rules of Criminal Procedure` | `fl-rules-criminal-floridabar` |
| Florida Rules of Appellate Procedure | `Fla. R. App. P. 9.030(a)(2)(A)(iv)`; `Florida Rule of Appellate Procedure 9.330`; `rule 9.141(d), Florida Rules of Appellate Procedure`; `Rule 9.331 of the Florida Rules of Appellate Procedure` | `fl-rules-appellate-floridabar` |
| Florida Rules of General Practice and Judicial Administration | `Fla. R. Gen. Prac. & Jud. Admin. 2.420`; `Fla. R. Jud. Admin. 2.516`; `Florida Rule of General Practice and Judicial Administration 2.514`; `Rule 2.420 of the Florida Rules of General Practice and Judicial Administration` | `fl-rules-judadmin-floridabar` |
| Florida Administrative Code | `Fla. Admin. Code R. 61G15-19.001`; `Fla. Admin. Code Ann. r. 62-302.530`; `rule 61G15-19.001, F.A.C.`; `Rule 62-302.530, Florida Administrative Code` | `fl-fac-flrules` → `fl-fac-lii` |
| Florida Administrative Register | `51 Fla. Admin. Reg. 1234 (Dec. 23, 2025)`; `Florida Administrative Register Volume 51, Number 247`; `FAR Vol. 52, No. 126` | `fl-far-flrules` |
| Reported Florida cases (Southern Reporter) | `Loyd v. State, 379 So. 3d 1080 (Fla. 2023)`; `Smith v. Jones, 123 So. 3d 456 (Fla. 4th DCA 2019)`; `Doe v. Roe, 987 So. 2d 65, 67 (Fla. 2d DCA 2008)`; `Smith v. State, 123 So. 3d 456 (Fla. 1st DCA 2013) (table)`; `Hoffman v. Jones, 280 So. 2d 431 (Fla. 1973)`; `Roe v. Doe, 222 So. 3d 333 (Fla. Dist. Ct. App. 2017)` | `fl-cases-justia` → `fl-sc-fsu-archive` → `fl-opinions-flcourts` |
| Florida Law Weekly (slip-opinion cites) | `48 Fla. L. Weekly D1234 (Fla. 4th DCA June 7, 2023)`; `50 Fla. L. Weekly S45 (Fla. Feb. 13, 2025)` | `fl-cases-justia` → `fl-sc-fsu-archive` |
| Florida appellate docket numbers (pre- and post-2023 ACIS forms) | `No. SC2022-0378`; `No. 4D2024-0558`; `Case No. 1D19-1234`; `SC19-87`; `6D23-3822` | `fl-cases-justia` → `fl-sc-fsu-archive` |
| Westlaw unreported cites | `2024 WL 123456 (Fla. 3d DCA Jan. 3, 2024)`; `2025 WL 98765, at *2 (Fla. Feb. 13, 2025)` | `fl-cases-justia` |

Regexes (case-insensitive):

- Florida Statutes: `Fla\.\s*Stat\.?(?:\s*Ann\.?)?\s*(?:§+|sec(?:tion|\.)|s\.)\s*(?P<section>\d{1,4}\.\d{2,5})(?!\d)|(?:§+|sec(?:tion|s|\.)?|ss?\.)\s*(?P<section2>\d{1,4}\.\d{2,5})(?!\d)(?:\([0-9a-zA-Z]+\))*(?:\s*[-–]\s*\d{1,4}\.\d{2,5}(?:\([0-9a-zA-Z]+\))*)?,?\s+(?:of\s+the\s+)?(?:Fla\.\s*Stat\.|Florida\s+Statutes|F\.\s*S\.)`
- Florida Evidence Code (Fla. Stat. ch. 90): `(?:Fla\.\s*Stat\.?\s*§+\s*(?P<section>90\.\d{3,4})|(?:§+|sec(?:tion|\.)?|s\.)\s*(?P<section2>90\.\d{3,4})(?:\([0-9a-zA-Z]+\))*,?\s+(?:of\s+the\s+)?(?:Florida\s+Evidence\s+Code|Fla\.\s*Stat\.|Florida\s+Statutes|F\.\s*S\.))`
- Laws of Florida (session laws): `ch(?:apter|\.)\s*(?P<year>(?:18|19|20)\d\d)-(?P<chapter>\d{1,4}),?(?:\s*§+\s*\d+,?)?\s+Laws\s+of\s+(?:Fla\.|Florida)`
- Florida Constitution: `Fla\.\s*Const\.\s*art\.\s*(?P<article>[IVX]+),?\s*§\s*(?P<section>\d+[a-z]?)|art(?:icle|\.)\s*(?P<article2>[IVX]+),?\s*(?:§|sec(?:tion|\.))\s*(?P<section2>\d+[a-z]?)(?:\([0-9a-zA-Z]+\))*,?\s*(?:Fla\.\s*Const\.|of\s+the\s+(?:Florida|Fla\.)\s+Constitution)`
- Florida Rules of Civil Procedure: `Fla\.\s*R\.\s*Civ\.\s*P\.\s*(?P<rule>1\.\d{3}[a-z]?)|Florida\s+Rules?\s+of\s+Civil\s+Procedure\s+(?P<rule2>1\.\d{3}[a-z]?)|rule\s+(?P<rule3>1\.\d{3}[a-z]?)(?:\([0-9a-zA-Z]+\))*,\s*Florida\s+Rules\s+of\s+Civil\s+Procedure|rule\s+(?P<rule4>1\.\d{3}[a-z]?)(?:\([0-9a-zA-Z]+\))*\s+of\s+the\s+Florida\s+Rules\s+of\s+Civil\s+Procedure`
- Florida Rules of Criminal Procedure: `Fla\.\s*R\.\s*Crim\.\s*P\.\s*(?P<rule>3\.\d{3}[a-z]?)|Florida\s+Rules?\s+of\s+Criminal\s+Procedure\s+(?P<rule2>3\.\d{3}[a-z]?)|rule\s+(?P<rule3>3\.\d{3}[a-z]?)(?:\([0-9a-zA-Z]+\))*,\s*Florida\s+Rules\s+of\s+Criminal\s+Procedure|rule\s+(?P<rule4>3\.\d{3}[a-z]?)(?:\([0-9a-zA-Z]+\))*\s+of\s+the\s+Florida\s+Rules\s+of\s+Criminal\s+Procedure`
- Florida Rules of Appellate Procedure: `Fla\.\s*R\.\s*App\.\s*P\.\s*(?P<rule>9\.\d{3}[a-z]?)|Florida\s+Rules?\s+of\s+Appellate\s+Procedure\s+(?P<rule2>9\.\d{3}[a-z]?)|rule\s+(?P<rule3>9\.\d{3}[a-z]?)(?:\([0-9a-zA-Z]+\))*,\s*Florida\s+Rules\s+of\s+Appellate\s+Procedure|rule\s+(?P<rule4>9\.\d{3}[a-z]?)(?:\([0-9a-zA-Z]+\))*\s+of\s+the\s+Florida\s+Rules\s+of\s+Appellate\s+Procedure`
- Florida Rules of General Practice and Judicial Administration: `Fla\.\s*R\.\s*(?:Gen\.\s*Prac\.\s*(?:&|and)\s*)?Jud\.\s*Admin\.\s*(?P<rule>2\.\d{3})|Florida\s+Rules?\s+of\s+(?:General\s+Practice\s+and\s+)?Judicial\s+Administration\s+(?P<rule2>2\.\d{3})|rule\s+(?P<rule3>2\.\d{3})(?:\([0-9a-zA-Z]+\))*\s+of\s+the\s+Florida\s+Rules\s+of\s+(?:General\s+Practice\s+and\s+)?Judicial\s+Administration`
- Florida Administrative Code: `Fla\.\s*Admin\.\s*Code\s*(?:Ann\.\s*)?R\.?\s*(?P<rule>\d{1,2}[A-Z]{0,2}\d{0,2}-\d{1,4}\.\d{3,4})|r(?:ule)?\.?\s*(?P<rule2>\d{1,2}[A-Z]{0,2}\d{0,2}-\d{1,4}\.\d{3,4})(?:\([0-9a-zA-Z]+\))*,?\s*(?:F\.\s*A\.\s*C\.|Florida\s+Administrative\s+Code)`
- Florida Administrative Register: `(?P<volume>\d{2})\s+Fla\.\s*Admin\.\s*Reg\.\s*(?P<page>\d+)|(?:Florida\s+Administrative\s+Register|FAR),?\s*Vol(?:ume|\.)\s*(?P<volume2>\d{2}),?\s*(?:No\.|Number)\s*(?P<number>\d{1,3})`
- Reported Florida cases (Southern Reporter): `(?P<volume>\d{1,4})\s+So\.\s*(?:(?P<series>[23])d\s+)?(?P<page>\d{1,5})(?:,\s*\d+(?:[-–]\d+)?)?\s*\((?P<court>Fla\.(?:\s*(?P<dca>[1-6](?:st|nd|d|rd|th))\s*DCA|\s*Dist\.\s*Ct\.\s*App\.)?)\s*(?P<year>\d{4})\)`
- Florida Law Weekly (slip-opinion cites): `(?P<volume>\d{1,2})\s+Fla\.\s*L\.\s*Weekly\s+(?:Supp\.\s+)?(?P<series>[SDC])?(?P<page>\d{1,5})`
- Florida appellate docket numbers (pre- and post-2023 ACIS forms): `\b(?P<court>SC|[1-6]D)(?P<year>\d{4}|\d{2})-(?P<seq>\d{1,4})\b`
- Westlaw unreported cites: `(?P<year>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Fla\.`

Short forms → URL key:

Fla. Stat. → `statutes`; Fla. Stat. Ann. → `statutes`; F.S. → `statutes`; Florida Statutes → `statutes`; Florida Evidence Code → `statutes`; Fla. Evid. Code → `statutes`; Fla. R. Civ. P. → `fl-rules-civil-floridabar`; Fla. R. Crim. P. → `fl-rules-criminal-floridabar`; Fla. R. App. P. → `fl-rules-appellate-floridabar`; Fla. R. Gen. Prac. & Jud. Admin. → `fl-rules-judadmin-floridabar`; Fla. R. Jud. Admin. → `fl-rules-judadmin-floridabar`; F.A.C. → `fl-fac-flrules`; Fla. Admin. Code → `fl-fac-flrules`; Fla. Admin. Code Ann. → `fl-fac-flrules`; FAR → `fl-far-flrules`; Fla. Admin. Reg. → `fl-far-flrules`

Florida has no public-domain/vendor-neutral case citation; cases are cited to So./So. 2d/So. 3d (West) or, before reporter publication, to Florida Law Weekly (commercial; S = Supreme Court, D = DCAs) or Westlaw. Florida style (Fla. R. App. P. 9.800) writes DCA courts as '(Fla. 4th DCA 2019)'; Bluebook writes '(Fla. Dist. Ct. App. 2019)': both are matched. Florida statutes are a single code (section = chapter.number), so no code key is needed; statutes are cited as 'Fla. Stat. § 768.81 (2024)' (Bluebook), '§ 768.81, Fla. Stat. (2024)' (Florida style) or 's. 768.81, F.S.' (legislative style). A '§§ 768.71-768.81' range is two sections, not one hyphenated number: the regex takes the first. The Evidence Code is statutory (ch. 90), not a court rule set. Guards: bare 'Rule 1.510', 'rule 3.850' or 'section 90.803' must not route here without a 'Fla.'/'Florida' marker (other states number rules similarly). Docket forms 'SC2022-0378' / '4D2024-0558' (ACIS, 2023 on) and '4D19-0993' / 'SC19-87' (earlier) are Florida-specific in shape but route only with Florida context. PCA (per curiam affirmed without opinion) decisions appear in So. 3d only as table entries and on Justia as one-line opinions; under Jenkins v. State, 385 So. 2d 1356 (Fla. 1980) (from memory, unverified), a citation-free PCA cannot be reviewed by the Supreme Court for conflict, so it is normally final. Since Jan. 1, 2023 there are six DCAs (Sixth DCA, Lakeland). CourtListener ids 'fla' and 'fladistctapp' are from memory and unverified; CourtListener groups all DCAs under one id. Rules Regulating The Florida Bar ('R. Regulating Fla. Bar 4-1.7') and Family Law / Small Claims / Juvenile rules were not probed: no route recorded. Evidence-code cites (§ 90.xxx, Fla. Stat.) match both the Florida Statutes and Evidence Code patterns; both route to the same statute sources, so the double match is harmless. Prose rule forms 'Rule 3.850 of the Florida Rules of Criminal Procedure' and 'Fla. Stat. section 83.56' added after the independent check.

## A. Statutes / code

### `fl-laws-of-florida` — Laws of Florida (session laws)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Florida Department of State (laws.flrules.org) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Chapter laws by year (tested 2023 and 2025); one PDF per chapter.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://laws.flrules.org/{year}/{chapter}`
  - Placeholders: From 'ch. 2023-15, Laws of Fla.': year = 2023, chapter = 15 unpadded. Serves the PDF (canonical file https://laws.flrules.org/files/Ch_{year}-{chapter:03d}.pdf, e.g. Ch_2023-015.pdf).
  - Index: `https://laws.flrules.org/`
- **Automation:** WebFetch ok · shell ok · robots: not separately read (flrules.org robots.txt answered curl with a Cloudflare challenge but fetch_doc.py's robots check passed)
  - Ch. 2023-15: 21 pages, 55,995 chars; read in full by both tools.
- **Currency:** none stated
- **Official status:** Department of State publication of enrolled chapter laws with 'Approved by the Governor' and 'Filed in Office Secretary of State' lines; no authentication statement.
- **Hazard:** Cloudflare fronting flrules.org may challenge some clients
- **Probe:** Ch. 2023-15, Laws of Fla. → `https://laws.flrules.org/2023/15` — expect: "CHAPTER 2023-15 Committee Substitute for Committee Substitute for House Bill No. 837"
- **Evidence (2026-10-16):** WebFetch: YES, 31 sections, 'Approved by the Governor March 24, 2023', not truncated. fetch_doc.py: pdf 21 pp; /2025/2 pdf 5 pp. | Independent check 2026-10-16: WebFetch YES: 'An act relating to civil remedies'; 'Approved by the Governor March 24, 2023'; complete; second citation Ch. 2024-5, Laws of Fla. ok

### `fl-statutes-flsenate` — Florida Statutes (Florida Senate)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · The Florida Senate · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Florida Statutes by year (year selector lists 2026 back to at least 2015); one page per section.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.flsenate.gov/Laws/Statutes/{year}/{section}`
  - Placeholders: section verbatim with its dot (768.81, 57.105, 90.803); a zero-padded chapter form (/2024/0768.81) also appears in public.law source links. year = edition year (2026 current).
  - Index: `https://www.flsenate.gov/Laws/Statutes`
- **Automation:** WebFetch ok · shell ok · robots: User-agent * — Crawl-delay: 10; Disallow /api/, /API/, admin and tracker paths; Allow /Laws/
  - Crawl-delay 10 s. On 2026-10-16 the host answered HTTP 429 after ~8 script fetches in a few minutes; fetch_doc.py now treats 429 as 'rate-limited, try later' (no day-long lockout). Re-test after the fix: fetch_doc.py info /2026/768.81 → html 15,341 chars. Use Online Sunshine as the first statute fetch and flsenate as the second; if the script gets 429, wait and retry or use WebFetch.
- **Currency:** breadcrumb and heading of each section page — observed: "2025 Florida Statutes (for /2025/ URLs); '2026 Florida Statutes' for /2026/"
- **Official status:** Footer of https://www.flsenate.gov/Laws/Statutes: 'Disclaimer: The information on this system is unverified. The journals or printed bills of the respective chambers should be consulted for official purposes.'
- **Hazard:** HTTP 429 rate-limiting under the 10-second crawl-delay (retry later, or use WebFetch)
- **Hazard:** year must be chosen in the URL
- **Probe:** Fla. Stat. § 57.105 (2025) → `https://www.flsenate.gov/Laws/Statutes/2025/57.105` — expect: "Upon the court's initiative or motion of any party, the"
- **Evidence (2026-10-16):** WebFetch: YES '…motion of any party, the', '2025 Florida Statutes', subsections (1)-(8), not truncated, disclaimer 'information on this system is unverified'. fetch_doc.py: /2025/768.81 15,273 chars; /2026/90.803 heading '2026 Florida Statutes … Section 803' with body. | Independent check 2026-10-16: WebFetch YES 'Upon the court's initiative or motion of any party, the'; '2025 Florida Statutes'; second citation Fla. Stat. § 83.56 (2026) ok | Script re-test 2026-10-16 after lsnet 429 fix: /2026/768.81 html 15,341 chars.

### `fl-statutes-online-sunshine` — Florida Statutes (Online Sunshine)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Florida Legislature (Office of Legislative Services) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Current Florida Statutes (header reads 'The 2026 Florida Statutes') plus prior editions 1997-2025 via a StatuteYear parameter; per-section, per-chapter and title-index pages.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL={range}/{chapter4}/Sections/{chapter4}.{subsection}.html`
  - Placeholders: Split the section at the dot: chapter = digits before it, subsection = digits after it verbatim (no padding change: 768.81 → '81', 1001.42 → '42', 90.803 → '803'). chapter4 = chapter zero-padded to 4 digits (0090, 0768, 1001). range = the hundred-block of the chapter as 'NNNN-NNNN' (ch. 90 → 0000-0099, ch. 768 → 0700-0799, ch. 1001 → 1000-1099). Prior years: add '&StatuteYear={YYYY}' (verified for 2023; header then reads 'The 2023 Florida Statutes (including Special Session C)'). Whole chapter: …&URL={range}/{chapter4}/{chapter4}.html (very long, see hazards); chapter contents: …/{chapter4}/{chapter4}ContentsIndex.html. http:// redirects to https://.
  - Index: `https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Index&Title_Request={TITLE_ROMAN}`
  - Navigation: Not needed for sections (constructible). The title index DOES show section ranges per chapter/part, e.g. 'Part I: GENERAL PROVISIONS (ss. 768.041-768.405)'.
- **Automation:** WebFetch ok · shell ok · robots: User-agent * — Disallow /employees/ only (Drifter and SemrushBot fully disallowed); /statutes allowed
  - Section pages are small (768.81: 9,490 chars; 1001.42: 51,064 chars). Whole-chapter pages are large (ch. 768: 217,351 chars) and exceed the WebFetch window — always use the per-section URL.
- **Currency:** page header above the title/chapter line on every section page — observed: "The 2026 Florida Statutes"
- **Official status:** No authentication statement on section pages (footer: 'Copyright 1995-2026 The Florida Legislature'). The sister site flsenate.gov states the online information 'is unverified' and the printed journals/bills should be consulted for official purposes. Florida has not enacted UELMA.
- **Hazard:** whole-chapter pages exceed the WebFetch ~100K window
- **Hazard:** currency is an edition year only (no 'current through' date)
- **Hazard:** page date stamp shows the server's next-day date (October 17, 2026)
- **Probe:** Fla. Stat. § 768.81 → `https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0700-0799/0768/Sections/0768.81.html` — expect: "(1) DEFINITIONS.—As used in this section, the term:"
- **Evidence (2026-10-16):** WebFetch: YES, body '(1) DEFINITIONS.—As used in this section, the term:'; 'The 2026 Florida Statutes'; complete through (6) and History. fetch_doc.py: 768.81 (9,490 chars), 90.803 ('The provision of s. 90.802 to the contrary notwithstanding'), 1001.42 (Title XLVIII) all body present; StatuteYear=2023 returns 'The 2023 Florida Statutes (including Special Session C)'. | Independent check 2026-10-16: WebFetch YES '(1) DEFINITIONS.—As used in this section, the term:'; 'The 2026 Florida Statutes'; complete; second citation Fla. Stat. § 316.193 (also § 83.56) ok
- **Notes:** Bulk: the Statutes Download page (index.cfm?Mode=Statutes%20Download&Submenu=7&Tab=statutes) offers only a Windows installer zip (FLLawDL2026.zip, 'Advanced Legislative Search & Browse'), not structured XML/JSON.

### `fl-statutes-justia` — Justia — Florida Statutes (2025)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Florida Statutes by year; unversioned URL serves the 2025 edition.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/florida/title-{title_roman_lower}/chapter-{chapter}/[part-{part_roman_lower}/]section-{chapter}-{subsection}/`
  - Placeholders: Section dot becomes a hyphen (768.81 → section-768-81). Title (Roman, lower case) and part (Roman, lower case; omitted when the chapter has no parts, e.g. ch. 90) are not in the citation: take them from the Online Sunshine title index, which shows 'Part II … (ss. 768.71-768.81)'. Examples: 768.81 → /title-xlv/chapter-768/part-ii/section-768-81/; 90.803 → /title-vii/chapter-90/section-90-803/. Part ranges: compare the digits after the dot as INTEGERS, not decimals — 83.56 → 56 lies in Part II 'ss. 83.40-83.684' (40-684), not Part I 'ss. 83.001-83.251' (1-251). The title Roman numeral is in the Online Sunshine section-page header ('Title VI'); that header gives no part, so take the part from the title index ranges.
  - Index: `https://law.justia.com/codes/florida/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: robots.txt returns 403 Cloudflare 'Just a moment...'
  - fetch_doc.py REFUSED (robots.txt challenge). WebFetch only.
- **Currency:** page heading and Universal Citation line — observed: "2025 Florida Statutes; 'FL Stat § 768.81 (2025)'"
- **Official status:** Third-party compilation; edition label only.
- **Hazard:** edition lags the official 2026 text
- **Hazard:** title/part segments need an index hop
- **Hazard:** shell blocked by Cloudflare
- **Hazard:** part hop ambiguous if ranges are read as decimals (83.56 vs 83.001-83.251): compare as integers
- **Probe:** Fla. Stat. § 768.81 → `https://law.justia.com/codes/florida/title-xlv/chapter-768/part-ii/section-768-81/` — expect: "(1) DEFINITIONS.—As used in this section, the term:"
- **Evidence (2026-10-16):** WebFetch: YES, '2025 Florida Statutes', 'FL Stat § 768.81 (2025)', complete. Also /title-vii/chapter-90/section-90-803/: YES 'The provision of s. 90.802 to the contrary notwithstanding, the'. | Independent check 2026-10-16: WebFetch YES; '2025 Florida Statutes'; 'FL Stat § 768.81 (2025)'; complete; second citation Fla. Stat. § 83.56 ok

### `fl-statutes-publiclaw` — public.law — Florida Statutes

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Public.Law · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Florida Statutes, 2024 edition text as captured Aug. 7, 2025, despite a 'Current through Fall 2025' label.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://florida.public.law/statutes/fla._stat._{section}`
  - Placeholders: section verbatim with its dot (fla._stat._768.81, fla._stat._57.105, fla._stat._90.803).
  - Index: `https://florida.public.law/statutes`
- **Automation:** WebFetch ok · shell ok · robots: User-agent * — Disallow /admin, /api, /data, /demo, /images, /users
  - Pages last-modified Aug. 7-8, 2025.
- **Currency:** section page (label) and Source line at the foot of the body — observed: "Current through Fall 2025; source 'Statutes/2024/0768.81 (accessed Aug. 7, 2025)'"
- **Official status:** Each section cites its source as flsenate.gov/Laws/Statutes/2024/… '(accessed Aug. 7, 2025)'.
- **Hazard:** stale: 2024 edition text despite the 'Fall 2025' label; misses 2025 and 2026 session changes
- **Probe:** Fla. Stat. § 57.105 → `https://florida.public.law/statutes/fla._stat._57.105` — expect: "Upon the court's initiative or motion of any party, the"
- **Evidence (2026-10-16):** WebFetch: YES, 'Current through Fall 2025', '(accessed Aug. 7, 2025)', complete through (8). fetch_doc.py: fla._stat._768.81 and fla._stat._90.803 body present; source line cites flsenate 2024. | Independent check 2026-10-16: WebFetch YES; 'Current through Fall 2025'; '(accessed Aug. 7, 2025)'; complete; second citation Fla. Stat. § 83.56 ok
- **Notes:** Use last: older than Justia (2025) and the official 2026 text.

## B. Constitution

### `fl-constitution-flsenate` — Florida Constitution (Florida Senate)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · The Florida Senate · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Constitution of 1968 as amended, whole document on one page with section anchors.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.flsenate.gov/Laws/Constitution#A{article_arabic}S{section:02d}`
  - Placeholders: Single page; anchors name='A{article}' and 'A{article}S{section:02d}' with Arabic article numbers (art. I § 9 → #A1S09; art. V § 3 → #A5S03). Anchors do not change what WebFetch reads.
  - Index: `https://www.flsenate.gov/Laws/Constitution`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay 10; /Laws/ allowed
  - WebFetch reports the page text as 133,252 chars: window 1 ends in Art. IV § 9; offset=100000 reaches Art. V § 3(b)(3) but ends at Art. V § 13. Articles VI-XII are beyond what WebFetch extracts. fetch_doc.py reads the whole page (419,692 chars incl. Art. VII § 6 'Homestead exemptions'). Articles VI-XII: prefer fl-constitution-online-sunshine via fetch_doc.py (Art. X § 4 reached at offset ~254K), since flsenate may rate-limit (429) the script.
- **Currency:** title line at top of the text — observed: "AS REVISED IN 1968 AND SUBSEQUENTLY AMENDED"
- **Official status:** Same flsenate.gov 'information on this system is unverified' disclaimer.
- **Hazard:** single huge page; WebFetch cannot reach Articles VI-XII
- **Hazard:** no amended-through date
- **Hazard:** HTTP 429 rate-limiting on flsenate.gov can interrupt the script route; for Arts. VI-XII use Online Sunshine via the script
- **Probe:** Fla. Const. art. I, § 9 → `https://www.flsenate.gov/Laws/Constitution` — expect: "No person shall be deprived of life, liberty or property"
- **Evidence (2026-10-16):** WebFetch: Art. I § 9 YES 'No person shall be deprived of life, liberty or property'; Art. V § 3(b)(3) NOT PRESENT in window 1, YES at offset=100000 ('May review any decision of a district court of appeal'). fetch_doc.py 419,692 chars, Art. VII reached. | Independent check 2026-10-16: WebFetch YES Art. I § 9; 'AS REVISED IN 1968 AND SUBSEQUENTLY AMENDED'; window 1 ends Art. IV § 9; second citation Art. V, § 3(b)(3), Fla. Const. ok

### `fl-constitution-online-sunshine` — Florida Constitution (Online Sunshine)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Florida Legislature · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Constitution as revised in 1968 and amended; one page with #A{n} / #A{n}S{nn} anchors.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.leg.state.fl.us/index.cfm?Mode=Constitution&Submenu=3&Tab=statutes#A{article_arabic}S{section:02d}`
  - Placeholders: Single page; same anchor scheme as flsenate (#A1S09).
  - Index: `https://www.leg.state.fl.us/index.cfm?Mode=Constitution&Submenu=3&Tab=statutes`
- **Automation:** WebFetch ok · shell ok · robots: Disallow /employees/ only
  - WebFetch text 136,480 chars; window 1 ends in Art. IV § 13. Art. V § 3(b)(3) sits at ~104K chars of the shell text. fetch_doc.py reads the whole page and is the preferred route to Articles VI-XII (Art. X § 4(a) 'Homestead; exemptions' at offset 254,535). The script follows a redirect to a /Statutes/index.cfm?…&CFID=… session URL (harmless). WebFetch may report the site title instead of the 'AS REVISED IN 1968' line.
- **Currency:** title line — observed: "AS REVISED IN 1968 AND SUBSEQUENTLY AMENDED"
- **Official status:** No authentication statement; legislative site.
- **Hazard:** single huge page; WebFetch truncation
- **Probe:** Fla. Const. art. I, § 9 → `https://www.leg.state.fl.us/index.cfm?Mode=Constitution&Submenu=3&Tab=statutes` — expect: "No person shall be deprived of life, liberty or property"
- **Evidence (2026-10-16):** WebFetch: Art. I § 9 YES; Art. V § 3(b)(3) NOT PRESENT (truncated in Art. IV § 13). fetch_doc.py grep found 'expressly and directly conflicts' (Art. V § 3(b)(3)) at offset 103,924. | Independent check 2026-10-16: WebFetch YES Art. I § 9; window 1 ends Art. IV § 13 (truncated); second citation Art. X, § 4(a), Fla. Const. ok

### `fl-constitution-justia` — Justia — Florida Constitution

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole constitution on one page with #A01S01 anchors.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/florida/#A{article:02d}S{section:02d}`
  - Placeholders: single page; anchors do not change what WebFetch reads
  - Index: `https://law.justia.com/constitution/florida/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (403 Cloudflare challenge)
  - WebFetch text 132,664 chars; window 1 ends mid Art. V § 10.
- **Currency:** title line — observed: "AS REVISED IN 1968 AND SUBSEQUENTLY AMENDED"
- **Official status:** Third-party copy; no currency date.
- **Hazard:** WebFetch truncation
- **Hazard:** shell blocked
- **Probe:** Fla. Const. art. I, § 9 → `https://law.justia.com/constitution/florida/` — expect: "No person shall be deprived of life, liberty or property"
- **Evidence (2026-10-16):** WebFetch: YES Art. I § 9; truncated mid Art. V § 10. | Independent check 2026-10-16: WebFetch YES Art. I § 9; truncated mid Art. V § 10 ('Retention; election and ter')
- **Notes:** WebFetch may report the title 'CONSTITUTION OF THE STATE OF FLORIDA' rather than the 'AS REVISED IN 1968…' line.

## C. Court rules

### `fl-rules-appellate-floridabar` — Florida Rules of Appellate Procedure (Florida Bar PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · The Florida Bar (rules adopted by the Supreme Court of Florida) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Full rule set in one PDF, re-published under a new dated filename after each amendment.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www-media.floridabar.org/uploads/2026/09/Appellate-Court-Rules-09-01-26.pdf`
  - Placeholders: Filename changes on every re-publication (e.g. Civil-Procedure-Rules-06-19-25.pdf → …-10-01-26.pdf). The Bar's index page is unreachable by both tools; find the newest PDF by WebSearch 'site:www-media.floridabar.org <rule set> Rules pdf' and prefer the latest date in the filename. Accept only the pamphlet filenames ('<Set>-Rules-MM-DD-YY.pdf' or 'YYYY_NN-MON-<Set>-Rules-M-D-YYYY.pdf'); ignore 'Proposed', 'Publication-Notice' and committee PDFs on the same host.
  - Index: `https://www.floridabar.org/rules/florida-rules-of-court/`
  - Navigation: index page (unreachable: WebFetch CLIENT_ERROR, shell Cloudflare) → newest www-media.floridabar.org/uploads/{yyyy}/{mm}/… PDF; in practice found by WebSearch
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.floridabar.org and www-media.floridabar.org answer robots.txt with a Cloudflare 'Attention Required!' page (403); fetch_doc.py REFUSED
  - WebFetch text stops after Rule 9.110 (112,114 chars); rules 9.120-9.900 are unreachable.
- **Currency:** PDF cover 'NOTE TO USERS' line (Civil, Appellate) or running header date (Criminal) — observed: "Rules on this webpage are current through 434 So.3d 978."
- **Official status:** Florida Bar pamphlet; the Civil and Appellate covers say the rules are current through a WL / So. 3d cite of the last amending opinion and point to the Supreme Court for later amendments.
- **Hazard:** WebFetch extracts only ~100-115K chars of the PDF: later rules are unreachable even with offset
- **Hazard:** script route blocked (Cloudflare)
- **Hazard:** URL changes on each amendment
- **Probe:** Fla. R. App. P. 9.030(a)(2)(A) → `https://www-media.floridabar.org/uploads/2026/09/Appellate-Court-Rules-09-01-26.pdf` — expect: "The supreme court shall review, by appeal: (i) final orders"
- **Evidence (2026-10-16):** WebFetch: Rule 9.030 YES; cover 'current through 434 So.3d 978'; text 112,114 chars, ends after Rule 9.110 notes; TOC lists rules to 9.900. | Independent check 2026-10-16: WebFetch YES Rule 9.030; 'current through 434 So.3d 978'; body ends Rule 9.110; second citation Fla. R. App. P. 9.020 ok

### `fl-rules-civil-floridabar` — Florida Rules of Civil Procedure (Florida Bar PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · The Florida Bar (rules adopted by the Supreme Court of Florida) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Full rule set in one PDF, re-published under a new dated filename after each amendment.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www-media.floridabar.org/uploads/2026/10/Civil-Procedure-Rules-10-01-26.pdf`
  - Placeholders: Filename changes on every re-publication (e.g. Civil-Procedure-Rules-06-19-25.pdf → …-10-01-26.pdf). The Bar's index page is unreachable by both tools; find the newest PDF by WebSearch 'site:www-media.floridabar.org <rule set> Rules pdf' and prefer the latest date in the filename. Accept only the pamphlet filenames ('<Set>-Rules-MM-DD-YY.pdf' or 'YYYY_NN-MON-<Set>-Rules-M-D-YYYY.pdf'); ignore 'Proposed', 'Publication-Notice' and committee PDFs on the same host.
  - Index: `https://www.floridabar.org/rules/florida-rules-of-court/`
  - Navigation: index page (unreachable: WebFetch CLIENT_ERROR, shell Cloudflare) → newest www-media.floridabar.org/uploads/{yyyy}/{mm}/… PDF; in practice found by WebSearch
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.floridabar.org and www-media.floridabar.org answer robots.txt with a Cloudflare 'Attention Required!' page (403); fetch_doc.py REFUSED
  - Rule 1.510 (summary judgment) is beyond what WebFetch extracts; no free official route to it was found.
- **Currency:** PDF cover 'NOTE TO USERS' line (Civil, Appellate) or running header date (Criminal) — observed: "Rules in this pamphlet are current through 2026 WL 2603472."
- **Official status:** Florida Bar pamphlet; the Civil and Appellate covers say the rules are current through a WL / So. 3d cite of the last amending opinion and point to the Supreme Court for later amendments.
- **Hazard:** WebFetch extracts only ~100-115K chars of the PDF: later rules are unreachable even with offset
- **Hazard:** script route blocked (Cloudflare)
- **Hazard:** URL changes on each amendment
- **Probe:** Fla. R. Civ. P. (cover note; Rule 1.510 probe) → `https://www-media.floridabar.org/uploads/2026/10/Civil-Procedure-Rules-10-01-26.pdf` — expect: "Rules in this pamphlet are current through 2026 WL 2603472"
- **Evidence (2026-10-16):** WebFetch: cover 'current through 2026 WL 2603472'; Rule 1.510 NOT PRESENT; window 1 ends in Rule 1.190(f); offset=100000 shows only Rule 1.200 then ends. Shell REFUSED (Cloudflare). | Independent check 2026-10-16: WebFetch: 'Rules in this pamphlet are current through 2026 WL 2603472.'; 1.510 absent; second citation Fla. R. Civ. P. 1.140 ok
- **Notes:** Earlier editions exist at …/uploads/2025/11/Civil-Procedure-Rules-06-19-25.pdf and …/uploads/2024/03/Civil-Procedure-Rules-04-01-24.pdf (WebSearch, not fetched).

### `fl-rules-criminal-floridabar` — Florida Rules of Criminal Procedure (Florida Bar PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · The Florida Bar (rules adopted by the Supreme Court of Florida) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Full rule set in one PDF, re-published under a new dated filename after each amendment.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www-media.floridabar.org/uploads/2026/08/2026_01-JUL-Criminal-Procedure-Rules-7-13-2026-2.pdf`
  - Placeholders: Filename changes on every re-publication (e.g. Civil-Procedure-Rules-06-19-25.pdf → …-10-01-26.pdf). The Bar's index page is unreachable by both tools; find the newest PDF by WebSearch 'site:www-media.floridabar.org <rule set> Rules pdf' and prefer the latest date in the filename. Accept only the pamphlet filenames ('<Set>-Rules-MM-DD-YY.pdf' or 'YYYY_NN-MON-<Set>-Rules-M-D-YYYY.pdf'); ignore 'Proposed', 'Publication-Notice' and committee PDFs on the same host.
  - Index: `https://www.floridabar.org/rules/florida-rules-of-court/`
  - Navigation: index page (unreachable: WebFetch CLIENT_ERROR, shell Cloudflare) → newest www-media.floridabar.org/uploads/{yyyy}/{mm}/… PDF; in practice found by WebSearch
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.floridabar.org and www-media.floridabar.org answer robots.txt with a Cloudflare 'Attention Required!' page (403); fetch_doc.py REFUSED
  - WebFetch text stops in Rule 3.130; 3.191, 3.850 etc. are unreachable.
- **Currency:** PDF cover 'NOTE TO USERS' line (Civil, Appellate) or running header date (Criminal) — observed: "Florida Rules of Criminal Procedure July 13, 2026 (running header)"
- **Official status:** Florida Bar pamphlet; the Civil and Appellate covers say the rules are current through a WL / So. 3d cite of the last amending opinion and point to the Supreme Court for later amendments.
- **Hazard:** WebFetch extracts only ~100-115K chars of the PDF: later rules are unreachable even with offset
- **Hazard:** script route blocked (Cloudflare)
- **Hazard:** URL changes on each amendment
- **Probe:** Fla. R. Crim. P. 3.191 → `https://www-media.floridabar.org/uploads/2026/08/2026_01-JUL-Criminal-Procedure-Rules-7-13-2026-2.pdf` — expect: "Florida Rules of Criminal Procedure July 13, 2026"
- **Evidence (2026-10-16):** WebFetch: Rule 3.191 NOT PRESENT; last body text Rule 3.130(d); text 114,916 chars; TOC lists to 3.996; header 'Florida Rules of Criminal Procedure July 13, 2026'. | Independent check 2026-10-16: WebFetch: header 'Florida Rules of Criminal Procedure July 13, 2026'; 3.191 absent; ends 3.130(d); second citation Fla. R. Crim. P. 3.111 ok
- **Notes:** Probe expect is the running header, not rule text: no criminal rule beyond 3.130 could be read.

### `fl-rules-flcourts` — Supreme Court of Florida — rules and rule-amendment opinions

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Supreme Court of Florida · text: **link-only** · official: official
- **Coverage:** Rule-amendment opinions (In re Amendments to …) and court rules pages.
- **Access:** `link-only` · format html
  - Index: `https://supremecourt.flcourts.gov/`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: supremecourt.flcourts.gov: 'User-agent: * Disallow: /' with Allow only for named search-engine bots
  - WebFetch ROBOTS_DISALLOWED on /case-information/opinions. Rule-amendment opinions are also in fl-sc-fsu-archive (e.g. SC2025-0016 'In Re: Amendments to Florida Rules of Juvenile Procedure').
- **Currency:** n/a
- **Official status:** Court's own site; amendment opinions are the adopting orders.
- **Hazard:** robots disallow for all non-search-engine agents
- **Probe:**  → `https://supremecourt.flcourts.gov/case-information/opinions`
- **Evidence (2026-10-16):** robots.txt 'Disallow: /' for User-agent *; WebFetch ROBOTS_DISALLOWED; fetch_doc.py REFUSED. | Re-confirmed blocked 2026-10-16: WebFetch ROBOTS_DISALLOWED on /case-information/opinions

### `fl-rules-judadmin-floridabar` — Florida Rules of General Practice and Judicial Administration (Florida Bar PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · The Florida Bar (rules adopted by the Supreme Court of Florida) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Full rule set in one PDF, re-published under a new dated filename after each amendment.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www-media.floridabar.org/uploads/2026/08/2027_01-JULY-Florida-Rules-of-General-Practice-and-Judicial-Administration-7-1-2026.pdf`
  - Placeholders: Filename changes on every re-publication (e.g. Civil-Procedure-Rules-06-19-25.pdf → …-10-01-26.pdf). The Bar's index page is unreachable by both tools; find the newest PDF by WebSearch 'site:www-media.floridabar.org <rule set> Rules pdf' and prefer the latest date in the filename. Accept only the pamphlet filenames ('<Set>-Rules-MM-DD-YY.pdf' or 'YYYY_NN-MON-<Set>-Rules-M-D-YYYY.pdf'); ignore 'Proposed', 'Publication-Notice' and committee PDFs on the same host.
  - Index: `https://www.floridabar.org/rules/florida-rules-of-court/`
  - Navigation: index page (unreachable: WebFetch CLIENT_ERROR, shell Cloudflare) → newest www-media.floridabar.org/uploads/{yyyy}/{mm}/… PDF; in practice found by WebSearch
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.floridabar.org and www-media.floridabar.org answer robots.txt with a Cloudflare 'Attention Required!' page (403); fetch_doc.py REFUSED
  - WebFetch body text ends in Rule 2.225(d)(3); 2.420, 2.514, 2.516 appear only in the TOC and are unreachable.
- **Currency:** running page header — observed: "July 1, 2026 Fla. R. Gen. Prac. & Jud. Admin."
- **Official status:** Florida Bar pamphlet; the Civil and Appellate covers say the rules are current through a WL / So. 3d cite of the last amending opinion and point to the Supreme Court for later amendments.
- **Hazard:** WebFetch extracts only ~100-115K chars of the PDF: later rules are unreachable even with offset
- **Hazard:** script route blocked (Cloudflare)
- **Hazard:** URL changes on each amendment
- **Probe:** Fla. R. Gen. Prac. & Jud. Admin. (running header; Rule 2.420 probe) → `https://www-media.floridabar.org/uploads/2026/08/2027_01-JULY-Florida-Rules-of-General-Practice-and-Judicial-Administration-7-1-2026.pdf` — expect: "July 1, 2026 Fla. R. Gen. Prac. & Jud. Admin."
- **Evidence (2026-10-16):** Research: not fetched (budget).  | Independent check 2026-10-16: WebFetch: PDF reads; header 'July 1, 2026 Fla. R. Gen. Prac. & Jud. Admin.'; 2.420 body ABSENT
- **Notes:** Probe expect is the running header: the probe rule 2.420 is beyond the WebFetch window.

## D. Administrative code

### `fl-fac-flrules` — Florida Administrative Code (flrules.org)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Florida Department of State, Administrative Code and Register section · text: **link-only** · official: official
- **Coverage:** Every FAC rule: metadata page (title, department/division, effective date, history notes, notice history since Jan. 6, 2006) plus the rule text as a Word .doc.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.flrules.org/gateway/ruleNo.asp?id={rule}`
  - Placeholders: rule verbatim (61G15-19.001, 62-302.530). Rule TEXT link on that page: https://flrules.org/gateway/readFile.asp?sid=0&tid={tid}&type=1&file={rule}.doc — tid is the id of the latest Final notice and is not derivable; take it from the page's VIEW_RULE link (WebFetch can return the href). Chapter page: https://www.flrules.org/gateway/ChapterHome.asp?Chapter={chapter}.
  - Index: `https://www.flrules.org/`
  - Navigation: ruleNo page (metadata) → VIEW_RULE link → .doc (binary Word; unreadable by both tools)
- **Automation:** WebFetch ok · shell ok · robots: curl got a Cloudflare challenge on flrules.org/robots.txt (www. 301s to bare host); fetch_doc.py's robots check returned ok with no rules
  - Metadata pages read fine by both tools. The rule text is served as a binary Word .doc (33,272 bytes for 61G15-19.001): WebFetch '[binary data]', fetch_doc.py returns OLE bytes. So quote rule text from fl-fac-lii (stale) or not at all; use this page for currency (effective date, history).
- **Currency:** rule page 'Effective Date' and 'History Notes' — observed: "Effective Date: 8/20/2026 (61G15-19.001)"
- **Official status:** flrules.org is the Department of State's FAC/FAR site (s. 120.55, Fla. Stat., from memory); rule pages state the 'Latest version of the final adopted rule presented in Florida Administrative Code (FAC)'.
- **Hazard:** rule text only as binary Word .doc
- **Hazard:** tid in text link not derivable
- **Hazard:** Cloudflare in front of host
- **Probe:** Fla. Admin. Code R. 61G15-19.001 → `https://www.flrules.org/gateway/ruleNo.asp?id=61G15-19.001` — expect: "Rule Title: Grounds for Disciplinary Proceedings"
- **Evidence (2026-10-16):** WebFetch: metadata only, body NOT in page; VIEW_RULE href readFile.asp?…tid=31199582…; effective 8/20/2026; no challenge. fetch_doc.py: 62-302.530 page 'Effective Date: 11/25/2025'. .doc text unreadable by both tools. | Independent check 2026-10-16: WebFetch YES 'Rule Title: Grounds for Disciplinary Proceedings'; 'Effective Date: 8/20/2026'; tid=31199582; second citation Fla. Admin. Code R. 64B8-9.003 ok

### `fl-fac-lii` — Cornell LII — Florida Administrative Code

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** FAC rules as HTML, one page per rule.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/florida/Fla-Admin-Code-Ann-R-{rule_hyphenated}`
  - Placeholders: rule with its dot replaced by a hyphen: 61G15-19.001 → Fla-Admin-Code-Ann-R-61G15-19-001; 62-302.530 → …-R-62-302-530.
  - Index: `https://www.law.cornell.edu/regulations/florida`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay: 10; disallows /search/ and admin paths
- **Currency:** last date in the rule's History note (Notes section), compared with the flrules.org 'Effective Date'; newer amendments also carry 'Amended by Florida Register Volume …' lines, older ones do not (64B8-9.003 ends '9-9-13') — observed: "Amended by Florida Register Volume 49, Number 065, April 4, 2023 effective 4/19/2023"
- **Official status:** Third-party copy; 'State regulations are updated quarterly'.
- **Hazard:** stale: 61G15-19.001 lacks the 3-20-26 technical change and 8-20-26 amendment shown on flrules.org — compare the history note with fl-fac-flrules before quoting
- **Probe:** Fla. Admin. Code R. 61G15-19.001 → `https://www.law.cornell.edu/regulations/florida/Fla-Admin-Code-Ann-R-61G15-19-001` — expect: "(1) Pursuant to Section 471.033(2), F.S., the Board, to the"
- **Evidence (2026-10-16):** WebFetch: YES, last amendment 'effective 4/19/2023'. fetch_doc.py: same body; 62-302.530 page present. | Independent check 2026-10-16: WebFetch YES '(1) Pursuant to Section 471.033(2), F.S.'; 'effective 4/19/2023'; second citation Fla. Admin. Code R. 64B8-9.003 ok

## D. Administrative register

### `fl-far-flrules` — Florida Administrative Register (flrules.org)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Florida Department of State · text: **fetch-and-quote** · official: official
- **Coverage:** Daily issues; year listings back to at least 1999 (search hits); 2026: 202 issues, 2025: 252.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Volume = year − 1974 (Vol. 51 = 2025, Vol. 52 = 2026). Issue page ids (IID) and PDF ids are not derivable. Entire-issue PDF: https://flrules.org/gateway/GotoLink.asp?Goto=BigDocFAW&Para={year}/{docid}/{docid}doc.pdf, which redirects to /Faw/FAWDocuments/FAWVOLUMEFOLDERS{year}/{docid}/{docid}doc.pdf. Individual notices: https://www.flrules.org/gateway/View_notice.asp?id={notice_id} (ids listed on each rule's history table). Observed docid = volume + 2-digit issue number (51247 = Vol. 51 No. 247; 5202 = Vol. 52 No. 2) — try it, but confirm via the issue page.
  - Index: `https://flrules.org/bigDoc/Default.asp?Year={YYYY}`
  - Navigation: year listing ('January 2, 2026 - Vol/No 52/01' …) → View_Faw.asp?IID={iid} → 'Entire Issue' PDF link (or View_Section.asp?Issue={iid}&Section={n})
- **Automation:** WebFetch ok · shell ok · robots: see fl-fac-flrules
  - https://www.flrules.org/Faw/FAWIssues.asp returned HTTP 500. Issue PDFs are long (Vol. 51/247: 27 pp, 165,321 chars) — beyond one WebFetch window; use fetch_doc.py.
- **Currency:** issue date in listing and PDF header — observed: "Florida Administrative Register Volume 51, Number 247, December 23, 2025"
- **Official status:** Department of State's register site; issue PDFs headed 'Florida Administrative Register Volume 51, Number 247'.
- **Hazard:** ids not derivable
- **Hazard:** issue PDFs exceed WebFetch window
- **Hazard:** notice text links are .doc files
- **Hazard:** issue PDFs truncated in WebFetch (Vol. 51/247 cut in Section VI)
- **Probe:** Fla. Admin. Reg. Vol. 51, No. 247 (Dec. 23, 2025) → `https://flrules.org/gateway/GotoLink.asp?Goto=BigDocFAW&Para=2025/51247/51247doc.pdf` — expect: "Florida Administrative Register Volume 51, Number 247, December 23, 2025"
- **Evidence (2026-10-16):** WebFetch: View_Faw.asp?IID=4546 gave the Entire Issue href. fetch_doc.py: PDF 27 pp, 165,321 chars, header as expected; year listing 'All FAR Issues in Year 2026'. | Independent check 2026-10-16: WebFetch YES header Vol. 51 No. 247; truncated in Section VI (as hazard says); second citation Fla. Admin. Reg. Vol. 52, No. 2 (Jan. 5, 2026) ok

## E. Case law

### `fl-opinions-flcourts` — Florida Supreme Court and District Courts of Appeal — official opinion pages

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Florida State Courts System · text: **link-only** · official: unofficial
- **Coverage:** Opinions of the Supreme Court (supremecourt.flcourts.gov) and 1st-6th DCAs ({n}dca.flcourts.gov); media on flcourts-media.flcourts.gov.
- **Access:** `link-only` · format pdf
  - Index: `https://supremecourt.flcourts.gov/case-information/opinions`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: supremecourt., www., 1dca. and flcourts-media.flcourts.gov: 'User-agent: * Disallow: /' with Allow only for named search engines; 2dca-6dca.flcourts.gov: '# Disallow all' 'User-agent: * Disallow: /'
  - WebFetch ROBOTS_DISALLOWED on supremecourt.flcourts.gov/case-information/opinions and 1dca.flcourts.gov/. Never fetch; link only.
- **Currency:** n/a
- **Official status:** Slip opinions ('NOT FINAL UNTIL TIME EXPIRES TO FILE REHEARING MOTION'); So. 3d is the reporter.
- **Hazard:** entire flcourts.gov family disallowed by robots
- **Probe:**  → `https://1dca.flcourts.gov/`
- **Evidence (2026-10-16):** robots.txt Disallow: / on all eight flcourts hosts checked; WebFetch ROBOTS_DISALLOWED (2 URLs); fetch_doc.py REFUSED. | Re-confirmed blocked 2026-10-16: WebFetch ROBOTS_DISALLOWED on https://1dca.flcourts.gov/

### `fl-sc-fsu-archive` — Florida Supreme Court Briefs & Opinions (FSU College of Law)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Florida State University College of Law Research Center (state university) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Selected Supreme Court cases (mainly those with briefs/argument, plus rule-amendment opinions): docket-year listings SC99-SC2026 (2024: ~80 dockets; 2025: ~70; 2026: ~15 so far) and older docket-number ranges. Not every disposition.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://library.law.fsu.edu/Digital-Collections/flsupct/dockets/{docket_dir}/{docket_dir}.html`
  - Placeholders: docket_dir varies: 'SC22-0378' and 'SC19-0087' (upper case, 4-digit seq) for recent years, 'sc05-13' (lower case, unpadded) for 2005; 2-digit year even for SC2022-0378 dockets. Opinion PDF in the same folder: op-{docket_dir lower case}.pdf (op-sc22-0378.pdf). Year listings: dockets/SC{YY}.html for 1999-2023, dockets/SC{YYYY}.html for 2024-2026.
  - Index: `https://library.law.fsu.edu/Digital-Collections/flsupct/index.html`
  - Navigation: index → year listing (dockets/SC23.html or dockets/SC2025.html) → docket page (gives date and So. 3d cite when reported) → op-*.pdf
- **Automation:** WebFetch ok · shell ok · robots: none (404)
- **Currency:** none stated; 2026 listing includes SC26-0718
- **Official status:** State-university library archive of court records; footer 'Not for Commercial Use'; opinion PDFs are the court's slip opinions.
- **Hazard:** selective coverage
- **Hazard:** slip pagination only ("- 2 -")
- **Hazard:** docket-folder case/padding inconsistent
- **Probe:** Loyd v. State, 379 So. 3d 1080 (Fla. 2023), No. SC2022-0378 → `https://library.law.fsu.edu/Digital-Collections/flsupct/dockets/SC22-0378/op-sc22-0378.pdf` — expect: "Markeith Demangzlo Loyd was charged with and convicted of first-degree murder"
- **Evidence (2026-10-16):** WebFetch: YES, complete, slip pagination '- 2 -'. fetch_doc.py: pdf 39 pp, 49,996 chars. Docket page shows 'Citation: 379 So.3d 1080'. | Independent check 2026-10-16: WebFetch YES 'Markeith Demangzlo Loyd was charged with and convicted of first-degree'; '- 2 -'; second citation In re Amendments to Rules Regulating The Florida Bar 4-7.19 & 4-7.20, 410 So. 3d 533 (Fla. 2025), No. SC2025-0018 ok
- **Notes:** Tier-1 classification is a judgment call (state university, not the court); see open_questions.

### `fl-cases-justia` — Justia — Florida case law

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1848-2026; District Courts of Appeal 1957-2026 (aggregate listing; sparse in 1959, 1984-85, 1990, 1998-99); per-court DCA listings incl. Sixth DCA (2025: 1,182 decisions). Includes PCAs as one-line opinions.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/florida/{court-slug}/{year}/{docket-slug}.html`
  - Placeholders: court-slug: supreme-court | first-district-court-of-appeal | second-… | third-… | fourth-… | fifth-… | sixth-district-court-of-appeal. year = decision year. docket-slug = docket number lower-cased as printed: 'SC2022-0378' → sc2022-0378; '4D2024-0558' → 4d2024-0558; '6D23-3822' → 6d23-3822. Older Justia slugs sometimes drop the court prefix (PDF names like 2020-19-0993 for 4D19-0993): if the guess 404s, scan the year listing https://law.justia.com/cases/florida/{court-slug}/{year}/ (500 per page). DCAs differ in docket form: the Third DCA still prints 2-digit-year dockets in 2026 (3D24-2193 → 3d24-2193.html), others use 4-digit years (4D2024-0558).
  - Index: `https://law.justia.com/cases/florida/`
  - Navigation: year listing → decision link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (403 Cloudflare challenge)
  - PDF copies are on cases.justia.com (not a vetted tier-2 host — do not use).
- **Currency:** none
- **Official status:** 'The opinions published on Justia State Caselaw are sourced from individual state court sites.'
- **Hazard:** slip text, no So. 3d pagination
- **Hazard:** docket-slug variants
- **Hazard:** shell blocked
- **Hazard:** coverage lag: on 2026-10-16 the newest Third DCA 2026 entry was Aug. 14, 2026 (~2 months behind)
- **Probe:** Loyd v. State, No. SC2022-0378 (Fla. Nov. 16, 2023) → `https://law.justia.com/cases/florida/supreme-court/2023/sc2022-0378.html` — expect: "PER CURIAM. Markeith Demangzlo Loyd was charged with and convicted of first-degree"
- **Evidence (2026-10-16):** WebFetch: YES, complete with concurrence. Also /fourth-district-court-of-appeal/2025/4d2024-0558.html: PCA 'PER CURIAM. Affirmed.' (Apr. 24, 2025); Sixth DCA 2025 listing '1 - 500 of 1182'. | Independent check 2026-10-16: WebFetch YES 'PER CURIAM. Markeith Demangzlo Loyd was charged'; Nov. 16, 2023; slip pagination only; second citation Key Largo Beautification, Inc. v. Monroe County, No. 3D24-2193 (Fla. 3d DCA Aug. 13, 2026) ok

## F. Subsequent history

### `fl-docket-acis` — ACIS — Florida appellate courts online docket

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Florida State Courts System · text: **link-only** · official: official
- **Coverage:** Dockets of the Supreme Court and DCAs, including orders accepting or declining discretionary (conflict) review.
- **Access:** `link-only` · format html
  - Index: `https://acis.flcourts.gov/`
- **Automation:** WebFetch fail · shell http-error · robots: /robots.txt returns the SPA's index.html (no robots rules)
  - JavaScript single-page app: WebFetch sees only 'this application doesn't work properly without JavaScript'; fetch_doc.py gets 200 with 0 text chars. The app bundle calls /api/v1 and includes an /altcha/challenge route (proof-of-work bot check) — not attempted.
- **Currency:** n/a
- **Official status:** The courts' own case-management portal (replaced the older online dockets in 2023, from memory).
- **Hazard:** JS-only
- **Hazard:** bot challenge on API (altcha)
- **Probe:**  → `https://acis.flcourts.gov/`
- **Evidence (2026-10-16):** WebFetch: JS shell, no content. fetch_doc.py info: html, 0 chars. | Independent check 2026-10-16: JS shell only: 'this application doesn't work properly without JavaScript enabled' (row left reported)
- **Notes:** The FSU docket pages link 'Full Docket (ACIS)' for each Supreme Court case.

### `fl-subsequent-history-justia` — Supreme Court of Florida review decisions on Justia (party-name search)

- **Status:** REPORTED 2026-10-16 · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court opinions issued after accepting conflict/certified-question review. Orders declining jurisdiction (the usual outcome) are unpublished orders and not expected here.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/cases/florida/supreme-court/{year}/`
  - Placeholders: Scan the year listing(s) after the DCA decision for the party names; Supreme Court parties keep petitioner/respondent order. Party-name only: no link from the DCA docket.
  - Index: `https://law.justia.com/cases/florida/supreme-court/`
  - Navigation: year listing → party name → opinion (cites the DCA decision)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (403 Cloudflare)
- **Currency:** none
- **Official status:** See fl-cases-justia.
- **Hazard:** party-name search only
- **Hazard:** declined-review orders absent
- **Probe:**  → `https://law.justia.com/cases/florida/supreme-court/`
- **Evidence (2026-10-16):** Supreme Court index fetched (years 1848-2026) but no DCA→Supreme Court review trail was traced. | Independent check 2026-10-16: Index lists years 1848-2026; 2026 listing href present (row left reported)
- **Notes:** Review route: Art. V, § 3(b)(3), Fla. Const. (express and direct conflict) and Fla. R. App. P. 9.030(a)(2)(A); a PCA without citation is not reviewable for conflict (Jenkins v. State, from memory). The So. 3d tables ('rev. denied, 123 So. 3d 456 (Fla. 2014)') are the usual published trace — not free.

## Not available (do not look for these again)

- **case_law** — Fetchable official opinion pages (Supreme Court and DCAs): All flcourts.gov hosts robots 'Disallow: /' for non-search-engine agents; WebFetch ROBOTS_DISALLOWED. (2026-10-16)
- **case_law** — Public-domain (vendor-neutral) citation format: None in use; Florida cites So. 3d / Fla. L. Weekly / WL. (2026-10-16)
- **case_law** — Free official reporter (So. 3d) pagination: FSU and Justia texts carry slip pagination only ('- 2 -'). (2026-10-16)
- **subsequent_history** — Text-fetchable record of Supreme Court orders declining review: Only in ACIS (JS app with bot challenge) and West tables; Justia/FSU hold opinions only. (2026-10-16)
- **court_rules** — Fetchable copy of later rules (e.g. Fla. R. Civ. P. 1.510, Fla. R. Crim. P. 3.850): Florida Bar PDFs: shell blocked by Cloudflare, WebFetch extracts only the first ~100-115K chars; flcourts.gov robots-disallowed; no Justia/LII/public.law copy found. (2026-10-16)
- **statutes** — Structured bulk statute download (XML/JSON): Online Sunshine download is a Windows installer zip (FLLawDL2026.zip); flsenate robots disallow /api/. (2026-10-16)
- **admin_code** — Machine-readable official FAC rule text: flrules.org serves rule text only as binary Word .doc files. (2026-10-16)
- **court_rules** — Fetchable text of Fla. R. Gen. Prac. & Jud. Admin. 2.420, 2.514, 2.516: Bar PDF reachable by WebFetch only to Rule 2.225(d)(3); shell blocked by Cloudflare; flcourts.gov robots-disallowed. (2026-10-16)

## Corpus candidates (maintainers)

- `fl-rules-civil-floridabar` — WebFetch stops in Rule 1.190(f) (offset window reaches only Rule 1.200); shell blocked by Cloudflare, so ingest needs a manual/offline copy
- `fl-rules-appellate-floridabar` — WebFetch text ends after Rule 9.110 (112,114 chars) of rules through 9.900; shell blocked
- `fl-rules-criminal-floridabar` — WebFetch text ends in Rule 3.130 of rules through 3.996; shell blocked
- `fl-constitution-flsenate` — single 420K-char page; WebFetch extracts 133K and cannot reach Articles VI-XII; fetch_doc.py reads it all
- `fl-rules-judadmin-floridabar` — WebFetch body text ends in Rule 2.225(d)(3); 2.420/2.514/2.516 unreachable; shell blocked

## Open questions

- Florida Bar rule PDFs: is there any route the shell may use (the Bar answers robots.txt with a Cloudflare 403)? Without one, corpus ingest of the rules cannot fetch the official file.
- Is the FSU College of Law archive acceptable as tier 1 (state university, not the court)? It is the only fetchable host serving Supreme Court slip-opinion PDFs.
- Subsequent history: no free fetchable source for orders declining conflict review (ACIS is JS + altcha). Confirm whether Justia's Supreme Court listing includes any jurisdiction-declined orders.
- Laws of Florida coverage start year on laws.flrules.org not checked.
- schema: automation.shell has no value for a 200 response that is an empty JavaScript shell (used 'http-error' for ACIS).
- Family Law, Small Claims, Juvenile, Probate rules and Rules Regulating The Florida Bar not probed.
- flsenate.gov year range before 2015 not confirmed.
