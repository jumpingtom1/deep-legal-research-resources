# District of Columbia (DC) — free legal sources

_Generated from `data/dc.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: the D.C. Code is on code.dccouncil.gov (Council, one page per section, constructible URL, 'Current through Sept. 26, 2026'); the Council's official GitHub repos (law-xml-codified, law-html) give bulk XML/HTML via raw.githubusercontent.com, lagging the site by months; Justia 2025 is the tier-2 fallback. No constitution: the Home Rule Act/District Charter is in D.C. Code Title 1 ch. 2. Court rules and opinions are PDFs on dccourts.gov, whose robots.txt answers with a bot check (script route refused) and which WebFetch read only intermittently; the D.C. App. R. PDF truncates at Rule 41. MOJs are listed by name only. Justia has D.C. Court of Appeals opinions 1923-2026. DCMR text is downloadable .doc files on dcregs.dc.gov (script ok, WebFetch gated); D.C. Register text sits behind postbacks.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| District of Columbia Court of Appeals | `dc (unverified)` | D.C. | A.3d, A.2d | — |
| Superior Court of the District of Columbia | `dcsuperct (unverified)` | D.C. Super. Ct. | Daily Wash. L. Rptr. | — |
| Municipal Court of Appeals for the District of Columbia (1942-1970, predecessor) | `dc (unverified)` | D.C. Mun. App. | A.2d, A. | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| D.C. Code (Official Code) | `D.C. Code § 16-1001`; `D.C. Code Ann. § 2-1402.11(a)`; `D.C. Code § 16-2399.09`; `D.C. Official Code § 29A-1053`; `D.C. Code § 5-545.06a`; `section 16-1001 of the D.C. Code`; `§ 16-1005(c) of the District of Columbia Official Code`; `D.C. Code (2012 Repl.) § 22-3020.53` | `dc-code-council` → `dc-code-github-xml` → `dc-code-justia` |
| D.C. Laws and Acts (session laws) | `D.C. Law 23-275`; `D.C. Law 17-368`; `D.C. Act 16-445` | `dc-laws-council` |
| Home Rule Act / District Charter | `Home Rule Act § 602(a)(3)`; `section 602 of the Home Rule Act`; `D.C. Code § 1-206.02(a)(3)`; `D.C. Home Rule Act § 404` | `dc-homerule-council` → `dc-code-justia` |
| D.C. Superior Court Rules | `Super. Ct. Civ. R. 12(b)(6)`; `D.C. Super. Ct. Civ. R. 56`; `Super. Ct. Crim. R. 33`; `Super. Ct. Dom. Rel. R. 4`; `Super. Ct. L&T R. 3`; `Super. Ct. Civ. R. 28-I`; `Superior Court Civil Rule 60(b)`; `Rule 12(b)(6) of the Superior Court Rules of Civil Procedure` | `dc-rules-superior` → `dc-rules-superior-compiled` |
| D.C. Court of Appeals Rules | `D.C. App. R. 28(g)`; `D.C. App. R. 40`; `D.C. Ct. App. R. 35`; `Rule 28 of the D.C. Court of Appeals Rules`; `D.C. Court of Appeals Rule 49` | `dc-rules-dcca` |
| D.C. Municipal Regulations (DCMR) | `14 DCMR § 308`; `14 DCMR § 308.1`; `14 D.C.M.R. 300`; `D.C. Mun. Regs. tit. 14, § 308`; `D.C. Mun. Regs. 14, § 308.2` | `dc-dcmr-dcregs` |
| D.C. Register | `61 DCR 5070`; `53 DCR 6443`; `40 D.C. Reg. 2204` | `dc-register-dcregs` |
| D.C. Court of Appeals (Atlantic Reporter / date parenthetical) | `150 A.3d 1213 (D.C. 2016)`; `M.A.P. v. Ryan, 285 A.2d 310 (D.C. 1971)`; `Jordan v. United States, No. 24-CF-0191 (D.C. Aug. 13, 2026)`; `Smith v. Jones, 123 A.3d 456, 460 (D.C. 2015)`; `Hall v. Hall, 100 A.2d 1 (D.C. Mun. App. 1953)`; `(D.C. 2023)` | `dc-opinions-dcca` → `dc-cases-justia` |
| D.C. Court of Appeals docket numbers (opinions and MOJs) | `No. 23-CF-389`; `Nos. 14-CV-101 & 14-CV-126`; `22-CO-0843`; `23-FS-0589`; `No. 22-CV-123, Mem. Op. & J. (D.C. Mar. 1, 2024)` | `dc-opinions-dcca` → `dc-cases-justia` |
| U.S. Supreme Court docket (certiorari from the D.C. Court of Appeals) | `District of Columbia v. R.W., No. 25-248 (U.S. Apr. 20, 2026)`; `No. 25-248, cert. granted` | `dc-scotus-docket` |

Regexes (case-insensitive):

- D.C. Code (Official Code): `(?:D\.\s*C\.\s*(?:Official\s+)?Code(?:\s+Ann\.)?|D\.C\.\s*Code\s+Ann\.|D\.C\.\s*Official\s+Code)\s*(?:\(\d{4}(?:\s+Repl\.)?\)\s*)?§+\s*(?P<section>\d{1,2}A?-\d{1,4}(?:\.\d{1,3}[a-z]?)?[a-z]?(?:\.\d{1,3})?(?:\((?:Perm|Temp)\))?)(?!\d)|(?:sec(?:tion|\.)|§)\s*(?P<section2>\d{1,2}A?-\d{1,4}(?:\.\d{1,3}[a-z]?)?[a-z]?(?:\.\d{1,3})?(?:\((?:Perm|Temp)\))?)(?:\([a-zA-Z0-9]+\))*\s+of\s+the\s+(?:D\.\s*C\.|District\s+of\s+Columbia)\s+(?:Official\s+)?Code`
- D.C. Laws and Acts (session laws): `D\.\s*C\.\s*Law\s+(?P<period>\d{1,2})-(?P<number>\d{1,3})(?!\d)|D\.\s*C\.\s*Act\s+(?P<aperiod>\d{1,2})-(?P<anumber>\d{1,3})(?!\d)`
- Home Rule Act / District Charter: `(?:(?:D\.\s*C\.\s*)?Home\s+Rule\s+Act|Home\s+Rule\s+Charter|District\s+Charter)\s*§\s*(?P<hra>\d{3}(?:\([a-z0-9]+\))*)|[Ss]ection\s+(?P<hra2>\d{3})(?:\([a-z0-9]+\))*\s+of\s+the\s+(?:D\.\s*C\.\s+|District\s+of\s+Columbia\s+)?(?:Home\s+Rule\s+Act|Home\s+Rule\s+Charter|Charter)|D\.\s*C\.\s*Code\s*§+\s*(?P<section>1-20[1-7]\.\d{2,3})(?!\d)`
- D.C. Superior Court Rules: `(?:D\.\s*C\.\s*)?Super\.\s*Ct\.\s*(?P<division>Civ|Crim|Dom\.\s*Rel|Fam|Juv|Neglect|L\s*&\s*T|Sm\.\s*Cl|Prob|Tax|Agency\s+Rev|Gen\.\s*Fam|Intrafam|R\.\s*Civ\.\s*P|R\.\s*Crim\.\s*P)\.?\s*(?:Proc\.\s*)?R\.?\s*(?P<rule>\d{1,3}(?:-[IVX]+)?(?:\.\d+)?)|Super(?:ior)?\s+Court\s+(?:Civil|Criminal|Domestic\s+Relations|Family|Landlord\s+and\s+Tenant|Probate)\s+Rule\s+(?P<rule2>\d{1,3}(?:-[IVX]+)?)|Rule\s+(?P<rule3>\d{1,3}(?:-[IVX]+)?)(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+(?:D\.\s*C\.\s+)?Superior\s+Court\s+(?:Rules\s+of\s+(?:Civil|Criminal)\s+Procedure|(?:Civil|Criminal|Family|Probate)\s+Rules)`
- D.C. Court of Appeals Rules: `D\.\s*C\.\s*(?:Ct\.\s*)?App\.\s*R\.\s*(?P<rule>\d{1,2}(?:\.\d)?)|(?:D\.\s*C\.\s*)?Court\s+of\s+Appeals\s+Rule\s+(?P<rule2>\d{1,2})(?=\D|$)(?![^.]{0,40}Circuit)|Rule\s+(?P<rule3>\d{1,2})(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+(?:Rules\s+of\s+the\s+)?(?:D\.\s*C\.|District\s+of\s+Columbia)\s+Court\s+of\s+Appeals(?:\s+Rules)?`
- D.C. Municipal Regulations (DCMR): `(?P<title>\d{1,2}[A-Z]?)\s+D\.?\s*C\.?\s*M\.?\s*R\.?\s*(?:§+\s*)?(?P<section>\d{1,5}(?:\.\d{1,3})?)|D\.\s*C\.\s*Mun\.\s*Regs\.\s*(?:tit\.\s*)?(?P<title2>\d{1,2}[A-Z]?),?\s*§+\s*(?P<section2>\d{1,5}(?:\.\d{1,3})?)`
- D.C. Register: `(?P<volume>\d{1,2})\s+(?:DCR|D\.\s*C\.\s*Reg\.)\s+(?P<page>\d{1,6})`
- D.C. Court of Appeals (Atlantic Reporter / date parenthetical): `(?P<volume>\d{1,4})\s+A\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+(?:[-–]\d+)?)?\s*\((?P<court>D\.\s*C\.)\s*(?:(?:en\s+banc)\s*)?(?P<year>\d{4})\)|\(D\.\s*C\.\s*(?:[A-Z][a-z]{2,4}\.?\s+\d{1,2},\s*)?(?P<year2>\d{4})\)|\(D\.\s*C\.\s*Mun\.\s*App\.\s*(?P<year3>\d{4})\)`
- D.C. Court of Appeals docket numbers (opinions and MOJs): `(?:No(?:s)?\.\s*)?(?P<yy>\d{2})-(?P<type>CV|CF|CM|CO|CT|FS|FM|FD|AA|BG|BS|OA|PR|SP|TX|DA|DV|CP)-(?P<num>\d{2,4})(?!\d)`
- U.S. Supreme Court docket (certiorari from the D.C. Court of Appeals): `(?:No\.\s*)?(?P<term>\d{2})-(?P<number>\d{1,5})\b(?=[^\n]{0,60}(?:U\.\s*S\.|cert|Supreme\s+Court))`

Short forms → URL key:

D.C. Code → `code`; D.C. Code Ann. → `code`; D.C. Official Code → `code`; D.C. Off. Code → `code`; DC Code → `code`; Home Rule Act → `code:1-2`; District Charter → `code:1-2`; DCMR → `dcmr`; D.C.M.R. → `dcmr`; D.C. Mun. Regs. → `dcmr`; DCR → `dcr`; D.C. Reg. → `dcr`; Super. Ct. Civ. R. → `Civil`; Super. Ct. Crim. R. → `Criminal`; Super. Ct. Dom. Rel. R. → `Domestic Relations`; Super. Ct. L&T R. → `Landlord and Tenant`; Super. Ct. Sm. Cl. R. → `Small Claims`; Super. Ct. Prob. R. → `Probate`; Super. Ct. Juv. R. → `Juvenile`; Super. Ct. Neglect R. → `Neglect and Abuse`; Super. Ct. Fam. R. → `General Rules of the Family Court`; D.C. App. R. → `DCCA`; D.C. Ct. App. R. → `DCCA`

OUT OF SCOPE, do not route here: the federal U.S. District Court for the District of Columbia ('D.D.C.', CourtListener 'dcd') and the U.S. Court of Appeals for the D.C. Circuit ('D.C. Cir.', 'cadc'; older 'App. D.C.' / 'U.S. App. D.C.' reporters). The case-law regex only accepts '(D.C. YYYY)' or '(D.C. Mon. D, YYYY)' — '(D.C. Cir. 2020)' and '(D.D.C. 2020)' do not match. Caution: D.C. Circuit decisions before Feb. 1, 1971 are binding D.C. precedent (M.A.P. v. Ryan, 285 A.2d 310 (D.C. 1971)) but are federal reports — route them to federal sources. D.C. has no state constitution: the Home Rule Act (Pub. L. 93-198; D.C. Code §§ 1-201.01 to 1-207.71) serves as the charter; Home Rule Act section numbers (§ 602) map to Code sections (§ 1-206.02) only through the Code's 'Section References'/history notes — no formula. D.C. Code section numbers contain a hyphen (title-section, e.g. 16-1001, 2-1402.11, 29A-1053, 5-545.06a): a range '§§ 16-1001 – 16-1058' is two sections joined by an en dash or 'to'; the regex takes the first. Some sections exist in '(Perm)' and '(Temp)' versions (e.g. 47-2501(Perm)); the suffix is captured but its URL form is untested. 'D.C. Code' with no 'Ann.' is the Bluebook form (Bluebook cites D.C. Code (LexisNexis/West)); practitioners also write 'D.C. Official Code'. Court rules: bare 'Rule 12(b)(6)', 'Civ. R.' or 'Rule 28' must not route here without 'Super. Ct.' / 'D.C. App. R.' / 'D.C. Court of Appeals' context (Delaware also uses 'Super. Ct. Civ. R.' — require D.C. context or a 'D.C.' prefix when the query is ambiguous). The Superior Court Civil Rules track the FRCP numbering, with D.C.-only rules such as 28-I and 12-I. D.C. has no codified rules of evidence (memory; not verified). MOJs (memorandum opinion and judgment) are unpublished; D.C. App. R. 28(g) (fetched 2026-10-16, 2021 revision) says unpublished orders/opinions may not be cited except for law of the case, res judicata, collateral estoppel, same-defendant criminal or same-respondent disciplinary matters. DCCA docket numbers are YY-TT-NNNN (CV civil, CF felony, CM misdemeanor, CO collateral criminal, FS/FM family, AA agency, BG bar); dockets are often cited without leading zeros (22-CO-043 = 22-CO-0843 per Justia listing typo — confirm). The DCCA is the highest local court; review is only by U.S. Supreme Court certiorari. DCMR cites: '14 DCMR § 308' → dcregs SectionNumber '14-308'; subsection '308.1' lives in section 308. CourtListener ids are from memory and unverified; 'dcsuperct' in particular is a guess.

## A. Statutes / code

### `dc-code-council` — Code of the District of Columbia (D.C. Law Library, code.dccouncil.gov)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Council of the District of Columbia (Office of the General Counsel), site by Open Law Library · text: **fetch-and-quote** · official: unknown
- **Coverage:** Entire D.C. Code (all titles incl. 1 Home Rule, 16, 22, 29A, 47 etc.), with history notes, section references, effect-of-amendments and emergency-legislation notes; one page per section; title pages list chapters with section ranges.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://code.dccouncil.gov/us/dc/council/code/sections/{section}`
  - Placeholders: section = the full D.C. Code number exactly as cited, hyphen kept, ASCII hyphen (not the en dash the page heading shows), dots and lower-case letter suffixes kept: 16-1001, 2-1402.11, 1-206.02, 2-651.04, 29A-1053, 5-545.06a. Title index https://code.dccouncil.gov/us/dc/council/code/titles/{title} (titles/16, titles/27A) lists chapters WITH section ranges ('Chapter 10 … §§ 16-1001 – 16-1058'); chapter index /titles/{title}/chapters/{chapter} lists subchapters with ranges. '(Perm)'/'(Temp)' variant URLs untested.
  - Index: `https://code.dccouncil.gov/us/dc/council/code`
- **Automation:** WebFetch gated · shell ok · robots: robots.txt (Cloudflare-managed) allows User-Agent * with 'Content-signal: search=yes,ai-train=no' and disallows ClaudeBot, GPTBot, CCBot and other AI crawlers by name, plus '/_*'. fetch_doc.py (its own UA) was allowed. Footer asks: 'Please do not scrape. Instead, bulk download the HTML or XML.' — prefer dc-code-github-xml for anything beyond single lookups.
  - WebFetch of URLs taken from search results returned full body (2-552, 11-502, /code root); the self-built URL for 16-1001 waited on a permission prompt and timed out (PROVENANCE_REQUIRED) — treat built URLs as gated and use fetch_doc.py. Section pages are short (16-1001 = 4,935 chars; 2-1402.11 = 22,009 chars) so truncation is not a concern.
- **Currency:** Code root page (/us/dc/council/code) 'Publication Information' block; not on section pages — observed: "Current through Sept. 26, 2026; Law 26-187 effective Sept. 26, 2026"
- **Official status:** Pages carry no official/authentication statement (WebFetch of /code: 'makes no statement about whether this online code is official'); footer says only that codes and laws are public domain. D.C. enacted UELMA (D.C. Law 21-251, D.C. Code §§ 2-651.01 et seq., applying from July 1, 2017) but no designation of this site as official was found.
- **Hazard:** Page headings print the section number with an en dash (§ 16–1001); URLs use an ASCII hyphen
- **Hazard:** Site asks users not to scrape and to use the bulk repos
- **Hazard:** no currency line on section pages
- **Hazard:** Self-built URLs gated for WebFetch
- **Hazard:** '(Perm)' / '(Temp)' parallel section versions exist (47-2501(Perm)); confirm which applies
- **Probe:** D.C. Code § 16-1001 → `https://code.dccouncil.gov/us/dc/council/code/sections/16-1001` — expect: "For the purposes of this subchapter, the term:"
- **Evidence (2026-10-16):** fetch_doc.py: 16-1001 kind=html 4,935 chars, body 'For the purposes of this subchapter, the term:' incl. (5A) 'Family member'; 2-1402.11 22,009 chars; 2-702, 2-651.02-.04 ok. WebFetch (search-result URLs): 2-552 YES '(a) The District of Columbia Office of Documents, established pursuant to', not truncated; 11-502 YES 'In addition to its jurisdiction as a United States district'. Built URL 16-1001: PROVENANCE_REQUIRED (gated).
- **Notes:** Official bulk mirrors: dc-code-github-xml (XML) and DCCouncil/law-html (HTML). Law Library also hosts D.C. Laws (dc-laws-council).

### `dc-code-github-xml` — D.C. Code bulk XML (DCCouncil/law-xml-codified on GitHub)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Council of the District of Columbia (GitHub organisation DCCouncil) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Codified D.C. Code, one XML file per section; sibling repo DCCouncil/law-html (master) holds the rendered HTML incl. a code index with a currency line.
- **Read via (in order):** **script**
- **Access:** `constructible` · format xml
  - Pattern: `https://raw.githubusercontent.com/DCCouncil/law-xml-codified/master/us/dc/council/code/titles/{title}/sections/{section}.xml`
  - Placeholders: title = the part of the section number before the first hyphen (16, 2, 29A); section verbatim (16-1001, 2-1402.11). HTML twin: https://raw.githubusercontent.com/DCCouncil/law-html/master/us/dc/council/code/sections/{section}.html. Branch is 'master' (main → 404). Do NOT use DCCouncil/law-xml (branch main): its README says it holds raw laws plus 'the code as it appeared on March 10, 2016' — its 16-1001.xml lacks the current (5A) 'Family member' definition.
  - Index: `https://raw.githubusercontent.com/DCCouncil/law-html/master/us/dc/council/code/index.html`
- **Automation:** WebFetch untested · shell ok · robots: raw.githubusercontent.com allowed by fetch_doc.py; github.com itself REFUSED (robots answered with a bot check) — do not use github.com pages
  - Use raw.githubusercontent.com only. Repo copy can lag the live site (law-html index says 'Current through Apr. 29, 2026' while the live site says Sept. 26, 2026): before quoting, compare with dc-code-council or check the section's history note.
- **Currency:** law-html code index.html 'Publication Information' (law-xml-codified index.xml shows only a template) — observed: "Current through Apr. 29, 2026; Last codified D.C. Law: Law 26-112"
- **Official status:** Linked from the Code root page as the bulk XML download ('bulk download the HTML or XML'); no authentication statement read. Press reports (2018) describe GitHub as D.C.'s official digital source — not verified on a government page.
- **Hazard:** Repo lags live site by months
- **Hazard:** Wrong repo (law-xml) serves a 2016 code
- **Hazard:** github.com HTML pages refuse automation
- **Probe:** D.C. Code § 16-1001 → `https://raw.githubusercontent.com/DCCouncil/law-xml-codified/master/us/dc/council/code/titles/16/sections/16-1001.xml` — expect: "(5A) "Family member" means a person:"
- **Evidence (2026-10-16):** fetch_doc.py: law-xml-codified 16-1001.xml 4,343 chars, grep 'Family member' 3 matches; 2-1402.11.xml 21,818 chars 'Prohibitions.'; law-html 16-1001.html 4,935 chars same text; law-xml/main 16-1001.xml lacks 'Family member' (stale 2016 code); law-xml-codified/main → 404.
- **Notes:** Corpus/bulk candidate for the whole Code.

### `dc-laws-council` — D.C. Laws (session laws) in the D.C. Law Library

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Council of the District of Columbia · text: **fetch-and-quote** · official: unknown
- **Coverage:** D.C. Laws by Council period, HTML text with links; enrolled PDFs under /laws/docs/.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://code.dccouncil.gov/us/dc/council/laws/{period}-{number}`
  - Placeholders: D.C. Law 23-275 → /laws/23-275 (period = Council period, number unpadded). PDF: /us/dc/council/laws/docs/{period}-{number}.pdf (17-368.pdf, 8 pp). D.C. Acts (emergency/temporary) URL form not tested.
  - Index: `https://code.dccouncil.gov/us/dc/council/laws`
- **Automation:** WebFetch gated · shell ok · robots: see dc-code-council
  - Not WebFetched; script only.
- **Currency:** none on law pages
- **Official status:** Same site as dc-code-council; no official statement on law pages.
- **Hazard:** D.C. Act URL form unverified
- **Probe:** D.C. Law 23-275 → `https://code.dccouncil.gov/us/dc/council/laws/23-275` — expect: "Intrafamily Offenses and Anti-Stalking Orders Amendment Act of 2020"
- **Evidence (2026-10-16):** fetch_doc.py: /laws/23-275 39,401 chars, 'D.C. Law 23-275. Intrafamily Offenses and Anti-Stalking Orders Amendment Act of 2020.'; /laws/docs/17-368.pdf kind=pdf 8 pages.

### `dc-code-justia` — Justia — District of Columbia Code (2025)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** D.C. Code editions incl. 2016, 2019 and 2025 (unversioned URL = 2025).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/district-of-columbia/title-{title}/chapter-{chapter}/[subchapter-{subchapter_roman_lower}/]section-{section}/`
  - Placeholders: title and chapter lower-case (title-38, chapter-1a); subchapter as lower-case Roman with hyphenated letter suffix (subchapter-i, subchapter-i-a, subchapter-ii); section verbatim with hyphen (section-16-1001). Chapter/subchapter come from dc-code-council's title/chapter index (which shows ranges); Justia's own indexes show NO section ranges. Year-specific: insert /{year}/ after /district-of-columbia/.
  - Index: `https://law.justia.com/codes/district-of-columbia/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: fetch_doc.py refused law.justia.com (robots.txt challenge) for the day
  - WebFetch only. A self-built section URL (16-1001) went through without a permission prompt.
- **Currency:** page header — observed: "2025 District of Columbia Code"
- **Official status:** Page says 'These codes may not be the most recent version.'
- **Hazard:** edition lag
- **Hazard:** indexes lack section ranges
- **Hazard:** shell blocked
- **Probe:** D.C. Code § 16-1001 → `https://law.justia.com/codes/district-of-columbia/title-16/chapter-10/subchapter-i/section-16-1001/` — expect: "For the purposes of this subchapter, the term: (1) “Attorney General”"
- **Evidence (2026-10-16):** WebFetch: 16-1001 YES, (5A) 'Family member' present, '2025 District of Columbia Code'; 38-131 YES 'The Chancellor of the District of Columbia Public Schools is', not truncated.
- **Notes:** public.law and Cornell LII do not host the D.C. Code (see absent).

## B. Constitution

### `dc-homerule-council` — District of Columbia Home Rule Act / District Charter (D.C. Code Title 1, Chapter 2)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Council of the District of Columbia (D.C. Law Library) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Home Rule Act as codified: subch. I-VII, §§ 1-201.01 – 1-207.71; the District Charter is subch. IV (§§ 1-204.01 – 1-204.115); limits on the Council at § 1-206.02.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://code.dccouncil.gov/us/dc/council/code/sections/{section}`
  - Placeholders: Use the D.C. Code section (1-206.02). A Home Rule Act section number (§ 602) has no formula to a Code section: open https://code.dccouncil.gov/us/dc/council/code/titles/1/chapters/2 (subchapter ranges shown) and match the Act section in each Code section's history note ('§ 602').
  - Index: `https://code.dccouncil.gov/us/dc/council/code/titles/1/chapters/2`
  - Navigation: chapter 2 index → subchapter (ranges shown) → section page; Act § number is in the history note
- **Automation:** WebFetch gated · shell ok · robots: see dc-code-council
- **Currency:** Code root page — observed: "Current through Sept. 26, 2026"
- **Official status:** Same as dc-code-council.
- **Hazard:** Act section ↔ Code section mapping only via history notes
- **Hazard:** no state constitution exists
- **Probe:** D.C. Code § 1-206.02 (Home Rule Act § 602) → `https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02` — expect: "The Council shall have no authority to pass any act contrary"
- **Evidence (2026-10-16):** fetch_doc.py: 1-206.02 '(a) The Council shall have no authority to pass any act contrary to the provisions'; /titles/1/chapters/2 lists subchapters I-VII with ranges.

## C. Court rules

### `dc-rules-dcca` — Rules of the District of Columbia Court of Appeals (complete rules PDF)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · District of Columbia Court of Appeals · text: **fetch-and-quote** · official: unknown
- **Coverage:** D.C. App. R. 1-49 and appendices; cover says revised effective Dec. 1, 2021 (file uploaded 2024-06). Older versions also on site (2019-02, 2020-11, 2021-07, 2022-07 uploads); per-rule PDFs exist (e.g. /sites/default/files/2019-05/Rule%2028.%20Briefs.pdf).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://dccourts.gov/sites/default/files/2024-06/DCCA_Complete_Rules.pdf`
  - Placeholders: Fixed upload path (/sites/default/files/{YYYY-MM}/...) — changes on re-issue; newer compilations may exist. Re-confirm from the Court of Appeals rules page.
  - Index: `https://www.dccourts.gov/court-of-appeals/rules`
  - Navigation: Court of Appeals rules page → complete rules PDF (index page itself not fetched)
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: www.dccourts.gov answers robots.txt with a bot check — fetch_doc.py REFUSED the host
  - Text 123,307 chars: window 1 ends at Rule 29(a)(6); window 2 (offset=100000) holds Rules 35 and 40 but stops mid-word in Rule 41(g) — Rules 42-49 and appendices not extracted. WebFetch on dccourts.gov was intermittent: 5 CLIENT_ERROR failures during the session.
- **Currency:** PDF cover page — observed: "(Revised effective December 1, 2021)"
- **Official status:** Published by the court on dccourts.gov; no official-text statement read.
- **Hazard:** WebFetch extraction stops in Rule 41(g)
- **Hazard:** shell blocked by bot check
- **Hazard:** upload-month path changes
- **Hazard:** intermittent WebFetch CLIENT_ERROR on dccourts.gov
- **Hazard:** currency possibly stale (2021 revision)
- **Probe:** D.C. App. R. 28(a) → `https://dccourts.gov/sites/default/files/2024-06/DCCA_Complete_Rules.pdf` — expect: "Brief of the Appellant (or Petitioner). The brief must contain,"
- **Evidence (2026-10-16):** WebFetch: Rule 28(a) YES 'Brief of the Appellant (or Petitioner). The brief must contain,'; Rule 40 NOT PRESENT in window 1; offset 100000: Rules 35 and 40 present, ends 'A mandate is not issued in a disciplinary cas' (Rule 41(g)). Shell: REFUSED (bot check).
- **Notes:** Rule 28(g) governs citation of unpublished MOJs (see citation_map.notes).

### `dc-rules-superior` — D.C. Superior Court Rules (per-rule PDFs)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Superior Court of the District of Columbia · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rule sets: Civil, Agency Review, Landlord and Tenant, Small Claims, Criminal, Crime Victim Compensation, D.C. Code 23-110 proceedings, Domestic Violence, Parentage and Support, General Family, Adoption, Juvenile, Domestic Relations, Mental Health, Neglect and Abuse, Probate (current and pre-Aug. 22, 2022), Tax.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.dccourts.gov/sites/default/files/rules-superior-court/{Division}%20Rule%20{N}.%20{Title}.pdf`
  - Placeholders: Per-rule file names embed the rule title ('Civil Rule 1. Scope and Purpose.pdf'), so the URL is not derivable from a citation — take the href from the rules index. Index page lists per-rule links but WebFetch did not expose hrefs.
  - Index: `https://www.dccourts.gov/superior-court/rules`
  - Navigation: rules index → rule set (e.g. 'Superior Court Rules of Civil Procedure') → 'Civil Rule N. Title' link → PDF; if hrefs are not visible, WebSearch 'dccourts.gov "Civil Rule N."' to obtain the URL
- **Automation:** WebFetch ok · shell blocked-challenge · robots: see dc-rules-dcca (bot check on robots.txt)
  - Index WebFetch returned rule-set names and per-rule titles but no hrefs.
- **Currency:** none stated on index; comments in each rule PDF — observed: "COMMENT TO 2017 AMENDMENTS"
- **Official status:** Published by the court on dccourts.gov; no official-text statement.
- **Hazard:** URL not constructible (title in file name)
- **Hazard:** no currency statement
- **Hazard:** shell blocked
- **Hazard:** intermittent WebFetch CLIENT_ERROR
- **Probe:** Super. Ct. Civ. R. 1 → `https://www.dccourts.gov/sites/default/files/rules-superior-court/Civil%20Rule%201.%20Scope%20and%20Purpose.pdf` — expect: "These rules govern the procedure in all civil actions and"
- **Evidence (2026-10-16):** WebFetch: Rule 1 YES 'These rules govern the procedure in all civil actions and'; heading 'COMMENT TO 2017 AMENDMENTS'. Index /superior-court/rules: 18 rule sets listed, hrefs not exposed.

### `dc-rules-superior-compiled` — D.C. Superior Court Rules of Civil Procedure 2025 (compiled PDF)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Superior Court of the District of Columbia · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full Civil Rules, 2025 compilation (per file name).
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.dccourts.gov/sites/default/files/superior-rules/Superior-Court-Rules-of-Civil-Procedure-2025.pdf`
  - Placeholders: Fixed file; year in name changes on re-issue.
  - Index: `https://www.dccourts.gov/superior-court/rules`
  - Navigation: found by WebSearch; not linked visibly on the index WebFetch output
- **Automation:** WebFetch fail · shell blocked-challenge · robots: see dc-rules-dcca
  - WebFetch CLIENT_ERROR twice (probably size or host flakiness).
- **Currency:** file name — observed: "Superior-Court-Rules-of-Civil-Procedure-2025.pdf"
- **Official status:** Court-published; not read.
- **Hazard:** could not be read by any route
- **Probe:** Super. Ct. Civ. R. 12(b) → `https://www.dccourts.gov/sites/default/files/superior-rules/Superior-Court-Rules-of-Civil-Procedure-2025.pdf`
- **Evidence (2026-10-16):** URL from WebSearch result; WebFetch 'There was an error while fetching' (twice); shell refused host.

## D. Administrative code

### `dc-dcmr-dcregs` — District of Columbia Municipal Regulations (DCMR) — dcregs.dc.gov

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Office of the Secretary of the District of Columbia, Office of Documents and Administrative Issuances · text: **fetch-and-quote** · official: unknown
- **Coverage:** All DCMR titles; per section: metadata page (effective date, authority, source note, rulemaking history) and a downloadable Word .doc with the text.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.dcregs.dc.gov/Common/DCMR/SectionList.aspx?SectionNumber={title}-{section}`
  - Placeholders: 14 DCMR § 308 → SectionNumber=14-308 (metadata only; text is behind a postback 'View Text'). Text route: chapter list https://www.dcregs.dc.gov/Common/DCMR/RuleList.aspx?ChapterNum={title}-{chapter} (chapter = section div 100 for 3-digit sections: 308 → 14-3) — each row's 'View text' anchor carries title/href 'https://dcregs.dc.gov/Common/DCMR/RuleList.aspx?DownloadFile={GUID}' → .doc file (e.g. 14308.doc). GUIDs are not derivable; take from the chapter page. Title list: ChapterList.aspx?TitleNum={title}. TitleList.aspx redirects to ErrorPage.aspx.
  - Index: `https://www.dcregs.dc.gov/Common/DCMR/ChapterList.aspx?TitleNum={title}`
  - Navigation: ChapterList.aspx?TitleNum=T → RuleList.aspx?ChapterNum=T-C (lists sections, headings, effective dates) → row's DownloadFile GUID → .doc text
- **Automation:** WebFetch gated · shell ok · robots: Cloudflare content-signal file ('search=yes,ai-train=no'); no Disallow lines in the portion read
  - fetch_doc.py treats the .doc as html: the read view shows binary noise but grep finds the text ('308.1 For purposes of this chapter, the term “security deposit”'). Quote via grep/verify, not read. WebFetch of the RuleList URL was gated (PROVENANCE_REQUIRED).
- **Currency:** per-section 'Effective Date' on SectionList and RuleList pages (1/1/1900 = original/unknown) — observed: "14-301 effective 10/10/2025; 14-308 Effective Date: 1/1/1900"
- **Official status:** Section page labels text 'Most recent version of the final adopted rule codified in the D.C. Municipal Regulations (DCMR)'; no authentication statement.
- **Hazard:** text only in Word .doc downloads
- **Hazard:** DownloadFile GUIDs not derivable
- **Hazard:** ASP.NET postbacks for many links
- **Hazard:** 1/1/1900 placeholder effective dates
- **Hazard:** WebFetch gated
- **Probe:** 14 DCMR § 308 → `https://dcregs.dc.gov/Common/DCMR/RuleList.aspx?DownloadFile=F072555F-0000-C01C-9C51-075D1CDEADB6` — expect: "For purposes of this chapter, the term “security deposit” shall mean"
- **Evidence (2026-10-16):** fetch_doc.py: RuleList ChapterNum=14-3 16,065 chars, 19 sections; DownloadFile GUID for 14-308 → filename=14308.doc 22,528 chars; text '308 SECURITY DEPOSITS 308.1 For purposes of this chapter'; SectionList 14-308 metadata with source note '5G DCRR § 2908'.
- **Notes:** Cornell LII does not carry D.C. regulations (its state-regulations list skips D.C.).

## D. Administrative register

### `dc-register-dcregs` — District of Columbia Register — dcregs.dc.gov

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Office of Documents and Administrative Issuances · text: **link-only** · official: unknown
- **Coverage:** Weekly D.C. Register issues and individual notices (rulemakings, Council actions, Mayor's orders) — e.g. Vol. 61 No. 21 (May 16, 2014).
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.dcregs.dc.gov/Common/NoticeDetail.aspx?NoticeId={noticeId}`
  - Placeholders: Notice ids (N0047614) come from a DCMR section's rulemaking-history table or Register search; issue page DCR/Issues/IssueDetailPage.aspx?issueID={n} (internal id: Vol 61 No 21 = 493). '61 DCR 5070' (volume + page) has no URL formula; whole-issue and notice text files are behind ASP.NET postbacks.
  - Index: `https://www.dcregs.dc.gov/`
  - Navigation: DCMR section page history → Notice ID → NoticeDetail (metadata, issue, publish date) → 'View text' (postback)
- **Automation:** WebFetch gated · shell ok · robots: see dc-dcmr-dcregs
  - Metadata pages reachable by GET; notice/issue text needs a postback and was not retrieved.
- **Currency:** issue page header — observed: "DISTRICT OF COLUMBIA REGISTER Vol.61 - No.21 May 16, 2014"
- **Official status:** Official publication of the Office of Documents; no online-authentication statement seen.
- **Hazard:** text behind postback
- **Hazard:** DCR volume/page not resolvable to a URL
- **Probe:** Notice N0047614 (61 DCR, May 16, 2014) → `https://www.dcregs.dc.gov/Common/NoticeDetail.aspx?NoticeId=N0047614`
- **Evidence (2026-10-16):** fetch_doc.py: NoticeDetail 12,176 chars of metadata (agency, chapters, 'Register Issue : 5/16/2014 Vol 61/21'); IssueDetailPage issueID=493 4,765 chars; notice text link is a postback — no text retrieved.

## E. Case law

### `dc-opinions-dcca` — D.C. Court of Appeals — Opinions and Memorandum Opinions and Judgments

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · District of Columbia Court of Appeals · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Published opinions as PDFs (oldest seen: 14-CV-101, decided 2016, amended 2018); MOJs are listed by name and docket only (page states the court 'only lists online the names and case numbers of MOJs'). Listing page=47 covered Nov. 2019 – Jan. 2020; ≥186 pages exist.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.dccourts.gov/court-of-appeals/opinions-memorandum-of-judgments?combine={text}&field_date_value={from}&field_date_value_1={to}&field_type_value=All&order=field_date&sort=desc&page={n}`
  - Placeholders: GET filter parameters seen in search-engine URLs (not tested by a successful fetch): combine = free text (party/docket), field_date_value / field_date_value_1 = date range, field_type_value = All (or a type), order/sort, page (0-based). Table columns: Appeal Number, Case, Date, Disposition, Judge. Opinion PDFs live at /sites/default/files/{upload YYYY-MM}/{file}.pdf (e.g. 2018-12/14-CV-101.pdf, 2026-05/Greer v US 23-CF-389.pdf) — upload month and file name are not derivable.
  - Index: `https://www.dccourts.gov/court-of-appeals/opinions-memorandum-of-judgments`
  - Navigation: listing (filter by text/date) → row → opinion PDF link; WebFetch of two listing pages showed NO hrefs in the table — if no link is visible, find the PDF by WebSearch '"<docket>" site:dccourts.gov' or use dc-cases-justia
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: robots.txt answered with a bot check; fetch_doc.py REFUSED the host for the day
  - WebFetch worked for listing ?page=47 and ?page=107 and the 14-CV-101 PDF (116,785 chars; window 1 ends at 100,000), then failed with CLIENT_ERROR on 4 listing/PDF URLs. Bare listing URL (self-built) was gated.
- **Currency:** none stated
- **Official status:** Slip opinions carry the notice that they are subject to formal revision before publication in the Atlantic Reporter; A.2d/A.3d (West) is the reporter.
- **Hazard:** slip pagination only (A.3d cite only in later amended footnotes)
- **Hazard:** MOJ text not online
- **Hazard:** PDF URLs not derivable
- **Hazard:** listing hrefs not exposed to WebFetch
- **Hazard:** intermittent WebFetch CLIENT_ERROR
- **Hazard:** shell blocked by bot check
- **Hazard:** long opinions exceed one WebFetch window
- **Probe:** Competitive Enterprise Institute v. Mann, Nos. 14-CV-101 & 14-CV-126 (D.C. Dec. 22, 2016, amended Dec. 13, 2018) → `https://www.dccourts.gov/sites/default/files/2018-12/14-CV-101.pdf` — expect: "These appeals present us with legal issues of first impression"
- **Evidence (2026-10-16):** WebFetch: body YES 'These appeals present us with legal issues of first impression'; footnote notes prior opinion at 150 A.3d 1213; ~58 pp; truncated at 100,000 of 116,785 chars. Listing ?page=47: MOJ/opinion rows, no links. Shell: REFUSED (bot check on robots.txt).
- **Notes:** Greer v. United States, 23-CF-389 (2026-05 upload) found by search but WebFetch CLIENT_ERROR.

### `dc-cases-justia` — Justia — District of Columbia Court of Appeals decisions

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** D.C. Court of Appeals 1923-2026 (year listings); no Superior Court listing. Per-curiam rows without summary/link are probably MOJs.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/district-of-columbia/court-of-appeals/{year}/{docket_lower}.html`
  - Placeholders: year = decision year; docket lower-case with 4-digit zero-padded number: 24-CF-0191 → 24-cf-0191; multi-docket cases use one of the dockets (Wilson: 22-co-0843); repeat decisions on a docket get -0 / -1 suffixes (24-cv-1001-0). Confirm from the year listing https://law.justia.com/cases/district-of-columbia/court-of-appeals/{year}/ if the first guess fails. Opinion PDF copy at cases.justia.com/district-of-columbia/court-of-appeals/{year}-{docket_lower}.pdf.
  - Index: `https://law.justia.com/cases/district-of-columbia/court-of-appeals/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (fetch_doc.py refused law.justia.com)
  - WebFetch only.
- **Currency:** year listing (newest rows) — observed: "2026 listing newest decisions dated August 13, 2026"
- **Official status:** Third-party compilation of slip opinions.
- **Hazard:** docket slug suffixes
- **Hazard:** listing typos in dockets
- **Hazard:** shell blocked
- **Hazard:** slip text, no A.3d pagination
- **Probe:** Jordan v. United States, No. 24-CF-0191 (D.C. Aug. 13, 2026) → `https://law.justia.com/cases/district-of-columbia/court-of-appeals/2026/24-cf-0191.html` — expect: "Marquette Jordan was convicted of second-degree murder and two related"
- **Evidence (2026-10-16):** WebFetch: body YES 'Marquette Jordan was convicted of second-degree murder and two related'; complete to 'So ordered.'; 2026 year listing gives docket slugs; court index lists only the Court of Appeals, years 1923-2026.
- **Notes:** Justia's listing lags the court by ~2 months (newest Aug. 13, 2026 on Oct. 16, 2026).

## F. Subsequent history

### `dc-enbanc-dcca` — D.C. Court of Appeals en banc / rehearing dispositions

- **Status:** REPORTED 2026-10-16 · **Tier 1** · District of Columbia Court of Appeals · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Petitions for rehearing / rehearing en banc under D.C. App. R. 35 and 40. En banc opinions appear in the opinions listing; orders granting en banc (which vacate the division opinion) and amended opinions (e.g. 14-CV-101 amended Dec. 13, 2018) appear as new PDF uploads.
- **Read via (in order):** **fetch tool**
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.dccourts.gov/court-of-appeals/opinions-memorandum-of-judgments?combine={docket_or_party}&field_type_value=All&order=field_date&sort=desc`
  - Placeholders: Search the DCCA listing by docket or party name (GET parameters as in dc-opinions-dcca, untested); Justia year listings also show later decisions on the same docket with -0/-1 suffixes. No separate published list of en banc grants was found.
  - Index: `https://www.dccourts.gov/court-of-appeals/opinions-memorandum-of-judgments`
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: see dc-opinions-dcca
- **Currency:** none stated
- **Official status:** Slip opinions and orders.
- **Hazard:** en banc grant orders may not be posted
- **Hazard:** docket/party search only
- **Probe:**  → ``
- **Evidence (2026-10-16):** Rules 35/40 confirmed in dc-rules-dcca; amended opinion seen (14-CV-101 'amended December 13, 2018'); no en banc order list located; listing search not tested.

### `dc-scotus-docket` — U.S. Supreme Court docket (certiorari from the D.C. Court of Appeals)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Supreme Court of the United States · text: **fetch-and-quote** · official: official
- **Coverage:** The D.C. Court of Appeals is D.C.'s highest court; the only further review is certiorari (28 U.S.C. § 1257(b)). Dockets show 'Lower Ct: District of Columbia Court of Appeals', 'Case Numbers: (23-FS-0589)', and the disposition.
- **Read via (in order):** **script**
- **Access:** `search-only` · format html
  - Pattern: `https://www.supremecourt.gov/docket/docketfiles/html/public/{term}-{number}.html`
  - Placeholders: Constructible only once the SCOTUS docket number is known (25-248). From a DCCA docket alone there is no URL: search the Supreme Court docket search by party name or the DCCA case number (search page not probed), or WebSearch '"<DCCA docket>" supremecourt.gov'.
  - Index: `https://www.supremecourt.gov/docket/docket.aspx`
- **Automation:** WebFetch untested · shell ok · robots: allowed for the docket path (fetch_doc.py ok)
- **Currency:** docket entries (dated) — observed: "May 22 2026 Judgment and Mandate Issued."
- **Official status:** Docket maintained by the Clerk of the Supreme Court.
- **Hazard:** no link from DCCA docket to SCOTUS docket
- **Hazard:** party names may be reversed or anonymised (R.W.)
- **Probe:** District of Columbia v. R.W., No. 25-248 (from DCCA No. 23-FS-0589) → `https://www.supremecourt.gov/docket/docketfiles/html/public/25-248.html` — expect: "Petition GRANTED. Judgment REVERSED and case REMANDED"
- **Evidence (2026-10-16):** fetch_doc.py: 15,277 chars; 'Lower Ct: District of Columbia Court of Appeals', 'Case Numbers: (23-FS-0589)'; Apr 20 2026 'Petition GRANTED. Judgment REVERSED and case REMANDED'.

## Not available (do not look for these again)

- **constitution** — A state constitution: D.C. is not a state; the Home Rule Act (D.C. Code Title 1, ch. 2, 'District Charter' subch. IV) is the governing charter (code.dccouncil.gov /titles/1/chapters/2). (2026-10-16)
- **statutes** — public.law edition of the D.C. Code: www.public.law home page names only Oregon/California-type state sites; no D.C. site linked (fetch_doc.py). (2026-10-16)
- **statutes** — Cornell LII D.C. Code, DCMR or opinions: https://www.law.cornell.edu/states/dc links out to LexisNexis D.C. Code, dccourts.gov and dcregs.dc.gov; /regulations list has no D.C. entry (fetch_doc.py). (2026-10-16)
- **case_law** — Free official reporter (A.3d) pagination: Court PDFs are slip opinions; A.2d/A.3d are West reporters. (2026-10-16)
- **case_law** — Public-domain (vendor-neutral) citation format: None used; D.C. App. R. 28 and Bluebook cite A.3d with '(D.C. YYYY)'. (2026-10-16)
- **case_law** — Text of MOJs (unpublished decisions) online: Listing page states the court only lists names and case numbers of MOJs online (WebFetch of ?page=47). (2026-10-16)

## Corpus candidates (maintainers)

- `dc-code-github-xml` — Whole D.C. Code; site asks users not to scrape and offers bulk XML/HTML · bulk: https://github.com/DCCouncil/law-xml-codified (XML, branch master); https://github.com/dccouncil/law-html (HTML)
- `dc-rules-dcca` — WebFetch extraction stops in Rule 41(g) of 49; shell blocked by bot check, so a corpus copy is the only full-text route
- `dc-rules-superior-compiled` — Compiled Civil Rules could not be read by WebFetch (CLIENT_ERROR) and the shell is blocked

## Open questions

- dccourts.gov: is the opinions listing GET filter (combine, field_date_value, field_type_value, page) usable, and do rows link to PDFs? WebFetch showed no hrefs and later failed with CLIENT_ERROR; shell is refused by a bot check on robots.txt.
- Is there a newer complete D.C. App. R. compilation than the 2024-06 upload (cover: revised effective Dec. 1, 2021)? Rules page /court-of-appeals/rules not fetched.
- D.C. App. R. 28(g) as fetched has no persuasive-citation exception for post-2007 MOJs; confirm against the current rules (memory suggested one).
- Has the Council designated code.dccouncil.gov or the GitHub repos as the official/authenticated Code under UELMA (D.C. Code § 2-651.03)? No statement found.
- URL form for '(Perm)'/'(Temp)' section versions on code.dccouncil.gov and for D.C. Acts under /laws/.
- D.C. Register text retrieval by GET (notice and issue files are postbacks).
- Superior Court opinions: no free official database located (not searched in depth).
- D.C. Rules of Professional Conduct (D.C. Bar / Court of Appeals) not probed.
- CourtListener ids 'dc' and 'dcsuperct' unverified.
