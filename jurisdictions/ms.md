# Mississippi (MS) — free legal sources

_Generated from `data/ms.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: the only government route to the Mississippi Code is LexisNexis's free unannotated container (JavaScript, no text to either tool), and the Legislature's hosts fail TLS verification, so Justia's 2025 Code (tier 2, WebFetch only; built section URLs verified) is the text source. Constitution: SOS annotated PDF ('updated May, 2022'; script reads all 193 pp). Court rules: courts.ms.gov PDFs for M.R.C.P., M.R.E., M.R.A.P., MRCrP, Professional Conduct, UCRCCC and UCCR are script-readable (corpus candidates). Case law: date-constructible SCT/COA hand-down lists (observed 2000-2026) link opinion PDFs with ¶ numbering; the Court's docket search is robots-disallowed, so Justia (constructible from docket + decision year) is the docket finder. Cert grants/denials appear on Supreme Court hand-down lists under -CT-…-SCT dockets. Admin code: SOS app returns no text; Cornell LII per-rule pages are constructible.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Mississippi | `miss (unverified)` | Miss. | So. 3d, So. 2d, So., Miss. | — |
| Court of Appeals of Mississippi | `missctapp (unverified)` | Miss. Ct. App. | So. 3d, So. 2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Mississippi Code of 1972 | `Miss. Code Ann. § 15-1-49`; `Miss. Code Ann. § 97-3-19(1)(a) (Rev. 2020)`; `Miss. Code Ann. §§ 11-9-101 to -147`; `Mississippi Code Section 11-7-13`; `Section 15-1-49 of the Mississippi Code`; `Miss. Code § 13-3-57` | `ms-code-justia` → `ms-code-lexis` |
| Mississippi Code of 1972 (bare "Section N-N-N", generic) *(only once this jurisdiction is known)* | `Section 15-1-49`; `section 11-46-11(3)` | `ms-code-justia` → `ms-code-lexis` |
| Mississippi Constitution of 1890 | `Miss. Const. art. 3, § 24`; `Miss. Const. art. 3, § 14`; `Miss. Const. § 273`; `Article 3, Section 24 of the Mississippi Constitution`; `Section 14 of the Mississippi Constitution`; `Miss. Const. of 1890, art. 6, § 146` | `ms-constitution-sos` → `ms-constitution-justia` |
| Mississippi Rules of Civil Procedure | `M.R.C.P. 12(b)(6)`; `Miss. R. Civ. P. 56(c)`; `MRCP 4(h)`; `Rule 12(b)(6) of the Mississippi Rules of Civil Procedure` | `ms-rules-civil` |
| Mississippi Rules of Evidence | `Miss. R. Evid. 803(4)`; `Rule 702 of the Mississippi Rules of Evidence` | `ms-rules-evidence` |
| Mississippi Rules of Evidence ("M.R.E." / "MRE", shared with Michigan) *(only once this jurisdiction is known)* | `M.R.E. 702`; `MRE 404(b)` | `ms-rules-evidence` |
| Mississippi Rules of Appellate Procedure | `M.R.A.P. 17`; `Miss. R. App. P. 17(a)`; `MRAP 28(a)(7)`; `Rule 17 of the Mississippi Rules of Appellate Procedure` | `ms-rules-appellate` |
| Mississippi Rules of Criminal Procedure | `MRCrP 8.1`; `Miss. R. Crim. P. 26.5`; `Rule 8.1 of the Mississippi Rules of Criminal Procedure` | `ms-rules-criminal` |
| Mississippi Rules of Professional Conduct | `Miss. R. Prof'l Conduct 1.7`; `Miss. R. Prof. Conduct 8.4(c)`; `Rule 1.7 of the Mississippi Rules of Professional Conduct` | `ms-rules-prof-conduct` |
| Mississippi Rules of Professional Conduct (bare "MRPC", shared with Michigan) *(only once this jurisdiction is known)* | `MRPC 1.7` | `ms-rules-prof-conduct` |
| Uniform Civil Rules of Circuit and County Court Practice | `UCRCCC 4.01`; `URCCC 9.04`; `Rule 4.01 of the Uniform Civil Rules of Circuit and County Court Practice`; `Unif. R. Cir. & Cnty. Ct. Prac. 9.04` | `ms-rules-ucrccc` |
| Uniform Chancery Court Rules | `UCCR 1.10`; `Unif. Ch. Ct. R. 8.05`; `Rule 8.05 of the Uniform Chancery Court Rules` | `ms-rules-chancery` |
| Mississippi Administrative Code | `Miss. Admin. Code 11-1:1.1`; `Miss. Admin. Code 23-200:1.3`; `11 Miss. Code R. 1-1.1`; `11 Miss. Code. R. 1-6.1` | `ms-admincode-lii` → `ms-admincode-sos` |
| Southern Reporter with a Mississippi parenthetical | `91 So. 3d 616 (Miss. 2012)`; `345 So. 3d 512, 516 (¶11) (Miss. 2022)`; `300 So. 3d 1, 5 (¶ 14) (Miss. Ct. App. 2020)`; `760 So. 2d 1265 (Miss. 2000)` | `ms-cases-justia` → `ms-sct-handdown` → `ms-coa-handdown` |
| Mississippi Reports (to 254 Miss., 1966) | `245 Miss. 123`; `Smith v. Jones, 250 Miss. 1, 163 So. 2d 676 (1964)` | `ms-cases-justia` |
| Mississippi appellate docket numbers (-SCT / -COA) | `2018-CA-01234-SCT`; `No. 2019-KA-00123-COA`; `2024-CT-01434-SCT`; `97-KA-01495-SCT`; `89-R-99012-SCT` | `ms-cases-justia` → `ms-sct-handdown` → `ms-coa-handdown` → `ms-cert-handdown` |
| Westlaw / Lexis cites for Mississippi decisions | `2024 WL 123456 (Miss. Ct. App. Mar. 5, 2024)`; `2023 Miss. LEXIS 123`; `2023 Miss. App. LEXIS 45` | `ms-cases-justia` |
| Mississippi certiorari history ("cert. denied/granted") *(only once this jurisdiction is known)* | `cert. denied, 300 So. 3d 1 (Miss. 2020)`; `cert. granted, 2024-CT-01434-SCT`; `cert. dismissed (Miss. 2026)` | `ms-cert-handdown` → `ms-cases-justia` |

Regexes (case-insensitive):

