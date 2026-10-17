# Colorado (CO) — free legal sources

_Generated from `data/co.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes and Constitution: the Office of Legislative Legal Services publishes the full 2026 C.R.S. (and Constitution as 'title-00') as one HTM/PDF/DOCX file per title on olls.info, plus whole-code zips — read them with fetch_doc.py or a corpus, since each file is millions of characters; public.law (per-section, 2024 text) and Justia (2025) are the WebFetch-friendly fallbacks, and the legislature's own C.R.S. link is a LexisNexis JS app. Court rules have no free consolidated text except LexisNexis (JS, link-only); coloradojudicial.gov hosts only rule-change orders. CCR is official on sos.state.co.us (shell gets HTTP 500; search paths robots-disallowed) with Cornell LII as a stale mirror. Case law: coloradojudicial.gov announcement sheets (published and unpublished COA decisions, SC opinions, cert denials) are reachable by WebFetch but the shell is IP-banned (403); full opinion text is most reliably read on Justia (with ¶ numbers); the judiciary's research.coloradojudicial.gov archive is a vLex JS app.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Colorado Supreme Court | `colo (unverified)` | Colo. | P.3d, P.2d, P., Colo. | YYYY CO N (e.g. 2019 CO 45, ¶ 12) |
| Colorado Court of Appeals | `coloctapp (unverified)` | Colo. App. | P.3d, P.2d, Colo. App. | YYYY COA N (e.g. 2026 COA 66, ¶ 14; modified opinions 'M' suffix, e.g. 2020 COA 12M) |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Colorado Revised Statutes | `C.R.S. § 13-80-102`; `Colo. Rev. Stat. § 13-80-102`; `§ 13-80-102(1)(a), C.R.S. 2025`; `section 13-80-102, C.R.S.`; `C.R.S. 18-3-102`; `Colo. Rev. Stat. Ann. § 25.5-4-301`; `§ 24-71.5-104, C.R.S.`; `CRS 38-12-503`; `Colorado Revised Statutes § 38-12-503`; `section 13-80-102.5 of the Colorado Revised Statutes`; `section 38-12-503(1), C.R.S. 2025` | `co-crs-olls` → `co-crs-publiclaw` → `co-crs-justia` → `co-crs-lexis` |
| Colorado Constitution | `Colo. Const. art. II, § 25`; `Colo. Const. art. X, § 20`; `Article II, Section 25 of the Colorado Constitution` | `co-constitution-olls` → `co-constitution-justia` |
| Colorado Rules of Civil Procedure | `C.R.C.P. 12(b)(5)`; `C.R.C.P. 16.1`; `Colo. R. Civ. P. 56`; `Rule 12(b)(5) of the Colorado Rules of Civil Procedure` | `co-rules-lexis` → `co-rules-changes` |
| Colorado Appellate Rules | `C.A.R. 35(e)`; `C.A.R. 4.1`; `Colo. App. R. 49`; `Rule 35(e) of the Colorado Appellate Rules` | `co-rules-lexis` → `co-rules-changes` |
| Colorado Rules of Evidence | `CRE 702`; `C.R.E. 403`; `Colo. R. Evid. 801(d)(2)`; `Rule 702 of the Colorado Rules of Evidence` | `co-rules-lexis` → `co-rules-changes` |
| Colorado Rules of Criminal Procedure | `Crim. P. 35(c)`; `Colo. R. Crim. P. 11`; `Rule 35(c) of the Colorado Rules of Criminal Procedure` | `co-rules-lexis` → `co-rules-changes` |
| Colorado Rules of Professional Conduct | `Colo. RPC 1.7`; `Colo. R.P.C. 8.4(c)`; `Colo. R. Prof'l Conduct 1.5`; `Rule 1.7 of the Colorado Rules of Professional Conduct` | `co-rules-lexis` → `co-rules-changes` |
| Code of Colorado Regulations | `1 CCR 101-1`; `8 CCR 1505-1, Rule 2.1`; `8 Colo. Code Regs. § 1505-1:2.1.1`; `6 CCR 1011-1` | `co-ccr-sos` → `co-ccr-lii` |
| Colorado Register | `47 CR 19, October 10, 2024`; `46 CR 09, May 10, 2023` | `co-register-sos` |
| Public-domain citations (since 2012) | `2019 CO 45`; `2019 CO 45, ¶ 12`; `2020 COA 12M`; `2026 COA 66, ¶ 14`; `2025 CO 63`; `26CO65` | `co-opinions-judicial` → `co-cases-justia` → `co-opinions-research` |
| Pacific Reporter and old Colorado Reports | `People v. Fields, 697 P.2d 749 (Colo. App. 1984)`; `Protect Our Mtn. v. District Court, 677 P.2d 1361 (Colo. 1984)`; `35 Colo. 225`; `12 Colo. App. 345` | `co-cases-justia` → `co-opinions-research` |
| Colorado docket numbers (unpublished COA opinions, SC dockets, cert petitions) | `No. 24CA1018`; `No. 26SC380`; `24SA148`; `People v. Martin, No. 23CA0715 (Colo. App. Sept. 3, 2026) (not published pursuant to C.A.R. 35(e))` | `co-opinions-judicial` → `co-cases-justia` → `co-subsequent-history-sc` |

Regexes (case-insensitive):

