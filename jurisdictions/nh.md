# New Hampshire (NH) — free legal sources

_Generated from `data/nh.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: gc.nh.gov (General Court) serves one HTML page per RSA section plus a whole-chapter '-mrg' page. URLs are constructible once the title (Roman) is known from the title index, which shows chapter ranges. The site says it is current through the 2026 regular session and is not official. The script route fails because gc.nh.gov drops the connection, and WebFetch waits for approval on built URLs, so use URLs taken from index pages. Justia (2025) is the tier-2 fallback. Constitution: the official nh.gov page could not be read; Justia's copy is dated 1990. Court rules are on courts.nh.gov as long single pages: WebFetch reads them but cuts them off (Evidence after Rule 902, Criminal Procedure in Rule 23), and the host blocks the script with a bot check. These are corpus candidates. Admin rules: gc.nh.gov per-chapter HTML (not official), Cornell LII per section (script ok), and a weekly Rulemaking Register in PDF. Case law: neutral citations ('2024 N.H. 1', paragraph pinpoints) since 1 Jan. 2024. Slip opinions are on courts.nh.gov, but the listing could not be read (WebFetch gated, script blocked). Justia has HTML by year. Certiorari history is on supremecourt.gov dockets ('Lower Ct: Supreme Court of New Hampshire'), which the script reads.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| New Hampshire Supreme Court | `nh (unverified)` | N.H. | N.H., A.3d, A.2d, A. | 2024 N.H. 1 (year N.H. opinion number; paragraph pinpoints ¶ N), for opinions issued on or after January 1, 2024 |
| New Hampshire Superior Court | `nhsuperct (unverified)` | N.H. Super. Ct. | — | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| New Hampshire Revised Statutes Annotated (RSA) | `RSA 358-A:2`; `RSA 567-A:1`; `RSA 126-G:2, I`; `N.H. Rev. Stat. Ann. § 458:2`; `N.H. Rev. Stat. Ann. § 507:7-d`; `RSA chapter 358-A`; `RSA ch. 126-G`; `New Hampshire Revised Statutes Annotated 458:2`; `section 637:3 of the New Hampshire Revised Statutes` | `nh-rsa-gc` → `nh-rsa-justia` |
| New Hampshire session laws | `1989 N.H. Laws 255:2`; `2019 N.H. Laws ch. 346`; `Laws 1995, 310:79` | `nh-session-laws-gc` |
| New Hampshire Constitution | `N.H. Const. pt. I, art. 15`; `N.H. CONST. pt. II, art. 73-a`; `Part I, Article 15 of the New Hampshire Constitution`; `Part II, Article 83 of the N.H. Constitution`; `Article 2-b of Part I of the New Hampshire Constitution` | `nh-constitution-nhgov` → `nh-constitution-justia` |
| New Hampshire court rules (with N.H. marker) | `N.H. R. Evid. 403`; `N.H. R. Crim. P. 15`; `N.H. Sup. Ct. R. 7`; `N.H. Super. Ct. R. 12`; `N.H. R. Prof. Conduct 1.7`; `Rule 403 of the New Hampshire Rules of Evidence`; `Rule 7 of the Rules of the Supreme Court of New Hampshire` | `nh-rules-evidence-courts` → `nh-rules-crimp-courts` → `nh-rules-supreme-courts` → `nh-rules-superior-courts` |
| New Hampshire court rules (generic forms) *(only once this jurisdiction is known)* | `Sup. Ct. R. 7`; `Supreme Court Rule 12-D`; `Super. Ct. R. 12`; `Superior Court Rule 12` | `nh-rules-supreme-courts` → `nh-rules-superior-courts` |
| New Hampshire Code of Administrative Rules (with N.H. marker) | `N.H. Admin. Code Ban 101.01`; `N.H. Code Admin. R. Env-Dw 702.01`; `N.H. Admin. R. Env-Wq 1001.01`; `N.H. Admin. Code § Ban 101.01` | `nh-admin-rules-gc` → `nh-admin-rules-lii` |
| New Hampshire administrative rules (bare agency prefix) *(only once this jurisdiction is known)* | `Env-Wq 1001.01`; `Ban 101.01`; `Saf-C 6000` | `nh-admin-rules-gc` → `nh-admin-rules-lii` |
| New Hampshire Rulemaking Register | `N.H. Rulemaking Register, Vol. XLVI, No. 34`; `New Hampshire Rulemaking Register No. 34 (Aug. 27, 2026)` | `nh-register-gc` |
| New Hampshire neutral citation and N.H. Reports | `State v. Smith, 2024 N.H. 1, ¶ 12`; `2025 N.H. 37`; `State v. Smith, 170 N.H. 100 (2017)`; `167 N.H. 123`; `123 A.3d 456 (N.H. 2015)`; `950 A.2d 175 (N.H. 2008)` | `nh-opinions-courts` → `nh-cases-justia` |
| New Hampshire Supreme Court docket numbers *(only once this jurisdiction is known)* | `No. 2022-0629`; `No. 2025-0297` | `nh-opinions-courts` → `nh-orders-courts` → `nh-cases-justia` |
| Certiorari / rehearing dispositions *(only once this jurisdiction is known)* | `cert. denied, 607 U.S. 1001 (2026)`; `reh'g denied` | `nh-scotus-docket` |

Regexes (case-insensitive):

