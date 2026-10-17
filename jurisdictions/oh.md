# Ohio (OH) — free legal sources

_Generated from `data/oh.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes, constitution and admin code: the official LSC site codes.ohio.gov (UELMA-official) is robots-disallowed ('User-agent: * Disallow: /', policy 2026-10-17), so there is no tier-1 text route; use Justia (2025 Ohio Revised Code; constitution per section; WebFetch only) and Cornell LII for the Administrative Code (colon→hyphen slugs; can lag by years and carries redline text), always disclosed. Court rules are long full-set PDFs on supremecourt.ohio.gov that WebFetch cuts off early (Civ.R. text stops at Rule 5) — read them with fetch_doc.py or a corpus. Case law: Ohio's public-domain webcite (2023-Ohio-3005, ¶ pinpoints) maps to a PDF URL once the court is known (rod/docs/pdf/{0|district}/{year}/{webcite}.pdf, county→district table in the record); the Reporter of Decisions search (1992-, POST only, and the year range must be set explicitly or it returns 0 rows) resolves webcites, Ohio St.3d cites and case numbers, and finds 'appeals not accepted for review' dispositions by the lower court's webcite. The Register of Ohio and legislature.ohio.gov fail TLS from the shell.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Ohio | `ohio (unverified)` | Ohio | Ohio St.3d, Ohio St.2d, Ohio St., N.E.3d, N.E.2d, N.E. | 2023-Ohio-3005 (YYYY-Ohio-N, ¶ pinpoints; since May 1, 2002, retroactively assigned to website documents from 1992) |
| Ohio Court of Appeals (First through Twelfth Districts) | `ohioctapp (unverified)` | Ohio Ct. App. | Ohio App.3d, Ohio App.2d, Ohio App., N.E.3d, N.E.2d | 2022-Ohio-1555 (Ohio style adds district: '(7th Dist.)') |
| Ohio Court of Claims | `ohioctcl (unverified)` | Ohio Ct. Cl. | Ohio Misc.2d, N.E.3d | 2025-Ohio-5905 |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Ohio Revised Code | `R.C. 2305.10`; `R.C. 2744.03(A)(6)`; `Ohio Rev. Code Ann. § 2305.10`; `Ohio Rev. Code § 2903.01(B)`; `ORC 1.42`; `section 2305.10 of the Revised Code`; `R.C. 2305.10 to 2305.12`; `R.C. Chapter 2744`; `Chapter 2744. of the Revised Code` | `oh-orc-justia` → `oh-orc-codes` |
| Ohio session laws / General Assembly bills | `Am.Sub.S.B. No. 80, 125th General Assembly`; `S.B. 17, 126th General Assembly`; `Sub.H.B. No. 33 (135th G.A.)`; `150 Ohio Laws, Part III, 3888` | `oh-session-laws-lis` |
| Ohio Constitution | `Ohio Const. art. I, § 16`; `Ohio Const. art. IV, § 2(B)(2)`; `Article I, Section 16 of the Ohio Constitution`; `Section 16, Article I, Ohio Constitution`; `Ohio Constitution, Article I, Section 10a`; `Ohio Const., Art. I, Sec. 16` | `oh-constitution-justia` → `oh-constitution-codes` |
| Ohio Rules of Civil Procedure | `Civ.R. 12(B)(6)`; `Civ. R. 56(C)`; `Ohio R. Civ. P. 12(b)(6)`; `Rule 60(B) of the Ohio Rules of Civil Procedure` | `oh-rules-civil` |
| Ohio Rules of Evidence | `Ohio R. Evid. 401`; `Rule 702 of the Ohio Rules of Evidence` | `oh-rules-evidence` |
| Ohio Rules of Evidence (bare Evid.R.) *(only once this jurisdiction is known)* | `Evid.R. 702`; `Evid. R. 803(6)` | `oh-rules-evidence` |
| Ohio Rules of Appellate Procedure | `App.R. 26(B)`; `App. R. 12(A)(1)(b)`; `Ohio R. App. P. 26`; `Rule 26(B) of the Ohio Rules of Appellate Procedure` | `oh-rules-appellate` |
| Ohio Rules of Criminal Procedure | `Crim.R. 11(C)(2)`; `Crim. R. 33`; `Ohio R. Crim. P. 11`; `Rule 11 of the Ohio Rules of Criminal Procedure` | `oh-rules-criminal` |
| Rules for the Government of the Bar | `Gov.Bar R. V(4)(G)`; `Gov. Bar R. VI`; `Rule V of the Supreme Court Rules for the Government of the Bar` | `oh-rules-govbar` |
| Ohio Rules of Professional Conduct | `Prof.Cond.R. 1.7`; `Prof. Cond. R. 8.4(c)`; `Ohio Rules of Professional Conduct 1.15`; `Rule 1.7 of the Ohio Rules of Professional Conduct` | `oh-rules-profconduct` |
| Rules of Superintendence for the Courts of Ohio | `Sup.R. 44(C)(2)`; `Sup. R. 11.09`; `Rule 26 of the Rules of Superintendence` | `oh-rules-superintendence` |
| Supreme Court Rules of Practice | `S.Ct.Prac.R. 7.08(B)(4)`; `S.Ct. Prac. R. 18.02`; `Supreme Court Rule of Practice 7.01` | `oh-rules-practice` |
| Rules for the Reporting of Opinions | `Rep.Op.R. 3.4`; `Rep. Op. R. 2.5` | `oh-rules-reporting` |
| Ohio Administrative Code | `Ohio Adm.Code 3701-17-01`; `Ohio Admin. Code 4123-5-01`; `Ohio Adm. Code 4901:1-10-01(A)` | `oh-oac-lii` → `oh-oac-codes` |
| Ohio Administrative Code (bare "OAC" / "of the Administrative Code", shared with Oklahoma) *(only once this jurisdiction is known)* | `OAC 3701-17-01`; `rule 3701-17-01 of the Administrative Code` | `oh-oac-lii` → `oh-oac-codes` |
| Ohio public-domain webcite (YYYY-Ohio-N) | `Harris v. Hilderbrand, 172 Ohio St.3d 471, 2023-Ohio-3005, ¶ 20`; `State v. Hurt, 2022-Ohio-2039, ¶ 5 (8th Dist.)`; `Hendriks v. GNA Canadian Holding Co., 2d Dist. Montgomery No. 30469, 2026-Ohio-1580`; `2025-Ohio-5905 (Ct. Cl.)` | `oh-opinions-rod` → `oh-cases-justia` |
| Ohio official and regional reporters | `172 Ohio St.3d 471`; `74 Ohio St.3d 186`; `65 Ohio St.2d 1`; `150 Ohio App.3d 12`; `123 N.E.3d 456 (Ohio 2019)`; `95 Ohio Misc.2d 1` | `oh-opinions-rod` → `oh-cases-justia` |
| Ohio appellate docket / unreported forms (district, county, case no.) | `8th Dist. Cuyahoga No. 110732`; `7th Dist. Jefferson No. 21 JE 0013`; `Jefferson App. No. 21 JE 0013`; `10th Dist. Franklin No. 01AP-782, 2001 WL 1664064 (Dec. 31, 2001)`; `Cuyahoga App. No. 115771` | `oh-opinions-rod` → `oh-cases-justia` |
| Supreme Court of Ohio case number *(only once this jurisdiction is known)* | `No. 2022-0784`; `Case No. 2026-0866` | `oh-opinions-rod` → `oh-subsequent-history-announcements` |

Regexes (case-insensitive):

- Ohio Revised Code: `(?:\bR\.\s?C\.\s*|\bOhio\s+Rev(?:ised)?\.?\s+Code(?:\s+Ann(?:otated)?\.?)?\s*(?:§+\s*)?|\bO\.?R\.?C\.?\s+(?:§\s*)?)(?P<section>\d{1,4}\.\d{1,4}[A-Za-z]?)(?![\d.])|\bsec(?:tion|\.)\s+(?P<section2>\d{1,4}\.\d{1,4}[A-Za-z]?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+(?:Ohio\s+)?Revised\s+Code|\bR\.\s?C\.\s+Chapter\s+(?P<chapter>\d{1,4})\b|\bChapter\s+(?P<chapter2>\d{1,4})\.?\s+of\s+the\s+(?:Ohio\s+)?Revised\s+Code`
- Ohio session laws / General Assembly bills: `(?P<prefix>(?:Am\.\s*)?(?:Sub\.\s*)?)(?P<chamber>[HS])\.\s*B\.\s*(?:No\.\s*)?(?P<number>\d{1,4}),?\s*(?:\(\s*)?(?P<ga>\d{2,3})(?:st|nd|rd|th)\s+(?:General\s+Assembly|G\.\s?A\.)|(?P<volume>\d{2,3})\s+Ohio\s+Laws,?\s*(?:Part\s+[IVX]+,?\s*)?(?P<page>\d{1,5})`
- Ohio Constitution: `Ohio\s+Const\.\s*,?\s*art\.\s*(?P<article>[IVXL]+),?\s*(?:§|Sec(?:tion|\.)?)\s*(?P<section>\d+[a-z]?)|Article\s+(?P<article2>[IVXL]+),\s+Section\s+(?P<section2>\d+[a-z]?)\s+of\s+the\s+Ohio\s+Constitution|Section\s+(?P<section3>\d+[a-z]?),\s+Article\s+(?P<article3>[IVXL]+),?\s+(?:of\s+the\s+)?Ohio\s+Constitution|Ohio\s+Constitution,\s+Article\s+(?P<article4>[IVXL]+),\s+Section\s+(?P<section4>\d+[a-z]?)`
- Ohio Rules of Civil Procedure: `(?<![A-Za-z]\.\s)(?<![A-Za-z]\.)(?<!Idaho\s)(?<!Iowa\s)(?<!Utah\s)(?<!Ohio\s)\bCiv\.\s?R\.\s*(?P<rule>\d{1,2}(?:\.\d)?)|Ohio\s+R\.\s*Civ\.\s*P\.\s*(?P<rule2>\d{1,2}(?:\.\d)?)|Rule\s+(?P<rule3>\d{1,2}(?:\.\d)?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Ohio\s+Rules\s+of\s+Civil\s+Procedure`
- Ohio Rules of Evidence: `Ohio\s+R\.\s*Evid\.\s*(?P<rule2>\d{3,4})|Rule\s+(?P<rule3>\d{3,4})(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Ohio\s+Rules\s+of\s+Evidence`
- Ohio Rules of Evidence (bare Evid.R.): `\bEvid\.\s?R\.\s*(?P<rule>\d{3,4})`
- Ohio Rules of Appellate Procedure: `(?<![A-Za-z]\.\s)(?<![A-Za-z]\.)(?<!Idaho\s)(?<!Iowa\s)(?<!Utah\s)(?<!Ohio\s)\bApp\.\s?R\.\s*(?P<rule>\d{1,2}(?:\.\d)?)|Ohio\s+R\.\s*App\.\s*P\.\s*(?P<rule2>\d{1,2}(?:\.\d)?)|Rule\s+(?P<rule3>\d{1,2}(?:\.\d)?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Ohio\s+Rules\s+of\s+Appellate\s+Procedure`
- Ohio Rules of Criminal Procedure: `(?<![A-Za-z]\.\s)(?<![A-Za-z]\.)(?<!Idaho\s)(?<!Iowa\s)(?<!Utah\s)(?<!Ohio\s)\bCrim\.\s?R\.\s*(?P<rule>\d{1,2}(?:\.\d)?)|Ohio\s+R\.\s*Crim\.\s*P\.\s*(?P<rule2>\d{1,2}(?:\.\d)?)|Rule\s+(?P<rule3>\d{1,2}(?:\.\d)?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Ohio\s+Rules\s+of\s+Criminal\s+Procedure`
- Rules for the Government of the Bar: `\bGov\.\s?Bar\s+R\.\s*(?P<rule>[IVXL]+)|Rule\s+(?P<rule2>[IVXL]+)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+(?:Supreme\s+Court\s+)?Rules\s+for\s+the\s+Government\s+of\s+the\s+Bar`
- Ohio Rules of Professional Conduct: `\bProf\.\s?Cond\.\s?R\.\s*(?P<rule>\d\.\d{1,2})|Ohio\s+Rules?\s+of\s+Prof(?:essional|')l?\s+Conduct\s+(?:R(?:ule)?\.?\s*)?(?P<rule2>\d\.\d{1,2})|Rule\s+(?P<rule3>\d\.\d{1,2})(?:\([a-z0-9]+\))*\s+of\s+the\s+Ohio\s+Rules\s+of\s+Professional\s+Conduct`
- Rules of Superintendence for the Courts of Ohio: `\bSup\.\s?R\.\s*(?P<rule>\d{1,3}(?:\.\d{1,2})?)|Rule\s+(?P<rule2>\d{1,3}(?:\.\d{1,2})?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Rules\s+of\s+Superintendence`
- Supreme Court Rules of Practice: `\bS\.\s?Ct\.\s?Prac\.\s?R\.\s*(?P<rule>\d{1,2}\.\d{2})|Supreme\s+Court\s+Rules?\s+of\s+Practice\s+(?P<rule2>\d{1,2}\.\d{2})`
- Rules for the Reporting of Opinions: `\bRep\.\s?Op\.\s?R\.\s*(?P<rule>\d\.\d{1,2})`
- Ohio Administrative Code: `Ohio\s+Adm(?:in)?\.?\s?Code\s*(?:§\s*)?(?P<rule>\d{3,4}(?::\d{1,2})?-\d{1,3}-\d{1,3}(?:\.\d{1,2})?)|\brule\s+(?P<rule2>\d{3,4}(?::\d{1,2})?-\d{1,3}-\d{1,3}(?:\.\d{1,2})?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Ohio\s+Administrative\s+Code`
- Ohio Administrative Code (bare "OAC" / "of the Administrative Code", shared with Oklahoma): `\bO\.?A\.?C\.?\s+(?P<rule>\d{3,4}(?::\d{1,2})?-\d{1,3}-\d{1,3}(?:\.\d{1,2})?)|\brule\s+(?P<rule2>\d{3,4}(?::\d{1,2})?-\d{1,3}-\d{1,3}(?:\.\d{1,2})?)(?:\([A-Za-z0-9]+\))*\s+of\s+the\s+Administrative\s+Code`
- Ohio public-domain webcite (YYYY-Ohio-N): `\b(?P<year>(?:199[2-9]|20\d\d))-Ohio-(?P<number>\d{1,5})\b(?:,\s*¶+\s*(?P<para>\d+))?(?:[^()]{0,40}\((?P<district>\d{1,2})(?:st|nd|rd|th)\s+Dist\.)?`
- Ohio official and regional reporters: `(?P<volume>\d{1,3})\s+Ohio\s+(?P<reporter>St\.(?:\s?[23]d)?|App\.(?:\s?[23]d)?|Misc\.(?:\s?2d)?)\s+(?P<page>\d{1,4})|(?P<nevolume>\d{1,3})\s+N\.E\.(?:\s?[23]d)?\s+(?P<nepage>\d{1,4})\s*\((?:Ohio|Ohio\s+Ct\.\s+App\.|Ohio\s+App\.)`
- Ohio appellate docket / unreported forms (district, county, case no.): `(?P<district>\d{1,2})(?:st|nd|rd|th)\s+Dist\.\s+(?P<county>[A-Z][a-z]+(?:\s[A-Z][a-z]+)?)\s+No(?:s)?\.\s*(?P<caseno>[A-Z0-9][A-Z0-9 -]{1,14}?)(?=,|\s*\(|$)|(?P<county2>[A-Z][a-z]+(?:\s[A-Z][a-z]+)?)\s+App\.\s+No(?:s)?\.\s*(?P<caseno2>[A-Z0-9][A-Z0-9 -]{1,14}?)(?=,|\s+and|\.|$)`
- Supreme Court of Ohio case number: `(?:Case\s+)?No\.\s*(?P<year>(?:19|20)\d\d)-(?P<seq>\d{4})\b`

Short forms → URL key:

R.C. → `ohio-revised-code`; Ohio Rev. Code → `ohio-revised-code`; Ohio Rev. Code Ann. → `ohio-revised-code`; ORC → `ohio-revised-code`; Revised Code → `ohio-revised-code`; Ohio Adm.Code → `ohio-administrative-code`; Ohio Admin. Code → `ohio-administrative-code`; OAC → `ohio-administrative-code`; Administrative Code → `ohio-administrative-code`; Ohio Const. → `ohio-constitution`; Ohio Constitution → `ohio-constitution`

Ohio style (Supreme Court of Ohio Writing Manual, from memory) differs from Bluebook: 'R.C. 2305.10' (no §), 'Ohio Adm.Code 3701-17-01', 'Civ.R. 12(B)(6)' with capital division letters, 'Section 16, Article I, Ohio Constitution' (section first), and case cites 'Name, 172 Ohio St.3d 471, 2023-Ohio-3005, ¶ 20' or for appeals 'Name, 2022-Ohio-1555, ¶ 10 (7th Dist.)'; pre-2023 manual form '7th Dist. Jefferson No. 21 JE 0013, 2022-Ohio-1555'. Pinpoint is the ¶ number, which is the same in the slip PDF, the official-version PDF and Ohio St.3d (Rep.Op.R. 2.5 requires numbered paragraphs). Rep.Op.R. 3.4: all court-of-appeals opinions issued after May 1, 2002 may be cited regardless of publication. The webcite alone does not name the court; the URL folder needs it: 0 = Supreme Court, 1-12 = district, 13 = Court of Claims. Take the district from the '(Nth Dist.)' parenthetical or the county ('Jefferson App. No.') via the county table in oh-opinions-rod; otherwise resolve with the ROD WebCite search. Routing guards: bare 'Civ.R. 12', 'Evid.R. 702', 'App.R. 26', 'Crim.R. 11' are Ohio house style, but a bare 'Rule 12' or a federal-rule cite must not route here — require the Ohio abbreviation or Ohio context. 'Revised Code' alone also names Washington's code (Revised Code of Washington): route 'R.C. NNNN.NN' (Ohio sections always contain a dot) or 'of the Revised Code' only with Ohio context. The webcite form YYYY-Ohio-N is unique to Ohio and routes on its own. Ranges like 'R.C. 2305.10 to 2305.12' or 'R.C. 2305.10-.12': take the first section; the regex stops at the first section number. 'Section 1.42' of the Revised Code is valid (Title 1 General Provisions). OAC rules may carry a colon in the agency number (4901:1-10-01) — keep it in the URL. Superintendence Rules were renumbered effective July 1, 2026 (e.g. old Sup.R. 44 → 11.09); older opinions cite old numbers. CourtListener ids (ohio, ohioctapp, ohioctcl) are from memory and unverified. ROUTING after the 2026-10-17 policy: codes.ohio.gov is robots-disallowed, so R.C. → oh-orc-justia, Ohio Const. → oh-constitution-justia, Ohio Adm.Code → oh-oac-lii (all tier 2, disclosed); the blocked official rows stay last in routes_to for link reference only. Regex extended 2026-10-17 for chapter cites ('R.C. Chapter 2744') and 'Ohio Const., Art. I, Sec. 16'. Bare 'OAC …' is shared with the Oklahoma Administrative Code (also colon-numbered), so it routes here only once Ohio is established. Bare 'Evid.R. NNN' (Ohio's usual short form) is context_required: Nebraska writes 'Neb. Evid. R. 702' (split 2026-10-17).

## A. Statutes / code

### `oh-orc-codes` — Ohio Revised Code (codes.ohio.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Ohio Legislative Service Commission (LSC) · text: **link-only** · official: official
- **Coverage:** Current Revised Code, one page per section (Titles 1-63 incl. Title 1 General Provisions), with prior versions for some sections; per-section authenticated PDF; chapter pages hold the full text of every section in the chapter.
- **Access:** `constructible` · format html
  - Pattern: `https://codes.ohio.gov/ohio-revised-code/section-{section}`
  - Placeholders: section = the R.C. number verbatim with its dot and any letter (2305.10, 2903.01, 1.42, 2305.131). Short form https://codes.ohio.gov/orc/{section} redirects to the same page. Chapter page: /ohio-revised-code/chapter-{chapter} (full text of all sections; 2305 = 233K chars). Title index: /ohio-revised-code/title-{title} lists chapters only (no section ranges); the chapter is the part before the dot, so no index hop is needed. Authenticated PDF: /assets/laws/revised-code/authenticated/{title}/{chapter}/{section}/{M-D-YYYY effective}/{section}-{M-D-YYYY}.pdf — the date segment is not derivable; take the 'Download Authenticated PDF' link from the section page.
  - Index: `https://codes.ohio.gov/ohio-revised-code`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: 200 text/plain, one line 'User-agent: * Disallow: /' (no newline); treated as Disallow: / for all agents (policy 2026-10-17)
  - BLOCKED for every route (incl. the /orc/ short form and /assets/… authenticated PDFs). Use oh-orc-justia (tier 2, disclose it). Earlier 2026-10-16 fetches were made before the policy decision and must not be repeated.
- **Currency:** every section page: banner under the search box, plus 'Effective:' and 'Latest Legislation:' lines above the text — observed: "Effective: August 3, 2006 / Latest Legislation: Senate Bill 17 - 126th General Assembly"
- **Official status:** https://codes.ohio.gov/about: UELMA (R.C. 149.21 to 149.27) designates LSC official publisher; electronic Revised Code and Administrative Code 'are official publications (R.C. 149.21 and 149.22)'. Authenticated PDF per section; the stamp verifies integrity, not freedom from error. Unannotated; repeals and court invalidations are not noted.
- **Hazard:** host robots-disallowed (Disallow: /) — never fetch, by any tool
- **Hazard:** no global 'current through' date — LSC updates 'on an ongoing basis' as it completes act review, so very recent acts may be missing
- **Hazard:** repealed sections vanish without notice; renumbered sections appear only under the new number
- **Hazard:** court invalidations not noted
- **Hazard:** chapter pages are very long (WebFetch truncation)
- **Hazard:** authenticated PDF URL contains the effective date — not constructible
- **Probe:** R.C. 2305.10 → `https://codes.ohio.gov/ohio-revised-code/section-2305.10` — expect: "(A) Except as provided in division (C) or (E) of this section"
- **Evidence (2026-10-17):** Before policy (2026-10-16, research): WebFetch: YES, body '(A) Except as provided in division (C) or (E) of', not truncated, 'Effective: August 3, 2006'. fetch_doc.py info: html 9,151 chars. Second citation R.C. 2903.01 (/section-2903.01): fetch_doc grep 'No person shall purposely, and with prior calculation and design' at offset 1083. Also section-1.42 ok; /orc/2305.10 redirects to the section page. Authenticated PDF /assets/laws/revised-code/authenticated/23/2305/2305.10/8-3-2006/2305.10-8-3-2006.pdf: 3 pp, body present. | Re-confirmed blocked 2026-10-17: fetch_doc check: 'REFUSED: robots.txt on codes.ohio.gov disallows ... (rule: Disallow: /)' exit 3; policy reads robots.txt 'User-agent: * Disallow: /' as disallow-all.
- **Notes:** Policy decision 2026-10-17 (coordinator): codes.ohio.gov's one-line robots.txt 'User-agent: * Disallow: /' is read by its evident intent — disallow all automation — so this host is BLOCKED for every route (fetch_doc.py refuses it; WebFetch is not used on it). This hurts: under Ohio's UELMA (R.C. 149.21-149.27) LSC's codes.ohio.gov text is the official, authenticated publication, and there is now no tier-1 text route. URL patterns are kept for reference/linking only. No bulk download or public statute API found (WebSearch for bulk XML/API returned only page URLs). No tier-1 statute text route remains; Cornell LII and public.law have no Revised Code.

### `oh-session-laws-lis` — Ohio General Assembly legislation API (bill versions incl. enrolled acts)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Ohio Legislative Service Commission / Legislative Information Systems · text: **fetch-and-quote** · official: unknown
- **Coverage:** Bills of the 129th and 126th General Assemblies probed, with all versions (introduced → enrolled); 135th GA HB 33 listing also returned. Earlier coverage not established.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format json
  - Pattern: `https://search-prod.lis.state.oh.us/api/v2/general_assembly_{ga}/legislation/{type}{number}/{formatted_version}_{version_id}/pdf`
  - Placeholders: ga = General Assembly number (126, 129, 135); type = hb | sb (also hjr/sjr/hcr/scr presumably, unverified); number unpadded. The version folder is not fixed (SB 202/129th and SB 17/126th enrolled = 05_EN, but 135th HB 33 07_EN 404s): GET https://search-prod.lis.state.oh.us/api/v2/general_assembly_{ga}/legislation/{type}{number} first — a JSON array of versions with formatted_version, version_id ('IN','EN',…), version label, effective_date and governor_signed_date.
  - Index: `https://search-prod.lis.state.oh.us/api/v2/general_assembly_{ga}/legislation/{type}{number}`
  - Navigation: GET the bill JSON → pick the version with version_id 'EN' (as enrolled) → GET …/{formatted_version}_{version_id}/pdf
- **Automation:** WebFetch ok · shell ok · robots: none (robots.txt 404, 'SOLAR API - Page Not Found')
  - Bill JSON for an omnibus bill (HB 33, 135th) is 267K chars — too big for WebFetch; use the shell.
- **Currency:** none stated
- **Official status:** Government API behind legislature.ohio.gov; no official-status statement seen. Enrolled ('EN') PDFs carry blank signature/effective-date blocks.
- **Hazard:** version folder must be read from the JSON
- **Hazard:** Ohio session-law volume cites ('150 Ohio Laws, Part III, 3888') cannot be mapped to this API — only GA + bill number can
- **Hazard:** enrolled PDF shows blank Approved/Effective lines; take dates from the JSON or the R.C. section's 'Latest Legislation' line
- **Probe:** Sub.S.B. No. 202, 129th General Assembly → `https://search-prod.lis.state.oh.us/api/v2/general_assembly_129/legislation/sb202/05_EN/pdf` — expect: "To enact section 2305.402 of the Revised Code to specify"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 5 pp, 'AN ACT To enact section 2305.402 of the Revised Code'; WebFetch same text, '(Substitute Senate Bill Number 202)'. Second: S.B. 17, 126th GA → /general_assembly_126/legislation/sb17/05_EN/pdf, 77 pp PDF. Bill JSON /general_assembly_129/legislation/sb202 lists versions with 'version_id'. | Independent check 2026-10-17: WebFetch YES 'To enact section 2305.402 of the Revised Code to specify'; fetch_doc grep same, 5 pp; second citation Sub.H.B. No. 68, 135th General Assembly ok
- **Notes:** Found via a WebSearch result URL. Session laws as bound volumes (Laws of Ohio) not located online. Second example: Sub.H.B. No. 68, 135th GA → /general_assembly_135/legislation/hb68/05_EN/pdf (10 pp).

### `oh-orc-justia` — Justia — Ohio Revised Code (2025)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Ohio Revised Code editions; unversioned URL serves the 2025 edition (2023, 2024 and earlier editions under /codes/ohio/{year}/).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/ohio/title-{title}/chapter-{chapter}/section-{section_dashed}/`
  - Placeholders: title: for chapters numbered 100 or more, title = chapter // 100 (149 → title-1, 2305 → title-23, 2903 → title-29, 4112 → title-41); chapters 1-99 sit in Title 1 (R.C. 1.42 → title-1/chapter-1). chapter = part of the section number before the dot, unpadded. section_dashed = section with the dot replaced by a hyphen (2305.10 → section-2305-10). Year-specific: insert /{year}/ after /ohio/. If a guess 404s, open https://law.justia.com/codes/ohio/2025/ (lists Title links; the bare /codes/ohio/ page lists only editions) → title → chapter list → section link.
  - Index: `https://law.justia.com/codes/ohio/2025/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable to the shell (Cloudflare challenge on robots.txt)
  - fetch_doc.py: 'REFUSED: law.justia.com refused automated access earlier (robots.txt challenge)'. WebFetch only; a built section URL (2903.01) went through without approval.
- **Currency:** page header and Universal Citation line — observed: "2025 Ohio Revised Code; 'OH Rev Code § 2305.10 (2025)'"
- **Official status:** Page states 'These codes may not be the most recent version' and points to official sources.
- **Hazard:** edition lags the official text by up to a year
- **Hazard:** shell blocked by Cloudflare
- **Hazard:** title index does not show section ranges (not needed: chapter is in the section number)
- **Hazard:** now the ONLY Revised Code text route (codes.ohio.gov robots-disallowed): every quote must disclose 'Justia, 2025 Ohio Revised Code' and that it may lag the official text
- **Hazard:** WebFetch only — fetch_doc.py is refused by Justia's Cloudflare challenge, so the two-fetch rule needs two WebFetch reads
- **Probe:** R.C. 2305.10 → `https://law.justia.com/codes/ohio/title-23/chapter-2305/section-2305-10/` — expect: "Except as provided in division (C) or (E) of this"
- **Evidence (2026-10-17):** WebFetch: YES, 'Except as provided in division (C) or (E) of this'; '2025 Ohio Revised Code'; 'OH Rev Code § 2305.10 (2025)'; complete through (G). Second citation R.C. 2903.01 at /title-29/chapter-2903/section-2903-01/: YES, '(A) No person shall purposely, and with prior calculation and design'. | Independent check 2026-10-17: WebFetch YES 'Except as provided in division (C) or (E) of this'; 'OH Rev Code § 2305.10 (2025)'; complete; second citation R.C. 149.43 (also R.C. 4112.02) ok
- **Notes:** First route for R.C. citations (tier 2, disclosed). public.law has no Ohio edition and Cornell LII does not host the Revised Code (verifier re-confirmed 2026-10-16).

## B. Constitution

### `oh-constitution-codes` — Ohio Constitution (codes.ohio.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Ohio Legislative Service Commission · text: **link-only** · official: unknown
- **Coverage:** Constitution of 1851 as amended (Articles I-XIX, 1851 and 1912 schedules), one page per section with effective date.
- **Access:** `constructible` · format html
  - Pattern: `https://codes.ohio.gov/ohio-constitution/section-{article_arabic}.{section}`
  - Placeholders: article Roman numeral → Arabic (I → 1, IV → 4, XVIII → 18); section verbatim incl. lower-case letter (Art. I § 10a → section-1.10a). Index https://codes.ohio.gov/ohio-constitution lists articles only.
  - Index: `https://codes.ohio.gov/ohio-constitution`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: 200 text/plain, one line 'User-agent: * Disallow: /' (no newline); treated as Disallow: / for all agents (policy 2026-10-17)
  - BLOCKED for every route (incl. the /orc/ short form and /assets/… authenticated PDFs). Use oh-constitution-justia (tier 2, disclose it). Earlier 2026-10-16 fetches were made before the policy decision and must not be repeated.
- **Currency:** 'Effective:' line above each section — observed: "Effective: January 1, 1913 (Art. I § 16)"
- **Official status:** Hosted by LSC with the official Revised Code; the About page's UELMA statement names only the Revised Code and Administrative Code.
- **Hazard:** host robots-disallowed (Disallow: /) — never fetch, by any tool
- **Probe:** Ohio Const. art. I, § 16 → `https://codes.ohio.gov/ohio-constitution/section-1.16` — expect: "All courts shall be open, and every person, for an injury"
- **Evidence (2026-10-17):** Before policy (2026-10-16, research): fetch_doc.py grep: 'All courts shall be open, and every person, for an injury' at offset 713; 1,084 chars. Second: art. IV, § 2 at /section-4.2: '(A) The Supreme Court shall, until otherwise provided by law, consist of seven judges'. art. I § 10a at /section-1.10a: heading present. | Re-confirmed blocked 2026-10-17: fetch_doc check: 'REFUSED: robots.txt on codes.ohio.gov disallows /ohio-constitution/section-1.16' exit 3; policy reads robots.txt 'User-agent: * Disallow: /' as disallow-all.
- **Notes:** Policy decision 2026-10-17 (coordinator): codes.ohio.gov's one-line robots.txt 'User-agent: * Disallow: /' is read by its evident intent — disallow all automation — so this host is BLOCKED for every route (fetch_doc.py refuses it; WebFetch is not used on it). This hurts: under Ohio's UELMA (R.C. 149.21-149.27) LSC's codes.ohio.gov text is the official, authenticated publication, and there is now no tier-1 text route. URL patterns are kept for reference/linking only. legislature.ohio.gov also links the constitution but fails TLS from the shell (see oh-constitution-legislature). Art. XIX (Congressional Redistricting) is not on Justia's article index, so it now has no text route.

### `oh-constitution-legislature` — Ohio General Assembly website (legislature.ohio.gov) — laws pages

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Ohio General Assembly · text: **link-only** · official: unknown
- **Coverage:** Legislature site; reportedly links to codes.ohio.gov for the Constitution and Revised Code.
- **Access:** `link-only` · format html
  - Index: `https://www.legislature.ohio.gov/`
- **Automation:** WebFetch untested · shell tls-error · robots: unreadable: curl 'SSL certificate problem: unable to get local issuer certificate'
  - Shell TLS failure; not retried by another route.
- **Currency:** none
- **Official status:** Not reached.
- **Hazard:** TLS chain fails from the sandbox
- **Probe:**  → `https://www.legislature.ohio.gov/robots.txt`
- **Evidence (2026-10-16):** curl robots.txt: TLS 'unable to get local issuer certificate'; not fetched further. Use oh-constitution-codes.
- **Notes:** Link-only; its constitution/code links lead to codes.ohio.gov, which is now robots-disallowed. Re-checked 2026-10-17: shell TLS failure persists; WebFetch untested.

### `oh-constitution-justia` — Justia — Ohio Constitution

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Preamble, Articles I-XVIII, 1851 and 1912 schedules; one page per section.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/ohio/article-{article_roman_lower}/section-{section}/`
  - Placeholders: article as lower-case Roman numeral (article-i, article-iv, article-xvi); section number as in the citation. Article pages list section links only; the index lists articles only.
  - Index: `https://law.justia.com/constitution/ohio/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - WebFetch only.
- **Currency:** disclaimer only — observed: "This Constitution may not be the most recent version.; history line e.g. '(1994, am. 2017)'"
- **Official status:** Page states 'This Constitution may not be the most recent version.'
- **Hazard:** no date; may lag amendments
- **Hazard:** index lists only up to Article XVIII (official has XIX)
- **Hazard:** shell blocked
- **Hazard:** now the ONLY constitution text route (codes.ohio.gov robots-disallowed)
- **Hazard:** WebFetch only (fetch_doc refused by Cloudflare)
- **Probe:** Ohio Const. art. I, § 16 → `https://law.justia.com/constitution/ohio/article-i/section-16/` — expect: "All courts shall be open, and every person, for an"
- **Evidence (2026-10-17):** WebFetch: YES 'All courts shall be open, and every person, for an'. Index and article-i pages are link lists (body NOT PRESENT); article-i links e.g. /article-i/section-16/. | Independent check 2026-10-17: WebFetch YES 'All courts shall be open, and every person, for an'; disclaimer present; complete; second citation Ohio Const. art. IV, § 2 (also art. I, § 10a) ok
- **Notes:** First route for Ohio Const. citations (tier 2, disclosed; currency = disclaimer plus each section's amendment-history line, e.g. '(1994, am. 2017)'). Verified: art. I § 16, art. IV § 2 (/article-iv/section-2/), art. I § 10a (/article-i/section-10a/). Art. XIX not on the index → no route.

## C. Court rules

### `oh-rules-appellate` — Ohio Rules of Appellate Procedure (PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of Ohio · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full rule set with staff notes/commentary; 83 pp., 182,195 chars of text.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/appellate/AppellateProcedure.pdf`
  - Placeholders: Fixed path; one PDF for the whole set. Re-confirm from the Ohio Rules of Court page if it 404s.
  - Index: `https://www.supremecourt.ohio.gov/laws-rules/ohio-rules-of-court`
  - Navigation: Ohio Rules of Court page → 'Ohio Rules of Appellate Procedure' link
- **Automation:** WebFetch gated · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - Not WebFetch-probed: the built PDF URL waited on approval (evidence.pdf timed out). Expect the ~100K-char WebFetch window seen on the Civil Rules PDF; use fetch_doc.py grep/section or a corpus.
- **Currency:** Ohio Rules of Court page, 'Amended Effective Date' column next to the link (not inside the PDF) — observed: "July 1, 2026"
- **Official status:** Published by the Supreme Court of Ohio on its Ohio Rules of Court page; no official/unofficial statement in the PDF.
- **Hazard:** single long PDF; WebFetch truncation
- **Hazard:** headings mix 'RULE 12.' and 'Rule 26.' capitalisation
- **Probe:** App.R. 26(A) → `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/appellate/AppellateProcedure.pdf` — expect: "Application for Reconsideration; Application for En Banc Consideration"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 83 pp, 182,195 chars; 'Rule 26. Application for Reconsideration; Application for En Banc Consideration' at offset 146,619 (p. 64); 'RULE 12. Determination and Judgment on Appeal.' at 100,128. | Independent check 2026-10-17: fetch_doc grep (WebFetch gated on this host; ROD built URL timed out): 'Rule 26. Application for Reconsideration; Application for En Banc' offset 146,633 p.64; second citation App.R. 4(A) ok

### `oh-rules-civil` — Ohio Rules of Civil Procedure (full set PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of Ohio · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full rule set with staff notes/commentary; 927 pp., 2,137,404 chars of text.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/civil/CivilProcedure.pdf`
  - Placeholders: Fixed path; one PDF for the whole set. Re-confirm from the Ohio Rules of Court page if it 404s.
  - Index: `https://www.supremecourt.ohio.gov/laws-rules/ohio-rules-of-court`
  - Navigation: Ohio Rules of Court page → 'Ohio Rules of Civil Procedure' link
- **Automation:** WebFetch ok (truncated) · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - WebFetch window ends after Rule 5 of 86 (Rule 12 is at ~160K chars). The PDF is 927 pages because it includes staff notes and the Appendix of Forms (forms from ~p. 229). Use fetch_doc.py or the corpus.
- **Currency:** Ohio Rules of Court page, 'Amended Effective Date' column next to the link (not inside the PDF) — observed: "July 1, 2026"
- **Official status:** Published by the Supreme Court of Ohio on its Ohio Rules of Court page; no official/unofficial statement in the PDF.
- **Hazard:** single long PDF; WebFetch truncation
- **Hazard:** WebFetch text stops after Rule 5
- **Hazard:** staff notes follow each rule; Appendix of Forms is most of the page count
- **Probe:** Civ.R. 12(B) → `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/civil/CivilProcedure.pdf` — expect: "Every defense, in law or fact, to a claim for relief"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 927 pp, 2,137,404 chars; 'RULE 12. Defenses and Objections' at offset 160,622 (p. 66); 12(B) 'Every defense, in law or fact, to a claim for relief' at 162,269. WebFetch: Rule 12(B) NOT PRESENT — text stops after Rule 5 ('[Content truncated due to length...]'). | Independent check 2026-10-17: fetch_doc grep (WebFetch gated on this host; ROD built URL timed out): 12(B) 'Every defense, in law or fact, to a claim for relief' offset 162,269 p.66; second citation Civ.R. 56(C) ok

### `oh-rules-criminal` — Ohio Rules of Criminal Procedure (PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of Ohio · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full rule set with staff notes/commentary; 193 pp., 374,255 chars of text.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/criminal/CriminalProcedure.pdf`
  - Placeholders: Fixed path; one PDF for the whole set. Re-confirm from the Ohio Rules of Court page if it 404s.
  - Index: `https://www.supremecourt.ohio.gov/laws-rules/ohio-rules-of-court`
  - Navigation: Ohio Rules of Court page → 'Ohio Rules of Criminal Procedure' link
- **Automation:** WebFetch gated · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - Not WebFetch-probed: the built PDF URL waited on approval (evidence.pdf timed out). Expect the ~100K-char WebFetch window seen on the Civil Rules PDF; use fetch_doc.py grep/section or a corpus.
- **Currency:** Ohio Rules of Court page, 'Amended Effective Date' column next to the link (not inside the PDF) — observed: "July 1, 2026"
- **Official status:** Published by the Supreme Court of Ohio on its Ohio Rules of Court page; no official/unofficial statement in the PDF.
- **Hazard:** single long PDF; WebFetch truncation
- **Probe:** Crim.R. 11.1 → `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/criminal/CriminalProcedure.pdf` — expect: "Standard Notice Concerning Possession or Purchase of a Firearm"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 193 pp, 374,255 chars; 'RULE 11.1. Standard Notice Concerning Possession or Purchase of a Firearm.' at offset 77,826 (p. 35). | Independent check 2026-10-17: fetch_doc grep (WebFetch gated on this host; ROD built URL timed out): 'RULE 11.1. Standard Notice Concerning Possession or Purchase of a Firearm' p.35; second citation Crim.R. 33 ok

### `oh-rules-evidence` — Ohio Rules of Evidence (PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of Ohio · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full rule set with staff notes/commentary; 102 pp., 185,608 chars of text.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/evidence/evidence.pdf`
  - Placeholders: Fixed path; one PDF for the whole set. Re-confirm from the Ohio Rules of Court page if it 404s.
  - Index: `https://www.supremecourt.ohio.gov/laws-rules/ohio-rules-of-court`
  - Navigation: Ohio Rules of Court page → 'Ohio Rules of Evidence' link
- **Automation:** WebFetch gated · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - Not WebFetch-probed: the built PDF URL waited on approval (evidence.pdf timed out). Expect the ~100K-char WebFetch window seen on the Civil Rules PDF; use fetch_doc.py grep/section or a corpus.
- **Currency:** Ohio Rules of Court page, 'Amended Effective Date' column next to the link (not inside the PDF) — observed: "July 1, 2025"
- **Official status:** Published by the Supreme Court of Ohio on its Ohio Rules of Court page; no official/unofficial statement in the PDF.
- **Hazard:** single long PDF; WebFetch truncation
- **Hazard:** Rule 702 sits at ~99K chars — at or past the WebFetch window edge
- **Probe:** Evid.R. 702 → `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/evidence/evidence.pdf` — expect: "A witness may testify as an expert if the proponent demonstrates"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 102 pp, 185,608 chars; 'RULE 702. Testimony by Experts.' at offset 98,861 (p. 59), text 'A witness may testify as an expert if the proponent demonstrates'. Second: 'Rule 616(C) Specific contradiction' staff note at p. 56. | Independent check 2026-10-17: fetch_doc grep (WebFetch gated on this host; ROD built URL timed out): 'RULE 702. ... A witness may testify as an expert if the proponent' p.59; second citation Evid.R. 803(6) ok

### `oh-rules-govbar` — Supreme Court Rules for the Government of the Bar of Ohio (PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of Ohio · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full rule set with staff notes/commentary; 276 pp., 715,862 chars of text.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/govbar/govbar.pdf`
  - Placeholders: Fixed path; one PDF for the whole set. Re-confirm from the Ohio Rules of Court page if it 404s.
  - Index: `https://www.supremecourt.ohio.gov/laws-rules/ohio-rules-of-court`
  - Navigation: Ohio Rules of Court page → 'Supreme Court Rules for the Government of the Bar of Ohio' link
- **Automation:** WebFetch gated · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - Not WebFetch-probed: the built PDF URL waited on approval (evidence.pdf timed out). Expect the ~100K-char WebFetch window seen on the Civil Rules PDF; use fetch_doc.py grep/section or a corpus.
- **Currency:** Ohio Rules of Court page, 'Amended Effective Date' column next to the link (not inside the PDF) — observed: "Sept. 6, 2026"
- **Official status:** Published by the Supreme Court of Ohio on its Ohio Rules of Court page; no official/unofficial statement in the PDF.
- **Hazard:** single long PDF; WebFetch truncation
- **Hazard:** Roman-numbered rules with numbered sections (Gov.Bar R. V(4)(G) = Rule V, Section 4(G))
- **Hazard:** grep 'RULE VI. ' with the period — 'RULE VI' alone also hits 'former Rule VI' notes
- **Probe:** Gov.Bar R. V → `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/govbar/govbar.pdf` — expect: "RULE V. DISCIPLINARY PROCEDURE Section 1. Board of Professional Conduct"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 276 pp, 715,862 chars; 'RULE V. DISCIPLINARY PROCEDURE Section 1. Board of Professional Conduct' at offset 102,791 (p. 41). | Independent check 2026-10-17: fetch_doc grep (WebFetch gated on this host; ROD built URL timed out): 'RULE V. DISCIPLINARY PROCEDURE Section 1. Board of Professional Conduct' p.41; second citation Gov.Bar R. VI ok

### `oh-rules-practice` — Supreme Court Rules of Practice (PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of Ohio · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full rule set with staff notes/commentary; 128 pp., 254,512 chars of text.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/practice/rulesofpractice.pdf`
  - Placeholders: Fixed path; one PDF for the whole set. Re-confirm from the Ohio Rules of Court page if it 404s.
  - Index: `https://www.supremecourt.ohio.gov/laws-rules/ohio-rules-of-court`
  - Navigation: Ohio Rules of Court page → 'Supreme Court Rules of Practice' link
- **Automation:** WebFetch gated · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - Not WebFetch-probed: the built PDF URL waited on approval (evidence.pdf timed out). Expect the ~100K-char WebFetch window seen on the Civil Rules PDF; use fetch_doc.py grep/section or a corpus.
- **Currency:** Ohio Rules of Court page, 'Amended Effective Date' column next to the link (not inside the PDF) — observed: "May 1, 2025"
- **Official status:** Published by the Supreme Court of Ohio on its Ohio Rules of Court page; no official/unofficial statement in the PDF.
- **Hazard:** single long PDF; WebFetch truncation
- **Hazard:** the probe phrase hits the table of contents first (p. 11); the rule body is at p. 49
- **Probe:** S.Ct.Prac.R. 7.01 → `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/practice/rulesofpractice.pdf` — expect: "Rule 7.01. Institution of Jurisdictional Appeal"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 128 pp, 254,512 chars; table of contents lists 'Rule 7.01. Institution of Jurisdictional Appeal' and 'Rule 7.02. Memorandum in Support of Jurisdiction' (p. 11). | Independent check 2026-10-17: fetch_doc grep (WebFetch gated on this host; ROD built URL timed out): 'Rule 7.01. Institution of Jurisdictional Appeal' TOC p.11 and body p.49; second citation S.Ct.Prac.R. 18.02 ok

### `oh-rules-profconduct` — Ohio Rules of Professional Conduct (PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of Ohio · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full rule set with staff notes/commentary; 207 pp., 537,206 chars of text.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/ProfConduct/profConductRules.pdf`
  - Placeholders: Fixed path; one PDF for the whole set. Re-confirm from the Ohio Rules of Court page if it 404s.
  - Index: `https://www.supremecourt.ohio.gov/laws-rules/ohio-rules-of-court`
  - Navigation: Ohio Rules of Court page → 'Ohio Rules of Professional Conduct' link
- **Automation:** WebFetch gated · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - Not WebFetch-probed: the built PDF URL waited on approval (evidence.pdf timed out). Expect the ~100K-char WebFetch window seen on the Civil Rules PDF; use fetch_doc.py grep/section or a corpus.
- **Currency:** Ohio Rules of Court page, 'Amended Effective Date' column next to the link (not inside the PDF) — observed: "Jan. 1, 2026"
- **Official status:** Published by the Supreme Court of Ohio on its Ohio Rules of Court page; no official/unofficial statement in the PDF.
- **Hazard:** single long PDF; WebFetch truncation
- **Hazard:** heading form 'RULE 1.7:' with a colon; curly apostrophes in text
- **Hazard:** grep the heading with its colon ('RULE 8.4:') — the bare number drowns in cross-references
- **Probe:** Prof.Cond.R. 1.7 → `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/ProfConduct/profConductRules.pdf` — expect: "A lawyer’s acceptance or continuation of representation of a client creates"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 207 pp, 537,206 chars; 'RULE 1.7: CONFLICT OF INTEREST: CURRENT CLIENTS (a) A lawyer’s acceptance or continuation' at offset 111,437 (p. 41). | Independent check 2026-10-17: fetch_doc grep (WebFetch gated on this host; ROD built URL timed out): 'RULE 1.7: CONFLICT OF INTEREST: CURRENT CLIENTS (a) A lawyer’s acceptance' p.41; second citation Prof.Cond.R. 8.4 ok

### `oh-rules-reporting` — Supreme Court Rules for the Reporting of Opinions (PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of Ohio · text: **fetch-and-quote** · official: unknown
- **Coverage:** Rules on publication, webcites, numbered paragraphs and citability of opinions; 8 pp. Short enough for one WebFetch window.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/reporting/Report.pdf`
  - Placeholders: Fixed path; one PDF for the whole set. Re-confirm from the Ohio Rules of Court page if it 404s.
  - Index: `https://www.supremecourt.ohio.gov/laws-rules/ohio-rules-of-court`
  - Navigation: Ohio Rules of Court page → 'Supreme Court Rules for the Reporting of Opinions' link
- **Automation:** WebFetch gated · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - Not WebFetch-probed: the built PDF URL waited on approval (evidence.pdf timed out). Expect the ~100K-char WebFetch window seen on the Civil Rules PDF; use fetch_doc.py grep/section or a corpus.
- **Currency:** Ohio Rules of Court page, 'Amended Effective Date' column next to the link (not inside the PDF) — observed: "July 1, 2012"
- **Official status:** Published by the Supreme Court of Ohio on its Ohio Rules of Court page; no official/unofficial statement in the PDF.
- **Probe:** Rep.Op.R. 3.4 → `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/reporting/Report.pdf` — expect: "All opinions of the courts of appeals issued after May 1, 2002 may be cited"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 8 pp, 7,676 chars; Rep.Op.R. 3.4 'All opinions of the courts of appeals issued after May 1, 2002 may be cited as legal authority'; Rep.Op.R. 2.5 numbered paragraphs. | Independent check 2026-10-17: fetch_doc grep (WebFetch gated on this host; ROD built URL timed out): 'Rep.Op.R. 3.4. Use of Opinions. All opinions of the courts of appeals' p.6; second citation Rep.Op.R. 2.5 ok

### `oh-rules-superintendence` — Rules of Superintendence for the Courts of Ohio (PDF)

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of Ohio · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full rule set with staff notes/commentary; 536 pp., 780,009 chars of text.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/superintendence/Superintendence.pdf`
  - Placeholders: Fixed path; one PDF for the whole set. Re-confirm from the Ohio Rules of Court page if it 404s.
  - Index: `https://www.supremecourt.ohio.gov/laws-rules/ohio-rules-of-court`
  - Navigation: Ohio Rules of Court page → 'Rules of Superintendence for the Courts of Ohio' link
- **Automation:** WebFetch gated · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - Not WebFetch-probed: the built PDF URL waited on approval (evidence.pdf timed out). Expect the ~100K-char WebFetch window seen on the Civil Rules PDF; use fetch_doc.py grep/section or a corpus.
- **Currency:** Ohio Rules of Court page, 'Amended Effective Date' column next to the link (not inside the PDF) — observed: "Aug. 6, 2026"
- **Official status:** Published by the Supreme Court of Ohio on its Ohio Rules of Court page; no official/unofficial statement in the PDF.
- **Hazard:** single long PDF; WebFetch truncation
- **Hazard:** 2026 restructuring renumbered the rules (effective July 1, 2026): pre-2026 citations (e.g. Sup.R. 44-47 public access) must be mapped via the commentary or the 'Rules of Superintendence Restructuring' page
- **Probe:** Sup.R. 11.09 (former Sup.R. 44) → `https://www.supremecourt.ohio.gov/docs/LegalResources/Rules/superintendence/Superintendence.pdf` — expect: "Rule 44 was renumbered to Rule 11.09"
- **Evidence (2026-10-17):** fetch_doc.py: PDF 536 pp, 780,009 chars; commentary 'Rule 44 was renumbered to Rule 11.09 as part of the 2026 restructuring' at offset 572,431 (p. 349). Search for 'RULE 44.' found no rule heading — old numbers are gone. | Independent check 2026-10-17: fetch_doc grep (WebFetch gated on this host; ROD built URL timed out): 'Rule 44 was renumbered to Rule 11.09' offset 572,431 p.349; second citation Sup.R. 11.09 ok

## D. Administrative code

### `oh-oac-codes` — Ohio Administrative Code (codes.ohio.gov)

- **Status:** BLOCKED 2026-10-17 · **Tier 1** · Ohio Legislative Service Commission · text: **link-only** · official: official
- **Coverage:** All rules in effect, published on their effective dates as filed through the electronic rule-filing system; one page per rule; chapter pages.
- **Access:** `constructible` · format html
  - Pattern: `https://codes.ohio.gov/ohio-administrative-code/rule-{rule}`
  - Placeholders: rule verbatim incl. the colon in agency numbers (3701-17-01, 4123-5-01, 4901:1-10-01). Chapter: /ohio-administrative-code/chapter-{agency}-{chapter} (e.g. chapter-3701-17). Authenticated PDF: /assets/laws/administrative-code/authenticated/{agency}/{division or 0}/{chapter}/{rule}_{YYYYMMDD effective}.pdf — date not derivable; take the link from the rule page.
  - Index: `https://codes.ohio.gov/ohio-administrative-code`
- **Automation:** WebFetch blocked · shell blocked-robots · robots: 200 text/plain, one line 'User-agent: * Disallow: /' (no newline); treated as Disallow: / for all agents (policy 2026-10-17)
  - BLOCKED for every route (incl. the /orc/ short form and /assets/… authenticated PDFs). Use oh-oac-lii (tier 2, disclose it). Earlier 2026-10-16 fetches were made before the policy decision and must not be repeated.
- **Currency:** rule page: 'Effective:' and 'Promulgated Under:' lines; WebFetch also reported a 'Last updated' line — observed: "Effective: July 17, 2025 / Last updated July 17, 2025 at 7:45 AM"
- **Official status:** https://codes.ohio.gov/about: under UELMA (R.C. 149.21-149.27) LSC's electronic Administrative Code is an official publication; authenticated PDF per rule.
- **Hazard:** host robots-disallowed (Disallow: /) — never fetch, by any tool
- **Hazard:** rescinded rules vanish without notice
- **Hazard:** court invalidations not noted
- **Probe:** Ohio Adm.Code 3701-17-01 → `https://codes.ohio.gov/ohio-administrative-code/rule-3701-17-01` — expect: "As used in rules 3701-17-01 to 3701-17-26 of the Administrative"
- **Evidence (2026-10-17):** Before policy (2026-10-16, research): WebFetch: YES 'As used in rules 3701-17-01 to 3701-17-26 of the Administrative'; 'Effective: July 17, 2025'; not truncated. fetch_doc.py: 12,038 chars. Second: rule-4123-5-01 'The administrator of workers' compensation may reorganize the work'. Colon form rule-4901:1-10-01 resolves. Authenticated PDF …/3701/0/17/3701-17-01_20250717.pdf: 7 pp. | Re-confirmed blocked 2026-10-17: fetch_doc check: 'REFUSED: robots.txt on codes.ohio.gov disallows /ohio-administrative-code/rule-3701-17-01' exit 3; policy reads robots.txt 'User-agent: * Disallow: /' as disallow-all.
- **Notes:** Policy decision 2026-10-17 (coordinator): codes.ohio.gov's one-line robots.txt 'User-agent: * Disallow: /' is read by its evident intent — disallow all automation — so this host is BLOCKED for every route (fetch_doc.py refuses it; WebFetch is not used on it). This hurts: under Ohio's UELMA (R.C. 149.21-149.27) LSC's codes.ohio.gov text is the official, authenticated publication, and there is now no tier-1 text route. URL patterns are kept for reference/linking only.

### `oh-oac-lii` — Cornell LII — Ohio Administrative Code

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Ohio Administrative Code, one page per rule, with Notes (effective date, five-year review dates, promulgated under).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/ohio/Ohio-Admin-Code-{rule_hyphenated}`
  - Placeholders: rule_hyphenated = the rule number with any ':' replaced by '-' (3701-17-01 → Ohio-Admin-Code-3701-17-01; 4901:1-10-01 → Ohio-Admin-Code-4901-1-10-01). The verbatim colon URL silently returns the OAC title index, not the rule. Index-anchored fallback: /regulations/ohio/title-{agency, ':'→'-'} → chapter-{chapter, ':'→'-'} (e.g. title-4901-1 → chapter-4901-1-10) → rule link.
  - Index: `https://www.law.cornell.edu/regulations/ohio`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay: 10; /regulations allowed
  - Respect the 10-second crawl delay; prefer fetch_doc.py (honours it) over WebFetch — LII returned HTTP 429 to WebFetch after ~4 page loads.
- **Currency:** page header and Notes 'Effective:' — observed: "State regulations are updated quarterly; Notes 'Effective: 1/1/2018'"
- **Official status:** Third-party mirror: 'State regulations are updated quarterly'.
- **Hazard:** STALE risk: LII can lag by years (3701-17-01 showed 'Effective: 1/1/2018' while the official rule is effective July 17, 2025); no official cross-check is possible now that codes.ohio.gov is blocked — always disclose LII's 'Effective:' date with any quote
- **Hazard:** redline markup: LII page text can carry struck-through amendment text (e.g. '~~shall~~' in 3745-1-04) and duplicate lettered paragraphs (two '(P)' in 3701-17-01); never quote struck text, and check the quote does not span a deletion
- **Hazard:** colon rules need ':'→'-' in the slug; the colon URL returns the title index without an error
- **Hazard:** HTTP 429 to WebFetch after a few loads
- **Probe:** Ohio Adm.Code 3701-17-01 → `https://www.law.cornell.edu/regulations/ohio/Ohio-Admin-Code-3701-17-01` — expect: "As used in rules 3701-17-01 to 3701-17-26 of the Administrative"
- **Evidence (2026-10-17):** WebFetch: YES 'As used in rules 3701-17-01 to 3701-17-26 of the Administrative'; 'Effective: 1/1/2018'. fetch_doc.py 13,781 chars, same. Second: Ohio-Admin-Code-4123-5-01 'may reorganize the work of the bureau', 'Effective: 12/12/2019'. | Independent check 2026-10-17: WebFetch YES 'As used in rules 3701-17-01 to 3701-17-26 of the Administrative'; 'Effective: 1/1/2018'; second citation Ohio Adm.Code 3745-1-04 ok ('Effective: 3/20/2024'); Ohio Adm.Code 4901:1-10-01 FAILED with the verbatim colon slug (title index returned) — works as Ohio-Admin-Code-4901-1-10-01 ('Effective: 4/8/2024'); pattern fixed
- **Notes:** First route for Ohio Adm.Code citations (tier 2, disclosed). regulations.justia.com also mirrors the OAC but is outside the tier-2 allowlist; law.justia.com carries no Administrative Code.

## D. Administrative register

### `oh-register` — Register of Ohio

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Ohio Legislative Service Commission (with Common Sense Initiative) · text: **link-only** · official: unknown
- **Coverage:** Proposed, adopted, emergency and no-change rule filings with rule text, summaries, fiscal analyses and hearing notices.
- **Read via (in order):** **fetch tool**
- **Access:** `search-only` · format html
  - Placeholders: Search form fields: rule number parts (Agency #, Division #, Chapter #, Rule #, Supp #), agency, keywords in title, hearing/effective/file date ranges, limit (all/active/no-change/emergency). Form method not established.
  - Index: `https://www.registerofohio.state.oh.us/rules/search`
  - Navigation: search by rule number → filing record
- **Automation:** WebFetch ok · shell tls-error · robots: unreadable: TLS 'unable to get local issuer certificate' (both www and bare host)
  - fetch_doc.py: 'TLS certificate chain does not verify from this sandbox'. WebFetch reads the search page (URL from a WebSearch result).
- **Currency:** none observed
- **Official status:** codes.ohio.gov/about calls it 'an electronic gazette published by LSC'; the search page shows no official-status text.
- **Hazard:** shell TLS failure
- **Hazard:** search results not probed
- **Hazard:** session ids (;jsessionid=…) in indexed URLs
- **Probe:** Register of Ohio rule search → `https://www.registerofohio.state.oh.us/rules/search`
- **Evidence (2026-10-16):** WebFetch: search page with Agency #/Division #/Chapter #/Rule # fields; no filing links. Shell: TLS failure. No filing probed. | Re-check 2026-10-17: shell TLS failure confirmed; WebFetch not re-run.

## E. Case law

### `oh-opinions-rod` — Supreme Court of Ohio Reporter of Decisions — Opinions & Announcements

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of Ohio, Office of the Reporter of Decisions · text: **fetch-and-quote** · official: official
- **Coverage:** Supreme Court: 1992- (1995 search returned 516 items incl. 74 Ohio St.3d 186 = 1995-Ohio-166; webcites retroactively assigned to pre-2002 website documents). Courts of Appeals: sparse 1999-2000 (1999: 234 rows; 1993, 1997: 0), comprehensive from about 2001 (2001 and 2002 both hit the 1000-row cap). Court of Claims (folder 13): present (2025: 163 rows). Also daily Case Announcements (merit decisions, jurisdictional decisions, motion rulings, official-version releases), each with its own webcite.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.supremecourt.ohio.gov/rod/docs/pdf/{court}/{year}/{year}-Ohio-{number}.pdf`
  - Placeholders: From webcite YYYY-Ohio-N: year = YYYY, number = N unpadded. court = 0 for the Supreme Court (and its Case Announcements), 1-12 for the appellate district, 13 for the Court of Claims. The webcite does not encode the court: use the '(Nth Dist.)' parenthetical, or the county ('Jefferson App. No.', '8th Dist. Cuyahoga No.') mapped by this fixed table — 1 = Hamilton; 2 = Champaign, Clark, Darke, Greene, Miami, Montgomery; 3 = Allen, Auglaize, Crawford, Defiance, Hancock, Hardin, Henry, Logan, Marion, Mercer, Paulding, Putnam, Seneca, Shelby, Union, Van Wert, Wyandot; 4 = Adams, Athens, Gallia, Highland, Hocking, Jackson, Lawrence, Meigs, Pickaway, Pike, Ross, Scioto, Vinton, Washington; 5 = Ashland, Coshocton, Delaware, Fairfield, Guernsey, Holmes, Knox, Licking, Morgan, Morrow, Muskingum, Perry, Richland, Stark, Tuscarawas; 6 = Erie, Fulton, Huron, Lucas, Ottawa, Sandusky, Williams, Wood; 7 = Belmont, Carroll, Columbiana, Harrison, Jefferson, Mahoning, Monroe, Noble; 8 = Cuyahoga; 9 = Lorain, Medina, Summit, Wayne; 10 = Franklin; 11 = Ashtabula, Geauga, Lake, Portage, Trumbull; 12 = Brown, Butler, Clermont, Clinton, Fayette, Madison, Preble, Warren. Never cycle through folders; if the court is unknown, resolve the webcite with the ROD search (oh-subsequent-history-announcements pattern_rules / script). ASP.NET form at https://www.supremecourt.ohio.gov/rod/docs/ (POST only; a plain GET with the field names is ignored and returns the default newest-first listing, and a GET carrying __VIEWSTATE returns 404). POST fields (prefix ctl00$MainContent$): tbQueryText (full text, quotes for phrases), ddlCourt (0 Supreme Court, 1-12 districts, 13 Court of Claims, 98 Misc., 99 All Sources, 100 All District Courts), ddlDecidedYearMin/Max (1992-2026), ddlCounty, tbCaseNumber, tbAuthor, tbWebCiteYear + tbWebCiteNumber (unique lookup, other filters ignored), tbCitation (e.g. '172 Ohio St.3d 471' → webcite), ddlRowsPerPage, btnSubmit=Submit, plus the page's hidden __VIEWSTATE/__VIEWSTATEGENERATOR. Rows give caption, case no., topics, author, reporter cite or county, decided/posted dates, WebCite. Results cap at 1000 rows. CRITICAL: the year selects default to the CURRENT year — always send every select field (ddlCourt, ddlDecidedYearMin, ddlDecidedYearMax, ddlCounty, ddlRowsPerPage) with explicit values and set ddlDecidedYearMin=1992 (or the lower decision's year) and ddlDecidedYearMax=the current year for full-text, case-number and party searches; a POST with only the hidden fields and a text field returns 0 rows, and '"2022-Ohio-1555"' (court 0) with default years returned 0 rows versus 3 rows with ddlDecidedYearMin=1992. (WebCite and Citation lookups ignore the other filters.)
  - Index: `https://www.supremecourt.ohio.gov/rod/docs/`
  - Navigation: constructible from webcite + court; else ROD search (POST) → row WebCite → PDF
- **Automation:** WebFetch ok · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - WebFetch reads these PDFs, but constructed URLs wait on approval — use fetch_doc.py for constructed URLs. Long opinions (75K chars for 2022-Ohio-2039) fit; very long ones may exceed WebFetch's window. Search is POST-only (ASP.NET viewstate); a plain GET returns only the newest-first default listing (582 rows on 2026-10-16).
- **Currency:** search rows show Decided/Posted dates; default listing is newest first — observed: "newest item posted 10/16/2026 (2026-Ohio-4060)"
- **Official status:** Rep.Op.R. 3.3 requires all court-of-appeals and Court of Claims opinions to be posted here; the site posts 'Ohio Official Reports versions' replacing slip opinions (announcement 2026-Ohio-3997 'SLIP OPINIONS REPLACED BY OHIO OFFICIAL REPORTS VERSIONS'); PDF cite line then carries the Ohio St.3d cite.
- **Hazard:** ROD POST search silently returns 0 rows for earlier years unless ddlDecidedYearMin is set (defaults to the current year) — a 0-row result is NOT evidence of no further review
- **Hazard:** webcite does not name the court — the URL folder must come from the district/county
- **Hazard:** slip PDFs are replaced in place by the official version (cite line changes; ¶ numbers do not)
- **Hazard:** pagination is slip pagination; pinpoint by ¶ not by Ohio St.3d page
- **Hazard:** search is POST-only
- **Hazard:** pre-2001 appellate coverage sparse; pre-1992 none
- **Hazard:** search results cap at 1000 rows
- **Probe:** Harris v. Hilderbrand, 172 Ohio St.3d 471, 2023-Ohio-3005 → `https://www.supremecourt.ohio.gov/rod/docs/pdf/0/2023/2023-Ohio-3005.pdf` — expect: "In this appeal from the Seventh District Court of Appeals, we"
- **Evidence (2026-10-17):** fetch_doc.py: /rod/docs/pdf/0/2023/2023-Ohio-3005.pdf 12 pp, '[Cite as Harris v. Hilderbrand, 172 Ohio St.3d 471, 2023-Ohio-3005.]', '{¶ 1} In this appeal from the Seventh District Court of Appeals'; slip page numbers 2,3,4 with 'January Term, 2023' running heads (no Ohio St.3d page breaks). Appellate: /7/2022/2022-Ohio-1555.pdf (Jefferson) 19 pp; /8/2022/2022-Ohio-2039.pdf (Cuyahoga) 43 pp; /2/2026/2026-Ohio-1580.pdf (Montgomery) 'SECOND APPELLATE DISTRICT MONTGOMERY COUNTY'; /1/2026/2026-Ohio-1178 (Hamilton), /11/2026/2026-Ohio-3514 (Trumbull) ok; /0/2022/2022-Ohio-1555.pdf 404 (wrong court folder). WebFetch on search-result URLs in /rod/docs/pdf/0/ (2023-Ohio-3741, 2024-Ohio-989, 2024-Ohio-2967, 2018-Ohio-1429) returned full text, not truncated; built opinion URL 2023-Ohio-3005 was gated. ROD POST search: WebCite 2022-1555 → 1 row 'Harris v. Hilderbrand 21 JE 0013 … Jefferson … 2022-Ohio-1555'; Citation '172 Ohio St.3d 471' → 2023-Ohio-3005; Case No. 2022-0784 → same. | Independent check 2026-10-17: WebFetch gated (approval timeout); fetch_doc grep '{¶ 1} In this appeal from the Seventh District Court of Appeals' p.1; second citation State v. Moore, 2026-Ohio-96 (Lucas App. Nos. L-24-1180, L-24-1181) ok
- **Notes:** Pre-May-2002 appellate decisions are usually cited by WL number plus district/county/case number; resolve via ROD case-number search for the district. Justices' annual opinion lists exist at /docs/SCO/justices/{name}/Opinions.pdf (search results; not probed).

### `oh-cases-justia` — Justia — Ohio case law

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court of Ohio, Courts of Appeals (First-Twelfth Districts), Court of Claims, Court of Common Pleas collections (year ranges not checked).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/ohio/{court-slug}/{year}/{docket-slug}.html`
  - Placeholders: court-slug: supreme-court-of-ohio | first-district-court-of-appeals … twelfth-district-court-of-appeals | court-of-claims | court-of-common-pleas. year = decision year. Supreme Court docket '2022-0784' → '2022-0784'. Appellate case no. lower-cased with spaces → hyphens ('21 JE 0013' → '21-je-0013'). Year listing https://law.justia.com/cases/ohio/{court-slug}/{year}/ lists every decision if a guess 404s.
  - Index: `https://law.justia.com/cases/ohio/`
  - Navigation: court → year listing → case
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (Cloudflare challenge)
  - WebFetch only; built case URLs went through.
- **Currency:** none
- **Official status:** Third-party compilation of the court-posted opinions.
- **Hazard:** shell blocked
- **Hazard:** may hold the slip version only
- **Hazard:** case-number slug variants
- **Probe:** Harris v. Hilderbrand, 2023-Ohio-3005 → `https://law.justia.com/cases/ohio/supreme-court-of-ohio/2023/2022-0784.html` — expect: "In this appeal from the Seventh District Court of Appeals,"
- **Evidence (2026-10-17):** WebFetch: YES '{¶ 1} In this appeal from the Seventh District Court of Appeals,' {¶ 1}-{¶ 34}, complete. Second: /seventh-district-court-of-appeals/2022/21-je-0013.html '[Cite as Harris v. Hilderbrand, 2022-Ohio-1555.]', ¶ markers preserved. | Independent check 2026-10-17: WebFetch YES '{¶ 1} In this appeal from the Seventh District Court of Appeals,' ¶1-¶34 complete

## F. Subsequent history

### `oh-docket-clerk` — Supreme Court of Ohio Clerk — online docket (case information)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Supreme Court of Ohio, Office of the Clerk · text: **link-only** · official: unknown
- **Coverage:** Supreme Court cases by case year/number, with docket, parties, decision and issues tabs; search by caption and prior (lower-court) case number.
- **Access:** `link-only` · format html
  - Pattern: `https://www.supremecourt.ohio.gov/clerk/ecms/#/caseinfo/{case_year}/{case_seq}`
  - Placeholders: Supreme Court case No. 2022-0784 → #/caseinfo/2022/0784. The page is an Ember single-page app; data comes from POST Ajax.ashx (actions include CaseSearch with paramPriorCaseNumber, GetCaseInfo-style CaseInfo model) carrying an X-CSRF-TOKEN header — not probed.
  - Index: `https://www.supremecourt.ohio.gov/clerk/ecms/`
- **Automation:** WebFetch untested · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - fetch_doc.py returns 0 chars of text (JS shell): usable as a link only.
- **Currency:** none
- **Official status:** Court's own docket system; no statement seen.
- **Hazard:** JavaScript-only app
- **Hazard:** POST JSON endpoint with CSRF header
- **Probe:** Supreme Court No. 2022-0784 → `https://www.supremecourt.ohio.gov/clerk/ecms/#/caseinfo/2022/0784`
- **Evidence (2026-10-16):** fetch_doc.py: html, 0 chars of text (SPA). site.min.js shows route '/caseinfo/:caseyear/:casenumber' and ajaxCall('Ajax.ashx', …) with action 'CaseSearch' and 'paramPriorCaseNumber'.

### `oh-subsequent-history-announcements` — Supreme Court of Ohio Case Announcements (jurisdictional decisions) via ROD full-text search

- **Status:** VERIFIED 2026-10-17 (independent) · **Tier 1** · Supreme Court of Ohio · text: **fetch-and-quote** · official: official
- **Coverage:** Case Announcements from 1992 (1995-Ohio-423 'Merit Docket') to date; sections include 'APPEALS ACCEPTED FOR REVIEW', 'APPEALS NOT ACCEPTED FOR REVIEW', merit decisions, reconsideration, dismissals, official versions released. Each not-accepted entry names the lower case: '2026-0866. Lewis v. BMW of Westlake. Cuyahoga App. No. 115771, 2026-Ohio-1870.'
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `search-only` · format pdf
  - Pattern: `https://www.supremecourt.ohio.gov/rod/docs/pdf/0/{year}/{year}-Ohio-{number}.pdf`
  - Placeholders: From the decision below: POST the ROD search with ddlCourt=0 and tbQueryText='"YYYY-Ohio-N"' (the lower court's webcite, quoted) → rows list every Supreme Court opinion and Case Announcement mentioning it (2022-Ohio-1555 → 2022-Ohio-3135 (accepted, 9/13/2022), 2023-Ohio-3005 (merit opinion), 2023-Ohio-3042 (announcement); 2026-Ohio-1870 → 2026-Ohio-3977 (not accepted, 10/13/2026), 2026-Ohio-3073). Open the announcement PDF (folder 0) and find the lower webcite under the disposition heading. For pre-2002 or unpublished decisions without a webcite, search the lower case number or party name. ASP.NET form at https://www.supremecourt.ohio.gov/rod/docs/ (POST only; a plain GET with the field names is ignored and returns the default newest-first listing, and a GET carrying __VIEWSTATE returns 404). POST fields (prefix ctl00$MainContent$): tbQueryText (full text, quotes for phrases), ddlCourt (0 Supreme Court, 1-12 districts, 13 Court of Claims, 98 Misc., 99 All Sources, 100 All District Courts), ddlDecidedYearMin/Max (1992-2026), ddlCounty, tbCaseNumber, tbAuthor, tbWebCiteYear + tbWebCiteNumber (unique lookup, other filters ignored), tbCitation (e.g. '172 Ohio St.3d 471' → webcite), ddlRowsPerPage, btnSubmit=Submit, plus the page's hidden __VIEWSTATE/__VIEWSTATEGENERATOR. Rows give caption, case no., topics, author, reporter cite or county, decided/posted dates, WebCite. Results cap at 1000 rows. CRITICAL: the year selects default to the CURRENT year — always send every select field (ddlCourt, ddlDecidedYearMin, ddlDecidedYearMax, ddlCounty, ddlRowsPerPage) with explicit values and set ddlDecidedYearMin=1992 (or the lower decision's year) and ddlDecidedYearMax=the current year for full-text, case-number and party searches; a POST with only the hidden fields and a text field returns 0 rows, and '"2022-Ohio-1555"' (court 0) with default years returned 0 rows versus 3 rows with ddlDecidedYearMin=1992. (WebCite and Citation lookups ignore the other filters.)
  - Index: `https://www.supremecourt.ohio.gov/rod/docs/`
  - Navigation: ROD POST full-text search on the lower webcite → Case Announcements row → PDF (folder 0)
- **Automation:** WebFetch ok · shell ok · robots: www.supremecourt.ohio.gov: User-agent * — Disallow /cms/ and /Content/ODCMB/ only; /docs/ and /rod/ allowed
  - Search is POST-only (WebFetch cannot run it); the announcement PDFs are WebFetch- and fetch_doc-readable.
- **Currency:** announcement date in the cite line — observed: "[Cite as 10/13/2026 Case Announcements, 2026-Ohio-3977.]"
- **Official status:** Each Case Announcement is itself cited by webcite (e.g. '[Cite as 10/13/2026 Case Announcements, 2026-Ohio-3977.]').
- **Hazard:** ROD POST search silently returns 0 rows for earlier years unless ddlDecidedYearMin is set (defaults to the current year) — a 0-row result is NOT evidence of no further review
- **Hazard:** POST-only search
- **Hazard:** announcement wording: 'APPEALS NOT ACCEPTED FOR REVIEW' (older: 'DISCRETIONARY APPEALS NOT ACCEPTED' / 'jurisdiction declined' — phrase search for these returned 0 rows in 2026, so search the webcite, not the phrase)
- **Hazard:** one lower decision can appear in several announcements (jurisdiction, merit decision, reconsideration)
- **Probe:** Lewis v. BMW of Westlake, 2026-Ohio-1870 (8th Dist.) → S.Ct. No. 2026-0866 → `https://www.supremecourt.ohio.gov/rod/docs/pdf/0/2026/2026-Ohio-3977.pdf` — expect: "APPEALS NOT ACCEPTED FOR REVIEW"
- **Evidence (2026-10-17):** ROD POST tbQueryText '"2026-Ohio-1870"' (court 0) → 2 rows incl. 2026-Ohio-3977; fetch_doc grep in 2026-Ohio-3977.pdf (10 pp): 'APPEALS NOT ACCEPTED FOR REVIEW … 2026-0866. Lewis v. BMW of Westlake. Cuyahoga App. No. 115771, 2026-Ohio-1870.' Second: '"2022-Ohio-1555"' → 2022-Ohio-3135 ('Appeals accepted for review'), 2023-Ohio-3005, 2023-Ohio-3042. | Independent check 2026-10-17: fetch_doc grep: 'APPEALS NOT ACCEPTED FOR REVIEW'; '2026-0866. Lewis v. BMW of Westlake. Cuyahoga App. No. 115771'; second citation State v. Wilson, 2026-Ohio-1178 (Hamilton App. No. C-240696) ok
- **Notes:** The Clerk's online docket (oh-docket-clerk) also shows jurisdictional dispositions per Supreme Court case number.

## Not available (do not look for these again)

- **statutes** — public.law edition of Ohio law: public.law covers only CA, CO, FL, NV, NY, OR, TX (per the DE run's check of the public.law home page, 2026-10-16); no Ohio site. (2026-10-16)
- **statutes** — Cornell LII Ohio Revised Code / Constitution: LII hosts the Ohio Administrative Code (/regulations/ohio); no Revised Code collection was found (LII state pages link out to official sites). (2026-10-16)
- **statutes** — Official bulk download / API for the Revised Code or Administrative Code: codes.ohio.gov offers per-section HTML and authenticated PDFs only; WebSearch for bulk XML/API found nothing beyond page URLs. (2026-10-16)
- **case_law** — Free Ohio St.3d / Ohio App.3d page pagination: Official-version PDFs carry the Ohio St.3d volume and first page in the cite line but slip page numbers inside (2023-Ohio-3005: pages '2', '3', '4'); Ohio pinpoints by ¶ instead. (2026-10-16)
- **case_law** — ROD documents before 1992: ROD year selector starts at 1992; Supreme Court 1995 rows exist; Courts of Appeals 1993 and 1997 returned 0 rows. (2026-10-16)
- **statutes** — Any tier-1 text route for the Revised Code, Constitution and Administrative Code: codes.ohio.gov robots.txt 'User-agent: * Disallow: /' treated as disallow-all (policy 2026-10-17); legislature.ohio.gov links there and fails TLS; no bulk download. (2026-10-17)

## Corpus candidates (maintainers)

- `oh-rules-civil` — 927 pp / 2.1M chars; WebFetch text stops after Rule 5 of 86
- `oh-rules-evidence` — 102 pp / 186K chars; Rule 702 at ~99K chars, at the WebFetch window edge
- `oh-rules-appellate` — 83 pp / 182K chars; App.R. 26 at ~147K chars
- `oh-rules-criminal` — 193 pp / 374K chars
- `oh-rules-govbar` — 276 pp / 716K chars
- `oh-rules-profconduct` — 207 pp / 537K chars; Rule 1.7 at ~111K chars
- `oh-rules-superintendence` — 536 pp / 780K chars; renumbered July 1, 2026
- `oh-rules-practice` — 128 pp / 255K chars

## Open questions

- Rules-of-court PDFs other than Civ.R. were not WebFetch-probed (built URLs gated); window position assumed from the Civ.R. probe.
- Register of Ohio: shell TLS failure; search form method and per-filing URLs not established.
- Clerk docket Ajax.ashx endpoint not probed (CSRF header).
- LIS API: enrolled-version folder varies (135th HB 33 07_EN 404); earliest General Assembly covered not established.
- Art. XIX of the Ohio Constitution has no text route (codes.ohio.gov blocked; not on Justia's index) — re-check Justia.
- CourtListener ids (ohio, ohioctapp, ohioctcl) unverified.
- Justia case-law generalisation (2022-Ohio-1555 appellate page) not re-run by the verifier (WebFetch HTTP 429); row marked independent on its main probe only.
