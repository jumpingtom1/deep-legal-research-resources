# Tennessee (TN) — free legal sources

_Generated from `data/tn.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Tennessee's official hosts are largely closed to tools: tncourts.gov (all court rules, opinions, Rule 11 lists) serves a browser-validation challenge to both the script and WebFetch, and capitol.tn.gov (General Assembly, constitution PDF) disallows all robots. The official T.C.A. is a LexisNexis JavaScript app, so statutes, constitution and case law fall to Justia (tier 2, WebFetch only; built URLs work). Administrative rules are readable: official SOS chapter PDFs by WebFetch (script refused by a CloudFront 403) and Cornell LII by script. Court rules and Rule 11 dispositions have no free tool-readable source.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Tennessee Supreme Court | `tenn (unverified)` | Tenn. | S.W.3d, S.W.2d, S.W., Tenn. | — |
| Tennessee Court of Appeals | `tennctapp (unverified)` | Tenn. Ct. App. | S.W.3d, S.W.2d, Tenn. App. | — |
| Tennessee Court of Criminal Appeals | `tenncrimapp (unverified)` | Tenn. Crim. App. | S.W.3d, S.W.2d, Tenn. Crim. App. | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Tennessee Code Annotated | `Tenn. Code Ann. § 28-3-104`; `T.C.A. § 28-3-104`; `TCA § 39-17-1307(a)`; `Tenn. Code Ann. §§ 29-20-201 to -205`; `Tennessee Code Annotated section 28-3-104(a)(1)`; `section 28-3-104 of the Tennessee Code Annotated`; `T.C.A. §§ 4-5-208, 71-5-105` | `tn-code-justia` → `tn-code-lexis` |
| Tennessee Public Acts (public chapters) | `2012 Tenn. Pub. Acts ch. 582`; `2022 Tenn. Pub. Acts, c. 1119`; `Public Chapter 1119 of 2022`; `Tenn. Pub. Ch. 582 (2012)` | `tn-public-acts-sos` |
| Tennessee Constitution | `Tenn. Const. art. I, § 8`; `Tenn. Const. art. II, sec. 24`; `Article I, section 8 of the Tennessee Constitution`; `Tennessee Constitution, Article XI, Section 16`; `Article I, Section 9 of the Constitution of Tennessee` | `tn-constitution-justia` → `tn-constitution-capitol` |
| Tennessee Rules of Civil/Criminal/Appellate Procedure and Evidence | `Tenn. R. Civ. P. 12.02(6)`; `Tenn. R. Evid. 702`; `Tenn. R. App. P. 11`; `Tenn. R. Crim. P. 11(c)`; `Rule 12.02(6) of the Tennessee Rules of Civil Procedure`; `Tennessee Rule of Evidence 702`; `Tennessee Rule of Appellate Procedure 3(e)`; `Tenn. R. Juv. Prac. & P. 1` | `tn-rules-tncourts` |
| Tennessee Supreme Court Rules (incl. Rule 8 RPC) and Court of Appeals / Court of Criminal Appeals Rules | `Tenn. Sup. Ct. R. 8, RPC 1.7`; `Tenn. Sup. Ct. R. 13`; `Tennessee Supreme Court Rule 4(G)(1)`; `Rule 4 of the Rules of the Supreme Court of Tennessee`; `Tenn. Ct. App. R. 10`; `Tenn. Ct. Crim. App. R. 20`; `Tenn. R. Prof'l Conduct 3.3` | `tn-rules-tncourts` |
| Tennessee court rules (bare forms) *(only once this jurisdiction is known)* | `Rule 12.02(6)`; `RPC 1.7`; `Rule 11 application` | `tn-rules-tncourts` |
| Rules and Regulations of the State of Tennessee | `Tenn. Comp. R. & Regs. 1200-08-01-.01`; `Tenn. Comp. R. & Regs. r. 0720-14-.01`; `Tenn. Comp. R. & Regs. ch. 1200-13-19`; `Rule 1200-13-19-.01`; `Tenn. R. & Regs. 0400-30-39-.02` | `tn-admincode-sos` → `tn-admincode-lii` |
| Tennessee appellate docket numbers | `No. M2022-01820-SC-R11-SV`; `W2021-00999-SC-R11-CV`; `E2024-00871-COA-R3-PT`; `No. W2023-00123-CCA-R3-CD`; `M2019-01234-SC-R3-WC` | `tn-cases-justia` → `tn-opinions-tncourts` |
| Tennessee court parentheticals and reporters | `123 S.W.3d 456 (Tenn. 2003)`; `2020 WL 1234567, at *3 (Tenn. Ct. App. Mar. 3, 2020)`; `(Tenn. Crim. App. 2015)`; `225 Tenn. 1`; `45 Tenn. App. 300`; `(Tenn. Workers' Comp. Panel 2018)` | `tn-cases-justia` → `tn-opinions-tncourts` |
| South Western Reporter (regional, generic) *(only once this jurisdiction is known)* | `123 S.W.3d 456`; `700 S.W.3d 12` | `tn-cases-justia` |
| Tennessee Rule 11 permission-to-appeal history | `perm. app. denied (Tenn. 2023)`; `perm. app. denied (Tenn. Jan. 12, 2024)`; `perm. app. granted (Tenn. Aug. 9, 2023)`; `no perm. app. filed` | `tn-rule11-tncourts` |

