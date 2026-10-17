# Kansas (KS) — free legal sources

_Generated from `data/ks.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: kslegislature.gov serves one K.S.A. section per constructible URL ('2026 Kansas Statutes', script and WebFetch ok); ksrevisor.gov has the same text plus long annotations; Justia is the tier-2 fallback (script bot-walled, WebFetch ok). Constitution: ksrevisor.gov per-section pages. Court rules: kscourts.gov per-rule PDFs (index-anchored) and the 712-page 2026 rulebook; civil procedure and evidence are K.S.A. chapter 60. Case law: searchdro.kscourts.gov slip-opinion PDFs (GUID URLs, located via list pages; script ok, WebFetch gated), official pagination and petition-for-review dispositions in the advance-sheet PDFs (2024-2026 only); Justia constructible by docket. K.A.R. and Kansas Register moved to the JavaScript app rules.ks.gov (unreadable); LII mirrors K.A.R.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Kansas | `kan (unverified)` | Kan. | Kan., P.3d, P.2d, P. | — |
| Court of Appeals of Kansas | `kanctapp (unverified)` | Kan. Ct. App. | Kan. App. 2d, Kan. App., P.3d, P.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Kansas Statutes Annotated (K.S.A.) | `K.S.A. 60-513`; `K.S.A. 2023 Supp. 60-513`; `Kan. Stat. Ann. § 60-513`; `K.S.A. 60-513(a)(4)`; `K.S.A. 79-32,117`; `K.S.A. 60-513a`; `K.S.A. 82a-701`; `K.S.A. 60-212(b)(6)`; `K.S.A. 60-456`; `K.S.A. 2024 Supp. 21-6804`; `Kan. Stat. Ann. § 21-5402 (2024)`; `K.S.A. 60-2101(b)`; `section 60-513 of the Kansas Statutes Annotated` | `ks-ksa-legislature` → `ks-ksa-revisor` → `ks-ksa-justia` |
| Kansas Constitution | `Kan. Const. art. 3, § 1`; `Kan. Const. Bill of Rights, § 5`; `Kan. Const. art. 11, § 1(a)`; `Article 3, Section 1 of the Kansas Constitution`; `Section 5 of the Kansas Constitution Bill of Rights`; `section 18 of the Kansas Constitution Bill of Rights`; `Section 18 of the Bill of Rights of the Kansas Constitution` | `ks-constitution-revisor` → `ks-constitution-justia` |
| Kansas Supreme Court Rules (marked) | `Kan. Sup. Ct. R. 6.02`; `Kan. S. Ct. R. 8.03`; `Kansas Supreme Court Rule 7.04`; `Supreme Court Rule 6.02(a)(5) (2024 Kan. S. Ct. R. at 36)`; `Rule 7.04 (2025 Kan. S. Ct. R. at 46)`; `KRPC 1.7`; `Kan. R. Prof'l Conduct 1.7`; `Kansas Rule of Professional Conduct 8.4`; `Rule 240, KRPC 1.7`; `Supreme Court Rule 7.041A (2026 Kan. S. Ct. R. at 50)`; `Kan. Sup. Ct. R. 7.041` | `ks-rules-kscourts` → `ks-rulebook-kscourts` |
| Kansas Supreme Court Rules (bare 'Supreme Court Rule 6.02', 'Rule 7.04') *(only once this jurisdiction is known)* | `Supreme Court Rule 7.04`; `Rule 6.02(a)(5)`; `Rule 8.03(b)`; `Supreme Court Rule 240`; `Rule 7.041A` | `ks-rules-kscourts` → `ks-rulebook-kscourts` |
| Kansas Administrative Regulations (K.A.R.) | `K.A.R. 28-1-2`; `Kan. Admin. Regs. § 28-1-2`; `K.A.R. 30-5-58`; `K.A.R. 2023 Supp. 28-1-2` | `ks-kar-rules` → `ks-kar-lii` |
| Kansas Register | `44 Kan. Reg. 1234`; `Kansas Register Volume 37, No. 17`; `43 Kan. Reg. 765 (July 4, 2024)` | `ks-register-rules` |
| Kansas Reports / Kansas Court of Appeals Reports | `Hilburn v. Enerpipe Ltd., 309 Kan. 1127, 442 P.3d 509 (2019)`; `65 Kan. App. 2d 756`; `Gould v. Crawley, 65 Kan. App. 2d 814`; `309 Kan. 1127, 1133` | `ks-advance-sheets-kscourts` → `ks-opinions-kscourts` → `ks-cases-justia` |
| Pacific Reporter with Kansas parenthetical | `442 P.3d 509 (Kan. 2019)`; `500 P.3d 100 (Kan. Ct. App. 2022)`; `525 P.3d 1, 5 (Kan. App. 2023)` | `ks-cases-justia` → `ks-opinions-kscourts` |
| Unpublished Kansas opinions (WL with Kan. parenthetical) | `State v. Yeargin-Charles, No. 125,754, 2024 WL 3548780 (Kan. App. 2024) (unpublished opinion)`; `2024 WL 4718465 (Kan. App. 2024)` | `ks-cases-justia` → `ks-opinions-kscourts` |
| Kansas appellate docket number (No. 127,715) *(only once this jurisdiction is known)* | `No. 127,715`; `No. 125,754` | `ks-opinions-kscourts` → `ks-cases-justia` → `ks-review-dispositions-advance-sheets` |
| Pacific Reporter (no state marker) *(only once this jurisdiction is known)* | `442 P.3d 509` | `ks-cases-justia` |
| Kansas petition for review disposition (rev. denied ... Kan. ...) | `rev. denied 317 Kan. 846 (2023)`; `rev. granted 321 Kan. 12 (2025)` | `ks-review-dispositions-advance-sheets` |
| Petition for review (generic phrase) *(only once this jurisdiction is known)* | `petition for review denied`; `review granted` | `ks-review-dispositions-advance-sheets` → `ks-appellate-records-ecourt` |

Regexes (case-insensitive):

