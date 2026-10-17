# Illinois (IL) — free legal sources

_Generated from `data/il.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes, Constitution and Admin Code: the official ilga.gov host refuses both routes from this workspace (WebFetch ROBOTS_DISALLOWED, shell TLS failure), so text comes only from tier 2 — Justia (ILCS 2025, Constitution) and Cornell LII (Admin Code). Court rules, Rules of Evidence, opinions (Supreme Court from 1996, Appellate Court, Rule 23 orders) and PLA disposition lists are on illinoiscourts.gov, which links through a 302 to blob-storage PDFs that WebFetch reads but fetch_doc.py refuses (blob robots.txt 403). Opinion search is ASP.NET POST-only; RSS feeds give recent opinions by GET. Illinois has public-domain citations (2021 IL 125656; 2026 IL App (1st) 232256-U) from July 1, 2011, and the Appellate number maps to the docket (1-23-2256).

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Illinois | `ill (unverified)` | Ill. | Ill., Ill. 2d, N.E.3d, N.E.2d, N.E., Ill. Dec. | 2021 IL 125656 |
| Appellate Court of Illinois | `illappct (unverified)` | Ill. App. Ct. | Ill. App. 3d, Ill. App. 2d, Ill. App., N.E.3d, N.E.2d, Ill. Dec. | 2026 IL App (1st) 232256; Rule 23 orders 2026 IL App (1st) 251481-U |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Illinois Compiled Statutes (ILCS) | `735 ILCS 5/2-619`; `815 ILCS 505/2`; `735 ILCS 5/2-619(a)(9)`; `735 Ill. Comp. Stat. 5/2-1401`; `740 ILCS 14/15(b)`; `625 ILCS 5/11-501.1`; `section 2-619 of the Code of Civil Procedure`; `section 10a of the Consumer Fraud and Deceptive Business Practices Act`; `720 ILCS 5/12-3.05` | `il-ilcs-ilga` → `il-ilcs-justia` |
| Illinois Constitution of 1970 | `Ill. Const. 1970, art. I, § 2`; `Ill. Const. art. VI, § 4(b)`; `article I, section 12 of the Illinois Constitution`; `Ill. Const. 1970, art. XIII, § 5` | `il-constitution-ilga` → `il-constitution-justia` |
| Illinois Supreme Court Rules | `Ill. S. Ct. R. 23(e)(1) (eff. Feb. 1, 2023)`; `Illinois Supreme Court Rule 315`; `Rule 304(a) of the Illinois Supreme Court Rules`; `Ill. S. Ct. R. 6` | `il-rules-supreme` |
| Illinois Rules of Professional Conduct of 2010 | `Ill. R. Prof'l Conduct (2010) R. 1.7`; `Rule 1.15 of the Illinois Rules of Professional Conduct of 2010` | `il-rules-supreme` |
| Illinois Rules of Evidence | `Ill. R. Evid. 401 (eff. Jan. 1, 2011)`; `Illinois Rule of Evidence 702`; `Rule 803(4) of the Illinois Rules of Evidence` | `il-rules-evidence` |
| Illinois Administrative Code | `35 Ill. Adm. Code 101.100`; `86 Ill. Admin. Code 130.101`; `Ill. Admin. Code tit. 86, § 130.101` | `il-admincode-jcar` → `il-admincode-lii` |
| Illinois Register | `47 Ill. Reg. 2116 (eff. Jan. 24, 2023)`; `39 Ill. Reg. 12,848` | `il-register-sos` |
| Public-domain citations (Ill. S. Ct. R. 6, from July 1, 2011) | `Rehfield v. Diocese of Joliet, 2021 IL 125656, ¶ 26`; `2026 IL App (1st) 232256`; `Moore v. Moore, 2026 IL App (1st) 251481-U`; `2015 IL App (1st) 141234WC`; `People v. Doe, 2011 IL App (1st) 101234, ¶¶ 21-23` | `il-opinions-courts` → `il-cases-justia` |
| Reporter citations (Ill. 2d, Ill. App. 3d, Ill. Dec., N.E. with Illinois parenthetical) | `People v. Redd, 173 Ill. 2d 1 (1996)`; `123 Ill. App. 3d 456 (1st Dist. 1984)`; `189 Ill. 2d 1, 723 N.E.2d 1 (2000)`; `250 Ill. Dec. 1`; `723 N.E.2d 1 (Ill. 2000)`; `10 N.E.3d 111 (Ill. App. Ct. 2014)` | `il-opinions-courts` → `il-cases-justia` |
| Appellate Court docket numbers | `No. 1-23-2256`; `No. 2-23-0584`; `Nos. 4-19-0123` | `il-opinions-courts` → `il-cases-justia` |
| Westlaw cites with Illinois parenthetical | `2019 WL 1234567 (Ill. App. Ct. Mar. 1, 2019)` | `il-opinions-courts` → `il-cases-justia` |

Regexes (case-insensitive):

