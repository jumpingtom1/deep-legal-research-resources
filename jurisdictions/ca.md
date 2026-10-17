# California (CA) — free legal sources

_Generated from `data/ca.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes and constitution: the official Legislative Counsel site (leginfo.legislature.ca.gov) sits behind a Cloudflare challenge and failed every WebFetch, so the working routes are tier 2. california.public.law has constructible per-section URLs for all 29 codes (shell and WebFetch both work). Justia covers the codes and the constitution, reached by index navigation. Rules of Court: courts.ca.gov/cms/rules is constructible and fetchable. Case law: the courts.ca.gov opinion listings (120-day slip window plus an older-than-120-days archive) can be fetched, but the opinion PDFs redirect to www4.courts.ca.gov, which is Cloudflare-challenged and robots-refused to WebFetch. The Official Reports (LexisNexis) site is robots-disallowed and the docket system is robots/challenge-blocked. Justia opinion pages (Supreme Court from 1853, Courts of Appeal from 1897) are the readable text route, with slip pagination only. CCR: the official Westlaw host is blocked, and Cornell LII serves constructible CCR sections. Supreme Court weekly conference-result PDFs on supreme.courts.ca.gov are fetchable and give review grants and denials by docket number.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of California | `cal (unverified)` | Cal. | Cal., Cal. 2d, Cal. 3d, Cal. 4th, Cal. 5th, Cal. Rptr., Cal. Rptr. 2d, Cal. Rptr. 3d, P., P.2d, P.3d | — |
| California Courts of Appeal (Districts 1-6) | `calctapp (unverified)` | Cal. Ct. App. | Cal. App., Cal. App. 2d, Cal. App. 3d, Cal. App. 4th, Cal. App. 5th, Cal. Rptr., Cal. Rptr. 2d, Cal. Rptr. 3d | — |
| Appellate Division of the Superior Court | `calappdeptsuperct (unverified)` | Cal. App. Dep't Super. Ct. | Cal. App. Supp., Cal. App. 2d Supp., Cal. App. 3d Supp., Cal. App. 4th Supp., Cal. App. 5th Supp., Cal. Rptr. 3d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| California codes (Bluebook, California Style Manual, prose) | `Cal. Civ. Code § 1714`; `Cal. Civ. Proc. Code § 437c`; `Code Civ. Proc., § 437c`; `Civil Code section 1714`; `Pen. Code, § 187`; `Bus. & Prof. Code § 17200`; `Gov. Code, § 12940`; `Welf. & Inst. Code, § 5150`; `section 1714 of the Civil Code`; `section 17200 of the Business and Professions Code` | `ca-codes-leginfo` → `ca-codes-publiclaw` → `ca-codes-justia` |
| California Constitution | `Cal. Const. art. I, § 1`; `Cal. Const., art. I, § 7`; `article I, section 1 of the California Constitution`; `Cal. Const., art. XIII A, § 1` | `ca-const-leginfo` → `ca-const-justia` |
| California Rules of Court | `Cal. Rules of Court, rule 8.500`; `Cal. R. Ct. 3.1350`; `rule 8.1115 of the California Rules of Court` | `ca-rules-court` |
| California Code of Regulations | `Cal. Code Regs., tit. 8, § 3203`; `Cal. Code Regs. tit. 2, § 11009`; `8 CCR 3203` | `ca-ccr-westlaw` → `ca-ccr-lii` |
| California reporters | `Rowland v. Christian (1968) 69 Cal.2d 108`; `105 Cal.App.5th 913`; `71 Cal. Rptr. 3d 1`; `12 Cal.App.5th Supp. 1` | `ca-opinions-courts` → `ca-opinions-justia` → `ca-official-reports-lexis` |

Regexes (case-insensitive):

- California codes (Bluebook, California Style Manual, prose): `(?<!Tex\.\s)(?<!Texas\s)(?<!Tex\s)(?<!La\.\s)(?<!V\.T\.C\.A\.\s)(?:Cal(?:ifornia)?\.?\s+)?(?P<code>Civ(?:il)?\.?\s+Proc(?:\.|edure)?(?:\s+Code)?|Code\s+(?:of\s+)?Civ(?:il|\.)?\s+Proc(?:\.|edure)?|Civ(?:il|\.)|Pen(?:al|\.)|Evid(?:ence|\.)|Bus(?:iness|\.)\s*(?:&|and)\s*Prof(?:essions|\.)|Gov(?:ernment|\.|'t)|Lab(?:or|\.)|Veh(?:icle|\.)|Fam(?:ily|\.)|Prob(?:ate|\.)|Corp(?:orations|\.)|Com(?:mercial|\.)|Health\s*(?:&|and)\s*Saf(?:ety|\.)|Ins(?:urance|\.)|Welf(?:are|\.)\s*(?:&|and)\s*Inst(?:itutions|\.)|Educ?(?:ation|\.)|Elec(?:tions|\.)|Fin(?:ancial|\.)|Fish\s*(?:&|and)\s*G(?:ame|\.)|Food\s*(?:&|and)\s*Agric?(?:ultural|\.)|Harb(?:ors|\.)\s*(?:&|and)\s*Nav(?:igation|\.)|Mil(?:itary|\.)\s*(?:&|and)\s*Vet(?:erans|\.)|Pub(?:lic|\.)\s*Cont(?:ract|\.)|Pub(?:lic|\.)\s*Res(?:ources|\.)|Pub(?:lic|\.)\s*Util(?:ities|\.)|Rev(?:enue|\.)\s*(?:&|and)\s*Tax(?:ation|\.)|Sts?(?:reets|\.)\s*(?:&|and)\s*High(?:ways|\.)|Unemp(?:loyment|\.)\s*Ins(?:urance|\.)|Water|Wat\.)(?:\s*Code)?,?\s*(?:§§?|sec(?:tion|\.)s?)\s*(?P<section>\d+(?:\.\d+)*[a-z]?)|(?:sec(?:tion|\.)s?|§§?)\s*(?P<section_p>\d+(?:\.\d+)*[a-z]?)(?:,?\s*subd(?:ivision|\.)\s*\([a-z0-9]+\))?\s+of\s+the\s+(?:California\s+)?(?P<code_p>Civ(?:il)?\.?\s+Proc(?:\.|edure)?(?:\s+Code)?|Code\s+(?:of\s+)?Civ(?:il|\.)?\s+Proc(?:\.|edure)?|Civ(?:il|\.)|Pen(?:al|\.)|Evid(?:ence|\.)|Bus(?:iness|\.)\s*(?:&|and)\s*Prof(?:essions|\.)|Gov(?:ernment|\.|'t)|Lab(?:or|\.)|Veh(?:icle|\.)|Fam(?:ily|\.)|Prob(?:ate|\.)|Corp(?:orations|\.)|Com(?:mercial|\.)|Health\s*(?:&|and)\s*Saf(?:ety|\.)|Ins(?:urance|\.)|Welf(?:are|\.)\s*(?:&|and)\s*Inst(?:itutions|\.)|Educ?(?:ation|\.)|Elec(?:tions|\.)|Fin(?:ancial|\.)|Fish\s*(?:&|and)\s*G(?:ame|\.)|Food\s*(?:&|and)\s*Agric?(?:ultural|\.)|Harb(?:ors|\.)\s*(?:&|and)\s*Nav(?:igation|\.)|Mil(?:itary|\.)\s*(?:&|and)\s*Vet(?:erans|\.)|Pub(?:lic|\.)\s*Cont(?:ract|\.)|Pub(?:lic|\.)\s*Res(?:ources|\.)|Pub(?:lic|\.)\s*Util(?:ities|\.)|Rev(?:enue|\.)\s*(?:&|and)\s*Tax(?:ation|\.)|Sts?(?:reets|\.)\s*(?:&|and)\s*High(?:ways|\.)|Unemp(?:loyment|\.)\s*Ins(?:urance|\.)|Water|Wat\.)(?:\s+Code)?(?!\s+of\s+(?!Civil)(?:Texas|Louisiana))`
- California Constitution: `Cal(?:ifornia)?\.?\s+Const(?:itution|\.)?,?\s+art(?:icle|\.)?\s+(?P<article>[IVXL]+(?:\s?[A-D])?),?\s*(?:§|sec(?:tion|\.)?)\s*(?P<section>\d+(?:\.\d+)?)|art(?:icle|\.)?\s+(?P<article2>[IVXL]+(?:\s?[A-D])?),?\s*(?:§|sec(?:tion|\.)?)\s*(?P<section2>\d+(?:\.\d+)?)\s+of\s+the\s+Cal(?:ifornia)?\.?\s+Const(?:itution)?`
- California Rules of Court: `(?:Cal(?:ifornia)?\.?\s+R(?:ules|\.)\s+(?:of\s+)?C(?:our)?t\.?,?\s*(?:rule\s*)?|rule\s+)(?P<title>[1-9]|10)\.(?P<rule>\d+(?:\.\d+)?)(?!\d)(?!\s+of\s+the\s+(?:Federal|Fed\.))(?!\s*(?:of\s+the\s+)?(?:Fed|FRCP|FRE|FRAP))`
- California Code of Regulations: `(?:Cal(?:ifornia)?\.?\s+Code\s+(?:of\s+)?Regs?(?:ulations|\.)?,?\s*tit(?:le|\.)\s*(?P<title>\d+),?\s*§\s*(?P<section>[\d.]+[A-Za-z]?)|(?P<title2>\d+)\s+C\.?C\.?R\.?\s*§?\s*(?P<section2>[\d.]+[A-Za-z]?))`
- California reporters: `(?P<volume>\d+)\s+(?P<reporter>Cal\.\s?(?:App\.\s?)?(?:[2-5](?:d|th)\s?)?(?:Supp\.\s?)?|Cal\.\s?Rptr\.\s?(?:[23]d)?)\s*(?P<page>\d+)`

There is no public-domain citation format. California Style Manual cites put the year in parentheses before the volume and omit spaces ("69 Cal.2d 108"); Bluebook adds spaces ("69 Cal. 2d 108"). Docket prefixes: S = Supreme Court; A, B, C, D, E, F, G, H = Courts of Appeal Districts 1, 2, 3, 4/Div1, 4/Div2, 5, 4/Div3, 6. An M suffix marks a modification; an N suffix appears on archive file names. The courtlistener_id values come from memory and have not been checked against CourtListener. Routing caution: bare code names (Penal Code, Civil Code, Government Code) and bare 'rule N.N' are shared with other states and the federal rules; the regexes exclude Texas/Louisiana prefixes and 'of the Federal Rules', but route here only when the query or citation context is Californian.

## A. Statutes / code

### `ca-codes-leginfo` — California Law (codes)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · California Legislative Counsel · text: **link-only** · official: unknown
- **Coverage:** All 29 California codes, current text
- **Access:** `constructible` · format html
  - Pattern: `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode={lawCode}&sectionNum={section}`
  - Placeholders: From memory, not verified. lawCode: BPC Bus&Prof, CIV Civil, CCP Civ Proc, COM Commercial, CORP Corporations, EDC Education, ELEC Elections, EVID Evidence, FAM Family, FIN Financial, FGC Fish&Game, FAC Food&Ag, GOV Government, HNC Harbors&Nav, HSC Health&Safety, INS Insurance, LAB Labor, MVC Military&Veterans, PEN Penal, PROB Probate, PCC Public Contract, PRC Public Resources, PUC Public Utilities, RTC Rev&Tax, SHC Streets&Highways, UIC Unemployment Ins, VEH Vehicle, WAT Water, WIC Welf&Inst. Justia's code-{slug} paths use the same abbreviations in lower case, which supports the table. sectionNum may need a trailing period ("1714.").
  - Index: `https://leginfo.legislature.ca.gov/faces/codes.xhtml`