- Colorado Revised Statutes: `(?:(?:C\.\s*R\.\s*S\.|\bCRS|Colo\.\s*Rev\.\s*Stat\.(?:\s*Ann\.)?|Colorado\s+Revised\s+Statutes)\s*(?:§+\s*)?(?P<title>\d{1,2}(?:\.\d)?)-(?P<article>\d{1,3}(?:\.\d{1,2})?)-(?P<section>\d{3,4}(?:\.\d{1,2})?)(?![\d-])|(?:§+|sec(?:tion|\.)s?)\s*(?P<title2>\d{1,2}(?:\.\d)?)-(?P<article2>\d{1,3}(?:\.\d{1,2})?)-(?P<section2>\d{3,4}(?:\.\d{1,2})?)(?![\d-])(?:\s*\([0-9a-zA-Z.]+\))*\s*(?:,\s*(?:C\.\s*R\.\s*S\.|\bCRS\b|Colo\.\s*Rev\.\s*Stat\.)|\s+of\s+the\s+Colorado\s+Revised\s+Statutes))`
- Colorado Constitution: `Colo\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+[a-z]?),?\s*§\s*(?P<section>\d+[a-z]?)|Article\s+(?P<article2>[IVXL]+[a-z]?),?\s+(?:Section|§)\s*(?P<section2>\d+[a-z]?)\s+of\s+the\s+Colorado\s+Constitution`
- Colorado Rules of Civil Procedure: `(?:C\.\s*R\.\s*C\.\s*P\.|Colo\.\s*R\.\s*Civ\.\s*P\.)\s*(?P<rule>\d{1,3}(?:\.\d)?)|Rule\s+(?P<rule2>\d{1,3}(?:\.\d)?)(?:\s*\([0-9a-zA-Z]+\))*\s+of\s+the\s+Colorado\s+Rules\s+of\s+Civil\s+Procedure`
- Colorado Appellate Rules: `(?<![\w.])C\.\s*A\.\s*R\.\s*(?P<rule>\d{1,2}(?:\.\d)?)|Colo\.\s*App\.\s*R\.\s*(?P<rule2>\d{1,2}(?:\.\d)?)|Rule\s+(?P<rule3>\d{1,2}(?:\.\d)?)(?:\s*\([0-9a-zA-Z]+\))*\s+of\s+the\s+Colorado\s+Appellate\s+Rules`
- Colorado Rules of Evidence: `(?:C\.\s*R\.\s*E\.|\bCRE|Colo\.\s*R\.\s*Evid\.)\s*(?P<rule>\d{3,4})|Colorado\s+Rules?\s+of\s+Evidence\s+(?P<rule2>\d{3,4})|Rule\s+(?P<rule3>\d{3,4})(?:\s*\([0-9a-zA-Z]+\))*\s+of\s+the\s+Colorado\s+Rules\s+of\s+Evidence`
- Colorado Rules of Criminal Procedure: `(?:Colo\.\s*R\.\s*Crim\.\s*P\.|(?<!R\.\s)(?<!R\.)Crim\.\s*P\.)\s*(?P<rule>\d{1,3}(?:\.\d)?)|Rule\s+(?P<rule2>\d{1,3}(?:\.\d)?)(?:\s*\([0-9a-zA-Z]+\))*\s+of\s+the\s+Colorado\s+Rules\s+of\s+Criminal\s+Procedure`
- Colorado Rules of Professional Conduct: `(?:Colo\.\s*RPC|Colo\.\s*R\.\s*P\.\s*C\.|Colo\.\s*R\.\s*Prof(?:'|’)?l\s*Conduct)\s*(?P<rule>\d\.\d{1,2})|Rule\s+(?P<rule2>\d\.\d{1,2})(?:\s*\([0-9a-zA-Z]+\))*\s+of\s+the\s+Colorado\s+Rules\s+of\s+Professional\s+Conduct`
- Code of Colorado Regulations: `(?P<title>\d{1,2})\s+(?:CCR|Colo\.\s*Code\s*Regs\.)\s*(?:§\s*)?(?P<agency>\d{3,4})-(?P<series>\d{1,3}(?:\.\d+)?)(?:(?:,\s*(?:Rule|§|sec\.)\s*|:)(?P<rule>\d+(?:\.\d+)*))?`
- Colorado Register: `(?P<volume>\d{2})\s+(?:CR|Colo\.\s*Reg\.)\s+(?P<issue>\d{1,2})\s*,\s*(?P<date>[A-Z][a-z]+\.?\s+\d{1,2},\s*\d{4})`
- Public-domain citations (since 2012): `(?:(?P<year>(?:19|20)\d\d)\s+(?P<court>COA|CO)\s+(?P<number>\d{1,3})(?P<modified>M)?|\b(?P<yy>\d\d)(?P<court2>COA|CO)(?P<number2>\d{1,3})(?P<modified2>M)?)(?!\d)(?:\s*,\s*¶+\s*(?P<para>\d+))?`
- Pacific Reporter and old Colorado Reports: `(?P<volume>\d{1,4})\s+P\.(?:\s*[23]d)?\s+(?P<page>\d{1,5})(?:\s*,\s*\d+)?\s*\((?P<court>Colo\.(?:\s*App\.)?)\s*(?P<year>\d{4})\)|(?P<volume2>\d{1,3})\s+Colo\.(?:\s*(?P<app>App)\.)?\s+(?P<page2>\d{1,4})\b`
- Colorado docket numbers (unpublished COA opinions, SC dockets, cert petitions): `(?:No\.\s*)?(?P<yy>\d{2})(?P<type>CA|SC|SA|PDJ|UPL)(?P<num>\d{1,4})\b`

Short forms → URL key:

C.R.S. → `crs`; CRS → `crs`; Colo. Rev. Stat. → `crs`; Colo. Rev. Stat. Ann. → `crs`; C.R.C.P. → `crcp`; Colo. R. Civ. P. → `crcp`; C.A.R. → `car`; Colo. App. R. → `car`; CRE → `cre`; C.R.E. → `cre`; Colo. R. Evid. → `cre`; Crim. P. → `crim`; Colo. R. Crim. P. → `crim`; Colo. RPC → `rpc`; Colo. R.P.C. → `rpc`; Colo. R. Prof'l Conduct → `rpc`; CCR → `ccr`; Colo. Code Regs. → `ccr`; CR → `register`; Colorado Revised Statutes → `crs`

C.R.S. section numbers are title-article-section, each part may carry a decimal (25.5-4-301, 24-71.5-104, 13-80-102.5); the olls.info file key is the TITLE only (two-digit padded: 01-09; 25.5, 26.5 keep the dot). Colorado style puts C.R.S. after the number ('section 13-80-102(1)(a), C.R.S. 2025'); the regex requires 'C.R.S.' or 'Colo. Rev. Stat.' before the number or after a comma — a bare 'N-N-N' or '§ 13-80-102' with no C.R.S. tag must not route here. Ranges ('C.R.S. §§ 13-80-101 to -103') match only the first section. Rule cites: 'Crim. P.' and 'C.R.E.' are Colorado-specific, but bare 'Rule 12' or 'Rule 702' must not route here without 'C.R.C.P.', 'CRE' or 'Colorado Rules of …'; Fed. R. … forms are excluded. Public-domain citations (YYYY CO N / YYYY COA N, ¶ pinpoints) began in 2012 (from memory); P.3d is a West reporter, Colorado Reports and Colo. App. reports ended in 1980 (from memory). Docket forms: YYCA#### (COA), YYSC### (cert petitions/review), YYSA### (original proceedings), YYPDJ### (disciplinary) — generic, route only with Colorado context. Unpublished COA decisions are announced as 'NOT PUBLISHED PURSUANT TO C.A.R. 35(e)'; whether and from what date they may be cited (C.A.R. 35(e) amendment) was not verified. Register cite 'VV CR NN, date' — regex requires the date to avoid colliding with other 'CR' abbreviations. CourtListener ids from memory, unverified. The C.R.S. regex also accepts 'CRS N-N-N' and 'Colorado Revised Statutes § N-N-N', and prose 'section N-N-N of the Colorado Revised Statutes' (added after the independent check). The court's own opinion listing writes '26CO65' with no spaces; the public-domain regex accepts a two-digit year and no spaces.