- Illinois Compiled Statutes (ILCS): `(?P<chapter>\d{1,3})\s+(?:ILCS|Ill\.\s*Comp\.\s*Stat\.(?:\s*Ann\.)?)\s*(?P<act>\d{1,4})\s*/\s*(?P<section>\d+(?:\.\d+)?[A-Za-z]?(?:-\d+(?:\.\d+)?[A-Za-z]?)*)(?![\d-])|(?:sec(?:tion|\.)|§)\s*(?P<section2>\d+(?:\.\d+)?[A-Za-z]?(?:-\d+(?:\.\d+)?[A-Za-z]?)*)(?:\([a-z0-9]+\))*\s+of\s+the\s+(?P<act_name>Code\s+of\s+Civil\s+Procedure|Code\s+of\s+Criminal\s+Procedure\s+of\s+1963|Criminal\s+Code\s+of\s+2012|Consumer\s+Fraud\s+and\s+Deceptive\s+Business\s+Practices\s+Act|Consumer\s+Fraud\s+Act|Illinois\s+Marriage\s+and\s+Dissolution\s+of\s+Marriage\s+Act|Illinois\s+Vehicle\s+Code|Illinois\s+Human\s+Rights\s+Act|Biometric\s+Information\s+Privacy\s+Act|Workers'\s+Compensation\s+Act|Illinois\s+Pension\s+Code|Probate\s+Act\s+of\s+1975|Unified\s+Code\s+of\s+Corrections|Freedom\s+of\s+Information\s+Act)`
- Illinois Constitution of 1970: `Ill\.\s*Const\.\s*(?:\(?1970\)?,?\s*)?art\.\s*(?P<article>[IVX]+),?\s*§\s*(?P<section>\d+(?:\.\d+)?)|article\s+(?P<article2>[IVX]+),\s+section\s+(?P<section2>\d+(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+(?:Illinois\s+Constitution|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Illinois)`
- Illinois Supreme Court Rules: `Ill\.\s*S(?:up)?\.\s*Ct\.\s*R\.\s*(?P<rule>\d{1,3}(?:\.\d+)?)|Illinois\s+Supreme\s+Court\s+Rule\s+(?P<rule2>\d{1,3}(?:\.\d+)?)|Rule\s+(?P<rule3>\d{1,3}(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Illinois\s+Supreme\s+Court\s+Rules`
- Illinois Rules of Professional Conduct of 2010: `Ill\.\s*R\.\s*Prof(?:'|’)?l\.?\s*Conduct\s*(?:\(2010\)\s*)?R\.\s*(?P<rule>\d\.\d+[a-z]?)|Rule\s+(?P<rule2>\d\.\d+[a-z]?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Illinois\s+Rules\s+of\s+Professional\s+Conduct`
- Illinois Rules of Evidence: `Ill\.\s*R\.\s*Evid\.\s*(?P<rule>\d{3,4})|Illinois\s+Rules?\s+of\s+Evidence\s+(?P<rule2>\d{3,4})|Rule\s+(?P<rule3>\d{3,4})(?:\([a-z0-9]+\))*\s+of\s+the\s+Illinois\s+Rules\s+of\s+Evidence`
- Illinois Administrative Code: `(?P<title>\d{1,2})\s+Ill\.\s*Adm(?:in)?\.\s*Code\s*(?:§+\s*)?(?P<section>\d{3,4}\.\d+[a-z]?)|Ill\.\s*Admin\.\s*Code\s+tit\.\s*(?P<title2>\d{1,2}),\s*§+\s*(?P<section2>\d{3,4}\.\d+[a-z]?)`
- Illinois Register: `(?P<volume>\d{1,2})\s+Ill\.\s*Reg\.\s*(?P<page>\d{1,3},\d{3}|\d+)`
- Public-domain citations (Ill. S. Ct. R. 6, from July 1, 2011): `(?P<year>(?:20)\d\d)\s+IL\s+(?:App\s+\((?P<district>1st|2d|3d|4th|5th)\)\s+)?(?P<number>\d{6})(?P<wc>WC)?(?:-(?P<suffix>U[BC]?|B|C))?(?:,\s*¶¶?\s*(?P<para>\d+))?`
- Reporter citations (Ill. 2d, Ill. App. 3d, Ill. Dec., N.E. with Illinois parenthetical): `(?P<volume>\d{1,3})\s+Ill\.\s*(?:(?P<app>App\.)\s*)?(?:(?P<series>[23])d\s+)?(?P<page>\d{1,4})(?![\d.])|(?P<decvol>\d{1,3})\s+Ill\.\s*Dec\.\s*(?P<decpage>\d{1,4})|(?P<nevol>\d{1,4})\s+N\.E\.\s*(?:[23]d\s+)?(?P<nepage>\d{1,5})(?:,\s*\d+)?\s*\((?:Ill\.(?:\s*App\.(?:\s*Ct\.)?)?)\s*(?:\d\w*\s*Dist\.\s*)?(?P<neyear>\d{4})\)`
- Appellate Court docket numbers: `\bNo(?:s)?\.\s*(?P<district>[1-5])-(?P<yy>\d{2})-(?P<seq>\d{4})(?P<wc>WC)?\b`
- Westlaw cites with Illinois parenthetical: `(?P<year>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Ill\.`

Short forms → URL key:

Code of Civil Procedure → `735 ILCS 5`; Code Civ. Proc. → `735 ILCS 5`; CCP → `735 ILCS 5`; Code of Criminal Procedure of 1963 → `725 ILCS 5`; Criminal Code of 2012 → `720 ILCS 5`; Criminal Code of 1961 → `720 ILCS 5`; Consumer Fraud and Deceptive Business Practices Act → `815 ILCS 505`; Consumer Fraud Act → `815 ILCS 505`; ICFA → `815 ILCS 505`; Illinois Marriage and Dissolution of Marriage Act → `750 ILCS 5`; IMDMA → `750 ILCS 5`; Illinois Vehicle Code → `625 ILCS 5`; Illinois Human Rights Act → `775 ILCS 5`; IHRA → `775 ILCS 5`; Biometric Information Privacy Act → `740 ILCS 14`; BIPA → `740 ILCS 14`; Workers' Compensation Act → `820 ILCS 305`; Illinois Pension Code → `40 ILCS 5`; Probate Act of 1975 → `755 ILCS 5`; Unified Code of Corrections → `730 ILCS 5`; Freedom of Information Act → `5 ILCS 140`; FOIA → `5 ILCS 140`; Ill. Comp. Stat. → `ILCS`; Ill. Comp. Stat. Ann. → `ILCS`