- **Automation:** WebFetch blocked · shell blocked-challenge · robots: unreadable: the shell got 403 with cf-mitigated: challenge, and WebFetch returned CLIENT_ERROR
  - The home page fetched through WebFetch once. Every codes_displaySection, codes.xhtml and faqs.xhtml fetch returned CLIENT_ERROR. Treat the host as blocked: link to it, do not quote from it.
- **Currency:** not observed
- **Official status:** Not confirmed. The FAQ page (leginfo.legislature.ca.gov/faces/faqs.xhtml) was unreachable.
- **Hazard:** Cloudflare challenge
- **Hazard:** JSF pages that may need a session
- **Probe:** Cal. Civ. Code § 1714 → `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1714` — expect: "Everyone is responsible, not only for the result of his"
- **Evidence (2026-10-16):** shell: HTTP 403 with cf-mitigated: challenge. WebFetch: CLIENT_ERROR on 6 code and FAQ URLs. The home page alone returned content. | Re-confirmed blocked 2026-10-16: WebFetch CLIENT_ERROR on codes_displaySection CIV 1714
- **Notes:** This is the citation target to link. Read the text from ca-codes-publiclaw instead.

### `ca-codes-justia` — Justia California Code

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** 29 codes. The current edition is labelled 2025; archived editions run from 2005 to 2024.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Placeholders: Section URLs follow /codes/california/code-{abbr}/{division-N}/{part-N}/.../section-{sec with dots as hyphens}/. The hierarchy segments cannot be derived from a citation.
  - Index: `https://law.justia.com/codes/california/`
  - Navigation: From /codes/california/code-{abbr}/ (abbr = lower-case lawCode: civ, ccp, pen, …) follow whichever child link's section range contains the section — division, part, title, chapter, article, as present (the Penal Code starts at parts, not divisions) — until a page lists individual section links; then open the section. Expect 3-5 hops. Title pages list chapters, never sections.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unread: the shell got a Cloudflare challenge (403) on law.justia.com/robots.txt. WebFetch was not refused robots-wise.
