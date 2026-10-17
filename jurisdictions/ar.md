# Arkansas (AR) — free legal sources

_Generated from `data/ar.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: the official Arkansas Code is a LexisNexis JavaScript app (link-only); quote from Justia's 2025 edition (tier 2, WebFetch, one subtitle hop), and read session-law PDFs from arkleg.state.ar.us by constructible URL. Constitution: Justia per-section pages; the SOS PDF is on an unconfirmed ark.org host. Court rules and opinions live on opinions.arcourts.gov (Lexum): the script reads opinions via item/{id}/index.do?iframe=true but gets 403 on document.do, so court-rule text needs the fetch tool. Public-domain citations (2024 Ark. 181) since 2009; review denials are in Supreme Court proceedings lists found by docket search. Admin rules: the official Code of Arkansas Rules (2025-) is script-readable by NEXT-walking; the legacy SOS rules search is robots-blocked.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Arkansas Supreme Court | `ark (unverified)` | Ark. | Ark., S.W.3d, S.W.2d, S.W. | 2024 Ark. 181 (opinions issued from July 1, 2009) |
| Arkansas Court of Appeals | `arkctapp (unverified)` | Ark. App. | Ark. App., S.W.3d, S.W.2d | 2021 Ark. App. 21 (opinions issued from July 1, 2009) |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Arkansas Code Annotated | `Ark. Code Ann. § 16-56-105`; `Ark. Code Ann. § 4-88-107(a)(10)`; `A.C.A. § 5-10-102`; `Arkansas Code Annotated § 16-56-105`; `section 16-56-105 of the Arkansas Code`; `Ark. Code Ann. §§ 16-56-101 to -130`; `Ark. Code Ann. § 16-114-209 (Repl. 2016)`; `Arkansas Code § 25-15-218` | `ar-code-justia` → `ar-code-lexis` |
| Acts of Arkansas (session laws), with Arkansas marker | `2021 Ark. Acts 276`; `2025 Ark. Acts No. 100`; `Arkansas Act 276 of 2021` | `ar-acts-arkleg` |
| Act N of YYYY (bare, generic) *(only once this jurisdiction is known)* | `Act 276 of 2021`; `Act 1 of the Fiscal Session of 2026` | `ar-acts-arkleg` |
| Arkansas Constitution of 1874 and amendments | `Ark. Const. art. 2, § 13`; `Ark. Const. art. 5, § 32`; `Ark. Const. amend. 80, § 3`; `Ark. Const. amend. 89`; `Article 2, Section 13 of the Arkansas Constitution`; `Amendment 80 to the Arkansas Constitution` | `ar-constitution-justia` → `ar-constitution-sos` → `ar-code-lexis` |
| Arkansas Rules of Civil/Criminal/Appellate Procedure, Evidence, Professional Conduct | `Ark. R. Civ. P. 12(b)(6)`; `Ark. R. Evid. 702`; `Ark. R. App. P.–Civ. 2(a)(1)`; `Ark. R. App. P.-Crim. 3`; `Ark. R. Crim. P. 37.1`; `Ark. R. Prof'l Conduct 1.7`; `Rule 12(b)(6) of the Arkansas Rules of Civil Procedure`; `Arkansas Rule of Evidence 702`; `Arkansas Rule of Criminal Procedure 37.1` | `ar-rules-arcourts` |
| Rules of the Supreme Court and Court of Appeals | `Ark. Sup. Ct. R. 5-2`; `Ark. Sup. Ct. R. 4-3(i)`; `Ark. Sup. Ct. R. 1-2(b)`; `Arkansas Supreme Court Rule 5-2`; `Ark. Ct. App. R. 5-1` | `ar-rules-arcourts` |
| Arkansas court rules (bare forms) *(only once this jurisdiction is known)* | `Rule 5-2`; `Rule 4-3(h)`; `Rule 37.1 petition`; `Rule 2(a)(1)` | `ar-rules-arcourts` |
| Code of Arkansas Rules (CAR, from 2025) | `2 CAR § 1-101`; `20 CAR § 1-101`; `20 C.A.R. § 1-101` | `ar-admincode-car` |
| Arkansas public-domain citations (from July 2009) | `2019 Ark. 123`; `2020 Ark. App. 45`; `Barrett v. State, 2021 Ark. App. 21, at 3`; `Ark. Post-Prison Transfer Bd. v. McGowan, 2024 Ark. 181` | `ar-opinions-arcourts` → `ar-cases-justia` |
| Arkansas Reports / Arkansas Appellate Reports and court parentheticals | `304 Ark. 32`; `104 Ark. App. 1`; `800 S.W.2d 415 (Ark. 1990)`; `(Ark. Ct. App. 2005)`; `(Ark. App. 1998)` | `ar-opinions-arcourts` → `ar-cases-justia` |
| Arkansas appellate docket numbers (generic) *(only once this jurisdiction is known)* | `CR-20-170`; `No. CV-24-373`; `CV-20-480` | `ar-opinions-arcourts` → `ar-review-arcourts` |
| South Western Reporter (regional, generic) *(only once this jurisdiction is known)* | `800 S.W.2d 415`; `617 S.W.3d 287` | `ar-cases-justia` |
| Petition for review / rehearing dispositions (generic) *(only once this jurisdiction is known)* | `review denied`; `petition for review denied`; `reh'g denied` | `ar-review-arcourts` |