Ill. S. Ct. R. 6 (verified): cases filed on or after July 1, 2011 are cited by public-domain citation — 'YYYY IL NNNNNN' (Supreme Court) or 'YYYY IL App (Nth) NNNNNN' (district: 1st, 2d, 3d, 4th, 5th) — with paragraph pinpoints ', ¶ 15' / ', ¶¶ 21-23'; Rule 23 orders add '-U'; earlier published cases are cited to the Official Reports (Ill., Ill. 2d, Ill. App., Ill. App. 2d/3d), N.E. and Ill. Dec. optional. Docket mapping (observed on Wancket/Moore and PLA lists): the six-digit Appellate number is the docket — 2026 IL App (1st) 232256 = No. 1-23-2256; the Supreme number is the Supreme docket (2021 IL 125656 = No. 125656). Workers' Compensation Division cites carry 'WC' (e.g. '141234WC'; from memory). Suffixes -B/-C (modified/upon rehearing) from memory. Rule 23 orders: not precedential; per Rule 23(e)(1) as amended (eff. Jan. 1, 2021, from memory) orders entered on or after that date may be cited for persuasive purposes. Routing guards: bare 'Rule 23', 'Supreme Court Rule 41' or 'Section 2-619' do not route here without 'Ill.'/'Illinois' or an Illinois act name (the Supreme Court Rule regex requires 'Ill. S. Ct. R.', 'Illinois Supreme Court Rule' or '… of the Illinois Supreme Court Rules'). N.E. and WL cites route here only with an '(Ill.' parenthetical (N.E. also covers IN, MA, NY, OH). 'Ill. Reg.' and 'Ill. Adm. Code' are distinct from reporter cites because a digit must follow 'Ill.' for the reporter regex. Ranges: '735 ILCS 5/2-619 to 2-622' captures only the first section; the section group refuses a trailing hyphen-digit run. Pre-1993 citations to Ill. Rev. Stat. ('Ill. Rev. Stat. 1991, ch. 110, par. 2-619') have no free source here; ch. 110 = 735 ILCS 5. CourtListener ids from memory: 'ill' (Supreme Court of Illinois), 'illappct' (Appellate Court of Illinois) — unverified.

## A. Statutes / code

### `il-ilcs-ilga` — Illinois Compiled Statutes (ILGA)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Illinois General Assembly / Legislative Reference Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** All ILCS chapters, acts and sections; Public Acts; bill status (from memory, not fetchable from this workspace).
- **Access:** `constructible` · format html
  - Pattern: `https://www.ilga.gov/legislation/ilcs/documents/{chapter:04d}{act:04d}0K{section}.htm`
  - Placeholders: Per-section document: chapter zero-padded to 4 digits + act zero-padded to 4 digits + literal '0K' + section verbatim (hyphens and dots kept). 815 ILCS 175/15-5 -> 081501750K15-5.htm; 735 ILCS 5/2-619 -> 073500050K2-619.htm. The pattern was seen in a WebSearch result and on the witnessslips.ilga.gov mirror, NOT on www.ilga.gov. Section links from the ILGA site's own pages (verified on illinoiscourts.gov) point to the redesigned scheme https://www.ilga.gov/Legislation/ILCS/Chapters, which is also blocked. Legacy act page: ilcs3.asp?ActID={id}&ChapterID={id} (ActID not derivable; e.g. 815 ILCS 505 = ActID 2017, ChapterID 56, from memory).
  - Index: `https://www.ilga.gov/Legislation/ILCS/Chapters`
  - Navigation: Unusable from this workspace: the index and every section document are refused.
- **Automation:** WebFetch blocked · shell tls-error · robots: unreadable: WebFetch returns ROBOTS_DISALLOWED even for /robots.txt; shell fails TLS before robots can be read
  - WebFetch: ROBOTS_DISALLOWED on /Legislation/ILCS/Chapters, /legislation/ilcs/ilcs3.asp, /robots.txt and ilga.gov/commission/lrb/conmain.htm. fetch_doc.py --research: 'TLS certificate chain does not verify' for www.ilga.gov and ilga.gov (also lrb.ilga.gov and witnessslips.ilga.gov). Never retry by another route.
- **Currency:** not readable
- **Official status:** Not checked: every www.ilga.gov page was refused (WebFetch robots) or failed TLS (shell), so no disclaimer could be read. From memory, ILGA's ILCS database carries an unofficial-text disclaimer (unverified).
- **Hazard:** host refused to WebFetch (robots) and to the shell (TLS)
- **Hazard:** site redesigned (new /Legislation/ILCS/ paths); legacy .asp and documents/ URLs may redirect
- **Probe:** 815 ILCS 505/2 → `https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=2017&ChapterID=56`
- **Evidence (2026-10-16):** WebFetch: ROBOTS_DISALLOWED (4 URLs incl. robots.txt). fetch_doc.py --research info: FETCH ERROR TLS certificate chain does not verify (www.ilga.gov, ilga.gov).
- **Notes:** The same publisher's content answers on witnessslips.ilga.gov (one WebFetch returned 815 ILCS 175/15-5 body text), but using a mirror host to get around www.ilga.gov's refusal would be a workaround, so it is NOT recorded as a source. See open_questions.

### `il-ilcs-justia` — Justia — Illinois Compiled Statutes (2025)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** ILCS 2025 edition (unversioned URL); prior years at /codes/illinois/{year}/... (2024 and 2023 links seen on the act page).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/illinois/chapter-{chapter}/act-{chapter}-ilcs-{act}/[article-{article_roman_lower}/]`
  - Placeholders: chapter and act unpadded (chapter-815/act-815-ilcs-505/, chapter-735/act-735-ilcs-5/). Small acts: the act page holds every section in sequence (no per-section links). Large acts (735 ILCS 5) have an act page that is only a list of articles; the article = the section prefix before the hyphen in Roman lower case (5/2-619 -> article-ii). No per-section URL: /section-815-ilcs-505-2/ returned a client error. Year-specific: insert /{year}/ after /illinois/.
  - Index: `https://law.justia.com/codes/illinois/`
  - Navigation: act page -> (large acts) article page -> find 'Sec. N.' / '(735 ILCS 5/2-619)' heading in the page text
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge on robots.txt; fetch_doc.py REFUSED law.justia.com for the day)
  - WebFetch reads 100,000 characters per call; use offset=100000 for later sections. 815 ILCS 505 act page = 125,589 chars; 735 ILCS 5 Article II page = 117,765 chars and stops mid-word after § 2-622.
