# Arizona (AZ) — free legal sources

_Generated from `data/az.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: azleg.gov per-section pages are constructible (/ars/{title}/{section zero-padded to 5, '.' -> '-'}.htm) and read cleanly by fetch_doc.py, but robots.txt sets Crawl-delay 120 (two minutes per request); azleg says its online ARS is unofficial (official edition is Thomson Reuters) and shows law effective the following January 1. Justia's 2025 ARS is a constructible tier-2 fallback. Constitution: azleg.gov /const/{article}/{section}.htm. Court rules: the only free official text is Westlaw's govt site (azrules.westgroup.com / govt.westlaw.com/azrules), which refuses automated access; no tier-2 copy exists. Admin Code and Register: apps.azsos.gov chapter/issue PDFs (WebFetch reads them; the shell route is refused by a bot check); Cornell LII mirrors the A.A.C. per section. Case law: Supreme Court opinion PDFs at www.azcourts.gov/Portals/0/OpinionFiles/Supreme/{year}/{docket}.pdf; the Court of Appeals search pages are JavaScript apps with a token-protected API, so Justia (1965-2026, both divisions, memorandum decisions included) is the practical route; apps.azcourts.gov docket PDFs give subsequent history (descendant/predecessor case numbers) while a case is recent.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Arizona Supreme Court | `ariz (unverified)` | Ariz. | Ariz., P.3d, P.2d, P. | — |
| Arizona Court of Appeals (Division One and Division Two) | `arizctapp (unverified)` | Ariz. Ct. App. | Ariz., Ariz. App., P.3d, P.2d | — |
| Arizona Tax Court | `ariztaxct (unverified)` | Ariz. Tax Ct. | Ariz., P.3d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Arizona Revised Statutes | `A.R.S. § 12-542`; `Ariz. Rev. Stat. Ann. § 12-542`; `Ariz. Rev. Stat. § 13-1105(A)(1)`; `A.R.S. § 12-341.01`; `ARS 41-1092.01`; `A.R.S. §§ 12-541 to -542`; `section 12-821.01 of the Arizona Revised Statutes`; `Arizona Revised Statutes section 13-1105` | `az-ars-azleg` → `az-ars-justia` |
| Arizona Constitution | `Ariz. Const. art. 2, § 4`; `Ariz. Const. art. II, § 4`; `Ariz. Const. art. 6, § 14`; `Ariz. Const. art. 2, § 2.1`; `Article 2, Section 4 of the Arizona Constitution`; `Ariz. Const. art. IV, pt. 2, § 1`; `Ariz. Const. art. 6.1, § 4`; `Article 4, Part 2, Section 1 of the Arizona Constitution` | `az-constitution-azleg` |
| Arizona Rules of Civil Procedure | `Ariz. R. Civ. P. 12(b)(6)`; `Rule 56 of the Arizona Rules of Civil Procedure`; `Ariz.R.Civ.P. 26.1` | `az-rules-westlaw` |
| Arizona Rules of Evidence | `Ariz. R. Evid. 702`; `Rule 803(6) of the Arizona Rules of Evidence` | `az-rules-westlaw` |
| Arizona Rules of Civil Appellate Procedure (ARCAP) | `ARCAP 13(a)(7)`; `Ariz. R. Civ. App. P. 21`; `Rule 13 of the Arizona Rules of Civil Appellate Procedure` | `az-rules-westlaw` |
| Arizona Rules of Criminal Procedure | `Ariz. R. Crim. P. 32.1(a)`; `Rule 15.1 of the Arizona Rules of Criminal Procedure` | `az-rules-westlaw` |
| Rules of the Supreme Court of Arizona (incl. Rule 42 ERs, Rule 111) | `Ariz. R. Sup. Ct. 111(c)`; `Ariz. R. Sup. Ct. 42, ER 1.7`; `Rule 42, ER 1.8 of the Rules of the Supreme Court`; `Ariz. Sup. Ct. R. 31` | `az-rules-westlaw` |
| Arizona Rules of Family Law Procedure | `Ariz. R. Fam. Law P. 49`; `Rule 91(a) of the Arizona Rules of Family Law Procedure`; `ARFLP 65` | `az-rules-westlaw` |
| Arizona Administrative Code | `A.A.C. R9-10-101`; `Ariz. Admin. Code R4-23-110`; `Ariz. Admin. Code § R9-10-101`; `Ariz. Admin. Code R9-10-101(12)` | `az-aac-sos` → `az-aac-lii` |
| Arizona Administrative Register | `8 A.A.R. 3559`; `32 Ariz. Admin. Reg. 2539` | `az-register-sos` |
| Arizona Reports (Ariz.) and old Arizona Appeals Reports (Ariz. App.) | `City of Mesa v. Ryan, 256 Ariz. 350 (App. 2023)`; `State v. Smith, 250 Ariz. 69, ¶ 12 (2020)`; `Foster v. Ames, 5 Ariz. App. 116 (1967)`; `123 Ariz. 456, 601 P.2d 589 (1979)` | `az-cases-justia` → `az-opinions-supreme-azcourts` |
| Pacific Reporter with an Arizona parenthetical | `540 P.3d 912 (Ariz. 2024)`; `530 P.3d 1234 (Ariz. Ct. App. 2023)` | `az-cases-justia` → `az-opinions-supreme-azcourts` |
| Appellate docket numbers (Supreme Court and Court of Appeals) | `No. CV-24-0143-PR`; `CR-23-0236-PR`; `CV-24-0251-T/AP`; `1 CA-CV 24-0785`; `No. 2 CA-CV 2023-0108`; `1 CA-CV 25-1023 FC` | `az-opinions-supreme-azcourts` → `az-cases-justia` → `az-dockets-appellate` |
| Memorandum decisions / Westlaw cites with Arizona parenthetical | `Anguiano v. Kile, 1 CA-CV 26-0175, 2026 WL 1234567, at *2, ¶ 8 (Ariz. App. Oct. 15, 2026) (mem. decision)`; `2024 WL 2812345 (Ariz. Ct. App. June 3, 2024)`; `2025 Ariz. App. Unpub. LEXIS 123` | `az-cases-justia` |

Regexes (case-insensitive):

- Arizona Revised Statutes: `(?:A\.\s?R\.\s?S\.|\bARS|Ariz(?:ona)?\.?\s+Rev(?:ised)?\.?\s+Stat(?:utes)?\.?(?:\s+Ann\.?)?)\s*(?:(?:§+|sec(?:tion|\.)?)\s*)?(?P<title>\d{1,2})-(?P<section>\d{3,4}(?:\.\d{1,2})?)(?!\d)|(?:sec(?:tion|\.)|§)\s*(?P<title2>\d{1,2})-(?P<section2>\d{3,4}(?:\.\d{1,2})?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Arizona\s+Revised\s+Statutes`
- Arizona Constitution: `Ariz(?:ona)?\.?\s*Const(?:itution)?\.?\s*art(?:icle)?\.?\s*(?P<article>[IVXL]+|\d{1,2}(?:\.\d)?),?\s*(?:(?:pt\.|part)\s*(?P<part>\d|[IV]+),?\s*)?(?:§|sec(?:tion|\.)?)\s*(?P<section>\d{1,2}(?:\.\d)?)|Article\s+(?P<article2>[IVXL]+|\d{1,2}(?:\.\d)?),?\s+(?:Part\s+(?P<part2>\d|[IV]+),?\s+)?Section\s+(?P<section2>\d{1,2}(?:\.\d)?)\s+of\s+the\s+Arizona\s+Constitution`
- Arizona Rules of Civil Procedure: `Ariz\.\s*R\.\s*Civ\.\s*P\.\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Arizona\s+Rules\s+of\s+Civil\s+Procedure`
- Arizona Rules of Evidence: `Ariz\.\s*R\.\s*Evid\.\s*(?P<rule>\d{3,4})|Rule\s+(?P<rule2>\d{3,4})(?:\([a-z0-9]+\))*\s+of\s+the\s+Arizona\s+Rules\s+of\s+Evidence`
- Arizona Rules of Civil Appellate Procedure (ARCAP): `(?:ARCAP|Ariz\.\s*R\.\s*Civ\.\s*App\.\s*P\.)\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Arizona\s+Rules\s+of\s+Civil\s+Appellate\s+Procedure`
- Arizona Rules of Criminal Procedure: `Ariz\.\s*R\.\s*Crim\.\s*P\.\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Arizona\s+Rules\s+of\s+Criminal\s+Procedure`
- Rules of the Supreme Court of Arizona (incl. Rule 42 ERs, Rule 111): `Ariz\.\s*(?:R\.\s*Sup\.\s*Ct\.|Sup\.\s*Ct\.\s*R\.)\s*(?P<rule>\d+(?:\.\d+)?)(?:\([a-z0-9]+\))*(?:,?\s*ER\s*(?P<er>\d\.\d{1,2}))?|Rule\s+(?P<rule2>\d+)(?:,\s*ER\s*(?P<er2>\d\.\d{1,2}))?\s+of\s+the\s+Rules\s+of\s+the\s+(?:Arizona\s+)?Supreme\s+Court(?!\s+of\s+(?:the\s+)?(?!Arizona\b)[a-z])`
- Arizona Rules of Family Law Procedure: `(?:Ariz\.\s*R\.\s*Fam\.\s*Law\s*P\.|ARFLP)\s*(?P<rule>\d+(?:\.\d+)?)|Rule\s+(?P<rule2>\d+(?:\.\d+)?)(?:\([a-z0-9]+\))*\s+of\s+the\s+Arizona\s+Rules\s+of\s+Family\s+Law\s+Procedure`
- Arizona Administrative Code: `(?:A\.\s?A\.\s?C\.|Ariz(?:ona)?\.?\s*Admin(?:istrative)?\.?\s*Code)\s*(?:§\s*)?R(?P<title>\d{1,2})-(?P<chapter>\d{1,3})-(?P<section>\d{3,4}(?:\.\d{1,2})?)`
- Arizona Administrative Register: `(?P<volume>\d{1,2})\s+(?:A\.\s?A\.\s?R\.|Ariz\.\s*Admin\.\s*Reg\.)\s*(?P<page>\d{1,5})`
- Arizona Reports (Ariz.) and old Arizona Appeals Reports (Ariz. App.): `(?P<volume>\d{1,3})\s+Ariz\.(?:\s*(?P<app>App)\.)?\s+(?P<page>\d{1,4})(?:,\s*(?:¶+\s*\d+|\d+))*(?:,\s*\d{1,4}\s+P\.(?:\s*[23]d)?\s+\d{1,5})?(?:\s*\((?P<appct>App\.\s*)?(?P<year>\d{4})\))?`
- Pacific Reporter with an Arizona parenthetical: `(?P<volume>\d{1,4})\s+P\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>Ariz\.(?:\s*(?:Ct\.\s*)?App\.)?)\s*(?P<year>\d{4})\)`
- Appellate docket numbers (Supreme Court and Court of Appeals): `\b(?P<type>CV|CR|SB|JC|WC|TX)-(?P<yy>\d{2})-(?P<num>\d{4})-(?P<sub>[A-Z]{1,4}(?:/[A-Z]{1,2})?)\b|\b(?P<div>[12])\s*CA-(?P<ctype>CV|CR|SA|JV|MH|IC|UB|TX|CC)\s+(?P<cyear>\d{4}|\d{2})-(?P<cnum>\d{4})(?:\s+(?P<suffix>[A-Z]{2,4}))?`
- Memorandum decisions / Westlaw cites with Arizona parenthetical: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?(?:,\s*¶+\s*\d+)?\s*\(Ariz\.|Ariz\.\s*(?:App\.\s*(?:Unpub\.\s*)?)?LEXIS\s+(?P<lexis>\d+))`