Regexes (case-insensitive):

- Arkansas Code Annotated: `(?:Ark(?:ansas|\.)\s*Code(?:\s*Ann(?:otated|\.)?)?|\bA\.\s*C\.\s*A\.)\s*(?:§§?|sec(?:tion|s?\.)s?)?\s*(?P<title>\d{1,2})-(?P<chapter>\d{1,3})-(?P<section>\d{3,4}(?:\.\d+)?)(?![\d-])|(?:sec(?:tion|\.)|§)\s*(?P<title2>\d{1,2})-(?P<chapter2>\d{1,3})-(?P<section2>\d{3,4}(?:\.\d+)?)(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+Arkansas\s+Code`
- Acts of Arkansas (session laws), with Arkansas marker: `(?P<year>(?:18|19|20)\d\d)\s+Ark\.\s*Acts,?\s*(?:No\.\s*)?(?P<act>\d{1,4})|Arkansas\s+Act\s+(?:No\.\s*)?(?P<act2>\d{1,4})\s+of\s+(?P<year2>(?:19|20)\d\d)`
- Act N of YYYY (bare, generic): `\bAct\s+(?:No\.\s*)?(?P<act>\d{1,4})\s+of\s+(?:the\s+(?:Regular|Fiscal|(?:First\s+|Second\s+)?Extraordinary)\s+Session\s+of\s+)?(?P<year>(?:19|20)\d\d)`
- Arkansas Constitution of 1874 and amendments: `Ark\.\s*Const\.,?\s*(?:art\.?\s*(?P<article>\d{1,2}|[IVXL]+),?\s*(?:§|sec\.?|section)\s*(?P<section>\d+)|amend\.?\s*(?P<amendment>\d{1,3})(?:,?\s*(?:§|sec\.?|section)\s*(?P<asection>\d+))?)|Article\s+(?P<article2>\d{1,2}|[IVXL]+),?\s+Section\s+(?P<section2>\d+)\s+of\s+the\s+(?:Arkansas\s+Constitution|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Arkansas)|Amendment\s+(?P<amendment2>\d{1,3})\s+(?:to|of)\s+the\s+Arkansas\s+Constitution`
- Arkansas Rules of Civil/Criminal/Appellate Procedure, Evidence, Professional Conduct: `Ark\.\s*R\.\s*(?P<set>Civ\.\s*P|Evid|Crim\.\s*P|App\.\s*P\.?\s*[–—-]\s*(?:Civ|Crim)|Prof'?l\s*Conduct)\.?\s*(?P<rule>\d{1,4}(?:\.\d+)?)|Arkansas\s+Rules?\s+of\s+(?P<set2>Civil\s+Procedure|Evidence|Criminal\s+Procedure|Appellate\s+Procedure\s*[–—-]\s*(?:Civil|Criminal)|Professional\s+Conduct)\s*(?P<rule2>\d{1,4}(?:\.\d+)?)|Rule\s+(?P<rule3>\d{1,4}(?:\.\d+)?)(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+Arkansas\s+Rules\s+of\s+(?P<set3>Civil\s+Procedure|Evidence|Criminal\s+Procedure|Appellate\s+Procedure\s*[–—-]\s*(?:Civil|Criminal)|Professional\s+Conduct)`
- Rules of the Supreme Court and Court of Appeals: `Ark\.\s*(?:Sup\.\s*Ct\.|Ct\.\s*App\.)\s*R\.\s*(?P<rule>\d-\d{1,2})|Arkansas\s+(?:Supreme\s+Court|Court\s+of\s+Appeals)\s+Rule\s+(?P<rule2>\d-\d{1,2})`
- Arkansas court rules (bare forms): `\bRule\s+(?P<rule>\d-\d{1,2})(?:\s*\([a-zA-Z0-9]+\))*|\bRule\s+(?P<rule2>37(?:\.\d)?)\s+petition|\bRule\s+(?P<rule3>\d{1,2})\s*\([a-z]\)\s*\(\d\)`
- Code of Arkansas Rules (CAR, from 2025): `(?P<title>\d{1,2})\s+(?:CAR|C\.A\.R\.)\s*§+\s*(?P<part>\d{1,4})-(?P<section>\d{3,4})`
- Arkansas public-domain citations (from July 2009): `\b(?P<year>20\d\d)\s+Ark\.(?P<app>\s*App\.)?\s+(?P<number>\d{1,4})\b`
- Arkansas Reports / Arkansas Appellate Reports and court parentheticals: `\b(?P<vol>\d{1,3})\s+Ark\.(?P<app>\s*App\.)?\s+(?P<page>\d{1,4})\b|\((?P<court>Ark\.(?:\s*(?:Ct\.\s*)?App\.)?)\s*(?:[A-Z][a-z]{2,4}\.?\s*\d{1,2},\s*)?(?P<year>(?:18|19|20)\d\d)\)`
- Arkansas appellate docket numbers (generic): `\b(?P<docket>(?P<type>CV|CR|CA|CACR|CACV|JV|E|D)-(?P<yy>\d{2})-(?P<num>\d{1,4}))\b`
- South Western Reporter (regional, generic): `\b(?P<vol>\d{1,4})\s+S\.\s*W\.\s*(?:2d|3d)?\s+(?P<page>\d{1,5})\b`
- Petition for review / rehearing dispositions (generic): `(?P<disp>(?:pet(?:ition)?\.?\s+for\s+)?review\s+(?:denied|granted)|reh'?g\s+denied)`