Regexes (case-insensitive):

- Tennessee Code Annotated: `(?:Tenn(?:essee|\.)\s*Code\s*Ann(?:otated|\.)?|\bT\.?\s*C\.?\s*A\.?)\s*(?:§§?|sec(?:tion|s?\.)s?)?\s*(?P<title>\d{1,2})-(?P<chapter>\d{1,3})-(?P<section>\d{3,4}(?:\.\d+)?)(?![\d-])|(?:sec(?:tion|\.)|§)\s*(?P<title2>\d{1,2})-(?P<chapter2>\d{1,3})-(?P<section2>\d{3,4}(?:\.\d+)?)(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+(?:Tennessee\s+Code|T\.?C\.?A\b)`
- Tennessee Public Acts (public chapters): `(?P<year>(?:18|19|20)\d\d)\s+Tenn\.\s*Pub\.\s*Acts,?\s*(?:ch\.|c\.|chapter)\s*(?P<chapter>\d+)|Public\s+Chapter\s+(?:No\.\s*)?(?P<chapter2>\d+)\s+of\s+(?:the\s+Acts\s+of\s+)?(?P<year2>(?:19|20)\d\d)|Tenn\.\s*Pub\.\s*Ch\.\s*(?P<chapter3>\d+)\s*\((?P<year3>(?:19|20)\d\d)\)`
- Tennessee Constitution: `Tenn\.\s*Const\.,?\s*art\.?\s*(?P<article>[IVXL]+),?\s*(?:§|sec\.?|section)\s*(?P<section>\d+)|Article\s+(?P<article2>[IVXL]+),?\s*Section\s+(?P<section2>\d+)\s+of\s+the\s+(?:Tennessee\s+Constitution|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Tennessee)|Tennessee\s+Constitution,?\s*Article\s+(?P<article3>[IVXL]+),?\s*Section\s+(?P<section3>\d+)`
- Tennessee Rules of Civil/Criminal/Appellate Procedure and Evidence: `Tenn\.\s*R\.\s*(?P<set>Civ\.\s*P|Evid|App\.\s*P|Crim\.\s*P|Juv\.\s*(?:Prac\.\s*&\s*)?P)\.?\s*(?P<rule>\d{1,3}(?:\.\d+)?)|Tennessee\s+Rules?\s+of\s+(?P<set2>Civil\s+Procedure|Evidence|Appellate\s+Procedure|Criminal\s+Procedure)\s*(?P<rule2>\d{1,3}(?:\.\d+)?)|Rule\s+(?P<rule3>\d{1,3}(?:\.\d+)?)(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+Tennessee\s+Rules\s+of\s+(?P<set3>Civil\s+Procedure|Evidence|Appellate\s+Procedure|Criminal\s+Procedure)`
- Tennessee Supreme Court Rules (incl. Rule 8 RPC) and Court of Appeals / Court of Criminal Appeals Rules: `Tenn\.\s*Sup\.\s*Ct\.\s*R\.\s*(?P<rule>\d{1,3}(?:\.\d+)?)(?:,\s*RPC\s*(?P<rpc>\d\.\d+))?|Tennessee\s+Supreme\s+Court\s+Rule\s*(?P<rule2>\d{1,3})|Rule\s+(?P<rule3>\d{1,3})(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+Rules\s+of\s+the\s+(?:Tennessee\s+Supreme\s+Court|Supreme\s+Court\s+of\s+Tennessee)|Tenn\.\s*Ct\.\s*(?P<court>App|Crim\.\s*App)\.\s*R\.\s*(?P<rule4>\d{1,2})|Tenn\.\s*R\.\s*Prof'?l\s*Conduct\s*(?P<rpc2>\d\.\d+)`
- Tennessee court rules (bare forms): `\bRule\s+(?P<rule>\d{1,2}\.\d{2})(?:\s*\([a-zA-Z0-9]+\))*|\bRPC\s+(?P<rpc>\d\.\d+)|\bRule\s+11\s+application`
- Rules and Regulations of the State of Tennessee: `Tenn\.\s*(?:Comp\.\s*)?R\.\s*&\s*Regs\.?\s*(?:r\.|ch\.|rule)?\s*(?P<rule>\d{4}-\d{2}(?:-\d{2})?(?:-\.\d{2})?)|\bRule\s+(?P<rule2>\d{4}-\d{2}(?:-\d{2})?-\.\d{2})`
- Tennessee appellate docket numbers: `\b(?P<docket>[EMW](?P<year>(?:19|20)\d\d)-\d{5}-(?P<court>SC|COA|CCA|WC)(?:-[A-Z0-9]{1,4}){1,3})\b`
- Tennessee court parentheticals and reporters: `\((?P<court>Tenn\.(?:\s*(?:Ct\.\s*App|Crim\.\s*App|Workers'?\s*Comp\.\s*Panel)\.?)?)\s*(?:[A-Z][a-z]{2,4}\.?\s*\d{1,2},\s*)?(?P<year>(?:18|19|20)\d\d)\)|\b(?P<vol>\d{1,3})\s+Tenn\.(?:\s*(?:App|Crim\.\s*App)\.)?\s+(?P<page>\d{1,4})\b`
- South Western Reporter (regional, generic): `\b(?P<vol>\d{1,4})\s+S\.\s*W\.\s*(?:2d|3d)?\s+(?P<page>\d{1,5})\b`
- Tennessee Rule 11 permission-to-appeal history: `(?P<disp>(?:no\s+)?perm\.\s*app\.\s*(?:denied|granted|dismissed|filed))(?:\s*\(Tenn\.\s*(?:[A-Z][a-z]{2,4}\.?\s*\d{1,2},\s*)?(?P<year>(?:19|20)\d\d)\))?`