## A. Statutes / code

### `co-crs-lexis` — Colorado Revised Statutes (LexisNexis free public access)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · LexisNexis for the Colorado Committee on Legal Services · text: **link-only** · official: unknown
- **Coverage:** Current C.R.S. (and Constitution, court rules via the same Lexis free-access portal).
- **Access:** `link-only` · format html
  - Index: `http://www.lexisnexis.com/hottopics/colorado/`
  - Navigation: leg.colorado.gov/laws/colorado-revised-statutes → LexisNexis link (redirects to advance.lexis.com/container?config=…). JavaScript application; no citation-to-URL route.
- **Automation:** WebFetch fail · shell ok · robots: advance.lexis.com robots permits (fetch_doc.py check OK)
  - fetch_doc.py info returns HTML with 0 characters of text (JS shell); WebFetch reports the page content as empty. Use only as a link for readers.
- **Currency:** none visible (JS app)
- **Official status:** leg.colorado.gov/laws/colorado-revised-statutes: 'Click here to access the Colorado Revised Statutes hosted by LexisNexis' — no official-status statement captured (page body is a JS app).
- **Hazard:** JavaScript-only application
- **Hazard:** terms-of-use gate in browser
- **Probe:** C.R.S. (portal) → `https://advance.lexis.com/container?config=0123JAAyMzg2MTYzZi1jMWNlLTRlOTQtODVjZS0xZTU0MDg1YmQ0OTUKAFBvZENhdGFsb2eEcVf2aFZwpM1qua3EYcVa`
- **Evidence (2026-10-16):** Script: 200, kind=html, chars=0. WebFetch: 'The web page content you provided is empty'. | Independent check 2026-10-16: fetch_doc.py info HTTP 200, kind=html, chars=0 (JS shell)

### `co-crs-olls` — Colorado Revised Statutes — OLLS title downloads (HTM / PDF / DOCX)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Colorado General Assembly, Office of Legislative Legal Services (Revisor of Statutes) · text: **fetch-and-quote** · official: unknown
- **Coverage:** All C.R.S. titles 1-44 (incl. 25.5, 26.5), the Colorado Constitution (title-00) and the general index, 2026 edition, with editor's notes and case annotations interleaved. One file per title; prior editions exist (crs2024 on content.leg.colorado.gov/sites/default/files/images/olls/; olls.info/crs-archive/ is robots-disallowed).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://olls.info/crs/crs{year}-title-{title}.pdf   (also .htm, .docx)`
  - Placeholders: year = edition year (2026 current; the 2025 edition is no longer at the old leg.colorado.gov path). title = C.R.S. title number zero-padded to two digits for 1-9 (title-01 … title-09, title-13, title-44); decimal titles keep the dot (title-25.5, title-26.5); title-00 = Colorado Constitution; crs{year}-index.pdf = general index. The whole title is one file: locate the section inside it by searching for '{title}-{article}-{section}.' followed by the catchline (e.g. '13-80-102. General limitation of actions - two years.'). The title's opening table of contents lists every article WITH its section range (e.g. 'Art. 80 … 13-80-101 to …'). Verified on 13-80-102 (title-13) and 18-3-102 (title-18), and Colo. Const. art. II, § 25 (title-00).
  - Index: `https://content.leg.colorado.gov/agencies/office-legislative-legal-services/2026-crs-titles-download`
  - Navigation: download page → per-title HTM/PDF/DOCX links (all on olls.info/crs/) → search the file for the section number + catchline.
- **Automation:** WebFetch gated · shell ok · robots: olls.info: User-agent * Disallow /crs-archive/ only
  - Files are huge (title 13: 1,769-page PDF, 5.8M chars; HTM 4.6M chars; title 24 PDF 4,892 pp), far past WebFetch's ~100K window, so the fetch tool can't reach most sections. The script route (fetch_doc.py grep/verify/section) is primary; HTM and PDF can both be quoted (fetch_doc.py now decodes the windows-1252 HTM correctly: title-13.htm has 6,090 '§' and no U+FFFD). WebFetch on olls.info is gated: the session permission prompt timed out, which is not a site refusal.
- **Currency:** download page (content.leg.colorado.gov …/2026-crs-titles-download), sentence above the links; the PDF running header gives only the edition 'Colorado Revised Statutes 2026' — observed: "Current with the changes made … by the Seventy-fifth General Assembly at its Second Regular Session in 2026."
- **Official status:** Download page (content.leg.colorado.gov/agencies/office-legislative-legal-services/2026-crs-titles-download) carries no official/unofficial statement; the legislature's C.R.S. page sends readers to the LexisNexis-hosted C.R.S. Colorado adopted UELMA (C.R.S. 24-71.5-101 et seq., HB 12-1209) but no authentication statement was seen on these files.
- **Hazard:** whole-title files exceed WebFetch window (use script or corpus)
- **Hazard:** case annotations and editor's notes interleaved with section text: quote only between the catchline and the 'Source:' history line
- **Hazard:** URL changes each edition year (crs2026 → crs2027)
- **Probe:** C.R.S. § 13-80-102 → `https://olls.info/crs/crs2026-title-13.pdf` — expect: "regardless of the theory upon which suit is brought, or against whom suit is brought"
- **Evidence (2026-10-16):** fetch_doc.py: title-13.pdf 1,769 pp, last-modified 2 Oct 2026; verify '…must be commenced within two years' VERIFIED p. 1421; same quote VERIFIED in title-13.htm. Second title: title-18.htm grep '18-3-102. Murder in the first degree. (1)' found. Running header 'Colorado Revised Statutes 2026'. | Independent check 2026-10-16: title-13.pdf quote VERIFIED p. 1421; HTM '13-80-102. General limitation of actions - two years. (1) The following civil actions'; PDF header 'Colorado Revised Statutes 2026'; second citation C.R.S. § 42-4-1301; C.R.S. § 25.5-4-301 ok
- **Notes:** Bulk: crs2026-htm.zip (37 MB), crs2026-pdf.zip (184 MB), crs2026-docx.zip (48 MB), all HTTP 200 application/zip. public.law cites the 2024 edition at content.leg.colorado.gov/sites/default/files/images/olls/crs2024-title-13.pdf (still 200 PDF via 301 from leg.colorado.gov).