No law_aliases: Ark. Code Ann. cites are title-chapter-section; the Justia URL needs a subtitle that is not in the citation (one index hop). 'Ark. Code Ann.', 'A.C.A.', 'Ark. R.', 'Ark. Sup. Ct. R.', 'Ark. Const.' and 'N CAR §' are Arkansas markers; a bare '§ 16-56-105' routes here only with 'of the Arkansas Code'. Ranges ('§§ 16-56-101 to -130') capture only the first section. Arkansas constitution articles are cited with Arabic numerals (art. 2, § 13); amendments are numbered (amend. 80). Public-domain citations 'YYYY Ark. N' / 'YYYY Ark. App. N' (opinions from July 1, 2009, per Ark. Sup. Ct. R. 5-2 from memory) cannot collide with Ark. Reports volumes (official reports ended at about 375 Ark. / 104 Ark. App. in 2009). Court of Appeals rules are in the joint 'Rules of the Supreme Court and Court of Appeals' (Rule N-N). Bare 'Rule 5-2', 'Rule 37.1 petition', dockets 'CR-20-170' and S.W. cites are context_required. Unreported/older unpublished CoA opinions are cited by docket and date; from 2009 every opinion carries a neutral cite.

## A. Statutes / code

### `ar-acts-arkleg` — Acts of Arkansas (session laws), Arkansas State Legislature

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Bureau of Legislative Research · text: **fetch-and-quote** · official: unknown
- **Coverage:** Acts by session (Regular 'R', Fiscal 'F', Extraordinary 'S1'…); verified 2021R, 2025R, 2026F.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F{year}{session}%2FPublic%2FACT{act}.pdf`
  - Placeholders: year = 4 digits; session = R (regular), F (fiscal), S1/S2 (extraordinary — confirm on /Acts/SearchByRange); act unpadded. Listing links use /Acts/FTPDocument?path=%2FACTS%2F2026F%2FPublic%2F&file=1.pdf&ddBienniumSession=2025%2F2026F, which redirects to the url_pattern form.
  - Index: `https://arkleg.state.ar.us/Acts/SearchByRange`
  - Navigation: SearchByRange?ddBienniumSession={biennium}%2F{year}{session} lists acts with PDF links.
- **Automation:** WebFetch untested · shell ok · robots: User-agent: * Allow: / (only ChatGPT agents disallowed)
- **Currency:** none stated
- **Official status:** Act PDFs are the enrolled bills ('Act 100 of the Regular Session'); no authentication statement seen.
- **Hazard:** PDF line numbers interleaved with text
- **Hazard:** stricken/underlined amendment markup lost in text extraction
- **Probe:** Act 276 of 2021 → `https://arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2021R%2FPublic%2FACT276.pdf` — expect: "Act 276 of the Regular Session"
- **Evidence (2026-10-17):** Script: ACT276.pdf (2021R) kind=pdf pages=3 'Act 276 of the Regular Session'; ACT100.pdf (2025R) pages=2 'Regular Session, 2025 SENATE BILL 146'; ACT1.pdf (2026F) pages=4.
- **Notes:** /Acts/CodeSectionsAmended lists Code sections amended by session.

### `ar-code-lexis` — Arkansas Code and Constitution of 1874 (free public access, LexisNexis)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Arkansas Code Revision Commission / LexisNexis · text: **link-only** · official: official
- **Coverage:** Entire Arkansas Code Annotated and the Constitution of 1874, free Lexis Advance container.
- **Access:** `link-only` · format html
  - Placeholders: No per-section URL; the container is navigated interactively.
  - Index: `http://www.lexisnexis.com/hottopics/arcode/`
  - Navigation: Human only: hottopics/arcode/ redirects to advance.lexis.com/container?config=00JAA3ZTU0NTIzYy0zZDEyLTRhYmQtYmRmMS1iMWIxNDgxYWMxZTQKAFBvZENhdGFsb2cubRW4ifTiwi5vLw6cI1uX → TOC → title → subtitle → chapter → subchapter → section. No text reachable by either tool.
