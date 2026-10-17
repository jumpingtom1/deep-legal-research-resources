# Hawaii (HI) — free legal sources

_Generated from `data/hi.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: the legislature's HRS (www.capitol.hawaii.gov) is Cloudflare-walled — script refused, fetch tool gated per URL — and its data. alternate hostname is excluded by policy, so HRS text comes from Justia (2025, tier 2, disclosed; title lookup hop). Constitution: lrb.hawaii.gov one-page text (script-readable); Justia per-article pages are stale. Court rules are HTML/PDF on courts.state.hi.us, which refuses the script route and truncates in WebFetch (HRCP at Rule 17, HRAP at Rule 32, HRPP HTML ends at Rule 36, RSCH at 2.3); the Rules of Evidence are statute (HRS ch. 626). HAR has no central official site (agency PDFs via the Lt. Governor's directory; Cornell LII per section); there is no administrative register. Case law: the Judiciary's opinions listing (2010-) is GET-filterable by year but has no docket search; Justia covers 1980- ICA and Supreme Court by docket slug. Cert dockets reuse the ICA number (CAAP-YY-N → SCWC-YY-N).

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Hawai'i | `haw (unverified)` | Haw. | Haw., Hawai'i (vols. 76+, cited 'Haw.' in Bluebook), P.3d, P.2d | — |
| Intermediate Court of Appeals of Hawai'i | `hawapp (unverified)` | Haw. Ct. App. | Haw. App. (vols. 1-10, 1980-1994), Haw. (from vol. 76), P.3d, P.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Hawaii Revised Statutes | `Haw. Rev. Stat. § 657-7`; `HRS § 657-7`; `HRS § 708-821(1)(b)`; `Haw. Rev. Stat. Ann. § 663-31 (LexisNexis 2025)`; `HRS § 431:10C-301`; `HRS § 657-1.5`; `Hawaii Revised Statutes § 708-821`; `section 657-7, Hawaii Revised Statutes`; `section 663-31 of the Hawai'i Revised Statutes`; `HRS §§ 657-7 to -13`; `HRS chapter 92F`; `chapter 514B, Hawaii Revised Statutes` | `hi-hrs-justia` → `hi-hrs-capitol` |
| Session Laws of Hawaii | `1972 Haw. Sess. Laws Act 189`; `Act 235, SLH 2025`; `Act 189, Session Laws of Hawaii 1972`; `SLH 2025, Act 235` | `hi-session-laws` |
| Hawaii Constitution | `Haw. Const. art. I, § 5`; `Haw. Const. art. VI, § 1`; `Hawai'i Constitution article I, section 7`; `Article I, Section 5 of the Hawaii Constitution`; `Article XII, Section 7 of the Hawaiʻi State Constitution` | `hi-constitution-lrb` → `hi-constitution-capitol` → `hi-constitution-justia` |
| Hawai'i Rules of Civil Procedure | `Haw. R. Civ. P. 12(b)(6)`; `HRCP Rule 12(b)(6)`; `HRCP 56(c)`; `Hawai'i Rules of Civil Procedure Rule 60(b)`; `Rule 56 of the Hawaiʻi Rules of Civil Procedure` | `hi-rules-hrcp` |
| Hawai'i Rules of Appellate Procedure | `Haw. R. App. P. 35(c)`; `HRAP Rule 40.1`; `HRAP 35(c)(2)`; `Hawai'i Rules of Appellate Procedure Rule 4(a)(1)`; `Rule 40.1 of the Hawaii Rules of Appellate Procedure` | `hi-rules-hrap` |
| Hawai'i Rules of Penal Procedure | `Haw. R. Penal P. 48(b)`; `HRPP Rule 48`; `HRPP 40(a)(1)`; `Rule 48 of the Hawai'i Rules of Penal Procedure` | `hi-rules-hrpp` |
| Hawaii Rules of Evidence (HRS chapter 626) | `Haw. R. Evid. 702`; `HRE Rule 702`; `HRE 403`; `Hawai'i Rules of Evidence Rule 803(b)(6)`; `Rule 702 of the Hawaii Rules of Evidence`; `Hawaii Rule of Evidence 404(b)` | `hi-hrs-justia` → `hi-hrs-capitol` |
| Other Hawai'i court rules (RSCH, HRPC, DCRCP, HFCR, RCCH, HPR ...) | `RSCH 2.12`; `HRPC Rule 1.7`; `DCRCP Rule 12`; `HFCR Rule 68`; `RCCH 12(q)`; `Haw. R. Prof'l Conduct 1.7`; `Rules of the Supreme Court of the State of Hawai'i, Rule 2.16` | `hi-rules-index` |
| Hawaii Administrative Rules | `HAR § 11-60.1-1`; `Haw. Admin. R. § 11-60.1-201`; `Haw. Code R. § 11-60.1-1`; `Hawaii Administrative Rules § 11-1-1`; `section 11-60.1-1, Hawaii Administrative Rules`; `HAR § 17-1720-5` | `hi-har-agencies` → `hi-har-lii` |
| Hawai'i Reports / Hawaii Appellate Reports | `State v. Young, 93 Hawai'i 224`; `93 Haw. 224`; `State v. Horn, 58 Haw. 252`; `140 Hawaiʻi 167`; `6 Haw. App. 580` | `hi-cases-justia` → `hi-opinions-judiciary` |
| Pacific Reporter with Hawai'i court parenthetical | `State v. Young, 999 P.2d 230 (Haw. 2000)`; `398 P.3d 756 (Haw. 2017)`; `150 P.3d 798, 803 (Haw. Ct. App. 2006)`; `350 P.3d 1000 (Haw. App. 2015)` | `hi-cases-justia` → `hi-opinions-judiciary` |
| Hawai'i appellate docket numbers (SCWC/SCAP/CAAP ...) | `SCWC-23-0000668`; `No. CAAP-25-0000731`; `SCAP-22-0000123`; `SCAD-20-0000767`; `SCWC-30557` | `hi-opinions-judiciary` → `hi-cases-justia` |
| Unpublished Hawai'i dispositions (WL / LEXIS) | `2020 WL 1234567 (Haw. App. Mar. 5, 2020) (SDO)`; `2019 WL 7046970, at *2 (Haw. Ct. App. Dec. 20, 2019) (mem. op.)`; `2021 Haw. App. LEXIS 123 (Haw. App. 2021)` | `hi-opinions-judiciary` → `hi-cases-justia` |
| SDO / memorandum opinion marker (generic) *(only once this jurisdiction is known)* | `(SDO)`; `(mem. op.)`; `summary disposition order` | `hi-opinions-judiciary` → `hi-cases-justia` |
| Hawai'i certiorari dispositions (cert. rejected / accepted) *(only once this jurisdiction is known)* | `cert. rejected, No. SCWC-23-0000400`; `cert. rejected`; `cert. accepted, SCWC-24-0000597`; `cert. granted` | `hi-subsequent-history-cert` |

Regexes (case-insensitive):

- Hawaii Revised Statutes: `(?:(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Rev(?:ised)?\.?\s*Stat(?:utes|s)?\.?(?:\s+Ann\.)?|\bHRS)\s*§*\s*(?P<chapter>\d{1,3}[A-Z]?)(?::(?P<article>\d{1,2}[A-Z]?))?-(?P<section>\d{1,4}(?:\.\d{1,2})?)|(?:sec(?:tion|\.)|§)\s*(?P<chapter2>\d{1,3}[A-Z]?)(?::(?P<article2>\d{1,2}[A-Z]?))?-(?P<section2>\d{1,4}(?:\.\d{1,2})?)(?:\([a-z0-9]+\))*,?\s+(?:of\s+the\s+)?(?:(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Revised\s+Statutes|HRS)|(?:\bHRS|(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Rev(?:ised)?\.?\s*Stat(?:utes|s)?\.?)\s*(?:ch(?:apter|\.)|c\.)\s*(?P<chapter3>\d{1,3}[A-Z]?)(?![\d-])|(?:ch(?:apter|\.))\s*(?P<chapter4>\d{1,3}[A-Z]?),?\s+(?:of\s+the\s+)?(?:(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Revised\s+Statutes|HRS)`
- Session Laws of Hawaii: `(?P<year>(?:18|19|20)\d\d)\s+(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Sess\.\s*Laws\s+Act\s+(?P<act>\d+)|Act\s+(?P<act2>\d+),?\s*(?:SLH|Session\s+Laws\s+of\s+(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?))\s*(?P<year2>(?:18|19|20)\d\d)|\bSLH\s*(?P<year3>(?:18|19|20)\d\d),?\s*Act\s+(?P<act3>\d+)`
- Hawaii Constitution: `(?:(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Const(?:itution)?\.?)\s*,?\s*art(?:icle|\.)?\s*(?P<article>[IVXL]+),?\s*(?:§|sec(?:tion|\.)?)\s*(?P<section>\d+[A-Za-z]?)|Article\s+(?P<article2>[IVXL]+),?\s+Section\s+(?P<section2>\d+[A-Za-z]?)\s+of\s+the\s+(?:State\s+of\s+)?(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*(?:State\s+)?Constitution`
- Hawai'i Rules of Civil Procedure: `(?:\bHRCP\b\s*(?:Rule\s*)?|(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*R\.\s*Civ\.\s*P\.\s*)(?P<rule>\d{1,3}(?:\.\d{1,2})?)|(?:(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*)?Rules\s+of\s+Civil\s+Procedure\s*(?:,\s*)?Rule\s+(?P<rule2>\d{1,3}(?:\.\d{1,2})?)|Rule\s+(?P<rule3>\d{1,3}(?:\.\d{1,2})?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Rules\s+of\s+Civil\s+Procedure`
- Hawai'i Rules of Appellate Procedure: `(?:\bHRAP\b\s*(?:Rule\s*)?|(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*R\.\s*App\.\s*P\.\s*)(?P<rule>\d{1,3}(?:\.\d{1,2})?)|(?:(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*)?Rules\s+of\s+Appellate\s+Procedure\s*(?:,\s*)?Rule\s+(?P<rule2>\d{1,3}(?:\.\d{1,2})?)|Rule\s+(?P<rule3>\d{1,3}(?:\.\d{1,2})?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Rules\s+of\s+Appellate\s+Procedure`
- Hawai'i Rules of Penal Procedure: `(?:\bHRPP\b\s*(?:Rule\s*)?|(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*R\.\s*Penal\s*P\.\s*)(?P<rule>\d{1,3}(?:\.\d{1,2})?)|(?:(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*)?Rules\s+of\s+Penal\s+Procedure\s*(?:,\s*)?Rule\s+(?P<rule2>\d{1,3}(?:\.\d{1,2})?)|Rule\s+(?P<rule3>\d{1,3}(?:\.\d{1,2})?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Rules\s+of\s+Penal\s+Procedure`
- Hawaii Rules of Evidence (HRS chapter 626): `(?:\bHRE\b\s*(?:Rule\s*)?|(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*R\.\s*Evid\.\s*)(?P<rule>\d{3,4}(?:\.\d{1,2})?)|(?:(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*)?Rules?\s+of\s+Evidence\s*(?:,\s*)?Rule\s+(?P<rule2>\d{1,3}(?:\.\d{1,2})?)|Rule\s+(?P<rule3>\d{1,3}(?:\.\d{1,2})?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Rules?\s+of\s+Evidence|(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Rules?\s+of\s+Evidence\s+(?P<rule4>\d{3,4}(?:\.\d{1,2})?)`
- Other Hawai'i court rules (RSCH, HRPC, DCRCP, HFCR, RCCH, HPR ...): `\b(?P<set>RSCH|HRPC|DCRCP|HFCR|RCCH|RDCH|HPR|HCTR|HCRR|HEFSR|RICA|RLC|RCJC|HAR\s+Arb\.)\s*(?:Rule\s*)?(?P<rule>\d{1,3}(?:\.\d{1,3})?)|(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*R\.\s*Prof(?:'|’)?l\s*Conduct\s*(?P<rule2>\d\.\d{1,2})|Rules\s+of\s+the\s+Supreme\s+Court\s+of\s+the\s+State\s+of\s+(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*,?\s*Rule\s+(?P<rule3>\d{1,3}(?:\.\d{1,3})?)`
- Hawaii Administrative Rules: `(?:\bHAR|(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*(?:Admin(?:istrative)?\.?\s*R(?:ules?|\.)|Code\s*R\.))\s*§*\s*(?P<title>\d{1,2})-(?P<chapter>\d{1,4}(?:\.\d)?[A-Z]?)-(?P<section>\d{1,4}(?:\.\d{1,2})?)|(?:sec(?:tion|\.)|§)\s*(?P<title2>\d{1,2})-(?P<chapter2>\d{1,4}(?:\.\d)?[A-Z]?)-(?P<section2>\d{1,4}(?:\.\d{1,2})?),?\s+(?:of\s+the\s+)?(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)\s*Administrative\s+Rules`
- Hawai'i Reports / Hawaii Appellate Reports: `(?P<volume>\d{1,3})\s+(?:Haw(?:ai(?:['‘’ʻ`]|\s)?i)?\.?)(?:\s*(?P<app>App)\.)?\s+(?P<page>\d{1,4})(?!\d)`
- Pacific Reporter with Hawai'i court parenthetical: `(?P<volume>\d{1,4})\s+P\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+(?:\s*n\.\s*\d+)?)?\s*\((?P<court>Haw\.(?:\s*(?:Ct\.\s*)?App\.)?)\s*(?P<year>\d{4})\)`
- Hawai'i appellate docket numbers (SCWC/SCAP/CAAP ...): `\b(?P<prefix>SCWC|SCAP|SCPW|SCAD|SCPR|SCOT|SCEC|SCCQ|SCMF|SCRU|CAAP)-(?:(?P<yy>\d{2})-(?P<seq>\d{7})|(?P<old>\d{5}))\b`
- Unpublished Hawai'i dispositions (WL / LEXIS): `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?|Haw\.\s*(?:App\.\s*)?LEXIS\s+(?P<lexis>\d+))\s*\((?P<court>Haw\.(?:\s*(?:Ct\.\s*)?App\.)?)`
- SDO / memorandum opinion marker (generic): `\((?:SDO|mem(?:\.|orandum)\s*op(?:\.|inion))\)|summary\s+disposition\s+order`
- Hawai'i certiorari dispositions (cert. rejected / accepted): `cert\.\s*(?P<disp>rejected|accepted|granted|dismissed)(?:,\s*(?:No\.\s*)?(?P<docket>SCWC-\d{2}-\d{7}))?`

Short forms → URL key:

Haw. Rev. Stat. → `HRS`; Haw. Rev. Stat. Ann. → `HRS`; Hawaii Revised Statutes → `HRS`; Hawai'i Revised Statutes → `HRS`; HRS → `HRS`; HRE → `626-1`; Haw. R. Evid. → `626-1`; Hawai'i Rules of Evidence → `626-1`; Haw. Admin. R. → `HAR`; Haw. Code R. → `HAR`; HAR → `HAR`

One code: HRS sections are 'chapter-section' (657-7, 708-821, 514B-1, 657-1.5) and the Insurance Code uses 'chapter:article-section' (431:10C-301); a range 'HRS §§ 657-7 to -13' is read as its first section. 'HRS' and 'Haw. Rev. Stat.' mark Hawaii; bare 'section 657-7' does not route without 'Hawaii Revised Statutes'/'HRS'. The Hawaii Rules of Evidence are codified in HRS § 626-1 (one file per rule; law_aliases map HRE → 626-1) and route to the statute sources. Court rules are cited 'HRCP Rule 12(b)(6)', 'HRAP Rule 40.1', 'HRPP Rule 48', 'RSCH 2.12', 'HRPC Rule 1.7' in Hawai'i opinions and 'Haw. R. Civ. P.' in Bluebook; bare 'Rule 12(b)(6)' never routes here. Hawai'i spellings vary: Hawaii, Hawai'i, Hawaiʻi, Hawai`i — all regexes accept them. Reporters: Haw. vols. 1-75 to 1994, then 'Hawai'i' 76+ (Bluebook 'Haw.'); Haw. App. 1-10 (1980-1994), after which ICA opinions appear in Hawai'i Reports; parallel P.2d/P.3d. No public-domain citation. Docket prefixes: SCWC (cert), SCAP (transfer), SCPW (writs), SCAD/SCPR (discipline/admission), SCOT, SCEC, SCCQ (certified questions), CAAP (ICA); pre-2010 five-digit numbers. Unpublished ICA SDOs and memorandum opinions are cited with WL and '(SDO)'/'(mem. op.)'; HRAP 35(c) governs citing them (rule text not reached). 'cert. rejected' is the Hawai'i form for denial of certiorari; the generic markers '(SDO)' and 'cert. granted' patterns are context_required. CourtListener ids 'haw' and 'hawapp' are from memory, unverified. Chapter-only cites ('HRS chapter 92F', 'chapter 514B, Hawaii Revised Statutes') match with chapter3/chapter4 groups and route to the chapter page. Statute text: read from Justia (tier 2) — the legislature's www host is bot-walled and its data. alternate hostname is excluded by policy.

## A. Statutes / code

### `hi-hrs-capitol` — Hawaii Revised Statutes (Legislature, www.capitol.hawaii.gov)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Hawaii State Legislature / Legislative Reference Bureau (Revisor of Statutes) · text: **fetch-and-quote** · official: unknown
- **Coverage:** Current HRS (labelled 'Hawaii Revised Statutes 2025'; files last-modified 6 Jan 2026), one static HTML file per section, with annotations (AG opinions, law reviews, case notes) on the same page. Includes Hawaii Rules of Evidence as HRS ch. 626 (§ 626-1, one file per rule) and the State Constitution (Vol01 05-CONST). Prior editions under /hrsarchive/hrs{YYYY}/ (1999 onward seen).
- **Access:** `constructible` · format html
  - Pattern: `https://www.capitol.hawaii.gov/hrscurrent/{volume_folder}/HRS{chapter:04d}{chapter_letter}/HRS_{chapter:04d}{chapter_letter}-{section:04d}[_{decimal:04d}].htm`
  - Placeholders: chapter = digits zero-padded to 4 plus any upper-case letter suffix (657 → 0657, 514B → 0514B, 42F → 0042F). section = integer part zero-padded to 4; a decimal section appends '_' + the decimal digits zero-padded to 4 (657-1.5 → HRS_0657-0001_0005; 657-7.3 → HRS_0657-0007_0003). Insurance Code style '431:10C-301' → HRS_0431-0010C-0301.htm in folder HRS0431 (article padded to 4 incl. letter). Rules of Evidence: HRE Rule N = § 626-1 Rule N → HRS0626/HRS_0626-0001-{rule:04d}.htm (Rule 702.1 → HRS_0626-0001-0702_0001.htm). Chapter table of contents: HRS_{chapter}-.htm. volume_folder is chosen from the chapter by range (the folder names carry the ranges): Vol01_Ch0001-0042F (ch. 1-42F, also 05-CONST), Vol02_Ch0046-0115, Vol03_Ch0121-0200D, Vol04_Ch0201-0257, Vol05_Ch0261-0319, Vol06_Ch0321-0344, Vol07_Ch0346-0398, Vol08_Ch0401-0429, Vol09_Ch0431-0435H, Vol10_Ch0436-0474, Vol11_Ch0476-0490, Vol12_Ch0501-0588, Vol13_Ch0601-0676, Vol14_Ch0701-0853. Lettered chapters sort after their number (431A..431S in Vol09; 0042F ends Vol01).
  - Index: `https://www.capitol.hawaii.gov/hrscurrent/`
  - Navigation: hrscurrent/ directory → volume folder → HRS{chapter} folder → section file. Human browse: /hrsall/AllDivisions.aspx → Division.aspx?id=N (titles with chapter ranges, e.g. Title 36 = ch. 651-676) → ChaptersByDivision.aspx?id=N. All on www.capitol.hawaii.gov (bot-walled): fetch tool only, each built URL needs approval.
- **Automation:** WebFetch gated · shell blocked-challenge · robots: www.capitol.hawaii.gov/robots.txt returns 403 'Attention Required! | Cloudflare' (bot wall)
  - Host policy (SCHEMA alternate-host rule, decided 2026-10-17): the data. hostname of capitol.hawaii.gov is the same legislature web app under an unadvertised second hostname that no legislature page links to, so it is NOT used — it would get around the Cloudflare wall on www. www.capitol.hawaii.gov is bot-walled: the script route refuses it; the fetch tool may read it only if it does, and built URLs need per-URL approval (gated). WebFetch of a www HRS URL has not yet been read (no search-result www URL found; built URLs gated). Until it is, read HRS text from hi-hrs-justia (tier 2, disclose).
- **Currency:** HRS browse pages header ('Hawaii Revised Statutes 2025'); no currency line on section pages, which end with the bracketed history note — observed: "Hawaii Revised Statutes 2025"
- **Official status:** No official/unofficial statement found on the HRS browse pages (hrsall/AllDivisions.aspx, hrsall/Default.aspx) or section pages; the bound HRS and supplements are published by the Revisor (LRB). No UELMA statement seen.
- **Hazard:** bot wall on www: script refused; fetch tool gated per URL
- **Hazard:** volume folder not derivable from the section alone — use the chapter-range table
- **Hazard:** decimal sections encoded as _NNNN suffix
- **Hazard:** annotations follow the section text — do not quote them as statute
- **Hazard:** do not use the data. alternate hostname (policy)
- **Probe:** HRS § 657-7 → `https://www.capitol.hawaii.gov/hrscurrent/Vol13_Ch0601-0676/HRS0657/HRS_0657-0007.htm` — expect: "shall be instituted within two years after the cause of action"
- **Evidence (2026-10-17):** File-layout pattern was proven on 2026-10-17 against the legislature's data. alternate hostname (HRS § 657-7, § 708-821, § 657-1.5, HRE Rule 702), which is excluded by policy; www: curl robots.txt 403 Cloudflare, fetch_doc.py REFUSED (bot check). | Independent check 2026-10-16: pattern generalised (HRS § 514B-1, § 46-1.5, § 431:10C-301, HRE Rule 404) on the data. hostname; verifier found no legislature page linking that hostname (home page, hrsall, lrb.hawaii.gov and the search app link only www) → not acceptable; www WebFetch untested (gated).
- **Notes:** Statute text route until www is read by the fetch tool: hi-hrs-justia (tier 2, 2025 edition, disclosed). TOC PDF on www: /docs/hrstoc.pdf.

### `hi-session-laws` — Session Laws of Hawaii (Acts, per-Act PDFs)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Hawaii State Legislature · text: **fetch-and-quote** · official: unknown
- **Coverage:** Per-Act PDFs by year (SLH1972 and SLH2025 seen), plus 'Index&Effects_SLH{year}.pdf'.
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.capitol.hawaii.gov/sessions/sessionlaws/Years/SLH{year}/SLH{year}_Act{act}.pdf`
  - Placeholders: year 4 digits; act number unpadded (Act1, Act10, Act235). Year folder is a directory listing.
  - Index: `https://www.capitol.hawaii.gov/sessions/sessionlaws/Years/`
- **Automation:** WebFetch gated · shell blocked-challenge · robots: www.capitol.hawaii.gov: 403 Cloudflare on robots.txt
  - Host policy (SCHEMA alternate-host rule, decided 2026-10-17): the data. hostname of capitol.hawaii.gov is the same legislature web app under an unadvertised second hostname that no legislature page links to, so it is NOT used — it would get around the Cloudflare wall on www. www.capitol.hawaii.gov is bot-walled: the script route refuses it; the fetch tool may read it only if it does, and built URLs need per-URL approval (gated).
- **Currency:** none stated
- **Official status:** Hosted on the legislature's site (www.capitol.hawaii.gov); no official statement seen.
- **Hazard:** bot wall on www: fetch tool only, gated
- **Hazard:** older scanned acts have OCR noise
- **Hazard:** do not use the data. alternate hostname (policy)
- **Probe:** Act 235, SLH 2025 → `https://www.capitol.hawaii.gov/sessions/sessionlaws/Years/SLH2025/SLH2025_Act235.pdf` — expect: "A Bill for an Act Relating to Agriculture."
- **Evidence (2026-10-17):** Act-number pattern proven on the data. alternate hostname (SLH2025 Act 235, SLH1972 Act 189), excluded by policy; www not readable by script. | Independent check 2026-10-16: pattern generalised (Act 100, SLH 2010) on the data. hostname; host not acceptable (unlinked alternate hostname).

### `hi-hrs-justia` — Justia — Hawaii Revised Statutes (2025)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** HRS 2025 edition (unversioned URLs); earlier editions under /codes/hawaii/{year}/.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/hawaii/title-{title}/chapter-{chapter_lower}/section-{chapter_lower}-{section}/`
  - Placeholders: title = HRS title number, lower-case letter suffix (title-23a, title-25a, title-30a); not derivable from the chapter. Known ranges (legislature Division 4 page): Title 32 = ch. 601-615, 33 = 621-626, 34 = 631-637, 35 = 641-642, 36 = 651-676; ch. 852 is in Title 38. Otherwise look the title up: https://law.justia.com/codes/hawaii/2025/ lists all titles by division (no chapter ranges) → title page lists its chapters. chapter lower-case (chapter-4e). Section verbatim (section-852-1, section-663-31). Year-specific: insert /{year}/ after /hawaii/.
  - Index: `https://law.justia.com/codes/hawaii/`
  - Navigation: https://law.justia.com/codes/hawaii/2025/ (titles 1-38 by division) → title page (chapters) → chapter page (sections listed individually, no ranges) → section page
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: law.justia.com refuses the shell (robots.txt challenge, recorded by fetch_doc.py 2026-10-16)
  - WebFetch only. Title pages list chapters; chapter pages list sections.
- **Currency:** page heading and citation line — observed: "2025 Hawaii Revised Statutes; 'HI Rev Stat § 852-1 (2025)'"
- **Official status:** Disclaimer: 'These codes may not be the most recent version. Hawaii may have more current or accurate information.'
- **Hazard:** title number needed in URL (lookup hop)
- **Hazard:** shell blocked by Cloudflare
- **Hazard:** edition lag
- **Probe:** HRS § 852-1 → `https://law.justia.com/codes/hawaii/title-38/chapter-852/section-852-1/` — expect: "Refusal to provide ingress or egress. (a) Whenever ingress"
- **Evidence (2026-10-17):** WebFetch: body present '§852-1 Refusal to provide ingress or egress. (a) Whenever ingress'; '2025 Hawaii Revised Statutes'; not truncated. Chapter page /title-38/chapter-852/ lists section-852-1, -852-2; /title-1/ lists chapter-1, chapter-4e, chapter-6k. | Independent check 2026-10-17: WebFetch YES 'Whenever ingress to or egress from any public or private place'; '2025 Hawaii Revised Statutes'; second citation HRS § 663-31 ok
- **Notes:** PRIMARY readable route for HRS text (tier 2 — disclose as Justia, 2025 edition): the legislature's www host is bot-walled and its data. alternate hostname is excluded by policy. HRE rules: HRS § 626-1 → /title-33/chapter-626/section-626-1/ (one long page, not probed).

## B. Constitution

### `hi-constitution-capitol` — Constitution of the State of Hawaii (HRS Volume 1, www.capitol.hawaii.gov)

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Hawaii State Legislature · text: **fetch-and-quote** · official: unknown
- **Coverage:** Constitution as amended, one file per section, with annotations.
- **Access:** `constructible` · format html
  - Pattern: `https://www.capitol.hawaii.gov/hrscurrent/Vol01_Ch0001-0042F/05-CONST/CONST_{article:04d}-{section:04d}.htm`
  - Placeholders: article = Roman numeral converted to Arabic, zero-padded to 4 (art. I → 0001, art. VI → 0006); section zero-padded to 4. Whole-constitution TOC: CONST_.htm.
  - Index: `https://www.capitol.hawaii.gov/hrscurrent/Vol01_Ch0001-0042F/05-CONST/`
- **Automation:** WebFetch gated · shell blocked-challenge · robots: www.capitol.hawaii.gov: 403 Cloudflare on robots.txt
  - Host policy (SCHEMA alternate-host rule, decided 2026-10-17): the data. hostname of capitol.hawaii.gov is the same legislature web app under an unadvertised second hostname that no legislature page links to, so it is NOT used — it would get around the Cloudflare wall on www. www.capitol.hawaii.gov is bot-walled: the script route refuses it; the fetch tool may read it only if it does, and built URLs need per-URL approval (gated). Use hi-constitution-lrb (publisher-linked, script-readable).
- **Currency:** none on section pages
- **Official status:** Published as part of the HRS online; no official statement.
- **Hazard:** bot wall on www: fetch tool only, gated
- **Hazard:** annotations follow the text
- **Hazard:** do not use the data. alternate hostname (policy)
- **Probe:** Haw. Const. art. I, § 1 → `https://www.capitol.hawaii.gov/hrscurrent/Vol01_Ch0001-0042F/05-CONST/CONST_0001-0001.htm` — expect: "All political power of this State is inherent in the"
- **Evidence (2026-10-17):** Per-section file pattern proven on the data. alternate hostname (art. I § 1, § 5; art. VI § 1), excluded by policy. | Independent check 2026-10-16: pattern generalised (art. XI § 9; art. I § 23 shows REPEALED [HB 2802 (2024)]) on the data. hostname; host not acceptable.

### `hi-constitution-lrb` — The Constitution of the State of Hawaii (Legislative Reference Bureau)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Legislative Reference Bureau · text: **fetch-and-quote** · official: unknown
- **Coverage:** Whole constitution on one HTML page (153,886 chars).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://lrb.hawaii.gov/constitution/`
  - Placeholders: single page; locate 'ARTICLE {roman}' then 'Section {n}.'
  - Index: `https://lrb.hawaii.gov/constitution/`
- **Automation:** WebFetch untested · shell ok · robots: not separately checked; fetch_doc.py permitted the fetch
  - 153,886 chars — beyond one WebFetch window; read with fetch_doc.py.
- **Currency:** Effective Date Note near the top — observed: "amendments made by HB 2802 (2024) and SB 2927 (2024)"
- **Official status:** LRB page; notes that 2024 amendments 'will be included in the printed copies of the 2025 Cumulative Supplement'.
- **Hazard:** page exceeds WebFetch window
- **Probe:** Haw. Const. art. I, § 1 → `https://lrb.hawaii.gov/constitution/` — expect: "All political power of this State is inherent in the people"
- **Evidence (2026-10-17):** fetch_doc.py verify 'All political power of this State is inherent in the people' VERIFIED at offset 11,053; art. I § 23 shown REPEALED (HB 2802 (2024), election Nov 5, 2024). | Independent check 2026-10-17: fetch_doc.py verify 'All political power of this State is inherent in the people' VERIFIED offset 11,053

### `hi-constitution-justia` — Justia — Hawaii Constitution

- **Status:** REPORTED 2026-10-17 · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-article pages; STALE — does not reflect 2024 amendments.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/constitution/hawaii/conart{article_arabic}.html`
  - Placeholders: article Roman → Arabic (art. I → conart1.html). Index is a section listing only.
  - Index: `https://law.justia.com/constitution/hawaii/`
  - Navigation: index → conart{N}.html (per-article page)
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: law.justia.com refuses the shell (robots.txt challenge, recorded by fetch_doc.py 2026-10-16)
  - Verified by the independent checker by WebFetch.
- **Currency:** none; only 'may not be the most recent version'
- **Official status:** Third-party compilation.
- **Hazard:** STALE: art. I § 23 (repealed 2024) still shows the opposite-sex marriage text
- **Hazard:** no currency string
- **Hazard:** shell blocked by Cloudflare
- **Probe:** Haw. Const. art. I, § 1 → `https://law.justia.com/constitution/hawaii/conart1.html` — expect: "All political power of this State is inherent in the people"
- **Evidence (2026-10-17):** Not fetched by research. | Independent check 2026-10-16: index lists per-article pages conart{N}.html; conart1.html body present but § 23 still reads 'The legislature shall have the power to reserve marriage to opposite-sex couples' (repealed 2024).
- **Notes:** Last resort only; prefer hi-constitution-lrb.

## C. Court rules

### `hi-rules-hrap` — Hawai'i Rules of Appellate Procedure

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Hawai'i Supreme Court / State Judiciary · text: **fetch-and-quote** · official: unknown
- **Coverage:** HRAP with amendments; HTML (…/2025/07/hrap.htm) and PDF (…/2025/07/hrap_ada.pdf). Separate amendment orders: Rule 35 (am. 07/21/2026), Rule 50, Rule 4 (eff. 01/01/2027).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.state.hi.us/wp-content/uploads/2025/07/hrap_ada.pdf`
  - Placeholders: Fixed upload path; re-confirm from rules index. Check the separate amendment-order PDFs listed beside HRAP (e.g. 2026_hrap35am_ada.pdf) — the consolidated file may predate them.
  - Index: `https://www.courts.state.hi.us/legal_references/rules/rulesofcourt`
  - Navigation: rules index → HRAP HTML or PDF
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: www.courts.state.hi.us/robots.txt answers 403 to the shell; fetch_doc.py refuses the host ('answers robots.txt with a bot check')
  - PDF: WebFetch window 1 ends in Rule 28(b)(11)(A); window 2 (offset=100000) ends in Rule 32(c). Rule 35(c) and 40.1 NOT PRESENT in either — at least a third/fourth window needed. HTML version hrap.htm was refused with PROVENANCE_REQUIRED.
- **Currency:** rules index; PDF cover 'Effective June 1, 1984 ... With Further Amendments as Noted' — observed: "Effective 07/01/2026 (index)"
- **Official status:** Published on the Judiciary rules index.
- **Hazard:** WebFetch truncation (Rule 35, 40.1 beyond window 2)
- **Hazard:** amendment orders published separately
- **Hazard:** script route refused by host
- **Probe:** Haw. R. App. P. 28(b) → `https://www.courts.state.hi.us/wp-content/uploads/2025/07/hrap_ada.pdf` — expect: "Within 40 days after the filing of the record on appeal"
- **Evidence (2026-10-17):** WebFetch window 1: body text present through Rule 28(b)(11)(A) (page marker HRAP--20); window 2: Rules 28(b)-32(c); Rule 35(c) NOT PRESENT; Rule 40.1 NOT PRESENT. | Independent check 2026-10-17: WebFetch: 28(b) 'Within 40 days after the filing of the record on appeal'; stops Rule 28(b)(11)(A); second citation HRAP Rule 4(a)(1) ok
- **Notes:** HRAP 35(c) governs citation of unpublished dispositions; 40.1 governs certiorari applications — both currently unreachable by WebFetch without further offsets.

### `hi-rules-hrcp` — Hawai'i Rules of Civil Procedure (HTML)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Hawai'i Supreme Court / State Judiciary · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full HRCP with amendment notes; 121,526 chars of text.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.courts.state.hi.us/wp-content/uploads/2024/09/hrcp_ada.htm`
  - Placeholders: Fixed upload path; re-confirm from the rules index (PDF: …/2024/09/hrcp_ada.pdf).
  - Index: `https://www.courts.state.hi.us/legal_references/rules/rulesofcourt`
  - Navigation: rules index → 'Hawai'i Rules of Civil Procedure' HTML
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: www.courts.state.hi.us/robots.txt answers 403 to the shell; fetch_doc.py refuses the host ('answers robots.txt with a bot check')
  - WebFetch window 1 (0-100,000) ends mid Rule 17(d)(3); Rule 56(c) NOT PRESENT — needs offset=100000 (21,526 chars remain).
- **Currency:** rules index 'Effective' column; document cover shows only 'Effective April 7, 1980 ... With Amendments as Noted' — observed: "Effective 07/01/2026 (index)"
- **Official status:** Published on the Judiciary rules index; no official statement.
- **Hazard:** WebFetch truncation at Rule 17
- **Hazard:** script route refused by host
- **Probe:** Haw. R. Civ. P. 12(b) → `https://www.courts.state.hi.us/wp-content/uploads/2024/09/hrcp_ada.htm` — expect: "Every defense, in law or fact, to a claim for relief"
- **Evidence (2026-10-17):** WebFetch: Rule 12(b) YES 'Every defense, in law or fact, to a claim for'; 56(c) NOT PRESENT; text stops in Rule 17(d)(3); page 121,526 chars. | Independent check 2026-10-17: WebFetch: 12(b) 'Every defense, in law or fact, to a claim for relief'; stops Rule 17(d)(3); second citation HRCP Rule 8(a) ok

### `hi-rules-hrpp` — Hawai'i Rules of Penal Procedure

- **Status:** REPORTED 2026-10-17 · **Tier 1** · Hawai'i Supreme Court / State Judiciary · text: **fetch-and-quote** · official: unknown
- **Coverage:** HRPP; HTML …/2024/12/hrpp.htm, PDF …/2024/12/hrpp_ada.pdf; effective 07/01/2026 per index.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.courts.state.hi.us/wp-content/uploads/2024/12/hrpp.htm`
  - Placeholders: Fixed upload path; re-confirm from rules index.
  - Index: `https://www.courts.state.hi.us/legal_references/rules/rulesofcourt`
  - Navigation: rules index → HRPP HTML or PDF
- **Automation:** WebFetch ok (truncated) · shell blocked-challenge · robots: www.courts.state.hi.us/robots.txt answers 403 to the shell; fetch_doc.py refuses the host ('answers robots.txt with a bot check')
  - Independent check: WebFetch reads hrpp.htm (124,231 chars) — window 1 ends Rule 21, window 2 ends at the Rule 36 heading ('CLERIC…'); Rule 48 NOT PRESENT in either, so hrpp.htm does not reach Rule 48. hrpp_ada.pdf (index) untested.
- **Currency:** rules index — observed: "Effective 07/01/2026"
- **Official status:** Published on the Judiciary rules index.
- **Hazard:** hrpp.htm ends at the Rule 36 heading — Rules 36 onward (incl. 48) unreachable via the HTML
- **Hazard:** script route refused by host
- **Hazard:** hrpp_ada.pdf untested
- **Probe:** HRPP Rule 48(b) → `https://www.courts.state.hi.us/wp-content/uploads/2024/12/hrpp.htm`
- **Evidence (2026-10-17):** Link and effective date read from the rules index via WebFetch; document fetch refused PROVENANCE_REQUIRED. | Independent check 2026-10-16: hrpp.htm window 1 ends Rule 21, window 2 ends at Rule 36 heading; Rule 48(b) NOT PRESENT.

### `hi-rules-index` — Hawai'i State Judiciary — Rules of Court index

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Hawai'i State Judiciary · text: **fetch-and-quote** · official: unknown
- **Coverage:** 31 rule sets with HTML and '_ada' PDF links and effective dates (HRPP, HRCP, RCCH, Hawai'i Arbitration Rules, HPR, RLC, HFCR, RDCH, HCTR, DCRCP, RSCD, HCRR, HEFSR, HRAP, RECPA, RSCH, HBBE, HRPC (Exhibit A to RSCH), RDB, RCJC, RICA, RTAC, and others). The Hawai'i Rules of Evidence are NOT on this page (they are HRS ch. 626).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Placeholders: Rule-set files live under /wp-content/uploads/{YYYY}/{MM}/{abbr}[_ada].htm|pdf; the upload folder changes when a set is re-issued, so always take the link from the index.
  - Index: `https://www.courts.state.hi.us/legal_references/rules/rulesofcourt`
  - Navigation: index → rule set HTML (preferred, text) or _ada PDF; amendment orders listed beside each set
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.courts.state.hi.us/robots.txt answers 403 to the shell; fetch_doc.py refuses the host ('answers robots.txt with a bot check')
  - Links on the index are WebFetch-reachable when they come from the fetched page, but several were refused with PROVENANCE_REQUIRED (gating), e.g. hrap.htm, hrpp.htm.
- **Currency:** index page footer; 'Effective' column per rule set — observed: "Last Updated: October 12, 2026"
- **Official status:** Rules index page has no official/unofficial statement; 'Last Updated: October 12, 2026'.
- **Hazard:** host refuses the script route
- **Hazard:** upload paths change on re-issue
- **Hazard:** HRE not here — it is HRS ch. 626
- **Hazard:** most rule-set HTML files exceed 100K chars: WebFetch window 1 of RSCH (rsch.htm, 123,023 chars) stops in Rule 2.3(e)(7), so RSCH 2.12 needs offset=100000; HRS-style sets need several windows
- **Hazard:** RSCH HTML (2025/10) and PDF (2025/07) sit in different upload folders — always take links from the index
- **Probe:** Rules of Court index → `https://www.courts.state.hi.us/legal_references/rules/rulesofcourt` — expect: "Hawai'i Rules of Civil Procedure"
- **Evidence (2026-10-17):** WebFetch: 31 rule sets listed with HTML/PDF links and effective dates (HRCP 07/01/2026; HRAP 07/01/2026 with Rule 35 am. 07/21/2026; RSCH 07/01/2026). | Independent check 2026-10-17: WebFetch: HRCP listed; 31 rule sets; 'Last Updated: October 12, 2026'; second citation RSCH 2.12 FAILED (rsch.htm window 1 stops in Rule 2.3(e)(7))

## D. Administrative code

### `hi-har-agencies` — Hawaii Administrative Rules (agency-published chapters)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Each issuing department; directory by the Office of the Lieutenant Governor · text: **fetch-and-quote** · official: unknown
- **Coverage:** HAR by title (= department), chapter PDFs posted by each agency; LRB Admin Rules Table & Directory (2025 Annual Supplement PDF) tells which chapters exist.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Placeholders: No constructible pattern: department sites differ (health.hawaii.gov/opppd/files/2026/08/chapter-11-1-HAR-effective-2005.02.14.pdf). HAR title = department (11 Health, 12 DLIR, 13 DLNR, 16 DCCA, 17 DHS, 18 Taxation …).
  - Index: `https://ltgov.hawaii.gov/the-office/administrative-rules/`
  - Navigation: Lt. Gov. 'Department Administrative Rules' page → department rules page (e.g. Title 11 → https://health.hawaii.gov/opppd/administrative-rules/; some divisions host their own) → chapter PDF. For existence/currency check the LRB table: https://lrb.hawaii.gov/admin-rules-directory/ → 2025AdminRules_Supplement.pdf.
- **Automation:** WebFetch untested · shell ok · robots: ltgov.hawaii.gov, health.hawaii.gov, lrb.hawaii.gov: fetch_doc.py permitted
  - The DOH OPPPD page holds only ch. 11-1; program chapters (e.g. 11-60.1 air) are on division pages — a guessed division URL (health.hawaii.gov/cab/hawaii-administrative-rules-har/) returned 404.
- **Currency:** PDF filename / cover (effective date of the compilation) — observed: "chapter-11-1-HAR-effective-2005.02.14.pdf"
- **Official status:** No consolidated official HAR online: each department posts its own chapters (PDF). The Lt. Governor's page links to department rule pages and disclaims responsibility for external sites.
- **Hazard:** no central official HAR site
- **Hazard:** per-agency URLs differ and move
- **Hazard:** effective-date compilations may lag amendments
- **Hazard:** department pages list only some chapters (DLIR page: 8 chapters); others are on division pages
- **Probe:** HAR § 11-1-1 → `https://health.hawaii.gov/opppd/files/2026/08/chapter-11-1-HAR-effective-2005.02.14.pdf` — expect: "RULES OF PRACTICE AND PROCEDURE"
- **Evidence (2026-10-17):** fetch_doc.py: Lt. Gov. page lists department links (Title 11 → health.hawaii.gov/opppd/administrative-rules/); DOH PDF 37 pp., 'CHAPTER 1 RULES OF PRACTICE AND PROCEDURE ... §11-1-1 Statement of scope and purpose'. | Independent check 2026-10-17: fetch_doc.py verify 'RULES OF PRACTICE AND PROCEDURE' VERIFIED page 3; second citation HAR § 12-30-1 (labor.hawaii.gov/wp-content/uploads/2013/02/12-30.pdf) ok

### `hi-har-lii` — Cornell LII — Hawaii Code of Rules (HAR)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** HAR titles 2-24 (index lists 21 titles), per-section pages.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/hawaii/Haw-Code-R-SS-{title}-{chapter_dots_as_hyphens}-{section}`
  - Placeholders: Dots in the chapter become hyphens: HAR § 11-60.1-1 → Haw-Code-R-SS-11-60-1-1; § 11-60.1-201 → …-11-60-1-201. A dotted URL (…-11-60.1-1) silently returns the HAR index page, not a 404 — check the page heading. Browse: /regulations/hawaii/title-{t}/subtitle-{s}/chapter-{c}/subchapter-{n} (subchapter pages show section ranges).
  - Index: `https://www.law.cornell.edu/regulations/hawaii`
- **Automation:** WebFetch untested · shell ok · robots: Crawl-delay: 10; /regulations allowed
  - Respect the 10 s crawl delay. Pages last-modified Aug 2025.
- **Currency:** bottom of section page — observed: "State regulations are updated quarterly"
- **Official status:** Third-party mirror; 'State regulations are updated quarterly'.
- **Hazard:** dotted chapter URL returns the index, not an error
- **Hazard:** quarterly lag (pages last-modified Aug 2025)
- **Probe:** HAR § 11-60.1-1 → `https://www.law.cornell.edu/regulations/hawaii/Haw-Code-R-SS-11-60-1-1` — expect: "As used in this chapter, unless otherwise defined for purposes of a particular subchapter"
- **Evidence (2026-10-17):** fetch_doc.py: heading 'Haw. Code R. § 11-60.1-1 - Definitions', body 'As used in this chapter, unless otherwise defined'; § 11-60.1-201 'The purpose of this subchapter is to further implement'. Dotted URL Haw-Code-R-SS-11-60.1-1 returned the index. | Independent check 2026-10-17: fetch_doc.py verify 'As used in this chapter, unless otherwise defined' VERIFIED; second citation HAR § 11-200.1-1 ok

## D. Administrative register

### `hi-admin-rules-updates` — Administrative Rules Updates — Monthly Reports (Office of the Lieutenant Governor)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Office of the Lieutenant Governor · text: **fetch-and-quote** · official: unknown
- **Coverage:** Monthly update reports by year, 2012 onward; proposed changes list.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format html
  - Placeholders: Year-page slugs vary (2025 is …-monthly-reports-2025-2/); take the year link from the index, never build it. No 2026 page linked as of 2026-10-17.
  - Index: `https://ltgov.hawaii.gov/the-office/administrative-rules/monthly-update-reports/`
  - Navigation: monthly-update-reports index → year link (follow, don't build) → 2025: HTML table (DOC. NO, DEPT, TITLE-CH-SEC, EFFECTIVE DATE, COMMENTS); older years may link PDFs. Proposed rules: /the-office/administrative-rules/proposed-changes/
- **Automation:** WebFetch untested · shell ok · robots: fetch_doc.py permitted
  - Monthly PDFs not opened.
- **Currency:** none stated
- **Official status:** Hawaii has no administrative register; the Lt. Governor posts monthly reports of rules filed and a 'Proposed Changes' page.
- **Hazard:** not a register: no page citations
- **Hazard:** monthly PDFs not probed
- **Hazard:** year-page slugs vary ('-2025-2'); no 2026 page linked
- **Probe:** monthly update reports index → `https://ltgov.hawaii.gov/the-office/administrative-rules/monthly-update-reports/` — expect: "2012"
- **Evidence (2026-10-17):** fetch_doc.py links: 15 links incl. year pages 2012, 2013, 2014, 2015 … | Independent check 2026-10-17: fetch_doc.py links: year pages 2012-2024 plus …-monthly-reports-2025-2/; second citation 2025 monthly reports (HTML table, e.g. 'DLNR Chap 13-60.4 1/2/2025') ok

## E. Case law

### `hi-opinions-judiciary` — Hawai'i State Judiciary — Opinions and Orders

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Hawai'i State Judiciary · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court and ICA opinions, memorandum opinions, summary disposition orders (SDOs), dismissal orders and certiorari orders in one table; year filter offers 2010-2026 (older PDFs under /docs/opin_ord/{sct|ica}/{YYYY}/{mon}/ seen for 2011, 2012, 2015-2016). 297 pages of listings.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.state.hi.us/opinions_and_orders/opinions/page/{n}?yr={YYYY}`
  - Placeholders: GET listing, newest first, mixed courts (column 'Ct.' = S.Ct or ICA). ?yr={YYYY} filters to a year (verified: page/18?yr=2016 showed only 2016 rows); a month selector exists but its GET parameter was not observed. No docket search. PDF links: 2016+ /wp-content/uploads/{YYYY}/{MM}/{DOCKET}{suffix}.pdf where suffix = '' (opinion), 'sdo', 'dsm' (dismissal), 'certacc', 'certrej', 'recond', 'ord' (order), plus 'ada' accessible variants; older /docs/opin_ord/{sct|ica}/{YYYY}/{Month}/{DOCKET}.pdf. Take URLs from the listing — do not build them.
  - Index: `https://www.courts.state.hi.us/opinions_and_orders/opinions`
  - Navigation: listing (?yr=YYYY, page through) → row with docket → PDF link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.courts.state.hi.us/robots.txt answers 403 to the shell; fetch_doc.py refuses the host ('answers robots.txt with a bot check')
  - Listing pages fetch fine. PDFs: those surfaced by WebSearch fetched fine (CAAP-17-0000351recondada.pdf, SCWC-23-0000412certacc.pdf); a PDF link taken from the fetched listing (SCWC-23-0000668.pdf) was refused PROVENANCE_REQUIRED — expect gating. RSS: https://www.courts.state.hi.us/opinions-orders/feed.
- **Currency:** none; listing newest row 'October 16, 2026'
- **Official status:** Slip opinions/orders; published opinions carry 'FOR PUBLICATION IN WEST'S HAWAI'I REPORTS AND PACIFIC REPORTER' — the reporter is West's, so these PDFs are not the paginated official text.
- **Hazard:** slip pagination only (no Haw./P.3d pages)
- **Hazard:** script route refused by host
- **Hazard:** no docket search — page through year listing
- **Hazard:** PDF links can be gated in WebFetch
- **Hazard:** scanned images with stamps 2010-July 2025; accessible text from August 2025 (page notice)
- **Probe:** State v. Winham, No. CAAP-17-0000351 (Haw. App. Apr. 22, 2019) (order) → `https://www.courts.state.hi.us/wp-content/uploads/2019/04/CAAP-17-0000351recondada.pdf` — expect: "Upon consideration of the April 12, 2019"
- **Evidence (2026-10-17):** WebFetch listing: 5 rows (e.g. Oct 14, 2026 SCWC-23-0000668 Norrie v. Maui County Board of Variances and Appeals). PDF: ICA order, 'NOT FOR PUBLICATION IN WEST'S HAWAII REPORTS OR THE PACIFIC REPORTER', body 'Upon consideration of the April 12, 2019'. | Independent check 2026-10-17: WebFetch YES 'Upon consideration of the April 12, 2019'; slip pages; second citation Robinson-Wells v. Knull, No. CAAP-25-0000731 (Haw. App. Oct. 16, 2026) (SDO) ok
- **Notes:** Page notice: 2010-July 2025 links are scanned images with file stamps; from August 2025 accessible files. See also 'Supreme Court Various Orders' https://www.courts.state.hi.us/courts/SCt_VariousOrders.

### `hi-cases-justia` — Justia — Hawaii case law

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court (years incl. 2019-2023 seen) and Intermediate Court of Appeals 1980-2026; includes SDOs and cert orders as well as opinions.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/hawaii/{court-slug}/{year}/{docket_lower}.html`
  - Placeholders: court-slug: supreme-court | court-of-appeals (ICA). docket lower-case as filed (scwc-17-0000581, caap-23-0000665, scad-20-0000767). A second document on the same docket gets a suffix (-0, -1): State v. Abion opinion = scwc-18-0000600-0.html. The plain slug may be the cert order, not the opinion (scwc-17-0000581.html = order accepting cert) — check the year listing https://law.justia.com/cases/hawaii/{court-slug}/{year}/.
  - Index: `https://law.justia.com/cases/hawaii/`
  - Navigation: year listing shows name, docket, date and link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: law.justia.com refuses the shell (robots.txt challenge, recorded by fetch_doc.py 2026-10-16)
  - Court PDF copy at https://cases.justia.com/hawaii/{court-slug}/{year}-{docket}.pdf?ts=…
- **Currency:** none
- **Official status:** Third-party; text copied from court PDFs.
- **Hazard:** docket-slug suffixes (-0, -1)
- **Hazard:** plain slug may be a cert order
- **Hazard:** no reporter pagination for the case itself
- **Hazard:** diacritics dropped ('Hawai i')
- **Probe:** State v. Abion, No. SCWC-18-0000600 (Haw. Dec. 29, 2020) → `https://law.justia.com/cases/hawaii/supreme-court/2020/scwc-18-0000600-0.html` — expect: "I. Introduction We address whether a defendant whose substance use results in"
- **Evidence (2026-10-17):** WebFetch: full opinion body 'I. Introduction We address whether a defendant whose substance use results in', not truncated. ICA: /court-of-appeals/2026/caap-23-0000665.html SDO body present, 'NOT FOR PUBLICATION'. Year listing 2020 and ICA index (1980-2026) fetched. | Independent check 2026-10-17: WebFetch YES 'We address whether a defendant whose substance use results in permanent'; second citation Robinson-Wells v. Knull, CAAP-25-0000731 (Haw. Ct. App. Oct. 16, 2026) ok

## F. Subsequent history

### `hi-subsequent-history-cert` — Hawai'i Supreme Court certiorari orders (accept / reject) and writ-of-cert archive

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Hawai'i State Judiciary · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Orders accepting/rejecting applications for writ of certiorari appear as rows in the Opinions listing (suffix certacc / certrej); a separate 'Writ of Certiorari / Motions for Reconsideration' archive lists SCWC dockets by posting date (1997-2026; 404 pages).
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.courts.state.hi.us/opinions_and_orders/opinions/page/{n}?yr={YYYY}`
  - Placeholders: Since the 2010 e-filing dockets, the certiorari docket reuses the ICA number: CAAP-YY-NNNNNNN → SCWC-YY-NNNNNNN (verified: CAAP-23-0000412 → SCWC-23-0000412; CAAP-11-0000049 → SCWC-11-0000049). So from an ICA decision, look for rows with the SCWC docket of the same digits in the listing for the year(s) after the ICA judgment; the order PDF is …/{SCWC-docket}certacc.pdf or certrej.pdf (take the link from the listing). Writ archive: https://www.courts.state.hi.us/writ-of-cert/page/{n} → per-docket page /writ-of-cert/{scwc-docket-lower}[-2] (application and responses). Pre-2010 dockets (5-digit 'No. 30557') do not follow this rule.
  - Index: `https://www.courts.state.hi.us/writ-of-cert/page/1`
  - Navigation: derive SCWC docket from CAAP docket → year listing rows / writ-of-cert archive → certacc|certrej PDF
- **Automation:** WebFetch ok · shell blocked-challenge · robots: www.courts.state.hi.us/robots.txt answers 403 to the shell; fetch_doc.py refuses the host ('answers robots.txt with a bot check')
  - Writ archive page/4 fetched; a per-docket page (/writ-of-cert/scwc-24-0000432) was refused PROVENANCE_REQUIRED. Archive entries show docket and posting date only — no case name or disposition.
- **Currency:** none
- **Official status:** Slip orders.
- **Hazard:** no docket search; listing must be paged
- **Hazard:** archive rows lack names/dispositions
- **Hazard:** script route refused by host
- **Probe:** State v. Ahina, CAAP-23-0000412 → SCWC-23-0000412 (cert. accepted May 8, 2026) → `https://www.courts.state.hi.us/wp-content/uploads/2026/05/SCWC-23-0000412certacc.pdf` — expect: "The application for writ of certiorari filed on March 10, 2026, by"
- **Evidence (2026-10-17):** WebFetch: order accepting cert, caption SCWC-23-0000412 with CAAP-23-0000412 and 2CPC-22-0000398(3); body 'The application for writ of certiorari filed on March 10, 2026, by'. Also SCWC-11-0000049 (2012) ↔ CAAP-11-0000049. Listing shows 'Order Rejecting Application for Writ of Certiorari' rows (Hasegawa v. Fang, SCWC-23-0000400certrej.pdf). | Independent check 2026-10-17: WebFetch YES 'The application for writ of certiorari filed on March 10,'; SCWC/CAAP-23-0000412; second citation State v. Wilhelm, SCWC-24-0000597 (cert. accepted Oct. 16, 2026) ok
- **Notes:** Hawai'i Bluebook/local usage: 'cert. rejected' (not 'denied') for refused applications; 'cert. granted'/'accepted' for accepted.

## Not available (do not look for these again)

- **admin_register** — A Hawaii administrative register (official periodic publication of proposed/adopted rules): Lt. Governor's administrative-rules page offers only 'Proposed Changes' and 'Administrative Rules Updates – Monthly Reports'; no register volume/page citation form exists. (2026-10-17)
- **admin_code** — A single official consolidated online HAR: ltgov.hawaii.gov directs to each department's own rules page and disclaims external content; Cornell LII is the only consolidated per-section copy. (2026-10-17)
- **statutes** — public.law edition of Hawaii statutes: fetch_doc.py: hawaii.public.law robots.txt unreachable (proxy 'Tunnel connection failed: 502'); public.law's state list (per the DE record) covers only CA, CO, FL, NV, NY, OR, TX. (2026-10-17)
- **statutes** — Cornell LII Hawaii statutes / constitution / opinions: https://www.law.cornell.edu/states/hawaii links out to lrb.hawaii.gov, capitol.hawaii.gov and courts.state.hi.us; LII hosts only the HAR. (2026-10-17)
- **case_law** — Free official reporter pagination (Haw./P.3d) for Hawai'i opinions: Court PDFs carry slip pagination and the legend 'FOR PUBLICATION IN WEST'S HAWAI'I REPORTS AND PACIFIC REPORTER'; Justia gives no reporter cite for the case. (2026-10-17)
- **case_law** — Public-domain (vendor-neutral) citation format: None used in Hawai'i opinions or listings; cites are Haw./P.3d or docket + WL. (2026-10-17)
- **court_rules** — Tier-2 (Justia/LII/public.law) copies of Hawai'i court rules: Not offered by LII's Hawaii page; Justia and public.law not observed hosting Hawai'i court rules. (2026-10-17)
- **statutes** — Script-readable official HRS / session laws: www.capitol.hawaii.gov is Cloudflare-walled (robots.txt 403); the data. alternate hostname is unlinked by any legislature page and excluded by policy (verifier 2026-10-16). (2026-10-17)

## Corpus candidates (maintainers)

- `hi-rules-hrcp` — 121,526 chars; WebFetch window 1 stops in Rule 17(d)(3). Host refuses the script route, so ingest is blocked unless access changes.
- `hi-rules-hrap` — WebFetch window 1 ends in Rule 28, window 2 in Rule 32; Rules 35 and 40.1 unreachable in two windows. Host refuses the script route.
- `hi-rules-hrpp` — Full rule set (not probed; expected beyond one WebFetch window). Host refuses the script route.
- `hi-constitution-lrb` — 153,886 chars on one page — beyond one WebFetch window; script-readable.

## Open questions

- HRAP Rule 35(c) (citation of unpublished dispositions) and Rule 40.1 text not reached by WebFetch (beyond window 2); HRPP not probed (PROVENANCE_REQUIRED).
- Month GET parameter of the Judiciary opinions listing not observed; only ?yr= verified.
- Earliest opinions on courts.state.hi.us: year selector starts 2010; older /docs/opin_ord/ PDFs (2011-2016 seen) — pre-2010 coverage not established.
- Justia Hawaii constitution page not fetched (reported).
- Decimal-section file suffix for two-digit decimals (e.g. § 46-1.15) assumed _0015, not tested.
- CourtListener ids haw / hawapp unverified.
- WebFetch hit a session usage limit once during this run (resumed after reset); several courts.state.hi.us URLs refused PROVENANCE_REQUIRED.
- HRPP: hrpp.htm stops at the Rule 36 heading; test hrpp_ada.pdf with offsets to reach Rule 48.
- www.capitol.hawaii.gov: test WebFetch on a search-result HRS URL (bot-wall rule allows the fetch tool if it reads); if it does, mark hi-hrs-capitol / hi-session-laws / hi-constitution-capitol verified with read route 'fetch tool'.
- data.capitol.hawaii.gov could be used only if the legislature links it or confirms it as a data endpoint.