- **Currency:** page heading — observed: "2025 California Code"
- **Official status:** The page disclaimer says "These codes may not be the most recent version... Please check official sources." https://law.justia.com/codes/california/2025/
- **Hazard:** edition is a year behind
- **Hazard:** deep hierarchy needs 3-5 hops
- **Probe:** Cal. Civ. Code § 1714 → `https://law.justia.com/codes/california/code-civ/division-3/part-3/section-1714/` — expect: "Everyone is responsible, not only for the result of his"
- **Evidence (2026-10-16):** WebFetch: YES, body (a)-(d)(2), labelled "2025 California Code". Reached by navigating code-civ -> division-3 -> part-3. | Independent check 2026-10-16: YES: 'Everyone is responsible, not only for the result of his'; '2025 California Code'; not truncated; second citation Pen. Code, § 187 ok

### `ca-codes-publiclaw` — California.Public.Law codes

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Public.Law · text: **fetch-and-quote** · official: unofficial
- **Coverage:** All 29 codes. The constitution is not available (/california_constitution and /constitution both returned 404).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://california.public.law/codes/{code_slug}_section_{section}`
  - Placeholders: code_slug is the code's full name in lower case with underscores: business_and_professions_code, civil_code, code_of_civil_procedure, commercial_code, corporations_code, education_code, elections_code, evidence_code, family_code, financial_code, fish_and_game_code, food_and_agricultural_code, government_code, harbors_and_navigation_code, health_and_safety_code, insurance_code, labor_code, military_and_veterans_code, penal_code, probate_code, public_contract_code, public_resources_code, public_utilities_code, revenue_and_taxation_code, streets_and_highways_code, unemployment_insurance_code, vehicle_code, water_code, welfare_and_institutions_code. Keep dotted sections as written (civil_code_section_1798.100) and letter suffixes in lower case (437c). Legacy slugs such as ca_civ_code_section_1714 return 301 to the canonical slug.
  - Index: `https://california.public.law/codes`