- Kansas Statutes Annotated (K.S.A.): `(?:K\.\s?S\.\s?A\.|Kan\.\s*Stat\.\s*Ann\.)\s*(?:§+\s*)?(?:(?P<supp>\d{4})\s+Supp\.\s*)?(?:§+\s*)?(?P<chapter>\d{1,2}[a-z]?)-(?P<section>\d{1,4}(?:,\d{1,3})?[a-z]{0,2})(?![\d-])|(?:§+|sec(?:tion)?\.?)\s*(?P<chapter2>\d{1,2}[a-z]?)-(?P<section2>\d{1,4}(?:,\d{1,3})?[a-z]{0,2})(?:\([0-9a-z]+\))*\s+of\s+the\s+Kansas\s+Statutes`
- Kansas Constitution: `Kan\.\s*Const\.\s*(?:art\.\s*(?P<article>\d{1,2}),?\s*§+\s*(?P<section>\d{1,3}[a-z]?)|Bill\s+of\s+Rights,?\s*§+\s*(?P<bor>\d{1,2}))|Article\s+(?P<article2>\d{1,2}),?\s+(?:Section|§)\s*(?P<section2>\d{1,3}[a-z]?)\s+of\s+the\s+Kansas\s+Constitution|(?:Section|§)\s*(?P<bor2>\d{1,2})\s+of\s+the\s+Kansas\s+Constitution\s+Bill\s+of\s+Rights|(?:Section|§)\s*(?P<bor3>\d{1,2})\s+of\s+the\s+Bill\s+of\s+Rights\s+of\s+the\s+Kansas\s+Constitution`
- Kansas Supreme Court Rules (marked): `(?:\bKan\.\s*(?:Sup|S)\.\s*Ct\.\s*R(?:ule)?\.?|\bKansas\s+Supreme\s+Court\s+Rule)\s*(?P<rule>\d{1,4}(?:\.\d{1,3})?[A-Z]?)(?![\d.]?\d)|(?:Supreme\s+Court\s+)?Rule\s+(?P<rule2>\d{1,4}(?:\.\d{1,3})?[A-Z]?)(?:\([0-9a-zA-Z]+\))*\s*\(\d{4}\s+Kan\.\s*S\.\s*Ct\.\s*R\.|(?:KRPC|Kan\.\s*R\.\s*Prof'?l\s*Conduct|\bKansas\s+Rules?\s+of\s+Professional\s+Conduct)\s*(?P<krpc>\d\.\d{1,2}[a-z]?)`
- Kansas Supreme Court Rules (bare 'Supreme Court Rule 6.02', 'Rule 7.04'): `(?:Supreme\s+Court\s+)?Rule\s+(?P<rule>\d{1,2}\.\d{2,3}[A-Z]?|\d{3}[A-Z]?)(?!\d)`
- Kansas Administrative Regulations (K.A.R.): `(?:K\.\s?A\.\s?R\.|Kan\.\s*Admin\.\s*Regs?\.)\s*(?:§+\s*)?(?:\d{4}\s+Supp\.\s*)?(?P<agency>\d{1,3})-(?P<article>\d{1,3})-(?P<section>\d{1,4}[a-z]?)`
- Kansas Register: `(?P<volume>\d{1,2})\s+Kan\.\s*Reg\.\s*(?P<page>\d{1,5})|Kansas\s+Register,?\s+Vol(?:ume|\.)\s*(?P<volume2>\d{1,2}),?\s*No\.\s*(?P<issue>\d{1,2})`
- Kansas Reports / Kansas Court of Appeals Reports: `(?<!\d)(?P<volume>\d{1,3})\s+Kan\.(?:\s*App\.\s*(?P<series>2d)?)?\s+(?P<page>\d{1,4})(?!\d)`
- Pacific Reporter with Kansas parenthetical: `(?P<volume>\d{1,4})\s+P\.\s*(?:(?P<series>[23])d\s+)?(?P<page>\d{1,5})(?:,\s*\d+(?:[-–]\d+)?)?\s*\(Kan\.(?:\s*(?:Ct\.\s*)?App\.)?\s*(?P<year>\d{4})\)`
- Unpublished Kansas opinions (WL with Kan. parenthetical): `(?P<year>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Kan\.`
- Kansas appellate docket number (No. 127,715): `No\.\s*(?P<docket>\d{2,3},\d{3})(?!\d)`
- Pacific Reporter (no state marker): `(?P<volume>\d{1,4})\s+P\.\s*(?:(?P<series>[23])d\s+)?(?P<page>\d{1,5})(?!\d)`
- Kansas petition for review disposition (rev. denied ... Kan. ...): `rev\.\s*(?P<disposition>denied|granted)\s+(?P<volume>\d{1,3})\s+Kan\.\s+(?P<page>\d{1,4})`
- Petition for review (generic phrase): `(?:petition\s+for\s+)?review\s+(?:denied|granted)`

Short forms → URL key:

K.S.A. → `KSA`; Kan. Stat. Ann. → `KSA`; Kan. Stat. → `KSA`; Kansas Statutes Annotated → `KSA`; K.A.R. → `KAR`; Kan. Admin. Regs. → `KAR`; Kan. Admin. Reg. → `KAR`; Kan. Sup. Ct. R. → `SCR`; Kan. S. Ct. R. → `SCR`; Kansas Supreme Court Rule → `SCR`; KRPC → `SCR 240`; Kan. R. Prof'l Conduct → `SCR 240`; Kan. Const. → `CONST`; Kan. Reg. → `KANREG`

Kansas style cites statutes as 'K.S.A. 60-513' (no section sign) and supplements as 'K.S.A. 2023 Supp. 60-513'; Bluebook uses 'Kan. Stat. Ann. § 60-513'. Section numbers may carry a comma (79-32,117: article 32, section 117) or letters (60-513a, chapter 82a); see pattern_rules for the URL split. Rules of civil procedure (K.S.A. 60-201 et seq.) and evidence (K.S.A. 60-401 et seq.) are statutes and route to the K.S.A. rows. Supreme Court rules are cited 'Supreme Court Rule 6.02(a)(5) (2024 Kan. S. Ct. R. at 36)'; bare 'Supreme Court Rule N' / 'Rule 6.02' is shared with other states (Illinois, Missouri) so it is context_required, while the '(YYYY Kan. S. Ct. R. at N)' parenthetical, 'Kan. Sup. Ct. R.' and 'KRPC' are distinctive. Rule 6.08 (not 6.02) governs citation form; Rule 7.04 governs unpublished opinions; Rule 8.03 petitions for review; KRPC is Rule 240. Constitution articles are arabic ('art. 3, § 1') and the Bill of Rights is cited separately. Kansas cites cases 'Hilburn v. Enerpipe Ltd., 309 Kan. 1127, 442 P.3d 509 (2019)' and history 'rev. denied 317 Kan. 846 (2023)'; unpublished: 'No. 125,754, 2024 WL 3548780 (Kan. App. 2024) (unpublished opinion)'. Docket numbers are shared by both courts and written with a comma (context_required). No public-domain citation. CourtListener ids from memory, unverified. Supreme Court rules can have three decimals and a letter (7.041, 7.041A, 7.042, 7.043): capture the full number; 7.041 is not 7.04. A WL cite that also carries 'No. 127,524' matches the context_required docket pattern too; route by the WL pattern. Marked rule pattern anchors 'Kansas' with \b so 'Arkansas Supreme Court Rule …' does not route here (2026-10-17).

## A. Statutes / code