- **Automation:** WebFetch untested · shell http-error · robots: advance.lexis.com/robots.txt 404 (no rules); www.lexisnexis.com robots does not cover /hottopics/
  - fetch_doc.py follows the redirect to the advance.lexis.com container and gets kind=html chars=0 (JavaScript app). WebFetch not spent: same container failed for GA and TN.
- **Currency:** not visible (app did not render)
- **Official status:** arkleg.state.ar.us home page links 'Arkansas Code and Constitution of 1874' (exit warning) to http://www.lexisnexis.com/hottopics/arcode/; Lexis publishes the official Ark. Code Ann. under state contract (from memory; no statement visible because the app did not render).
- **Hazard:** JavaScript-only app: empty to both tools
- **Hazard:** no per-section URLs
- **Probe:** Ark. Code Ann. § 16-56-105 → `http://www.lexisnexis.com/hottopics/arcode/`
- **Evidence (2026-10-17):** Link from arkleg.state.ar.us home page (raw HTML). Script: redirect to advance.lexis.com container, kind=html chars=0.
- **Notes:** Use as the citation target for a human reader only; quote from ar-code-justia.

### `ar-code-justia` — Justia — Arkansas Code (2025 edition)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Arkansas Code titles 1-28, current edition labelled '2025 Arkansas Code'; archived editions 2010-2024.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/codes/arkansas/title-{title}/subtitle-{subtitle}/chapter-{chapter}/subchapter-{subchapter}/section-{title}-{chapter}-{section}/`
  - Placeholders: title, chapter, section from the citation, unpadded. subtitle is NOT in the citation: open the title page (lists 'Subtitle N - name', no chapter ranges) or the subtitle page (lists chapter links, no section ranges) to find the subtitle holding the chapter. subchapter = the section's hundreds digit in the usual case (16-56-105 → subchapter-1; 16-56-201 → subchapter-2); the chapter page lists subchapters WITH section ranges ('§§ 16-56-101 to 16-56-130'), so confirm there. Undated path = current edition; /codes/arkansas/2024/… for older editions.
  - Index: `https://law.justia.com/codes/arkansas/title-{title}/`
  - Navigation: title page → subtitle link → chapter link → chapter page lists subchapters with section ranges → section page. Verified: § 16-56-105 → /title-16/subtitle-5/chapter-56/subchapter-1/section-16-56-105/; § 5-10-102 → /title-5/subtitle-2/chapter-10/subchapter-1/section-5-10-102/.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: fetch_doc.py: law.justia.com answered robots.txt with a bot check earlier today (host off for the day, 2026-10-17)
  - Built section URLs went through WebFetch without a permission prompt.
- **Currency:** page heading and disclaimer — observed: "2025 Arkansas Code; These codes may not be the most recent version."
- **Official status:** Each page: 'These codes may not be the most recent version.' (law.justia.com/codes/arkansas/2025/).
- **Hazard:** subtitle hop not derivable from citation
- **Hazard:** tier 2; edition lags session laws
- **Probe:** Ark. Code Ann. § 16-56-105 → `https://law.justia.com/codes/arkansas/title-16/subtitle-5/chapter-56/subchapter-1/section-16-56-105/` — expect: "The following actions shall be commenced within three (3) years"
- **Evidence (2026-10-17):** WebFetch: § 16-56-105 body 'The following actions shall be commenced within three (3) years', complete with History. Second: § 5-10-102 '(a) A person commits murder in the first degree if:' (label '2025 Arkansas Code'). Script REFUSED (host off for day).

## B. Constitution

### `ar-constitution-sos` — Constitution of the State of Arkansas of 1874 (Secretary of State PDF)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Arkansas Secretary of State · text: **link-only** · official: unknown
- **Coverage:** Full constitution through Amendment 87 per its table of contents (per WebFetch).
- **Read via (in order):** **fetch tool**
- **Access:** `link-only` · format pdf
  - Index: `https://ssl-sos-site.ark.org/uploads/education/ArkansasConstitution1874.pdf`
  - Navigation: Single PDF; found by web search (results labelled sos.arkansas.gov); www.sos.arkansas.gov/uploads/education/ArkansasConstitution1874.pdf is 404 and no SOS page linking the ark.org host was found.
- **Automation:** WebFetch ok (truncated) · shell http-error · robots: unreachable: proxy CONNECT 502 to ssl-sos-site.ark.org (twice, 2026-10-17)
  - WebFetch read 100,000 of 125,699 characters; text stopped in Article 5, § 30.