- New Hampshire Revised Statutes Annotated (RSA): `(?:\bRSA|N\.\s*H\.\s*Rev\.\s*Stat\.(?:\s*Ann\.)?|New\s+Hampshire\s+Revised\s+Statutes(?:\s+Annotated)?)\s*(?:§+\s*)?(?:(?P<chapter>\d{1,3}(?:-[A-Za-z]{1,2})?):(?P<section>\d{1,3}(?:-[a-z]{1,2})?)(?![\d:])|(?:ch(?:apter|\.)\s*)(?P<chapter2>\d{1,3}(?:-[A-Za-z]{1,2})?)\b)|sec(?:tion|\.)\s*(?P<chapter3>\d{1,3}(?:-[A-Za-z]{1,2})?):(?P<section3>\d{1,3}(?:-[a-z]{1,2})?)(?:,\s*[IVXL]+)?\s+of\s+the\s+(?:New\s+Hampshire|N\.\s*H\.)\s+Revised\s+Statutes(?:\s+Annotated)?`
- New Hampshire session laws: `(?P<year>(?:17|18|19|20)\d{2})\s+N\.\s*H\.\s+Laws,?\s*(?:ch\.\s*)?(?P<chapter>\d{1,3})(?::(?P<section>\d+))?|\bLaws\s+(?P<year2>(?:17|18|19|20)\d{2}),\s*(?P<chapter2>\d{1,3}):(?P<section2>\d+(?:-[a-z])?)`
- New Hampshire Constitution: `N\.\s*H\.\s*Const\.\s*pt\.\s*(?P<part>I{1,2}|1|2),?\s*art\.\s*(?P<article>\d{1,3}(?:-[a-z])?)|Part\s+(?P<part2>I{1,2}|First|Second|1|2),?\s+Art(?:icle|\.)\s*(?P<article2>\d{1,3}(?:-[a-z])?)\s+of\s+the\s+(?:New\s+Hampshire|N\.\s*H\.)\s+Constitution|Art(?:icle|\.)\s*(?P<article3>\d{1,3}(?:-[a-z])?)\s+of\s+Part\s+(?P<part3>I{1,2}|First|Second|1|2)\s+of\s+the\s+(?:New\s+Hampshire|N\.\s*H\.)\s+Constitution`
- New Hampshire court rules (with N.H. marker): `N\.\s*H\.\s*(?:R\.\s*(?P<set>Evid|Crim\.\s*P|Prof\.\s*Conduct)\.?|(?P<court>Sup|Super|Dist|Prob|Fam|Cir)\.\s*Ct\.\s*R\.)\s*(?P<rule>\d{1,3}(?:\.\d+)?(?:-[A-Z])?)|Rule\s+(?P<rule2>\d{1,3}(?:\.\d+)?(?:-[A-Z])?)(?:\([a-z0-9]+\))*\s+of\s+the\s+(?:New\s+Hampshire\s+Rules\s+of\s+(?:Evidence|Criminal\s+Procedure|Professional\s+Conduct)|Rules\s+of\s+the\s+(?:Supreme|Superior)\s+Court\s+of\s+(?:the\s+State\s+of\s+)?New\s+Hampshire)`
- New Hampshire court rules (generic forms): `(?:Sup(?:reme)?\.?\s*(?:Ct\.|Court)\s*R(?:ule|\.)|Super(?:ior)?\.?\s*(?:Ct\.|Court)\s*R(?:ule|\.))\s*(?P<rule>\d{1,3}(?:-[A-Z])?)`
- New Hampshire Code of Administrative Rules (with N.H. marker): `N\.\s*H\.\s*(?:Admin\.\s*Code|Code\s+Admin\.\s*R(?:ules|\.)?|Admin\.\s*R(?:ules|\.)?)\s*(?:§\s*)?(?P<prefix>[A-Z][a-z]{1,3}(?:-[A-Z][a-z]{0,3})?)\s+(?P<section>\d{2,4}(?:\.\d{2,3})?)`
- New Hampshire administrative rules (bare agency prefix): `(?-i:\b(?!(?:Rule|Rules|Laws?|Part|Art|Title|Vol|Page|Sec|Supp|Chap|Ch|Act|Acts|Note|Form|Pub|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|No)\b)(?P<prefix>[A-Z][a-z]{1,3}(?:-[A-Z][a-z]{0,3})?)\s+(?P<section>\d{3,4}(?:\.\d{2,3})?)\b)`
- New Hampshire Rulemaking Register: `(?:N\.\s*H\.|New\s+Hampshire)\s+Rulemaking\s+Register(?:,?\s*Vol\.\s*(?P<volume>[IVXLC]+))?(?:,?\s*No\.\s*(?P<number>\d{1,2}))?`
- New Hampshire neutral citation and N.H. Reports: `\b(?P<pdyear>(?:19|20)\d{2})\s+N\.\s*H\.\s+(?P<pdnum>\d{1,4})(?!\d)|\b(?P<volume>\d{1,3})\s+N\.\s*H\.\s+(?P<page>\d{1,4})\b|\b(?P<avol>\d{1,3})\s+A\.(?:2d|3d)?\s+(?P<apage>\d{1,4})(?:,\s*\d+)?\s*\(N\.\s*H\.\s*(?:Super\.\s*(?:Ct\.\s*)?)?\d{4}\)`
- New Hampshire Supreme Court docket numbers: `\bNo\.\s*(?P<year>(?:19|20)\d{2})-(?P<num>\d{4})\b`
- Certiorari / rehearing dispositions: `cert\.\s+(?P<disp>denied|granted|dismissed)(?:,\s*(?P<volume>\d{1,3})\s+U\.S\.\s+(?P<page>\d{1,4}))?|reh'?g\s+(?:denied|granted)`

Short forms → URL key:

RSA → `rsa`; N.H. Rev. Stat. Ann. → `rsa`; N.H. Rev. Stat. → `rsa`; NH RSA → `rsa`; New Hampshire Revised Statutes Annotated → `rsa`

