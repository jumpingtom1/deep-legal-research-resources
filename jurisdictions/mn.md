# Minnesota (MN) — free legal sources

_Generated from `data/mn.json` (compiled 2026-10-17, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes, session laws, constitution, court rules, Minnesota Rules and the State Register are all on revisor.mn.gov, with clean per-section, per-rule and per-part URLs that both WebFetch and fetch_doc.py read (statutes and agency rules are UELMA-authenticated; the court-rule pages are disclaimed as unofficial). Case law is the gap: mncourts.gov shows only the current week's releases, its opinion PDFs are robots-disallowed and the shell gets a Cloudflare challenge; the State Law Library's static archive (1996 to Feb. 2016) is WebFetch-readable, while its 1996-present search is CAPTCHA-protected. Justia (tier 2) is the working route for opinion text, constructible by docket. Subsequent history: the Supreme Court keeps the Court of Appeals docket on review; denials are on the current PFR list or the 1996-2016 archive PFR PDFs, otherwise only in P-MACS (blocked).

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Minnesota Supreme Court | `minn (unverified)` | Minn. | N.W.3d, N.W.2d, N.W., Minn. | — |
| Minnesota Court of Appeals | `minnctapp (unverified)` | Minn. Ct. App. | N.W.3d, N.W.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Minnesota Statutes | `Minn. Stat. § 541.05 (2024)`; `Minn. Stat. § 541.05, subd. 1(5) (2024)`; `Minn. Stat. § 336.2-725`; `Minn. Stat. §§ 609.185-.19`; `Minn. Stat. §§ 541.05-541.07`; `Minn. Stat. Ann. § 260C.007`; `Minnesota Statutes, section 541.05`; `Minnesota Statutes 2024, section 609.185`; `section 541.05 of the Minnesota Statutes`; `Minn. Stat. ch. 541`; `Minnesota Statutes, chapter 363A`; `M.S.A. § 541.05` | `mn-statutes-revisor` → `mn-statutes-justia` |
| Minnesota Session Laws | `2024 Minn. Laws ch. 127, art. 2, § 5`; `1984 Minn. Laws ch. 543, § 69`; `Laws 2015, chapter 5, article 15, section 18`; `2015 c 5 art 15 s 18` | `mn-laws-revisor` |
| Minnesota Constitution | `Minn. Const. art. I, § 8`; `Minn. Const. art. XIII, § 4`; `Article I, Section 8 of the Minnesota Constitution`; `Minnesota Constitution, article I, section 7`; `Minn. Const. art. 1, § 7` | `mn-constitution-revisor` → `mn-constitution-justia` |
| Minnesota Rules of Civil Procedure | `Minn. R. Civ. P. 12.02(e)`; `Minn. R. Civ. P. 56.03`; `Rule 12.02 of the Minnesota Rules of Civil Procedure`; `Minn. R. Civ. P. 4.043` | `mn-courtrules-revisor` → `mn-courtrules-revisor-pdf` |
| Minnesota Rules of Evidence | `Minn. R. Evid. 702`; `Minn. R. Evid. 803(6)`; `Rule 404(b) of the Minnesota Rules of Evidence` | `mn-courtrules-revisor` → `mn-courtrules-revisor-pdf` |
| Minnesota Rules of Civil Appellate Procedure | `Minn. R. Civ. App. P. 103.03(a)`; `Minn. R. Civ. App. P. 136.01, subd. 1(c)`; `Rule 117 of the Minnesota Rules of Civil Appellate Procedure` | `mn-courtrules-revisor` → `mn-courtrules-revisor-pdf` |
| Minnesota Rules of Criminal Procedure | `Minn. R. Crim. P. 15.01`; `Minn. R. Crim. P. 28.02, subd. 4(3)`; `Rule 15.05 of the Minnesota Rules of Criminal Procedure` | `mn-courtrules-revisor` → `mn-courtrules-revisor-pdf` |
| General Rules of Practice for the District Courts | `Minn. Gen. R. Prac. 115.03`; `Minn. Gen. R. Prac. 302.01`; `Rule 115 of the Minnesota General Rules of Practice` | `mn-courtrules-revisor` → `mn-courtrules-revisor-pdf` |
| Minnesota Rules of Professional Conduct | `Minn. R. Prof. Conduct 1.7`; `MRPC 8.4(c)`; `Rule 1.7 of the Minnesota Rules of Professional Conduct` | `mn-courtrules-revisor` → `mn-courtrules-revisor-pdf` |
| Minnesota Rules (administrative) | `Minn. R. 7050.0222`; `Minn. R. 7050.0222, subp. 4 (2023)`; `Minnesota Rules, part 1400.5100`; `Minn. R. ch. 7050`; `Minnesota Rules, chapter 1400` | `mn-rules-revisor` → `mn-rules-lii` |
| Minnesota State Register | `50 Minn. Reg. 123`; `9 SR 2276`; `26 S.R. 391` | `mn-register-revisor` |
| Reported Minnesota cases (N.W. / Minn.) | `Larson v. Wasemiller, 738 N.W.2d 300 (Minn. 2007)`; `Dukowitz v. Hannon Sec. Servs., 841 N.W.2d 147, 150 (Minn. 2014)`; `[name], 700 N.W.2d 100 (Minn. App. 2005) (form only)`; `[name], 700 N.W.2d 100 (Minn. Ct. App. 2005), review denied (Minn. Sept. 20, 2005) (form only)`; `312 Minn. 1` | `mn-cases-justia` → `mn-opinions-lawlib-archive` → `mn-opinions-mncourts` |
| Unpublished / nonprecedential Court of Appeals opinions and appellate docket numbers | `Thigpen v. Best Home Care LLC, No. A23-1544 (Minn. App. July 29, 2024)`; `State v. Senn, No. A25-1783 (Minn. App. Oct. 5, 2026)`; `A25-1783`; `C3-96-1234` | `mn-cases-justia` → `mn-opinions-lawlib-archive` → `mn-opinions-mncourts` |
| Minnesota Supreme Court review dispositions | `review denied (Minn. Mar. 1, 2023)`; `review granted (Minn. Oct. 15, 2024)`; `review denied (Minn. Sept. 30, 2026)` | `mn-pfr-orders-mncourts` → `mn-pfr-archive-lawlib` → `mn-subsequent-justia` |

Regexes (case-insensitive):

- Minnesota Statutes: `(?:Minn(?:esota)?\.?\s*Stat(?:utes)?\.?(?:\s+Ann\.)?|M\.\s*S\.\s*A\.?)\s*(?:(?:19|20)\d\d,?\s*)?(?:§§?|sec(?:tion|s?\.)|,\s*sections?)\s*(?P<section>\d{1,3}[A-Z]{0,2}\.\d+[A-Za-z]?(?:-\d+(?!\d)(?!\.\d))?)|(?:Minn(?:esota)?\.?\s*Stat(?:utes)?\.?(?:\s+Ann\.)?)\s*(?:(?:19|20)\d\d)?,?\s*(?:ch\.|chapter)\s*(?P<chapter>\d{1,3}[A-Z]{0,2})\b|sec(?:tion|\.)\s*(?P<section2>\d{1,3}[A-Z]{0,2}\.\d+[A-Za-z]?(?:-\d+(?!\d)(?!\.\d))?)(?:,\s*subd(?:ivision|\.)\s*\d+[a-z]?)?(?:\([a-z0-9]+\))*\s+of\s+(?:the\s+)?Minnesota\s+Statutes`
- Minnesota Session Laws: `(?P<year>(?:18|19|20)\d\d)\s+Minn\.\s*Laws\s+(?:\d(?:st|nd|rd|th)\s+Spec\.\s*Sess\.\s+)?ch\.\s*(?P<chapter>\d+)|Laws\s+(?P<year2>(?:18|19|20)\d\d),\s*(?:First\s+Special\s+Session\s+)?chapter\s+(?P<chapter2>\d+)|\b(?P<year3>(?:18|19|20)\d\d)\s+c\s+(?P<chapter3>\d+)(?:\s+art\s+\d+)?\s+s\s+\d+`
- Minnesota Constitution: `Minn\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+|\d{1,2}),?\s*§\s*(?P<section>\d+[a-z]?)|Article\s+(?P<article2>[IVXL]+|\d{1,2}),?\s+Section\s+(?P<section2>\d+[a-z]?)\s+of\s+the\s+Minnesota\s+Constitution|Minnesota\s+Constitution,?\s+article\s+(?P<article3>[IVXL]+|\d{1,2}),?\s+section\s+(?P<section3>\d+[a-z]?)`
- Minnesota Rules of Civil Procedure: `Minn\.\s*R\.\s*Civ\.\s*P\.\s*(?P<rule>\d{1,3})(?:\.(?P<sub>\d+))?|Rule\s+(?P<rule2>\d{1,3})(?:\.\d+)?(?:\([a-z0-9]+\))*\s+of\s+the\s+Minnesota\s+Rules\s+of\s+Civil\s+Procedure`
- Minnesota Rules of Evidence: `Minn\.\s*R\.\s*Evid\.\s*(?P<rule>\d{3,4})|Rule\s+(?P<rule2>\d{3,4})(?:\([a-z0-9]+\))*\s+of\s+the\s+Minnesota\s+Rules\s+of\s+Evidence`
- Minnesota Rules of Civil Appellate Procedure: `Minn\.\s*R\.\s*Civ\.\s*App\.\s*P\.\s*(?P<rule>\d{3})(?:\.\d+)?|Rule\s+(?P<rule2>\d{3})(?:\.\d+)?\s+of\s+the\s+Minnesota\s+Rules\s+of\s+Civil\s+Appellate\s+Procedure`
- Minnesota Rules of Criminal Procedure: `Minn\.\s*R\.\s*Crim\.\s*P\.\s*(?P<rule>\d{1,2})(?:\.\d+)?|Rule\s+(?P<rule2>\d{1,2})(?:\.\d+)?\s+of\s+the\s+Minnesota\s+Rules\s+of\s+Criminal\s+Procedure`
- General Rules of Practice for the District Courts: `Minn\.\s*Gen\.\s*R\.\s*Prac\.\s*(?P<rule>\d{1,3})(?:\.\d+)?|Rule\s+(?P<rule2>\d{1,3})(?:\.\d+)?\s+of\s+the\s+Minnesota\s+General\s+Rules\s+of\s+Practice`
- Minnesota Rules of Professional Conduct: `(?:Minn\.\s*R\.\s*Prof(?:'l|\.)?\s*Conduct|MRPC)\s*(?P<rule>\d\.\d{1,2})|Rule\s+(?P<rule2>\d\.\d{1,2})(?:\([a-z0-9]+\))*\s+of\s+the\s+Minnesota\s+Rules\s+of\s+Professional\s+Conduct`
- Minnesota Rules (administrative): `Minn(?:esota)?\.?\s*R(?:ules)?\.?,?\s*(?:pt\.|part)?\s*(?P<part>\d{4}\.\d{4})|Minn(?:esota)?\.?\s*R(?:ules)?\.?,?\s*(?:ch\.|chapter)\s*(?P<chapter>\d{4})`
- Minnesota State Register: `(?P<volume>\d{1,2})\s+(?:Minn\.\s*Reg\.|S\.?R\.?)\s+(?P<page>\d{1,5})`
- Reported Minnesota cases (N.W. / Minn.): `(?P<volume>\d{1,4})\s+N\.\s*W\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})(?:,\s*\d+(?:-\d+)?)?\s*\((?P<court>Minn\.(?:\s*(?:Ct\.\s*)?App\.)?)\s*(?P<year>\d{4})\)|(?P<mvol>\d{1,3})\s+Minn\.\s+(?P<mpage>\d{1,4})\b`
- Unpublished / nonprecedential Court of Appeals opinions and appellate docket numbers: `\b(?P<docket>A(?P<yy>\d{2})-(?P<num>\d{1,4}))\b|\b(?P<olddocket>C[0-9]-\d{2}-\d{1,4})\b|(?P<year>(?:19|20)\d\d)\s+WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Minn\.(?:\s*(?:Ct\.\s*)?App\.)?`
- Minnesota Supreme Court review dispositions: `review\s+(?P<disposition>denied|granted|dismissed)\s*\(Minn\.\s*(?P<date>[A-Z][a-z]{2,4}\.?\s+\d{1,2},\s*(?P<year>\d{4}))\)`

Short forms → URL key:

Minn. R. Civ. P. → `cp`; Minn. R. Evid. → `ev`; Minn. R. Crim. P. → `cr`; Minn. Gen. R. Prac. → `gp`; Minn. R. Civ. App. P. → `ap/subtype/rcap`; Minn. R. Prof. Conduct → `pr/subtype/cond`; MRPC → `pr/subtype/cond`; Minn. R. Juv. Delinq. P. → `ju`; Minn. R. Juv. Prot. P. → `ju`; Minn. Sent. Guidelines → `sg`; Minn. Spec. R. Prac. (Ct. App.) → `ap/subtype/spec`; Minn. R. Civ. App. P. (family) → `ap/subtype/flam`

No public-domain citation format: Minnesota cites N.W.2d / N.W.3d (Minn. reports ended at vol. 312, 1977, from memory). Minn. R. Civ. App. P. 136.01, subd. 1(c) (effective Aug. 1, 2020): nonprecedential opinions are not binding but may be cited as persuasive; older 'unpublished' opinions are governed by Minn. Stat. § 480A.08, subd. 3. Minnesota style uses 'Minn. App.' where Bluebook uses 'Minn. Ct. App.'; both are matched. The same appellate docket number (A##-####) is used in the Court of Appeals and, on review, in the Supreme Court (Thigpen, A23-1544, verified on Justia), so a docket finds the later Supreme Court decision. Pre-2000s dockets look like C3-96-1234. Route bare docket numbers (A25-1783) and WL cites here only with Minnesota context: 'A##-####' collides with other courts' docket styles. Bare 'Rule 12' or 'R. Civ. P.' without 'Minn.' must not route here. The prose form of the General Rules of Practice requires 'Minnesota' ('Rule 115 of the Minnesota General Rules of Practice'): the bare 'General Rules of Practice' also names North Carolina's 'General Rules of Practice for the Superior and District Courts' (build.py --cross). Constitution articles are matched in Roman or Arabic numerals ('art. 1, § 7'). 'Minn. R.' followed immediately by NNNN.NNNN is an administrative rule part (Minn. R. 7050.0222); 'Minn. R. Civ. P.', 'Minn. R. Evid.' etc. are court rules — the admin regex requires digits right after 'Minn. R.'. Statute sections are CHAPTER.SECTION (541.05, 260C.007, 3E.04); UCC sections carry a hyphen (336.2-725). A range 'Minn. Stat. §§ 609.185-.19' or '§§ 541.05-541.07' is a span: the regex keeps the first section and does not read the hyphen as part of the number (only '-digits' not followed by '.digit' is kept, as in 336.2-725). Revisor history notes use '2015 c 5 art 15 s 18' (session law) and '9 SR 2276' (State Register). 'SR' and 'Minn. Reg.' should only route here with Minnesota context. law_aliases map court-rule citation prefixes to the Revisor's court_rules path key used in mn-courtrules-revisor's url_pattern. CourtListener ids 'minn' and 'minnctapp' are from memory, unverified. Examples marked (form only) illustrate citation shape, not real cases; the WL branch of the docket pattern has no example (no real WL number was verified).

## A. Statutes / code

### `mn-laws-revisor` — Minnesota Session Laws (Revisor of Statutes)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Minnesota Office of the Revisor of Statutes · text: **fetch-and-quote** · official: official
- **Coverage:** Session laws by year and chapter; regular and special sessions.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.revisor.mn.gov/laws/{year}/{special_session}/{chapter}/`
  - Placeholders: special_session = 0 for the regular session, 1, 2 … for special sessions (2021 Minn. Laws 1st Spec. Sess. ch. 11 → /laws/2021/1/11/, verified) (from the revisor's own links, e.g. /laws/2015/0/5/laws.15.18.0 for '2015 c 5 art 15 s 18'). chapter unpadded. Section anchor form seen in history links: /laws/{year}/0/{chapter}/laws.{article}.{section}.0.
  - Index: `https://www.revisor.mn.gov/laws/`
- **Automation:** WebFetch untested · shell ok · robots: revisor.mn.gov: User-agent * — Disallow /alpha/, /beta/, /search/doc_result.php, /bills/status_results.php, /rules/status/result; /statutes, /laws, /rules, /court_rules, /constitution, /state_register allowed
  - Omnibus chapters are enormous (2024 c 127 = 4.17M chars; 2015 c 5 = 390K chars): use the script's grep/section, never WebFetch.
- **Currency:** page heading — observed: "Minnesota Session Laws - 2024 Regular Session"
- **Official status:** Pages carry an 'Authenticate' link (UELMA authenticated PDF, Minn. Stat. ch. 3E) and the footer 'Official Publication of the State of Minnesota'.
- **Hazard:** very large omnibus chapters exceed WebFetch window
- **Probe:** 2024 Minn. Laws ch. 127 → `https://www.revisor.mn.gov/laws/2024/0/127/` — expect: "Minnesota Session Laws - 2024 Regular Session"
- **Evidence (2026-10-16):** Script: 200 html 4,174,473 chars; heading 'Laws 93rd Legislature (2023 - 2024) 2024 Regular Session Chapter 127'. /laws/2015/0/5/: 389,733 chars.

### `mn-statutes-revisor` — Minnesota Statutes (Revisor of Statutes)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Minnesota Office of the Revisor of Statutes · text: **fetch-and-quote** · official: official
- **Coverage:** Current edition (2025 Minnesota Statutes) per section; prior editions by year from the 1940s/1905 compilations onward (/statutes/{year}/cite/{section}); version lists per section; full chapter text at /statutes/cite/{chapter}/full.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.revisor.mn.gov/statutes/cite/{section}`
  - Placeholders: section verbatim as cited, chapter prefix included (541.05, 609.185, 336.2-725, 260C.007). No padding. Specific edition: https://www.revisor.mn.gov/statutes/{year}/cite/{section} (verified 2024 and 2025). Legacy form /statutes/?id={section} 301-redirects to /statutes/cite/{section}. Authenticated PDF: /statutes/cite/{section}/pdf. Chapter TOC: /statutes/cite/{chapter}; whole chapter: /statutes/cite/{chapter}/full (very long: ch. 609 = 1.06M chars). Subdivision anchors: /statutes/{year}/cite/{section}/subd/{section}.{n}.
  - Index: `https://www.revisor.mn.gov/statutes/`
- **Automation:** WebFetch gated · shell ok · robots: revisor.mn.gov: User-agent * — Disallow /alpha/, /beta/, /search/doc_result.php, /bills/status_results.php, /rules/status/result; /statutes, /laws, /rules, /court_rules, /constitution, /state_register allowed
  - Script is the primary route. Section pages are 8-11K chars of text (nav menu ~5.4K chars precedes the body), so WebFetch reads them whole. WebFetch on the bare built URL /statutes/cite/541.05 hit PROVENANCE_REQUIRED (permission prompt) — the search-surfaced form /statutes/2025/cite/609.185 and /statutes/?id=… went through. Repealed sections return a stub '[Repealed, …]', not body text.
- **Currency:** page heading above the section and in the right-hand resource box — observed: "2025 Minnesota Statutes"
- **Official status:** https://www.revisor.mn.gov/statutes/info: two official versions — the printed edition and the online authenticated PDFs designated under Minn. Stat. § 3E.04, subd. 2 (UELMA). HTML pages carry the footer 'Official Publication of the State of Minnesota' and an 'Authenticate' link; per-section PDF at /statutes/cite/{section}/pdf.
- **Hazard:** Current edition is 2025: 2026 session-law amendments are not in the text until the 2026 edition; check /statutes/table2?full={section} (Statutes Changed, Table 2) and 'Recent History' on the page
- **Hazard:** repealed sections return a short repeal stub (e.g. 441.51 'MS 1984 [Repealed, 1984 c 543 s 69]')
- **Hazard:** full-chapter pages are huge (ch. 609 ≈ 1.06M chars) — use per-section pages
- **Hazard:** built URLs may need WebFetch approval; the script route is reliable
- **Probe:** Minn. Stat. § 541.05 → `https://www.revisor.mn.gov/statutes/cite/541.05` — expect: "Except where the Uniform Commercial Code otherwise prescribes, the following actions"
- **Evidence (2026-10-16):** Script: 200 html 8,731 chars; '541.05 VARIOUS CASES, SIX YEARS.' then 'Except where the Uniform Commercial Code otherwise prescribes'; heading '2025 Minnesota Statutes'. Also 609.185 (10,681 chars, 'Whoever does any of the following is guilty of murder in the first degree'), 336.2-725 ('An action for breach of any contract for sale must be commenced'). WebFetch /statutes/2025/cite/609.185: YES, complete, '2025 Minnesota Statutes'. /statutes/2024/cite/541.05: '2024 Minnesota Statutes'. /statutes/cite/541.05/pdf: PDF 1 p.
- **Notes:** Index pages are unnecessary: the chapter is the part of the section number before the dot.

### `mn-statutes-justia` — Justia — Minnesota Statutes (2025)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Minnesota Statutes editions 1997-2025 (29 editions listed); unversioned URLs serve 2025.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/codes/minnesota/{chapter_group}/chapter-{chapter}/section-{section_dashed}/`
  - Placeholders: chapter_group is a range slug such as chapters-540-552, chapters-324-342, chapters-609-624, or chapter-13d for single-chapter groups; take it from the 2025 index, whose link texts DO show chapter ranges. chapter lower-case (chapter-541, chapter-260c). section_dashed = section with '.' replaced by '-' (541.05 → section-541-05; 336.2-725 → section-336-2-725). Year-specific editions: /codes/minnesota/{year}/… (index verified, sections not).
  - Index: `https://law.justia.com/codes/minnesota/2025/`
  - Navigation: 2025 index → 'Chapters A - B' group containing the chapter → chapter-{chapter} → section-{section_dashed}
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: robots.txt returns 403 Cloudflare 'Just a moment...' to the shell
  - Script: 'law.justia.com refused automated access (robots.txt challenge)'. WebFetch only.
- **Currency:** page heading and universal citation — observed: "2025 Minnesota Statutes; 'MN Stat § 541.05 (2025)'"
- **Official status:** Page says 'These codes may not be the most recent version'; universal citation 'is not necessarily the official citation'.
- **Hazard:** edition lag (annual)
- **Hazard:** shell blocked by Cloudflare
- **Hazard:** group slug needs the index hop
- **Probe:** Minn. Stat. § 541.05 → `https://law.justia.com/codes/minnesota/chapters-540-552/chapter-541/section-541-05/` — expect: "Except where the Uniform Commercial Code otherwise prescribes, the following"
- **Evidence (2026-10-16):** WebFetch: YES, Subds. 1-2 and History complete; 'MN Stat § 541.05 (2025)'. Second citation /chapters-324-342/chapter-336/section-336-2-725/: YES '(1) An action for breach of any contract for sale'; 'MN Stat § 336.2-725 (2025)'.

## B. Constitution

### `mn-constitution-revisor` — Minnesota Constitution (Revisor of Statutes)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Minnesota Office of the Revisor of Statutes · text: **fetch-and-quote** · official: unknown
- **Coverage:** Whole constitution (Arts. I-XIV) on one page; version list.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.revisor.mn.gov/constitution/#section_{article_arabic}_{section}`
  - Placeholders: Article may be cited in Roman or Arabic numerals (art. I = art. 1). Single page; anchors id="article_{n}" and id="section_{n}_{s}" with the article in Arabic numerals (Art. I § 8 → #section_1_8). The anchor does not change what WebFetch reads; the whole page (~80K chars) fits in one window.
  - Index: `https://www.revisor.mn.gov/constitution/`
- **Automation:** WebFetch ok · shell ok · robots: revisor.mn.gov: User-agent * — Disallow /alpha/, /beta/, /search/doc_result.php, /bills/status_results.php, /rules/status/result; /statutes, /laws, /rules, /court_rules, /constitution, /state_register allowed
  - 79,554 chars; complete in one WebFetch window.
- **Currency:** top of the text gives adoption/revision dates; the 2025-01-09 version date appears only in the Version List / PDF link (/constitution/pdf/version/2025-01-09…) — observed: "Generally Revised November 5, 1974; PDF version 2025-01-09"
- **Official status:** Revisor page; footer 'Official Publication of the State of Minnesota'; a dated PDF version is linked (/constitution/pdf/version/2025-01-09…). No UELMA statement seen for the constitution specifically.
- **Hazard:** no explicit 'current through' statement; check the Version List and LRL constitutional amendments page
- **Probe:** Minn. Const. art. I, § 8 → `https://www.revisor.mn.gov/constitution/` — expect: "Every person is entitled to a certain remedy in the laws"
- **Evidence (2026-10-16):** WebFetch: Art. I § 8 YES 'Every person is entitled to a certain remedy in the'; last section Art. XIV § 13; not truncated. Script: 79,554 chars, 'Sec. 8. Redress of injuries or wrongs.' found.

### `mn-constitution-justia` — Justia — Minnesota Constitution

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** One page per article (Article1.html … Article14.html).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/minnesota/Article{article_arabic}.html`
  - Placeholders: article in Arabic numerals, capital A (Article1.html).
  - Index: `https://law.justia.com/constitution/minnesota/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: robots.txt returns 403 Cloudflare 'Just a moment...' to the shell
  - WebFetch only.
- **Currency:** none stated
- **Official status:** Index says 'This Constitution may not be the most recent version.'
- **Hazard:** no currency date
- **Hazard:** shell blocked
- **Probe:** Minn. Const. art. I, § 8 → `https://law.justia.com/constitution/minnesota/Article1.html` — expect: "Every person is entitled to a certain remedy in the"
- **Evidence (2026-10-16):** WebFetch: YES 'Every person is entitled to a certain remedy in the'; Article I ends Sec. 17; no currency statement.

## C. Court rules

### `mn-courtrules-revisor` — Minnesota Court Rules (Revisor of Statutes, per rule)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Minnesota Office of the Revisor of Statutes (rules promulgated by the Minnesota Supreme Court) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Civil Procedure (cp), Evidence (ev), Criminal Procedure (cr), General Rules of Practice (gp), Appellate Procedure (ap: subtypes rcap = Civil Appellate Procedure, spec = Special Rules of Practice for the Court of Appeals, flam = family/other), Juvenile (ju), District Court Special Rules (dc), Professional Rules (pr: cond = Rules of Professional Conduct, prof = Lawyers Professional Responsibility, judi, admi, boar …), Record Access (ra), Sentencing Guidelines (sg), Miscellaneous (ms).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.revisor.mn.gov/court_rules/{set}/id/{rule}/  |  https://www.revisor.mn.gov/court_rules/{set}/subtype/{subtype}/id/{rule}/`
  - Placeholders: set/subtype key from citation_map.law_aliases: Minn. R. Civ. P. → cp; Minn. R. Evid. → ev; Minn. R. Crim. P. → cr; Minn. Gen. R. Prac. → gp; Minn. R. Civ. App. P. → ap/subtype/rcap; Minn. R. Prof. Conduct → pr/subtype/cond. {rule} = the whole rule number before the first dot for cp/cr/gp/rcap (12.02(e) → id/12; 15.01 → id/15; 115.03 → id/115; 103.03 → id/103), with the subpart anchored as #12.02; evidence rules are three/four digits (id/702); Professional Conduct uses the dotted number (id/1.7). Alternative per-rule form /court_rules/rule/{set}-{rule}/ (e.g. /court_rules/rule/ev-702/) also serves the text. Table of contents: /court_rules/rule/{set}-toh/ (e.g. ev-toh, cr-toh, gp-toh, aprcap-toh, prcond-toh).
  - Index: `https://www.revisor.mn.gov/court_rules/`
- **Automation:** WebFetch gated · shell ok · robots: revisor.mn.gov: User-agent * — Disallow /alpha/, /beta/, /search/doc_result.php, /bills/status_results.php, /rules/status/result; /statutes, /laws, /rules, /court_rules, /constitution, /state_register allowed
  - Script is the primary route. Per-rule pages are mostly 10-35K chars including comments, but some reach ~75K (cr/id/26); WebFetch read a search-surfaced URL, while built Revisor URLs may hit PROVENANCE_REQUIRED.
- **Currency:** amendment note after each rule (no site-wide date on the per-rule page); full-set PDFs carry 'With amendments effective through …' — observed: "(Amended effective September 1, 2006.) — Minn. R. Evid. 702"
- **Official status:** https://www.revisor.mn.gov/court_rules/info/: 'Rules information on this website is not intended to replace an official source'; the official edition is the printed Minnesota Court Rules volume (Minn. Stat. § 3C.08).
- **Hazard:** online text disclaimed as not official
- **Hazard:** per-rule pages give only the rule's amendment history, not a site currency date — compare the full-set PDF cover date
- **Probe:** Minn. R. Evid. 702 → `https://www.revisor.mn.gov/court_rules/ev/id/702` — expect: "If scientific, technical, or other specialized knowledge will assist the trier"
- **Evidence (2026-10-16):** WebFetch ev/id/702: YES, complete, '(Amended effective September 1, 2006.)'; /court_rules/rule/ev-702/ also YES. Script: cp/id/12 ('Defendant shall serve an answer within 21 days'), cr/id/15 ('Before the judge accepts a guilty plea'), gp/id/115, ap/subtype/rcap/id/103 ('103.03 Appealable Judgments and Orders'), ap/subtype/rcap/id/136 (136.01 subd. 1(c) present), pr/subtype/cond/id/1.7 ('a lawyer shall not represent a client if the representation involves').
- **Notes:** Rule 136.01, subd. 1(c) (nonprecedential opinions citable as persuasive) verified at /court_rules/ap/subtype/rcap/id/136/.

### `mn-courtrules-revisor-pdf` — Minnesota Court Rules — full-set PDFs (Revisor of Statutes)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Minnesota Office of the Revisor of Statutes · text: **fetch-and-quote** · official: unofficial
- **Coverage:** One PDF per rule set: cp 174 pp, ev 70 pp, cr 259 pp, ap 142 pp, gp 341 pp (plus ju, dc, pr, ra, sg, ms).
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.revisor.mn.gov/court_rules/{set}/pdf/`
  - Placeholders: set = cp | ev | cr | ap | gp | ju | dc | pr | ra | sg | ms. Sub-set PDFs: /court_rules/rule/{set}{subtype}-toh/pdf/ (e.g. aprcap-toh, prcond-toh).
  - Index: `https://www.revisor.mn.gov/court_rules/`
- **Automation:** WebFetch ok (truncated) · shell ok · robots: revisor.mn.gov: User-agent * — Disallow /alpha/, /beta/, /search/doc_result.php, /bills/status_results.php, /rules/status/result; /statutes, /laws, /rules, /court_rules, /constitution, /state_register allowed
  - WebFetch of ev/pdf stopped mid-Rule 609 (Rule 1101 NOT PRESENT). Use the per-rule HTML (mn-courtrules-revisor) or the script.
- **Currency:** PDF cover page — observed: "cp: through July 1, 2025; ev: received through July 1, 2019; cr, gp: through July 1, 2026"
- **Official status:** Same disclaimer as mn-courtrules-revisor (court_rules/info).
- **Hazard:** WebFetch truncation (~100K chars)
- **Hazard:** Evidence PDF cover reads 'amendments received through July 1, 2019' — may lag later amendments; check per-rule notes
- **Probe:** Minn. R. Evid. (full set) → `https://www.revisor.mn.gov/court_rules/ev/pdf` — expect: "With amendments received through July 1, 2019"
- **Evidence (2026-10-16):** WebFetch ev/pdf: truncated, last rule seen 609, Rule 1101 NOT PRESENT; 'With amendments received through July 1, 2019'. Script: cp 174 pp/562,992 chars; ev 70 pp/259,893; cr 259 pp/772,403; ap 142 pp/435,502; gp 341 pp/1,192,256.

## D. Administrative code

### `mn-rules-revisor` — Minnesota Rules (Revisor of Statutes)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Minnesota Office of the Revisor of Statutes · text: **fetch-and-quote** · official: official
- **Coverage:** All agency rules by part (NNNN.NNNN); version lists back to ~2014 snapshots; chapter full text.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.revisor.mn.gov/rules/{part}/`
  - Placeholders: part = 4-digit chapter + '.' + 4-digit part, verbatim (7050.0222, 1400.5100). Chapter TOC: /rules/{chapter}/; whole chapter: /rules/{chapter}/full. Versions: /rules/{part}/version/{timestamp} (from version list).
  - Index: `https://www.revisor.mn.gov/rules/`
- **Automation:** WebFetch gated · shell ok · robots: revisor.mn.gov: User-agent * — Disallow /alpha/, /beta/, /search/doc_result.php, /bills/status_results.php, /rules/status/result; /statutes, /laws, /rules, /court_rules, /constitution, /state_register allowed
  - Script is the primary route: WebFetch on built per-part URLs hits PROVENANCE_REQUIRED (independent check on 4410.4300 and 1400.5100); a search-surfaced URL went through. Long parts exceed WebFetch: 7050.0222 page is ~100,210 chars to WebFetch and was cut in subp. 3c item B; use offset=100000 or the script (139,178 chars).
- **Currency:** bottom of each part, after History — observed: "Published Electronically: August 6, 2013 (1400.5100)"
- **Official status:** Footer 'Official Publication of the State of Minnesota'; https://www.revisor.mn.gov/authenticate/ says authenticated PDFs of statutes, laws and administrative rules are official records under UELMA (Minn. Stat. ch. 3E).
- **Hazard:** built URLs may need WebFetch approval; script route is reliable
- **Hazard:** WebFetch truncation on long parts (water-quality tables)
- **Hazard:** 'Published Electronically' is the date that part last changed, not a site-wide currency date
- **Probe:** Minn. R. 1400.5100 → `https://www.revisor.mn.gov/rules/1400.5100/` — expect: ""Administrative law judge" or "judge" means the person or persons assigned"
- **Evidence (2026-10-16):** Script 1400.5100: 8,458 chars, 'Subpart 1. Administrative law judge or judge.'; 'Published Electronically: August 6, 2013'; History '9 SR 2276; 15 SR 1595; 26 SR 391'. 7050.0222: WebFetch YES subp. 1 'The numeric and narrative water quality standards in this part', truncated in subp. 3c.

### `mn-rules-lii` — Cornell LII — Minnesota Administrative Rules

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Minnesota Rules organised by agency; per-part pages.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/minnesota/Minn-R-{chapter}-{part4}`
  - Placeholders: Minn. R. 1400.5100 → Minn-R-1400-5100 (dot → hyphen).
  - Index: `https://www.law.cornell.edu/regulations/minnesota`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay: 10; /regulations allowed
  - Respect the 10-second crawl delay.
- **Currency:** HTTP Last-Modified only — observed: "last-modified Sun, 03 Aug 2025 (1400.5100)"
- **Official status:** Third-party mirror; no currency statement on the index.
- **Hazard:** mirror may lag the Revisor by months (Aug. 2025 snapshot)
- **Probe:** Minn. R. 1400.5100 → `https://www.law.cornell.edu/regulations/minnesota/Minn-R-1400-5100` — expect: ""Administrative law judge" or "judge" means the person or persons assigned"
- **Evidence (2026-10-16):** Script: 4,069 chars, subp. 1 text present, notes '9 SR 2276; 15 SR 1595; 26 SR 391'. Second citation Minn-R-7050-0222: 99,488 chars, heading present. WebFetch of index: agency list ('Agency 101 - Abstracters Board').

## D. Administrative register

### `mn-register-revisor` — Minnesota State Register (Revisor index; issues published by the Department of Administration)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Minnesota Department of Administration (Minnesota's Bookstore); index by the Revisor of Statutes · text: **fetch-and-quote** · official: official
- **Coverage:** Vol. 1 to current (Vol. 51, Jul.-Oct. 2026, nos. 1-15); vols. 1-40 as searchable PDFs with indexes on revisor.mn.gov, vol. 41 onward as per-issue PDFs on mn.gov/admin/assets.
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.revisor.mn.gov/state_register/{volume}/{number}/`
  - Placeholders: volume and issue number unpadded; the revisor URL 302-redirects to the issue PDF on mn.gov (e.g. /state_register/50/1/ → https://mn.gov/admin/assets/SR50_01_tcm36-696254.pdf; the tcm id is not derivable). Volume page /state_register/{volume}/ lists issue number, date and page range — use it to map a 'NN SR PPPP' page cite to an issue. Vols. 1-40: /state_register/{volume}/pdf/ (volume PDF / index).
  - Index: `https://www.revisor.mn.gov/state_register/`
  - Navigation: index → volume page (issue, date, page range) → issue link (redirects to mn.gov PDF) → page
- **Automation:** WebFetch gated · shell ok · robots: revisor.mn.gov: User-agent * — Disallow /alpha/, /beta/, /search/doc_result.php, /bills/status_results.php, /rules/status/result; /statutes, /laws, /rules, /court_rules, /constitution, /state_register allowed | mn.gov: User-agent * — Disallow /cgi-bin, /cgi-sys, /cd_upload/Search, /law-library-stat/archive/, /law-library-stat/briefs/; Visit-time: 0000-1200 (GMT); Request-rate: 10. /web/prod/static/lawlib/ and /admin/assets/ are not disallowed
  - WebFetch read the index page; the built issue URL /state_register/50/1/ hit PROVENANCE_REQUIRED (not retried). Script follows the redirect: 24 pp, 83,257 chars.
- **Currency:** issue masthead — observed: "Monday, July 7, 2025 Volume 50, Number 1 Pages 1 - 24"
- **Official status:** Issue masthead: 'Judicial Notice Shall Be Taken of Material Published in the Minnesota State Register'; 'the official publication of the State of Minnesota's Executive Branch'.
- **Hazard:** cross-host redirect to mn.gov (ShieldSquare bot-check seen elsewhere on mn.gov)
- **Hazard:** page cite → issue requires the volume page hop
- **Hazard:** mn.gov robots.txt asks for Visit-time 0000-1200 GMT
- **Probe:** 50 SR 1 (July 7, 2025) → `https://www.revisor.mn.gov/state_register/50/1/` — expect: "Judicial Notice Shall Be Taken of Material Published in the Minnesota State Register"
- **Evidence (2026-10-16):** Script: redirected to mn.gov/admin/assets/SR50_01_tcm36-696254.pdf, 24 pp; masthead 'Volume 50, Number 1'. WebFetch index: 'Vol. 51 … Jul, 2026 to Oct, 2026'.

## E. Case law

### `mn-opinions-lawlib-archive` — Minnesota State Law Library — appellate opinion archive (static pages, 1996-Feb. 2016)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Minnesota State Law Library · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court opinions and orders (incl. orders on petitions for further review) and Court of Appeals published and unpublished opinions, May 1996 to early 2016 (Supreme Court quarterly index ends Jan.-Mar. 2016, last entry Feb. 3, 2016). The archive home page still says 'May 2, 1996 - March 27, 2013'.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://mn.gov/web/prod/static/lawlib/live/archive/{court}{yy}q{quarter}.html`
  - Placeholders: Quarterly listing pages: court = sct (Supreme Court) | cau (Court of Appeals unpublished/order) | cap? (published, unverified); yy = 2-digit year; quarter 1-4 (sct16q1, sct15q1, cau13q4 verified). PDFs: /archive/supct/{yyyy}/OPA{docket6}-{mmddyy}.pdf (2016 form) or /archive/ctapun/{yymm}/opa{docket6}-{mmddyy}.pdf; docket6 = 2-digit year + 4-digit zero-padded number (A12-1997 → a121997). Take PDF links from the quarterly page; do not build them. Links on the archive home page are relative and resolve wrongly (/archive/sctdate.html on mn.gov root).
  - Index: `https://mn.gov/web/prod/static/lawlib/live/archive/sctdate.html`
  - Navigation: date index (Supreme Court: https://mn.gov/web/prod/static/lawlib/live/archive/sctdate.html; Court of Appeals: https://mn.gov/web/prod/static/lawlib/live/archive/capdate.html) → quarterly page for the decision date (sct{yy}q{n}.html / cau{yy}q{n}.html) → PDF link. Do not start from archive/index.html: its index links point to the wrong root (www.mn.gov/archive/sctdate.html).
- **Automation:** WebFetch ok · shell blocked-challenge · robots: mn.gov: User-agent * — Disallow /cgi-bin, /cgi-sys, /cd_upload/Search, /law-library-stat/archive/, /law-library-stat/briefs/; Visit-time: 0000-1200 (GMT); Request-rate: 10. /web/prod/static/lawlib/ and /admin/assets/ are not disallowed
  - Route legitimacy (independent check 2026-10-17): fetch_doc check says robots.txt permits /web/prod/static/lawlib/live/archive/ and REFUSES /law-library-stat/archive/; the library's own quarterly pages (cau13q4.html, sct15q1.html) link with absolute hrefs to the static path. The same archive is also addressed as /law-library-stat/archive/ (disallowed by robots.txt — never use that path). The /web/prod/static/lawlib/ path is permitted and is the one the archive's own pages link to. The script read the index, sctdate.html and two PDFs, but other requests were redirected to a ShieldSquare CAPTCHA (validate.perfdrive.com) — treat as a bot check; prefer WebFetch.
- **Currency:** archive home page — observed: "Supreme Court opinions and orders (May 2, 1996 - March 27, 2013)"
- **Official status:** Slip opinions as released; no reporter pagination.
- **Hazard:** ShieldSquare CAPTCHA intermittently for the shell (capdate.html redirected to validate.perfdrive.com; never worked around; fetch_doc.py now reports it as REFUSED, exit 3)
- **Hazard:** archive/index.html links to the wrong root (www.mn.gov/archive/…); start from sctdate.html / capdate.html
- **Hazard:** robots-disallowed alias path /law-library-stat/archive/
- **Hazard:** stale coverage statement; ends early 2016
- **Hazard:** slip pagination only
- **Probe:** State v. Bridges, No. A12-1997 (Minn. App. Dec. 30, 2013) → `https://mn.gov/web/prod/static/lawlib/live/archive/ctapun/1312/opa121997-123013.pdf` — expect: "This opinion will be unpublished and may not be cited except as provided by"
- **Evidence (2026-10-16):** WebFetch cau13q4.html: 'October - December 2013 Unpublished and Order Opinions', links to ctapun/1312/…pdf. WebFetch sct16q1.html: latest Feb. 3, 2016. Script PDF: 23 pp, 41,143 chars, caption 'IN COURT OF APPEALS A12-1997'. Script capdate.html: ShieldSquare CAPTCHA.

### `mn-opinions-lawlib-search` — Minnesota State Law Library — opinion archive search (1996-present)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Minnesota State Law Library · text: **link-only** · official: unofficial
- **Coverage:** Per the search page: Supreme Court opinions and orders May 2, 1996 to present; Court of Appeals precedential and nonprecedential opinions May 7, 1996 to present; order opinions Jan. 2, 2025 to present; Special Term orders from Jan. 1, 2023; briefs.
- **Access:** `search-only` · format html
  - Pattern: `https://mn.gov/law-library/search/?v:sources=mn-law-library-opinions`
  - Placeholders: Form fields (labels): Keyword, Sort By, Docket #, Party Names, Citation (reporter N.W./N.W.2d/N.W.3d/Minn. + volume + page), From/To Date, Type of Opinion. A plain GET with &query=A23-1544 returned the empty landing page — the GET parameter names are unknown.
  - Index: `https://mn.gov/law-library/search/?v:sources=mn-law-library-opinions`
- **Automation:** WebFetch fail · shell blocked-challenge · robots: mn.gov: User-agent * — Disallow /cgi-bin, /cgi-sys, /cd_upload/Search, /law-library-stat/archive/, /law-library-stat/briefs/; Visit-time: 0000-1200 (GMT); Request-rate: 10. /web/prod/static/lawlib/ and /admin/assets/ are not disallowed
  - Script: every request redirected to validate.perfdrive.com 'Please validate your request … solve this CAPTCHA'. WebFetch shows the form but no results for the GET query tried.
- **Currency:** search page help text — observed: "Supreme Court opinions and orders from May 2, 1996 to present"
- **Official status:** Slip opinions.
- **Hazard:** ShieldSquare CAPTCHA
- **Hazard:** search requires the form; GET parameters unknown
- **Hazard:** result PDFs may live under the robots-disallowed /law-library-stat/archive/ path (unverified)
- **Probe:** docket A23-1544 → `https://mn.gov/law-library/search/?v:sources=mn-law-library-opinions&query=A23-1544`
- **Evidence (2026-10-16):** Script: CAPTCHA page (193 chars) for every query. WebFetch: landing page with coverage statement; no results.
- **Notes:** The only free official route to 2016-present opinion text, but not machine-usable. Give the user the link for manual search.

### `mn-opinions-mncourts` — Minnesota Judicial Branch — recent appellate opinions (mncourts.gov)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Minnesota Judicial Branch · text: **link-only** · official: unofficial
- **Coverage:** Current release only: Supreme Court (weekly Wednesday release), Court of Appeals precedential / nonprecedential / order opinions (Monday release). No date archive on the listing pages.
- **Access:** `link-only` · format pdf
  - Pattern: `https://mncourts.gov/_media/migration/appellate/{court}/standard-opinions/{release_ddmonyy}/{OP|OR}{docket}-{filed_mmddyy}.pdf`
  - Placeholders: court = court-of-appeals | supreme-court; release folder e.g. 12oct26; docket lower-case or upper-case without hyphen and zero-padded to 4 (A26-0557 → a260557 / A251802); OP = opinion, OR = order. Listing pages: https://mncourts.gov/courtofappeals/recentopinions/{precedential-opinions|nonprecedential-opinions|order-opinions}, https://mncourts.gov/supremecourt/recentopinions/minnesota-supreme-court-opinion. PDFs are robots-disallowed: link only.
  - Index: `https://mncourts.gov/courtofappeals/recentopinions/nonprecedential-opinions`
  - Navigation: listing page (this week's release only) → PDF link (link only; do not fetch)
- **Automation:** WebFetch blocked · shell blocked-challenge · robots: mncourts.gov/robots.txt answers the shell with a Cloudflare challenge (403 'Just a moment...'); WebFetch reports ROBOTS_DISALLOWED for /_media/… opinion PDFs
  - WebFetch reads the listing pages (case name, docket, date, PDF link), but both opinion PDFs tried returned ROBOTS_DISALLOWED. Script: REFUSED (bot check).
- **Currency:** listing heading — observed: "NONPRECEDENTIAL OPINIONS FILED OCTOBER 12, 2026"
- **Official status:** Slip opinions; reported text and pagination are in N.W.2d/N.W.3d (West).
- **Hazard:** PDFs robots-disallowed
- **Hazard:** Cloudflare challenge for the shell
- **Hazard:** listing shows only the latest release
- **Probe:** Villanueva v. GEICO Cas. Co., No. A26-0557 (Minn. App. Oct. 12, 2026) → `https://mncourts.gov/_media/migration/appellate/court-of-appeals/standard-opinions/12oct26/OPa260557-101226.pdf`
- **Evidence (2026-10-16):** WebFetch listing: 9 nonprecedential opinions filed Oct. 12, 2026 with PDF links. WebFetch PDF: ROBOTS_DISALLOWED (also Supreme Court ORA251802-100626.pdf). Script: 'mncourts.gov answers robots.txt with a bot check (challenge)'.
- **Notes:** Use the listing only to learn case name, docket and date; read the text on Justia (mn-cases-justia).

### `mn-cases-justia` — Justia — Minnesota Supreme Court and Court of Appeals

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court and Court of Appeals by year, including nonprecedential opinions (A25-1783, Oct. 5, 2026) through the current month; early years not checked.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/minnesota/{court}/{year}/{docket_lower}.html`
  - Placeholders: court = supreme-court | court-of-appeals; year = decision year; docket lower-case with hyphen and 4-digit zero-padded number (A23-1544 → a23-1544; A25-0354 → a25-0354). Year listing /cases/minnesota/{court}/{year}/ lists all decisions with links when a slug misses.
  - Index: `https://law.justia.com/cases/minnesota/`
  - Navigation: year listing → decision
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: robots.txt returns 403 Cloudflare 'Just a moment...' to the shell
  - WebFetch only.
- **Currency:** none
- **Official status:** Third-party copy of slip opinions; no reporter citation for the case itself.
- **Hazard:** consolidated appeals use only the first docket in the slug (A24-1341/A24-1489 → a24-1341.html)
- **Hazard:** posting lag of about a week behind mncourts.gov releases
- **Hazard:** slip pagination only (bare page numerals in the text, dissents D-1…)
- **Hazard:** no N.W.3d cite for the case itself
- **Hazard:** shell blocked
- **Probe:** Thigpen v. Best Home Care LLC, No. A23-1544 (Minn. Dec. 24, 2025) → `https://law.justia.com/cases/minnesota/supreme-court/2025/a23-1544.html` — expect: "The penalty under Minnesota law for obtaining unemployment benefit overpayments"
- **Evidence (2026-10-16):** WebFetch: YES, syllabus, majority and two dissents, ends at D-1, not truncated; no N.W.3d cite for the case. Second citation court-of-appeals/2026/a25-1783.html: YES 'In this direct appeal from the judgment of conviction for'; nonprecedential notice present. Also court-of-appeals/2024/a23-1544.html (July 29, 2024).
- **Notes:** Primary readable route for opinions after Feb. 2016, because mncourts.gov PDFs are robots-disallowed and the law-library search is CAPTCHA-protected.

## F. Subsequent history

### `mn-pfr-archive-lawlib` — State Law Library archive — Orders on Petitions for Further Review (1996-Feb. 2016)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Minnesota State Law Library · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Weekly PFR lists linked from each Supreme Court quarterly archive page through early 2016.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://mn.gov/web/prod/static/lawlib/live/archive/supct/{yyyy}/pfr{mm}-{dd}-{yyyy}.pdf`
  - Placeholders: Dated by filing date (pfr01-27-2016.pdf); take links from the sct{yy}q{n}.html quarterly page. No docket index: scan the lists for the quarters after the Court of Appeals decision (petitions are due 30 days after the decision; dispositions usually follow within ~60 days).
  - Index: `https://mn.gov/web/prod/static/lawlib/live/archive/sct16q1.html`
  - Navigation: sct{yy}q{n}.html for the months after the decision → 'List of ORDERS ON PETITIONS FOR FURTHER REVIEW' PDFs → grep the docket
- **Automation:** WebFetch ok · shell blocked-challenge · robots: mn.gov: User-agent * — Disallow /cgi-bin, /cgi-sys, /cd_upload/Search, /law-library-stat/archive/, /law-library-stat/briefs/; Visit-time: 0000-1200 (GMT); Request-rate: 10. /web/prod/static/lawlib/ and /admin/assets/ are not disallowed
  - Script read pfr01-27-2016.pdf (1 p) but mn.gov intermittently serves a ShieldSquare CAPTCHA to the shell; WebFetch read the quarterly page.
- **Currency:** none — observed: "Filed – January 27, 2016"
- **Official status:** Archived court lists.
- **Hazard:** no docket index — date scanning required
- **Hazard:** a list can be posted under a later release date (list filed Mar. 17, 2015 sits under the Mar. 25 release): scan both dates
- **Hazard:** ends early 2016
- **Hazard:** CAPTCHA for the shell
- **Probe:** State v. Adams, No. A14-1891, review denied (Minn. Jan. 27, 2016) → `https://mn.gov/web/prod/static/lawlib/live/archive/supct/2016/pfr01-27-2016.pdf` — expect: "State of Minnesota vs. Benjamin Paul Adams – A14-1891 – Denied"
- **Evidence (2026-10-16):** Script: PDF 1 p, 'ORDERS ON PETITIONS FOR FURTHER REVIEW Filed – January 27, 2016'; '…Benjamin Paul Adams – A14-1891 – Denied'. WebFetch sct16q1.html links the PFR lists.

### `mn-pfr-orders-mncourts` — Minnesota Supreme Court — Orders on Petitions for Further Review (current list)

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 1** · Minnesota Judicial Branch · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Only the latest filing date(s): granted, granted/stayed, denied, with case name and Court of Appeals docket (A##-####). No archive on the page.
- **Read via (in order):** **fetch tool**
- **Access:** `link-only` · format html
  - Pattern: `https://mncourts.gov/supremecourt/recentopinions/orders-on-petitions-for-further-review`
  - Placeholders: Single listing page; entries are plain text (no links): 'Party vs. Party – A25-1985' under Granted / Denied headings; petitioner in italics.
  - Index: `https://mncourts.gov/supremecourt/recentopinions/orders-on-petitions-for-further-review`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: Cloudflare challenge to the shell; WebFetch permitted for this page
  - Useful only for decisions of the last week or two.
- **Currency:** page heading — observed: "FILED WEDNESDAY, SEPTEMBER 30, 2026"
- **Official status:** Court web listing; no official-status statement.
- **Hazard:** no history: older dispositions are not on the page
- **Hazard:** page can lag by weeks (still Sept. 30, 2026 on Oct. 17)
- **Hazard:** shell blocked
- **Probe:** Honcik v. American Family Mut. Ins. Co., No. A25-1985 (review granted) → `https://mncourts.gov/supremecourt/recentopinions/orders-on-petitions-for-further-review` — expect: "James W. Honcik vs. American Family Mutual Insurance Company, S.I. – A25-1985"
- **Evidence (2026-10-16):** WebFetch: 'FILED WEDNESDAY, SEPTEMBER 30, 2026'; Granted items 1-5, Denied items 8-38, plus 'Denied – Filed September 25, 2026'; entries are unlinked text with dockets.

### `mn-pmacs` — P-MACS — Minnesota Appellate Courts Case Management System (public)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Minnesota Judicial Branch · text: **link-only** · official: official
- **Coverage:** Appellate dockets including petitions for review and their dispositions.
- **Access:** `link-only` · format html
  - Pattern: `https://macsnc.courts.state.mn.us/ctrack/publicLogin.jsp`
  - Placeholders: Interactive search by case number or party; no deep links known.
  - Index: `https://macsnc.courts.state.mn.us/ctrack/publicLogin.jsp`
- **Automation:** WebFetch gated · shell blocked-challenge · robots: macsnc.courts.state.mn.us: 'User-agent: * Allow: /'
  - Script: 0 chars of text; curl shows a JavaScript bot-defence page (server volt-adc, obfuscated script) instead of the form. WebFetch: PROVENANCE_REQUIRED (not retried).
- **Currency:** n/a
- **Official status:** The courts' own docket system ('public view of the Minnesota Appellate Courts Case Management System').
- **Hazard:** JavaScript bot challenge
- **Hazard:** interactive only
- **Probe:** docket lookup → `https://macsnc.courts.state.mn.us/ctrack/publicLogin.jsp`
- **Evidence (2026-10-16):** Script info: kind=html chars=0; page body is a JS challenge (volt-adc).
- **Notes:** Give the user this link for review dispositions after Feb. 2016 that are not on the current PFR list.

### `mn-subsequent-justia` — Justia — Supreme Court decision on review, found by the Court of Appeals docket

- **Status:** VERIFIED 2026-10-16 (research) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court decisions after a grant of review (not denials).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/minnesota/supreme-court/{year}/{docket_lower}.html`
  - Placeholders: The Supreme Court keeps the Court of Appeals docket number on review, so the COA docket is the slug; year = Supreme Court decision year (try the 1-2 years after the COA decision, or the year listing).
  - Index: `https://law.justia.com/cases/minnesota/supreme-court/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: robots.txt returns 403 Cloudflare 'Just a moment...' to the shell
  - WebFetch only.
- **Currency:** none
- **Official status:** Third-party copy.
- **Hazard:** denials of review are not on Justia
- **Hazard:** year must be guessed or found in the listing
- **Probe:** Thigpen v. Best Home Care LLC, No. A23-1544 (Minn. App. July 29, 2024), rev'd (Minn. Dec. 24, 2025) → `https://law.justia.com/cases/minnesota/supreme-court/2025/a23-1544.html` — expect: "Appellant Christopher Thigpen received unemployment benefits from the Department of"
- **Evidence (2026-10-16):** WebFetch: COA /court-of-appeals/2024/a23-1544.html (July 29, 2024, nonprecedential) and Supreme Court /supreme-court/2025/a23-1544.html (Dec. 24, 2025) both exist under the same docket.

## Not available (do not look for these again)

- **case_law** — Public-domain (vendor-neutral) citation format: Minnesota cites N.W.2d/N.W.3d; Minn. R. Civ. App. P. 136.01 and Justia pages show no neutral citation. (2026-10-16)
- **case_law** — Free official reporter (N.W.3d) pagination: Justia and archive PDFs carry slip pagination only; Thigpen (A23-1544) page has no N.W.3d cite. (2026-10-16)
- **case_law** — Machine-readable opinions on mncourts.gov: WebFetch ROBOTS_DISALLOWED on /_media/… opinion PDFs; script REFUSED (Cloudflare challenge). (2026-10-16)
- **statutes** — Official bulk download / API for Minnesota Statutes: /downloads/ 404, /data/ 502; web search found none. (2026-10-16)
- **court_rules** — Tier-2 copy of Minnesota court rules on Justia / LII / public.law: Not found in this run (not probed beyond search); Revisor per-rule pages make it unnecessary. (2026-10-16)

## Corpus candidates (maintainers)

- `mn-courtrules-revisor-pdf` — WebFetch stops mid-Rule 609 of 1101; 70 pp.
- `mn-courtrules-revisor-pdf` — 174 pp, 562,992 chars — far beyond WebFetch's window.
- `mn-courtrules-revisor-pdf` — 259 pp, 772,403 chars.
- `mn-courtrules-revisor-pdf` — 142 pp, 435,502 chars.
- `mn-courtrules-revisor-pdf` — 341 pp, 1,192,256 chars.

## Open questions

- GET parameter names for the State Law Library opinion search (mn.gov/law-library/search) — and whether its result PDFs sit under the robots-disallowed /law-library-stat/archive/ path.
- Whether mncourts.gov has any dated archive of past releases (only the current week was found).
- Court of Appeals published-opinion quarterly page name in the static archive (cap{yy}q{n}.html assumed, unverified).
- Session-law WebFetch behaviour not tested (pages are multi-megabyte; script verified).
- Whether the Revisor flags 2026 amendments on 2025-edition section pages beyond 'Recent History'.
- CourtListener ids minn / minnctapp unverified; Minnesota Tax Court and Workers' Compensation Court of Appeals not covered.
- Minn. R. Evid. full-set PDF cover says 'received through July 1, 2019' — confirm whether later amendments exist.