Short forms → URL key:

A.R.S. → `ars`; ARS → `ars`; Ariz. Rev. Stat. → `ars`; Ariz. Rev. Stat. Ann. → `ars`; Arizona Revised Statutes → `ars`; A.A.C. → `aac`; Ariz. Admin. Code → `aac`; A.A.R. → `aar`; Ariz. Admin. Reg. → `aar`; ARCAP → `civ-app-p`; Ariz. R. Civ. App. P. → `civ-app-p`; Ariz. R. Civ. P. → `civ-p`; Ariz. R. Crim. P. → `crim-p`; Ariz. R. Evid. → `evid`; Ariz. R. Sup. Ct. → `sup-ct`; Ariz. Sup. Ct. R. → `sup-ct`; ER → `sup-ct-42`; Ariz. R. Fam. Law P. → `fam-law-p`; ARFLP → `fam-law-p`

Arizona has no public-domain citation; opinions use numbered paragraphs, and Arizona courts pinpoint by ¶ (e.g. '256 Ariz. 350, ¶ 12 (App. 2023)'), so a slip PDF gives a pinpoint without reporter pages. Arizona style puts Court of Appeals cites as '(App. YYYY)'; Bluebook uses '(Ariz. Ct. App. YYYY)'. 'Ariz. App.' is the closed Arizona Appeals Reports (1965-1976 era, per memory); later Court of Appeals opinions are in 'Ariz.'. Memorandum decisions: from memory, Ariz. R. Sup. Ct. 111(c) allows citing memorandum decisions issued on or after Jan. 1, 2015 for persuasive value, with the docket number, date and '(mem. decision)'; the Justia copies carry the legend 'THIS DECISION IS NOT PRECEDENTIAL AND MAY BE CITED ONLY AS AUTHORIZED BY RULE' (rule text itself not fetched; Westlaw is blocked). 'Petition for review denied' dispositions appear in the subsequent-history parenthetical ('review denied'). Routing guards: bare 'Rule 12(b)(6)', 'Rule 702', 'ER 1.7' and 'Rule 42' must not route here without an 'Ariz.' prefix or Arizona context ('ER' numbering is also used by other states' rules of professional conduct). 'A.R.S.' is unique to Arizona, but 'ARS' alone is a common acronym: route only when followed by a TT-SSS section number. Docket numbers 'CV-24-0143-PR' resemble other states' forms; route on them only with Arizona context; '1 CA-CV' / '2 CA-CR' are Arizona-specific. A '§§ 12-541 to -542' range is two sections: the regex takes the first. Statute URL keys: title unpadded (/ars/1/, /ars/12/); section zero-padded to 5 digits with '.' replaced by '-' (12-341.01 -> /ars/12/00341-01.htm). CourtListener ids from memory, unverified. Constitution Article 4 has parts ('art. IV, pt. 2, § 1'): the regex captures part; the azleg URL form for parts is unverified. Family Law Procedure rules ('Ariz. R. Fam. Law P.', 'ARFLP') route to the blocked Westlaw row.

## A. Statutes / code

### `az-ars-azleg` — Arizona Revised Statutes (Arizona Legislature)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Arizona State Legislature (Legislative Council) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All ARS titles; one HTML page per section.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.azleg.gov/ars/{title}/{section:05d}{-decimal}.htm`
  - Placeholders: title = integer, unpadded, including single-digit titles (/ars/1/, /ars/12/, /ars/41/; /ars/01/00213.htm is 404). section = the part after the hyphen, zero-padded to 5 digits; a decimal point becomes a hyphen and the decimal digits are kept as written: 12-542 -> /ars/12/00542.htm; 13-1105 -> /ars/13/01105.htm; 12-341.01 -> /ars/12/00341-01.htm; 41-1092.01 -> /ars/41/01092-01.htm. The bare .htm page is the section text only (no navigation); the wrapper https://www.azleg.gov/viewdocument/?docName=https://www.azleg.gov/ars/{title}/{section}.htm serves the same text with site chrome and the currency banner.
  - Index: `https://www.azleg.gov/arsDetail/?title={title}`
  - Navigation: Title index lists every chapter WITH section ranges ('Chapter 5 LIMITATIONS OF ACTIONS Sec: 12-501-12-559.03') and every section as a viewdocument link; not needed for URL construction.
- **Automation:** WebFetch gated · shell ok · robots: User-agent * — Crawl-delay: 120; disallows /search/, /xml/, /FormatDocument.asp, /FormatForPrint.asp, /DocumentsForBill.asp, WordPress paths; /ars/, /arsDetail/, /viewdocument/, /const/ allowed
  - Script (fetch_doc.py) is the primary route. WebFetch is gated: constructed /ars/ URLs need a permission approval and fail with PROVENANCE_REQUIRED; only URLs surfaced by a prior search/fetch (e.g. the viewdocument wrapper for 22-101 from the title-22 index) were fetched. Crawl-delay 120 s: plan one azleg request per citation.
- **Currency:** banner on arsDetail title index and viewdocument wrapper pages; not on bare /ars/ pages (use the Last-Modified header there) — observed: "updated to include the revised sections from the 57th Legislature, 2nd Regular Session"
- **Official status:** Title index page (https://www.azleg.gov/arsDetail/?title=12): 'The official version of the Arizona Revised Statutes is published by Thomson Reuters.' and the online version is 'primarily maintained for legislative drafting purposes'.
- **Hazard:** Crawl-delay 120 s on www.azleg.gov
- **Hazard:** text shows the version effective January 1 of the year after the latest session, so it can be ahead of the law in force mid-year
- **Hazard:** publisher disclaims official status (Thomson Reuters edition is official)
- **Hazard:** /xml/ is robots-disallowed: no permitted bulk route
- **Hazard:** WebFetch gated on constructed azleg URLs (PROVENANCE_REQUIRED) — use the script
- **Probe:** A.R.S. § 12-542 → `https://www.azleg.gov/ars/12/00542.htm` — expect: "Except as provided in section 12-551 there shall be commenced"
- **Evidence (2026-10-16):** fetch_doc.py: /ars/12/00542.htm 1,035 chars, 'Except as provided in section 12-551 there shall be commenced', Last-Modified 9 Sep 2026; /ars/13/01105.htm 'A. A person commits first degree murder if:'; /ars/12/00341-01.htm and /ars/41/01092-01.htm both body present. WebFetch: viewdocument wrapper for A.R.S. § 22-101 'A. The board of supervisors shall divide the county into', complete, with 57th Legislature currency banner. /ars/1/00213.htm body present; /ars/01/00213.htm 404. | Independent check 2026-10-16: fetch_doc.py /ars/28/00701-02.htm '28-701.02. Excessive speeds; classification A. A person shall not', Last-Modified 9 Sep 2026; second citation Arizona Revised Statutes § 28-701.02 ok
- **Notes:** Title index (arsDetail) is ~70-80K characters of text, within one WebFetch window.

### `az-ars-justia` — Justia — Arizona Revised Statutes (2025)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** ARS editions 2005-2025 (year listing pages 2017-2025 seen); the unversioned URL serves 2025.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/arizona/title-{title}/section-{title}-{section}/`
  - Placeholders: No chapter or article segment. section verbatim with '.' replaced by '-': 12-559.03 -> /title-12/section-12-559-03/; 13-751 -> /title-13/section-13-751/. Year-specific: insert /{year}/ after /arizona/ (e.g. /codes/arizona/2021/title-13/section-13-751/). Old 2005 edition uses a different form (/codes/arizona/2005/title12/00542.html).
  - Index: `https://law.justia.com/codes/arizona/title-{title}/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: law.justia.com answers robots.txt with a Cloudflare challenge (fetch_doc.py refusal recorded 2026-10-16)
  - WebFetch only.
- **Currency:** page heading and Universal Citation line — observed: "2025 Arizona Revised Statutes; 'AZ Rev Stat § 12-559.03 (2025)'"
- **Official status:** Third-party compilation; pages labelled '2025 Arizona Revised Statutes'; title page has no currency disclaimer.
- **Hazard:** edition lags official compilation (2025 edition while azleg shows 57th Leg. 2nd Reg. Sess. 2026)
- **Hazard:** shell blocked by Cloudflare
- **Hazard:** title index lists sections only (no chapter links or section ranges)
- **Probe:** A.R.S. § 12-559.03 → `https://law.justia.com/codes/arizona/title-12/section-12-559-03/` — expect: "A. Except as provided in subsections B, C and D"
- **Evidence (2026-10-16):** WebFetch: body present 'A. Except as provided in subsections B, C and D'; '2025 Arizona Revised Statutes'. Second: /title-13/section-13-751/ 'A. If the state has filed a notice of intent'. 2005 edition /2005/title12/00542.html body present. | Independent check 2026-10-16: 'A. Except as provided in subsections B, C and D'; '2025 Arizona Revised Statutes'; second citation A.R.S. § 33-1321 ok
- **Notes:** public.law and Cornell LII do not host the ARS (not separately probed; see absent).

## B. Constitution

### `az-constitution-azleg` — Arizona Constitution (Arizona Legislature)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Arizona State Legislature · text: **fetch-and-quote** · official: unknown
- **Coverage:** Constitution of 1912 as amended; one HTML page per section; articles 1-30 (articles 23-24 absent from the index; 6.1 present).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.azleg.gov/const/{article}/{section}.htm`
  - Placeholders: article = Arabic number (convert Roman: II -> 2, VI -> 6); section = Arabic; a decimal section uses an underscore (Art. 2 § 2.1 -> /const/2/2_1.htm). Article 6.1 folder name not verified. Wrapper with currency banner: https://www.azleg.gov/viewDocument/?docName=https://www.azleg.gov/const/{article}/{section}.htm. Article listing: https://www.azleg.gov/constitution/?article={article}. Article 4 is divided into Part 1 and Part 2 (cited 'art. IV, pt. 2, § 1'); the folder/file naming for parts is NOT verified — take the link from https://www.azleg.gov/constitution/?article=4.
  - Index: `https://www.azleg.gov/Constitution/`
  - Navigation: Index links constitution?article=N; each article page lists viewDocument links per section.
- **Automation:** WebFetch gated · shell ok · robots: see az-ars-azleg (Crawl-delay 120)
  - Script is the primary route. WebFetch gated on constructed azleg URLs (PROVENANCE_REQUIRED).
- **Currency:** constitution index page banner — observed: "updated to include the revised sections from the 55th Legislature, 1st Regular Session"
- **Official status:** No official/unofficial statement on the constitution index; the site disclaims official status for the ARS only.
- **Hazard:** stale currency banner (refers to 2021 session, next update 'January 2022') — check later amendments
- **Hazard:** Crawl-delay 120 s
- **Hazard:** '.p.htm' style URLs 404 (/const/2/4.p.htm)
- **Hazard:** bare section pages carry old Last-Modified dates (2002) and the index banner is stale (55th Leg.) — no reliable currency signal
- **Hazard:** Article 4 part folder naming unverified
- **Probe:** Ariz. Const. art. 2, § 4 → `https://www.azleg.gov/const/2/4.htm` — expect: "No person shall be deprived of life, liberty, or property"
- **Evidence (2026-10-16):** fetch_doc.py: /const/2/4.htm 'Section 4. No person shall be deprived of life, liberty, or' (136 chars); /const/6/14.htm 'The superior court shall have original jurisdiction'; /const/2/2_1.htm 'Victims' bill of rights' body present. | Independent check 2026-10-16: fetch_doc.py /const/2/8.htm 'Section 8. No person shall be disturbed in his private affairs'; second citation Ariz. Const. art. 2, § 8 ok

## C. Court rules

### `az-rules-amendments-azcourts` — Arizona Supreme Court rule-amendment orders and pending petitions

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Arizona Supreme Court · text: **link-only** · official: official
- **Coverage:** Orders amending rules and pending rule petitions; not a consolidated rule text.
- **Access:** `index-anchored` · format pdf
  - Placeholders: Order PDFs under /Portals/0/20/{year} Rules/…; ids not derivable.
  - Index: `https://www.azcourts.gov/rules/Recent-Amendments`
  - Navigation: azcourts.gov/rules -> Recent Amendments -> order PDF
- **Automation:** WebFetch gated · shell ok · robots: www.azcourts.gov: disallows /*/ctl/, /admin/, DNN system folders; /rules, /Portals allowed
  - Only the /rules landing page was fetched (links listed); individual orders not probed.
- **Currency:** none stated
- **Official status:** Signed court orders (e.g. 'Final Rules Order R-18-0002') posted on azcourts.gov/rules.
- **Hazard:** amendment orders only — not the rule as amended
- **Hazard:** www.azcourts.gov serves a Cloudflare challenge on some paths (/azrules/); one challenge switches the host off in fetch_doc.py for the day — request rule pages last
- **Probe:**  → `https://www.azcourts.gov/rules`
- **Evidence (2026-10-16):** fetch_doc.py read /rules: links to Recent-Amendments and a 2018 'Final Rules Order R-18-0002' PDF; no order opened. | Independent check 2026-10-16: not reachable — script host lock from the earlier /azrules/ challenge; WebFetch gated (not fresh evidence about this page)

### `az-rules-westlaw` — Arizona Court Rules (Westlaw government site)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Arizona Supreme Court via Thomson Reuters (govt.westlaw.com/azrules) · text: **link-only** · official: unknown
- **Coverage:** All statewide rule sets (Civ. P., Evid., ARCAP, Crim. P., Sup. Ct. incl. Rule 42 ERs, Fam. Law P., etc.), per memory.
- **Access:** `link-only` · format html
  - Index: `http://azrules.westgroup.com/`
  - Navigation: azcourts.gov/rules -> 'Court Rules' -> azrules.westgroup.com -> govt.westlaw.com/azrules
- **Automation:** WebFetch gated · shell blocked-challenge · robots: azrules.westgroup.com and govt.westlaw.com both answer robots.txt with a bot check
  - No Westlaw rules URL was surfaced by search, so WebFetch could not be attempted. www.azcourts.gov/azrules/Help returned HTTP 403 Cloudflare challenge to fetch_doc.py; WebFetch on it errored 'There was an error while fetching'.
- **Currency:** not reachable
- **Official status:** azcourts.gov 'Court Rules' menu link points to http://azrules.westgroup.com/; no statement could be read.
- **Hazard:** host refuses automated access
- **Hazard:** no tier-2 copy of Arizona rules on Justia, LII or public.law
- **Hazard:** the /azrules/ path on www.azcourts.gov triggers a Cloudflare challenge that makes fetch_doc.py mark ALL of www.azcourts.gov refused for the day — never request it from the script
- **Probe:** Ariz. R. Civ. P. 12(b)(6) → `http://azrules.westgroup.com/`
- **Evidence (2026-10-16):** fetch_doc.py: 'REFUSED: azrules.westgroup.com answers robots.txt with a bot check'; same for govt.westlaw.com.
- **Notes:** Rule text can be linked, never quoted, unless a future run finds an official PDF set.

## D. Administrative code

### `az-aac-sos` — Arizona Administrative Code (Secretary of State, chapter PDFs)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Arizona Secretary of State, Administrative Rules Division · text: **fetch-and-quote** · official: unknown
- **Coverage:** One file per chapter, Title_{TT}/{T}-{CC}.pdf (some chapters also as .rtf).
- **Access:** `constructible` · format pdf
  - Pattern: `https://apps.azsos.gov/public_services/Title_{title:02d}/{title}-{chapter:02d}.pdf`
  - Placeholders: From observed URLs: Title_17/17-09.pdf, Title_09/9-09.rtf, Title_09/9-03.rtf — folder title 2-digit padded, file title unpadded, chapter 2-digit padded. Section R9-10-101 lives in chapter file 9-10. Not verified on a live chapter (the 17-09 file is a recodified stub). UNPROVEN on a live chapter: independent check could not fetch 9-10.pdf (WebFetch gated, shell refused).
  - Index: `https://apps.azsos.gov/public_services/Title_{title:02d}/`
- **Automation:** WebFetch gated · shell blocked-challenge · robots: apps.azsos.gov and azsos.gov answer robots.txt with a bot check (fetch_doc.py REFUSED)
  - WebFetch read the previously surfaced 17-09 PDF but constructed chapter URLs (9-10.pdf) are gated (PROVENANCE_REQUIRED); shell refused by bot check. Long chapter PDFs will truncate in WebFetch.
- **Currency:** chapter file header ('Supp. YY-Q') — observed: "Supp. 14-3 (17-09, recodified stub)"
- **Official status:** Register contents page says 'The Register as published by the Division is the official version.'; no comparable statement seen for Code chapter files.
- **Hazard:** shell route refused by bot check
- **Hazard:** .rtf files unreadable by WebFetch
- **Hazard:** long chapter PDFs truncate in WebFetch
- **Hazard:** pattern seen only on a recodified stub chapter
- **Hazard:** chapter pattern unproven on a live chapter (9-10.pdf not reachable 2026-10-16)
- **Probe:** 17 A.A.C. 9 (recodified) → `https://apps.azsos.gov/public_services/Title_17/17-09.pdf` — expect: "This Chapter was recodified to 13 A.A.C. 13"
- **Evidence (2026-10-16):** WebFetch: 17-09.pdf header 'Supp. 14-3', editor's note 'recodified to 13 A.A.C. 13'; no section text. 9-09.rtf: '[binary data]'. Shell refused by bot check. | Independent check 2026-10-16: 17-09.pdf 'This Chapter was recodified to 13 A.A.C. 13', 'Supp. 14-3'; live chapter 9-10.pdf gated
- **Notes:** Needs a live-chapter probe (e.g. Title_09/9-10.pdf for R9-10-101) by a run that can WebFetch it.

### `az-aac-lii` — Cornell LII — Arizona Administrative Code

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-section pages for A.A.C. titles, including repealed/renumbered stubs.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/arizona/Ariz-Admin-Code-SS-R{title}-{chapter}-{section}`
  - Placeholders: Citation 'R9-10-101' -> Ariz-Admin-Code-SS-R9-10-101 (no padding). Browse: /regulations/arizona/title-{title}/chapter-{chapter}.
  - Index: `https://www.law.cornell.edu/regulations/arizona`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay: 10; /regulations allowed (per Delaware record)
  - Respect 10-second crawl delay.
- **Currency:** history note at foot of section — observed: "Last-Modified 30 Jul 2025; notes list amendments with 'Supp.' numbers"
- **Official status:** Third-party mirror; per-section history notes cite A.A.R. and Supp. numbers.
- **Hazard:** may lag the official Code (Last-Modified July 2025)
- **Hazard:** repealed/renumbered sections still have pages
- **Hazard:** history notes may stop at an older A.A.R. entry (R9-10-101 latest '28 A.A.R. 927, effective 4/15/2022' on 2026-10-16) — compare with the official chapter Supp. before quoting
- **Probe:** A.A.C. R9-10-101 → `https://www.law.cornell.edu/regulations/arizona/Ariz-Admin-Code-SS-R9-10-101` — expect: "In addition to the definitions in A.R.S. §§ 36-401(A) and 36-439"
- **Evidence (2026-10-16):** fetch_doc.py: 54,978 chars, 'In addition to the definitions in A.R.S. §§ 36-401(A) and 36-439'; history '8 A.A.R. 3559, effective August 1, 2002 (Supp. 02-3)'. Second: R4-23-110 'In addition to definitions in A.R.S. § 32-1901'. | Independent check 2026-10-16: WebFetch 'In addition to the definitions in A.R.S. §§ 36-401(A) and'; latest history '28 A.A.R. 927, effective 4/15/2022'; second citation Ariz. Admin. Code § R18-2-101 ok

## D. Administrative register

### `az-register-sos` — Arizona Administrative Register

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Arizona Secretary of State, Administrative Rules Division · text: **fetch-and-quote** · official: official
- **Coverage:** Weekly issues; yearly contents pages /register/{YYYY}/contents.htm (2009-2026 seen in search); 2026 = Volume 32.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://apps.azsos.gov/public_services/register/{YYYY}/{issue}/contents.pdf`
  - Placeholders: Volume = year - 1994 (2026 -> Vol. 32). The yearly contents page gives each issue number with its page range; pick the issue whose range contains the cited A.A.R. page. The 'contents.pdf' file holds the whole issue, not only the contents.
  - Index: `https://apps.azsos.gov/public_services/register/{YYYY}/contents.htm`
  - Navigation: yearly contents.htm -> issue whose page range covers the page -> {issue}/contents.pdf
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot check on robots.txt (fetch_doc.py REFUSED)
  - WebFetch truncated Issue 42 partway through p. 2560 of 2539-2634.
- **Currency:** 2026 contents page — observed: "Issue 42, Friday, October 16, 2026 (pp. 2539-2634)"
- **Official status:** 2026 contents page: 'The Register as published by the Division is the official version.'
- **Hazard:** WebFetch truncation of issue PDFs
- **Hazard:** shell refused
- **Hazard:** section headings (e.g. 'Participate in Rulemaking') are not on every issue — match the 'Volume NN, Issue NN' header instead
- **Probe:** 32 A.A.R. 2539 (Oct. 16, 2026) → `https://apps.azsos.gov/public_services/register/2026/42/contents.pdf` — expect: "Volume 32, Issue 42"
- **Evidence (2026-10-16):** WebFetch: 2026 contents.htm lists 'Volume 32', Issue 42 pp. 2539-2634; issue PDF: Information p. 2540, Participate in Rulemaking p. 2541, rulemaking notices from p. 2543; truncated in p. 2560. | Independent check 2026-10-16: 'Volume 32, Issue 42, October 16, 2026'; truncated in p. 2560; 2025 Issue 20 (pp. 1573-1620) read pp. 1574-1597 then truncated; second citation 31 A.A.R. 1574 (May 16, 2025) ok

## E. Case law

### `az-opinions-coa1-azcourts` — Court of Appeals Division One — Decisions (coa1.azcourts.gov)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Arizona Court of Appeals, Division One · text: **link-only** · official: unofficial
- **Coverage:** Opinions and memorandum decisions; search covers Division One and Supreme Court (app flags courts: Division1, Supreme).
- **Access:** `search-only` · format pdf
  - Placeholders: The Search Decisions page is an Elm app (Elm.Views.Opinions.Main) calling a DNN service ('Azcourts/Opinions': GetOpinions, GetDecisions, GetOpinionFiles) with ModuleId/TabId/anti-forgery headers; GET guesses at /API/Azcourts/Opinions/GetOpinions returned 404. Decision PDF URL form not found (guesses under /Portals/0/OpinionFiles/Div1/ and coa1 /Portals/1/ 404).
  - Index: `https://coa1.azcourts.gov/Decisions/SearchDecisions`
- **Automation:** WebFetch gated · shell ok · robots: same DNN robots as www.azcourts.gov; /Decisions allowed
  - Pages fetch (shell) but hold no decision rows. Use az-cases-justia for text.
- **Currency:** none
- **Official status:** Opinions page notes later proceedings 'may affect the legal status of any Opinion'; slip decisions.
- **Hazard:** JS-only search; token-protected API
- **Probe:** Fuller v. Scottsdale, 1 CA-CV 24-0785 (Ariz. App. Jan. 15, 2026) (mem. decision) → `https://coa1.azcourts.gov/Decisions/SearchDecisions`
- **Evidence (2026-10-16):** fetch_doc.py: page 295,958 bytes, app container only, no PDF links; Opinions page text explains posting, no rows. | Independent check 2026-10-16: fetch_doc.py 36,904 chars of page text, 0 '.pdf' matches (app shell)

### `az-opinions-coa2` — Court of Appeals Division Two — decisions (appeals2.az.gov)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Arizona Court of Appeals, Division Two · text: **link-only** · official: unknown
- **Coverage:** Recent decisions listing at /odsplus/recentdecisions.cfm (linked from azcourts.gov opinions search page).
- **Access:** `index-anchored` · format pdf
  - Index: `http://www.appeals2.az.gov/odsplus/recentdecisions.cfm`
- **Automation:** WebFetch gated · shell http-error · robots: unreachable: robots.txt returns an HTML error page, so fetch_doc.py treats the host as disallowed
  - WebFetch permission for the listing was not granted in this session.
- **Currency:** unknown
- **Official status:** Not reached.
- **Hazard:** robots.txt unreachable
- **Hazard:** http (not https) links
- **Hazard:** robots.txt unreachable (HTML error page) — script treats the host as disallowed; use az-cases-justia for Division Two
- **Probe:**  → `http://www.appeals2.az.gov/odsplus/recentdecisions.cfm`
- **Evidence (2026-10-16):** fetch_doc.py: 'robots.txt on www.appeals2.az.gov unreachable after a retry' (HTML error page). | Independent check 2026-10-16: robots.txt still unreachable; WebFetch gated
- **Notes:** Justia carries Division Two memorandum decisions (2 CA-CR 2026-0161-PR seen).

### `az-opinions-supreme-azcourts` — Arizona Supreme Court opinions (azcourts.gov OpinionFiles)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Arizona Supreme Court · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Opinions page offers 'Search By Year' 2002-2026.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.azcourts.gov/Portals/0/OpinionFiles/Supreme/{year}/{type}{yy}{num}{sub}.pdf`
  - Placeholders: From the docket number: 'CV-24-0143-PR' filed in 2025 -> /Supreme/2025/CV240143PR.pdf (hyphens removed; folder = year the opinion was FILED, not the docket year). Only one docket verified; sub-types with a slash (T/AP) unverified. The year listing https://www.azcourts.gov/Default.aspx?startDate={YYYY}-01-01&endDate={YYYY}-12-31&court=Supreme&TabId=9535 is a JavaScript (Elm) app whose rows come from a token-protected DNN API — fetch tools see no rows.
  - Index: `https://www.azcourts.gov/opinions`
- **Automation:** WebFetch gated · shell ok · robots: disallows /*/ctl/, /admin/, DNN system folders; /Portals allowed
  - Script is the primary route (read the PDF: 15 pp, 34,371 chars). WebFetch gated on constructed azcourts URLs (PROVENANCE_REQUIRED).
- **Currency:** none; Last-Modified header — observed: "Last-Modified Tue, 10 Jun 2025 (opinion filed Apr 29, 2025)"
- **Official status:** Slip opinions; the official reporter is Arizona Reports ('Ariz.'), not printed on the PDFs (Cravens PDF shows no reporter cite).
- **Hazard:** slip pagination; pinpoint by ¶ instead
- **Hazard:** amended opinions: the case page links a separate '…AmendedOpinion.PDF'; OpinionFiles copy may be replaced in place (Last-Modified after filing date)
- **Hazard:** year listings are a JS app
- **Hazard:** Cloudflare challenge on some azcourts.gov paths can lock the script out of the whole host for a day
- **Hazard:** www.azcourts.gov serves a Cloudflare challenge on some paths (/azrules/); one challenge switches the host off in fetch_doc.py for the day — request rule pages last
- **Hazard:** azcourts.gov intermittently serves a Cloudflare challenge; after one, the script refuses the whole host for ~24 h and built URLs are gated for WebFetch — fall back to Justia / CourtListener for text
- **Probe:** Cravens v. Montano, No. CV-24-0143-PR (Ariz. Apr. 29, 2025) → `https://www.azcourts.gov/Portals/0/OpinionFiles/Supreme/2025/CV240143PR.pdf` — expect: "We consider the meaning of the phrase “in connection with"
- **Evidence (2026-10-16):** fetch_doc.py: application/pdf 15 pp; caption 'No. CV-24-0143-PR Filed April 29, 2025'; '¶1 We consider the meaning of the phrase'; lists decision below 'No. 2 CA-CV 2023-0108'. Form '/2025/CV-24-0143-PR.pdf' -> 404. Second citation not probed (host lock). | Independent check 2026-10-16: not reproducible — script host lock from the research run's /azrules/ challenge (not fresh evidence); State v. Gordon CR240064PR.pdf and T/AP form untested | Independent re-check 2026-10-17: FAILED — script refused azcourts.gov (Cloudflare challenge seen 2026-10-16 23:04; the script keeps a challenged host off for ~24 h); WebFetch of built URLs gated, so no route that day.
- **Notes:** High-profile case pages (https://www.azcourts.gov/News-Info/{docket}) link briefs and amended opinions.

### `az-cases-justia` — Justia — Arizona case law

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court (year pages, e.g. 2024); Court of Appeals 1965-2026 split into division/published-unpublished collections; Territorial Supreme Court.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/arizona/{court-slug}/{year}/{docket-slug}.html`
  - Placeholders: Supreme: court-slug 'supreme-court'; docket lower-cased, '/' -> '-' (CV-23-0284-PR -> cv-23-0284-pr; CV-24-0251-T/AP -> cv-24-0251-t-ap). Court of Appeals memorandum decisions: 'court-of-appeals-division-one-unpublished' / 'court-of-appeals-division-two-unpublished'; docket lower-cased, spaces -> '-' (1 CA-CV 26-0175 -> 1-ca-cv-26-0175; '1 CA-CV 25-1023 FC' -> 1-ca-cv-25-1023-fc). Published Court of Appeals opinions: 'court-of-appeals-division-one-published' / 'court-of-appeals-division-two-published' (slugs seen in the /court-of-appeals/2026/ listing; no published page fetched yet). Per-collection year URLs (e.g. …/court-of-appeals-division-one-unpublished/2026/) return the same combined listing for all divisions; the combined listing is https://law.justia.com/cases/arizona/court-of-appeals/{year}/.
  - Index: `https://law.justia.com/cases/arizona/`
  - Navigation: year listing -> decision page (listing shows 500 of N per page)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - WebFetch only. Court of Appeals 2026 listing showed 'first 500 of 1,141'.
- **Currency:** none; newest listing entry dated Oct. 16, 2026
- **Official status:** Third-party; no reporter citation for the decision itself, no Universal Citation line.
- **Hazard:** no Ariz./P.3d pagination; pinpoint by ¶
- **Hazard:** year listing paginates (500 per page)
- **Hazard:** published vs unpublished collections use different slugs
- **Hazard:** per-collection year URLs return the combined Court of Appeals listing (both divisions, published and unpublished)
- **Probe:** City of Mesa v. Ryan, No. CV-23-0284-PR (Ariz. Oct. 17, 2024) → `https://law.justia.com/cases/arizona/supreme-court/2024/cv-23-0284-pr.html` — expect: "Under A.R.S. § 12-821.01(A), a person with a claim against"
- **Evidence (2026-10-16):** WebFetch: full opinion ¶1-¶22, '¶1 Under A.R.S. § 12-821.01(A), a person with a claim against'. Second: Anguiano v. Kile, 1 CA-CV 26-0175 (unpublished slug) full text through ¶19, legend 'THIS DECISION IS NOT PRECEDENTIAL AND MAY BE CITED ONLY AS AUTHORIZED BY RULE.' | Independent check 2026-10-16: '¶1 Under A.R.S. § 12-821.01(A), a person with a claim against'; complete through ¶22; State v. Gordon CR-24-0064-PR ¶1-¶60 complete; second citation Hartman v. Parrott, No. 1 CA-CV 26-0042 FC (Ariz. App. Oct. 15, 2026) (mem. decision) ok

## F. Subsequent history

### `az-dockets-appellate` — Arizona appellate case dockets (apps.azcourts.gov docket PDFs)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Arizona Supreme Court / Court of Appeals clerks · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court (ASC) and Division One (1CA) dockets with predecessor and descendant case numbers, decision type/date, disposition, proceeding entries. Only some dockets are present: open or recently active cases (CR-26-0026-PR, CV-26-0046-PR, 1 CA-CV 24-0785, 1 CA-CV 26-0175 found; closed CV-24-0143-PR and several 2025 dockets 404). Division Two dockets: 2CA guesses 404.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://apps.azcourts.gov/aacc/appella/{court}/{type}/{type}{yy}{num}.pdf`
  - Placeholders: court = ASC | 1CA. Supreme 'CV-26-0046-PR' -> ASC/CV/CV260046.PDF; Division One '1 CA-CV 24-0785' -> 1CA/CV/CV240785.pdf (sub-type suffix dropped). Search engines index these with backslashes (ASC\CV\…); forward slashes work. Extension case-insensitive on the server as observed (.PDF and .pdf both seen).
  - Index: `https://www.azcourts.gov/appellatecourtcases`
  - Navigation: Decision below's docket PDF -> 'D E S C E N D E N T C A S E (S)' line gives the Supreme Court PR number -> open that ASC docket for status/disposition; reverse via 'P R E D E C E S S O R'.
- **Automation:** WebFetch ok · shell ok · robots: none (404)
  - WebFetch also read a constructed docket URL in the independent check.
- **Currency:** docket footer — observed: "Case Docket as of 10-Aug-2026"
- **Official status:** Docket footer: information 'may not reflect all case activity and is subject to change without notice'.
- **Hazard:** docket PDFs disappear (404) for closed/older cases
- **Hazard:** Division Two dockets not found by this pattern
- **Hazard:** review dispositions of closed cases must then be found by party name (Justia / Supreme Court opinion or order)
- **Probe:** Fuller v. Scottsdale, 1 CA-CV 24-0785 -> ASC CV-26-0046-PR → `https://apps.azcourts.gov/aacc/appella/1CA/CV/CV240785.pdf` — expect: "ASC CV-26-0046-PR"
- **Evidence (2026-10-16):** fetch_doc.py and WebFetch (backslash URL from search): 'MEMORANDUM DECISION' 15-Jan-2026, descendant 'ASC CV-26-0046-PR', 'Case Docket as of 10-Aug-2026'; ASC/CV/CV260046.PDF status 'Pending'; ASC/CR/CR260026.PDF lists predecessor '1 CA-SA 25-0153'. | Independent check 2026-10-16: descendant 'ASC CV-26-0046-PR'; 'Case Docket as of 10-Aug-2026'; 1CA/CV/CV260042.pdf 3 pp 'CASE DECISION 15-Oct-2026 MEMORANDUM DECISION' (FC suffix dropped); second citation Hartman v. Parrott, 1 CA-CV 26-0042 FC ok
- **Notes:** The public case search (https://apps.azcourts.gov/publicaccess/ and the Party-Case / Lower Court Case Number indexes) is the human route; not probed.

## Not available (do not look for these again)

- **court_rules** — Any fetchable official or tier-2 text of Arizona court rules: Official text only on Westlaw govt site (bot check). Justia, LII and public.law host no Arizona rules (no results in searches; LII Arizona offering is the Admin Code). (2026-10-16)
- **case_law** — Public-domain (vendor-neutral) citation format: Opinions carry docket numbers and ¶ numbers only; Arizona cites to 'Ariz.' / P.3d or WL for memorandum decisions (Cravens slip PDF, Justia pages). (2026-10-16)
- **statutes** — Permitted bulk ARS download: azleg.gov robots.txt disallows /xml/; no other bulk route seen. (2026-10-16)
- **case_law** — Free official reporter (Ariz.) pagination: Slip PDFs and Justia copies show no Ariz. page numbers for the decision itself; Arizona pinpoints by ¶, which the slip text carries. (2026-10-16)

## Corpus candidates (maintainers)

- `az-register-sos` — Issue PDFs truncate in WebFetch (Issue 42 stopped in p. 2560 of 2539-2634) and the shell route is refused.
- `az-aac-sos` — Chapter PDFs (e.g. 9 A.A.C. 10, health care institutions) are long; the shell route is refused and WebFetch truncates around 100K characters. URL from the pattern, not fetched.

## Open questions

- Arizona Supreme Court OpinionFiles pattern verified on one docket only; a second docket (and T/AP sub-types) needs a probe on a day when www.azcourts.gov is not locked out in the script cache.
- Division One and Division Two decision PDF URL forms not found; the Division One DNN API endpoint path and headers not established.
- Westlaw azrules: WebFetch never attempted (no search-surfaced URL); confirm whether WebFetch can read it.
- A.A.C. chapter-PDF pattern seen only on a recodified stub (17-09) and .rtf files; probe a live chapter (9-10).
- Ariz. R. Sup. Ct. 111(c) memorandum-decision citation rule stated from memory; rule text unreachable.
- Constitution Article 6.1 folder name (/const/6.1/ vs /const/6_1/) unverified.
- CourtListener ids (ariz, arizctapp, ariztaxct) unverified.
- WebFetch in this session only fetched URLs surfaced by WebSearch/WebFetch; constructed azleg and azcourts URLs were refused for want of permission — WebFetch status of az-constitution-azleg and azcourts PDFs is untested.
- Re-check az-opinions-supreme-azcourts (CR240064PR.pdf, CV240220TAP.pdf) and az-rules-amendments-azcourts from a fresh day, before any /azrules/ request; consider whether a Cloudflare challenge on one azcourts.gov path should lock the whole host.
- A.A.C. chapter-PDF pattern unproven on a live chapter: needs a search-surfaced live-chapter URL (WebFetch) since the shell is refused.
- Constitution Article 4 parts: azleg folder/file naming for 'art. IV, pt. 2' unverified.
- Justia published Court of Appeals slugs (court-of-appeals-division-one-published / -division-two-published) seen in a listing only; fetch one published page.
- az-opinions-supreme-azcourts: downgraded to reported 2026-10-17 after an intermittent Cloudflare challenge left no route; re-probe once the script's host lock expires and restore to verified if the probe passes.