RSA citations are distinctive ('RSA 358-A:2', chapter:section with a colon). The URL also needs the title as a Roman numeral, which a citation does not carry; take it from the chapter ranges on https://gc.nh.gov/rsa/html/nhtoc.htm. Subdivisions are Roman numerals after a comma ('RSA 126-G:2, I'), so do not read the ', I' as part of the section. Neutral citations ('2024 N.H. 1') have a four-digit year and N.H. Reports citations ('176 N.H. 319') have a three-digit volume; the regex keeps the two apart. Bare 'Sup. Ct. R. 7', 'Superior Court Rule 12', bare agency-prefixed rule numbers ('Env-Wq 1001.01', 'Ban 101.01'), bare docket numbers and 'cert. denied' are context_required. The Supreme Court's nonprecedential final orders (Sup. Ct. R. 12-D) are cited by docket number and date. CourtListener ids 'nh' and 'nhsuperct' are from memory and unverified. The bare agency-prefix pattern is case-sensitive (inline (?-i:)) and excludes common words (Rule, Laws, Part, Title, month names …), so 'RSA 507', 'Laws 1986' and 'Rule 404' no longer match it (independent check 2026-10-17).

## A. Statutes / code

### `nh-rsa-gc` — New Hampshire Revised Statutes Online (RSA)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · New Hampshire General Court (Office of Legislative Services) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All RSA titles I-LXV. One HTML page per section, plus a whole-chapter page {chapter}-mrg.htm.
- **Access:** `constructible` · format html
  - Pattern: `https://gc.nh.gov/rsa/html/{title_roman}/{chapter}/{chapter}-{section}.htm`
  - Placeholders: title_roman: the RSA title in upper-case Roman numerals. A citation does not give it: look it up in the chapter ranges on https://gc.nh.gov/rsa/html/nhtoc.htm ('TITLE XXXI: TRADE AND COMMERCE (Includes Chapters 333 - 359-V)'). chapter: as cited, with an upper-case letter suffix (567-A, 126-G). section: the part after the colon; the colon becomes a hyphen (567-A:1 → 567-A-1.htm). Whole chapter: https://gc.nh.gov/rsa/html/{title_roman}/{chapter}/{chapter}-mrg.htm. Chapter TOC: https://gc.nh.gov/rsa/html/NHTOC/NHTOC-{title_roman}-{chapter}.htm. Lettered section suffixes are lower case in file names (RSA 507:7-d → /rsa/html/LII/507/507-7-d.htm; independently verified). The older host www.gencourt.state.nh.us serves the same paths.
  - Index: `https://gc.nh.gov/rsa/html/nhtoc.htm`
  - Navigation: nhtoc.htm (titles with chapter ranges) → NHTOC/NHTOC-{title}.htm (chapters) → NHTOC/NHTOC-{title}-{chapter}.htm (section links and the -mrg whole-chapter link) → section page.
- **Automation:** WebFetch gated · shell http-error · robots: unreadable: the connection closed without a response on gc.nh.gov and www.gencourt.state.nh.us (twice, 2026-10-17)
  - WebFetch reads pages whose URL came from a search result or a fetched page (NHTOC-X-126-G.htm, 126-G-2.htm, 126-G-mrg.htm, 567-A-1.htm). URLs built from the pattern (358-A-2.htm, and NHTOC-XXXI-358-A.htm even though it was linked from NHTOC-XXXI.htm) waited on a permission prompt (PROVENANCE_REQUIRED). fetch_doc.py: 'robots.txt on gc.nh.gov unreachable after a retry (Remote end closed connection without response)'.