- Mississippi Code of 1972: `(?:Miss(?:\.|issippi)\s*Code(?:\s*(?:Ann(?:\.|otated)?|of\s*1972))*,?\s*(?:§§?|[Ss]ec(?:tion|\.)s?)?\s*|(?:[Ss]ection|§)\s*(?=\d{1,3}-\d{1,3}-\d+(?:\.\d+)?(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+Mississippi\s+Code))(?P<title>\d{1,3})-(?P<chapter>\d{1,3})-(?P<section>\d+(?:\.\d+)?)(?![\d-])`
- Mississippi Code of 1972 (bare "Section N-N-N", generic): `\b[Ss]ection\s+(?P<title>\d{1,3})-(?P<chapter>\d{1,3})-(?P<section>\d+(?:\.\d+)?)(?![\d-])`
- Mississippi Constitution of 1890: `Miss\.\s*Const\.(?:\s*(?:of\s*)?1890)?,?\s*(?:art\.?\s*(?P<article>\d{1,2}),?\s*)?§\s*(?P<section>\d{1,3}[A-Z]?)|(?:Article\s+(?P<article2>\d{1,2}),?\s*)?Section\s+(?P<section2>\d{1,3}[A-Z]?)\s+of\s+the\s+(?:Mississippi\s+Constitution|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Mississippi)`
- Mississippi Rules of Civil Procedure: `(?:\bM\.?R\.?C\.?P\.?|Miss\.\s*R\.\s*Civ\.\s*P\.)\s*(?P<rule>\d{1,2}(?:\.\d)?)|Rule\s+(?P<rule2>\d{1,2}(?:\.\d)?)(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+Mississippi\s+Rules\s+of\s+Civil\s+Procedure`
- Mississippi Rules of Evidence: `Miss\.\s*R\.\s*Evid\.\s*(?P<rule>\d{3})|Rule\s+(?P<rule2>\d{3})(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+Mississippi\s+Rules\s+of\s+Evidence`
- Mississippi Rules of Evidence ("M.R.E." / "MRE", shared with Michigan): `\bM\.?R\.?E\.?\s*(?P<rule>\d{3})`
- Mississippi Rules of Appellate Procedure: `(?:\bM\.?R\.?A\.?P\.?|Miss\.\s*R\.\s*App\.\s*P\.)\s*(?P<rule>\d{1,2}(?:\.\d)?)|Rule\s+(?P<rule2>\d{1,2}(?:\.\d)?)(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+Mississippi\s+Rules\s+of\s+Appellate\s+Procedure`
- Mississippi Rules of Criminal Procedure: `(?:\bM\.?R\.?Cr\.?P\.?|Miss\.\s*R\.\s*Crim\.\s*P\.)\s*(?P<rule>\d{1,2}(?:\.\d{1,2})?)|Rule\s+(?P<rule2>\d{1,2}(?:\.\d{1,2})?)(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+Mississippi\s+Rules\s+of\s+Criminal\s+Procedure`
- Mississippi Rules of Professional Conduct: `Miss\.\s*R\.\s*Prof(?:'?l|\.)?\s*Conduct\s*(?P<rule>\d\.\d{1,2})|Rule\s+(?P<rule2>\d\.\d{1,2})(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+Mississippi\s+Rules\s+of\s+Professional\s+Conduct`
- Mississippi Rules of Professional Conduct (bare "MRPC", shared with Michigan): `\bMRPC\s*(?P<rule>\d\.\d{1,2})`
- Uniform Civil Rules of Circuit and County Court Practice: `\bU\.?C?\.?R\.?C\.?C\.?C\.?\s*(?P<rule>\d{1,2}\.\d{2})|Unif\.\s*(?:Civ\.\s*)?R\.\s*Cir\.\s*&\s*C(?:ou)?nty\.?\s*Ct\.\s*Prac\.\s*(?P<rule3>\d{1,2}\.\d{2})|Rule\s+(?P<rule2>\d{1,2}\.\d{2})\s+of\s+the\s+Uniform\s+(?:Civil\s+)?Rules\s+of\s+Circuit\s+and\s+County\s+Court(?:\s+Practice)?`
- Uniform Chancery Court Rules: `\bUCCR\s*(?P<rule>\d{1,2}\.\d{2})|Unif\.\s*Ch(?:anc)?\.\s*Ct\.\s*R\.\s*(?P<rule3>\d{1,2}\.\d{2})|Rule\s+(?P<rule2>\d{1,2}\.\d{2})\s+of\s+the\s+Uniform\s+Chancery\s+Court\s+Rules`
- Mississippi Administrative Code: `Miss\.\s*Admin\.\s*Code\s*(?:R\.\s*)?(?:§\s*)?(?P<title>\d{1,2})-(?P<part>\d{1,4}):(?P<rule>\d+(?:\.\d+)+)|(?P<title2>\d{1,2})\s+Miss\.\s*Code\.?\s*R\.\s*(?P<part2>\d{1,4})-(?P<rule2>\d+(?:\.\d+)+)`
- Southern Reporter with a Mississippi parenthetical: `(?P<volume>\d{1,4})\s+So\.\s*(?P<series>[23]d)?\s*(?P<page>\d{1,5})(?:,\s*\d+(?:-\d+)?)?(?:\s*\(¶+\s*\d+(?:-\d+)?\))?\s*\((?P<court>Miss\.(?:\s*Ct\.\s*App\.)?)\s*(?P<year>\d{4})\)`
- Mississippi Reports (to 254 Miss., 1966): `(?P<volume>\d{1,3})\s+Miss\.\s+(?P<page>\d{1,4})(?!\d)`
- Mississippi appellate docket numbers (-SCT / -COA): `\b(?P<docket>(?P<year>(?:19|20)\d{2}|\d{2})-(?P<type>[A-Z]{1,2})-(?P<number>\d{5})-(?P<court>SCT|COA))\b`
- Westlaw / Lexis cites for Mississippi decisions: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Miss\.|Miss\.\s*(?:(?P<lexapp>App\.)\s*)?LEXIS\s+(?P<lexis>\d+))`
- Mississippi certiorari history ("cert. denied/granted"): `cert\.\s*(?P<disposition>denied|granted|dismissed)`

Short forms → URL key:

Miss. Code Ann. → `mca1972`; Miss. Code → `mca1972`; Mississippi Code → `mca1972`; Mississippi Code of 1972 → `mca1972`; M.R.C.P. → `mrcp`; MRCP → `mrcp`; Miss. R. Civ. P. → `mrcp`; M.R.E. → `mre`; MRE → `mre`; Miss. R. Evid. → `mre`; M.R.A.P. → `mrap`; MRAP → `mrap`; Miss. R. App. P. → `mrap`; MRCrP → `mrcrp`; Miss. R. Crim. P. → `mrcrp`; Miss. R. Prof'l Conduct → `mrpc`; MRPC → `mrpc`; UCRCCC → `ucrccc`; URCCC → `ucrccc`; UCCR → `uccr`; Miss. Admin. Code → `mac`; Miss. Code R. → `mac`

No public-domain citation: Mississippi cites So. 3d (So. 2d / So. earlier; 'Miss.' official reports ended 1966) with ¶ pinpoints, e.g. '345 So. 3d 512, 516 (¶11) (Miss. 2022)'; slip opinions are identified by docket '{year}-{type}-{5 digits}-{SCT|COA}' (types include CA civil, KA criminal, CP civil pro se, KM, CT certiorari, IA interlocutory, DR death-post-conviction, SA state agency, FC federal certified question, R rules). The -SCT/-COA suffix is distinctive, so docket numbers route here without context. A petition for certiorari from a Court of Appeals decision becomes '{year}-CT-{number}-SCT' (same number as the COA case — from memory; CT dockets observed on hand-down lists). Bare 'Section 15-1-49' (Mississippi's own style) is shared with Alabama and others: context_required. 'MRPC' is also used by Michigan and Minnesota: context_required; 'M.R.E.'/'MRE' are shared with Michigan: context_required; 'Miss. R. Prof'l Conduct' is distinctive. 'M.R.C.P.', 'M.R.E.', 'M.R.A.P.' are Mississippi's house abbreviations; Montana/Maine use 'M. R. Civ. P.'/'M.R. Civ. P.' which these regexes do not match (C must be followed by P). 'cert. denied' routes here only with Mississippi context. A '§§ 11-9-101 to -147' range takes the first section only. CourtListener ids miss / missctapp from memory, unverified.

## A. Statutes / code

### `ms-code-lexis` — Mississippi Code of 1972 (unannotated, free public access via LexisNexis)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · State of Mississippi / LexisNexis (official publisher) · text: **link-only** · official: unknown
- **Coverage:** Entire Mississippi Code of 1972, unannotated (per SOS page).
- **Access:** `link-only` · format html
  - Placeholders: No per-section URL; the hottopics link 302-redirects to an advance.lexis.com container (JavaScript app).
  - Index: `https://www.lexisnexis.com/hottopics/mscode/`
  - Navigation: Human only: sos.ms.gov/node/147 or courts.ms.gov 'MS Code' → lexisnexis.com/hottopics/mscode/ → advance.lexis.com container → TOC → title → chapter → section.