- **Currency:** none stated
- **Official status:** Title page 'CONSTITUTION OF THE STATE OF ARKANSAS OF 1874.'; no edition date or authentication statement.
- **Hazard:** WebFetch truncation at Article 5
- **Hazard:** alternate host not confirmed as linked by SOS pages
- **Hazard:** amendments after 87 may be missing
- **Probe:** Ark. Const. art. 2, § 13 → `https://ssl-sos-site.ark.org/uploads/education/ArkansasConstitution1874.pdf` — expect: "Every person is entitled to a certain remedy in the"
- **Evidence (2026-10-17):** WebFetch: art. 2 § 13 body present ('Every person is entitled to a certain remedy in the'); truncated at 100K chars (Art. 5 § 30). Script: proxy 502. Kept 'reported' because the publisher link to this host is unconfirmed.

### `ar-constitution-justia` — Justia — Arkansas Constitution

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Articles 1-19, amendments, schedule.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/arkansas/article-{article}/section-{section}/`
  - Placeholders: article and section as Arabic integers. Amendments: /constitution/arkansas/amendments/amendment-{n} (seen in search results, not fetched). The article page is an index only.
  - Index: `https://law.justia.com/constitution/arkansas/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: bot check on robots.txt (fetch_doc.py, host off for the day)
- **Currency:** page notice — observed: "This Constitution may not be the most recent version."
- **Official status:** Page notice: 'This Constitution may not be the most recent version.'
- **Hazard:** article page lists section titles only
- **Probe:** Ark. Const. art. 2, § 13 → `https://law.justia.com/constitution/arkansas/article-2/section-13/` — expect: "Every person is entitled to a certain remedy in the"
- **Evidence (2026-10-17):** WebFetch: body present 'Every person is entitled to a certain remedy in the'. /article-2/ is an index (NOT PRESENT).

## C. Court rules

### `ar-rules-arcourts` — Arkansas Court Rules (Arkansas Judiciary, Lexum collection 'cr')

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Arkansas Supreme Court / Administrative Office of the Courts · text: **fetch-and-quote** · official: unknown
- **Coverage:** Each rule set is one document: Civil Procedure (item 16712), Evidence (1876), Appellate Procedure–Civil (1885), Appellate Procedure–Criminal (1884), Rules of the Supreme Court and Court of Appeals (1871), Criminal Procedure (1879), Professional Conduct current (1868), District Court Rules (1878), Code of Judicial Conduct (1874), Amendments-Adoptions-Updates (18217), and others.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://opinions.arcourts.gov/ark/cr/en/{item}/1/document.do`
  - Placeholders: item = rule-set id from the listing (16712 Civ. P., 1876 Evid., 1885 App. P.–Civ., 1884 App. P.–Crim., 1871 Sup. Ct. & Ct. App. Rules, 1879 Crim. P., 1868 Prof. Conduct). The whole rule set is one page; find the rule inside it.
  - Index: `https://opinions.arcourts.gov/ark/cr/en/nav_date.do?iframe=true`
  - Navigation: listing (iframe=true form returns the list to the script) → item/{item}/index.do?iframe=true shows 'Rule Current To' date only → text at {item}/1/document.do (fetch tool).
- **Automation:** WebFetch ok · shell blocked-challenge · robots: opinions.arcourts.gov disallows only 4 specific item URLs for *, and / for BUbiNG
  - fetch_doc.py: listing and item?iframe=true pages 200, but every */document.do tried returned HTTP 403 (refused). WebFetch read 1876/1/document.do (URL from a search result); 16712/1/document.do built from the listing was gated (permission prompt timed out).
- **Currency:** item page 'Rule Current To' field (iframe=true) — observed: "Civ. P.: Rule Current To 10/01/2026; Evid.: 06/04/2026"
- **Official status:** Linked as 'Court Rules' from arcourts.gov; item pages show 'Rule Current To' dates; no official-text statement.
- **Hazard:** script 403 on document.do
- **Hazard:** WebFetch gated for built URLs
- **Hazard:** Civil Procedure document likely > 100K chars
- **Probe:** Ark. R. Evid. 702 → `https://opinions.arcourts.gov/ark/cr/en/1876/1/document.do` — expect: "If scientific, technical, or other specialized knowledge will assist the"
- **Evidence (2026-10-17):** WebFetch: Rule 702 body present, page runs Rule 101 through 1102, not truncated. Script: listing 200 (23 rule sets), item 16712 'Rule Current To 10/01/2026', document.do 403.
- **Notes:** Proposed rule changes: https://arcourts.gov/proposed-rule-changes. Administrative Orders collection: https://opinions.arcourts.gov/ark/ao/en/nav_date.do.

## D. Administrative code