- **Automation:** WebFetch ok · shell ok · robots: User-agent * disallows only /admin /api /data /demo /images /users
  - Page titles carry the edition year, for example "California Penal Code section 187 (2025)".
- **Currency:** on the section page (badge plus Verified date) and on each code's index page (Refreshed). Disclose the 'Verified: <date>' badge as the currency string; the '(updated …; accessed …)' line in the source credit is not currency. — observed: "Up to date; Verified: Oct. 12, 2026 (codes index: Updated October 5, 2026)"
- **Official status:** The index makes no claim to be official. Page metadata names the author as "Cal. Legislature". https://california.public.law/codes
- **Hazard:** edition label in the page title (2025) can lag the verified date
- **Hazard:** per-code 'Refreshed' date (Civil Code 2025-05-12) can disagree with the section badge
- **Probe:** Cal. Civ. Code § 1714 → `https://california.public.law/codes/civil_code_section_1714` — expect: "Everyone is responsible, not only for the result of his"
- **Evidence (2026-10-16):** WebFetch returned the full text of § 1714 subd. (a)-(d)(2), not truncated. A second probe, code_of_civil_procedure_section_437c, returned through subd. (u), not truncated. Shell returned 200 for Penal § 187, Evid § 1200, Veh § 23152, B&P § 17200, Gov § 12940 and W&I § 5150. | Independent check 2026-10-16: YES: 'Everyone is responsible, not only for the result of his'; 'Verified: Oct. 12, 2026'; full; second citation Health & Saf. Code, § 11350 ok

## B. Constitution

### `ca-const-leginfo` — California Constitution (leginfo)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · California Legislative Counsel · text: **link-only** · official: unknown
- **Coverage:** Current constitution
- **Access:** `constructible` · format html
  - Pattern: `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CONS&article={article}&sectionNum={section}.`
  - Placeholders: From memory and not verified. article is the Roman numeral, and sectionNum has a trailing period.
  - Index: `https://leginfo.legislature.ca.gov/faces/codesTOCSelected.xhtml?tocCode=CONS`
- **Automation:** WebFetch blocked · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - Same host as ca-codes-leginfo
- **Currency:** not observed
- **Official status:** Not reachable
- **Hazard:** Cloudflare challenge
- **Probe:** Cal. Const. art. I, § 1 → `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1.&lawCode=CONS&article=I` — expect: "All people are by nature free and independent and have"
- **Evidence (2026-10-16):** WebFetch CLIENT_ERROR. The shell host returns 403 with cf-mitigated: challenge. | Re-confirmed blocked 2026-10-16: WebFetch CLIENT_ERROR on lawCode=CONS article=I sectionNum=1.

### `ca-const-justia` — Justia California Constitution

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Current constitution, one section per page
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/california/article-{article_roman_lower}/section-{section}/`
  - Placeholders: article is the Roman numeral in lower case (I -> i). section is the section number. Letter-suffixed articles (XIII A etc.) are unverified: use the index for those.
  - Index: `https://law.justia.com/constitution/california/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unread (Cloudflare challenge on shell)
  - Article index pages list sections only. The text is on the section pages.
- **Currency:** none stated. Only the amendment history note. — observed: "Sec. 1 added Nov. 5, 1974, by Proposition 7."
- **Official status:** Disclaimer: "This Constitution may not be the most recent version."
- **Hazard:** no edition date
- **Hazard:** article pages are TOC only
- **Probe:** Cal. Const. art. I, § 1 → `https://law.justia.com/constitution/california/article-i/section-1/` — expect: "All people are by nature free and independent and have"
- **Evidence (2026-10-16):** WebFetch: YES, the body begins with the expected words. The article-i index page holds no body text. | Independent check 2026-10-16: YES: 'All people are by nature free and independent and have'; '(Sec. 1 added Nov. 5, 1974, by Proposition 7...)'; second citation Cal. Const., art. IV, § 8 ok
- **Notes:** Only one article/section was probed. The handling of articles with letter suffixes (XIII A etc.) is unverified.

## C. Court rules