- **Currency:** Revised Statutes Online landing page (https://gc.nh.gov/rsa/html/indexes/default.aspx); section pages show only a 'Source.' history line — observed: "current through the 2026 regular legislative session. Last updated: September 2026."
- **Official status:** https://gc.nh.gov/rsa/html/indexes/default.aspx footer: 'THE MATERIAL AVAILABLE ON THIS WEBSITE, WHILE BELIEVED TO BE ACCURATE, IS PROVIDED FOR INFORMATIONAL PURPOSES ONLY.' No UELMA authentication statement seen.
- **Hazard:** the title (Roman numeral) cannot be derived from the citation; it needs the nhtoc.htm chapter ranges
- **Hazard:** built URLs are gated for WebFetch
- **Hazard:** script route fails: the server drops the connection
- **Hazard:** the chapter TOC pages hold no section text
- **Hazard:** repealed sections are listed in the TOC as 'Repealed'
- **Probe:** RSA 126-G:2 → `https://gc.nh.gov/rsa/html/X/126-G/126-G-2.htm` — expect: "In this chapter: I. "Area" means "area" as defined in"
- **Evidence (2026-10-17):** WebFetch 126-G-2.htm YES 'In this chapter: I. "Area" means'; Source line '1989, 255:2. 1995, 310:79'. Second citation RSA 567-A:1 (title LVI): YES 'A person who is aggrieved by a decree, order, appointment'. 126-G-mrg.htm holds 126-G:1 to :5, not truncated. nhtoc.htm shows chapter ranges. | Independent check 2026-10-17: WebFetch YES 'In this chapter: I. "Area" means'; Source '1989, 255:2. 1995, 310:79'; second citation RSA 507:7-d (title LII) and RSA 637:3 (title LXII) ok
- **Notes:** Two titles verified (X and LVI). The script route needs a later retry; if gc.nh.gov answers, set automation.shell from the result.

### `nh-session-laws-gc` — New Hampshire chaptered laws (General Court bill status)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · New Hampshire General Court · text: **link-only** · official: unknown
- **Coverage:** Chaptered laws reached through the gc.nh.gov bill-status pages. Not probed.
- **Access:** `link-only` · format html
  - Index: `https://gc.nh.gov/bill_Status/`
  - Navigation: Not probed. The RSA section 'Source.' lines give year and chapter:section ('1989, 255:2').
- **Automation:** WebFetch fail · shell http-error · robots: unreadable (connection closed)
  - gc.nh.gov drops script connections.
- **Currency:** unknown
- **Hazard:** not probed
- **Hazard:** index https://gc.nh.gov/bill_Status/ unreadable: WebFetch CLIENT_ERROR (independent check 2026-10-17); no working route to session-law text
- **Probe:**  → ``
- **Evidence (2026-10-17):** Not probed (budget and priority). The gc.nh.gov 'dynamicdatadump' bulk files cover bills/LSRs, not session-law text. | Independent check 2026-10-17: WebFetch https://gc.nh.gov/bill_Status/ CLIENT_ERROR 'There was an error while fetching.' (failed)

### `nh-rsa-justia` — Justia: 2025 New Hampshire Revised Statutes

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** RSA, 2025 edition; earlier editions (2014-2024) under /codes/new-hampshire/{year}/.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/new-hampshire/title-{title_roman_lower}/chapter-{chapter_lower}/section-{chapter_lower}-{section}/`
  - Placeholders: title in lower-case Roman numerals (title-xliii), chapter in lower case (chapter-458-a); the section slug replaces the colon with a hyphen (458:2 → section-458-2). The title comes from gc.nh.gov's nhtoc.htm chapter ranges. Some chapters are listed without a link (457-A).
  - Index: `https://law.justia.com/codes/new-hampshire/`
  - Navigation: title page → chapter page (section links) → section page
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (law.justia.com robots.txt answered with a challenge; host off for the day in fetch_doc.py)
- **Currency:** page heading — observed: "2025 New Hampshire Revised Statutes"
- **Official status:** Third-party compilation; the page says 'These codes may not be the most recent version.'
- **Hazard:** edition lags the official site (2025 vs. 2026 session)
- **Hazard:** some chapters are listed without a link
- **Probe:** RSA 458:2 → `https://law.justia.com/codes/new-hampshire/title-xliii/chapter-458/section-458-2/` — expect: "If any doubt exists whether any marriage is void, or"
- **Evidence (2026-10-17):** WebFetch YES 'If any doubt exists whether any marriage is void, or'; heading '2025 New Hampshire Revised Statutes'. Title and chapter pages list section links in the pattern above. | Independent check 2026-10-17: WebFetch YES 'If any doubt exists whether any marriage is void, or'; '2025 New Hampshire Revised Statutes'; second citation RSA 637:3 ok

## B. Constitution

### `nh-constitution-nhgov` — New Hampshire State Constitution (NH.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · State of New Hampshire · text: **link-only** · official: unknown
- **Coverage:** Current constitution (reported).
- **Access:** `link-only` · format html
  - Index: `https://www.nh.gov/glance/state-constitution`
  - Navigation: Unknown: the page could not be read.
- **Automation:** WebFetch fail · shell blocked-challenge · robots: www.nh.gov answers robots.txt with a bot check
  - WebFetch: 'There was an error while fetching.'
- **Currency:** unknown
- **Official status:** Wikipedia labels the link 'Official state website'; the page itself could not be read.
- **Hazard:** bot check on the host; never route around it
- **Probe:** N.H. Const. pt. I, art. 15 → `https://www.nh.gov/glance/state-constitution`
- **Evidence (2026-10-17):** fetch_doc.py: REFUSED, 'www.nh.gov answers robots.txt with a bot check'. WebFetch: CLIENT_ERROR 'There was an error while fetching.' | Re-confirmed blocked 2026-10-17: WebFetch CLIENT_ERROR 'There was an error while fetching.'; fetch_doc.py check REFUSED (bot check)
- **Notes:** No other official constitution text found: gc.nh.gov and sos.nh.gov hosted none in search results. sos.nh.gov's robots.txt also answers with a bot check.

### `nh-constitution-justia` — Justia: New Hampshire Constitution

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Part First (Bill of Rights) on billofrights.html; Part Second (Form of Government) split over 11 pages by subject.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/constitution/new-hampshire/{part_page}`
  - Placeholders: pt. I: billofrights.html. pt. II: choose the page by article range. formofgov.html Arts. 1-8; house 9-24; senate 25-40; governor 41-59; council 60-66; secretary 67-70; treasurer 71-72; judicial 72-a-81; clerks 82; lit 83; oaths 84-101. Only formofgov.html and judicial.html were seen as file names; take the other page links from the index, not by appending '.html' to the stem. Find the article on the page by its number heading.
  - Index: `https://law.justia.com/constitution/new-hampshire/`
  - Navigation: index (headings and page links, no text) → billofrights.html for pt. I, or the pt. II subject page whose article range covers the article (pt. II, art. 73-a → judicial.html)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (403 challenge)
  - formofgov.html not probed; it may pass the 100K WebFetch window.
- **Currency:** page header on billofrights.html — observed: "AS SUBSEQUENTLY AMENDED AND IN FORCE DECEMBER 1990"
- **Official status:** Third-party; index says 'may not be the most recent version.'
- **Hazard:** stale: in force December 1990; later amendments (e.g. pt. I art. 2-b, 2018) may be missing
- **Hazard:** index page holds headings only
- **Hazard:** pt. II is split across 11 pages: formofgov.html holds only Arts. 1-8 (independent check 2026-10-17 found pt. II art. 73-a on judicial.html, not formofgov.html)
- **Hazard:** pt. I art. 2-b is missing from billofrights.html (confirmed independently)
- **Probe:** N.H. Const. pt. I, art. 15 → `https://law.justia.com/constitution/new-hampshire/billofrights.html` — expect: "No subject shall be held to answer for any crime,"
- **Evidence (2026-10-17):** WebFetch YES 'No subject shall be held to answer for any crime,'; header 'IN FORCE DECEMBER 1990'; amendment notes 1966 and 1984; not truncated. Index page: Art. 15 body NOT PRESENT. | Independent check 2026-10-17: WebFetch YES Art. 15 'No subject shall be held to answer for any crime,'; 'IN FORCE DECEMBER 1990'; pt. II art. 73-a failed at formofgov.html, found on judicial.html 'The chief justice of the supreme court shall be the administrative'
- **Notes:** Only as a last resort, and always with the 1990 currency warning.

## C. Court rules

### `nh-rules-crimp-courts` — New Hampshire Rules of Criminal Procedure

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · New Hampshire Judicial Branch · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Rules 1-53 on one page (136,231 characters).
- **Read via (in order):** **fetch tool**
- **Access:** `link-only` · format html
  - Index: `https://courts.nh.gov/new-hampshire-rules-criminal-procedure`
  - Navigation: Single page. WebFetch window 1 ends mid Rule 23; use offset=100000 for Rules 23-53.
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: courts.nh.gov answers robots.txt with a bot check
- **Currency:** Rule 2(b) — observed: "These rules govern all proceedings filed on or after January 1, 2024."
- **Official status:** Rules index says it 'is not an official publication of the court rules'.
- **Hazard:** truncation at about 100K characters (ends in Rule 23)
- **Hazard:** script route blocked
- **Probe:** N.H. R. Crim. P. 1 → `https://courts.nh.gov/new-hampshire-rules-criminal-procedure` — expect: "These rules govern the procedure in circuit court-district division and"
- **Evidence (2026-10-17):** WebFetch YES Rule 1 'These rules govern the procedure in circuit court-district division and'; 136,231 chars; truncated mid Rule 23. | Independent check 2026-10-17: WebFetch YES Rule 1(a); Rule 2(b) currency string present; 136,231 chars, cut mid Rule 23(b)(8)

### `nh-rules-evidence-courts` — New Hampshire Rules of Evidence

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · New Hampshire Judicial Branch · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Rules 100-1103 on one page (110,415 characters).
- **Read via (in order):** **fetch tool**
- **Access:** `link-only` · format html
  - Index: `https://courts.nh.gov/rules-evidence`
  - Navigation: Single page holding every rule. WebFetch window 1 (offset 0) ends in Rule 902(4)(A); read later rules with offset=100000.
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: courts.nh.gov answers robots.txt with a bot check
  - Per-rule pages exist on courts.nh.gov (e.g. a GAL rule at /system-wide-guardian-ad-litem-.../rule-11-authority-and, a slug cut off mid-word), but no evidence-rule slug was found.
- **Currency:** amendment notes under the rules — observed: "made by supreme court order dated April 20, 2017, effective July 1, 2017"
- **Official status:** Rules index (https://www.courts.state.nh.us/rules/index.htm) says it 'is not an official publication of the court rules'.
- **Hazard:** truncation at about 100K characters
- **Hazard:** script route blocked by bot check
- **Probe:** N.H. R. Evid. 403 → `https://courts.nh.gov/rules-evidence` — expect: "The court may exclude relevant evidence if its probative value is"
- **Evidence (2026-10-17):** WebFetch YES Rule 403 'The court may exclude relevant evidence if its probative value is'; Rule 401 present; page 110,415 chars, cut off after Rule 902(4)(A). | Independent check 2026-10-17: WebFetch YES Rule 403; 'April 20, 2017, effective July 1, 2017' note; cut in 902(4)(A); fetch_doc.py REFUSED (exit 3)

### `nh-rules-superior-courts` — Rules of the Superior Court of the State of New Hampshire

- **Status:** REPORTED 2026-10-17 · **Tier 1** · New Hampshire Judicial Branch · text: **link-only** · official: unofficial
- **Coverage:** Superior Court Rules (civil and criminal practice). Circuit Court (District, Probate, Family Division) rules and e-filing rules are listed on the same index.
- **Access:** `link-only` · format html
  - Index: `https://courts.nh.gov/rules-superior-court-state-new-hampshire`
  - Navigation: Single page (URL from search). Not read.
- **Automation:** WebFetch fail · shell blocked-challenge · robots: courts.nh.gov answers robots.txt with a bot check
  - WebFetch: 'There was an error while fetching.' The page is probably very long.
- **Currency:** unknown
- **Official status:** Rules index disclaimer: 'not an official publication of the court rules'.
- **Hazard:** WebFetch error
- **Hazard:** script blocked
- **Hazard:** independent check 2026-10-17: WebFetch CLIENT_ERROR again; no readable route to the rule text
- **Probe:** N.H. Super. Ct. R. 12 → `https://courts.nh.gov/rules-superior-court-state-new-hampshire`
- **Evidence (2026-10-17):** WebFetch CLIENT_ERROR 'There was an error while fetching.' | Independent check 2026-10-17: WebFetch CLIENT_ERROR 'There was an error while fetching.' (failed)

### `nh-rules-supreme-courts` — Rules of the Supreme Court of the State of New Hampshire

- **Status:** REPORTED 2026-10-17 · **Tier 1** · New Hampshire Judicial Branch · text: **link-only** · official: unofficial
- **Coverage:** Supreme Court Rules (incl. Rule 7 appeals, Rule 12-D final orders, Rule 22 rehearing).
- **Read via (in order):** **fetch tool**
- **Access:** `link-only` · format html
  - Index: `https://www.courts.state.nh.us/rules/scr/index.htm`
  - Navigation: Link-only: the old-host TOC (https://www.courts.state.nh.us/rules/scr/index.htm) lists rule titles ('Rule 7. Appeal from Trial Court Decision on the Merits.') but WebFetch returns no hrefs, so no rule body is reachable. The current page sits under https://www.courts.nh.gov/rules-supreme-court-state-new-hampshire; only its /note subpage was read.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.courts.state.nh.us and courts.nh.gov answer robots.txt with a bot check
  - No rule body text reached.
- **Currency:** note page — observed: "subject to revisions promulgated from time to time"
- **Official status:** Rules index disclaimer: 'not an official publication of the court rules'. The note says revisions are published in the New Hampshire Bar News.
- **Hazard:** TOC without links in WebFetch output
- **Hazard:** body text not reached
- **Probe:** N.H. Sup. Ct. R. 7 → `https://www.courts.state.nh.us/rules/scr/index.htm`
- **Evidence (2026-10-17):** WebFetch: TOC only, Rule 7 body NOT PRESENT; /note subpage holds only the revision note. | Independent check 2026-10-17: WebFetch TOC only, no hrefs (confirmed)

## D. Administrative code

### `nh-admin-rules-gc` — New Hampshire Code of Administrative Rules (Office of Legislative Services)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · NH General Court, Office of Legislative Services, Administrative Rules · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Rules by agency, one HTML file per chapter; online text may lag amendments or include expired rules.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://gc.nh.gov/rules/State_Agencies/{prefix_lower}{chapter}.html`
  - Placeholders: Agency TOC: /rules/state_agencies/{prefix}.html (prefix lower-cased, hyphen kept: env-dw.html, ban.html; some file names mixed case, e.g. Ec-Wst.html, Saf-Mec.html; some agencies have no link). Chapter file: {prefix}{chapter hundred}.html (Ban 101.01 → ban100.html; Env-Dw 702.01 → env-dw700.html). Chapter links on agency TOCs often point to http://gencourt.state.nh.us/rules/State_Agencies/{file}, which 302-redirects to gc.nh.gov with 'State_Agencies' in mixed case. Treat the path as case-sensitive: use the redirect target exactly as given and re-issue WebFetch on it. Confirm the chapter file through the agency TOC.
  - Index: `https://gc.nh.gov/rules/about_rules/listagencies.aspx`
  - Navigation: listagencies.aspx → agency TOC (chapters, parts, section titles; no text) → chapter link (old gencourt host, 302 to gc.nh.gov/rules/State_Agencies/…) → chapter file holds the section text
- **Automation:** WebFetch ok · shell http-error · robots: unreadable (connection closed)
  - Pages reached by following links read fine; built URLs are likely gated, as they are on the RSA pages.
- **Currency:** none on chapter pages; check with /rules/about_rules/checkrule.aspx
- **Official status:** https://gc.nh.gov/rules/about_rules/official_version.aspx: 'There is no official publisher of the complete New Hampshire Code of Administrative Rules'; rules on the website are 'NOT the official version'.
- **Hazard:** not official
- **Hazard:** online text may lag or include expired rules
- **Hazard:** file-name case is inconsistent
- **Hazard:** chapter links go through a 302 from gencourt.state.nh.us to a mixed-case State_Agencies path; re-issue WebFetch on the redirect
- **Hazard:** large chapter files pass the 100K WebFetch window (env-dw700.html 103,496 chars)
- **Probe:** N.H. Admin. Code Ban 101.01 → `https://gc.nh.gov/rules/state_agencies/ban100.html` — expect: "The purpose of these rules is to describe the New Hampshire"
- **Evidence (2026-10-17):** WebFetch YES Ban 101.01 'The purpose of these rules is to describe the New Hampshire'; source note '#1596, eff 6-30-80'. ban.html is a TOC with chapter links ban100/500/700.html. | Independent check 2026-10-17: WebFetch YES 'The purpose of these rules is to describe the New Hampshire banking'; second citation N.H. Code Admin. R. Env-Dw 702.01 (env-dw700.html) ok

### `nh-admin-rules-lii` — Cornell LII: New Hampshire Code of Administrative Rules

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All agency titles, per section, with 'Amended by' Register references.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/new-hampshire/N-H-Admin-Code-SS-{prefix}-{section}`
  - Placeholders: prefix as cited, case and hyphen kept (Ban, Env-Dw); section with its dot (101.01). Ban 101.01 → N-H-Admin-Code-SS-Ban-101.01; Env-Dw 702.01 → N-H-Admin-Code-SS-Env-Dw-702.01. Browse: /regulations/new-hampshire/title-{prefix}/chapter-{prefix}-{chapter}/part-{prefix}-{part}.
  - Index: `https://www.law.cornell.edu/regulations/new-hampshire`
  - Navigation: title-{prefix} → chapter → part → section links
- **Automation:** WebFetch untested · shell ok · robots: User-agent * Crawl-delay 10; /regulations/ not disallowed
- **Currency:** HTTP Last-Modified only; the page has no currency line — observed: "last-modified Mon, 04 Aug 2025"
- **Official status:** Third-party compilation (state regulations collection).
- **Hazard:** stale: LII's Ban 101.01 history ends '#10258, eff 1-24-13' while gc.nh.gov shows 'ss by #14096, eff 10-3-24' (Last-Modified Aug. 2025)
- **Hazard:** expired chapters still listed
- **Probe:** N.H. Admin. Code Ban 101.01 → `https://www.law.cornell.edu/regulations/new-hampshire/N-H-Admin-Code-SS-Ban-101.01` — expect: "The purpose of these rules is to describe the New Hampshire banking department"
- **Evidence (2026-10-17):** fetch_doc.py grep: 2,825 chars, 'The purpose of these rules is to describe the New Hampshire banking department'. Second: N-H-Admin-Code-SS-Env-Dw-702.01, 2,755 chars, '#9699, eff 5-1-10'. | Independent check 2026-10-17: fetch_doc.py grep 2,825 chars 'describe the New Hampshire banking department'; LM Aug 4 2025; second citation N.H. Admin. Code Saf-C 6001.01 ok

## D. Administrative register

### `nh-register-gc` — New Hampshire Rulemaking Register

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · NH General Court, Office of Legislative Services · text: **fetch-and-quote** · official: official
- **Coverage:** Weekly issues since 2000, PDF. Through WebFetch only the latest issue is linkable.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.gc.nh.gov/rules/register/default.aspx`
  - Navigation: default.aspx → viewer link for the LATEST issue only (viewer.aspx?fileName=F:\Websites\GCNHWeb\Rules\register\{year}\No {n} {Month} {d} {year}.PDF; copy it from the listing, never build it). In WebFetch output earlier 2026 issues and all earlier years are plain text and the year list has no hrefs. Back issues are link-only: cite them by number and date, or get them from adminrules@gc.nh.gov.
- **Automation:** WebFetch ok · shell http-error · robots: unreadable (connection closed)
- **Currency:** register listing page — observed: "published weekly each Thursday (or earlier if Thursday is a holiday)"
- **Official status:** Published by the Office of Legislative Services; electronic-only since July 14, 2018 (availability.aspx).
- **Hazard:** viewer URL embeds a Windows file path with spaces
- **Hazard:** issue No 33 (Aug. 20, 2026) listed without a link
- **Hazard:** only the latest issue is reachable; back issues (e.g. 2025 No. 10) failed in the independent check 2026-10-17
- **Probe:** N.H. Rulemaking Register No. 34 (Aug. 27, 2026) → `https://www.gc.nh.gov/rules/register/viewer.aspx?fileName=F:\Websites\GCNHWeb\Rules\register\2026\No 34 August 27 2026.PDF` — expect: "NEW HAMPSHIRE RULEMAKING REGISTER OFFICE OF LEGISLATIVE SERVICES"
- **Evidence (2026-10-17):** WebFetch YES 'NEW HAMPSHIRE RULEMAKING REGISTER OFFICE OF LEGISLATIVE SERVICES ROOM 234,'; not truncated. Listing: earliest year 2000; latest No 34, Aug. 27, 2026. | Independent check 2026-10-17: WebFetch YES 'NEW HAMPSHIRE RULEMAKING REGISTER OFFICE OF LEGISLATIVE SERVICES ROOM 234,'; 'Number 34, August 27, 2026'

## E. Case law

### `nh-opinions-courts` — New Hampshire Supreme Court opinions (Judicial Branch)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · New Hampshire Judicial Branch (Reporter of Decisions) · text: **link-only** · official: unofficial
- **Coverage:** Slip-opinion PDFs. From 1 Jan. 2024 they are listed by neutral citation number in reverse order; earlier ones by case number. Older PDFs sit under /sites/g/files/ehbemt471/files/documents/{yyyy-mm}/{slug}.pdf (e.g. 2021-07/2020021torromeo.pdf).
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.courts.state.nh.us/supreme/opinions/index.htm`
  - Navigation: The old-host opinions page shows only the notice, with no list or hrefs. The current listing is under courts.nh.gov (Supreme Court → Orders and Opinions → Opinions) but could not be read. A site search exists at https://courts.nh.gov/search?page=N; its query parameter was not seen. Neutral-citation paragraphs (¶) replace page pinpoints from 2024.
- **Automation:** WebFetch gated · shell blocked-challenge · robots: courts.nh.gov, www.courts.nh.gov and www.courts.state.nh.us answer robots.txt with a bot check
  - WebFetch reads pages whose URL came from a search result (news release, taxonomy/term/1856, search?page=28) but returns no hrefs from them. The built listing URL and an opinion PDF taken from the search page were gated (PROVENANCE_REQUIRED).
- **Currency:** listing page (not read)
- **Official status:** Opinions page: slip opinions are subject to rehearing and formal revision before publication in the New Hampshire Reports. Since 2024 opinions carry neutral citations (news release https://www.courts.nh.gov/news-and-media/supreme-court-announces-adoption-neutral-citation-form).
- **Hazard:** listing not read; the opinions page on the old host shows only the notice
- **Hazard:** script route blocked by bot check
- **Hazard:** slip pagination; N.H. Reports pagination added later; neutral ¶ numbers from 2024
- **Probe:** Torromeo Indus. v. State, No. 2019-0121 → `https://www.courts.nh.gov//sites/g/files/ehbemt471/files/documents/2021-07/2020021torromeo.pdf`
- **Evidence (2026-10-17):** Opinions page: notice only, no list. Neutral-citation release read: '2024 N.H. 1' format, paragraph pinpoints. Opinion PDF: WebFetch PROVENANCE_REQUIRED.
- **Notes:** Most important gap: no verified official route to opinion text.

### `nh-orders-courts` — New Hampshire Supreme Court case orders (final orders, Rule 12-D)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · New Hampshire Judicial Branch · text: **link-only** · official: unofficial
- **Coverage:** Nonprecedential final orders and case orders listed by docket number and title.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Index: `https://www.courts.nh.gov/taxonomy/term/1856?page=0`
  - Navigation: Paged listing (?page=0,1,2…) of docket number and title. WebFetch gave no hrefs or dates.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot check on robots.txt
- **Currency:** none stated
- **Hazard:** no dates or links in WebFetch output
- **Hazard:** orders are not precedent
- **Probe:** State v. Ruel, No. 2023-0175 → `https://www.courts.nh.gov/taxonomy/term/1856?page=0` — expect: "2023-0175, State of New Hampshire v. Kevin M. Ruel"
- **Evidence (2026-10-17):** WebFetch: nine entries, e.g. '2023-0175, State of New Hampshire v. Kevin M. Ruel'; no hrefs, no dates; order text not reached.

### `nh-cases-justia` — Justia: New Hampshire Supreme Court decisions

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court opinions by year (2023: 61 cases), HTML plus a cases.justia.com PDF of the slip opinion.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/new-hampshire/supreme-court/{year}/{docket}.html`
  - Placeholders: year = DECISION year, taken from the year listing; it is not the docket prefix (State v. Sleeper, No. 2024-0035, decided Dec. 5, 2025 → /2025/2024-0035.html). docket = NH Supreme Court case number as printed. Year listing: /cases/new-hampshire/supreme-court/{year}/. Pages for 2024 on show the neutral citation ('Citation: State v. Sleeper, 2025 N.H. 52') and ¶ numbers. PDF link on the page: https://cases.justia.com/new-hampshire/supreme-court/{year}-{docket}.pdf?ts=…
  - Index: `https://law.justia.com/cases/new-hampshire/supreme-court/`
  - Navigation: year listing (case name, docket, date) → case page
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: unreadable (challenge)
  - Long opinions pass 100K characters (Brown v. Secretary of State: 122,410); use offset=100000.
- **Currency:** none stated
- **Official status:** Third-party copy of slip opinions.
- **Hazard:** truncation of long opinions
- **Hazard:** no N.H. Reports citation shown for recent opinions
- **Hazard:** slip text, not the revised N.H. Reports text
- **Hazard:** decision year ≠ docket year; never take {year} from the docket prefix
- **Probe:** Brown v. Sec'y of State, No. 2022-0629 (N.H. Nov. 29, 2023) → `https://law.justia.com/cases/new-hampshire/supreme-court/2023/2022-0629.html` — expect: "This case presents a question of first impression"
- **Evidence (2026-10-17):** WebFetch: 'DONOVAN, J. This case presents a question of first impression'; 122,410 chars, cut off in the dissent; PDF href cases.justia.com/.../2023-2022-0629.pdf. 2023 listing: 61 cases with docket and date. | Independent check 2026-10-17: WebFetch YES 'DONOVAN, J. This case presents a question of first impression'; 122,410 chars truncated; second citation State v. Sleeper, 2025 N.H. 52 (No. 2024-0035) ok

## F. Subsequent history

### `nh-scotus-docket` — U.S. Supreme Court docket (certiorari from the New Hampshire Supreme Court)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of the United States · text: **fetch-and-quote** · official: official
- **Coverage:** New Hampshire has no intermediate appellate court; the Supreme Court is the court of last resort, so further review is certiorari only (rehearing motions under Sup. Ct. R. 22 are decided by the same court). Dockets show 'Lower Ct: Supreme Court of New Hampshire', 'Case Numbers: (2025-0297)' and the disposition.
- **Read via (in order):** **script**
- **Access:** `search-only` · format html
  - Pattern: `https://www.supremecourt.gov/docket/docketfiles/html/public/{scotus_docket}.html`
  - Placeholders: Constructible only once the SCOTUS docket number is known (25-1390, 24A1016). From an NH docket alone there is no URL: WebSearch '"<NH docket>" supremecourt.gov' or 'Lower Ct: Supreme Court of New Hampshire', or search by party name.
  - Index: `https://www.supremecourt.gov/docket/docket.aspx`
- **Automation:** WebFetch untested · shell ok · robots: docket path allowed (fetch_doc.py ok)
- **Currency:** dated docket entries — observed: "Oct 05 2026 Petition DENIED."
- **Official status:** Docket kept by the Clerk of the Supreme Court.
- **Hazard:** no link from the NH docket to the SCOTUS docket
- **Probe:** Richard v. New Hampshire, No. 25-1390 (from N.H. No. 2025-0297) → `https://www.supremecourt.gov/docket/docketfiles/html/public/25-1390.html` — expect: "Petition DENIED."
- **Evidence (2026-10-17):** fetch_doc.py grep: 4,941 chars; 'Lower Ct: Supreme Court of New Hampshire'; 'Case Numbers: (2025-0297)'; 'Oct 05 2026 Petition DENIED.' Also 24A1016 (2024-0491), 25A908 (2025-0454) show NH lower court. | Independent check 2026-10-17: fetch_doc.py grep 4,941 chars 'Oct 05 2026 Petition DENIED.'; second citation G. M. v. New Hampshire, No. 24A1016 (N.H. No. 2024-0491) ok
- **Notes:** Respondent name on 25-1390 not checked (title 'Daniel Richard, Petitioner'). The citation string is a probe label only.

## Not available (do not look for these again)

- **case_law** — Free official New Hampshire Reports text with official pagination: Opinions page says slip opinions are revised before publication in the New Hampshire Reports; no free N.H. Reports source found. From 2024 the neutral citation with ¶ pinpoints removes the need for page numbers. (2026-10-17)
- **subsequent_history** — Intermediate appellate court / leave-to-appeal dispositions: New Hampshire has no intermediate appellate court; appeals go straight to the Supreme Court. (2026-10-17)
- **statutes** — Official bulk download of RSA text: https://www.gc.nh.gov/dynamicdatadump lists 13 .txt files (legislators, LSRs, dockets, roll calls); none holds RSA text. (2026-10-17)
- **statutes** — Cornell LII New Hampshire statutes/constitution: LII's New Hampshire holding seen is the administrative code only (https://www.law.cornell.edu/regulations/new-hampshire). (2026-10-17)

## Corpus candidates (maintainers)

- `nh-rules-evidence-courts` — Single 110,415-char page; WebFetch stops in Rule 902(4)(A); script route blocked by bot check.
- `nh-rules-crimp-courts` — Single 136,231-char page; WebFetch stops in Rule 23 of 53.
- `nh-rules-superior-courts` — Single page; WebFetch errored, probably on length.

## Open questions

- gc.nh.gov / www.gencourt.state.nh.us dropped the script connection on robots.txt (twice, 2026-10-17). Retry; if it answers, the RSA, admin-rules and register rows may become script-ok.
- Locate and probe the courts.nh.gov Supreme Court opinions listing and one slip-opinion PDF (WebFetch gated, script blocked). Confirm the GET search parameter for https://courts.nh.gov/search.
- Official constitution text: www.nh.gov/glance/state-constitution could not be read (WebFetch error; bot check for the script). Is there a gc.nh.gov or sos.nh.gov copy?
- Supreme Court Rules and Superior Court Rules body text not reached; check whether per-rule pages exist on courts.nh.gov.
- Session laws (chaptered laws) on gc.nh.gov not probed.
- Justia regulations (regulations.justia.com) for NH admin rules and new-hampshire.public.law (proxy 502 on robots.txt) not checked.
- CourtListener ids 'nh' and 'nhsuperct' unverified.
- Superior Court Rules: two WebFetch errors (research and independent). Look for per-rule pages on courts.nh.gov or ingest as a corpus once a route exists.
- Session laws: find a readable chaptered-laws page linked from gc.nh.gov; bill_Status/ fails in WebFetch and the script cannot connect.
- Rulemaking Register back issues: find a per-year archive URL linked from gc.nh.gov.