### `ar-admin-rules-sos-legacy` — Arkansas Administrative Rules search (SOS, pre-CAR filings)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Arkansas Secretary of State · text: **link-only** · official: unknown
- **Coverage:** Filed agency rules (notice, proposed, final, emergency) before codification.
- **Access:** `search-only` · format html
  - Index: `http://www.sos.arkansas.gov/rules_and_regs/index.php/rules/search/new`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: www.sos.arkansas.gov: User-agent: * Disallow: /rules_and_regs/
  - Blocked for every route per policy.
- **Currency:** 
- **Hazard:** robots disallow
- **Probe:**  → `http://www.sos.arkansas.gov/rules_and_regs/index.php/rules/search/new`
- **Evidence (2026-10-17):** Script: REFUSED robots.txt on www.sos.arkansas.gov disallows /rules_and_regs/ (link from /rules-regulations/ 'Arkansas Administrative Rules').
- **Notes:** Bulk data is via INA paid subscription ($10 minimum per download), not free.

### `ar-admincode-car` — Code of Arkansas Rules (CAR)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Arkansas Secretary of State / Bureau of Legislative Research · text: **fetch-and-quote** · official: official
- **Coverage:** Codified agency rules, titles 1-27 (parallel to Code titles), from 2025; emergency rules listed separately.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Pattern: `https://codeofarrules.arkansas.gov/Rules/Rule?levelType=section&titleID={title}&chapterID={id}&subChapterID={id}&partID={id}&subPartID={id}&sectionID={id}`
  - Placeholders: Chapter/subchapter/part/subpart/section IDs are internal database ids, not citation numbers. Citation '20 CAR § 1-101' = title 20, part 1, section 101.
  - Index: `https://codeofarrules.arkansas.gov/Rules/RuleQuickSearch?titleNumber={title}&chapterNumber=&subChapterLetter=&partNumber={part}&subPartNumber=&sectionNumber=&appendixNumber=`
  - Navigation: Quick-find GET with title + part (all parameters present, others empty) redirects to the part page; quick-find with a section number returned 'No rule found' in every form tried. From the part page follow NEXT (subpart → first section → next section…) until the heading '{title} CAR § {part}-{section}'. Page links render '&sectionID' as '§ionID' (%C2%A7ionID): repair to '&sectionID=' before following. Verified: 2 CAR § 1-101 (sectionID=54466) and 20 CAR § 1-101 (sectionID=18899).
- **Automation:** WebFetch gated · shell ok · robots: User-agent: * Allow: / (ChatGPT agents disallowed)
  - WebFetch on a built section URL timed out on the permission prompt. Section text is in the page twice (plain and in inline HTML).
- **Currency:** page footer — observed: "Last Updated: 10/12/2026 5:18:46 AM"
- **Official status:** Footer on every page: under Ark. Code § 25-15-218 'This online searchable database constitutes the official version of the Code of Arkansas Rules' (effective January 1, 2025).
- **Hazard:** internal ids, no citation URL
- **Hazard:** '§ionID' entity bug in links
- **Hazard:** quick-find by section number fails
- **Hazard:** updated weekly; may not reflect recent rulemaking
- **Probe:** 20 CAR § 1-101 → `https://codeofarrules.arkansas.gov/Rules/Rule?levelType=section&titleID=20&chapterID=32&subChapterID=123&partID=443&subPartID=3034&sectionID=18899` — expect: "The State Registrar of Vital Records, under the direction of the State Board of Health"
- **Evidence (2026-10-17):** Script: '20 CAR § 1-101. Duties of State Registrar of Vital Records generally.' with body; 2 CAR § 1-101 'To increase the availability of alternative fuels produced in Arkansas'.
- **Notes:** Keyword search form is POST (/Rules/Search); citation search (tbCitation) finds rules citing a Code section.

## D. Administrative register

