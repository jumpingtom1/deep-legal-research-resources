# Connecticut (CT) — free legal sources

_Generated from `data/ct.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: the official General Statutes on cga.ct.gov cannot be read by either route (the script fails TLS verification; the fetch tool reports ROBOTS_DISALLOWED on every cga.ct.gov page except one cached titles index), so Justia's 2025 Connecticut General Statutes (constructible per section, chapter learned from Justia's title page which shows section ranges) is the working fallback. Constitution: the Secretary of the State's Register and Manual page on portal.ct.gov (one ~113K-char page; script reads it whole). Court rules (Practice Book, Code of Evidence) are PDFs on www.jud.ct.gov, which fails TLS for the script and whose built URLs are gated for the fetch tool: reported only. Case law: jud.ct.gov advance-release archives (from July 2000) and Connecticut Law Journal / official-reports PDFs (Conn. from vol. 320, Conn. App. full volumes) are readable by the fetch tool but hrefs are not exposed, so per-opinion text is read on Justia (Supreme 1846-, Appellate 1983-). Cert denials appear as 'Orders' PDFs in the Law Journal (Conn. Reports pages). Regulations: eregulations.ct.gov is a JavaScript shell; Cornell LII serves RCSA sections per URL.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Connecticut Supreme Court | `conn (unverified)` | Conn. | Conn., A.3d, A.2d, A. | — |
| Connecticut Appellate Court | `connappct (unverified)` | Conn. App. Ct. | Conn. App., A.3d, A.2d | — |
| Connecticut Superior Court | `connsuperct (unverified)` | Conn. Super. Ct. | Conn. Supp., Conn. L. Rptr., A.3d, A.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Connecticut General Statutes | `Conn. Gen. Stat. § 52-577`; `Conn. Gen. Stat. Ann. § 42-110b(a)`; `General Statutes § 52-577`; `General Statutes (Rev. to 2019) § 53a-54a`; `General Statutes §§ 52-577 and 52-584`; `§ 42-110b of the Connecticut General Statutes`; `C.G.S. § 52-190a`; `CGS § 4-183` | `ct-statutes-justia` → `ct-statutes-cga` |
| General Statutes prose form (shared with North Carolina) *(only once this jurisdiction is known)* | `section 52-584 of the General Statutes` | `ct-statutes-justia` → `ct-statutes-cga` |
| Connecticut Public Acts (session laws) | `Public Acts 2023, No. 23-45`; `Public Acts 1993, No. 93-228, § 1`; `Conn. Pub. Acts 21-104` | `ct-statutes-cga` |
| Public Act number (bare P.A.) *(only once this jurisdiction is known)* | `P.A. 23-45`; `Public Act 21-104` | `ct-statutes-cga` |
| Connecticut Constitution | `Conn. Const. art. I, § 7`; `Conn. Const., art. I, § 8`; `Conn. Const. art. first, § 7`; `article first, § 7, of the Connecticut constitution`; `Conn. Const. amend. XVII`; `article fifth, § 2, of the constitution of Connecticut`; `Article I, Section 7 of the Connecticut Constitution`; `article XVIII of the amendments to the Connecticut constitution` | `ct-constitution-sots` → `ct-constitution-justia` → `ct-constitution-cga` |
| Connecticut Practice Book | `Practice Book § 10-30`; `Practice Book (2023) § 61-10`; `Conn. Practice Book § 17-49`; `Practice Book §§ 10-6 and 10-30`; `§ 60-5 of the Practice Book`; `P.B. § 63-1` | `ct-rules-practicebook` |
| Connecticut Code of Evidence | `Conn. Code Evid. § 7-2`; `Conn. Code Evid. § 8-3 (1)`; `Connecticut Code of Evidence § 4-5`; `§ 8-6 of the Connecticut Code of Evidence` | `ct-rules-evidence` |
| Code of Evidence (bare, no state marker) *(only once this jurisdiction is known)* | `Code of Evidence § 7-2`; `§ 4-6 of the Code of Evidence` | `ct-rules-evidence` |
| Regulations of Connecticut State Agencies | `Regs., Conn. State Agencies § 22a-174-1`; `Conn. Agencies Regs. § 17b-262-1`; `Conn. Agencies Regs. § 22a-174-1`; `§ 22a-174-1 of the Regulations of Connecticut State Agencies`; `RCSA § 22a-174-1` | `ct-regs-lii` → `ct-regs-eregulations` |
| Connecticut official reports (Conn., Conn. App., Conn. Supp.) | `Alico, LLC v. Somers, 348 Conn. 401 (2023)`; `Unifoods, S.A. de C.V. v. Magallanes, 230 Conn. App. 102 (2024)`; `State v. Overstreet, 232 Conn. App. 273`; `Ventura v. East Haven, 330 Conn. 613, 199 A.3d 1 (2019)`; `45 Conn. Supp. 123`; `26 Conn. L. Rptr. 104` | `ct-official-reports-lawjournal` → `ct-cases-justia` → `ct-opinions-aro` |
| Atlantic Reporter with Connecticut court parenthetical | `199 A.3d 1 (Conn. 2019)`; `123 A.3d 456 (Conn. App. Ct. 2015)`; `750 A.2d 123 (Conn. Super. Ct. 1999)` | `ct-cases-justia` → `ct-opinions-aro` |
| Connecticut docket numbers (SC / AC) *(only once this jurisdiction is known)* | `SC 20748`; `AC 46166`; `Docket No. SC20748` | `ct-opinions-aro` → `ct-cases-justia` |
| Connecticut Superior Court docket numbers | `HHD-CV-19-6112345-S`; `Docket No. FST-CV-21-6052345-S`; `NNH-CV20-6101234-S` | `ct-cases-justia` |
| Westlaw / Lexis unreported Connecticut cites | `2019 WL 1234567 (Conn. Super. Ct. Jan. 2, 2019)`; `2021 Conn. Super. LEXIS 123` | `ct-cases-justia` |
| Certification granted / denied (Conn. Reports orders) | `cert. denied, 345 Conn. 901 (2022)`; `cert. granted, 352 Conn. 910 (2025)`; `cert. denied, 352 Conn. 911, 300 A.3d 120 (2025)` | `ct-cert-orders-lawjournal` |
| cert. denied with regional reporter only *(only once this jurisdiction is known)* | `cert. denied, 300 A.3d 120 (2025)` | `ct-cert-orders-lawjournal` |

Regexes (case-insensitive):

- Connecticut General Statutes: `(?:Conn(?:ecticut)?\.?\s*Gen(?:eral)?\.?\s*Stat(?:utes|s?\.)?(?:\s*Ann\.)?|(?<![\w.])General\s+Statutes(?:\s*\((?:Rev\.|Supp\.)[^)]{0,20}\))?|(?<![\w.])C\.\s*G\.\s*S\.(?:\s*A\.)?|\bCGS)\s*§§?\s*(?P<section>\d{1,2}[a-z]{0,2}-\d{1,4}[a-z]{0,3}(?![\w-]))|(?:sec(?:tion|\.)|§)\s*(?P<section2>\d{1,2}[a-z]{0,2}-\d{1,4}[a-z]{0,3}(?![\w-]))(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Connecticut\s+General\s+Statutes`
- General Statutes prose form (shared with North Carolina): `(?:sec(?:tion|\.)|§)\s*(?P<section>\d{1,2}[a-z]{0,2}-\d{1,4}[a-z]{0,3}(?![\w-]))(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+General\s+Statutes`
- Connecticut Public Acts (session laws): `Public\s+Acts\s+(?P<year>(?:19|20)\d\d),\s*No\.\s*(?P<act>\d{2}-\d{1,3})|Conn\.\s*Pub\.\s*Acts?\s*(?:No\.\s*)?(?P<act2>\d{2}-\d{1,3})`
- Public Act number (bare P.A.): `(?:P\.\s*A\.|Public\s+Act)\s*(?:No\.\s*)?(?P<act>\d{2}-\d{1,3})(?!\d)`
- Connecticut Constitution: `Conn\.\s*Const\.,?\s*(?:art\.\s*(?P<article>[IVXL]+|[a-z]+(?:-[a-z]+)?),?\s*§\s*(?P<section>\d+)|amend\.\s*(?P<amend>[IVXL]+))|article\s+(?P<article2>[IVXL]+|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth),?\s*(?:§|section)\s*(?P<section2>\d+),?\s+of\s+the\s+(?:Connecticut\s+constitution|constitution\s+of\s+Connecticut)|article\s+(?P<amend2>[IVXL]+|[a-z]+(?:-[a-z]+)?)\s+of\s+the\s+amendments\s+to\s+the\s+(?:Connecticut\s+constitution|constitution\s+of\s+Connecticut)`
- Connecticut Practice Book: `(?:(?:Conn(?:ecticut)?\.?\s*)?Practice\s+Book(?:\s*\(\d{4}\))?|(?<![\w.])P\.\s*B\.)\s*§§?\s*(?P<section>\d{1,2}-\d{1,3}[A-Z]?)|(?:sec(?:tion|\.)|§)\s*(?P<section2>\d{1,2}-\d{1,3}[A-Z]?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:Connecticut\s+)?Practice\s+Book`
- Connecticut Code of Evidence: `Conn(?:ecticut)?\.?\s*Code\s*(?:of\s+)?Evid(?:ence|\.)\s*§\s*(?P<section>\d{1,2}-\d{1,2})|(?:sec(?:tion|\.)|§)\s*(?P<section2>\d{1,2}-\d{1,2})(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Connecticut\s+Code\s+of\s+Evidence`
- Code of Evidence (bare, no state marker): `Code\s+of\s+Evidence\s*§\s*(?P<section>\d{1,2}-\d{1,2})|(?:sec(?:tion|\.)|§)\s*(?P<section2>\d{1,2}-\d{1,2})(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Code\s+of\s+Evidence`
- Regulations of Connecticut State Agencies: `(?:Regs\.,?\s*Conn\.\s*State\s+Agencies|Conn\.\s*Agencies\s+Regs\.|(?<![\w.])R\.?C\.?S\.?A\.?)\s*§\s*(?P<section>\d{1,2}[a-z]{0,2}-\d{1,4}[a-z]{0,3}-[\w.]+)|(?:sec(?:tion|\.)|§)\s*(?P<section2>\d{1,2}[a-z]{0,2}-\d{1,4}[a-z]{0,3}-[\w.]+?)\s+of\s+the\s+Regulations\s+of\s+Connecticut\s+State\s+Agencies`
- Connecticut official reports (Conn., Conn. App., Conn. Supp.): `(?P<volume>\d{1,3})\s+Conn\.(?:\s*(?P<series>App\.|Supp\.|L\.\s*Rptr\.|Cir\.\s*Ct\.))?\s+(?P<page>\d{1,4})(?!\d)`
- Atlantic Reporter with Connecticut court parenthetical: `(?P<volume>\d{1,4})\s+A\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})\s*(?:,\s*\d+)?\s*\((?P<court>Conn\.(?:\s*(?:App\.(?:\s*Ct\.)?|Super\.(?:\s*Ct\.)?))?)\s*(?:[A-Z][a-z]{2,3}\.?\s*\d{1,2},\s*)?(?P<year>\d{4})\)`
- Connecticut docket numbers (SC / AC): `(?<![\w-])(?P<court>SC|AC)\s?(?P<docket>\d{5})(?!\d)`
- Connecticut Superior Court docket numbers: `(?<![\w-])(?P<district>[A-Z]{3})-?(?P<case_type>CV|FA|CR|LND|HHB|MV)-?(?P<year>\d{2})-?(?P<number>\d{6,7})-?(?P<suffix>[A-Z])(?![\w-])`
- Westlaw / Lexis unreported Connecticut cites: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Conn\.|Conn\.\s*(?:(?P<lexcourt>Super\.|App\.)\s*)?LEXIS\s+(?P<lexis>\d+))`
- Certification granted / denied (Conn. Reports orders): `cert\.\s*(?P<disposition>denied|granted|dismissed)(?:\s+in\s+part)?,\s*(?P<volume>\d{1,3})\s+Conn\.\s+(?P<page>\d{1,4})`
- cert. denied with regional reporter only: `cert\.\s*(?P<disposition>denied|granted|dismissed),\s*(?P<volume>\d{1,4})\s+A\.(?:\s*[23]d)?\s+(?P<page>\d{1,5})`

Short forms → URL key:

Conn. Gen. Stat. → `CGS`; Conn. Gen. Stat. Ann. → `CGS`; C.G.S. → `CGS`; C.G.S.A. → `CGS`; CGS → `CGS`; General Statutes → `CGS`; Gen. Stat. → `CGS`; Practice Book → `PB`; P.B. → `PB`; Conn. Practice Book → `PB`; Conn. Code Evid. → `CCE`; Code of Evidence → `CCE`; Regs., Conn. State Agencies → `RCSA`; Conn. Agencies Regs. → `RCSA`; RCSA → `RCSA`

Connecticut has no public-domain/vendor-neutral case citation. Connecticut courts cite statutes as 'General Statutes § 52-577' (no 'Conn.'), regulations as 'Regs., Conn. State Agencies § X', rules as 'Practice Book § 10-30' and 'Conn. Code Evid. § 7-2'; Bluebook forms are 'Conn. Gen. Stat. § 52-577' and 'Conn. Agencies Regs. § X'. Bare 'General Statutes § N' routes here because the NN[a]-NNN[a] section shape plus 'General Statutes' is Connecticut usage; if another state's record uses bare 'General Statutes', resolve by context. Statute sections are title-section (52-577, 53a-54a, 22a-174); the chapter is NOT derivable from the section: use Justia's title page (shows chapter section ranges) or cga.ct.gov titles index. A '§§ 52-577 and 52-584' list or '§§ a to b' range is several sections: the regex takes the first. Practice Book sections are chapter-section (10-30, 61-10) and Code of Evidence sections are article-section (7-2); bare 'Code of Evidence § N-N' and bare 'P.A. NN-NN' are context_required (Illinois also uses 'P.A.'). Docket numbers 'SC 20748' / 'AC 46166' are context_required. Official reports pagination: Connecticut Law Journal / Conn. Reports and Conn. App. PDFs carry official page numbers; Justia and advance-release slip opinions do not (Justia shows '0 Conn. App. 1' placeholder). Cert dispositions: CT style is 'cert. denied, 352 Conn. 911 (2025)'; the Conn. volume makes it distinctive; a cert cite with only A.3d is context_required. CourtListener ids from memory, unverified. Amendment articles are also cited in prose as 'article XVIII of the amendments to the Connecticut constitution' (matched). '§ 4-6 of the Code of Evidence' without 'Connecticut' is context_required.

## A. Statutes / code

### `ct-statutes-cga` — General Statutes of Connecticut (cga.ct.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Connecticut General Assembly, Legislative Commissioners' Office · text: **link-only** · official: unknown
- **Coverage:** General Statutes revised to January 1, 2025, plus the 2026 Supplement (separate /2026/sup/ chapter pages holding only amended sections); prior revisions under /{year}/pub/. Also hosts the Constitution and Public Acts.
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.cga.ct.gov/current/pub/chap_{chapter}.htm#sec_{section}`
  - Placeholders: chapter = chapter number as printed, lower-case letter suffix kept (chap_926, chap_735a); anchor sec_{section} (sec_52-577). Chapter is not derivable from the section: titles.htm shows chapter and section ranges per title; title_{title}.htm (title_01, title_52, title_19a) lists chapters. Supplement: /{year}/sup/chap_{chapter}.htm holds only sections amended since the last revision.
  - Index: `https://cga.ct.gov/Current/pub/titles.htm`
  - Navigation: titles.htm (shows 'Chapters 1 to 15e', 'Secs. 1-1 to 1-500' per title) → title_{NN}.htm → chap_{NNN}.htm#sec_{section}; then check /{year}/sup/chap_{NNN}.htm for amendments after the revision date.
- **Automation:** WebFetch blocked · shell tls-error · robots: robots.txt (as served by the same site at prdext3.cga.ct.gov, headed 'robots.txt for https://www.cga.ct.gov') disallows only /cgi-bin/, /asp/menu/, /html/, /images/, /js/ and similar; no rule covers /Current/pub/.
  - Script: 'TLS certificate chain does not verify' on both www.cga.ct.gov and cga.ct.gov. Fetch tool: ROBOTS_DISALLOWED on www.cga.ct.gov/Current/Pub/titles.htm, /Current/pub/title_12.htm, /2025/pub/chap_883.htm, robots.txt itself, and on cga.ct.gov/Current/pub/title_01.htm and title_52.htm; only cga.ct.gov/Current/pub/titles.htm returned content (twice). Built chap_926.htm was permission-gated. Server-node hostnames prdext2/prdext3.cga.ct.gov serve the same site and pass TLS, but no CGA page was found linking to them: not used (alternate-host rule). Policy-table row: the fetch tool's own ROBOTS_DISALLOWED is treated as a robots disallow (blocked for every route); the script separately fails TLS (never disable verification). Re-check route: fetch_doc.py --research check (fails at TLS before a robots verdict) and, only if it clears, one WebFetch.
- **Currency:** titles.htm header — observed: "Revised to January 1, 2025; refer to the 2026 Supplement, revised to January 1, 2026"
- **Official status:** Titles index says the compilation was 'Prepared under the direction of the Legislative Commissioners' Office' (https://cga.ct.gov/Current/pub/titles.htm); no UELMA authentication statement was seen (only one page could be read).
- **Hazard:** neither route can read the official text from this sandbox
- **Hazard:** chapter not derivable from section number
- **Hazard:** annual revision plus separate supplement pages
- **Hazard:** long chapters exceed fetch-tool window
- **Probe:** Conn. Gen. Stat. § 52-577 → `https://www.cga.ct.gov/current/pub/chap_926.htm` — expect: "No action founded upon a tort shall be brought but"
- **Evidence (2026-10-17):** Script: TLS certificate chain does not verify (www and bare host). WebFetch: ROBOTS_DISALLOWED on 6 cga.ct.gov URLs; chap_926.htm gated. Only titles.htm read: 'Revised to January 1, 2025'. | Re-confirmed blocked 2026-10-17: fetch_doc.py --research check: 'TLS certificate chain does not verify' (exit 4)
- **Notes:** The fetch tool's robots refusal does not match the robots.txt text read via prdext3 (no Disallow for /Current/pub/); recorded as blocked because no permitted route returns text. Re-test when the TLS chain or the fetch tool's robots reading changes.

### `ct-statutes-justia` — Justia — Connecticut General Statutes (2025)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Connecticut General Statutes, per-section pages; unversioned URL serves the 2025 edition (chapter listing pages headed 2024).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/connecticut/title-{title}/chapter-{chapter}/section-{section}/`
  - Placeholders: title = the part of the section before the hyphen, lower-case (title-52, title-42, title-53a, title-22a); chapter = chapter number with letter suffix (chapter-926, chapter-735a), learned from the title page, which shows '(Secs. 52-573 to 52-598a)' per chapter; section verbatim (section-52-577, section-42-110b).
  - Index: `https://law.justia.com/codes/connecticut/title-{title}/`
  - Navigation: title page (chapter list with section ranges) → pick chapter whose range covers the section → section URL.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable to the script (Cloudflare challenge)
  - fetch_doc.py: 'law.justia.com refused automated access earlier (robots.txt challenge)'. Use the fetch tool only. Built section URLs were not gated.
- **Currency:** page heading and Universal Citation line — observed: "2025 Connecticut General Statutes; 'CT Gen Stat § 52-577. (2025)'"
- **Official status:** Section page disclaimer: 'These codes may not be the most recent version.'
- **Hazard:** edition lags the official revision
- **Hazard:** shell blocked by Cloudflare
- **Hazard:** chapter must be looked up on the title page
- **Probe:** Conn. Gen. Stat. § 52-577 → `https://law.justia.com/codes/connecticut/title-52/chapter-926/section-52-577/` — expect: "No action founded upon a tort shall be brought but"
- **Evidence (2026-10-17):** WebFetch: body present, 'No action founded upon a tort shall be brought but'; '2025 Connecticut General Statutes'. Second: /title-42/chapter-735a/section-42-110b/ 'No person shall engage in unfair methods of competition and'. Title-52 page shows '(Secs. 52-573 to 52-598a)' for ch. 926. | Independent check 2026-10-17: YES 'No action founded upon a tort shall be brought but'; '2025 Connecticut General Statutes'; second citation General Statutes § 53a-54a ok
- **Notes:** Only route that returns statute text in this environment. public.law and Cornell LII do not host the Connecticut statutes (not found).

## B. Constitution

### `ct-constitution-cga` — Connecticut Constitution (cga.ct.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Connecticut General Assembly · text: **link-only** · official: unknown
- **Coverage:** Constitution and historical constitutions under /asp/Content/constitutions/ (1818 Constitution page seen in search results).
- **Access:** `link-only` · format html
  - Index: `https://www.cga.ct.gov/asp/content/constitutions/1818Constitution.htm`
- **Automation:** WebFetch blocked · shell tls-error · robots: no Disallow for /asp/Content/ seen
  - Same host refusals as ct-statutes-cga; not probed separately. Policy-table row: the fetch tool's own ROBOTS_DISALLOWED is treated as a robots disallow (blocked for every route); the script separately fails TLS (never disable verification). Re-check route: fetch_doc.py --research check (fails at TLS before a robots verdict) and, only if it clears, one WebFetch.
- **Currency:** unknown
- **Official status:** Not readable; see ct-statutes-cga.
- **Hazard:** host unreadable from this sandbox
- **Probe:** Conn. Const. (1818) — index → `https://www.cga.ct.gov/asp/content/constitutions/1818Constitution.htm`
- **Evidence (2026-10-17):** Host-level: script TLS failure; fetch tool ROBOTS_DISALLOWED on www.cga.ct.gov. | Re-confirmed blocked 2026-10-17: fetch_doc.py --research check: 'TLS certificate chain does not verify' (exit 4)

### `ct-constitution-sots` — Constitution of the State of Connecticut (Register and Manual)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Connecticut Secretary of the State · text: **fetch-and-quote** · official: unknown
- **Coverage:** 1965 Constitution (articles first-fourteenth as adopted) followed by Articles of Amendment I onward; last 'Adopted' date on the page is November 30, 2022.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://portal.ct.gov/SOTS/Register-Manual/Section-I/Constitution-of-the-State-of-Connecticut`
  - Placeholders: single page; locate 'ARTICLE FIRST.' … then 'SEC. {n}.'; amended sections carry a note '(Sec. 8 amended in 1982. See Art. XVII of Amendments ...)' — read the amendment article too. Amendments are headed 'ARTICLE {Roman}.'
  - Index: `https://portal.ct.gov/SOTS/Register-Manual/Section-I/Constitution-of-the-State-of-Connecticut`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: portal.ct.gov: Allow / with Disallows for /sitecore/* and beta paths only
  - Page text ~113-114K chars; the fetch tool stops at 100K (mid Art. XXIX of the amendments) — use offset=100000 or the script, which reads it whole.
- **Currency:** none stated; last amendment's 'Adopted' line — observed: "Adopted November 30, 2022."
- **Official status:** Published in the Secretary of the State's Register and Manual on portal.ct.gov; no official/authentication statement on the page; the fetch tool reported a canonical URL with 'archived=true'.
- **Hazard:** amendments printed separately from the articles they amend
- **Hazard:** page exceeds fetch-tool window
- **Hazard:** may not show amendments approved after 2022
- **Hazard:** amended sections appear twice (original article text and the amendment article, e.g. art. I § 8 at offsets ~6031 and ~78528): quote the amendment-article version
- **Probe:** Conn. Const. art. I, § 7 → `https://portal.ct.gov/SOTS/Register-Manual/Section-I/Constitution-of-the-State-of-Connecticut` — expect: "The people shall be secure in their persons, houses, papers and possessions"
- **Evidence (2026-10-17):** fetch_doc.py verify: VERIFIED exact at offset 5219 (113,252 chars). Second: art. I § 8 'In all criminal prosecutions, the accused shall have a right'. WebFetch: § 7 present, truncated at 100,000 of 114,066 chars. | Independent check 2026-10-17: script grep 'The people shall be secure in their persons' offset 5219; last 'Adopted November 30, 2022.'; second citation Conn. Const. art. I, § 8 ok
- **Notes:** Whether the November 2024 ballot amendment (no-excuse absentee voting) is missing is unverified: no 2024 date found on the page.

### `ct-constitution-justia` — Justia — Connecticut Constitution

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole constitution and amendments on one page.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/connecticut/`
  - Placeholders: single page
  - Index: `https://law.justia.com/constitution/connecticut/`
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: unreadable (Cloudflare)
  - 112,710 chars; fetch tool reads 100K, use offset=100000 for late amendments.
- **Currency:** none stated — observed: "Approved at referendum on December 14, 1965"
- **Official status:** Third-party compilation; no currency statement.
- **Hazard:** page exceeds fetch-tool window
- **Hazard:** no currency date
- **Probe:** Conn. Const. art. I, § 7 → `https://law.justia.com/constitution/connecticut` — expect: "The people shall be secure in their persons, houses, papers"
- **Evidence (2026-10-17):** WebFetch: art. I § 7 present, 'The people shall be secure in their persons, houses, papers'; one page, 112,710 chars. | Independent check 2026-10-17: YES 'The people shall be secure in their persons, houses, papers'; 112,710 chars, truncated at 100K

## C. Court rules

### `ct-rules-evidence` — Connecticut Code of Evidence (2023 Edition)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Connecticut Judicial Branch · text: **link-only** · official: unknown
- **Coverage:** Code of Evidence with commentary.
- **Access:** `link-only` · format pdf
  - Index: `https://www.jud.ct.gov/pub.htm`
  - Navigation: pub.htm → 'Connecticut Code of Evidence, 2023 Edition' (href not exposed to the fetch tool).
- **Automation:** WebFetch untested · shell tls-error · robots: unreadable (TLS handshake failure)
  - PDF URL not discovered; jud.ct.gov pages lose their hrefs in the fetch tool.
- **Currency:** publications page link text — observed: "Connecticut Code of Evidence, 2023 Edition"
- **Official status:** Listed on https://www.jud.ct.gov/pub.htm as 'Connecticut Code of Evidence, 2023 Edition'; a law library post notes an amendment to § 7-3 effective May 2, 2023.
- **Hazard:** PDF URL unknown
- **Probe:** Conn. Code Evid. § 7-2 → ``
- **Evidence (2026-10-17):** pub.htm (WebFetch) shows the 2023 Edition link text; no URL readable.

### `ct-rules-practicebook` — Connecticut Practice Book (official annual edition)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Connecticut Judicial Branch · text: **link-only** · official: unknown
- **Coverage:** Superior Court rules (civil, family, criminal, juvenile), Appellate Procedure (chs. 60-86), Rules of Professional Conduct, Code of Judicial Conduct; one large annual PDF; amendments published in the Connecticut Law Journal.
- **Access:** `link-only` · format pdf
  - Index: `https://www.jud.ct.gov/pub.htm`
  - Navigation: pub.htm → 'Connecticut Practice Book' (href not exposed to the fetch tool; from memory https://www.jud.ct.gov/Publications/PracticeBook/PB.pdf).
- **Automation:** WebFetch blocked · shell tls-error · robots: unreadable: SSLV3_ALERT_HANDSHAKE_FAILURE fetching robots.txt
  - Fetch tool: ROBOTS_DISALLOWED on https://www.jud.ct.gov/Publications/PracticeBook/PB.pdf (independent check 2026-10-17; earlier the same URL was permission-gated). Under the policy table this is a robots disallow: blocked for every route. Other www.jud.ct.gov /lawjournal/ PDFs read fine. Script: TLS handshake failure on jud.ct.gov.
- **Currency:** unknown
- **Official status:** Listed on the Judicial Branch publications page (https://www.jud.ct.gov/pub.htm) under Court Rules; the PDF itself could not be opened.
- **Hazard:** single PDF of several hundred pages will truncate in the fetch tool
- **Hazard:** PDF URL unconfirmed
- **Hazard:** PB.pdf path refused by the fetch tool as robots-disallowed
- **Probe:** Practice Book § 10-30 → `https://www.jud.ct.gov/Publications/PracticeBook/PB.pdf`
- **Evidence (2026-10-17):** WebFetch PB.pdf: ROBOTS_DISALLOWED (independent check); script: SSLV3_ALERT_HANDSHAKE_FAILURE; pub.htm lists 'Connecticut Practice Book' with no year.
- **Notes:** No tier-2 host (Justia, LII, public.law) carries the Practice Book.

## D. Administrative code

### `ct-regs-eregulations` — Connecticut eRegulations System — Regulations of Connecticut State Agencies

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Connecticut Secretary of the State · text: **link-only** · official: unknown
- **Coverage:** RCSA by title/subtitle/section, plus proposed, emergency and final-approved regulations, public notices and regulation-making records (the state's notice function).
- **Access:** `index-anchored` · format html
  - Pattern: `https://eregulations.ct.gov/eRegsPortal/Browse/RCSA/Title_{title}Subtitle_{subtitle}Section_{section}`
  - Placeholders: Seen in a search result: Title_20Subtitle_20-406Section_20-406-2-20-406-3 (sections can be grouped). Not confirmed to deliver text.
  - Index: `https://eregulations.ct.gov/eRegsPortal/Browse/RCSA`
  - Navigation: JavaScript application: the served HTML contains only navigation.
- **Automation:** WebFetch fail · shell ok · robots: none (404)
  - Both routes receive only the shell (~2.2K chars, 'Browse>List of Titles', no regulation text); no JSON endpoint identified.
- **Currency:** none in served HTML
- **Official status:** Hosted by the Office of the Secretary of the State; no official-text statement visible in the served HTML.
- **Hazard:** JavaScript-only content
- **Probe:** Regs., Conn. State Agencies § 20-406-2 → `https://eregulations.ct.gov/eRegsPortal/Browse/RCSA/Title_20Subtitle_20-406Section_20-406-2-20-406-3`
- **Evidence (2026-10-17):** WebFetch: NOT PRESENT, navigation only. Script: HTTP 200, 2,223 chars of navigation for a Title_22a… URL; Browse/RCSA has 0 title links.

### `ct-regs-lii` — Cornell LII — Connecticut Administrative Code (RCSA)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute · text: **fetch-and-quote** · official: unofficial
- **Coverage:** RCSA by title, part and section, with version comparison.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/connecticut/Regs-Conn-State-Agencies-SS-{section}`
  - Placeholders: section verbatim incl. both hyphens (22a-174-1, 17b-262-1). Title index: /regulations/connecticut/title-{title}; part index /title-{title}/{part} (e.g. title-22a/174). Letter-bearing section suffixes work as-is (Regs-Conn-State-Agencies-SS-19a-36-A2).
  - Index: `https://www.law.cornell.edu/regulations/connecticut/title-{title}`
- **Automation:** WebFetch ok · shell ok · robots: not blocking /regulations/ (script allowed)
- **Currency:** below section text — observed: "State regulations are updated quarterly; we currently have two versions available."
- **Official status:** Third-party; 'State regulations are updated quarterly; we currently have two versions available.'
- **Hazard:** quarterly lag behind eRegulations
- **Probe:** Conn. Agencies Regs. § 22a-174-1 → `https://www.law.cornell.edu/regulations/connecticut/Regs-Conn-State-Agencies-SS-22a-174-1` — expect: "Except as may otherwise be provided"
- **Evidence (2026-10-17):** fetch_doc.py verify: VERIFIED exact (37,231 chars). Second: Regs-Conn-State-Agencies-SS-17b-262-1 'Effective June 4, 1996'. WebFetch on title-22a index OK. | Independent check 2026-10-17: script grep 'Except as may otherwise be provided' offset 1629; 'State regulations are updated quarterly'; second citation Regs., Conn. State Agencies § 19a-36-A2 ok
- **Notes:** Section URL learned from the part page's link (fetch_doc.py links).

## D. Administrative register

### `ct-register-eregulations` — eRegulations — notices, proposed, emergency and final approved regulations

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Connecticut Secretary of the State · text: **link-only** · official: unknown
- **Coverage:** Public notices, regulation-making records, recently published RCSA sections.
- **Access:** `link-only` · format html
  - Index: `https://eregulations.ct.gov/eRegsPortal/Browse/RecentlyPublishedRCSASections`
- **Automation:** WebFetch untested · shell ok · robots: none (404)
  - Same JavaScript shell as the RCSA browse pages (inferred, not probed separately).
- **Currency:** none
- **Official status:** Connecticut has no separate administrative register; the Law Journal FAQ refers readers to the 'Connecticut eRegulations System website'.
- **Hazard:** JavaScript-only content
- **Probe:**  → ``
- **Evidence (2026-10-17):** Links seen on the eRegulations navigation (script links): Public Notices, Regulation-Making Records, Final Approved Regulations.

## E. Case law

### `ct-official-reports-lawjournal` — Connecticut Law Journal — Connecticut Reports and Connecticut Appellate Reports (official pagination)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Connecticut Judicial Branch (Reporter of Judicial Decisions) · text: **fetch-and-quote** · official: official
- **Coverage:** Law Journals published after June 13, 2017 (FAQ); Conn. Reports from vol. 320 in release segments ('Connecticut Reports Vol.353 Pages 564 - 665'); full Conn. App. volumes as single PDFs (AP108 = 2008).
- **Read via (in order):** **fetch tool**
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.jud.ct.gov/lawjournal/Docs/{Appellate|CTReports}/{year}/{issue}/{prefix}{volume}_{serial}.pdf`
  - Placeholders: From search results: Appellate/2025/27/md233_8701.pdf (memorandum decisions, 233 Conn. App.), CTReports/2025/27/ord352_8701.pdf (orders, 352 Conn.), Appellate/FullVolume/AP108.pdf. {serial} is shared by documents of the same Law Journal issue (8701 = July 1, 2025 issue 27); not derivable from a citation.
  - Index: `https://jud.ct.gov/LawJournal/CR/ConnecticutReports.aspx`
  - Navigation: Works ONLY when a PDF URL is already in hand (e.g. from a web-search result such as 'jud.ct.gov/lawjournal/Docs ... md233'). The listing pages (ConnecticutReports.aspx, AppellateReports.aspx) show no links to the fetch tool and served a stale copy (newest entry 01/20/2026, Vol. 354), so a Conn. cite cannot be turned into a PDF from the listing. Otherwise fall back to ct-cases-justia (slip pagination).
- **Automation:** WebFetch ok (truncated) · shell tls-error · robots: unreadable (TLS handshake failure)
  - Per-issue PDFs fit the fetch tool; full volumes (AP108: 112,939 chars of text) truncate at 100K.
- **Currency:** Law Journal running head — observed: "CONNECTICUT LAW JOURNAL July 1, 2025"
- **Official status:** AP108.pdf title page: 'Official Connecticut Appellate Reports, Volume 108'; Law Journal PDFs carry Conn./Conn. App. running heads with official page numbers.
- **Hazard:** URLs not derivable; listing hrefs invisible
- **Hazard:** full-volume PDFs truncate
- **Hazard:** listing page showed only the newest volume
- **Hazard:** listing pages expose no hrefs and serve a stale copy (newest 01/20/2026 in Oct 2026)
- **Probe:** 108 Conn. App. 1 (Cabral v. Commissioner of Correction) → `https://www.jud.ct.gov/lawjournal/Docs/Appellate/FullVolume/AP108.pdf` — expect: "CABRAL v. COMMISSIONER OF CORRECTION"
- **Evidence (2026-10-17):** WebFetch AP108.pdf: 'Official Connecticut Appellate Reports, Volume 108'; first case Cabral at page 1; truncated at 100K. md233_8701.pdf: '233 Conn. App. MEMORANDUM DECISIONS 903'. | Independent check 2026-10-17: AP108.pdf 'OFFICIAL CONNECTICUT APPELLATE REPORTS Volume 108'; Cabral at p. 1; truncated at 100K; second citation 233 Conn. App. 903 (md233_8701.pdf) ok
- **Notes:** Only free source with official Conn./Conn. App. pagination for recent volumes.

### `ct-opinions-aro` — Advance Release Opinions and archives (Supreme and Appellate Courts)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Connecticut Judicial Branch · text: **link-only** · official: unofficial
- **Coverage:** Supreme and Appellate Court opinions officially released from July 2000; yearly archive pages archiveAROsup{yy}.htm (Supreme) and archiveAROap{yy}.htm (Appellate), plus a memorandum-decision archive.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://jud.ct.gov/external/supapp/archiveAROsup{yy}.htm`
  - Placeholders: yy = two-digit year (archiveAROsup04.htm, archiveAROap05.htm, from search results); current: /external/supapp/aro.htm.
  - Index: `https://jud.ct.gov/external/supapp/archiveAROsup.htm`
  - Navigation: archive index (years 2000-2026) → year page: entries 'SC16446 - State v. Colon' grouped under 'Published in Connecticut Law Journal - 12/28/04' → PDF link. The fetch tool strips the hrefs, so the PDF cannot be followed: read the opinion on ct-cases-justia: same docket in its URL only for recent years; older years via Justia's year listing.
  - Read via: ct-cases-justia: docket-slug URL only for recent years (confirmed 2016, 2023-2025); for older years find the case on Justia's year listing (/cases/connecticut/{court}/{year}/), whose slugs are volume-based (2004/272cr131.html, 2005/92ap28.html). jud.ct.gov PDFs unreachable: script TLS failure, hrefs invisible to the fetch tool.
- **Automation:** WebFetch ok · shell tls-error · robots: unreadable (SSLV3_ALERT_HANDSHAKE_FAILURE)
  - Built archiveAROsup24.htm was permission-gated; archiveAROsup04.htm (from search) read fine. Answers 'NO URLS' when asked for link targets.
- **Currency:** aro.htm header date — observed: "Friday, January 16, 2026 (as served to the fetch tool)"
- **Official status:** ARO page: opinions 'subject to modification and technical correction prior to official publication'; 'the latest print version is to be considered authoritative'.
- **Hazard:** hrefs not visible to the fetch tool
- **Hazard:** slip pagination, not official
- **Hazard:** fetch tool may serve a stale copy (Jan 2026 page in Oct 2026)
- **Hazard:** handoff to Justia by docket fails for older cases (AC25704 of 2005 is Justia 2005/92ap28.html)
- **Probe:** State v. Colon (SC16446, released 12/28/04) → `https://jud.ct.gov/external/supapp/archiveAROsup04.htm` — expect: "SC16446 - State v. Colon"
- **Evidence (2026-10-17):** WebFetch: 'SC16446 - State v. Colon' under 'Published in Connecticut Law Journal - 12/28/04'; index covers July 2000 to 2026; no hrefs. | Independent check 2026-10-17: YES 'SC16446 - State v. Colon' under 'Published in Connecticut Law Journal - 12/28/04'; no hrefs; archiveAROap05.htm lists AC25704 (listing ok; Justia docket handoff failed)
- **Notes:** Listing locates (court, docket, release date); no plain-GET search found.

### `ct-cases-justia` — Justia — Connecticut Supreme Court and Appellate Court decisions

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1846-2026; Appellate Court 1983-2026. Docket-slug URLs confirmed only for 2016 and 2023-2025; older years use volume-based slugs.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/connecticut/{court}/{year}/{docket}.html`
  - Placeholders: Docket-slug era only (confirmed 2016, 2023, 2024, 2025): court = supreme-court | court-of-appeals (Appellate Court); docket lower-case, no space (sc20748, ac46166, ac47975); year = decision year. OLDER years use volume-based slugs ({vol}cr{n}.html for Supreme, e.g. 2004/272cr131.html State v. Colon; {vol}ap{n}.html for Appellate, e.g. 2005/92ap28.html Dickinson v. Mullaney) that cannot be built: take the URL from the year listing /cases/connecticut/{court}/{year}/. The cutover year between slug styles is unconfirmed: if a built docket URL errors, fall back to the year listing. PDF: https://cases.justia.com/connecticut/{court}/{year}-{docket}.pdf (linked from the case page).
  - Index: `https://law.justia.com/cases/connecticut/supreme-court/`
  - Navigation: Recent years: build the docket URL. Older years (or any built URL that errors): year listing /cases/connecticut/{court}/{year}/ → find case by name/docket → follow its link.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare)
- **Currency:** year listing — observed: "Connecticut Supreme Court Decisions 2023"
- **Official status:** Third-party copy of slip opinions; appellate page notes the advance release version may be modified.
- **Hazard:** slip pagination only; no Conn. cite ('0 Conn. App. 1' placeholder)
- **Hazard:** shell blocked
- **Hazard:** docket-based URL fails for older years (built 2004/sc16446.html errored; real slug 2004/272cr131.html): use the year listing
- **Probe:** Alico, LLC v. Somers (SC20748, Dec. 19, 2023) → `https://law.justia.com/cases/connecticut/supreme-court/2023/sc20748.html` — expect: "General Statutes § 12-71 (f) (1)"
- **Evidence (2026-10-17):** WebFetch: full opinion, starts 'General Statutes § 12-71 (f) (1)1 authorizes Connecticut towns to'; not truncated. Second: court-of-appeals/2024/ac46166.html 'MOLL, J. The plaintiff, Unifoods, S.A. de C.V., appeals from'. | Independent check 2026-10-17: YES body starts 'General Statutes § 12-71 (f) (1)1 authorizes Connecticut towns'; not truncated; second citation AC47975 (2025) ok, but State v. Colon SC16446 (2004) docket URL failed (volume slug 272cr131.html)

## F. Subsequent history

### `ct-cert-orders-lawjournal` — Connecticut Law Journal — Orders on petitions for certification (Connecticut Reports)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Connecticut Judicial Branch · text: **fetch-and-quote** · official: official
- **Coverage:** Supreme Court orders granting/denying certification to appeal from the Appellate Court, by Law Journal issue (from vol. 320 / mid-2017).
- **Read via (in order):** **fetch tool**
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.jud.ct.gov/lawjournal/Docs/CTReports/{year}/{issue}/ord{volume}_{serial}.pdf`
  - Placeholders: Not derivable from the decision below; ConnecticutReports.aspx lists 'Orders Vol.354 Pages 901 - 901' by release date.
  - Index: `https://jud.ct.gov/LawJournal/CR/ConnecticutReports.aspx`
  - Navigation: Works ONLY with a PDF URL already in hand (web search for the case name or Conn. App. cite plus 'jud.ct.gov lawjournal ord' found ord352_8701.pdf and others). The listing page shows no links to the fetch tool and served a stale copy (newest 01/20/2026). No docket lookup; in practice found by party name or Conn. App. cite.
- **Automation:** WebFetch ok · shell tls-error · robots: unreadable (TLS handshake failure)
  - hrefs on the listing page are invisible to the fetch tool.
- **Currency:** order entry — observed: "Decided June 17, 2025"
- **Official status:** Orders are paginated in the Connecticut Reports ('ORDERS 910 352 Conn.').
- **Hazard:** no lookup by docket
- **Hazard:** listing hrefs invisible
- **Hazard:** listing page stale (newest 01/20/2026) and without visible hrefs
- **Probe:** State v. Overstreet, 232 Conn. App. 273, cert. denied (352 Conn.) → `https://www.jud.ct.gov/lawjournal/Docs/CTReports/2025/27/ord352_8701.pdf` — expect: "petition for certification to appeal"
- **Evidence (2026-10-17):** WebFetch: 'Certification Petition Denials, June 17, 2025'; State v. Overstreet, 232 Conn. App. 273 (AC 46253) denied; running heads 'ORDERS 910 352 Conn.'. | Independent check 2026-10-17: YES 'petition for certification to appeal'; Overstreet 232 Conn. App. 273 denied; 'ORDERS 910 352 Conn.'
- **Notes:** Justia does not carry cert orders.

## Not available (do not look for these again)

- **statutes** — Connecticut General Statutes on public.law or Cornell LII: Not found in searches; only Justia hosts them among tier-2 hosts. (2026-10-17)
- **court_rules** — Tier-2 copy of the Practice Book or Code of Evidence: Justia/LII/public.law do not carry them; search results show only non-vetted third parties. (2026-10-17)
- **case_law** — Public-domain / vendor-neutral citation: Connecticut cites Conn./Conn. App./A.3d only. (2026-10-17)

## Corpus candidates (maintainers)

- `ct-rules-practicebook` — Single annual PDF of all court rules, far beyond the fetch tool's window; currently blocked (fetch tool ROBOTS_DISALLOWED, script TLS failure) — ingest only if the block clears.
- `ct-rules-evidence` — Code of Evidence (2023 Edition) PDF with commentary; URL not discovered.
- `ct-constitution-sots` — 113K-char single page; fetch tool stops mid amendment Art. XXIX.
- `ct-statutes-cga` — Long chapter pages would truncate; currently unreadable (TLS / fetch-tool robots refusal). · bulk: none found

## Open questions

- cga.ct.gov: why does the fetch tool report ROBOTS_DISALLOWED when robots.txt (read at prdext3.cga.ct.gov) has no matching Disallow? Re-test; if it clears, verify chap_926.htm#sec_52-577 and a second title.
- jud.ct.gov: TLS handshake failure (SSLV3_ALERT_HANDSHAKE_FAILURE) for the script; confirm Practice Book PDF URL and edition string, Code of Evidence PDF URL.
- Advance-release opinion PDF URL pattern (believed /external/supapp/Cases/AROcr/CR{vol}/{vol}CR{n}.pdf) not confirmed.
- Superior Court decisions: whether jud.ct.gov publishes a searchable memorandum-of-decision database (not probed).
- Official bulk download of the General Statutes: none found.
- Constitution page: does it include the 2024 amendment?
- Justia CT cases: the year in which slugs switch from volume-based ({vol}cr{n}/{vol}ap{n}) to docket-based is unconfirmed (docket slugs seen 2016, 2023-2025).
- jud.ct.gov Practice Book PDF: fetch tool now ROBOTS_DISALLOWED; confirm against jud.ct.gov robots.txt once the TLS handshake works.