### `ca-local-rules` — Superior court local rules index

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Judicial Council of California · text: **link-only** · official: unknown
- **Coverage:** Local rules of the 58 superior courts. The index shows each set's effective date.
- **Read via (in order):** **fetch tool**
- **Access:** `link-only` · format html
  - Index: `https://courts.ca.gov/forms-rules/rules-court/local-rules`
  - Navigation: Index -> county link -> that court's local-rules page (hosts and formats vary, mostly PDF)
- **Automation:** WebFetch ok · shell untested · robots: courts.ca.gov: allowed. County hosts were not checked.
- **Currency:** per county entry — observed: "Alameda County (Eff. July 1, 2026)"
- **Official status:** The index links to each county court's own site
- **Hazard:** county hosts vary; some are http-only (e.g. amadorcourt.org)
- **Probe:**  → `https://courts.ca.gov/forms-rules/rules-court/local-rules` — expect: "Alameda County"
- **Evidence (2026-10-16):** WebFetch listed county entries with effective dates and links (Alameda, Alpine, Amador...) | Independent check 2026-10-16: YES: 'Alameda County (Eff. July 1, 2026)', then Alpine, Amador
- **Notes:** Only the index was verified. No county rule text was fetched.

### `ca-rules-court` — California Rules of Court

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Judicial Council of California · text: **fetch-and-quote** · official: unknown
- **Coverage:** Titles 1-10 plus the Standards of Judicial Administration, 2026 edition. The Evidence Code and Code of Civil Procedure are statutes (see ca-codes-*).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://courts.ca.gov/cms/rules/index/{title_word}/rule{title}_{rule}`
  - Placeholders: title_word: one, two, three, four, five, seven, eight, nine or ten, from the digit before the dot. Replace the dot with an underscore: 8.500 -> eight/rule8_500, 3.1350 -> three/rule3_1350. Standards: index/standards. www.courts.ca.gov also works.
  - Index: `https://courts.ca.gov/rules-forms/rules-court`
- **Automation:** WebFetch ok · shell ok · robots: Drupal default. Disallows /core/, /profiles/, /search*, /cjer and a few others. /cms/rules is allowed.
  - Whole-title PDFs exist (courts.ca.gov/system/files?file=file/roc-title-8_0.pdf, etc.). WebFetch truncated the Title 8 PDF. Use the per-rule pages.