No law_aliases needed: T.C.A. cites are title-chapter-section and the Justia URL is built from the numbers (part = section // 100). 'T.C.A.'/'TCA' and 'Tenn. Code Ann.' are Tennessee markers; bare '§ 28-3-104' routes here only with 'of the Tennessee Code'. Ranges ('§§ 29-20-201 to -205') capture only the first section. Bare 'Rule 12.02(6)', 'RPC 1.7' and regional S.W. cites are context_required. Docket numbers [EMW]YYYY-NNNNN-(SC|COA|CCA|WC)-… are uniquely Tennessee. Unpublished opinions are cited by docket + WL with a '(Tenn. Ct. App. date)' parenthetical and Rule 11 history ('perm. app. denied'). No public-domain citation format. Special Workers' Compensation Appeals Panel opinions are on Justia under workers-compensation; CourtListener id for that panel not known.

## A. Statutes / code

### `tn-code-lexis` — Tennessee Code Annotated (free public access, LexisNexis)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · State of Tennessee (Tennessee Code Commission) / LexisNexis · text: **link-only** · official: official
- **Coverage:** Entire Tennessee Code Annotated, on the Lexis Advance free-access container.
- **Access:** `link-only` · format html
  - Placeholders: No per-section URL; the free container is navigated interactively.
  - Index: `https://www.lexisnexis.com/hottopics/tncode/`
  - Navigation: Human only: hottopics/tncode/ 302-redirects to advance.lexis.com/container?config=014CJAA5ZGVhZjA3NS02MmMzLTRlZWQtOGJjNC00YzQ1MmZlNzc2YWYKAFBvZENhdGFsb2e9zYpNUjTRaIWVfyrur9ud → TOC → title → chapter → part → section. No text reachable by either tool.
- **Automation:** WebFetch fail · shell http-error · robots: script robots check passed (advance.lexis.com permits)
  - WebFetch: 302 to the container, then empty content (JavaScript app). fetch_doc.py: kind=html chars=0.
- **Currency:** none observed (app did not render)
- **Official status:** The T.C.A. is published by LexisNexis under contract with the Tennessee Code Commission; state pages (www.tn.gov Commerce fireworks laws page; LII state page) send readers to lexisnexis.com/hottopics/tncode/ for the Code. No online authentication statement seen (app did not render).
- **Hazard:** JavaScript-only app
- **Hazard:** no per-section URLs
- **Hazard:** terms of use restrict automated access
- **Probe:** T.C.A. (container) → `https://www.lexisnexis.com/hottopics/tncode/`
- **Evidence (2026-10-17):** Link found on www.tn.gov laws page (script links). WebFetch: 302 → advance.lexis.com container, page content empty. Script: kind=html chars=0.
- **Notes:** The General Assembly site (capitol.tn.gov) is robots-blocked, so no government-hosted, tool-readable T.C.A. text exists. Public.Resource.Org's copy (law.resource.org) is not a vetted source and is not allowed.

### `tn-legislature-capitol` — Tennessee General Assembly website (bills, legislation, documents)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Tennessee General Assembly · text: **link-only** · official: unknown
- **Coverage:** Bills and legislative history; links to Lexis for the Code.
- **Access:** `link-only` · format html
  - Index: `https://www.capitol.tn.gov/`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.capitol.tn.gov and wapp.capitol.tn.gov: 'User-agent: *  Disallow: /' (Allow only for named search-engine bots)
  - Blocked for every route per policy.
- **Currency:** 
- **Hazard:** robots disallow all
- **Probe:**  → `https://www.capitol.tn.gov/`
- **Evidence (2026-10-17):** Script: REFUSED robots.txt on www.capitol.tn.gov disallows / (rule: Disallow: /); same on wapp.capitol.tn.gov.

### `tn-public-acts-sos` — Public Acts (Public Chapters) of Tennessee

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Tennessee Secretary of State, Division of Publications · text: **fetch-and-quote** · official: official
- **Coverage:** Public chapters by General Assembly; seen for the 107th GA (2011-2012). Older acts as HTM on sharetngov.tnsosfiles.com/sos/acts/{GA}/pub/PUBC{NNNN}.htm (search result, not fetched).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://publications.tnsosfiles.com/acts/{ga}/pub/pc{chapter4}.pdf`
  - Placeholders: ga = General Assembly number = (year - 1797) // 2 (2012 → 107, 2022 → 112, 2024 → 113); chapter4 = public chapter number zero-padded to 4 digits (582 → 0582). Verified on one citation only.
  - Index: `https://sos.tn.gov/node/730`
  - Navigation: Index page (Public Acts | Private Acts | Indexes) reported from search, not fetched.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: robots.txt returns a CloudFront 403 'Request blocked' page; script refuses
  - Scanned/OCR'd PDF: OCR garbles names and dates in places; bill contents may be an attachment.
- **Currency:** n/a (enrolled act)
- **Official status:** Enrolled public chapters as signed, published by the Secretary of State (signature blocks present in the PDF).
- **Hazard:** OCR errors
- **Hazard:** script route refused (CloudFront 403)
- **Probe:** 2012 Tenn. Pub. Acts ch. 582 → `https://publications.tnsosfiles.com/acts/107/pub/pc0582.pdf` — expect: "PUBLIC CHAPTER NO. 582 SENATE BILL NO. 2183"
- **Evidence (2026-10-17):** WebFetch: starts "~tate of ~ennessee PUBLIC CHAPTER NO. 582 SENATE BILL NO. 2183"; signature blocks present; OCR garbled in places.
- **Notes:** URL taken from a search result; the constructible rule is inferred from the path and verified on this one chapter.

### `tn-code-justia` — Tennessee Code (Justia)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Current edition labelled '2025 Tennessee Code'; prior editions under /codes/tennessee/{year}/ (2010, 2014, 2017-2019, 2021, 2023 seen in search results).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/tennessee/title-{title}/chapter-{chapter}/part-{part}/section-{title}-{chapter}-{section}/`
  - Placeholders: From T.C.A. § T-C-S: title = T, chapter = C, section number S as cited; part = integer part of S divided by 100 (104 → 1, 205 → 2, 1307 → 13). For a §§ range use the first section. Year-specific editions: insert /{year}/ after /tennessee/.
  - Index: `https://law.justia.com/codes/tennessee/`
  - Navigation: Fallback: title-{T}/chapter-{C}/ lists parts by name only (no section ranges) → part page → section.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: script: law.justia.com answers robots.txt with a bot check
  - Built section URLs went through WebFetch without a permission prompt in this session. Script route refused.
- **Currency:** page heading and title — observed: "2025 Tennessee Code; Tennessee Code Title 28, Chapter 3 (2025)"
- **Official status:** Justia pages say 'These codes may not be the most recent version' and 'Please check official sources.'
- **Hazard:** edition lags the current T.C.A. by up to a year
- **Hazard:** part index pages show no section ranges
- **Probe:** Tenn. Code Ann. § 28-3-104 → `https://law.justia.com/codes/tennessee/title-28/chapter-3/part-1/section-28-3-104/` — expect: "(a) (1) Except as provided in subdivision (a)(2), the following"
- **Evidence (2026-10-17):** WebFetch § 28-3-104: body present, starts "(a) (1) Except as provided in subdivision (a)(2), the following", not truncated. Second built URL § 39-17-1307 (part-13): body starts "A person commits an offense who carries, with the intent"; heading year 2025.

## B. Constitution

### `tn-constitution-capitol` — Constitution of the State of Tennessee (General Assembly PDF)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Tennessee General Assembly · text: **link-only** · official: unknown
- **Coverage:** Current constitution as amended (PDF).
- **Access:** `link-only` · format pdf
  - Index: `http://www.capitol.tn.gov/about/docs/TN-Constitution.pdf`
  - Navigation: Linked from law.cornell.edu/states/tennessee.
- **Automation:** WebFetch blocked · shell blocked-robots · robots: Disallow: / for User-agent: *
  - Not fetched by any route.
- **Currency:** 
- **Hazard:** robots disallow all
- **Probe:** Tenn. Const. → `http://www.capitol.tn.gov/about/docs/TN-Constitution.pdf`
- **Evidence (2026-10-17):** Script check: REFUSED robots.txt on www.capitol.tn.gov disallows /about/docs/TN-Constitution.pdf (rule: Disallow: /).
- **Notes:** sos.tn.gov/node/1487 ('Tennessee State Constitution') is a TSLA history page on the 1796 constitution, not the current text.

### `tn-constitution-justia` — Tennessee Constitution (Justia)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Current constitution, one page per section.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/tennessee/article-{article}/section-{section}/`
  - Placeholders: article = Roman numeral in lower case (I → i, XI → xi); section = Arabic number.
  - Index: `https://law.justia.com/constitution/tennessee/`
  - Navigation: Article page lists section links only (no text).
- **Automation:** WebFetch ok · shell blocked-challenge · robots: script: law.justia.com answers robots.txt with a bot check
- **Currency:** none stated (footer copyright only) — observed: "This Constitution may not be the most recent version."
- **Official status:** Page disclaimer: 'This Constitution may not be the most recent version.'
- **Hazard:** no amendment date stated
- **Probe:** Tenn. Const. art. I, § 8 → `https://law.justia.com/constitution/tennessee/article-i/section-8/` — expect: "That no man shall be taken or imprisoned, or disseized"
- **Evidence (2026-10-17):** WebFetch art. I § 8: body starts "That no man shall be taken or imprisoned, or disseized". Built art. II § 24: starts "No public money shall be expended except pursuant to appropriations".

## C. Court rules

### `tn-rules-tncourts` — Tennessee court rules (Tenn. R. Civ. P., Evid., App. P., Crim. P., Sup. Ct. R. incl. Rule 8 RPC, Ct. App. R., Ct. Crim. App. R.)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Tennessee Administrative Office of the Courts · text: **link-only** · official: unknown
- **Coverage:** Per-rule HTML pages (e.g. /rules/rules-civil-procedure/1202) and amendment orders as PDFs.
- **Access:** `link-only` · format html
  - Placeholders: Per-rule slugs seen in memory/search (rules-civil-procedure/1202 = Rule 12.02) but unverifiable: host challenged.
  - Index: `http://www.tncourts.gov/courts/rules`
- **Automation:** WebFetch blocked · shell blocked-challenge · robots: robots.txt itself answers with the JavaScript browser-validation page (no parseable rules)
  - Every www.tncourts.gov / tncourts.gov URL tried (rule page, opinions page, node page, PDF under /sites/default/files/) returns a 138-character 'Please wait while we validate your browser' JavaScript challenge, to the script and to WebFetch alike. Host treated as bot-walled for both routes on 2026-10-17.
- **Currency:** 
- **Hazard:** bot challenge on every URL
- **Probe:** Tenn. R. Civ. P. 12.02 → `https://www.tncourts.gov/rules/rules-civil-procedure/1202`
- **Evidence (2026-10-17):** Script: kind=html chars=138 "Please wait while we validate your browser". WebFetch tncourts.gov/node/3216: CHALLENGE.
- **Notes:** No tier-2 copy: Justia and LII do not host Tennessee court rules (LII links out to tncourts.gov). Rules are also printed in the T.C.A. court-rules volumes on Lexis (link-only).

## D. Administrative code

### `tn-admincode-sos` — Rules and Regulations of the State of Tennessee (official compilation, chapter PDFs)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Tennessee Secretary of State, Division of Publications · text: **fetch-and-quote** · official: official
- **Coverage:** All effective rules, one PDF per chapter, by agency number (0020 Accountancy …).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Chapter PDFs are publications.tnsosfiles.com/rules/{agency}/{agency-division}/{chapter}.{YYYYMMDD}.pdf; the date suffix is the edition date and is NOT constructible. Agency index pages are publications.tnsosfiles.com/rules/{agency}/{agency}.htm (seen for 1330).
  - Index: `https://sos.tn.gov/rules-and-regulations`
  - Navigation: sos.tn.gov/rules-and-regulations (agency list, 4-digit numbers) → agency page publications.tnsosfiles.com/rules/{agency}/{agency}.htm → chapter PDF link. WebFetch does not expose the hrefs on these index pages; take PDF URLs from a search result or the rendered page.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: sos.tn.gov and publications.tnsosfiles.com: robots.txt returns CloudFront 403 'Request blocked'
  - WebFetch reads pages and PDFs; a built agency-index URL (0720/0720.htm) hit the provenance gate (gated).
- **Currency:** chapter PDF page header; sos index blurb — observed: "July, 2022 (Revised)"
- **Official status:** sos.tn.gov/rules-and-regulations calls it the 'official compilation, Rules and Regulations of the State of Tennessee'.
- **Hazard:** date-stamped file names (not constructible)
- **Hazard:** chapters transferred/renumbered (1200-08-01 → 0720-14)
- **Hazard:** WebFetch hides index hrefs
- **Probe:** Tenn. Comp. R. & Regs. 1200-08-01-.01 → `https://publications.tnsosfiles.com/rules/1200/1200-08/1200-08-01.20220701.pdf` — expect: "RULES OF THE TENNESSEE DEPARTMENT OF HEALTH BOARD FOR LICENSING HEALTH"
- **Evidence (2026-10-17):** WebFetch: starts "July, 2022 (Revised) 1 RULES OF THE TENNESSEE DEPARTMENT OF HEALTH"; rules .01-.15 all 'TRANSFERRED' to 0720-14; not truncated.
- **Notes:** Older PDFs also on sharetngov.tnsosfiles.com/sos/rules/… (search result; robots 403 bot wall, not fetched).

### `tn-admincode-lii` — Tennessee Compilation of Rules & Regulations (Cornell LII)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Cornell Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Rule-level pages for all agencies.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/tennessee/Tenn-Comp-R-Regs-{rule}`
  - Placeholders: rule = the rule number exactly as cited, with its '-.NN' tail: 1200-13-19-.01, 0720-14-.01 (chapters without a subchapter have three parts). An unknown number silently returns the generic Tennessee index (5,850 chars) instead of a 404: check that the page heading names the rule.
  - Index: `https://www.law.cornell.edu/regulations/tennessee`
  - Navigation: title-{agency} → chapter-{chapter} → rule pages.
- **Automation:** WebFetch untested · shell ok · robots: permits; crawl-delay 10
  - Not tried with WebFetch (budget).
- **Currency:** page foot — observed: "State regulations are updated quarterly"
- **Official status:** Third-party republication; page says state regulations are updated quarterly.
- **Hazard:** lags the official compilation (1200-13-19-.01 shows 2015 history although SOS lists a 3/4/2026 amendment)
- **Hazard:** bad rule numbers fall back to an index page
- **Probe:** Tenn. Comp. R. & Regs. 1200-13-19-.01 → `https://www.law.cornell.edu/regulations/tennessee/Tenn-Comp-R-Regs-1200-13-19-.01` — expect: "This chapter governs all administrative hearings conducted for the purpose"
- **Evidence (2026-10-17):** Script grep: 1200-13-19-.01 body "This chapter governs all administrative hearings conducted for the purpose"; 0720-14-.01 body "(1) Abuse. The willful infliction of injury"; last-modified Aug 2025.

## D. Administrative register

### `tn-admin-register-sos` — Tennessee Administrative Register / rulemaking filings

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Tennessee Secretary of State, Division of Publications · text: **fetch-and-quote** · official: official
- **Coverage:** Rulemaking hearing notices, emergency and permanent rule filings as PDFs.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Filing PDFs are publications.tnsosfiles.com/rules_filings/{MM-DD-YY}.pdf where MM-DD-YY is a filing tracking number, not a date to construct.
  - Index: `https://sos.tn.gov/publications/services/recently-effective-rules-and-regulations`
  - Navigation: Recently Effective Rules page (lists chapters and effective dates; hrefs not exposed to WebFetch) → filing PDF. The Administrative Register index page itself was not located/fetched.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: CloudFront 403 bot wall on robots.txt
- **Currency:** recently-effective page list — observed: "entries from 3/5/2026 back to 1/28/2026 (as summarised by WebFetch)"
- **Official status:** Filings are stamped by the Department of State, Division of Publications (form SS-7037).
- **Hazard:** tracking-number file names
- **Hazard:** recently-effective page may not be up to date
- **Probe:** Notice of Rulemaking Hearing, ch. 0400-30-39 → `https://publications.tnsosfiles.com/rules_filings/04-09-24.pdf` — expect: "SS-7037 (March 2020) 1 RDA 1693 Department of State Division of Publications"
- **Evidence (2026-10-17):** WebFetch: 30-page notice of rulemaking hearing, Air Pollution Control Board, filed April 11, 2024; starts "SS-7037 (March 2020) 1 RDA 1693 Department of State".

## E. Case law

### `tn-opinions-tncourts` — Opinions of the Tennessee Supreme Court, Court of Appeals, Court of Criminal Appeals (tncourts.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Tennessee Administrative Office of the Courts · text: **link-only** · official: unknown
- **Coverage:** Slip opinions as PDFs (court listing pages per court).
- **Access:** `link-only` · format pdf
  - Index: `http://www.tncourts.gov/courts/supreme-court/opinions`
- **Automation:** WebFetch blocked · shell blocked-challenge · robots: robots.txt itself answers with the JavaScript browser-validation page (no parseable rules)
  - Every www.tncourts.gov / tncourts.gov URL tried (rule page, opinions page, node page, PDF under /sites/default/files/) returns a 138-character 'Please wait while we validate your browser' JavaScript challenge, to the script and to WebFetch alike. Host treated as bot-walled for both routes on 2026-10-17.
- **Currency:** 
- **Hazard:** bot challenge on every URL
- **Probe:**  → `https://www.tncourts.gov/courts/supreme-court/opinions`
- **Evidence (2026-10-17):** Script: kind=html chars=138 "Please wait while we validate your browser".

### `tn-cases-justia` — Tennessee opinions (Justia)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court, Court of Appeals, Court of Criminal Appeals, Special Workers' Compensation Appeals Panel; year listings (earliest year not shown on the court pages). Slip pagination only ('- 13 -' page markers); no S.W.3d cites.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/tennessee/{court}/{year}/{docket_lower}.html`
  - Placeholders: court = supreme-court | court-of-appeals | court-of-criminal-appeals | workers-compensation; year = decision year; docket_lower = the docket number lower-cased (M2022-01820-SC-R11-SV → m2022-01820-sc-r11-sv). Separate opinions may share a docket: check the year listing https://law.justia.com/cases/tennessee/{court}/{year}/ (it shows docket numbers and dates).
  - Index: `https://law.justia.com/cases/tennessee/`
  - Navigation: Court → year listing (case name, docket, date) → opinion page (full text) → PDF copy on cases.justia.com.
  - Read via: Each page links the court PDF at cases.justia.com/tennessee/{court}/{year}-{docket_lower}.pdf?ts=… (ts not constructible). fetch_doc.py read it (13 pages, 37,216 chars) — cases.justia.com is not on the vetted tier-2 list; see open_questions.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: script: law.justia.com answers robots.txt with a bot check
- **Currency:** year listing heading — observed: "Tennessee Court of Appeals Decisions 2025 (latest entry December 30, 2025)"
- **Official status:** Third-party republication of the courts' slip opinions.
- **Hazard:** slip pagination only
- **Hazard:** AI-written summary beside the opinion is not opinion text
- **Probe:** Pharma Conference Educ., Inc. v. State, No. W2021-00999-SC-R11-CV (Tenn. Dec. 20, 2024) → `https://law.justia.com/cases/tennessee/supreme-court/2024/w2021-00999-sc-r11-cv.html` — expect: "Pharma Conference Education, Inc., entered into an agreement with the University of"
- **Evidence (2026-10-17):** WebFetch: full opinion through signature, page marker "- 13 -", footnotes 1-4, not truncated. COA 2025 listing: URL docket = lower-cased docket for all entries.

## F. Subsequent history

### `tn-rule11-tncourts` — Tennessee Supreme Court discretionary appeals lists (Tenn. R. App. P. 11 grants/denials) and appellate case search

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Tennessee Supreme Court / Appellate Court Clerk · text: **link-only** · official: unknown
- **Coverage:** Periodic PDF lists of Rule 11 applications granted/denied (2025 lists seen in search results); docket-based appellate case search.
- **Access:** `link-only` · format pdf
  - Placeholders: List file names are irregular (e.g. 'Discretionary Appeals List -October-13-2025.pdf', 'Discretionary Appeals - 4-21-2025.pdf'); not constructible.
  - Index: `https://www.tncourts.gov/sites/default/files/AppealsFileAttachments/Discretionary%20Appeals%20List%20-October-13-2025.pdf`
- **Automation:** WebFetch blocked · shell blocked-challenge · robots: robots.txt itself answers with the JavaScript browser-validation page (no parseable rules)
  - Every www.tncourts.gov / tncourts.gov URL tried (rule page, opinions page, node page, PDF under /sites/default/files/) returns a 138-character 'Please wait while we validate your browser' JavaScript challenge, to the script and to WebFetch alike. Host treated as bot-walled for both routes on 2026-10-17.
- **Currency:** 
- **Hazard:** bot challenge on every URL
- **Probe:**  → `https://www.tncourts.gov/sites/default/files/AppealsFileAttachments/Discretionary%20Appeals%20List%20-October-13-2025.pdf`
- **Evidence (2026-10-17):** WebFetch: CHALLENGE "Please wait while we validate your browser"; script: kind=html chars=138, same text.
- **Notes:** Free fallback: a Supreme Court opinion on Justia states 'Appeal by Permission from the Court of Appeals' and its docket carries -SC-R11-; Rule 11 denials have no free tool-readable source and can only be found by party name or docket on the blocked host.

## Not available (do not look for these again)

- **statutes** — Government-hosted, tool-readable T.C.A. text or official bulk download: Code link from tn.gov and LII goes to LexisNexis free container (JS app, empty to both tools); capitol.tn.gov robots Disallow: /. No bulk/API found. (2026-10-17)
- **statutes** — public.law and Cornell LII editions of the Tennessee Code / Constitution: tennessee.public.law: proxy 502 on robots.txt; law.cornell.edu/states/tennessee links out to capitol.tn.gov, LexisNexis, tncourts.gov (LII hosts only the regulations). (2026-10-17)
- **court_rules** — Tier-2 copy of Tennessee court rules: Not on Justia or LII (LII links to tncourts.gov/courts/rules). (2026-10-17)
- **case_law** — Public-domain (vendor-neutral) citation format: Opinions identified by docket number (e.g. W2021-00999-SC-R11-CV) and S.W.3d/WL cites; no medium-neutral format. (2026-10-17)
- **case_law** — Free official reporter pagination: Justia pages and PDFs carry slip pagination only ('- 13 -'); no S.W.3d page numbers. (2026-10-17)
- **subsequent_history** — Tool-readable Rule 11 (permission to appeal) dispositions: Only on tncourts.gov discretionary-appeals PDFs and case search, both behind the browser-validation challenge. (2026-10-17)

## Open questions

- cases.justia.com (Justia's copy of the court PDF, linked from every law.justia.com opinion page) passes the script (no robots challenge) and would give a script route for Tennessee opinions; it is not on the vetted tier-2 host list. Maintainers to decide whether to admit it.
- tncourts.gov challenge: re-test later; if it lifts, verify per-rule URL slugs (rules-civil-procedure/1202), opinion listings and the discretionary-appeals PDFs.
- Tennessee Administrative Register index page on sos.tn.gov not located; only filing PDFs verified.
- Public Acts URL rule (acts/{GA}/pub/pc{NNNN}.pdf) verified on one chapter (107th GA) only; confirm for a recent GA (e.g. 113/pub/pc0123.pdf).
- sos.tn.gov may host the current Constitution (Tennessee Blue Book); not found in budget.
- LII Tennessee regulations may lag SOS (1200-13-19-.01 history ends 2015 although SOS lists a 3/4/2026 amendment) — compare before quoting.