- **Currency:** page header — observed: "2025 Illinois Compiled Statutes"
- **Official status:** Chapter page states 'These codes may not be the most recent version.' (https://law.justia.com/codes/illinois/chapter-815/)
- **Hazard:** edition lags the official ILCS by up to a year
- **Hazard:** no per-section pages; long acts/articles exceed one WebFetch window (use offset=100000)
- **Hazard:** 735 ILCS 5 Article II page ends after § 2-622: later Article II sections (e.g. 2-1001, 2-1401) NOT PRESENT even with offset
- **Hazard:** shell blocked by Cloudflare
- **Probe:** 815 ILCS 505/2 → `https://law.justia.com/codes/illinois/chapter-815/act-815-ilcs-505/` — expect: "Unfair methods of competition and unfair or deceptive acts or practices, including"
- **Evidence (2026-10-16):** WebFetch: 505/2 body 'Unfair methods of competition and unfair or deceptive acts or practices, including'; '2025 Illinois Compiled Statutes'. Second: 735 ILCS 5/2-619 at /act-735-ilcs-5/article-ii/ offset=100000 '(a) Defendant may, within the time for pleading, file a motion for'.
- **Notes:** The only reachable statute text for Illinois from this workspace. Where to find sections past § 2-622 of 735 ILCS 5 Article II on Justia is unresolved (open question).

## B. Constitution

### `il-constitution-ilga` — Illinois Constitution (ILGA / Legislative Reference Bureau)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Illinois General Assembly, Legislative Reference Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** 1970 Constitution as amended.
- **Access:** `index-anchored` · format html
  - Placeholders: Index link from illinoiscourts.gov home page: https://www.ilga.gov/commission/lrb/conmain.htm (article pages not seen).
  - Index: `https://www.ilga.gov/commission/lrb/conmain.htm`
  - Navigation: Unusable: host refused.
- **Automation:** WebFetch blocked · shell tls-error · robots: unreadable (see il-ilcs-ilga)
  - WebFetch on ilga.gov/commission/lrb/conmain.htm: ROBOTS_DISALLOWED; shell TLS failure on ilga.gov.
- **Currency:** not readable
- **Official status:** Not readable (host refused).
- **Hazard:** host refused (robots / TLS)
- **Probe:** Ill. Const. 1970, art. I, § 2 → `https://ilga.gov/commission/lrb/conmain.htm`
- **Evidence (2026-10-16):** WebFetch ROBOTS_DISALLOWED; fetch_doc.py TLS certificate chain does not verify.

### `il-constitution-justia` — Justia — Illinois Constitution

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Preamble, Articles I-XIV and Transition Schedule, one page per article.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/illinois/con{article}.html`
  - Placeholders: article = Arabic article number, unpadded (Art. I -> con1.html, Art. VI -> con6.html). Preamble and Transition Schedule slugs not checked: take them from the index.
  - Index: `https://law.justia.com/constitution/illinois/`
  - Navigation: index lists article links only (no text)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - Article I page complete through § 24 in one window.
- **Currency:** none stated (disclaimer only) — observed: "This Constitution may not be the most recent version."
- **Official status:** Index page disclaimer: 'This Constitution may not be the most recent version.'
- **Hazard:** no currency date; recent amendments (e.g. 2022 Art. I § 25 workers' rights) may be missing — Art. I page ended at § 24
- **Hazard:** shell blocked by Cloudflare
- **Probe:** Ill. Const. 1970, art. I, § 2 → `https://law.justia.com/constitution/illinois/con1.html` — expect: "No person shall be deprived of life, liberty or property without due"
- **Evidence (2026-10-16):** WebFetch: § 2 'No person shall be deprived of life, liberty or property without due'; second citation art. I, § 12 'Every person shall find a certain remedy in'; page runs through § 24. Index: con6.html link for Art. VI (not fetched).
- **Notes:** The Art. I page ending at § 24 suggests Justia lacks Art. I § 25 (Workers' Rights Amendment, 2022, from memory) — treat as possibly stale.

## C. Court rules

### `il-rules-appellate-local` — Appellate Court Local Rules

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Illinois Appellate Court · text: **link-only** · official: unknown
- **Coverage:** Local rules of the five appellate districts (linked from the illinoiscourts.gov menu).
- **Access:** `link-only` · format html
  - Index: `https://www.illinoiscourts.gov/courts/appellate-court/appellate-court-local-rules/`
- **Automation:** WebFetch untested · shell untested · robots: www.illinoiscourts.gov allows /
- **Currency:** 
- **Official status:** Not fetched.
- **Probe:**  → ``
- **Evidence (2026-10-16):** Link seen on the illinoiscourts.gov home page menu (shell); page not fetched.
- **Notes:** Low priority; IPI jury instructions are at /rules-law/ipi-jury-instructions/ (link only).

### `il-rules-evidence` — Illinois Rules of Evidence (per-rule PDFs)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of Illinois · text: **fetch-and-quote** · official: unknown
- **Coverage:** Ill. R. Evid. 101-1101 (eff. Jan. 1, 2011, as amended), with the committee's general commentary on the index page.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.illinoiscourts.gov/resources/{guid}/file`
  - Placeholders: guid from the index row (Rule 401 -> 6a5bd4c5-f59c-4bdd-9183-0a0e78f9e2a7). Some index hrefs contain a stray space before '/file' ('ad47521f-… /file' for Rule 702) — strip it. Redirects 302 to the blob host ('Evid.%20Rule%20401.pdf').
  - Index: `https://www.illinoiscourts.gov/courts/supreme-court/courts-supreme-court-illinois-rules-of-evidence/`
  - Navigation: index table (Article | Rule N | title link) -> /resources/{guid}/file -> 302 -> blob PDF
  - Read via: ilcourtsaudio.blob.core.windows.net (WebFetch ok; fetch_doc.py refused)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: see il-rules-supreme
  - Index 38,665 chars (shell ok).
- **Currency:** history line at the end of each rule PDF; index row status cell — observed: "Adopted September 27, 2010, eff. January 1, 2011."
- **Official status:** Published on illinoiscourts.gov; no official statement seen.
- **Hazard:** two-hop redirect to blob storage
- **Hazard:** stray spaces in some index hrefs
- **Hazard:** script route refused on the PDF host
- **Probe:** Ill. R. Evid. 401 → `https://ilcourtsaudio.blob.core.windows.net/antilles-resources/resources/6a5bd4c5-f59c-4bdd-9183-0a0e78f9e2a7/Evid.%20Rule%20401.pdf` — expect: "Relevant evidence means evidence having any tendency to make the existence of"
- **Evidence (2026-10-16):** WebFetch: 'Relevant evidence means evidence having any tendency to make the existence of'; complete. Second citation not fetched (Rule 702 guid ad47521f-… recorded from index).

### `il-rules-supreme` — Illinois Supreme Court Rules (per-rule PDFs), incl. Rules of Professional Conduct of 2010 and Code of Judicial Conduct of 2023

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of Illinois / Administrative Office of the Illinois Courts · text: **fetch-and-quote** · official: unknown
- **Coverage:** All Supreme Court Rules, Articles I-XI, one PDF per rule; Article VIII = Illinois Rules of Professional Conduct of 2010; index row gives the latest amendment date. Amendment archive at /rules/supreme-court-rules/amendment-archive (not fetched).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.illinoiscourts.gov/resources/{guid}/file`
  - Placeholders: guid is not derivable: take it from the index row whose 'Rule N' cell matches (Rule 6 -> 2374deda-…, Rule 23 -> 650f76b5-…, Rule 315 -> ce707476-…, RPC 1.7 -> e3223b75-…). /resources/{guid}/file answers 302 to https://ilcourtsaudio.blob.core.windows.net/antilles-resources/resources/{guid}/{filename}.pdf (filename e.g. 'Rule%2023.pdf'). WebFetch does not follow that cross-host redirect: call it again on the Location URL it reports.
  - Index: `https://www.illinoiscourts.gov/rules-law/supreme-court-rules/`
  - Navigation: index (one table: Article | Rule N | linked title + 'Amended …, eff. …') -> /resources/{guid}/file -> 302 -> blob PDF
  - Read via: PDF text lives on ilcourtsaudio.blob.core.windows.net: WebFetch ok; fetch_doc.py REFUSED (blob robots.txt answers 401/403).
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.illinoiscourts.gov: User-agent * Allow /, Disallow /antilles/, /App_Code/, /Bin/. ilcourtsaudio.blob.core.windows.net: robots.txt refused (401/403) -> fetch_doc.py treats host as bot-walled
  - Index page is shell-readable (fetch_doc.py ok, 145,695 chars); WebFetch window 1 of the index ends near Article VIII (RPC 1.7 row at char ~107,900) — use offset=100000 for RPC and later articles. Each rule PDF is short and fits one window.
- **Currency:** index row status cell and the history line at the end of each rule PDF — observed: "Rule 23: Amended June 3, 2025, eff. immediately (PDF history line)"
- **Official status:** Published by the court on illinoiscourts.gov; no official/unofficial statement seen on the index or the rule PDFs.
- **Hazard:** two-hop cross-host redirect to blob storage
- **Hazard:** guid per rule not derivable
- **Hazard:** index longer than one WebFetch window
- **Hazard:** script route refused on the PDF host
- **Hazard:** repealed rules listed in the same table (e.g. 'VIII - Repealed Rule 1.7')
- **Probe:** Ill. S. Ct. R. 23(e)(1) → `https://ilcourtsaudio.blob.core.windows.net/antilles-resources/resources/650f76b5-3cce-40b9-acc3-d93b1aced5f4/Rule%2023.pdf` — expect: "An order entered under subpart (b) or (c) of this rule is"
- **Evidence (2026-10-16):** WebFetch: 23(e)(1) 'An order entered under subpart (b) or (c) of this rule is'; history ends 'amended June 3, 2025, eff. immediately.' Second: Rule 6 PDF 'Citation of Illinois cases filed prior to July 1, 2011, and published'.
- **Notes:** Rule 6 (citation form) and Rule 23 (unpublished orders) drive the citation_map. Rule 315 (PLA) at guid ce707476-e53a-48e3-9119-6496ef58aa41 (not fetched).

## D. Administrative code

### `il-admincode-jcar` — Illinois Administrative Code (JCAR)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Joint Committee on Administrative Rules, Illinois General Assembly · text: **fetch-and-quote** · official: unknown
- **Coverage:** All Ill. Adm. Code titles (from memory).
- **Access:** `index-anchored` · format html
  - Placeholders: Index link from illinoiscourts.gov: https://www.ilga.gov/agencies/JCAR/AdminCode (legacy /commission/jcar/admincode/titles.html linked from Cornell LII).
  - Index: `https://www.ilga.gov/agencies/JCAR/AdminCode`
  - Navigation: Unusable: host refused.
- **Automation:** WebFetch blocked · shell tls-error · robots: unreadable (see il-ilcs-ilga)
  - WebFetch ROBOTS_DISALLOWED; shell TLS failure.
- **Currency:** not readable
- **Official status:** Not readable (host refused).
- **Hazard:** host refused (robots / TLS)
- **Probe:** 35 Ill. Adm. Code 101.100 → `https://www.ilga.gov/agencies/JCAR/AdminCode`
- **Evidence (2026-10-16):** WebFetch: ROBOTS_DISALLOWED. Shell: TLS certificate chain does not verify (www.ilga.gov).

### `il-admincode-lii` — Cornell LII — Illinois Administrative Code

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All Ill. Adm. Code titles 1-95 (index lists 32 titles), per-section pages with Ill. Reg. history notes.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/illinois/Ill-Admin-Code-tit-{title}-SS-{section}`
  - Placeholders: title unpadded; section = Part.Section verbatim (101.100, 130.101). Browse: /regulations/illinois/title-{title}/part-{part}/subpart-{A..}; subpart links show section ranges ('§ 101.100 to 101.114'). A non-existent section returns the Illinois index page (HTTP 200), not a 404 — check the page heading.
  - Index: `https://www.law.cornell.edu/regulations/illinois`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay: 10; /regulations allowed
  - Respect 10-second crawl delay. Last-Modified headers on probed pages: Aug 1, 2025.
- **Currency:** page Notes section — observed: "State regulations are updated quarterly; we currently have two versions available."
- **Official status:** Third-party mirror: 'State regulations are updated quarterly; we currently have two versions available.'
- **Hazard:** quarterly (or older) lag: probed pages Last-Modified Aug 2025
- **Hazard:** wrong section silently returns the index page
- **Hazard:** compare the latest Ill. Reg. note with the official Code before quoting
- **Probe:** 35 Ill. Adm. Code 101.100 → `https://www.law.cornell.edu/regulations/illinois/Ill-Admin-Code-tit-35-SS-101.100` — expect: "This Part sets forth the rules generally applicable to proceedings before the"
- **Evidence (2026-10-16):** WebFetch: 'This Part sets forth the rules generally applicable to proceedings before the'; fetch_doc.py ok, note 'Amended at 43 Ill. Reg. 9674'. Second: 86 Ill. Adm. Code 130.101 (fetch_doc.py) heading present, 'Amended at 47 Ill. Reg. 2116'.
- **Notes:** The only reachable Admin Code text for Illinois from this workspace.

## D. Administrative register

### `il-register-sos` — Illinois Register (Secretary of State)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Illinois Secretary of State, Index Department · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Weekly issues (index page seen shows 2022, Volume 46).
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.ilsos.gov/departments/index/register/volume{volume}/register_volume{volume}_issue_{issue}.pdf`
  - Placeholders: Pattern inferred from an agency mirror in a WebSearch result (ilaging.illinois.gov/.../register/volume45/register_volume45_issue_3.pdf); the ilsos.gov form was refused, so unverified.
  - Index: `https://www.ilsos.gov/departments/index/register/home.html`
  - Navigation: index -> volume -> issue PDF (links not visible to WebFetch)
- **Automation:** WebFetch blocked · shell http-error · robots: shell: robots.txt unreachable (remote end closed connection) on www.ilsos.gov and www.cyberdriveillinois.com
  - WebFetch read the home.html index (no issue links extracted) but returned ROBOTS_DISALLOWED for the volume50 issue PDF.
- **Currency:** index page — observed: "2022, Volume 46"
- **Official status:** Register index page: 'This electronic document is not the official publication of the Illinois Register.'
- **Hazard:** issue PDFs robots-disallowed to WebFetch
- **Hazard:** index page appears stale (Vol. 46, 2022)
- **Hazard:** shell cannot read robots.txt
- **Probe:** 50 Ill. Reg. (2026 issue) → `https://www.ilsos.gov/departments/index/register/volume50/register_volume50_issue_40.pdf`
- **Evidence (2026-10-16):** WebFetch: ROBOTS_DISALLOWED on the issue PDF; home.html readable, 'not the official publication of the Illinois Register'. Shell: robots.txt unreachable.
- **Notes:** Ill. Reg. history notes on LII pages (il-admincode-lii) are the practical way to identify amending Register cites.

## E. Case law

### `il-opinions-courts` — Illinois Courts — Opinions (Supreme Court, Appellate Court, Workers' Compensation Division)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of Illinois / Administrative Office of the Illinois Courts (Reporter of Decisions) · text: **fetch-and-quote** · official: official
- **Coverage:** Supreme Court opinions from May 23, 1996 (earliest rows: People v. Redd, Franson v. Micelli, 05/23/1996); Appellate Court opinions and Rule 23 orders, all five districts and the Workers' Compensation Commission Division (appellate start year not established). Pre-July-2011 rows have no public-domain citation. Status column: Slip / Released / Final.
- **Read via (in order):** **fetch tool**
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.illinoiscourts.gov/resources/{guid}/file`
  - Placeholders: The opinion URL uses a guid that is not derivable from the citation; the file name on the blob host after the 302 is '{Case name} {citation}.pdf' (e.g. 'Rehfield v. Diocese of Joliet, 2021 IL 125656.pdf') but the guid is still needed. Finding an opinion: (1) the listing page shows the latest ~150 rows (case name link, citation, filing date, court, Opinion/Rule 23, status); (2) the search form is ASP.NET POST-only (GET query strings such as ?ctl00$ctl04$txtFilterName=… are ignored — tested): fields ctl00$ctl04$txtFilterName (free text — matches opinion full text, not just party names: searching 'Rehfield' also returned cases citing it), ddlFilterFilingDate ('Search All Years'), ddlFilterCourtType ('Supreme Court', 'First District Appellate Court' … 'Workers' Compensation'), ddlFilterType ('Opinion' | 'Rule 23'), ddlFilterStatus; hdnSortField=FilingDate, hdnSortDirection=ASC|DESC; results 150 rows per page, paged by __doPostBack Page$N. (3) RSS (plain GET, XML): /views/courts/rss/opinions-supreme.aspx and /views/courts/rss/opinions-appellate.aspx with opinion:citationnum, filingdate, court, docketstatus and a direct link.
  - Index: `https://www.illinoiscourts.gov/top-level-opinions/`
  - Navigation: listing / POST search / RSS -> row link /resources/{guid}/file -> 302 -> ilcourtsaudio.blob.core.windows.net/…/{name}.pdf (WebFetch: call again on the reported Location)
  - Read via: PDFs on ilcourtsaudio.blob.core.windows.net: WebFetch ok; fetch_doc.py REFUSED (robots.txt 401/403 -> bot wall).
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.illinoiscourts.gov: Allow / (Disallow /antilles/, /App_Code/, /Bin/); blob host robots.txt refused
  - Listing page: shell ok (328 KB HTML); WebFetch reads it but text is 175,706 chars (window 1 = first ~100K). Several 'Connection reset by peer' / proxy tunnel closures on rapid POSTs — space requests. Opinion PDFs fit one WebFetch window (Rehfield 70 ¶¶, Wancket 86 ¶¶).
- **Currency:** listing (newest filing date) and RSS pubDate — observed: "newest rows filed 10/16/2026"
- **Official status:** Final opinions carry the 'Illinois Official Reports' header (Rehfield, 2021 IL 125656); since July 1, 2011 the public-domain citation is the citation form required by Ill. S. Ct. R. 6. Slip opinions lack the header and the site cautions they may change (Rule 367 rehearing).
- **Hazard:** guid URLs not derivable; search is POST-only
- **Hazard:** cross-host 302 to blob storage; script route refused there
- **Hazard:** slip opinions may change on rehearing; 'Illinois Official Reports' header only on final versions
- **Hazard:** running page headers ('No. 1-23-2256') split sentences across pages — quote-match across the break
- **Hazard:** free-text filter matches citing cases, not just the named case
- **Hazard:** WebFetch 'first words of ¶ N' answers were unreliable once (Wancket ¶ 2) — confirm with a phrase search
- **Probe:** Rehfield v. Diocese of Joliet, 2021 IL 125656 → `https://ilcourtsaudio.blob.core.windows.net/antilles-resources/resources/231556cb-4e60-4b7d-871d-fc1c1a871a41/Rehfield%20v.%20Diocese%20of%20Joliet,%202021%20IL%20125656.pdf` — expect: "Plaintiff Mary Rehfield filed a two-count amended complaint against defendant, the Diocese"
- **Evidence (2026-10-16):** POST search (Supreme Court, all years, 'Rehfield v. Diocese of Joliet') -> 2021 IL 125656, 02/04/2021, Final. WebFetch PDF: ¶ 1 present, 'Illinois Official Reports' header, ¶¶ 1-70 complete. Second: Wancket, 2026 IL App (1st) 232256 (Slip, no header, ¶¶ 1-86); Rule 23 order Moore, 2026 IL App (1st) 251481-U ok.
- **Notes:** Rule 23 orders show 'NOTICE: This order was filed under Supreme Court Rule 23 and is not precedent except' at the top. Ill. S. Ct. R. 23(e)(1): such orders entered on or after Jan. 1, 2021 may be cited for persuasive purposes (from memory; 23(e)(1) text verified only by its first words).

### `il-cases-justia` — Justia — Illinois case law

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court and Appellate Court districts (ranges not checked).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/illinois/{court-slug}/{year}/{docket}.html`
  - Placeholders: Supreme Court: court-slug supreme-court, docket = the six-digit number of the public-domain cite (2021 IL 125656 -> /supreme-court/2021/125656.html). Appellate: court-slug court-of-appeals-{first|second|third|fourth|fifth}-appellate-district, docket = district-yy-nnnn built from the public-domain number (2026 IL App (1st) 232256 -> 1-23-2256 -> /court-of-appeals-first-appellate-district/2026/1-23-2256.html). Rule 23 (-U) and Workers' Compensation slugs not checked.
  - Index: `https://law.justia.com/cases/illinois/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
- **Currency:** none
- **Official status:** Third-party copy; adds its own summary/'Primary Holding'.
- **Hazard:** Justia summary text is not the opinion — quote only from the opinion body
- **Hazard:** shell blocked
- **Hazard:** slip text; no N.E.3d pagination
- **Probe:** Rehfield v. Diocese of Joliet, 2021 IL 125656 → `https://law.justia.com/cases/illinois/supreme-court/2021/125656.html` — expect: "Plaintiff Mary Rehfield filed a two-count amended complaint against defendant, the Diocese"
- **Evidence (2026-10-16):** WebFetch: ¶ 1 present, ¶¶ 1-70 complete. Second: /court-of-appeals-first-appellate-district/2026/1-23-2256.html = Wancket, 2026 IL App (1st) 232256, complete through 'Affirmed.'

## F. Subsequent history

### `il-subsequent-history-pla` — Supreme Court of Illinois — Petition for Leave to Appeal Dispositions

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of Illinois (Clerk) · text: **fetch-and-quote** · official: unknown
- **Coverage:** One PDF per disposition date; year filter 2007-2026 on the page. Each list ~300 entries (Sept. 30, 2026: dockets 131298-133508).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://ilcourtsaudio.blob.core.windows.net/antilles-resources/resources/{guid}/{Month}%20{D}%20{YYYY}.pdf`
  - Placeholders: guid not derivable; take the dated link from the index. Entries: Supreme docket - case name (petitioner/respondent) - 'Appellate Court, {N} District' + appellate docket ('2-23-0584') - disposition ('Petition for Leave to Appeal Denied' / 'Allowed', supervisory orders). Lists do NOT use public-domain citations: convert the decision below first — '2026 IL App (1st) 232256' -> docket 1-23-2256 (district digit, then the 6-digit number split 2+4) — and search the lists dated after the appellate filing (PLA due 35 days after judgment, Rule 315(b), from memory).
  - Index: `https://www.illinoiscourts.gov/courts/supreme-court/leave-to-appeal/`
  - Navigation: index (links are direct blob URLs, newest first; older years via the category filter) -> dated PDF -> find appellate docket
  - Read via: blob host: WebFetch ok, fetch_doc.py refused
- **Automation:** WebFetch ok · shell blocked-challenge · robots: see il-opinions-courts
  - Index page is shell-readable; the year filter is a postback (only current-year links in the initial HTML, ~120).
- **Currency:** index (newest list date) — observed: "September 30 2026"
- **Official status:** Court-published lists; no statement.
- **Hazard:** no search: scan dated lists
- **Hazard:** keyed by appellate docket, not citation
- **Hazard:** year filter is POST/postback
- **Probe:** PLA dispositions, Sept. 30, 2026 → `https://ilcourtsaudio.blob.core.windows.net/antilles-resources/resources/819ce661-8298-4ed3-b7dc-c942e285d8c7/September%2030%202026.pdf` — expect: "THE FOLLOWING CASES ON THE LEAVE TO APPEAL DOCKET WERE DISPOSED OF AS INDICATED:"
- **Evidence (2026-10-16):** WebFetch: heading present; first entry '131298 - People State of Illinois, petitioner, v. Terry T. Collins, respondent.'; ~305 entries, complete.
- **Notes:** When leave is allowed, the Supreme Court opinion itself names the appellate citation; search the opinions POST filter with the appellate citation or party name (free-text). US cert is the only further review.

## Not available (do not look for these again)

- **statutes** — public.law edition of the ILCS: fetch_doc.py on illinois.public.law: proxy 'Tunnel connection failed: 502'; www.public.law home text names only oregon.public.law (other states in the pilot logs: CA, CO, FL, NV, NY, OR, TX). (2026-10-16)
- **statutes** — Cornell LII copy of the ILCS / Illinois Constitution / Illinois opinions: https://www.law.cornell.edu/states/illinois links out to ilga.gov and illinoiscourts.gov; LII hosts only the Illinois Administrative Code. (2026-10-16)
- **case_law** — Free official reporter pagination for pre-2011 cases (Ill. 2d, Ill. App. 3d) and any free opinions before May 1996 on the court site: Opinions database ascending sort: earliest Supreme rows 05/23/1996 with no citation column; pre-2011 PDFs are slip/court copies. (2026-10-16)

## Corpus candidates (maintainers)

- `il-rules-supreme` — Index page (145,695 chars) exceeds one WebFetch window (Article VIII rows past char 100,000); text is ~400 separate per-rule PDFs reached by a two-hop redirect. A corpus would remove both hops — but ingest must read the blob host, which fetch_doc.py refuses (robots.txt 403).
- `il-rules-evidence` — Per-rule PDFs behind a two-hop redirect; small set (~60 rules) suited to a corpus once the blob host is readable.

## Open questions

- ilga.gov: is WebFetch's ROBOTS_DISALLOWED a real robots.txt rule or a fetch failure reported as robots (it was returned even for /robots.txt)? Re-test from a host with working TLS before treating ILCS as permanently tier-2-only.
- Policy decision needed: witnessslips.ilga.gov (and lrb.ilga.gov) mirror ILGA content; one WebFetch returned 815 ILCS 175/15-5 body text from witnessslips. Not recorded as a source because using it would work around www.ilga.gov's refusal.
- ILCS bulk data (ILGA FTP, from memory) not checkable: host refused.
- Justia 735 ILCS 5 Article II page ends after § 2-622; where Justia serves §§ 2-1001 onward (e.g. 2-1401) is unknown.
- Appellate Court coverage start year on illinoiscourts.gov not established (POST searches hit connection resets).
- Justia slugs for Rule 23 (-U) orders and Workers' Compensation Division decisions not checked.
- Illinois Register current issues: ilsos.gov PDFs robots-disallowed to WebFetch; no reachable source for Ill. Reg. text.
- Rule 23(e)(1) persuasive-citation date (Jan. 1, 2021) and WC/-B/-C citation suffixes are from memory.
- CourtListener court ids ill / illappct unverified.
- Session laws (Public Acts) not researched: ilga.gov refused.