### `co-session-laws` — Session Laws of Colorado (leg.colorado.gov)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Colorado General Assembly · text: **link-only** · official: unknown
- **Coverage:** Session-law PDFs per bill (e.g. HB26-1001) listed on /laws/session-laws.
- **Access:** `index-anchored` · format pdf
  - Placeholders: Download links /laws/session-laws/{BILL}/{n}/download — {n} is an internal id.
  - Index: `https://leg.colorado.gov/laws/session-laws`
  - Navigation: session-laws page → bill row → /download (robots-disallowed).
- **Automation:** WebFetch untested · shell blocked-robots · robots: leg.colorado.gov robots: Disallow /laws/session-laws/*/download (also /bill_files/*/download etc.)
  - Never fetch the PDFs automatically; link only.
- **Currency:** none stated
- **Official status:** No statement captured.
- **Hazard:** robots-disallowed downloads
- **Hazard:** site migration banner: legacy session data links may not work
- **Probe:** HB26-1001 session law → `https://leg.colorado.gov/laws/session-laws/HB26-1001/8/download`
- **Evidence (2026-10-16):** robots.txt (read 2026-10-16) disallows /laws/session-laws/*/download; not fetched. | Independent check 2026-10-16: not re-tested (WebFetch of /laws/session-laws and robots.txt gated by a permission timeout); the block still rests on the 2026-10-16 robots.txt reading

### `co-crs-justia` — Justia — Colorado Revised Statutes (2025)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** 2025 C.R.S. (unversioned URL); earlier editions under /codes/colorado/{year}/.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/codes/colorado/title-{title}/{division-slug}/article-{article}/[part-{part}/]section-{title}-{article}-{section}/`
  - Placeholders: Some titles have a division slug between title and article (title-13 → limitation-of-actions for Arts. 80-82; courts-of-record for Arts. 1-9); others do not (title-18/article-3/part-1/section-18-3-102/). Part level appears only where the article has parts (article-80 has none). Dots in section numbers become hyphens (section-13-80-102-5). The division slug is not derivable: open the title index.
  - Index: `https://law.justia.com/codes/colorado/title-{title}/`
  - Navigation: title index (shows division article ranges, not section ranges) → division page → article page. If the article has no parts, the article page links the sections and shows the section range (e.g. §§ 13-80-101 - 13-80-105.5). If it has parts, the article page lists the parts with their section ranges → part page → section link (e.g. title-38/tenants-and-landlords/article-12/part-5/section-38-12-503/).
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge to the shell)
  - fetch_doc.py: REFUSED (law.justia.com robots/challenge). WebFetch only. A guessed URL with a wrong level (…/article-80/part-1/…) returned a fetch error.
- **Currency:** page header — observed: "2025 Colorado Revised Statutes"
- **Official status:** Page disclaimer: the code 'may not be the most recent version'.
- **Hazard:** division slug and part level must be read from indexes
- **Hazard:** shell blocked
- **Hazard:** edition lag
- **Probe:** C.R.S. § 13-80-102 → `https://law.justia.com/codes/colorado/title-13/limitation-of-actions/article-80/section-13-80-102/` — expect: "The following civil actions, regardless of the theory upon which"
- **Evidence (2026-10-16):** WebFetch: body present, '2025 Colorado Revised Statutes', not truncated. Second: /title-18/article-3/part-1/section-18-3-102/ body present ('A person commits the crime of murder in the first'). | Independent check 2026-10-16: 'The following civil actions, regardless of the theory upon which'; '2025 Colorado Revised Statutes'; not truncated; second citation C.R.S. § 38-12-503 ok

### `co-crs-publiclaw` — Colorado.Public.Law — Colorado Revised Statutes

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Public.Law · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All C.R.S. titles, one page per section; text taken from the 2024 OLLS edition (index says 'Current through Fall 2025').
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://colorado.public.law/statutes/crs_{title}-{article}-{section}`
  - Placeholders: section number verbatim with hyphens and dots (crs_13-80-102, crs_18-3-102, crs_25.5-8-101, crs_13-80-102.5). A 404 means the section is absent from public.law's edition (e.g. crs_18-1-105 returned 404 — check the article index).
  - Index: `https://colorado.public.law/statutes`
- **Automation:** WebFetch ok · shell ok · robots: User-agent * disallows /admin, /api, /data, /demo, /images, /users; /statutes allowed
  - The script route is primary (constructible). WebFetch also works, though one WebFetch here was gated (permission prompt timed out).
- **Currency:** statutes index page under the heading; per-page 'Source' line names the edition — observed: "Current through Fall 2025 (source: crs2024-title-13.pdf, accessed May 26, 2025)"
- **Official status:** Third-party compilation; each page cites as 'Source' the OLLS crs2024 title PDF.
- **Hazard:** lags official text by one or more sessions (page source is the 2024 edition)
- **Hazard:** some sections 404 (crs_18-1-105)
- **Probe:** C.R.S. § 13-51-101 → `https://colorado.public.law/statutes/crs_13-51-101` — expect: "This article shall be known and may be cited as"
- **Evidence (2026-10-16):** WebFetch: body present, 'Current through Fall 2025', source crs2024-title-13.pdf. Script: crs_13-80-102 6,688 chars, body present; crs_18-3-102 verify 'After deliberation and with the intent to cause the death' VERIFIED. | Independent check 2026-10-16: 'This article shall be known and may be cited as'; 'Current through Fall 2025'; second citation C.R.S. § 38-12-503 ok
- **Notes:** WebFetch of crs_13-80-102 itself was not sent (session permission prompt timed out); script route covers it.

## B. Constitution

### `co-constitution-olls` — Colorado Constitution — OLLS 'title-00' download

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Colorado General Assembly, Office of Legislative Legal Services · text: **fetch-and-quote** · official: unknown
- **Coverage:** Constitution of 1876 as amended, with annotations; 2026 edition (1,578-page PDF).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://olls.info/crs/crs{year}-title-00.pdf   (also .htm)`
  - Placeholders: Single file; search 'Section {n}. {catchline}.' within the article. Article TOC on p. 1.
  - Index: `https://content.leg.colorado.gov/agencies/office-legislative-legal-services/2026-crs-titles-download`
- **Automation:** WebFetch gated · shell ok · robots: olls.info: Disallow /crs-archive/ only
  - 6.57M characters, so the WebFetch window can't reach most articles; the script route is primary and PDF and HTM can both be quoted. WebFetch is gated (permission prompt timed out).
- **Currency:** download page sentence; the PDF header gives only 'Colorado Revised Statutes 2026' — observed: "Current with … Second Regular Session in 2026."
- **Official status:** Same download page as co-crs-olls; no official statement. leg.colorado.gov/laws/colorado-constitution links only to LexisNexis.
- **Hazard:** huge single file
- **Hazard:** annotations interleaved
- **Probe:** Colo. Const. art. II, § 25 → `https://olls.info/crs/crs2026-title-00.pdf` — expect: "No person shall be deprived of life, liberty or property, without due process of law"
- **Evidence (2026-10-16):** fetch_doc.py: 1,578 pp; verify art. II § 25 quote VERIFIED p. 566; art. II § 6 'Courts of justice shall be open to every person' found p. 23. | Independent check 2026-10-16: grep title-00.pdf p. 566 'Section 25. Due process of law. No person shall be deprived'; second citation Colo. Const. art. X, § 20 (p. 1140) ok

### `co-constitution-justia` — Justia — Colorado Constitution

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** One page per article.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/colorado/cnart{article_arabic}.html`
  - Placeholders: article number in Arabic (Art. II → cnart2.html, Art. I → cnart1.html); index at /constitution/colorado/ lists section titles only. Lettered articles (XVIIIa etc.) not checked.
  - Index: `https://law.justia.com/constitution/colorado/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
- **Currency:** none stated
- **Official status:** Disclaimer: 'This Constitution may not be the most recent version.'
- **Hazard:** no currency date
- **Hazard:** shell blocked
- **Hazard:** lettered-article slugs unverified
- **Probe:** Colo. Const. art. II, § 25 → `https://law.justia.com/constitution/colorado/cnart2.html` — expect: "No person shall be deprived of life, liberty or property,"
- **Evidence (2026-10-16):** WebFetch: art. II § 25 and § 6 bodies present. Index page: body NOT PRESENT (titles only), links cnart1.html, cnart2.html. | Independent check 2026-10-16: 'No person shall be deprived of life, liberty or property,'; not truncated; second citation Colo. Const. art. X, § 20 (cnart10.html) ok

## C. Court rules

### `co-rules-changes` — Colorado Supreme Court rule-change orders (PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Colorado Supreme Court / Colorado Judicial Branch · text: **fetch-and-quote** · official: official
- **Coverage:** Rule Change orders, e.g. 'RULE CHANGE 2026(11)' (C.R.C.P. 1 and 16.2), back to at least 2012; each reproduces amended rules with [NO CHANGE] markers — not a consolidated rule set.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.coloradojudicial.gov/sites/default/files/{YYYY-MM}/Rule%20Change%20{year}%28{nn}%29.pdf`
  - Placeholders: Upload folder YYYY-MM and file names vary (older ones re-uploaded under 2023-06/Rule_Change_2014-12.PDF; node pages /node/{id} per change). Not constructible: find via the rule-changes listing or a web search for 'Rule Change {year}({nn})'.
  - Index: `https://www.coloradojudicial.gov/supreme-court/adopted-proposed-rule-changes?topic=78&wrapped=true`
  - Navigation: adopted/proposed rule changes listing (reached from /supreme-court) → /node/{id} page → PDF. A web search for 'Rule Change {year}({nn})' also finds the PDF.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.coloradojudicial.gov: User-agent * disallows /core/, /profiles/, README etc. (Drupal default); /sites/default/files allowed
  - Shell: uncached pages return HTTP 403 '… has been banned up to …' (IP ban); fetch_doc.py REFUSED for the day. WebFetch reaches the host. Long packages truncate (Rule Change 2015(05) cut in Rule 37(a)(4)).
- **Currency:** order's adoption/effective line — observed: "Amended and Adopted by the Court, En Banc, April 23, 2026"
- **Official status:** Orders of the Supreme Court amending the rules ('Amended and adopted by the Court, En Banc …').
- **Hazard:** amendment orders only, not consolidated text
- **Hazard:** shell IP-banned (403)
- **Hazard:** WebFetch truncation on long packages
- **Hazard:** WebFetch drops redline markup (strike/underline), so old and new text show as two copies that can't be told apart; check the PDF visually or with the script.
- **Probe:** C.R.C.P. 1(a) (Rule Change 2026(11)) → `https://www.coloradojudicial.gov/sites/default/files/2026-04/Rule%20Change%202026%2811%29.pdf` — expect: "These rules govern the procedure in the supreme court, court of"
- **Evidence (2026-10-16):** WebFetch: 'RULE CHANGE 2026(11)', C.R.C.P. 1 and 16.2, body present. Also /media/12394 = 'RULE CHANGE 2015(05)' with C.R.C.P. 12(b) text ('Every defense, in law or in fact, to a claim'), truncated. | Independent check 2026-10-16: 'RULE CHANGE 2026(11)', Rules 1 and 16.2; 'Amended and Adopted by the Court, En Banc, April 23, 2026'; second citation Rule Change 2025(17) (C.R.C.P. 121 § 1-26) ok

### `co-rules-lexis` — Colorado Court Rules (LexisNexis free access)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · LexisNexis for the Colorado Judicial Branch · text: **link-only** · official: unknown
- **Coverage:** Consolidated Colorado court rules (reported).
- **Access:** `link-only` · format html
  - Index: `http://www.lexisnexis.com/hottopics/colorado/`
  - Navigation: Lexis free-access portal (JS app)
- **Automation:** WebFetch fail · shell ok · robots: permits
  - JS app: 0 characters of text to the script and WebFetch (see co-crs-lexis).
- **Currency:** none visible
- **Official status:** Not captured; the free Lexis portal is the only consolidated free text found for C.R.C.P., C.A.R., CRE, Crim. P., Colo. RPC.
- **Hazard:** JavaScript-only
- **Probe:** C.R.C.P. 12(b)(5) → `http://www.lexisnexis.com/hottopics/colorado/`
- **Evidence (2026-10-16):** Portal URL from the OLLS agency page; same JS shell as co-crs-lexis (script chars=0). | Independent check 2026-10-16: fetch_doc.py info → advance.lexis.com/container?config=0345…, chars=0
- **Notes:** No tier-2 consolidated rule text found: public.law Colorado has statutes only (court_rules/rules paths 404).

## D. Administrative code

### `co-ccr-sos` — Code of Colorado Regulations (Secretary of State)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Colorado Secretary of State · text: **link-only** · official: official
- **Coverage:** All state agency rules, browse by department/agency/rule; rule PDFs.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Browse: /CCR/NumericalDeptList.do → /CCR/NumericalAgencyList.do?deptID={n} → rule list → rule PDF (GenerateRulePdf.do, id-based). robots.txt disallows /CCR/Rule.do, /CCR/KeywordSearch.do, /CCR/NumericalSubDocList.do — do not use those.
  - Index: `https://www.sos.state.co.us/CCR/NumericalDeptList.do`
  - Navigation: department list → agency list → rule → PDF (ids not derivable from '8 CCR 1505-1')
- **Automation:** WebFetch ok · shell http-error · robots: sos.state.co.us: * disallows /CCR/KeywordSearch.do, /CCR/Rule.do, /CCR/NumericalSubDocList.do, /apps/, /biz/… ; SemrushBot etc. disallowed
  - Shell: fetch_doc.py and curl get HTTP 500 'Service Unavailable' on /CCR/ pages of www.sos.state.co.us and www.coloradosos.gov (re-confirmed by the independent check). WebFetch reaches NumericalAgencyList.do?deptID=11 and shows the 'Official Publication' banner and agency list, but no link URLs, so the rule-PDF step (GenerateRulePdf.do) can't be followed. Link-only until a rule-PDF route is proven; read text from co-ccr-lii and disclose that it is stale. WebFetch to NumericalDeptList.do, RegisterHome.do and Welcome.do was gated (permission prompt timed out).
- **Currency:** per-rule PDF certificate / effective date (not captured)
- **Official status:** CCR FAQs (coloradosos.gov/pubs/CCR/FAQs.html): SOS 'publishes the official Code and Register online'; each regulation PDF carries a digital certificate. Agency page banner: 'Official Publication of the State Administrative Rules (24-4-103(11)'.
- **Hazard:** id-based rule URLs
- **Hazard:** robots-disallowed search and Rule.do paths
- **Hazard:** shell gets HTTP 500
- **Hazard:** no rule-PDF route proven: rule text can't be reached from this host
- **Probe:** Department of Law agency list (CCR 901-904) → `https://www.sos.state.co.us/CCR/NumericalAgencyList.do?deptID=11` — expect: "Code of Colorado Regulations Official Publication of the State Administrative Rules"
- **Evidence (2026-10-16):** WebFetch: agency list page reached (Department of Law divisions), but no rule text fetched; shell HTTP 500 'Service Unavailable'. | Independent check 2026-10-16: script HTTP 500 (exit 4); WebFetch showed the 'Official Publication of the State Administrative Rules' banner and agencies 901-904, no hrefs

### `co-ccr-lii` — Cornell LII — Code of Colorado Regulations

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** CCR by department; per-rule pages with Colorado Register history notes.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/colorado/{title}-CCR-{agency}-{series}-{rule}`
  - Placeholders: rule = top-level rule number (8 CCR 1505-1, Rule 2 → 8-CCR-1505-1-2; subrules 2.1.1 live on that page). Without the rule suffix (…/1-CCR-101-1) LII silently returns the top-level Colorado index (same hash), not a 404. Browse: /regulations/colorado/department-{dept}/division-{agency}/{title}-CCR-{agency}-{series}.
  - Index: `https://www.law.cornell.edu/regulations/colorado`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay 10; /regulations allowed
  - Respect the 10-second crawl delay.
- **Currency:** page foot and Notes — observed: "updated quarterly; last note '47 CR 19, October 10, 2024, effective 10/30/2024'"
- **Official status:** Third-party mirror; 'State regulations are updated quarterly'.
- **Hazard:** stale: page last-modified 31 Jul 2025
- **Hazard:** missing-suffix URL returns the index, not 404
- **Probe:** 8 CCR 1505-1, Rule 2.1.1 → `https://www.law.cornell.edu/regulations/colorado/8-CCR-1505-1-2` — expect: "An applicant may submit a properly executed voter registration form"
- **Evidence (2026-10-16):** WebFetch: 2.1.1 body present, not truncated; script: 20,297 chars, body present, last-modified 31 Jul 2025. | Independent check 2026-10-16: 'An applicant may submit a properly executed voter registration form'; '47 CR 19, October 10, 2024, effective 10/30/2024'; second citation 8 CCR 1505-6, Rule 1 ok
- **Notes:** regulations.justia.com also mirrors the CCR but is outside the brief's tier-2 list (law.justia.com only); not recorded as a source.

## D. Administrative register

### `co-register-sos` — Colorado Register (Secretary of State)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Colorado Secretary of State · text: **link-only** · official: official
- **Coverage:** Twice-monthly issues; cited 'VV CR NN, Month D, YYYY'.
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.coloradosos.gov/CCR/RegisterHome.do`
  - Navigation: Register home → issue → documents (not probed)
- **Automation:** WebFetch gated · shell http-error · robots: see co-ccr-sos
  - WebFetch not sent (permission prompt timed out); shell gets HTTP 500.
- **Currency:** not captured
- **Official status:** CCR FAQs: SOS publishes the official Code and Register online; Register published on the 10th and 25th of each month.
- **Hazard:** not probed
- **Hazard:** no route has reached the Register (script HTTP 500; WebFetch gated)
- **Probe:** 47 CR 19 → `https://www.coloradosos.gov/CCR/RegisterHome.do`
- **Evidence (2026-10-16):** URL given on coloradosos.gov/pubs/CCR/FAQs.html (WebFetch); page itself not fetched. | Independent check 2026-10-16: fetch_doc.py HTTP 500 for RegisterHome.do; WebFetch not tried

## E. Case law

### `co-opinions-judicial` — Colorado Supreme Court / Court of Appeals opinions pages and announcement sheets (coloradojudicial.gov)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Colorado Judicial Branch · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Weekly Supreme Court case announcements (2021-2026 year facet; Monday PDFs named M.D.YY.pdf) and Thursday Court of Appeals announcement PDFs (MM-DD-YY.pdf) listing every published (YYYY COA N) and unpublished ('NOT PUBLISHED PURSUANT TO C.A.R. 35(e)') decision with docket, panel and disposition. The sheets link the opinion PDFs from the public-domain citation; Supreme Court opinions are also listed at /supreme-court/opinions (see co-opinions-sc-listing).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.coloradojudicial.gov/sites/default/files/{YYYY-MM}/{date}.pdf`
  - Placeholders: date formats vary (9.28.26.pdf, 10.6.26%20r.pdf, 09-03-26.pdf, 03-12-26%20.pdf, 04-09-26_0.pdf) — not constructible; use the listing.
  - Index: `https://www.coloradojudicial.gov/es/node/47`
  - Navigation: SC announcements listing (/es/node/47?page=N, facet f[0]=case_announcement_sc_year:YYYY) → /node/{id} → PDF; COA sheets found by web search on the decision date.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.coloradojudicial.gov: User-agent * disallows /core/, /profiles/, README etc. (Drupal default); /sites/default/files allowed
  - Shell IP-banned (HTTP 403 'has been banned up to …'). WebFetch to /supreme-court/opinions not sent (permission prompt timed out).
- **Currency:** announcement date — observed: "COLORADO COURT OF APPEALS announcements September 3, 2026"
- **Official status:** Announcement sheets: slip opinions 'are subject to modification, rehearing, withdrawal, or clerical corrections'.
- **Hazard:** opinion PDF links are inside the sheet (not shown by WebFetch)
- **Hazard:** irregular file names
- **Hazard:** shell blocked
- **Probe:** 2026 COA 66 (No. 24CA1018) → `https://www.coloradojudicial.gov/sites/default/files/2026-09/09-03-26.pdf` — expect: "2026 COA 66"
- **Evidence (2026-10-16):** WebFetch: 15-page COA sheet, '2026 COA 66' / 'Court of Appeals No. 24CA1018'; unpublished entries 'NOT PUBLISHED PURSUANT TO C.A.R. 35(e)'. SC sheet 06.30.25.pdf lists '2025 CO 47' (24SA148); no opinion text in sheets. | Independent check 2026-10-16: '2026 COA 66', No. 24CA1018; 'NOT PUBLISHED PURSUANT TO C.A.R. 35(e)'; 15 pp; second citation People v. Duong, No. 23CA0217 (Colo. App. Oct. 1, 2026) (unpublished; 10-01-26.pdf) ok
- **Notes:** Locating an opinion by (court, docket, date): find the week's sheet, confirm citation/docket, then read the text on Justia (co-cases-justia) — the official opinion PDF URL was not obtained.

### `co-opinions-research` — Colorado Judicial Branch legal research site (appellate opinions, published and unpublished)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Colorado Judicial Branch (platform by vLex) · text: **link-only** · official: unknown
- **Coverage:** Reported: appellate opinions back to 1864 (COA from 1891), including unpublished Court of Appeals opinions (per CBA 'Colorado Lawyer' article, unverified).
- **Access:** `search-only` · format html
  - Index: `https://research.coloradojudicial.gov/`
  - Navigation: JS search app; /search?q= returns 404 to a plain GET
- **Automation:** WebFetch gated · shell ok · robots: none (404 'Cannot GET /robots.txt')
  - fetch_doc.py info: 200, 0 characters (vLex single-page app). WebFetch not sent (permission prompt timed out).
- **Currency:** none
- **Official status:** leg.colorado.gov/laws/colorado-appellate-court-opinions: per 13-2-122 C.R.S. every opinion is published online, linking to research.coloradojudicial.gov.
- **Hazard:** JavaScript-only
- **Hazard:** no GET search
- **Probe:** (site home) → `https://research.coloradojudicial.gov/`
- **Evidence (2026-10-16):** Script: HTML shell, chars=0; GET /search?q=Jargowsky → 404. | Independent check 2026-10-16: fetch_doc.py info HTTP 200, chars=0 (vLex JS shell)

### `co-opinions-sc-listing` — Colorado Supreme Court opinions listing (coloradojudicial.gov)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Colorado Judicial Branch · text: **link-only** · official: unofficial
- **Coverage:** Supreme Court opinions grouped by release date. The intro says July 1, 2025 – June 30, 2026, but entries run through Oct. 12, 2026; the earliest seen was Sept. 8, 2025 (2025 CO 49). Each entry gives the citation, docket and case name, and links a /node/{id} page.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Placeholders: Citations are written '26CO65' or '2025 CO 65' (normalise both). Node ids aren't derivable. The opinion PDF URL behind /node/{id} hasn't been observed.
  - Index: `https://www.coloradojudicial.gov/supreme-court/opinions?topic=78&wrapped=true`
  - Navigation: listing → entry under its release date (citation, docket, name) → /node/{id} → opinion PDF (pattern unknown)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.coloradojudicial.gov: Drupal default; /supreme-court allowed
  - Shell is IP-banned (HTTP 403). The listing has no pagination; it covers roughly one term. WebFetch to a /node/{id} page was gated for the verifier (permission prompt timed out).
- **Currency:** page introduction — observed: "listing covers July 1, 2025 through June 30, 2026 (entries to Oct. 12, 2026)"
- **Official status:** Slip opinions, subject to modification (per the announcement sheets).
- **Hazard:** only about one term listed; older years not found here
- **Hazard:** citation spacing varies (26CO65 vs 2025 CO 65)
- **Hazard:** PDF URL unknown; read the text on co-cases-justia
- **Hazard:** shell blocked
- **Probe:** Litterer v. Vail Summit Resorts, 2026 CO 65 (25SC134) → `https://www.coloradojudicial.gov/supreme-court/opinions?topic=78&wrapped=true` — expect: "26CO65"
- **Evidence (2026-10-16):** WebFetch 2026-10-16: '26CO65, 25SC134 Litterer, John v. Vail Summit Resorts, Inc.' → /node/17940; '26CO64, 25SA265' → /node/17941; '2025 CO 65, 25SA154, People v. Havens' → /node/15461; earliest Sept. 8, 2025.
- **Notes:** Found by the independent check, then probed by research.

### `co-cases-justia` — Justia — Colorado Supreme Court and Court of Appeals opinions

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court and Court of Appeals by year; 2026 COA listing shows 1,049 items and includes unpublished decisions (e.g. 23CA0715, announced as not published). Includes PDJ disciplinary decisions.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/colorado/{court}/{year}/{docket}.html`
  - Placeholders: court = supreme-court | court-of-appeals; year = decision year; docket lower-case (24ca1018, 23sc847, 24sa276); consolidated cases use the first docket; duplicates get -0 suffix (24sc207-0). Year listing /cases/colorado/{court}/{year}/ pages 500 per page.
  - Index: `https://law.justia.com/cases/colorado/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - WebFetch only.
- **Currency:** none
- **Official status:** Third-party copy of slip opinions.
- **Hazard:** slip text only; ¶ numbers present (use them for pinpoints)
- **Hazard:** shell blocked
- **Hazard:** docket suffix variants
- **Hazard:** unpublished COA pages carry 'NOT PUBLISHED PURSUANT TO C.A.R. 35(e)' but no COA number in the text; confirm the docket from the URL or the announcement sheet
- **Probe:** People v. Kennedy, 2025 CO 63 (No. 23SC847) → `https://law.justia.com/cases/colorado/supreme-court/2025/23sc847.html` — expect: "In this criminal case, we address whether Kari Mobley Kennedy's sentence was"
- **Evidence (2026-10-16):** WebFetch: full opinion ¶¶ 1-59, citation '2025 CO 63', not truncated. Second: /court-of-appeals/2026/24ca1018.html = 2026 COA 66, ¶¶ 1-69 ('Mischa Jargowsky appeals the judgment of conviction entered after a jury found'). | Independent check 2026-10-16: 2025 CO 63, ¶¶ 1-59, 'In this criminal case, we address whether Kari Mobley Kennedy's'; second citation People v. Duong, No. 23CA0217 (Colo. App. 2026) and Litterer v. Vail Summit Resorts, 2026 CO 65 (25SC134) ok

## F. Subsequent history

### `co-subsequent-history-sc` — Colorado Supreme Court weekly case announcements (certiorari dispositions)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Colorado Supreme Court · text: **fetch-and-quote** · official: official
- **Coverage:** Each Monday sheet lists cert petitions decided, e.g. 'No. 26SC380, Court of Appeals Case No. 23CA1830 … Petition for Writ of Certiorari DENIED. EN BANC.' Listing years 2021-2026 on the site.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.coloradojudicial.gov/sites/default/files/{YYYY-MM}/{M.D.YY}.pdf`
  - Placeholders: File names irregular; take them from the listing.
  - Index: `https://www.coloradojudicial.gov/es/node/47`
  - Navigation: listing (newest first; ?page=N; year facet f[0]=case_announcement_sc_year:YYYY) → weekly PDF → search it for the COA case number (e.g. 23CA1830). No search by COA number across weeks: scan the sheets after the COA decision date, or web-search the COA number; cert grants and denials also appear on Justia only when an opinion issues.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.coloradojudicial.gov: User-agent * disallows /core/, /profiles/, README etc. (Drupal default); /sites/default/files allowed
  - Shell IP-banned (403).
- **Currency:** the date on the listing row (/es/node/47); the sheet header line itself carries no date — observed: "COLORADO SUPREME COURT CASE ANNOUNCEMENTS"
- **Official status:** Court's own weekly announcement of orders.
- **Hazard:** no cross-week search by lower-court number
- **Hazard:** irregular file names
- **Hazard:** shell blocked
- **Probe:** Ocampo v. People, No. 26SC380 (COA No. 23CA1830), cert. denied → `https://www.coloradojudicial.gov/sites/default/files/2026-09/9.28.26.pdf` — expect: "Petition for Writ of Certiorari DENIED. EN BANC."
- **Evidence (2026-10-16):** WebFetch: 4-page sheet, 'No. 26SC380, Court of Appeals Case No. 23CA1830' … 'Petition for Writ of Certiorari DENIED. EN BANC.'; listing /es/node/47 shows Oct. 12, 2026 sheet and year facet. | Independent check 2026-10-16: 'No. 26SC380, Court of Appeals Case No. 23CA1830' and 'Petition for Writ of Certiorari DENIED. EN BANC.'; second citation Messersmith v. Cari, No. 26SC141 (COA No. 25CA185), cert. denied (10.12.26.pdf) ok

## Not available (do not look for these again)

- **court_rules** — Free consolidated court-rule text on a tier-1 government host or on public.law / Justia / LII: coloradojudicial.gov has rule-change orders only; legislature links court material to LexisNexis; colorado.public.law/court_rules and /rules return 404; public.law home lists Colorado statutes only. (2026-10-16)
- **constitution** — public.law Colorado Constitution: https://colorado.public.law/constitution → HTTP 404 (script). (2026-10-16)
- **case_law** — Free official reporter pagination: Colorado's official citation is the public-domain YYYY CO/COA N with ¶ numbers (seen in Justia text of 2025 CO 63 and 2026 COA 66); P.3d pages are West's. (2026-10-16)
- **statutes** — Official XML/JSON statute API: OLLS offers only HTM/PDF/DOCX per title and zips (crs2026-htm.zip 37 MB, -pdf.zip 184 MB, -docx.zip 48 MB); no structured API found. (2026-10-16)

## Corpus candidates (maintainers)

- `co-crs-olls` — Each title is one file of up to ~13.7M characters (title 24: 4,892 pp); WebFetch reads ~100K, so nearly every section is unreachable by the fetch tool. · bulk: https://olls.info/crs/crs2026-pdf.zip (also crs2026-htm.zip, crs2026-docx.zip)
- `co-constitution-olls` — 1,578-page single file (6.57M chars) with annotations; beyond WebFetch. · bulk: https://olls.info/crs/crs2026-pdf.zip

## Open questions

- WebFetch on olls.info (C.R.S. title files), research.coloradojudicial.gov, coloradojudicial.gov/supreme-court/opinions and the SOS CCR browse/Register pages could not be tested: the session's permission prompt timed out (not a site refusal).
- C.A.R. 35(e): whether unpublished COA opinions issued after a 2023 amendment may be cited as persuasive authority — not verified.
- CCR rule-PDF (GenerateRulePdf.do) route and robots status not tested because the shell gets HTTP 500 from sos.state.co.us; WebFetch saw no link URLs on the agency list.
- Colorado Register issue URLs and currency not probed.
- Justia Constitution slugs for lettered articles (XVIIIa, XXVII …) not checked.
- CourtListener ids colo / coloctapp unverified.
- Official SC opinion PDF URL behind /node/{id} (coloradojudicial.gov/supreme-court/opinions listing) not observed; shell IP-banned (HTTP 403 'banned up to Sat, 17 Oct 2026 16:31 UTC').
- Colorado Register (RegisterHome.do): script HTTP 500 for research and verifier; retest with WebFetch.
- co-session-laws robots block not re-confirmed by the independent check (permission timeout).