- **Currency:** page header, and the title index — observed: "California Rules of Court 2026 (index: Current as of July 1, 2025)"
- **Official status:** The rules index page (https://courts.ca.gov/rules-forms/rules-court) makes no statement about official status. The Judicial Council adopts the rules.
- **Hazard:** title index currency string lags the page edition
- **Hazard:** PDF file names carry _N suffixes and are not stable
- **Probe:** Cal. Rules of Court, rule 8.500 → `https://www.courts.ca.gov/cms/rules/index/eight/rule8_500` — expect: "A party may file a petition in the Supreme Court"
- **Evidence (2026-10-16):** WebFetch: YES, (a)-(g) plus history, not truncated. A second probe, rule 3.1350 (courts.ca.gov/cms/rules/index/three/rule3_1350), also returned YES. | Independent check 2026-10-16: Body present, 'California Rules of Court 2026', (a)-(g) full; expect string not contiguous; second citation Cal. Rules of Court, rule 2.111 ok

## D. Administrative code

### `ca-ccr-westlaw` — California Code of Regulations (official online)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Office of Administrative Law, via Thomson Reuters (Barclays) · text: **link-only** · official: official
- **Coverage:** Full CCR
- **Access:** `link-only` · format html
  - Index: `https://govt.westlaw.com/calregs/Index?transitionType=Default&contextData=%28sc.Default%29`
- **Automation:** WebFetch blocked · shell blocked-challenge · robots: shell got 403 on govt.westlaw.com/robots.txt
  - WebFetch returned SITE_BLOCKED
- **Currency:** not observed
- **Official status:** OAL says it contracts with Barclays/Thomson Reuters to provide a free online version of the Official CCR. https://oal.ca.gov/publications/ccr/
- **Hazard:** blocked
- **Probe:**  → `https://govt.westlaw.com/calregs/Index`
- **Evidence (2026-10-16):** WebFetch: SITE_BLOCKED (Access to this website has been blocked). Shell: 403 with Cf-Mitigated: challenge. | Re-confirmed blocked 2026-10-16: WebFetch SITE_BLOCKED
- **Notes:** Cite and link to this host. Read the text from ca-ccr-lii.

### `ca-ccr-lii` — LII California Code of Regulations

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Cornell Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** CCR titles 1-28 (index lists title-1..). LII keeps 2 versions.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/california/{title}-CCR-{section}`
  - Placeholders: title is the CCR title number and section is as cited (8-CCR-3203, 2-CCR-11009). The alternate form Cal-Code-Regs-Tit-8-SS-3203 returns 200 but has no body text. Do not use it.
  - Index: `https://www.law.cornell.edu/regulations/california`
  - Navigation: Fallback: title-N -> division-N -> chapter-N -> subchapter -> group -> article -> section link
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay: 10. Disallows /search/, /user/ and admin paths. /regulations is allowed.
  - Respect the 10 s crawl delay
- **Currency:** version note near the top. The history notes cite the Register. — observed: "State regulations are updated quarterly; we currently have two versions available."
- **Official status:** LII page. There is no official claim and no Westlaw attribution.
- **Hazard:** wrong URL form returns 200 with no body (soft 404)
- **Hazard:** quarterly lag
- **Probe:** Cal. Code Regs., tit. 8, § 3203 → `https://www.law.cornell.edu/regulations/california/8-CCR-3203` — expect: "(a) Effective July 1, 1991, every employer shall establish, implement"
- **Evidence (2026-10-16):** WebFetch: YES, (a)-(c)(7) plus notes, not truncated. Shell: 2-CCR-11009 returned 200 with the title 'Principles of Employment Discrimination'. | Independent check 2026-10-16: YES: '(a) Effective July 1, 1991, every employer shall establish, implement'; quarterly-version note; second citation Cal. Code Regs., tit. 22, § 72527 ok

## D. Administrative register

### `ca-notice-register` — California Regulatory Notice Register

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Office of Administrative Law · text: **fetch-and-quote** · official: official
- **Coverage:** Online issues from January 1, 2018 to date, weekly
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Issue PDFs follow https://oal.ca.gov/wp-content/uploads/sites/166/{YYYY}/{MM}/{YYYY}-Notice-Register-No.-{NN}-Z-{Month}-{D}-{YYYY}.pdf, but the slugs vary. Use the index.
  - Index: `https://oal.ca.gov/california_regulatory_notice_online/`
  - Navigation: Index -> monthly page (e.g. /august-2026-california-regulatory-notice-registers/) -> issue PDF
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay: 10. Disallows /wp-admin/.
  - Six of ten 2026 month links on the index are WordPress preview URLs (?page_id=…&preview=true); follow them from the index, never construct.
- **Currency:** issue title — observed: "Number 33-Z, August 14, 2026"
- **Official status:** Published by OAL, the agency responsible for it
- **Hazard:** unstable month-page slugs; file names vary (one carries a '-1' suffix) — follow links, never construct
- **Probe:**  → `https://oal.ca.gov/august-2026-california-regulatory-notice-registers/` — expect: "2026-Notice-Register-No.-32-Z-August-7-2026.pdf"
- **Evidence (2026-10-16):** WebFetch listed the issue PDFs No. 32-Z (Aug 7) and 33-Z (Aug 14) with their URLs | Independent check 2026-10-16: YES: 32-Z Aug 7 PDF linked, plus 33-Z, 34-Z, 35-Z; second citation Notice Register 2026, No. 29-Z (July 17, 2026) ok
- **Notes:** Listing verified; an issue PDF (29-Z, July 17, 2026) was read in full by the independent check.

## E. Case law

### `ca-official-reports-lexis` — California Official Reports public access (LexisNexis)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · LexisNexis under contract with the Judicial Council · text: **link-only** · official: official
- **Coverage:** Published opinions 1850 to present, with official pagination
- **Access:** `link-only` · format html
  - Index: `https://www.lexisnexis.com/clients/CACourts/`
  - Navigation: redirects to advance.lexis.com
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.lexisnexis.com/robots.txt: User-agent * Disallow: /clients/
  - WebFetch returned ROBOTS_DISALLOWED
- **Currency:** not observed
- **Official status:** The courts.ca.gov listing describes "Official Reports Opinions (Searchable 1850-Present)" as a no-fee LexisNexis service that reflects post-filing corrections
- **Hazard:** robots-disallowed
- **Probe:**  → `https://www.lexisnexis.com/clients/CACourts/`
- **Evidence (2026-10-16):** WebFetch ROBOTS_DISALLOWED. robots.txt Disallow: /clients/. The shell got 301 to advance.lexis.com (not followed). | Re-confirmed blocked 2026-10-16: WebFetch ROBOTS_DISALLOWED
- **Notes:** This is the only free source of official pagination, and automation cannot reach it.

### `ca-opinions-courts` — California appellate slip opinions (Judicial Branch)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Judicial Council of California · text: **link-only** · official: unofficial
- **Coverage:** Supreme Court, Courts of Appeal (all 6 districts and divisions) and the Appellate Division. Published and unpublished opinions from the last 120 days. Older published opinions: /opinions/published-opinions-older-120-days (8+ pages of archive). Review-granted lists.
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.ca.gov/opinions/documents/{docket}.PDF (published, 120-day window); /opinions/nonpub/{docket}.PDF (unpublished); /opinions/archive/{docket}.PDF (older)`
  - Placeholders: The PDF URLs are constructible from the docket number, but every one 301-redirects to www4.courts.ca.gov, which is blocked (see automation). Listing filters: ?field_opinion_source_target_id=103 (Supreme Court; 100 1st Dist, 102 2nd, 107 3rd, 106 4th/1, 98 4th/2, 101 4th/3, 99 5th, 105 6th, 104 Appellate Division) and &field_case_number_plain_value={docket}. Both were confirmed with the shell.
  - Index: `https://courts.ca.gov/opinions`
  - Navigation: publishedcitable-opinions or unpublishednon-citable-opinions -> filter by court/docket -> PDF link. Older: published-opinions-older-120-days (each row links to the PDF and an appellatecases docket).
- **Automation:** WebFetch blocked · shell ok · robots: courts.ca.gov: Drupal default, listings allowed. www4.courts.ca.gov (PDF host): Cloudflare challenge on robots.txt in the shell, and WebFetch returns ROBOTS_DISALLOWED.
  - WebFetch reads the listing pages fine. The shell downloaded F089182.PDF (200, application/pdf) after the redirect. The WebFetch refusal means the skill cannot read the PDFs. Some archive links 404 (B340734, A170747).
- **Currency:** listing page — observed: "Slip opinions from the last 120 days are posted together on this page"
- **Official status:** The listing page says slip opinions are "as-filed versions" and do not reflect Official Reports corrections. https://courts.ca.gov/opinions/publishedcitable-opinions
- **Hazard:** PDF host refuses WebFetch (ROBOTS_DISALLOWED)
- **Hazard:** slip pagination only
- **Hazard:** 120-day window; unpublished opinions vanish from the listing
- **Hazard:** some archive links 404
- **Probe:** San Joaquin Facilities Management, Inc. v. Dept. of Conservation, F089182 (Cal. Ct. App. 5th Dist. 2026) → `https://www.courts.ca.gov/opinions/documents/F089182.PDF` — expect: "A byproduct of oil production is"
- **Evidence (2026-10-16):** WebFetch ROBOTS_DISALLOWED on www.courts.ca.gov/.../F089182.PDF, on courts.ca.gov/... and on archive/A170226.PDF. Listing pages: WebFetch OK (Oct 15, 2026 entries). The shell PDF opens 'Filed 9/17/26; Certified for Publication 10/15/26'. | Re-confirmed blocked 2026-10-16: WebFetch ROBOTS_DISALLOWED on F089182.PDF; listing page fetched fine (Oct 15, 2026 entries)
- **Notes:** Use it to locate opinions (docket and date to PDF link) and link to them. Read the text from ca-opinions-justia.

### `ca-opinions-justia` — Justia California case law

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1853 to 2026; Courts of Appeal 1897 to 2026 (sparse in early years)
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/california/{court}/{year}/{docket_lower}.html`
  - Placeholders: court is supreme-court or court-of-appeal. year is Justia's 'Date Decided' year, which for an opinion certified for publication after filing is the certification date (B339467: filed 9/18/26, dated 10/13/26) — near January try both years, or use the year index. docket is lower case (s287946, a172398). The PDF is at cases.justia.com/california/{court}/{year}-{docket}.pdf?ts=... (the ts is not constructible). The year index pages list older cases, which may use other slugs.
  - Index: `https://law.justia.com/cases/california/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unread (Cloudflare challenge on shell)
- **Currency:** none; decision date shown — observed: "decision date August 6, 2026"
- **Official status:** Third-party republication of slip opinions. AI summaries on the page are flagged as possibly inaccurate.
- **Hazard:** slip pagination only, no Cal.5th/Cal.App.5th cite or star paging
- **Hazard:** AI summary on page
- **Hazard:** slug pattern for pre-modern cases unverified
- **Probe:** Gorobets v. Jaguar Land Rover North America, LLC, S287946 (Cal. 2026) → `https://law.justia.com/cases/california/supreme-court/2026/s287946.html` — expect: "Generally, the right to recover costs at the conclusion of"
- **Evidence (2026-10-16):** WebFetch: full text through the disposition, not truncated. A second probe, court-of-appeal/2026/a172398.html (In re Marriage of Trousset), was also full text. | Independent check 2026-10-16: YES: 'Generally, the right to recover costs at the conclusion of'; date 'August 6, 2026'; no Cal.5th; second citation McInerney v. Regents of the Univ. of California, B339467 (Cal. Ct. App. 2d Dist., Oct. 13, 2026) ok

## F. Subsequent history

### `ca-appellate-dockets` — Appellate Courts Case Information

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Judicial Council of California · text: **link-only** · official: official
- **Coverage:** Dockets for the Supreme Court and the Courts of Appeal
- **Access:** `link-only` · format html
  - Pattern: `https://appellatecases.courtinfo.ca.gov/search/searchResults.cfm?dist={dist}&search=number&useSession=0&query_caseNumber={docket}`
  - Placeholders: dist: 0 Supreme Court, 1-6 Court of Appeal district. The pattern was taken from links on the courts.ca.gov opinion listings.
  - Index: `https://appellatecases.courtinfo.ca.gov/`
- **Automation:** WebFetch blocked · shell blocked-challenge · robots: unreadable (403 cf-mitigated: challenge)
  - WebFetch returned ROBOTS_DISALLOWED
- **Currency:** not observed
- **Official status:** The conference-results PDF says the docket shows the "full and official result"
- **Hazard:** blocked
- **Probe:** S287285 → `https://appellatecases.courtinfo.ca.gov/search/searchResults.cfm?dist=0&search=number&useSession=0&query_caseNumber=S287285`
- **Evidence (2026-10-16):** WebFetch ROBOTS_DISALLOWED. Shell robots.txt: 403 with cf-mitigated: challenge. | Re-confirmed blocked 2026-10-16: WebFetch ROBOTS_DISALLOWED
- **Notes:** Give the user the link only.

### `ca-review-granted-lists` — Published / unpublished opinions: review granted

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Judicial Council of California · text: **link-only** · official: unknown
- **Coverage:** Court of Appeal opinions for which the Supreme Court has granted review
- **Access:** `index-anchored` · format html
  - Index: `https://courts.ca.gov/opinions/published-opinions-review-granted`
  - Navigation: Listing rows link to the opinion PDF (blocked host) and the appellatecases docket (blocked)
- **Automation:** WebFetch untested · shell ok · robots: courts.ca.gov allowed
  - The shell returned 200 with rows linking to appellatecases dockets (e.g. A170385).
- **Currency:** not observed
- **Official status:** Listing page on courts.ca.gov
- **Probe:**  → `https://courts.ca.gov/opinions/published-opinions-review-granted` — expect: "Published Opinions: Review Granted"
- **Evidence (2026-10-16):** Shell 200. Page title 'Published Opinions: Review Granted'. Rows link to appellatecases search URLs.
- **Notes:** Shell-verified only. WebFetch was not run.

### `ca-sc-conference-results` — Supreme Court weekly conference results

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Supreme Court of California · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Weekly petition-conference results, 2024 to 2026 per the year list. Covers review grants and denials, depublication and rehearing. Lists case #, Court of Appeal #, and action.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Placeholders: File names vary ("conference results - 093026 - R.pdf", "conference results 092326 - R.pdf", "..._0.pdf"; older ones crMMDDYY.pdf). Do not construct them.
  - Index: `https://supreme.courts.ca.gov/case-information/weekly-conference-results`
  - Navigation: Index (by year) -> weekly PDF -> search the PDF text for the S docket number or the Court of Appeal docket number
- **Automation:** WebFetch ok · shell ok · robots: supreme.courts.ca.gov: User-agent * Disallow /profiles/ (Drupal default)
  - Posted Thursday mornings
- **Currency:** PDF heading — observed: "Results from the petition conference of 7/15/2026"
- **Official status:** The PDF says the Results column is abbreviated and points to the docket for the full and official result
- **Hazard:** file-name drift
- **Hazard:** finding a docket means scanning weekly PDFs; there is no search by docket
- **Hazard:** Action type and result are separate columns (e.g. 'Petition for Review' | 'Granted'); results include variants such as 'Granted and Held' and 'Denied'. Match the S or Court of Appeal docket number, then read the row's result column.
- **Probe:** Marriage of Bowman, S296637 (B331924) → `https://supreme.courts.ca.gov/sites/default/files/supremecourt/default/documents/conference%20results%20-%20071526%20-%20R.pdf` — expect: "S296637 B331924 Petition for Review Granted"
- **Evidence (2026-10-16):** WebFetch read the heading and rows (S287285/C102071 Opinion Modification: Denied; S296637/B331924 Petition for Review: Granted). The index listed results through Sept 30, 2026. | Independent check 2026-10-16: Heading 'Results from the petition conference of 7/15/2026'; S296637 B331924 Petition for Review | Granted; second citation People v. Hernandez, S298093 (B352278), conference of 9/30/2026 ok

## Not available (do not look for these again)

- **constitution** — California Constitution on california.public.law: /california_constitution and /constitution both returned 404 in the shell. The home page links only to /codes. (2026-10-16)
- **statutes** — California codes on Cornell LII: law.cornell.edu/states/california links out to leginfo. LII hosts only CCR for California. (2026-10-16)
- **case_law** — Public-domain (vendor-neutral) citation format: California has no public-domain citation format (2026-10-16)

## Open questions

- leginfo.legislature.ca.gov: confirm the lawCode table and the sectionNum trailing-period convention from a network that is not challenged. Confirm the official-status disclaimer on the FAQ page.
- Justia constitution URLs for articles with letter suffixes (e.g. XIII A, XIII B) are unverified.
- Does any free source give official Cal./Cal.App. pagination that automation can reach? Lexis Official Reports is robots-disallowed and Justia shows slip pagination only.
- www4.courts.ca.gov opinion PDFs: WebFetch returns ROBOTS_DISALLOWED and the shell's robots.txt fetch gets a Cloudflare challenge. Recheck whether this is policy or transient.
- Unpublished-opinions review-granted page (courts.ca.gov/opinions/unpublished-opinions-review-granted?) not probed.
- Superior court appellate division opinions: covered in the courts.ca.gov listing filter (id 104). Justia coverage for them is unverified.
- Rules of Court: route bare 'rule N.N' only with California context (see citation_map notes).