### `ar-register-sos` — Arkansas Register (monthly report)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Arkansas Secretary of State · text: **fetch-and-quote** · official: unknown
- **Coverage:** Monthly issues (Volume 51 = 2026) listing adopted/emergency rules with docket numbers and effective dates; no rule text. Older issues (2006-2011+) under /uploads/rulesRegs/Arkansas%20Register/.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Placeholders: Recent issue file names vary (January_2025_Register_Report1.pdf); take links from the index.
  - Index: `https://www.sos.arkansas.gov/rules-regulations/arkansas-register/`
  - Navigation: index lists month links → PDF (e.g. http://www.sos.arkansas.gov/uploads/September_2026_Register_Report.pdf).
- **Automation:** WebFetch untested · shell ok · robots: Crawl-delay 5; Disallow /rules_and_regs/ (not the Register uploads)
  - WebFetch hit the session usage limit on the 2011 issue.
- **Currency:** issue cover — observed: "Volume 51 Number 9 September 2026"
- **Hazard:** index of rules only, no rule text
- **Hazard:** inconsistent file names
- **Probe:**  → `https://www.sos.arkansas.gov/uploads/September_2026_Register_Report.pdf` — expect: "ADOPTED RULES AND REGULATIONS"
- **Evidence (2026-10-17):** Script: pdf pages=4 'Volume 51 Number 9 September 2026 … ADOPTED RULES AND REGULATIONS'; 2011 issue pdf pages=10 'Volume XXXV, Number 2 August 2011'.

## E. Case law

### `ar-opinions-arcourts` — Arkansas Judiciary opinions (Supreme Court and Court of Appeals, Lexum)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Arkansas Supreme Court / Reporter of Decisions · text: **fetch-and-quote** · official: official
- **Coverage:** Supreme Court from 1837 (1837 date listing has 13 items), Court of Appeals from 1979 (reported); scanned Ark. Reports for older cases (e.g. 304 Ark. 32 with S.W.2d parallel).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `search-only` · format html
  - Pattern: `https://opinions.arcourts.gov/ark/{court}/en/item/{id}/index.do?iframe=true`
  - Placeholders: court = supremecourt | courtofappeals. id is an internal item number. Find it by (a) date listing https://opinions.arcourts.gov/ark/supremecourt/en/{year}/nav_date.do?iframe=true, or (b) full-text GET search https://opinions.arcourts.gov/ark/en/d/s/index.do?cont={terms}&iframe=true — a quoted docket number (cont=%22CR-20-170%22) returns the opinion plus the proceedings lists that mention it. Searches containing 'Ark.' (citation strings) and the ref= parameter returned 403.
  - Index: `https://opinions.arcourts.gov/ark/supremecourt/en/nav_date.do?iframe=true`
  - Navigation: search/listing → item/{id}/index.do?iframe=true (metadata: Date, Neutral Citation, Docket Number, Author, then full opinion text with slip page numbers) — the script reads this; {id}/1/document.do is the same text for the fetch tool.
- **Automation:** WebFetch ok · shell ok · robots: Disallow for * only 4 specific item/document URLs; BUbiNG disallowed /
  - Script 403 (refused) on document.do, the host root, courtofappeals nav_date listings, and searches containing 'Ark.'; item/{id}/index.do?iframe=true and supremecourt listings return 200. Without iframe=true item pages are only menus. WebFetch reads document.do from search-result URLs; built item URLs were gated. Search engines often index the proceedings ('syllabus') lists instead of opinions. Alternate-path check (2026-10-17, maintainer): the publisher's own year listings link each opinion as item/{id}/index.do and {id}/1/document.do; robots.txt permits item pages, so reading the item page is the publisher's linked case page, not a workaround. The 403s on document.do and other URLs are per-URL refusals and are never retried.
- **Currency:** site footer — observed: "Website last modified: 10/15/2026"
- **Official status:** Item pages carry a 'Neutral Citation' field (2024 Ark. 181; 2021 Ark. App. 21); from July 2009 the court's own web opinions are the official report under Ark. Sup. Ct. R. 5-2 (from memory, rule text not fetched).
- **Hazard:** script 403 on document.do and some listings
- **Hazard:** iframe=true required
- **Hazard:** OCR artifacts in old scanned reports
- **Hazard:** slip pagination only (no S.W.3d page numbers) for post-2009 opinions
- **Probe:** Barrett v. State, 2021 Ark. App. 21 → `https://opinions.arcourts.gov/ark/courtofappeals/en/item/491539/index.do?iframe=true` — expect: "A basic summary of the trial testimony places Barrett’s Rule 37 arguments into context"
- **Evidence (2026-10-17):** Script: item iframe 23,436 chars, 'Neutral Citation 2021 Ark. App. 21', 'Docket Number CR-20-170'; quote VERIFIED at offset 2586. Supreme item 523216: '2024 Ark. 181', CV-24-373. WebFetch: 264176/1/document.do = 304 Ark. 32 (1990), body 'Tom GLAZE, Justice. This is an appeal from the trial'.
- **Notes:** Collections: supremecourt, courtofappeals, cr (court rules), ao (administrative orders). RSS: https://opinions.arcourts.gov/ark/en/rss/index.do.

### `ar-cases-justia` — Justia — Arkansas Supreme Court and Court of Appeals opinions

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Court of Appeals 1979-2026; Supreme Court (year range not checked).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/cases/arkansas/{court}/{year}/{docket-lowercase}.html`
  - Placeholders: court = supreme-court | court-of-appeals; file = lower-case docket (cr-25-323), sometimes with a suffix (cr-24-681-0); confirm on the year page.
  - Index: `https://law.justia.com/cases/arkansas/{court}/{year}/`
  - Navigation: year page → case page (body text + neutral citation) → PDF on cases.justia.com.
  - Read via: cases.justia.com PDFs read by fetch_doc.py (linked from the case page)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: law.justia.com: bot check on robots.txt (script host off for the day); cases.justia.com PDFs fetched by the script without refusal
- **Currency:** none stated
- **Official status:** Third-party compilation.
- **Hazard:** docket suffixes (-0)
- **Probe:** Armstrong v. State, 2026 Ark. App. 374 → `https://law.justia.com/cases/arkansas/court-of-appeals/2026/cr-25-323.html` — expect: "Aechia Armstrong appeals from a Benton County Circuit Court sentencing"
- **Evidence (2026-10-17):** WebFetch: body present, '2026 Ark. App. 374', CR-25-323, Aug. 26, 2026, not truncated. Script verify on cases.justia.com/arkansas/court-of-appeals/2026-cr-25-323.pdf: VERIFIED.

## F. Subsequent history

### `ar-review-arcourts` — Arkansas Supreme Court proceedings lists (petitions for review, rehearing)

- **Status:** VERIFIED 2026-10-17 (research) · **Tier 1** · Arkansas Supreme Court Clerk · text: **fetch-and-quote** · official: unknown
- **Coverage:** Weekly 'ARKANSAS SUPREME COURT PROCEEDINGS OF {date}' lists (titled 'SYLLABUS') in the supremecourt collection, with 'REVIEWS DENIED: Petitions for review were denied today…' by docket; Court of Appeals publishes its own proceedings lists.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `search-only` · format html
  - Pattern: `https://opinions.arcourts.gov/ark/en/d/s/index.do?cont=%22{docket}%22&iframe=true`
  - Placeholders: docket exactly as on the CoA opinion (CR-20-170), quoted. Results include the opinion and every proceedings list naming the docket; a later Supreme Court 'SYLLABUS' item is the review disposition.
  - Index: `https://opinions.arcourts.gov/ark/supremecourt/en/nav_date.do?iframe=true`
  - Navigation: docket search → supremecourt item 'MM-DD-YYYY.SYLLABUS' → item/{id}/index.do?iframe=true → find docket under 'REVIEWS DENIED' / 'REVIEWS GRANTED'.
- **Automation:** WebFetch ok · shell ok · robots: as ar-opinions-arcourts
  - Found by docket number, not only party name. WebFetch read CoA proceedings document.do pages from search results. Alternate-path check (2026-10-17, maintainer): the publisher's own year listings link each opinion as item/{id}/index.do and {id}/1/document.do; robots.txt permits item pages, so reading the item page is the publisher's linked case page, not a workaround. The 403s on document.do and other URLs are per-URL refusals and are never retried.
- **Currency:** list heading — observed: "ARKANSAS SUPREME COURT PROCEEDINGS OF MARCH 18, 2021"
- **Hazard:** search must be by docket, not citation (citation searches 403)
- **Probe:** Barrett v. State, 2021 Ark. App. 21 (CR-20-170) → `https://opinions.arcourts.gov/ark/supremecourt/en/item/494454/index.do?iframe=true` — expect: "Petitions for review were denied today in the following cases"
- **Evidence (2026-10-17):** Script: docket search cont=%22CR-20-170%22 → 4 hits incl. supremecourt item 494454 '03-18-2021.SYLLABUS'; that page: 'REVIEWS DENIED: … CR-20-170. Josh M. Barrett v. State of Arkansas'.
- **Notes:** U.S. Supreme Court cert dispositions are not on this site.

## Not available (do not look for these again)

- **statutes** — Free official bulk download or API of the Arkansas Code: None linked from arkleg.state.ar.us; code is only in the Lexis container. (2026-10-17)
- **admin_code** — Free bulk download of administrative rules: sos.arkansas.gov/rules-regulations/bulk-data-download: INA subscription, $10 minimum per download. (2026-10-17)
- **case_law** — Free S.W.3d pagination for post-2009 opinions: Item pages show neutral citation and slip pages only. (2026-10-17)

## Corpus candidates (maintainers)

- `ar-constitution-sos` — WebFetch stops at Article 5 § 30 (100K of 125,699 chars); script cannot reach host (proxy 502).
- `ar-rules-arcourts` — Whole Rules of Civil Procedure on one page (likely > 100K chars); script gets 403, WebFetch gated for built URL.

## Open questions

- ar-constitution-sos: confirm an SOS page links ssl-sos-site.ark.org (alternate-host rule) and retry the script when the proxy reaches it.
- ar-rules-arcourts: Civil Procedure document (16712) not read by any tool (WebFetch gated, script 403); check length and truncation.
- Court of Appeals coverage start (1979?) on opinions.arcourts.gov not confirmed: courtofappeals listings 403 to the script.
- Ark. Sup. Ct. R. 5-2 (neutral citation, effective July 1, 2009) text not fetched; from memory.
- Tier-2 court rules (Justia / LII) for Arkansas not checked; public.law and Cornell LII coverage of Arkansas statutes not checked.
- ar-code-lexis: WebFetch not tried (assumed empty JS app as for GA/TN).
