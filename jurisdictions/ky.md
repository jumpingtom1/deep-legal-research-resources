# Kentucky (KY) — free legal sources

_Generated from `data/ky.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: apps.legislature.ky.gov serves each KRS section as a PDF at statute.aspx?id=N, where the numeric id comes from the chapter page (title page, then chapter, then section); fetch_doc.py reads them, built URLs are gated for WebFetch, and Justia 2025 is a constructible tier-2 fallback. The constitution and session laws (Ky. Acts) are on the same host, and KAR regulation pages have constructible URLs (3-digit padded) with engrossed PDFs; the Administrative Register is published as monthly PDFs. Consolidated court rules (CR, RCr, KRE, RAP, SCR) are only on govt.westlaw.com, which is blocked; kycourts.gov serves only the Supreme Court's adopting and amending orders as PDFs (RAP order 2022-49 is a corpus candidate). Case law: the official opinion hosts fail (opinions.kycourts.net has a TLS error; appellatepublic.kycourts.net is a JavaScript app). Supreme Court and Court of Appeals minutes PDFs on apps.kycourts.net list every opinion and discretionary-review order by docket. Justia supplies the opinion text, with cases.justia.com slip PDFs readable by the script.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Kentucky | `ky (unverified)` | Ky. | S.W.3d, S.W.2d | — |
| Court of Appeals of Kentucky (intermediate court, 1976-) | `kyctapp (unverified)` | Ky. Ct. App. | S.W.3d, S.W.2d | — |
| Court of Appeals of Kentucky (highest court before 1976) | `kyctapphigh (unverified)` | Ky. | S.W.2d, S.W., Ky. | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Kentucky Revised Statutes (KRS) | `KRS 413.140`; `KRS 413.140(1)(a)`; `Ky. Rev. Stat. Ann. § 413.140`; `Ky. Rev. Stat. § 186.010`; `KRS 342.0011(1)`; `KRS 304.20-450`; `KRS 311.530 to 311.620`; `KRS Chapter 413`; `section 413.140 of the Kentucky Revised Statutes` | `ky-krs-lrc` → `ky-krs-justia` |
| Kentucky Acts (session laws) | `2019 Ky. Acts ch. 37`; `2024 Ky. Acts ch. 1, sec. 2`; `1942 Ky. Acts ch. 208` | `ky-acts-lrc` |
| Kentucky Constitution | `Ky. Const. § 115`; `Ky. Const. §§ 27-28`; `Section 115 of the Kentucky Constitution`; `Kentucky Constitution Section 116`; `Section 2 of the Constitution of Kentucky`; `Ky. Const. sec. 14` | `ky-constitution-lrc` → `ky-constitution-justia` |
| Kentucky Rules of Civil Procedure (CR, dotted form) | `CR 12.02(f)`; `CR 56.03`; `CR 60.02`; `CR 76.28(4)(c)`; `Ky. R. Civ. P. 12.02` | `ky-rules-westlaw` → `ky-rules-orders-kycourts` |
| Kentucky Rules of Criminal Procedure (RCr) | `RCr 11.42`; `RCr 10.26`; `Ky. R. Crim. P. 11.42` | `ky-rules-westlaw` → `ky-rules-orders-kycourts` |
| Kentucky Rules of Evidence (KRE) | `KRE 702`; `KRE 803(6)`; `Ky. R. Evid. 702` | `ky-rules-westlaw` |
| Kentucky Rules of Appellate Procedure (Ky. RAP) | `Ky. RAP 41`; `Ky. R. App. P. 41(A)`; `RAP 41 of the Kentucky Rules of Appellate Procedure` | `ky-rules-orders-kycourts` → `ky-rules-westlaw` |
| Rules of Appellate Procedure (bare RAP) *(only once this jurisdiction is known)* | `RAP 41`; `RAP 32(A)(4)` | `ky-rules-orders-kycourts` → `ky-rules-westlaw` |
| Rules of the Supreme Court of Kentucky (SCR) | `SCR 3.130(1.7)`; `SCR 3.130-1.7`; `SCR 1.030(3)`; `Ky. SCR 3.130` | `ky-rules-westlaw` → `ky-rules-orders-kycourts` |
| Civil Rules (bare CR without dotted number) *(only once this jurisdiction is known)* | `CR 56` | `ky-rules-westlaw` |
| Kentucky Administrative Regulations (KAR) | `201 KAR 9:260`; `401 KAR 5:005`; `13 KAR 2:020`; `907 KAR 1:005E`; `201 KAR 9:260, Section 1`; `201 Ky. Admin. Regs. 9:260` | `ky-kar-lrc` → `ky-kar-lii` |
| Administrative Register of Kentucky (Ky.R.) | `47 Ky.R. 374`; `53 Ky.R. 1120` | `ky-register-lrc` |
| Kentucky cases, South Western Reporter with Kentucky parenthetical | `Hoskins v. Maricle, 150 S.W.3d 1 (Ky. 2004)`; `Commonwealth v. Bredhold, 599 S.W.3d 409 (Ky. 2020)`; `123 S.W.3d 456 (Ky. App. 2021)`; `123 S.W.3d 456 (Ky. Ct. App. 2021)`; `Steelvest, Inc. v. Scansteel Serv. Ctr., Inc., 807 S.W.2d 476 (Ky. 1991)` | `ky-cases-justia` → `ky-coa-minutes` → `ky-sc-minutes` |
| Kentucky Reports (official, to 1951) | `314 Ky. 1`; `290 Ky. 213` | `ky-cases-justia` |
| Kentucky unpublished / Westlaw opinion with Kentucky parenthetical | `No. 2019-CA-001234-MR, 2021 WL 123456 (Ky. App. Jan. 8, 2021)`; `2020 WL 1234567 (Ky. Mar. 26, 2020)` | `ky-cases-justia` → `ky-coa-minutes` |
| Kentucky appellate docket numbers | `No. 2024-CA-0287-MR`; `2025-SC-0115-MR`; `2019-CA-001234-MR`; `2025-SC-0451-DG`; `2026-SC-0211-DGE`; `No. 2025-SC-0239-D`; `2026-SC-0231-DE` | `ky-coa-minutes` → `ky-sc-minutes` → `ky-cases-justia` |
| South Western Reporter (bare, no court parenthetical) *(only once this jurisdiction is known)* | `150 S.W.3d 1`; `807 S.W.2d 476` | `ky-cases-justia` |
| Discretionary review (Kentucky parenthetical) | `disc. rev. denied (Ky. Mar. 15, 2023)`; `discretionary review denied (Ky. 2023)` | `ky-sc-minutes` |
| Discretionary review (bare) *(only once this jurisdiction is known)* | `disc. rev. denied`; `discretionary review granted` | `ky-sc-minutes` |

Regexes (case-insensitive):

- Kentucky Revised Statutes (KRS): `(?:\bKRS|Ky\.\s*Rev\.\s*Stat\.(?:\s*Ann\.)?)\s*(?:§+\s*)?(?P<chapter>\d{1,3}[A-Z]?)\.(?P<section>\d{2,4}[A-Z]?(?:-\d{2,4}(?![.\d]))?)(?!\d)|(?:\bKRS|Ky\.\s*Rev\.\s*Stat\.(?:\s*Ann\.)?)\s+[Cc]h(?:apter|\.)\s*(?P<chapter_only>\d{1,3}[A-Z]?)\b|(?:[Ss]ec(?:tion|\.)|§)\s*(?P<chapter2>\d{1,3}[A-Z]?)\.(?P<section2>\d{2,4}[A-Z]?(?:-\d{2,4}(?![.\d]))?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Kentucky\s+Revised\s+Statutes`
- Kentucky Acts (session laws): `(?P<year>\d{4})\s+Ky\.\s*Acts\.?\s*(?:ch\.|chapter)\s*(?P<chapter>\d+)`
- Kentucky Constitution: `Ky\.\s*Const\.\s*(?:§+|sec(?:tion|s?\.))\s*(?P<section>\d+[A-Za-z]?)|Section\s+(?P<section2>\d+[A-Za-z]?)\s+of\s+the\s+(?:Kentucky\s+Constitution|Constitution\s+of\s+Kentucky)|Kentucky\s+Constitution,?\s+(?:Section|§)\s*(?P<section3>\d+[A-Za-z]?)`
- Kentucky Rules of Civil Procedure (CR, dotted form): `(?<![A-Za-z.])CR\s+(?P<rule>\d{1,2}\.\d{2,3})|Ky\.\s*R\.\s*Civ\.\s*P\.\s*(?P<rule2>\d{1,2}(?:\.\d{2,3})?)`
- Kentucky Rules of Criminal Procedure (RCr): `\bRCr\s+(?P<rule>\d{1,2}\.\d{2,3})|Ky\.\s*R\.\s*Crim\.\s*P\.\s*(?P<rule2>\d{1,2}(?:\.\d{2,3})?)`
- Kentucky Rules of Evidence (KRE): `\bKRE\s+(?P<rule>\d{3}[A-Z]?)|Ky\.\s*R\.\s*Evid\.\s*(?P<rule2>\d{3}[A-Z]?)`
- Kentucky Rules of Appellate Procedure (Ky. RAP): `Ky\.\s*RAP\s*(?P<rule>\d{1,2})|Ky\.\s*R\.\s*App\.\s*P\.\s*(?P<rule2>\d{1,2})|RAP\s+(?P<rule3>\d{1,2})(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Kentucky\s+Rules\s+of\s+Appellate\s+Procedure`
- Rules of Appellate Procedure (bare RAP): `\bRAP\s+(?P<rule>\d{1,2})(?!\.\d)`
- Rules of the Supreme Court of Kentucky (SCR): `(?:Ky\.\s*)?\bSCR\s+(?P<rule>\d\.\d{3})(?:[-(](?P<subrule>\d+\.\d+[a-z]?)\)?)?`
- Civil Rules (bare CR without dotted number): `(?<![A-Za-z.])CR\s+(?P<rule>\d{1,2})(?![.\d])`
- Kentucky Administrative Regulations (KAR): `(?P<title>\d{1,3})\s+(?:KAR|Ky\.\s*Admin\.\s*Regs\.)\s+(?P<chapter>\d{1,3}):(?P<reg>\d{1,3})(?P<emergency>E)?`
- Administrative Register of Kentucky (Ky.R.): `(?P<volume>\d{1,2})\s+Ky\.\s?R\.\s+(?P<page>\d+)`
- Kentucky cases, South Western Reporter with Kentucky parenthetical: `(?P<volume>\d{1,4})\s+S\.\s?W\.(?:\s?(?P<series>2d|3d))?\s+(?P<page>\d+)(?:,\s*\d+(?:-\d+)?)?\s*\((?P<court>(?:Ky\.\s*(?:Ct\.\s*)?App\.|Ky\.))\s*(?P<year>\d{4})\)`
- Kentucky Reports (official, to 1951): `(?P<volume>\d{1,3})\s+Ky\.\s+(?P<page>\d+)(?![\d.])`
- Kentucky unpublished / Westlaw opinion with Kentucky parenthetical: `(?P<year>\d{4})\s+WL\s+(?P<number>\d+)\s*\((?P<court>(?:Ky\.\s*(?:Ct\.\s*)?App\.|Ky\.))\s+[A-Z][a-z]{2,4}\.?\s+\d{1,2},\s+\d{4}\)`
- Kentucky appellate docket numbers: `(?P<year>(?:19|20)\d{2})-(?P<court>SC|CA)-(?P<number>\d{3,6})-(?P<type>MR|DGE|DG|DE|D|WC|ME|OA|KB|TG|CL|KP|NA)\b`
- South Western Reporter (bare, no court parenthetical): `(?P<volume>\d{1,4})\s+S\.\s?W\.(?:\s?(?P<series>2d|3d))?\s+(?P<page>\d+)`
- Discretionary review (Kentucky parenthetical): `(?:disc\.\s*rev\.|discretionary\s+review)\s+(?P<disposition>denied|granted|dismissed)\s*\(Ky\.`
- Discretionary review (bare): `(?:disc\.\s*rev\.|discretionary\s+review)\s+(?P<disposition>denied|granted|dismissed)`

Short forms → URL key:

KRS → `KRS`; Ky. Rev. Stat. → `KRS`; Ky. Rev. Stat. Ann. → `KRS`; KAR → `KAR`; Ky. Admin. Regs. → `KAR`; Ky.R. → `KyR`; CR → `CR`; Ky. R. Civ. P. → `CR`; RCr → `RCr`; Ky. R. Crim. P. → `RCr`; KRE → `KRE`; Ky. R. Evid. → `KRE`; RAP → `RAP`; Ky. R. App. P. → `RAP`; SCR → `SCR`

KRS sections are chapter.section (413.140, 342.0011, 422A.0702) and the insurance code uses chapter.article-section (304.20-450); chapters can carry a letter suffix (15A, 164A, 422A). 'KRS 311.530 to 311.620' or '311.530-311.620' is a range: the regex takes the first section, and the -NNN tail only binds to 2-4 digit article-section forms after a dot. KRS URLs are not constructible: statute.aspx?id= is an opaque id read from the chapter page. KRE are numbered rules (KRE 702); KRS chapter 422A holds only 'Renumbered as KRE nnn' stubs, so KRE text is not on the legislature site. Kentucky court rules carry no state marker in practice ('CR 12.02(f)', 'RCr 11.42', 'KRE 702', 'SCR 3.130(1.7)', 'RAP 41'). The dotted CR NN.NN, RCr, KRE and SCR d.ddd forms are treated as distinctive. Bare 'RAP 41' is shared with Washington's RAP and bare 'CR 56' with Washington's CR, so both are context_required. SCR is matched only in the d.ddd form, which keeps Wisconsin 'SCR 20:1.7' and other states' SCR forms out. Kentucky style is '(Ky. App. 2021)'; Bluebook is '(Ky. Ct. App. 2021)'. Before 1976 the Court of Appeals was the highest court, so cite '(Ky. 1970)'. No public-domain citation. Dockets: YYYY-SC-NNNNNN-XX and YYYY-CA-NNNNNN-XX, with type suffixes MR (matter of right), DG/DGE (discretionary review granted), WC (workers' comp), ME, OA (original action), KB (bar), TG (transfer granted). The suffix list keeps Mississippi '-COA/-SCT' and Florida trial '-CA-...-O' numbers out. Unpublished opinions are cited under RAP 41 (formerly CR 76.28(4)(c)); they must be attached to the brief and usually carry a WL cite. 'disc. rev. denied' is Kentucky's subsequent-history phrase, but North Carolina uses 'disc. review denied', so the bare form is context_required. CourtListener ids are from memory and unverified. Kentucky Acts before 1998 are not on the LRC Acts site (98RS is its first session): '1942 Ky. Acts ch. 208' routes to ky-acts-lrc only for 1998+; earlier Acts are absent (link-free citation). Docket suffixes also include -D and -DE (motions in the Supreme Court minutes). Constitution prose forms 'Section 2 of the Constitution of Kentucky' and 'Ky. Const. sec. 14' are matched.

## A. Statutes / code

### `ky-acts-lrc` — Acts of the Kentucky General Assembly (session laws)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kentucky Legislative Research Commission · text: **fetch-and-quote** · official: unknown
- **Coverage:** Regular and extraordinary sessions 1998 (98RS) through the 2026 Regular Session; nothing earlier on this host. Each session has a whole-volume PDF and per-chapter PDFs.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://apps.legislature.ky.gov/law/acts/{yy}RS/documents/{chapter4}.pdf`
  - Placeholders: {yy} = last two digits of the session year; {chapter4} = Acts chapter zero-padded to 4 digits (2024 Ky. Acts ch. 1 -> 24RS/documents/0001.pdf). Extraordinary sessions use {yy}SS (22SS seen on the index), so check KyActs.aspx for the session code. Table by chapter: /law/acts/{yy}RS/acts_table_by_chapter.html; full volume: /law/acts/{yy}RS/actsmas.pdf.
  - Index: `https://legislature.ky.gov/Law/Pages/KyActs.aspx`
- **Automation:** WebFetch untested · shell ok · robots: apps.legislature.ky.gov: 404 (no rules)
  - Built URLs would be gated for WebFetch; use fetch_doc.py.
- **Currency:** KyActs.aspx session list — observed: "2026 Regular Session"
- **Official status:** No authentication statement seen on the Acts pages (https://legislature.ky.gov/Law/Pages/KyActs.aspx).
- **Hazard:** whole-session volume PDFs (actsmas.pdf) are very long; use per-chapter PDFs
- **Hazard:** coverage starts 1998: pre-1998 Acts (e.g. 1942 Ky. Acts ch. 208) are not here and have no free routed source; cite them link-free from the KRS history line
- **Probe:** 2024 Ky. Acts ch. 1 → `https://apps.legislature.ky.gov/law/acts/24RS/documents/0001.pdf` — expect: "CHAPTER 1 ( HB 161 ) AN ACT"
- **Evidence (2026-10-17):** fetch_doc.py --research: 24RS/documents/0001.pdf PDF 1 p, 1,413 chars, 'CHAPTER 1 ( HB 161 ) AN ACT'; second citation 2023 Ky. Acts ch. 5 -> 23RS/documents/0005.pdf, 2 pp, 'CHAPTER 5 ( SB 72'. Chapter links confirmed on acts_table_by_chapter.html. | Independent check 2026-10-17: fetch_doc.py: 24RS/documents/0001.pdf 1 p, 1,413 chars, 'CHAPTER 1'; second citation 2022 Ky. Acts ch. 100 (also 2000 Ky. Acts ch. 1) ok

### `ky-krs-lrc` — Kentucky Revised Statutes (KRS) online

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kentucky Legislative Research Commission (LRC) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All KRS chapters, current text with history notes and LRC notes; repealed and renumbered sections remain as one-line stubs.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://apps.legislature.ky.gov/law/statutes/`
  - Navigation: KRS title page (lists every chapter, 'CHAPTER 413 LIMITATION OF ACTIONS') -> chapter.aspx?id={opaque chapter id} (lists sections as '.140 Actions to be brought within one year.') -> statute.aspx?id={opaque section id}, which returns the section as a PDF. Ids are not derivable from the citation: always read them from the chapter page (fetch_doc.py links <chapter url> '^\.140 ' --regex). The title page shows chapter numbers and names only; chapter pages show every section number.
- **Automation:** WebFetch gated · shell ok · robots: apps.legislature.ky.gov/robots.txt: 404 (no rules); fetch_doc.py check: permits
  - WebFetch on a built statute.aspx URL and on the title page returned PROVENANCE_REQUIRED (not retried); WebFetch read statute.aspx?id=50197 (a search-result URL) correctly, so it handles the PDFs when the URL has provenance. Use fetch_doc.py. Sections are short PDFs (KRS 413.140: 2 pages; 342.0011: 8 pages).
- **Currency:** title page and chapter pages, under the heading; chapter pages also show the database update date — observed: "Includes enactments through the 2026 Regular Session; KRS database was last updated on 10/17/2026"
- **Official status:** KRS page notice: the statutes on the site are 'an unofficial posting' and 'do not constitute official text'; the certified versions are to be consulted (https://legislature.ky.gov/Law/Statutes/Pages/default.aspx). The Certified Versions page says that under KRS 7.138(2) only the official LRC database or a certified print version (LexisNexis, Thomson Reuters) may be cited in court (https://legislature.ky.gov/Law/Statutes/Pages/KRSEDS.aspx). The same page bars commercial use without agreement (KRS 61.874).
- **Hazard:** unofficial online text: KRS 7.138(2) requires the official or certified version for citation in court
- **Hazard:** section ids are opaque (statute.aspx?id=58050 = 413.140): never guess, read from the chapter page
- **Hazard:** chapter-page link text is '.140 Title', without the chapter number: filter on '^\.140 '
- **Hazard:** renumbered and repealed sections return a one-line PDF stub ('422A.0702 Renumbered as KRE 702.')
- **Hazard:** history and LRC notes follow the text in the same PDF: stop quoting at 'Effective:' / 'History:'
- **Probe:** KRS 413.140 → `https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=58050` — expect: "The following actions shall be commenced within one (1) year after the cause of"
- **Evidence (2026-10-17):** fetch_doc.py --research: title page 42,632 chars -> chapter.aspx?id=39261 (KRS 413) -> statute.aspx?id=58050: PDF 2 pp, 5,536 chars, '413.140 Actions to be brought within one year.' Second citation: KRS 342.0011 via chapter.aspx?id=38914 -> statute.aspx?id=56771, PDF 8 pp, 'As used in this chapter, unless the context otherwise requires'. WebFetch on statute.aspx?id=50197 (KRS 304.20-450, a repealed stub): read correctly. | Independent check 2026-10-17: fetch_doc.py: statute.aspx?id=58050 'The following actions shall be commenced within one (1) year'; second citation KRS 186.010 ok
- **Notes:** KRS citations in the certified editions are 'KRS 413.140'; Bluebook uses 'Ky. Rev. Stat. Ann. § 413.140 (West 20xx)'.

### `ky-krs-justia` — Kentucky Revised Statutes on Justia

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** KRS 2025 edition (unyeared URLs); earlier years 2023, 2024 and 2012 back to about 2011.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/kentucky/chapter-{chapter}/section-{chapter}-{section}/`
  - Placeholders: {chapter} as cited, letter suffix kept lower-case (assumed: 422a); {section} = the digits after the dot, so 413.140 becomes chapter-413/section-413-140. NOT constructible for insurance-code article-sections (304.12-230): section-304-12-230 fails, and the chapter-304 page lists no 304.NN-NNN sections. Route those to ky-krs-lrc only. Unyeared URLs serve the newest edition (2025); yeared editions are at /codes/kentucky/{year}/.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com/robots.txt answers with a Cloudflare 'Just a moment...' challenge (curl 403)
  - fetch_doc.py: REFUSED (robots.txt challenge; host off for the day). WebFetch read both a linked and a built URL.
- **Currency:** page heading / breadcrumb — observed: "2025 Kentucky Revised Statutes"
- **Official status:** Third-party compilation; the page says 'These codes may not be the most recent version.'
- **Hazard:** tier 2: disclose the edition year; lags the LRC database by up to a session
- **Hazard:** KRS 304.NN-NNN (insurance code subtitles) not reachable on Justia: chapter-304/section-304-12-230 failed (2026-10-17); use ky-krs-lrc
- **Probe:** KRS 413.140 → `https://law.justia.com/codes/kentucky/chapter-413/section-413-140/` — expect: "The following actions shall be commenced within one (1) year"
- **Evidence (2026-10-17):** WebFetch: KRS 413.140 YES, 'The following actions shall be commenced within one (1) year', '2025 Kentucky Revised Statutes'. Second citation: KRS 57.320 at /codes/kentucky/chapter-57/section-57-320/ YES, 'The state law librarian, under direction of the Supreme Court'. | Independent check 2026-10-17: WebFetch: YES 'The following actions shall be commenced within one (1) year'; '2025 Kentucky Revised Statutes'; second citation KRS 186.010 (ok); KRS 304.12-230 (failed) ok

## B. Constitution

### `ky-constitution-lrc` — Constitution of Kentucky

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kentucky Legislative Research Commission · text: **fetch-and-quote** · official: unknown
- **Coverage:** The 1891 Constitution as amended, sections 1-263 plus the schedule.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://apps.legislature.ky.gov/law/constitution`
  - Navigation: The index page lists every section as 'Section 115 ... Right of appeal -- Procedure.' and links it to /Law/Constitution/Constitution/ViewConstitution?rsn={opaque id}. The rsn is not the section number (Section 1 = rsn 3, Section 115 = rsn 131), so read it from the index (fetch_doc.py links <index> '^Section 115 ' --regex). Each link returns a one-section PDF.
- **Automation:** WebFetch untested · shell ok · robots: apps.legislature.ky.gov: 404 (no rules)
  - Built URLs would be gated for WebFetch (same host as the KRS).
- **Currency:** index page heading — observed: "(Includes Amendments Ratified On or Before November 5, 2024)"
- **Official status:** The index page gives no authentication statement (https://apps.legislature.ky.gov/law/constitution).
- **Hazard:** rsn ids are opaque and offset from the section numbers
- **Probe:** Ky. Const. § 115 → `https://apps.legislature.ky.gov/Law/Constitution/Constitution/ViewConstitution?rsn=131` — expect: "In all cases, civil and criminal, there shall be allowed as a matter of right"
- **Evidence (2026-10-17):** fetch_doc.py --research: index 36,907 chars; Section 115 -> rsn=131, PDF 1 p, 838 chars, 'Section 115 Right of appeal -- Procedure.' Index links for Sections 1, 2 and 110 resolve to rsn 3, 4 and 121. | Independent check 2026-10-17: fetch_doc.py: rsn=131 'In all cases, civil and criminal, there shall be allowed'; second citation Ky. Const. § 27 ok

### `ky-constitution-justia` — Kentucky Constitution on Justia

- **Status:** REPORTED 2026-10-17 · **Tier 2** · Justia · text: **link-only** · official: unofficial
- **Coverage:** Sections grouped by subject on list pages (list1.html ...).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Index: `https://law.justia.com/constitution/kentucky/`
  - Navigation: index -> grouped list page with subject anchors (list1.html#Appellate for Sections 115-116). The list page shows section titles only, NOT section text; per-section page URLs are not known. Link-only until a section page is found.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com: Cloudflare challenge on robots.txt
  - Only the index was fetched; no section text was probed.
- **Currency:** index page — observed: "This Constitution may not be the most recent version."
- **Official status:** Page: 'This Constitution may not be the most recent version.'
- **Hazard:** sections are grouped several to a page under subject anchors
- **Hazard:** list pages hold titles only: independent check 2026-10-17 found no Section 115 text at list1.html#Appellate
- **Probe:** Ky. Const. § 115 → `https://law.justia.com/constitution/kentucky/list1.html#Appellate` — expect: "In all cases, civil and criminal"
- **Evidence (2026-10-17):** WebFetch: index YES, grouped entry 'Appellate Policy -- Rule-Making Power - Sections 115 and 116' -> list1.html#Appellate; section text not fetched. | Independent check 2026-10-17: list1.html#Appellate gave section titles only, no Section 115 body text; stays reported.

## C. Court rules

### `ky-rules-orders-kycourts` — Supreme Court of Kentucky orders adopting and amending rules

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kentucky Court of Justice (Supreme Court) · text: **fetch-and-quote** · official: official
- **Coverage:** Supreme Court orders from about 2005 to now (rule adoptions and amendments for CR, RCr, KRE, RAP, SCR, FCRPP, and administrative procedures). These are amendment texts, not a consolidated rulebook, except that Order 2022-49 sets out the full RAP as adopted.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.kycourts.gov/Courts/Supreme-Court/Supreme%20Court%20Orders/{year}{order2}.pdf (extension may be .PDF: take it from the link)`
  - Index: `https://www.kycourts.gov/Courts/Supreme-Court/Pages/Administrative-Orders.aspx`
  - Navigation: The Administrative Orders page lists every order by year with its title ('Amending Supreme Court Rule 2.112 2026 - 2026-36 Order'). It links /Courts/Supreme-Court/Supreme Court Orders/{yyyy}{nn}.pdf (order 2026-01 -> 202601.pdf). Find the latest order amending the rule by title, then read the PDF. The Court of Appeals page links the RAP adopting order directly as 'Rules of Appellate Procedure'. fetch_doc.py links prints these URLs with spaces ('Supreme Court Orders/202615.pdf'); current fetch_doc.py percent-encodes them, but encode spaces as %20 if passing them elsewhere. Some files end in .PDF (201808.PDF): filter links case-insensitively (fetch_doc.py links <page> '(?i)\.pdf' --regex) and take the extension from the link.
- **Automation:** WebFetch ok (truncated) · shell ok · robots: www.kycourts.gov/robots.txt: Azure Front Door 403 'The request is blocked.' to plain curl; fetch_doc.py check reports 'robots.txt permits' and fetches pages 200
  - WebFetch read 202601.pdf in full and stopped Order 2022-49 (89 pp) mid-RAP 32: 'RAP 41 NOT PRESENT'. fetch_doc.py reads the whole PDF (205,517 chars).
- **Currency:** each order's caption and effective-date sentence — observed: "amendments ... shall be effective April 1, 2026 (Order 2026-01)"
- **Official status:** The orders are the Supreme Court's own signed orders promulgating the rules (e.g. Order 2022-49 creating the RAP, effective January 1, 2023).
- **Hazard:** amendment orders only: the current text of a rule is the base order plus every later amending order
- **Hazard:** Order 2022-49 is cut off by WebFetch at RAP 32 of 75
- **Hazard:** order PDFs mix several rule sets (RAP plus CR/RCr/FCRPP amendments)
- **Hazard:** file extension varies (.pdf / .PDF): never build the name, take it from the Administrative Orders page
- **Probe:** RAP 41 → `https://www.kycourts.gov/Courts/Supreme-Court/Supreme%20Court%20Orders/202249.pdf` — expect: "Order Creating Rules of Appellate Procedure and Amending Rules of Civil Procedure"
- **Evidence (2026-10-17):** fetch_doc.py --research: 202249.pdf 89 pp, 205,517 chars, last-modified 2022-10-25, opens 'IN RE: Order Creating Rules of Appellate Procedure'; 202601.pdf 12 pp 'amendments to the Rules of Appellate Procedure shall be effective April 1, 2026'. WebFetch on 202601.pdf: complete; on 202249.pdf: truncated at RAP 32(E)(1)(b). | Independent check 2026-10-17: fetch_doc.py: 202249.pdf 89 pp, 'Order Creating Rules of Appellate Procedure and Amending Rules of Civil Procedure'; second citation CR 3.02 (Order 2026-15) ok

### `ky-rules-westlaw` — Kentucky Rules of Court (CR, RCr, KRE, RAP, SCR, FCRPP) on Westlaw govt

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Thomson Reuters for the Kentucky Supreme Court · text: **link-only** · official: unknown
- **Coverage:** Consolidated current text of all Kentucky court rules: the only consolidated free source.
- **Access:** `link-only` · format html
  - Index: `https://govt.westlaw.com/kyrules/Index?transitionType=Default&contextData=%28sc.Default%29`
- **Automation:** WebFetch gated · shell blocked-challenge · robots: govt.westlaw.com answers robots.txt with a bot challenge (fetch_doc.py REFUSED, 2026-10-17)
  - Not attempted with WebFetch (a built or script-derived URL would be gated; other records report WebFetch SITE_BLOCKED on this host). Not retried by any route.
- **Currency:** none observed — observed: "not fetched"
- **Official status:** kycourts.gov links it as 'Supreme Court Rules & Procedures (Westlaw)' and 'West's Rules & Procedures' (https://www.kycourts.gov/Courts/Pages/Rules-of-Practice.aspx).
- **Hazard:** blocked host: cite the rule and link it, never quote from it
- **Probe:** CR 12.02 → `https://govt.westlaw.com/kyrules/Index?transitionType=Default&contextData=%28sc.Default%29` — expect: "n/a (blocked)"
- **Evidence (2026-10-17):** fetch_doc.py --research: 'REFUSED: govt.westlaw.com refused automated access earlier (robots.txt challenge, 2026-10-17T09:38:19)'. | Re-confirmed blocked 2026-10-17: WebFetch PROVENANCE_REQUIRED (unanswered); fetch_doc.py check: REFUSED robots.txt bot check

## D. Administrative code

### `ky-kar-lrc` — Kentucky Administrative Regulations (KAR)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kentucky Legislative Research Commission · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All current KAR titles (001-922), with emergency (E) and in-process versions; the PDFs carry the Register history line.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://apps.legislature.ky.gov/law/kar/titles/{title3}/{chapter3}/{reg3}/`
  - Placeholders: Zero-pad title, chapter and regulation to 3 digits: 201 KAR 9:260 -> titles/201/009/260/; 13 KAR 2:020 -> titles/013/002/020/ (titles/13/... is 404). The page links 'Download PDF' -> /law/kar/downloads/docs/{opaque doc id}/document.engrossed.pdf (read that link from the page). Emergency regulations (E suffix) are not at .../005E/ (404): use the chapter page or EmergencyRegs.aspx.
  - Index: `https://apps.legislature.ky.gov/law/kar/titles.htm`
- **Automation:** WebFetch gated · shell ok · robots: apps.legislature.ky.gov: 404 (no rules)
  - WebFetch read a KAR engrossed PDF from a search result; built regulation URLs are expected to be gated, as on the KRS pages. HTML pages are long (401 KAR 5:005: 164,689 chars) because the text appears twice: prefer the engrossed PDF.
- **Currency:** KAR home page notice — observed: "Administrative regulations are updated approximately once a month"
- **Official status:** KAR home: 'Unofficial WWW Version'; the regulations are 'an unofficial posting' of the LRC's official internal database (https://legislature.ky.gov/Law/kar/Pages/default.aspx).
- **Hazard:** the HTML page holds two copies of the text (an 'ALTERNATE VIEW' pre-engrossment copy first, then the engrossed text): quote from the engrossed PDF
- **Hazard:** some generated PDFs for old repealers contain only 'Not available' placeholders
- **Hazard:** history line '(47 Ky.R. 374, 944; eff. 11-19-2020.)' ends the text; 'Crt to Am' notes signal a pending amendment
- **Hazard:** the 'Download PDF' can be a pending amendment: if the heading carries '(Amendment)' or the history line ends without an 'eff.' date for the latest Ky.R. filing, it is not yet in force (907 KAR 1:005, docs/10618, modified 2026-10-17). Check the heading and prefer the in-force text (history line ending in 'eff. <date>')
- **Probe:** 201 KAR 9:260 → `https://apps.legislature.ky.gov/law/kar/titles/201/009/260/` — expect: "Section 1. Applicability. (1) Any licensee who is authorized to prescribe, dispense, or administer"
- **Evidence (2026-10-17):** fetch_doc.py --research: titles/201/009/260/ html 59,500 chars, '201 KAR 9:260.Professional standards for prescribing'; its 'Download PDF' docs/1885/document.engrossed.pdf has 8 pp, 30,012 chars and ends '47 Ky.R. 374, 944; eff. 11-19-2020.' Second and third: 401 KAR 5:005 (titles/401/005/005/, 164,689 chars) and 13 KAR 2:020 (titles/013/002/020/) ok. WebFetch on docs/845/document.engrossed.pdf (search result) matched the script (placeholder repealer). | Independent check 2026-10-17: fetch_doc.py: titles/201/009/260/ 'Section 1. Applicability. (1) Any licensee who is authorized'; second citation 907 KAR 1:005 ok

### `ky-kar-lii` — Kentucky Administrative Regulations on Cornell LII

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute (Cornell) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All KAR titles; the pages fetched were last modified 2025-08-02, so the copy may be stale.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/kentucky/{title}-KAR-{chapter}-{reg}`
  - Placeholders: Unpadded numbers as cited: 201 KAR 9:260 -> 201-KAR-9-260.
  - Index: `https://www.law.cornell.edu/regulations/kentucky`
- **Automation:** WebFetch untested · shell ok · robots: www.law.cornell.edu: User-agent * Crawl-delay 10; regulations paths allowed
- **Currency:** foot of the regulation page — observed: "State regulations are updated quarterly; we currently have two versions available."
- **Official status:** Third-party compilation; the page says 'State regulations are updated quarterly'.
- **Hazard:** last-modified 2025-08-02 on the pages probed: check against the LRC page
- **Probe:** 201 KAR 9:260 → `https://www.law.cornell.edu/regulations/kentucky/201-KAR-9-260` — expect: "Section 1. Applicability. (1) Any licensee who is authorized to prescribe"
- **Evidence (2026-10-17):** fetch_doc.py --research: 201-KAR-9-260 html 32,166 chars, 'Section 1. Applicability.' present; 401-KAR-5-005 html 87,808 chars. | Independent check 2026-10-17: fetch_doc.py: 201-KAR-9-260 'Section 1. Applicability.' present; last-modified 2025-08-02; second citation 907 KAR 1:005 ok

## D. Administrative register

### `ky-register-lrc` — Administrative Register of Kentucky

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kentucky Legislative Research Commission · text: **fetch-and-quote** · official: unknown
- **Coverage:** Monthly issues, each volume running July-June (Volume 53 = 2026-27), with archive volumes listed on the same page.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://legislature.ky.gov/Law/kar/Pages/Registers.aspx`
  - Navigation: The Registers page lists each issue by month: apps.legislature.ky.gov/law/kar/registers/{vol}Ky_R_{yyyy}-{yy}/{nn}_{Mon}.pdf (53Ky_R_2026-27/04_Oct.pdf). Month spellings vary ('01_July', '02_Aug', '03_Sep'), so take the link from the page. Ky.R. page numbers run through the volume, so find the issue for a page from the issue's page range. The Registers page shows no page ranges: open issues in the volume and read each one's page range from its cover/contents, or narrow by the date in the history line.
- **Automation:** WebFetch untested · shell ok · robots: legislature.ky.gov: 403 'The request is blocked.' to plain curl; fetch_doc.py check permits
  - Issues are huge (Oct 2026: 242 pp, 2.2M chars): use fetch_doc.py grep, not WebFetch.
- **Currency:** cover page — observed: "VOLUME 53, NUMBER 4 ... OCTOBER 1, 2026"
- **Official status:** The Register is the LRC's own monthly publication under KRS Chapter 13A; no authentication statement seen.
- **Hazard:** very long PDFs: WebFetch will truncate
- **Hazard:** Ky.R. cites give volume and page, not month
- **Hazard:** no page-range index: mapping a Ky.R. page to an issue means opening issues
- **Probe:** 53 Ky.R. (Oct. 2026) → `https://apps.legislature.ky.gov/law/kar/registers/53Ky_R_2026-27/04_Oct.pdf` — expect: "VOLUME 53, NUMBER 4"
- **Evidence (2026-10-17):** fetch_doc.py --research: 04_Oct.pdf 242 pp, 2,211,430 chars, last-modified 2026-10-01, opens 'VOLUME 53, NUMBER 4 ... ADMINISTRATIVE REGISTER OF KENTUCKY'. | Independent check 2026-10-17: fetch_doc.py: 04_Oct.pdf 242 pp, 'VOLUME 53, NUMBER 4'; second citation 52 Ky.R. (Dec. 2025 issue) ok

## E. Case law

### `ky-coa-minutes` — Court of Appeals of Kentucky minutes (opinions rendered)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kentucky Court of Justice (Court of Appeals Clerk) · text: **fetch-and-quote** · official: official
- **Coverage:** Weekly minutes for 2026 (through Oct. 9, 2026 at check) and earlier years. Each entry gives the case, CA docket, county, 'TO BE PUBLISHED' / 'NOT TO BE PUBLISHED', the disposition and the panel.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.kycourts.gov/Courts/Court-of-Appeals/Pages/Court-of-Appeals-Minutes.aspx`
  - Navigation: The minutes page lists weekly dates -> apps.kycourts.net/Appeals/Minutes/MNT{mm}{dd}{yyyy}.pdf. Grep for the docket (2024-CA-1103-MR) to get the rendition date and publication status, then read the text on Justia (ky-cases-justia).
  - Read via: ky-cases-justia (opinion text); the official text hosts fail (ky-opinions-kycourts-legacy TLS error; ky-opinions-appellatepublic JS app)
- **Automation:** WebFetch untested · shell ok · robots: apps.kycourts.net: fetch_doc.py permits
- **Currency:** PDF heading — observed: "JANUARY 09, 2026 MINUTES RELEASED: 10:00 A.M."
- **Official status:** The Clerk's official minutes of opinions rendered each Friday.
- **Hazard:** minutes only, not opinion text
- **Probe:** 2024-CA-1103-MR → `https://apps.kycourts.net/Appeals/Minutes/MNT01092026.pdf` — expect: "NOT TO BE PUBLISHED OPINION AFFIRMING"
- **Evidence (2026-10-17):** fetch_doc.py --research: MNT01092026.pdf 8 pp, 9,792 chars; '2024-CA-1103-MR ALLEN ELLIOT YOUNG, ET AL. NOT TO BE PUBLISHED OPINION AFFIRMING'. | Independent check 2026-10-17: fetch_doc.py: '2024-CA-1103-MR ALLEN ELLIOT YOUNG ... NOT TO BE PUBLISHED OPINION AFFIRMING'; second citation 2024-CA-0287-MR (Aug. 28, 2026) ok

### `ky-opinions-appellatepublic` — Kentucky appellate public access portal (dockets, documents, opinions)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Kentucky Court of Justice · text: **link-only** · official: unknown
- **Coverage:** Appellate case search with docket entries, documents and an opinions search type (from the app's JavaScript labels).
- **Access:** `search-only` · format json
  - Index: `https://appellatepublic.kycourts.net/`
- **Automation:** WebFetch untested · shell http-error · robots: fetch_doc.py check: robots.txt permits
  - The page is a Vue app shell (0 chars of text). properties.js sets apiRoot '/api/api/v1'; /api/api/v1/searches/types returned HTTP 500 to fetch_doc.py.
- **Currency:** n/a — observed: "not reached"
- **Official status:** Court of Justice public-access application (the page title is 'publicaccess').
- **Hazard:** JavaScript-only app: no text without the API
- **Probe:** n/a → `https://appellatepublic.kycourts.net/` — expect: "n/a"
- **Evidence (2026-10-17):** fetch_doc.py --research: 200, html 0 chars (app shell); API probe HTTP 500. | Independent check 2026-10-17: WebFetch PROVENANCE_REQUIRED; fetch_doc.py: 200, html 0 chars (app shell), as recorded

### `ky-opinions-kycourts-legacy` — Kentucky Court of Justice searchable opinions (dtSearch)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Kentucky Court of Justice · text: **link-only** · official: unknown
- **Coverage:** Supreme Court and Court of Appeals slip opinions (coverage not confirmed).
- **Access:** `search-only` · format pdf
  - Index: `http://opinions.kycourts.net/dtsearch.html`
- **Automation:** WebFetch gated · shell tls-error · robots: not readable: robots.txt connection reset (curl); TLS chain fails for fetch_doc.py
  - fetch_doc.py: 'TLS certificate chain does not verify'. WebFetch on the linked dtsearch.html: PROVENANCE_REQUIRED (not retried).
- **Currency:** not reached — observed: "not fetched"
- **Official status:** Linked as 'Searchable Opinions' from the Court of Appeals page (https://www.kycourts.gov/Courts/Court-of-Appeals/Pages/default.aspx).
- **Hazard:** TLS failure: not usable by script
- **Probe:** n/a → `http://opinions.kycourts.net/dtsearch.html` — expect: "search form"
- **Evidence (2026-10-17):** fetch_doc.py: TLS error; WebFetch: PROVENANCE_REQUIRED. | Independent check 2026-10-17: WebFetch PROVENANCE_REQUIRED; fetch_doc.py: TLS certificate chain does not verify, as recorded

### `ky-cases-justia` — Kentucky Supreme Court and Court of Appeals opinions on Justia

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court of Kentucky 1976-2026; Court of Appeals 1894-2026 (before 1976 the Court of Appeals was the highest court).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Index: `https://law.justia.com/cases/kentucky/`
  - Navigation: /cases/kentucky/{supreme-court|court-of-appeals}/{year}/ lists cases with docket and date -> /{year}/{docket-lower}.html (2024-ca-0287-mr.html; older ones may use a 6-digit docket and a '-1' suffix). The case page links the slip PDF at cases.justia.com/kentucky/{court}/{year}-{docket}.pdf?ts=... , which fetch_doc.py reads.
  - Read via: cases.justia.com slip PDF: fetch_doc.py ok
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com: Cloudflare challenge on robots.txt; cases.justia.com permitted
  - Use WebFetch on law.justia.com pages; use fetch_doc.py on the cases.justia.com PDF link taken from the page.
- **Currency:** year listing — observed: "Kentucky Court of Appeals 2026 (latest year listed)"
- **Official status:** Third-party host; the attached PDF is the court's slip opinion (cases.justia.com).
- **Hazard:** slip pagination only (no S.W.3d pin pages)
- **Hazard:** unpublished opinions are included: check the 'NOT TO BE PUBLISHED' header (RAP 41)
- **Probe:** Scotty's Contracting & Stone, LLC v. Graves, No. 2024-CA-0287-MR (Ky. App. Aug. 28, 2026) → `https://law.justia.com/cases/kentucky/court-of-appeals/2026/2024-ca-0287-mr.html` — expect: "appeals the Barren Circuit Court's"
- **Evidence (2026-10-17):** WebFetch: full text YES, 'TO BE PUBLISHED', Aug. 28, 2026, not truncated; PDF link cases.justia.com/kentucky/court-of-appeals/2026-2024-ca-0287-mr.pdf. fetch_doc.py on that PDF: 48 pp, 79,135 chars, 'RENDERED: AUGUST 28, 2026; 10:00 A.M. TO BE PUBLISHED'. Supreme Court listing (2000) shows docket and date. | Independent check 2026-10-17: WebFetch: YES, 'appeals the Barren Circuit Court's', 'TO BE PUBLISHED', not truncated; second citation Jordan v. Commonwealth, No. 2025-SC-0115-MR (Ky. Sept. 24, 2026) ok

## F. Subsequent history

### `ky-sc-minutes` — Supreme Court of Kentucky minutes (opinions rendered and motions for discretionary review)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Kentucky Court of Justice (Supreme Court Clerk) · text: **fetch-and-quote** · official: official
- **Coverage:** Monthly minutes from about 2009 (MNT01222009.pdf) to now. They list each opinion rendered (case, docket, county, publication status, author, disposition) and the orders granting and denying discretionary review.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.kycourts.gov/Courts/Supreme-Court/Pages/Supreme-Court-Minutes.aspx`
  - Navigation: The minutes page lists months by year -> apps.kycourts.net/Supreme/Minutes/MNT{mm}{yyyy}.pdf (special renditions MNT{mm}{dd}{yyyy}.pdf; older files use other date forms). Grep the PDF for the party name or the SC docket. Sections are headed 'ORDER GRANTING DISCRETIONARY REVIEW' and 'ORDER DENYING DISCRETIONARY REVIEW' with dates. The minutes give the Supreme Court docket and county, NOT the Court of Appeals docket, so a disposition below is found by party name.
- **Automation:** WebFetch untested · shell ok · robots: apps.kycourts.net: fetch_doc.py permits
- **Currency:** each PDF's heading (minutes date) — observed: "MNT092026.pdf last-modified Thu, 24 Sep 2026"
- **Official status:** The Clerk's official minutes of the Court's dispositions.
- **Hazard:** Court of Appeals docket not listed: search by party name
- **Hazard:** monthly files can run 17+ pages
- **Hazard:** the index links future months before they are issued (MNT102026.pdf was an 84-char placeholder): check the file length
- **Hazard:** motion dockets use -D and -DE suffixes (2025-SC-0239-D, 2026-SC-0231-DE)
- **Probe:** 2025-SC-0115-MR → `https://apps.kycourts.net/Supreme/Minutes/MNT092026.pdf` — expect: "ORDER DENYING DISCRETIONARY REVIEW - September 16, 2026"
- **Evidence (2026-10-17):** fetch_doc.py --research: MNT092026.pdf 17 pp, 24,004 chars; '2025-SC-0115-MR FAYETTE ... TO BE PUBLISHED OPINION OF THE COURT'; 'ORDER GRANTING DISCRETIONARY REVIEW (ORAL ARGUMENT) - September 16, 2026'. No '-CA-' docket strings in the file. | Independent check 2026-10-17: fetch_doc.py: MNT092026.pdf 17 pp, 'ORDER DENYING DISCRETIONARY REVIEW - September 16, 2026'; second citation 2026-SC-0022-DG (DR granted June 17, 2026) ok
- **Notes:** The same minutes are the finding aid for Supreme Court opinions by (docket, date).

## Not available (do not look for these again)

- **court_rules** — Consolidated current text of CR, RCr, KRE, SCR and RAP on a reachable government host: kycourts.gov rules links go only to govt.westlaw.com/kyrules (blocked) or to adopting/amending order PDFs. KRS chapter 422A holds only 'Renumbered as KRE nnn' stubs (statute.aspx?id=18198). (2026-10-17)
- **case_law** — Public-domain (vendor-neutral) citation: Kentucky cites S.W.3d / WL with docket numbers; RAP-adopting order 2022-49 gives the citation form 'Doe v. Roe, ___ S.W.3d ___ (Ky. App. [date])'. (2026-10-17)
- **statutes** — Official bulk download / API for the KRS: No bulk link on the KRS pages; the Statutes page bars commercial use without LRC agreement (KRS 61.874). (2026-10-17)
- **statutes** — Kentucky Acts before 1998 (session laws) online free: KyActs.aspx lists sessions from 98RS to 26RS only (independent check 2026-10-17). (2026-10-17)

## Corpus candidates (maintainers)

- `ky-rules-orders-kycourts` — Full RAP as adopted (89 pp, 205K chars); WebFetch stops at RAP 32. Later amendments (e.g. Order 2026-01) must be merged in.
- `ky-register-lrc` — Monthly issues are 200+ pages (2.2M chars); grep with fetch_doc.py rather than ingest

## Open questions

- govt.westlaw.com/kyrules is blocked: is there a reachable government copy of the consolidated CR, RCr, KRE and SCR? (Check whether kycourts.gov posts rule PDFs elsewhere.)
- opinions.kycourts.net fails TLS for the script and WebFetch is gated: retest with a provenance-bearing URL (e.g. one linked from a search result).
- appellatepublic.kycourts.net API: map the opinion search endpoint (the /api/api/v1 root was seen; searches/types returned 500).
- Justia KRS URL form for article-sections (304.20-450) and letter-suffixed chapters (422A) has not been verified.
- Justia constitution section pages not probed; the constitution and KAR WebFetch rows are untested.
- Justia Kentucky Constitution: find per-section page URLs linked from list1.html; the list page itself carries no section text.