### `ks-ksa-legislature` — Kansas Statutes (K.S.A.) on the Kansas Legislature site

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kansas Office of Revisor of Statutes / Kansas Legislature · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All K.S.A. chapters (1-84 plus lettered chapters), current text with history line; sidebar lists bills affecting the section. Constitution chapters 092/093 are not linked from the chapter list.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://kslegislature.gov/b2025_26/laws/{chapter}_000_0000_chapter/{chapter}_{article}_0000_article/{chapter}_{article}_{section}_section/{chapter}_{article}_{section}_k/`
  - Placeholders: {chapter} = K.S.A. chapter zero-padded to 3 digits, keeping any letter suffix (60 -> 060, 8 -> 008, 82a -> 082a). Split the part after the hyphen into article and section: if it contains a comma ('79-32,117', '40-2,105') the article is before the comma and the section after it; otherwise the section is the LAST TWO DIGITS and the article is everything before them (513 -> art 5 / sec 13; 5402 -> 54 / 02; 1567 -> 15 / 67; 2101 -> 21 / 01). {article} = article zero-padded to 3 digits; {section} = section zero-padded to 4 digits plus any trailing letter(s) (60-513a -> 0013a). Drop subsections '(a)(4)' and the 'YYYY Supp.' edition marker before building. Verified: 60-513 -> 060_005_0013, 21-5402 -> 021_054_0002, 79-32,117 -> 079_032_0117, 60-513a -> 060_005_0013a, 82a-701 -> 082a_007_0001. The biennium segment (b2025_26) only changes the bills sidebar: b2023_24 still serves the 2026 text, so there is no historical version by path. The old /li/b2025_26/statute/... path redirects here. Section PDF: https://kslegislature.gov/media/statute/{chapter}_000_0000_chapter/{chapter}_{article}_0000_article/{chapter}_{article}_{section}_section/{chapter}_{article}_{section}_k.pdf (linked from the page; not probed). Article index: .../{chapter}_{article}_0000_article/ lists 'NN-NNN - title' for every section.
  - Index: `https://kslegislature.gov/b2025_26/laws/`