- **Automation:** WebFetch fail · shell http-error · robots: script robots check passed (followed redirect to advance.lexis.com)
  - WebFetch: 302 to advance.lexis.com container (not followed; Georgia's identical Lexis container returned empty content). fetch_doc.py: kind=html chars=0, 0 links.
- **Currency:** none observed (app did not render)
- **Official status:** sos.ms.gov/node/147 ('Mississippi Law') says the searchable unannotated Code is provided through LexisNexis, the Code's official publisher; no statement that the online text is official.
- **Hazard:** JavaScript-only app
- **Hazard:** no per-section URLs
- **Probe:** Miss. Code (container) → `https://www.lexisnexis.com/hottopics/mscode/`
- **Evidence (2026-10-17):** Link from sos.ms.gov/node/147 and courts.ms.gov rules page. Script: redirect to advance.lexis.com container, html chars=0.
- **Notes:** The legislature's own hosts (www.legislature.ms.gov, billstatus.ls.state.ms.us, www.ls.state.ms.us) fail TLS verification from the sandbox, so no government source serves Code text to either tool.

### `ms-legislature-session-laws` — Mississippi Legislature — bill status and General Laws (session laws)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Mississippi Legislature · text: **link-only** · official: unknown
- **Coverage:** Bills, enacted measures by session (expected).
- **Access:** `search-only` · format html
  - Index: `https://www.legislature.ms.gov/`
  - Navigation: Human only until TLS works: legislature.ms.gov → Legislation → session → bill status page.
- **Automation:** WebFetch gated · shell tls-error · robots: not readable (TLS)
  - fetch_doc.py: TLS certificate chain does not verify for www.legislature.ms.gov, legislature.ms.gov, billstatus.ls.state.ms.us, www.ls.state.ms.us. WebFetch of www.legislature.ms.gov: PROVENANCE_REQUIRED (approval prompt unanswered).
- **Currency:** none observed
- **Official status:** Not reached (TLS failure).
- **Hazard:** TLS chain fails to verify (missing intermediate?)
- **Probe:** legislature home → `https://www.legislature.ms.gov/`
- **Evidence (2026-10-17):** Script: FETCH ERROR TLS certificate chain does not verify (4 legislature hosts).

### `ms-code-justia` — Justia — Mississippi Code 1972 (2025)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** 2025 Mississippi Code 1972 (unversioned URLs); earlier editions under /codes/mississippi/{year}/ (2014-2024 seen in search results).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/codes/mississippi/title-{title}/chapter-{chapter}/[article-{article}/]section-{title}-{chapter}-{section}/`
  - Placeholders: Title and chapter from the citation (15-1-49 → title-15/chapter-1/section-15-1-49/). Chapters divided into articles add /article-{n}/; the article is not in the citation: read it from the chapter index, whose links show '§§' ranges (e.g. 'Article 3 - Justice Courts (§§ 11-9-101 - 11-9-147)'). Title indexes show chapter §§ ranges, or 'Arts. 1 - 3' for chapters with articles. Year editions: insert /{year}/ after /mississippi/.
  - Index: `https://law.justia.com/codes/mississippi/title-{title}/`
  - Navigation: title index (chapter links with §§ ranges; 'Arts.' marks a chapter with articles) → if 'Arts.', open the chapter index and pick the article by §§ range → section page. Verified built URLs: 15-1-49 → /title-15/chapter-1/section-15-1-49/; 97-3-19 → /title-97/chapter-3/section-97-3-19/.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: law.justia.com answers robots.txt with a bot check (fetch_doc.py REFUSED)
  - Built section URLs passed WebFetch without an approval prompt. Article-level section URLs (e.g. 11-9-143) inferred from the Georgia pattern, not fetched.
- **Currency:** page header — observed: "2025 Mississippi Code 1972"
- **Official status:** Page states 'These codes may not be the most recent version.'; third-party compilation.
- **Hazard:** article level not derivable from the citation (index hop)
- **Hazard:** edition lags the session laws
- **Hazard:** shell blocked by bot check: WebFetch only
- **Probe:** Miss. Code Ann. § 15-1-49 → `https://law.justia.com/codes/mississippi/title-15/chapter-1/section-15-1-49/` — expect: "All actions for which no other period of limitation is"
- **Evidence (2026-10-17):** WebFetch: YES, 'All actions for which no other period of limitation is'; '2025 Mississippi Code 1972'; not truncated. Second: § 97-3-19 'The killing of a human being without the authority of'.
- **Notes:** The only text route for the Code reachable by the skill; quotes are single-source tier 2 and must say so.

## B. Constitution

### `ms-constitution-sos` — Constitution of the State of Mississippi, annotated (Secretary of State PDF)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Mississippi Secretary of State · text: **fetch-and-quote** · official: unknown
- **Coverage:** Constitution of 1890 as amended, with sources and annotations; 193 pp, 368,794 chars; sections run consecutively (1-285) across articles.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.sos.ms.gov/sites/default/files/publications/Mississippi_Constitution.pdf`
  - Placeholders: Single fixed PDF; sections numbered consecutively, so 'art. 3, § 24' = 'SECTION 24.' heading.
  - Index: `https://www.sos.ms.gov/node/147`
  - Navigation: sos.ms.gov/node/147 → 'Mississippi Constitution' PDF → grep 'SECTION {n}.' (the first hit is the article's section list; the second is the body).
- **Automation:** WebFetch gated · shell ok · robots: sos.ms.gov: Drupal defaults (/admin/, /search/, /user/…); /sites/default/files/ allowed
  - WebFetch: PROVENANCE_REQUIRED (approval prompt unanswered), not a site refusal. Script reads all 193 pages.
- **Currency:** PDF cover — observed: "ANNOTATED UPDATED MAY, 2022"
- **Official status:** Published by the Secretary of State (sos.ms.gov/node/147 'Mississippi Law'); no official/unofficial statement seen.
- **Hazard:** cover says updated May 2022 though file last-modified 15 Apr 2026: check later amendments
- **Hazard:** annotations and SOURCES lines follow each section
- **Hazard:** section list at the head of each article repeats headings
- **Probe:** Miss. Const. art. 3, § 24 → `https://www.sos.ms.gov/sites/default/files/publications/Mississippi_Constitution.pdf` — expect: "All courts shall be open; and every person for an injury done him"
- **Evidence (2026-10-17):** Script grep: page 16 'SECTION 24. Open courts; remedy for injury. All courts shall be open'; § 14 'No person shall be deprived of life, liberty, or property'; § 273 'Amendments to this Constitution may be proposed by the Legislature'.

### `ms-constitution-justia` — Justia — Mississippi Constitution

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole constitution on one page (120,868 chars); age of text unknown.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/mississippi/`
  - Placeholders: One page for all sections; no anchors.
  - Index: `https://law.justia.com/constitution/mississippi/`
  - Navigation: single page; WebFetch window 1 reaches Section 156, offset=100000 for the rest
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: unreadable (bot check)
  - Window 1 ends inside Section 157.
- **Currency:** none stated — observed: "ADOPTED NOVEMBER 1, A.D., 1890."
- **Official status:** Third-party page; no version statement (only 'ADOPTED NOVEMBER 1, A.D., 1890').
- **Hazard:** possibly stale text
- **Hazard:** truncated at ~Section 157: use offset 100000
- **Hazard:** shell blocked
- **Probe:** Miss. Const. art. 3, § 24 → `https://law.justia.com/constitution/mississippi/` — expect: "All courts shall be open; and every person for an"
- **Evidence (2026-10-17):** WebFetch: YES, Section 24 'All courts shall be open; and every person for an'; highest complete section in window 1: 156; page 120,868 chars.

## C. Court rules

### `ms-rules-appellate` — Mississippi Rules of Appellate Procedure

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Mississippi (Administrative Office of Courts) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Complete rule set with comments / advisory committee notes in one PDF (183 pp, 352,863 chars; last-modified 23 Jun 2026).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.ms.gov/research/rules/msrulesofcourt/Rules%20of%20Appellate%20Procedure%20Current.pdf`
  - Placeholders: Single PDF; the file name changes when the Court reissues the set (dated names such as '2026-07-01 Rules of ...'), so always take the current link from the index.
  - Index: `https://courts.ms.gov/research/rules/rules.php`
  - Navigation: rules.php → link 'Mississippi Rules of Appellate Procedure' → PDF; locate the rule by its 'RULE 17. REVIEW IN THE SUPREME COURT ...' heading (script grep/section).
- **Automation:** WebFetch gated · shell ok · robots: courts.ms.gov: User-agent * — /research/ not disallowed (disallows /appellatecourts/docket/, /search/, /scripts/ etc.)
  - WebFetch on courts.ms.gov URLs waited on the session's URL-approval prompt (PROVENANCE_REQUIRED) — not a site refusal. Far beyond one ~100K WebFetch window: script or corpus only.
- **Currency:** amendment notes in brackets after each rule; file name / last-modified — observed: "'[Amended effective May 5, 2020.]' style notes; last-modified 23 Jun 2026"
- **Official status:** Published by the Supreme Court on courts.ms.gov 'MS Rules of Court'; no official/unofficial statement seen.
- **Hazard:** long PDF (beyond WebFetch window)
- **Hazard:** file name changes on reissue
- **Hazard:** comments/advisory notes follow each rule: do not quote as rule text
- **Probe:** M.R.A.P. 17 → `https://courts.ms.gov/research/rules/msrulesofcourt/Rules%20of%20Appellate%20Procedure%20Current.pdf` — expect: "Decisions of Court of Appeals Reviewable by Writ of Certiorari"
- **Evidence (2026-10-17):** Script verify: VERIFIED page 57 'Decisions of Court of Appeals Reviewable by Writ of Certiorari' (Rule 17(a)).

### `ms-rules-chancery` — Uniform Chancery Court Rules (UCCR)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Mississippi (Administrative Office of Courts) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Complete rule set with comments / advisory committee notes in one PDF (32 pp, 48,463 chars; last-modified 1 Jul 2026).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.ms.gov/research/rules/msrulesofcourt/uniform_chancery_rules.pdf`
  - Placeholders: Single PDF; the file name changes when the Court reissues the set (dated names such as '2026-07-01 Rules of ...'), so always take the current link from the index.
  - Index: `https://courts.ms.gov/research/rules/rules.php`
  - Navigation: rules.php → link 'Uniform Chancery Court Rules' → PDF; locate the rule by its 'RULE 1.10 DISCOVERY DEADLINES AND PRACTICE' heading (script grep/section).
- **Automation:** WebFetch gated · shell ok · robots: courts.ms.gov: User-agent * — /research/ not disallowed (disallows /appellatecourts/docket/, /search/, /scripts/ etc.)
  - WebFetch on courts.ms.gov URLs waited on the session's URL-approval prompt (PROVENANCE_REQUIRED) — not a site refusal. Far beyond one ~100K WebFetch window: script or corpus only.
- **Currency:** amendment notes in brackets after each rule; file name / last-modified — observed: "last-modified 1 Jul 2026"
- **Official status:** Published by the Supreme Court on courts.ms.gov 'MS Rules of Court'; no official/unofficial statement seen.
- **Hazard:** long PDF (beyond WebFetch window)
- **Hazard:** file name changes on reissue
- **Hazard:** comments/advisory notes follow each rule: do not quote as rule text
- **Probe:** UCCR 1.10 → `https://courts.ms.gov/research/rules/msrulesofcourt/uniform_chancery_rules.pdf` — expect: "All discovery must be completed within ninety days from service of an answer"
- **Evidence (2026-10-17):** Script grep: 'RULE 1.00 ... may be cited as UCCR'; p. 9 'RULE 1.10 ... All discovery must be completed within ninety days'.

### `ms-rules-civil` — Mississippi Rules of Civil Procedure (with Advisory Committee Notes)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Mississippi (Administrative Office of Courts) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Complete rule set with comments / advisory committee notes in one PDF (231 pp, 467,917 chars; last-modified 1 Jul 2026).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.ms.gov/research/rules/msrulesofcourt/2026-07-01%20Rules%20of%20Civil%20Procedure%20with%20Advisory%20Committee%20Notes%20(with%20Forms%206-8%20attached).pdf`
  - Placeholders: Single PDF; the file name changes when the Court reissues the set (dated names such as '2026-07-01 Rules of ...'), so always take the current link from the index.
  - Index: `https://courts.ms.gov/research/rules/rules.php`
  - Navigation: rules.php → link 'Mississippi Rules of Civil Procedure' → PDF; locate the rule by its 'RULE 56. SUMMARY JUDGMENT' heading (script grep/section).
- **Automation:** WebFetch gated · shell ok · robots: courts.ms.gov: User-agent * — /research/ not disallowed (disallows /appellatecourts/docket/, /search/, /scripts/ etc.)
  - WebFetch on courts.ms.gov URLs waited on the session's URL-approval prompt (PROVENANCE_REQUIRED) — not a site refusal. Far beyond one ~100K WebFetch window: script or corpus only.
- **Currency:** amendment notes in brackets after each rule; file name / last-modified — observed: "file name '2026-07-01 Rules of Civil Procedure'"
- **Official status:** Published by the Supreme Court on courts.ms.gov 'MS Rules of Court'; no official/unofficial statement seen.
- **Hazard:** long PDF (beyond WebFetch window)
- **Hazard:** file name changes on reissue
- **Hazard:** comments/advisory notes follow each rule: do not quote as rule text
- **Hazard:** PDF line numbers leak into text (e.g. 'granted, 35 (7)'): verify quotes with fetch_doc verify
- **Probe:** M.R.C.P. 12(b)(6) → `https://courts.ms.gov/research/rules/msrulesofcourt/2026-07-01%20Rules%20of%20Civil%20Procedure%20with%20Advisory%20Committee%20Notes%20(with%20Forms%206-8%20attached).pdf` — expect: "Failure to state a claim upon which relief can be granted"
- **Evidence (2026-10-17):** Script: 231 pp; Rule 12(b)(6) p. 43 '(6) Failure to state a claim upon which relief can be granted'; 'RULE 56. SUMMARY JUDGMENT' p. 156.

### `ms-rules-criminal` — Mississippi Rules of Criminal Procedure (effective July 1, 2023 version)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Mississippi (Administrative Office of Courts) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Complete rule set with comments / advisory committee notes in one PDF (185 pp, 356,996 chars; last-modified 19 Mar 2026).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.ms.gov/research/rules/msrulesofcourt/Rules%20of%20Criminal%20Procedure%20Post-070123.pdf`
  - Placeholders: Single PDF; the file name changes when the Court reissues the set (dated names such as '2026-07-01 Rules of ...'), so always take the current link from the index.
  - Index: `https://courts.ms.gov/research/rules/rules.php`
  - Navigation: rules.php → link 'Mississippi Rules of Criminal Procedure' → PDF; locate the rule by its 'Rule 8.1 Definitions and Requirements.' heading (script grep/section).
- **Automation:** WebFetch gated · shell ok · robots: courts.ms.gov: User-agent * — /research/ not disallowed (disallows /appellatecourts/docket/, /search/, /scripts/ etc.)
  - WebFetch on courts.ms.gov URLs waited on the session's URL-approval prompt (PROVENANCE_REQUIRED) — not a site refusal. Far beyond one ~100K WebFetch window: script or corpus only.
- **Currency:** amendment notes in brackets after each rule; file name / last-modified — observed: "index link text 'effective July 1, 2023'"
- **Official status:** Published by the Supreme Court on courts.ms.gov 'MS Rules of Court'; no official/unofficial statement seen.
- **Hazard:** long PDF (beyond WebFetch window)
- **Hazard:** file name changes on reissue
- **Hazard:** comments/advisory notes follow each rule: do not quote as rule text
- **Hazard:** rule headings are mixed case without 'RULE' caps: grep 'Rule N.N Title.'
- **Probe:** MRCrP 8.1 → `https://courts.ms.gov/research/rules/msrulesofcourt/Rules%20of%20Criminal%20Procedure%20Post-070123.pdf` — expect: "Whenever the terms below appear in these Rules, they shall have"
- **Evidence (2026-10-17):** Script grep: p. 39 'Rule 8 Release Rule 8.1 Definitions and Requirements. Whenever the terms below appear'.

### `ms-rules-evidence` — Mississippi Rules of Evidence (restyled)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Mississippi (Administrative Office of Courts) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Complete rule set with comments / advisory committee notes in one PDF (146 pp, 333,606 chars; last-modified 19 Mar 2026).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.ms.gov/research/rules/msrulesofcourt/2025-04-07%20Restyled%20Rules%20of%20Evidence.pdf`
  - Placeholders: Single PDF; the file name changes when the Court reissues the set (dated names such as '2026-07-01 Rules of ...'), so always take the current link from the index.
  - Index: `https://courts.ms.gov/research/rules/rules.php`
  - Navigation: rules.php → link 'Mississippi Rules of Evidence' → PDF; locate the rule by its 'Rule 702. Testimony by Expert Witnesses' heading (script grep/section).
- **Automation:** WebFetch gated · shell ok · robots: courts.ms.gov: User-agent * — /research/ not disallowed (disallows /appellatecourts/docket/, /search/, /scripts/ etc.)
  - WebFetch on courts.ms.gov URLs waited on the session's URL-approval prompt (PROVENANCE_REQUIRED) — not a site refusal. Far beyond one ~100K WebFetch window: script or corpus only.
- **Currency:** amendment notes in brackets after each rule; file name / last-modified — observed: "file name '2025-04-07 Restyled Rules of Evidence'"
- **Official status:** Published by the Supreme Court on courts.ms.gov 'MS Rules of Court'; no official/unofficial statement seen.
- **Hazard:** long PDF (beyond WebFetch window)
- **Hazard:** file name changes on reissue
- **Hazard:** comments/advisory notes follow each rule: do not quote as rule text
- **Probe:** M.R.E. 702 → `https://courts.ms.gov/research/rules/msrulesofcourt/2025-04-07%20Restyled%20Rules%20of%20Evidence.pdf` — expect: "A witness who is qualified as an expert by knowledge, skill, experience"
- **Evidence (2026-10-17):** Script verify: VERIFIED page 86 'A witness who is qualified as an expert by knowledge, skill, experience'.

### `ms-rules-local` — Local Circuit / Chancery / County Court Rules (index pages)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Supreme Court of Mississippi · text: **fetch-and-quote** · official: unknown
- **Coverage:** Local rules by judicial district (not opened).
- **Access:** `index-anchored` · format pdf
  - Index: `https://courts.ms.gov/research/rules/localcircuitrules.php`
  - Navigation: rules.php → 'Local Circuit Court Rules' / 'Local Chancery Court Rules' (localchanceryrules.php) / 'Local County Court Rules' (localcountyrules.php) → district PDF.
- **Automation:** WebFetch untested · shell untested · robots: permitted path
  - Links seen on rules.php; not opened (budget).
- **Currency:** not checked
- **Official status:** Court-approved local rules listed by district on courts.ms.gov.
- **Probe:**  → `https://courts.ms.gov/research/rules/localcircuitrules.php`
- **Evidence (2026-10-17):** Link texts seen by script links on rules.php.
- **Notes:** Rule amendments: courts.ms.gov/research/rules/ruleamendments/ruleamendments.php; rules for comment: …/rulesforcomment/rulesforcomment.php.

### `ms-rules-prof-conduct` — Mississippi Rules of Professional Conduct

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Mississippi (Administrative Office of Courts) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Complete rule set with comments / advisory committee notes in one PDF (143 pp, 361,479 chars; last-modified 6 Jul 2026).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.ms.gov/research/rules/msrulesofcourt/rules_of_professional_conduct.pdf`
  - Placeholders: Single PDF; the file name changes when the Court reissues the set (dated names such as '2026-07-01 Rules of ...'), so always take the current link from the index.
  - Index: `https://courts.ms.gov/research/rules/rules.php`
  - Navigation: rules.php → link 'Mississippi Rules of Professional Conduct' → PDF; locate the rule by its 'RULE 1.7 CONFLICT OF INTEREST: GENERAL RULE' heading (script grep/section).
- **Automation:** WebFetch gated · shell ok · robots: courts.ms.gov: User-agent * — /research/ not disallowed (disallows /appellatecourts/docket/, /search/, /scripts/ etc.)
  - WebFetch on courts.ms.gov URLs waited on the session's URL-approval prompt (PROVENANCE_REQUIRED) — not a site refusal. Far beyond one ~100K WebFetch window: script or corpus only.
- **Currency:** amendment notes in brackets after each rule; file name / last-modified — observed: "'[Amended effective November 3, 2005.]' style notes; last-modified 6 Jul 2026"
- **Official status:** Published by the Supreme Court on courts.ms.gov 'MS Rules of Court'; no official/unofficial statement seen.
- **Hazard:** long PDF (beyond WebFetch window)
- **Hazard:** file name changes on reissue
- **Hazard:** comments/advisory notes follow each rule: do not quote as rule text
- **Probe:** Miss. R. Prof'l Conduct 1.7 → `https://courts.ms.gov/research/rules/msrulesofcourt/rules_of_professional_conduct.pdf` — expect: "A lawyer shall not represent a client if the representation of that client"
- **Evidence (2026-10-17):** Script verify: VERIFIED page 29 'A lawyer shall not represent a client if the representation of that client'.

### `ms-rules-ucrccc` — Uniform Civil Rules of Circuit and County Court Practice (UCRCCC)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Mississippi (Administrative Office of Courts) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Complete rule set with comments / advisory committee notes in one PDF (25 pp, 62,492 chars; last-modified 21 May 2026).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.ms.gov/research/rules/msrulesofcourt/UCRCCC%20Post-070117.pdf`
  - Placeholders: Single PDF; the file name changes when the Court reissues the set (dated names such as '2026-07-01 Rules of ...'), so always take the current link from the index.
  - Index: `https://courts.ms.gov/research/rules/rules.php`
  - Navigation: rules.php → link 'Uniform Civil Rules of Circuit and County Court Practice' → PDF; locate the rule by its 'Rule 4.01 COST DEPOSIT' heading (script grep/section).
- **Automation:** WebFetch gated · shell ok · robots: courts.ms.gov: User-agent * — /research/ not disallowed (disallows /appellatecourts/docket/, /search/, /scripts/ etc.)
  - WebFetch on courts.ms.gov URLs waited on the session's URL-approval prompt (PROVENANCE_REQUIRED) — not a site refusal. Far beyond one ~100K WebFetch window: script or corpus only.
- **Currency:** amendment notes in brackets after each rule; file name / last-modified — observed: "'Adopted Effective May 1, 1995; Amended Effective July 1, 2017'"
- **Official status:** Published by the Supreme Court on courts.ms.gov 'MS Rules of Court'; no official/unofficial statement seen.
- **Hazard:** long PDF (beyond WebFetch window)
- **Hazard:** file name changes on reissue
- **Hazard:** comments/advisory notes follow each rule: do not quote as rule text
- **Probe:** UCRCCC 4.01 → `https://courts.ms.gov/research/rules/msrulesofcourt/UCRCCC%20Post-070117.pdf` — expect: "A cost deposit shall be made with the clerk"
- **Evidence (2026-10-17):** Script grep: Rule 1.01 'may be cited as "UCRCCC _.__."'; Rule 4.01 'A cost deposit shall be made with the cler[k]'.
- **Notes:** Short enough for one WebFetch window (62K chars) once the approval gate is not in the way. Criminal practice moved to the Rules of Criminal Procedure in 2017.

## D. Administrative code

### `ms-admincode-sos` — Mississippi Administrative Code (Secretary of State search)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Mississippi Secretary of State · text: **link-only** · official: unknown
- **Coverage:** All titles/parts as filed; rule PDFs under /adminsearch/ACCode/{8 digits}{letter}.pdf (e.g. 00000300c.pdf = Title 2 Part 904, 2012).
- **Access:** `search-only` · format pdf
  - Placeholders: PDF ids are opaque numbers, not derivable from a citation.
  - Index: `https://www.sos.ms.gov/adminsearch/default.aspx`
  - Navigation: Human only: sos.ms.gov/regulation-enforcement/administrative-code (iframe) → adminsearch/default.aspx → search by title/agency → part PDF.
- **Automation:** WebFetch gated · shell http-error · robots: sos.ms.gov: /adminsearch/ not disallowed
  - fetch_doc.py: adminsearch/ and default.aspx return html chars=0 (ASP.NET/JS). One ACCode PDF opened by script (2 pp, 'Title 2: Agriculture and Commerce Part 904'), but its id came from a guess, so it is not a route. WebFetch: PROVENANCE_REQUIRED.
- **Currency:** none observed
- **Official status:** Secretary of State is the filing office; app did not render, no statement read.
- **Hazard:** app returns no HTML text
- **Hazard:** opaque PDF ids
- **Probe:** admin code search → `https://www.sos.ms.gov/adminsearch/default.aspx`
- **Evidence (2026-10-17):** Script: kind=html chars=0 for adminsearch/ and default.aspx; admin-code page embeds it as an iframe.

### `ms-admincode-lii` — Cornell LII — Mississippi Administrative Code

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All titles 1-40, per-rule pages with Notes (authority, amendment history).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/mississippi/{title}-Miss-Code-R-SS-{part}-{rule_dots_to_hyphens}`
  - Placeholders: Miss. Admin. Code {title}-{part}:{chapter}.{rule} → {title}-Miss-Code-R-SS-{part}-{chapter}-{rule} (11-1:1.1 → 11-Miss-Code-R-SS-1-1-1; 11-1:6.1 → 11-Miss-Code-R-SS-1-6-1). LII's own cite form: '11 Miss. Code. R. 1-1.1'.
  - Index: `https://www.law.cornell.edu/regulations/mississippi`
  - Navigation: index → /title-{t} (parts with chapter ranges) → /title-{t}/part-{p} → /chapter-{c} → rule links.
- **Automation:** WebFetch untested · shell ok · robots: permits; crawl-delay 10
  - Search-result URLs of the form Miss-Admin-Code-11-8-31 return only a navigation shell (no rule).
- **Currency:** rule page, below Notes — observed: "State regulations are updated quarterly; Amended 11/22/2015 (11-1:1.1)"
- **Official status:** Third-party; page says 'State regulations are updated quarterly'.
- **Hazard:** crawl-delay 10 s
- **Hazard:** quarterly lag
- **Hazard:** multi-level rule numbers (x.y.z) not tested
- **Probe:** Miss. Admin. Code 11-1:1.1 → `https://www.law.cornell.edu/regulations/mississippi/11-Miss-Code-R-SS-1-1-1` — expect: "The Commission delegates the following powers to the Executive Director of MDEQ"
- **Evidence (2026-10-17):** Script: '11 Miss. Code. R. 1-1.1 - Delegations … The Commission delegates the following powers'; built 11-Miss-Code-R-SS-1-6-1 → '11 Miss. Code. R. 1-6.1 - General'.
- **Notes:** regulations.justia.com also hosts the code but is not on the tier-2 list (only law.justia.com).

## D. Administrative register

### `ms-admin-bulletin` — Mississippi Administrative Bulletin (Secretary of State)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Mississippi Secretary of State · text: **link-only** · official: unknown
- **Coverage:** Filed proposed/final rule notices (expected).
- **Access:** `search-only` · format html
  - Index: `https://www.sos.ms.gov/adminsearch/default.aspx?current_page=Bulletin`
  - Navigation: Human only: sos.ms.gov/regulation-enforcement/administrative-code/administrative-bulletin (iframe) → adminsearch default.aspx?current_page=Bulletin.
- **Automation:** WebFetch untested · shell http-error · robots: not disallowed
  - Same ASP.NET app as ms-admincode-sos (0 chars to script).
- **Currency:** none observed
- **Official status:** Not reached.
- **Hazard:** app returns no text
- **Probe:** bulletin → `https://www.sos.ms.gov/adminsearch/default.aspx?current_page=Bulletin`
- **Evidence (2026-10-17):** Script: bulletin page body is only an iframe pointing to default.aspx?current_page=Bulletin.

## E. Case law

### `ms-appellate-docket` — Mississippi appellate General Docket (case search, docket entries, order PDFs)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Clerk of the Appellate Courts · text: **link-only** · official: official
- **Coverage:** Docket entries and orders (sendPDF.php).
- **Access:** `search-only` · format html
  - Index: `https://courts.ms.gov/appellatecourts/docket/`
  - Navigation: Not usable: robots.txt Disallow: /appellatecourts/docket/ and /appellatecourts/docket/sendPDF.php.
- **Automation:** WebFetch blocked · shell blocked-robots · robots: Disallow: /appellatecourts/docket/; Disallow: /appellatecourts/docket/sendPDF.php
- **Currency:** n/a
- **Official status:** Clerk's docket.
- **Hazard:** robots-disallowed
- **Probe:** 89-R-99012-SCT order → `https://courts.ms.gov/appellatecourts/docket/sendPDF.php?f=700_779108.pdf&c=17875&a=N&s=2`
- **Evidence (2026-10-17):** Script: REFUSED robots.txt disallows /appellatecourts/docket/sendPDF.php (link from SCT10-15-2026 hand-down list).
- **Notes:** Order PDFs linked on hand-down lists (rules orders, some en banc orders) live here and are therefore unreadable; the list's disposition text is the readable record.

### `ms-coa-handdown` — Mississippi Court of Appeals — Hand Down Lists (by date)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Mississippi Court of Appeals · text: **fetch-and-quote** · official: official
- **Coverage:** One list per hand-down day (Tuesdays); observed 2010-01-05 and 2026 dates.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://courts.ms.gov/Images/HDList/COA{MM}-{DD}-{YYYY}.html`
  - Placeholders: As ms-sct-handdown, prefix COA; Court of Appeals hands down on Tuesdays. Opinion links resolve to /Images/Opinions/CO{id}.pdf.
  - Index: `https://courts.ms.gov/appellatecourts/coa/coa.php`
  - Navigation: COA decisions page is the same JavaScript calendar; build from date.
- **Automation:** WebFetch untested · shell ok · robots: /Images/ permitted
  - Day ZIP: Images/ZIPS/CourtOfAppeals/COA{YYYYMMDD}.ZIP.
- **Currency:** list heading — observed: "Mississippi Court of Appeals Hand Down List October 13, 2026"
- **Official status:** The Court's own hand-down list.
- **Hazard:** backslash relative links
- **Hazard:** need the hand-down date
- **Probe:** Harrison v. Harrison, No. 2025-CA-00913-COA (Miss. Ct. App. Oct. 13, 2026) → `https://courts.ms.gov/Images/HDList/COA10-13-2026.html` — expect: "Wiley Bryant Harrison v. Ellen Trainor Harrison; Lee Chancery Court"
- **Evidence (2026-10-17):** Script: 7,363 chars; '2025-CA-00913-COA Wiley Bryant Harrison v. Ellen Trainor Harrison'; link ..\Opinions\CO195485.pdf.

### `ms-opinion-pdfs` — Mississippi Supreme Court and Court of Appeals opinion PDFs

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Mississippi · text: **fetch-and-quote** · official: unknown
- **Coverage:** Opinions linked from hand-down lists (2000 list links Conv8477.pdf; 2026 CO19xxxx.pdf).
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.ms.gov/Images/Opinions/CO{id}.pdf`
  - Placeholders: {id} is opaque; take it from the hand-down list link for the docket.
  - Index: `https://courts.ms.gov/Images/HDList/SCT{MM}-{DD}-{YYYY}.html`
  - Navigation: hand-down list (SCT/COA by date) → docket link → PDF.
  - Read via: located on ms-sct-handdown / ms-coa-handdown; read here (script ok)
- **Automation:** WebFetch gated · shell ok · robots: /Images/ permitted
  - WebFetch: PROVENANCE_REQUIRED (approval prompt). Paragraphs numbered ¶1., ¶2. — pinpoint by ¶ as Mississippi courts do.
- **Currency:** caption block — observed: "DISPOSITION: REVERSED AND REMANDED - 10/15/2026"
- **Official status:** Slip opinions; caption 'IN THE SUPREME COURT OF MISSISSIPPI NO. 2025-CA-00269-SCT'; no statement of official status.
- **Hazard:** slip pagination only (So. 3d pages not in the PDF)
- **Hazard:** PDF may be replaced after rehearing (withdrawn and substituted opinions)
- **Probe:** Park Wind Apartments, LLC v. Mayze, No. 2025-CA-00269-SCT → `https://courts.ms.gov/Images/Opinions/CO196092.pdf` — expect: "Glenda Mayze’s knee was injured when she tried to avoid a puddled sidewalk"
- **Evidence (2026-10-17):** Script: 11 pp, 20,320 chars; 'NO. 2025-CA-00269-SCT'; '¶1. Glenda Mayze’s knee was injured'. COA CO195485.pdf: 'NO. 2025-CA-00913-COA'.

### `ms-sct-handdown` — Supreme Court of Mississippi — Hand Down Lists (by date)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Mississippi · text: **fetch-and-quote** · official: official
- **Coverage:** One HTML list per hand-down day (Thursdays) with docket, style, trial court, disposition, votes, opinion PDF links; also en banc orders incl. certiorari grants/denials and rehearing rulings. Observed 2000-01-06 through 2026-10-15 (2010, 2019 also); a 1998 URL returned a 190-char stub.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://courts.ms.gov/Images/HDList/SCT{MM}-{DD}-{YYYY}.html`
  - Placeholders: Zero-padded month and day (SCT10-15-2026.html). Supreme Court hands down on Thursdays; the date is the hand-down date, not the opinion's internal date. Opinion links are written with backslashes ('..%5COpinions%5CCO196092.pdf'): resolve to https://courts.ms.gov/Images/Opinions/CO{id}.pdf.
  - Index: `https://courts.ms.gov/appellatecourts/sc/scdecisions.php`
  - Navigation: scdecisions.php is a JavaScript calendar (no links to the script); build the list URL from the date instead.
- **Automation:** WebFetch gated · shell ok · robots: /Images/ not disallowed; /appellatecourts/docket/ and /search/ are
  - Lists observed for 10/15, 10/08, 10/01, 9/24/2026, 3/07/2019, 1/07/2010, 1/06/2000. Day ZIP of WordPerfect opinions: Images/ZIPS/SupremeCourt/SC{YYYYMMDD}.ZIP.
- **Currency:** list heading — observed: "Supreme Court of Mississippi Hand Down List October 15, 2026"
- **Official status:** The Court's own hand-down list; opinions are the slip opinions as handed down.
- **Hazard:** backslash relative links
- **Hazard:** order PDFs on the same list point to robots-disallowed /appellatecourts/docket/sendPDF.php
- **Hazard:** no finder by docket: need the hand-down date (or Justia)
- **Probe:** Park Wind Apartments, LLC v. Mayze, No. 2025-CA-00269-SCT (Miss. Oct. 15, 2026) → `https://courts.ms.gov/Images/HDList/SCT10-15-2026.html` — expect: "Park Wind Apartments, LLC v. Glenda Mayze; Hinds Circuit Court 1st District"
- **Evidence (2026-10-17):** Script: 7,139 chars; '2025-CA-00269-SCT Park Wind Apartments, LLC v. Glenda Mayze … Disposition: Reversed and Remanded.' 9 links.

### `ms-cases-justia` — Justia — Mississippi Supreme Court and Court of Appeals decisions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Year listings /cases/mississippi/supreme-court/{year}/ and /court-of-appeals/{year}/; case pages carry the full text and a cases.justia.com PDF.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/mississippi/{court}/{year}/{docket_lower}.html`
  - Placeholders: court = supreme-court | court-of-appeals; year = decision year (not docket year); docket lower-cased (2020-CA-00293-SCT → 2020-ca-00293-sct). Year listing shows dockets but some entries have no link.
  - Index: `https://law.justia.com/cases/mississippi/supreme-court/{year}/`
  - Navigation: build from docket + decision year; if the year is unknown, open the year listings.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (bot check)
  - Built COA URL passed WebFetch without approval prompt.
- **Currency:** decision date on page — observed: "October 13, 2026 (Harrison, posted same week)"
- **Official status:** Third-party copy of the slip opinions.
- **Hazard:** year segment is the decision year
- **Hazard:** shell blocked
- **Probe:** Weber v. Estate of Hill, No. 2020-CA-00293-SCT (Miss. 2021) → `https://law.justia.com/cases/mississippi/supreme-court/2021/2020-ca-00293-sct.html` — expect: "A Jones County jury returned a $4 million verdict in favor of"
- **Evidence (2026-10-17):** WebFetch: YES, 'A Jones County jury returned a $4 million verdict in favor of'; ¶ numbers through ¶81; not truncated. Built /court-of-appeals/2026/2025-ca-00913-coa.html: 'Wiley Harrison appeals from a final judgment'.
- **Notes:** Practical docket → opinion finder, since the Court's docket search is robots-disallowed.

## F. Subsequent history

### `ms-cert-handdown` — Certiorari and rehearing dispositions on Supreme Court hand-down lists

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Supreme Court of Mississippi · text: **fetch-and-quote** · official: official
- **Coverage:** EN BANC entries: 'Petition for Writ of Certiorari … is granted/denied/dismissed as untimely', with order date and votes; rehearing rulings on SCT and COA lists.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://courts.ms.gov/Images/HDList/SCT{MM}-{DD}-{YYYY}.html`
  - Placeholders: A cert petition from a Court of Appeals decision is docketed with the same year and number and case type 'CT' with suffix -SCT (observed: 2024-CT-01022-SCT, 2025-CT-00076-SCT; the COA original keeps its type, e.g. -KA-/-CA-…-COA — same-number mapping from memory). Scan the Thursday lists after the COA decision (M.R.A.P. 17: cert petition after rehearing denial).
  - Index: `https://courts.ms.gov/appellatecourts/sc/scdecisions.php`
  - Navigation: No docket search (robots). Scan SCT lists by date for '{year}-CT-{number}-SCT'; Justia SC year listings also carry -CT- opinions after grant.
- **Automation:** WebFetch gated · shell ok · robots: /Images/ permitted
  - Denials are on the lists (e.g. 10/01/2026 'Petition for Writ of Certiorari filed by David Allen Breland is denied').
- **Currency:** list heading — observed: "Hand Down List October 1, 2026"
- **Official status:** Court's hand-down list.
- **Hazard:** date-scan needed: findable by docket number only by scanning lists, or by party name on Justia
- **Hazard:** CT docket replaces COA suffix
- **Probe:** Breland v. State, No. 2024-CT-01022-SCT (cert. denied Sept. 24, 2026) → `https://courts.ms.gov/Images/HDList/SCT10-01-2026.html` — expect: "Petition for Writ of Certiorari filed by David Allen Breland is denied"
- **Evidence (2026-10-17):** Script grep: '2024-CT-01022-SCT David Allen Breland … is denied. To Deny: All Justices. Order entered 9/24/26.' Grants on 10/08 and 10/15/2026 lists.

## Not available (do not look for these again)

- **case_law** — Public-domain / vendor-neutral citation format: Opinions observed (2025-CA-00269-SCT, 2025-CA-00913-COA) carry only docket numbers and ¶ numbers; none adopted (memory). (2026-10-17)
- **statutes** — Government-hosted Mississippi Code text readable by either tool: Lexis container returns 0 chars; legislature hosts fail TLS verification. (2026-10-17)
- **case_law** — Plain-GET opinion/docket search on courts.ms.gov: robots.txt disallows /search/ and /appellatecourts/docket/; decisions pages are a JavaScript calendar. (2026-10-17)

## Corpus candidates (maintainers)

- `ms-rules-civil` — 231 pp, 467,917 chars; WebFetch gated and window far too small.
- `ms-rules-evidence` — 146 pp, 333,606 chars.
- `ms-rules-appellate` — 183 pp, 352,863 chars.
- `ms-rules-criminal` — 185 pp, 356,996 chars.
- `ms-rules-prof-conduct` — 143 pp, 361,479 chars.
- `ms-constitution-sos` — 193 pp, 368,794 chars, annotated; WebFetch gated.

## Open questions

- WebFetch untested on courts.ms.gov and sos.ms.gov: every attempt waited on the session's URL-approval prompt (PROVENANCE_REQUIRED). All those rows are script-verified; an independent pass should run WebFetch on them.
- Legislature hosts (legislature.ms.gov, billstatus.ls.state.ms.us) fail TLS verification from the sandbox: session-law route unestablished.
- Earliest hand-down list year: 2000-01-06 list exists with PDFs; a 1998 date returned a 190-char stub and a 1996 date a connection error — not resolved.
- Same-number mapping COA docket → {year}-CT-{number}-SCT is from memory; confirm on a known pair.
- Justia article-level code URLs (/article-{n}/section-…) inferred from the title/chapter index, not fetched.
- Constitution PDF cover says 'UPDATED MAY, 2022'; whether later amendments (e.g. 2025 ballot measures) are reflected not checked.
- WebFetch quota ran out once mid-session (session limit); 14 WebFetch calls used in total.