- **Automation:** WebFetch ok · shell ok · robots: none (404 at https://kslegislature.gov/robots.txt)
  - Pages are ~4-9K chars of text including a long site menu; statute body follows the 'Prev Article N. - TITLE Next' line and ends at 'History:'. The bill sidebar ('Measures Affecting This Section') precedes the body and quotes bill titles: do not quote it as statute text.
- **Currency:** heading above the body on every section page; footer shows data refresh time — observed: "2026 Kansas Statutes"
- **Official status:** Revisor FAQ (https://www.ksrevisor.gov/questions.html): 'An unofficial version of the K.S.A. is available online'; the official set is the printed K.S.A. and cumulative supplements distributed by the Secretary of State (K.S.A. 77-138).
- **Hazard:** unofficial online text: cite the K.S.A. volume or 'K.S.A. YYYY Supp.' edition, not the web page
- **Hazard:** bill sidebar ('Measures Affecting This Section', including bills only 'As Introduced') sits above the statute body
- **Hazard:** biennium path segment does not select a historical statute version
- **Hazard:** comma-numbered sections (79-32,117) and lettered chapters/sections (82a-701, 60-513a) need the pattern_rules split
- **Probe:** K.S.A. 60-513 → `https://kslegislature.gov/b2025_26/laws/060_000_0000_chapter/060_005_0000_article/060_005_0013_section/060_005_0013_k/` — expect: "60-513. Actions limited to two years. (a) The following actions shall be brought within two years"
- **Evidence (2026-10-17):** fetch_doc.py --research: 200 html 8,664 chars, '2026 Kansas Statutes', '60-513. Actions limited to two years.' through 'History: L. 1963, ch. 303'. Second citations: K.S.A. 21-5402 (8,956 chars, '21-5402. Murder in the first degree.'), 79-32,117 (079_032_0117), 60-513a, 82a-701 all ok. WebFetch on 60-513: YES, body (a)-(e) and History, not truncated. | Independent check 2026-10-17: Script and WebFetch: '60-513. Actions limited to two years. (a)...'; '2026 Kansas Statutes'; not truncated; second citation K.S.A. 8-1567 ok
- **Notes:** Search box accepts statute numbers but runs client-side; use the constructible URL.

### `ks-ksa-revisor` — Kansas Statutes Annotated (Revisor of Statutes site)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kansas Office of Revisor of Statutes · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All K.S.A. sections, with history, Revisor's notes, cross references, research and practice aids, law review articles and case annotations on the same page.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.ksrevisor.gov/statutes/chapters/ch{chapter_bare}/{chapter}_{article}_{section}.html`
  - Placeholders: {chapter} = K.S.A. chapter zero-padded to 3 digits, keeping any letter suffix (60 -> 060, 8 -> 008, 82a -> 082a). Split the part after the hyphen into article and section: if it contains a comma ('79-32,117', '40-2,105') the article is before the comma and the section after it; otherwise the section is the LAST TWO DIGITS and the article is everything before them (513 -> art 5 / sec 13; 5402 -> 54 / 02; 1567 -> 15 / 67; 2101 -> 21 / 01). {article} = article zero-padded to 3 digits; {section} = section zero-padded to 4 digits plus any trailing letter(s) (60-513a -> 0013a). Drop subsections '(a)(4)' and the 'YYYY Supp.' edition marker before building. Verified: 60-513 -> 060_005_0013, 21-5402 -> 021_054_0002, 79-32,117 -> 079_032_0117, 60-513a -> 060_005_0013a, 82a-701 -> 082a_007_0001. {chapter_bare} = chapter number without padding (ch60, ch8, ch82a). Chapter index https://www.ksrevisor.gov/statutes/ksa_ch{chapter_bare}.html links every section but its link text is the section TITLE only (no numbers); the numbers are in the URLs.
  - Index: `https://www.ksrevisor.gov/ksa.html`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: Disallow only /images/, /cgi-bin/, /err/, /css/, /sjtest/, /scripts/ for *; statute paths allowed
  - Heavily annotated sections are long (60-513: 105,961 chars) and WebFetch cut it mid-annotation (entry 376). Use fetch_doc.py; the statute text comes first, so quotes from the body are safe in both routes.
- **Currency:** none stated on section pages — observed: "none stated; footer 'www.ksrevisor.gov 2026' only"
- **Official status:** Revisor FAQ (https://www.ksrevisor.gov/questions.html): 'An unofficial version of the K.S.A. is available online.'
- **Hazard:** case annotations and law-review lists follow the statute text: stop quoting at 'History:'
- **Hazard:** long annotated pages truncated by WebFetch (60-513 cut at annotation 376)
- **Hazard:** no currency statement; prefer ks-ksa-legislature for the '2026 Kansas Statutes' edition string
- **Hazard:** unofficial online text
- **Probe:** K.S.A. 21-5402 → `https://www.ksrevisor.gov/statutes/chapters/ch21/021_054_0002.html` — expect: "21-5402. Murder in the first degree. (a) Murder in the first degree is the killing"
- **Evidence (2026-10-17):** fetch_doc.py --research: 21-5402 page 11,552 chars, '21-5402. Murder in the first degree.'; 60-513 (060_005_0013.html) 105,961 chars incl. annotations; 79-32,117, 60-513a, 82a-701 ok. WebFetch on 60-513: body YES, 'Truncated: Yes ... ends mid-entry at annotation 376'. | Independent check 2026-10-17: Script: '21-5402. Murder in the first degree. (a) Murder in the first degree is the killing'; WebFetch YES, not truncated (short page); second citation K.S.A. 44-510e ok
- **Notes:** Same Revisor also publishes the Constitution (ks-constitution-revisor). Composite lists of 2026 new/amended/repealed sections: https://www.ksrevisor.gov/rpts/2026NewAmendsAndRepealsKSAOrder.pdf.

### `ks-session-laws-sos` — Session Laws of Kansas (chapter list linking enrolled bills)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kansas Secretary of State · text: **fetch-and-quote** · official: unknown
- **Coverage:** Current-year session laws by chapter ('Chapter 4: House Bill 2274'), each linked to an sos.ks.gov HTML page holding the session-law text; the index also links the printed volumes as PDFs (2026-Session-Laws-Book-1.pdf, ch. 1-124; Book-2.pdf, ch. 125-166 and indices).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Index: `https://www.sos.ks.gov/publications/session-laws.html`
  - Navigation: session-laws page -> 'Chapter N: House/Senate Bill NNNN' link -> sos.ks.gov HTML chapter page (e.g. /publications/sessionlaws/2026/Chapter-04-HB-2274.html) with the text 'CHAPTER 4 House Bill No. 2274 An Act concerning ...'. Printed Volume 1/2 PDFs are linked from the same index (not probed). Always follow links; do not build chapter-page names.
- **Automation:** WebFetch untested · shell ok · robots: sos.ks.gov disallows /index.html, /ent/, /api/, /eforms/BusinessEntity/Search.aspx, /CM_ServiceWM/displaydocuments.aspx for *; /publications/ allowed. kslegislature.gov: none (404)
  - sos.ks.gov returned 403 to the script on /publications/pubs_kar.aspx (that URL refused for the day); the .html publication pages read fine. Earlier the chapter links pointed to kslegislature.gov enrolled-bill PDFs (hb2347_enrolled.pdf read ok); the independent check found sos.ks.gov HTML chapter pages instead.
- **Currency:** page heading — observed: "2026 Session Laws of Kansas"
- **Official status:** Session-laws index on sos.ks.gov describes the Session Laws as containing all acts passed each session; chapter pages are the SOS's HTML rendering, and the printed volumes are linked as PDFs. No statement that the HTML is official.
- **Hazard:** HTML chapter page, not the printed volume page: cite 'L. 2026, ch. N, § M'; printed Volume 1/2 PDFs (unprobed) carry the volume pagination
- **Hazard:** chapter links changed during this research (enrolled-bill PDFs on 2026-10-17 morning, sos.ks.gov HTML pages by the independent check): follow the index links
- **Probe:** L. 2026, ch. 4 (HB 2274) → `https://www.sos.ks.gov/publications/session-laws.html` — expect: "2026 Session Laws of Kansas"
- **Evidence (2026-10-17):** fetch_doc.py --research: session-laws.html 30,175 chars, '2026 Session Laws of Kansas'; Chapter 2 link -> hb2347_enrolled.pdf, 12 pages, 43,498 chars. | Independent check 2026-10-17: Script: '2026 Session Laws of Kansas' present; 'Chapter 4: House Bill 2274' links an sos.ks.gov HTML page; second citation L. 2026, ch. 4 (HB 2274) ok

### `ks-ksa-justia` — Kansas Statutes on Justia

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** K.S.A. by chapter/article/section; annual editions.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/kansas/chapter-{chapter}/article-{article}/section-{chapter}-{rest}/`
  - Placeholders: {chapter} as cited (60, 82a); {article} unpadded article number from the K.S.A. split (60-513 -> 5); {rest} = the cited part after the hyphen (513). Comma sections untested.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: fetch_doc.py: law.justia.com refused (robots.txt challenge) earlier on 2026-10-17; host off for the day
  - Bot wall for the script; WebFetch reads it (policy: fetch-tool route allowed for challenge hosts).
- **Currency:** page heading — observed: "2025 Kansas Statutes"
- **Official status:** Justia page disclaimer: 'These codes may not be the most recent version.'
- **Hazard:** one edition behind the Legislature site (2025 vs 2026)
- **Hazard:** tier 2: disclose with currency string
- **Probe:** K.S.A. 60-513 → `https://law.justia.com/codes/kansas/chapter-60/article-5/section-60-513/` — expect: "(a) The following actions shall be brought within two years"
- **Evidence (2026-10-17):** WebFetch: YES, first words '(a) The following actions shall be brought within two years:', '2025 Kansas Statutes', not truncated. Script REFUSED (robots.txt challenge, host off for the day). | Independent check 2026-10-17: WebFetch: '(a) The following actions shall be brought within two years:'; '2025 Kansas Statutes'; not truncated; second citation K.S.A. 8-1567 ok
- **Notes:** Only one citation probed on this row (budget); the pattern is the standard Justia codes layout.

## B. Constitution

### `ks-constitution-revisor` — Constitution of the State of Kansas (Revisor of Statutes)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kansas Office of Revisor of Statutes · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Bill of Rights, Articles 1-15, Kansas-Nebraska Act and Ordinance material, amendment lists; one page per section with history and cross references.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.ksrevisor.gov/kanconst/{part}_{article}_{section}.html`
  - Placeholders: Bill of Rights: {part}=092, {article}=001, {section}=section zero-padded to 4 (Bill of Rights § 5 -> 092_001_0005). Articles: {part}=093, {article}=article number zero-padded to 3, {section}=section zero-padded to 4 (art. 3, § 1 -> 093_003_0001; art. 11, § 1 -> 093_011_0001). Lettered sections (art. 15, § 3c) are untested: take the link from https://www.ksrevisor.gov/kanconst.html.
  - Index: `https://www.ksrevisor.gov/kanconst.html`
- **Automation:** WebFetch untested · shell ok · robots: statute/constitution paths allowed (see ks-ksa-revisor)
  - kslegislature.gov serves 092_/093_ paths as a 169-character bare fragment and does not link them from its chapter list; not used.
- **Currency:** none stated — observed: "none stated; each section ends with a History line"
- **Official status:** Published alongside the K.S.A., which the Revisor FAQ calls 'an unofficial version' online; no separate statement for the Constitution.
- **Hazard:** Kansas numbers articles in arabic numerals (art. 3), unlike most states
- **Hazard:** Bill of Rights sections are cited separately from articles
- **Probe:** Kan. Const. Bill of Rights, § 5 → `https://www.ksrevisor.gov/kanconst/092_001_0005.html` — expect: "§ 5. Trial by jury. The right of trial by jury shall be inviolate."
- **Evidence (2026-10-17):** fetch_doc.py --research: 092_001_0005 'BILL OF RIGHTS § 5. Trial by jury.'; second citation art. 3, § 1 (093_003_0001) 'Article 3.—JUDICIAL § 1. Judicial power; seals; rules.'; art. 11, § 1 ok. | Independent check 2026-10-17: Script: 'BILL OF RIGHTS § 5. Trial by jury. The right of trial by jury shall be inviolate.'; second citation Kan. Const. art. 2, § 16 ok

### `ks-constitution-justia` — Kansas Constitution on Justia

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Bill of Rights and each article on one page apiece.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/kansas/{page}.html`
  - Placeholders: {page} = 'rights' for the Bill of Rights; 'art{N}' for Article N (art3). All sections of a part on one page. Verified art2.html for Article 2.
  - Index: `https://law.justia.com/constitution/kansas/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: script refused law.justia.com (robots.txt challenge) 2026-10-17
- **Currency:** disclaimer only — observed: "may not be the most recent version"
- **Official status:** Justia disclaimer: may not be the most recent version; official state website may have more current information.
- **Hazard:** tier 2; no edition date
- **Probe:** Kan. Const. Bill of Rights, § 5 → `https://law.justia.com/constitution/kansas/rights.html` — expect: "The right of trial by jury shall be inviolate."
- **Evidence (2026-10-17):** WebFetch: index lists rights.html and art3.html; rights.html YES, § 5 text present, §§ 1-20 on one page. | Independent check 2026-10-17: WebFetch: § 5 'The right of trial by jury shall be inviolate.'; disclaimer 'may not be the most recent version'; second citation Kan. Const. art. 2, § 16 ok

## C. Court rules

### `ks-local-rules-kscourts` — District court local rules (index)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kansas Judicial Branch · text: **link-only** · official: unknown
- **Coverage:** Local rules for the 31 judicial districts.
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.kscourts.gov/About-the-Courts/District-Courts/District-Court-Rules`
  - Navigation: index -> 'Nth Judicial District' link -> PDF/DOCX on kscourts.gov (e.g. 02JDLocalRules.pdf) or a county site (shawneecourt.org, franklincoks.org, 5thjd.org). kscourts.gov-hosted PDFs sit under different paths (/media/KsCourts/District%20Court%20Rules/02JDLocalRules.pdf, /media/6_JD/06JDLocalRules.pdf): follow links.
- **Automation:** WebFetch untested · shell ok · robots: kscourts.gov allowed; county hosts not checked
  - Off-host local rules are not on the allowlist: link only.
- **Currency:** none on index — observed: "none stated"
- **Official status:** Index page on kscourts.gov links each judicial district's rules, many hosted by county or district sites.
- **Hazard:** many districts host rules on county websites outside this record
- **Probe:** 2nd Judicial District local rules → `https://www.kscourts.gov/About-the-Courts/District-Courts/District-Court-Rules` — expect: "2nd Judicial District"
- **Evidence (2026-10-17):** fetch_doc.py --research links: '2nd Judicial District' -> kscourts.gov 02JDLocalRules.pdf; 3rd -> shawneecourt.org; 5th -> 5thjd.org .docx. | Independent check 2026-10-17: Script links: '2nd Judicial District' -> 02JDLocalRules.pdf; 3rd shawneecourt.org; 5th 5thjd.org .docx

### `ks-rulebook-kscourts` — Reports of Rules Adopted by the Supreme Court of Kansas, 2026 Edition (Kan. S. Ct. R.)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kansas Supreme Court, Reporter of Decisions · text: **fetch-and-quote** · official: official
- **Coverage:** Every Supreme Court rule with history notes and supplemental orders, amendments through January 1, 2026; the volume Kansas courts cite as 'YYYY Kan. S. Ct. R. at N'.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.kscourts.gov/Rules-Orders/Rules`
  - Navigation: Rules index -> 'Rules Adopted by the Supreme Court (2026 Rulebook in PDF)' -> https://www.kscourts.gov/KSCourts/media/KsCourts/Rules/2026-RuleBook.pdf (filename changes each year).
- **Automation:** WebFetch untested · shell ok · robots: allowed (see ks-rules-kscourts)
  - 712 pages, 1.79M chars: far beyond WebFetch's ~100K; use fetch_doc.py grep/section.
- **Currency:** title page (PDF page 1) — observed: "2026 Edition ... amendments through January 1, 2026"
- **Official status:** Title page: 'Published annually under authority of law by direction of the Supreme Court of Kansas', Sara R. Stratton, Official Reporter.
- **Hazard:** amendments after Jan. 1, 2026 appear only in per-rule PDFs and advance sheets
- **Hazard:** page numbers in 'Kan. S. Ct. R. at N' refer to the printed volume of the cited year
- **Hazard:** PDF text hyphenates words across lines ('guide- lines'): pick verify strings without line-break hyphens
- **Probe:** 2026 Kan. S. Ct. R. → `https://www.kscourts.gov/KSCourts/media/KsCourts/Rules/2026-RuleBook.pdf` — expect: "amendments through January 1, 2026"
- **Evidence (2026-10-17):** fetch_doc.py --research: PDF 712 pages, 1,793,376 chars, Last-Modified 19 Feb 2026; page 1 '2026 Edition', 'amendments through January 1, 2026'. | Independent check 2026-10-17: Script: 712 pp; 'amendments through January 1, 2026'; expect string NOT found verbatim ('guide- lines' hyphenated); second citation Kan. Sup. Ct. R. 8.03 (2026 Kan. S. Ct. R.) ok

### `ks-rules-kscourts` — Rules Adopted by the Supreme Court of Kansas (per-rule pages and PDFs)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kansas Judicial Branch · text: **fetch-and-quote** · official: official
- **Coverage:** All Supreme Court rules: Chapter 1 (appellate procedure 1.01-10.xx), district court rules (100s), discipline (200s, KRPC as Rule 240), admission (700s), judicial conduct (601B), etc. Civil procedure and evidence are STATUTES (K.S.A. 60-201 et seq., 60-401 et seq.): route those to the K.S.A. rows.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.kscourts.gov/Rules-Orders/Rules`
  - Navigation: Rules index lists every rule as 'Rule 6.02: Content of Appellant's Brief' (KRPC as 'Rule 240 1.7: Conflict of Interest: Current Clients') -> title-slug page (/Rules-Orders/Rules/Content-of-Appellant-s-Brief) -> its 'View PDF' link (/KSCourts/media/KsCourts/Rules/Rule-6-02.pdf?ext=.pdf; KRPC: RULE-1-7.pdf) holds the text. Slugs and PDF names are not uniform: always follow links.
- **Automation:** WebFetch gated · shell ok · robots: www.kscourts.gov: 'User-agent: *' with no Disallow (sitemap only)
  - WebFetch on the Rule 7.04 PDF returned PROVENANCE_REQUIRED (permission not answered). Per-rule HTML page holds only the title and 'View PDF'.
- **Currency:** PDF Last-Modified header; history line at end of each rule — observed: "Rule PDFs last-modified 22 May 2025; history '[History: ... Am. effective ...]'"
- **Official status:** Rules are adopted by the Supreme Court and published by the court (Reporter of Decisions); per-rule pages link the adopting order (e.g. 2021-RL-169).
- **Hazard:** text only in the per-rule PDF, not the HTML page
- **Hazard:** PDF names inconsistent (Rule-7-04.pdf vs RULE-1-7.pdf)
- **Hazard:** several index entries share 'Rule 240' (KRPC preamble, scope, each KRPC rule)
- **Probe:** Kan. Sup. Ct. R. 7.04 → `https://www.kscourts.gov/KSCourts/media/KsCourts/Rules/Rule-7-04.pdf?ext=.pdf` — expect: "Rule 7.04 OPINION OF APPELLATE COURT (a) Memorandum or Formal Opinion"
- **Evidence (2026-10-17):** fetch_doc.py --research: Rule-7-04.pdf 2 pages 4,368 chars 'Rule 7.04 OPINION OF APPELLATE COURT'; second citation Rule 6.02 (Rule-6-02.pdf, 1 page) 'Rule 6.02 CONTENT OF APPELLANT'S BRIEF'; KRPC 1.7 page links RULE-1-7.pdf. WebFetch: PROVENANCE_REQUIRED (gated). | Independent check 2026-10-17: Script: Rule-7-04.pdf 2 pp, 'Rule 7.04 OPINION OF APPELLATE COURT (a) Memorandum or Formal Opinion'; second citation Kan. Sup. Ct. R. 8.03 ok
- **Notes:** Case annotations for rules: https://www.kscourts.gov/KSCourts/media/KsCourts/Rules/Case-Annotations.pdf (not probed).

## D. Administrative code

### `ks-kar-rules` — Kansas Administrative Regulations online (rules.ks.gov)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Kansas Secretary of State · text: **link-only** · official: unknown
- **Coverage:** Current permanent and temporary K.A.R.; replaces the old sos.ks.gov pubs_kar.aspx pages.
- **Access:** `search-only` · format html
  - Index: `https://rules.ks.gov/`
  - Navigation: JavaScript application; no static per-regulation URL was observed.
- **Automation:** WebFetch gated · shell unreadable-format · robots: 'User-agent: * / Disallow:' (allow all)
  - fetch_doc.py: 200 with 0 characters of text (client-rendered shell). WebFetch: PROVENANCE_REQUIRED. Old https://sos.ks.gov/publications/pubs_kar.aspx: HTTP 403 to the script.
- **Currency:** not observed — observed: "not observed"
- **Official status:** SOS FAQ (https://sos.ks.gov/publications/publications-faq.html): the most current version of all adopted regulations is in the online K.A.R.; searchable by agency, article, number or keyword.
- **Hazard:** JavaScript-only application
- **Hazard:** no constructible per-regulation URL found
- **Probe:** K.A.R. 28-1-2 → `https://rules.ks.gov/` — expect: "28-1-2"
- **Evidence (2026-10-17):** Linked from https://sos.ks.gov/publications/kansas-administrative-regulations.html ('Kansas Administrative Regulations' -> https://rules.ks.gov/). fetch_doc.py: 200, 0 chars; WebFetch gated. Body text never seen.
- **Notes:** Use ks-kar-lii for text; link rules.ks.gov as the official source.

### `ks-kar-lii` — Kansas Administrative Regulations on Cornell LII

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute (Cornell) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** K.A.R. by agency/article/regulation with authority and history notes.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/kansas/K-A-R-{agency}-{article}-{section}`
  - Placeholders: K.A.R. 28-1-2 -> K-A-R-28-1-2 (numbers as cited, unpadded). Article index: /regulations/kansas/agency-{agency}/article-{article}. Lettered sections work as cited (K.A.R. 117-2-2a -> K-A-R-117-2-2a).
  - Index: `https://www.law.cornell.edu/regulations/kansas`
- **Automation:** WebFetch untested · shell ok · robots: fetch_doc.py check passed (robots permits)
- **Currency:** history note at end of regulation; HTTP Last-Modified — observed: "updated quarterly; 28-1-2 page Last-Modified 02 Aug 2025"
- **Official status:** Third-party compilation; LII notes 'State regulations are updated quarterly'.
- **Hazard:** may lag the official online K.A.R. by months
- **Hazard:** tier 2: disclose currency
- **Probe:** K.A.R. 28-1-2 → `https://www.law.cornell.edu/regulations/kansas/K-A-R-28-1-2` — expect: "Reporting requirements for infectious or contagious diseases and conditions"
- **Evidence (2026-10-17):** fetch_doc.py --research: 10,665 chars, 'Kan. Admin. Regs. § 28-1-2 - Reporting requirements for infectious or contagious diseases', history 'Kansas Register Volume 37, No. 17; effective 5/11/2018'; second citation K.A.R. 30-5-58 ('Definitions') ok. | Independent check 2026-10-17: Script: 'Kan. Admin. Regs. § 28-1-2 - Reporting requirements for infectious or contagious diseases'; second citation K.A.R. 117-2-2a ok

## D. Administrative register

### `ks-register-rules` — Kansas Register (current, on rules.ks.gov)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Kansas Secretary of State · text: **link-only** · official: official
- **Coverage:** Weekly Register: new regulations, notices, laws effective on publication.
- **Access:** `search-only` · format html
  - Index: `https://rules.ks.gov/`
  - Navigation: https://www.sos.ks.gov/publications/kansas-register.html links only to rules.ks.gov ('link to new K.A.R. and Kansas register page'); JavaScript application.
- **Automation:** WebFetch gated · shell unreadable-format · robots: allow all
  - Same JS app as ks-kar-rules.
- **Currency:** not observed — observed: "not observed"
- **Official status:** SOS FAQ: 'The Kansas Register is the official state newspaper of Kansas'.
- **Hazard:** JavaScript-only application
- **Probe:** Kansas Register → `https://rules.ks.gov/` — expect: "Kansas Register"
- **Evidence (2026-10-17):** kansas-register.html (script ok, 4,968 chars) links to https://rules.ks.gov/; that app returns 0 chars to the script; WebFetch gated.
- **Notes:** Legacy issue pages exist on sos.ks.gov (e.g. https://sos.ks.gov/publications/Register/Volume-43/Issues/Regulation-Index/07-04-24-Index.html, script 200, 19,550 chars) but the current Register page no longer links them; found by web search only.

## E. Case law

### `ks-advance-sheets-kscourts` — Kansas Reports and Kansas Court of Appeals Reports advance sheets

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kansas Supreme Court, Reporter of Decisions · text: **fetch-and-quote** · official: official
- **Coverage:** Supreme Court Kan. vol. 320 No. 1 (Jan.-Feb. 2025) to vol. 322 No. 2 (May-July 2026); Court of Appeals Kan. App. 2d vol. 65 No. 1 (Sept.-Oct. 2024) to vol. 66 No. 5. Includes administrative orders amending rules and the petitions-for-review table.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.kscourts.gov/Cases-Decisions/Advance-Sheets`
  - Navigation: Advance Sheets page -> 'Volume 321, No. 2' link -> PDF under https://www.kscourts.gov/KSCourts/media/KsCourts/advance-sheets/ (SupremeCourtVol{vol}No{n}.pdf or CourtofAppealsVol{vol}No{n}.pdf, but some names carry a '_1' suffix, e.g. SupremeCourtVol320No2_1.pdf, CourtofAppealsVol65No3_1.pdf: ALWAYS take the URL from the link, never build it). Both courts' links have the same text form; tell them apart by volume range (Kan. 320-322 vs Kan. App. 2d 65-66) or the URL prefix. The table of cases near the front gives the starting page.
- **Automation:** WebFetch untested · shell ok · robots: allowed
  - 282-page / 657K-char PDFs: beyond WebFetch; use fetch_doc.py grep for the running heads 'VOL. {vol} SUPREME COURT OF KANSAS {page}' or 'VOL. {vol} COURT OF APPEALS OF KANSAS {page}'.
- **Currency:** Advance Sheets page list — observed: "Volume 322, No. 2 (May – July 2026, PDF)"
- **Official status:** kscourts.gov Cases & Decisions: published decisions are printed in the Kansas Reports / Kansas Court of Appeals Reports, the court's official publication; advance sheets carry that pagination ('VOL. 321 SUPREME COURT OF KANSAS 261').
- **Hazard:** only the most recent volumes are online; older Kan. / Kan. App. 2d volumes are not free on kscourts.gov
- **Hazard:** running heads give the official page: 'VOL. 321 SUPREME COURT OF KANSAS 261' (Kan.) and 'VOL. 66 COURT OF APPEALS OF KANSAS 699' (Kan. App. 2d)
- **Hazard:** PDF filenames are not uniform ('_1' suffix on some issues): never construct them
- **Probe:** 321 Kan. No. 2 advance sheet → `https://www.kscourts.gov/KSCourts/media/KsCourts/advance-sheets/SupremeCourtVol321No2.pdf` — expect: "PETITIONS FOR REVIEW OF DECISIONS OF THE COURT OF APPEALS"
- **Evidence (2026-10-17):** fetch_doc.py --research: SupremeCourtVol321No2.pdf 282 pages, 657,158 chars, Last-Modified 01 Sep 2026; running head 'VOL. 321 SUPREME COURT OF KANSAS 261'. CourtofAppealsVol66No4.pdf 219 pages, 549,165 chars. | Independent check 2026-10-17: Script: SupremeCourtVol321No2.pdf 282 pp, 'PETITIONS FOR REVIEW OF DECISIONS OF THE COURT OF APPEALS 321 Kan. No. 2'; second citation 66 Kan. App. 2d 699 (State v. Garrett) ok

### `ks-opinions-kscourts` — Kansas Supreme Court and Court of Appeals decisions (slip opinions)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kansas Judicial Branch · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Published slip opinions online from October 25, 1996; unpublished from September 4, 2015 (per https://www.kscourts.gov/Cases-Decisions). PDF, slip pagination.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://searchdro.kscourts.gov/Data/decisionsList`
  - Navigation: Recent (about 12 months, back to Oct. 2025 on 2026-10-17): decisionsList page groups by court -> year -> release date, each docket number links its PDF (https://searchdro.kscourts.gov/documents/pdf/caseDecisions/{guid}_{docket}.pdf). Daily release list (PDF): https://searchdro.kscourts.gov/Documents/Released. Older: the search form at https://searchdro.kscourts.gov/Documents/LoadPage (date range, court, published status, keyword) is JavaScript-driven; a plain-GET query was not found. In decisionsList the link text is the docket WITHOUT comma: fetch_doc.py links https://searchdro.kscourts.gov/Data/decisionsList 127524. Each entry is labelled (Published)/(Unpublished); unpublished PDFs say 'NOT DESIGNATED FOR PUBLICATION'.
- **Automation:** WebFetch gated · shell ok · robots: searchdro.kscourts.gov: none (404). Pages carry <meta name=robots content='noindex, nofollow'> (not a robots.txt rule).
  - PDF names contain a GUID: not constructible from the docket. WebFetch on an opinion PDF: PROVENANCE_REQUIRED. A plain curl of LoadPage got a Cloudflare error page; the script was not challenged.
- **Currency:** decisionsList / Released list headings — observed: "KANSAS APPELLATE COURT OPINIONS FILED October 16, 2026"
- **Official status:** Citing Decisions page (https://www.kscourts.gov/Cases-Decisions/Citing-Decisions): Reporter of Decisions makes a final edit before publication in Kansas Reports / Kansas Court of Appeals Reports; Rule 6.08 requires the official citation.
- **Hazard:** slip pagination only; official Kan./Kan. App. 2d pages are in the advance sheets (ks-advance-sheets-kscourts)
- **Hazard:** PDF URL has a GUID, so locate via list pages
- **Hazard:** decisionsList holds only about the last 12 months
- **Hazard:** Cloudflare in front of searchdro (other clients may be challenged)
- **Probe:** Martin v. City of Topeka, No. 127,715 (Kan. 2026) → `https://searchdro.kscourts.gov/documents/pdf/caseDecisions/bc839305-04d5-48c3-851d-ed090456f05c_127715.pdf` — expect: "The public-duty doctrine is a common-law rule limiting when a plaintiff may sue"
- **Evidence (2026-10-17):** fetch_doc.py --research: PDF 25 pages, 49,857 chars, 'IN THE SUPREME COURT OF THE STATE OF KANSAS No. 127,715', syllabus present. decisionsList 222,375 chars (Supreme Court + Court of Appeals, 2026 and 2025). Released list PDF ok. WebFetch: PROVENANCE_REQUIRED (gated). | Independent check 2026-10-17: Script: 25 pp; syllabus 'The public-duty doctrine is a common-law rule limiting when a plaintiff may sue'; second citation State v. Shrout, No. 127,524 (Kan. App. Oct. 16, 2026) (unpublished) ok
- **Notes:** Docket numbers are shared by both courts (e.g. 127,715) and written with a comma in opinions.

### `ks-cases-justia` — Kansas Supreme Court and Court of Appeals opinions on Justia

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Kansas Supreme Court and Court of Appeals opinions by year (published and unpublished; listing does not label which).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/kansas/{court}/{year}/{docket}.html`
  - Placeholders: {court} = supreme-court | court-of-appeals; {year} = decision year; {docket} = docket number without comma (127,715 -> 127715). Year index: https://law.justia.com/cases/kansas/{court}/{year}/. PDF copy on cases.justia.com (linked from the page).
- **Automation:** WebFetch ok · shell blocked-challenge · robots: script refused law.justia.com (robots.txt challenge) 2026-10-17
- **Currency:** none — observed: "(Kan. 2025) in page title; no reporter citation shown"
- **Official status:** Third-party republication of court slip opinions.
- **Hazard:** no official Kan./P.3d page numbers
- **Hazard:** tier 2
- **Probe:** State v. Cunningham, No. 125,865 (Kan. 2025) → `https://law.justia.com/cases/kansas/supreme-court/2025/125865.html` — expect: "A jury convicted Jason Cunningham of eight counts of sexual"
- **Evidence (2026-10-17):** WebFetch: YES, body present, not truncated, PDF link cases.justia.com/kansas/supreme-court/2025-125865.pdf. Year indexes: supreme-court/2025/ (In re Kort 129389.html ...) and court-of-appeals/2025/ (Beltz v. State 127820.html ...). | Independent check 2026-10-17: WebFetch: 'A jury convicted Jason Cunningham of eight counts of sexual misconduct'; not truncated; no reporter cite; second citation State v. Shrout, No. 127,524 (Kan. App. 2026) ok
- **Notes:** Current: the independent check found a Court of Appeals opinion one day after filing (court-of-appeals/2026/127524.html).

## F. Subsequent history

### `ks-appellate-records-ecourt` — Kansas eCourt appellate case records search

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Kansas Judicial Branch · text: **link-only** · official: unknown
- **Coverage:** Appellate docket entries (would show petition-for-review rulings).
- **Access:** `link-only` · format html
  - Index: `https://www.kscourts.gov/eCourt/Search-Appellate-Court-Records`
  - Navigation: Landing page describes eCourt access tiers (public, attorney, justice partner); the public search is a portal application not probed.
- **Automation:** WebFetch untested · shell untested · robots: kscourts.gov allowed
  - Landing page read by script; portal not followed.
- **Currency:** n/a — observed: "n/a"
- **Official status:** Linked from kscourts.gov Cases & Decisions as 'Search Appellate Court Records'.
- **Hazard:** portal application; may need an account for some records
- **Probe:** n/a → `https://www.kscourts.gov/eCourt/Search-Appellate-Court-Records` — expect: "Search Appellate Court Records"
- **Evidence (2026-10-17):** fetch_doc.py read of landing page: 'eCourt Case Management System', access tiers; no docket search reached.

### `ks-review-dispositions-advance-sheets` — Petitions for review of Court of Appeals decisions (table in Kansas Reports advance sheets)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kansas Supreme Court, Reporter of Decisions · text: **fetch-and-quote** · official: official
- **Coverage:** Each advance sheet lists title, Court of Appeals docket number, disposition (Granted/Denied), date and where reported below (Kan. App. 2d cite or 'Unpublished'). Online only for the advance sheets still posted (vol. 320-322).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.kscourts.gov/Cases-Decisions/Advance-Sheets`
  - Navigation: Advance Sheets page -> Supreme Court volume PDF -> fetch_doc.py grep for the Court of Appeals docket number with comma ('127,118') or 'PETITIONS FOR REVIEW OF DECISIONS OF THE COURT OF APPEALS' (table follows the case index; its PDF page varies by issue: p. 32 in 321 No. 2, p. 12 in 322 No. 2). Take the PDF URL from the link (names may carry '_1')..
- **Automation:** WebFetch untested · shell ok · robots: allowed
  - Searchable by docket number, not only party name.
- **Currency:** table heading — observed: "321 Kan. No. 2"
- **Official status:** Printed in the Kansas Reports advance sheet (official reporter); this table is what 'rev. denied 317 Kan. 846 (2023)' cites.
- **Hazard:** older dispositions (before vol. 320) are not online here
- **Hazard:** docket in the table uses a comma (127,118)
- **Probe:** A.S. v. Vineyard Church of Overland Park, 65 Kan. App. 2d 756, rev. granted → `https://www.kscourts.gov/KSCourts/media/KsCourts/advance-sheets/SupremeCourtVol321No2.pdf` — expect: "PETITIONS FOR REVIEW OF DECISIONS OF THE COURT OF APPEALS"
- **Evidence (2026-10-17):** fetch_doc.py --research pages 32-33: table '321 Kan. No. 2'; row 'A.S. v. Vineyard Church of Overland Park 127,118 Granted 10/17/2025 65 Kan. App. 2d 756'. | Independent check 2026-10-17: Script p. 32: 'A.S. v. Vineyard Church of Overland Park ... 127,118 Granted 10/17/2025 65 Kan. App. 2d 756'; second citation Casey v. State, No. 127,729, rev. denied (322 Kan. No. 2) ok
- **Notes:** A Court of Appeals opinion's later history can also show in the Supreme Court opinion itself ('We granted ... petition for review').

## Not available (do not look for these again)

- **case_law** — Free official Kansas Reports / Kansas Court of Appeals Reports volumes older than the posted advance sheets: Advance Sheets page lists only Kan. vols. 320-322 and Kan. App. 2d vols. 65-66; Cases & Decisions page says online slip opinions date to Oct. 25, 1996 (unpublished to Sept. 4, 2015). (2026-10-17)
- **case_law** — Public-domain / vendor-neutral citation format: Citing Decisions page: Rule 6.08 requires the official (Kan./Kan. App. 2d) citation followed by a reporter citation; no paragraph-numbered neutral cite. (2026-10-17)

## Corpus candidates (maintainers)

- `ks-rulebook-kscourts` — 712 pages / 1.79M chars; WebFetch keeps ~100K
- `ks-advance-sheets-kscourts` — 282 pages / 657K chars per issue; holds official pagination and the petitions-for-review table
- `ks-ksa-revisor` — annotated sections exceed WebFetch's limit (60-513: 105,961 chars, cut at annotation 376); statute text itself is short

## Open questions

- searchdro.kscourts.gov search form (Documents/LoadPage) is JavaScript-driven; is there a plain-GET query by docket or date range for opinions older than ~12 months?
- rules.ks.gov (K.A.R. and Kansas Register) is a JavaScript app: script gets 0 chars, WebFetch gated. Does it expose static per-regulation or per-issue URLs or a JSON API?
- No official bulk download of the K.S.A. was found (not searched exhaustively).
- Lettered constitution sections (art. 15, § 3c) URL form on ksrevisor.gov untested.
- kslegislature.gov section PDF (/media/statute/...) linked from each page but not probed.
- Session laws: printed 2026-Session-Laws-Book-1.pdf / Book-2.pdf are linked from https://www.sos.ks.gov/publications/session-laws.html but not probed.
