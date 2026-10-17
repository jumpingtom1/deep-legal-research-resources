# Virginia (va) probe log — 2026-10-16

Tools: WF = WebFetch; FD = `python3 scripts/fetch_doc.py --research` (info/read/grep); LN = a scratchpad helper that calls `lsnet.get(..., allow_unlisted=True)`, which applies the same robots, challenge and rate-limit rules, to list the hrefs on a page; WS = WebSearch (discovery only). All entries are dated 2026-10-16. About 26 WebFetch calls were used.

## A. Statutes

| URL | Tool | Result |
|---|---|---|
| https://law.lis.virginia.gov/vacode/title8.01/chapter4/section8.01-243/ | FD info/read | 200 html 8,729 chars; body "A. Unless otherwise provided in this section or by other statute" |
| https://law.lis.virginia.gov/vacode/title18.2/chapter4/section18.2-32/ | FD | 200, 5,013 chars; body "Murder, other than aggravated murder, by poison, lying in wait" |
| https://law.lis.virginia.gov/robots.txt | FD | HTTP 404 (no robots) |
| https://law.lis.virginia.gov/vacode/8.01-243/ | FD | 200, 8,142 chars, body present (short form works) |
| https://law.lis.virginia.gov/vacode/title8.01/section8.01-243/ | FD | 200, body present |
| https://law.lis.virginia.gov/vacode/title8.01/chapter9/section8.01-243/ | FD | 200, § 8.01-243 served (wrong chapter segment is ignored) |
| https://law.lis.virginia.gov/vacode/title8.01/chapter4/ | FD | chapter TOC; "Article 3. Personal Actions Generally … § 8.01-243" |
| https://law.lis.virginia.gov/vacode/title8.01/ | FD | title TOC with ranges "[§§ 8.01-228 through 8.01-256]" |
| https://law.lis.virginia.gov/vacode/8.01-243/ | WF (built) | PROVENANCE_REQUIRED — permission not answered (gated) |
| https://law.lis.virginia.gov/vacode/title18.2/chapter4/section18.2-32/ | WF (built) | PROVENANCE_REQUIRED (gated) |
| WS "law.lis.virginia.gov vacode 8.01-243 …" | WS | returned /vacode/8.01-243/ and variants |
| https://law.lis.virginia.gov/vacode/8.01-243/ | WF (search-sourced) | YES; "Unless otherwise provided in this section or by other statute, every action"; no currency line; complete |
| https://law.lis.virginia.gov/vacode/18.2-67.2:1/ | WF | "§ 18.2-67.2:1. Repealed." — colon URL works; repealed stub |
| https://law.lis.virginia.gov/vacode/title18.2/chapter4/section18.2-62/ | WF | "§ 18.2-62. Repealed." stub |
| https://law.lis.virginia.gov/vacode/19.2-8 | WF | YES; "A prosecution for a misdemeanor, or any pecuniary fine, forfeiture,"; complete |
| https://law.lis.virginia.gov/vacode/ | FD grep | no currency string; "2026 Updates" link → /vacodeupdates/ |
| https://law.lis.virginia.gov/vacodeupdates/ | FD | "list of updated sections that took effect on July 1, 2026" |
| https://law.lis.virginia.gov/ , /developers/ , /law-library/ | FD + LN | "available via a web service"; law library links /library/cov/Title{t}.pdf and /CSV/CoVTitle_{t}.csv |
| https://law.lis.virginia.gov/jsonapi/ | FD + LN | lists /api/CoV…, /api/Constitution…, /api/AdministrativeCode… GET services |
| https://law.lis.virginia.gov/library/cov/Title8.01.pdf | FD info | pdf 484 pp, 1,330,735 chars, Last-Modified 15 Aug 2025 |
| https://law.lis.virginia.gov/CSV/CoVTitle_8.01.csv | FD | 1,420,185 chars; header "TitleNum,TitleName,…,Section,Title,Body"; Last-Modified 13 Aug 2025 |
| https://law.lis.virginia.gov/api/CoVSectionsGetSectionDetailsJson/8.01-243 | FD | 200 JSON (redirect adds "/"); "ChapterNum":"4"; Body "A. Unless otherwise provided…" |
| https://law.lis.virginia.gov/vacodepopularnames/ | FD grep | no "Electronic Legal Material" (no UELMA entry found) |
| WS Justia 8.01-243 | WS | returned law.justia.com/codes/virginia/title-8-01/chapter-4/section-8-01-243/ |
| https://law.justia.com/codes/virginia/title-8-01/chapter-4/section-8-01-243/ | WF | YES; "2025 Code of Virginia"; "VA Code § 8.01-243 (2025)"; no section ranges in navigation |
| same | FD info | REFUSED: law.justia.com refused automated access earlier (robots/challenge) |
| https://law.justia.com/codes/virginia/title-1/chapter-2-1/section-1-219-1/ | WF | YES; "A. The right to private property being a fundamental right,"; 2025 edition |
| https://www.public.law/ | FD grep "Virginia" | 0 matches |
| https://virginia.public.law/ | FD | robots unreachable (proxy 502); not retried |
| https://www.law.cornell.edu/states/virginia | FD + LN | links out to law.lis.virginia.gov and courts.state.va.us; LII hosts only the VAC |

## B. Constitution

| URL | Tool | Result |
|---|---|---|
| https://law.lis.virginia.gov/constitution/article1/section11/ | FD | 5,402 chars; "That no person shall be deprived of his life, liberty, or property" |
| https://law.lis.virginia.gov/constitution/article6/section1/ | FD | "The judicial power of the Commonwealth shall be vested in a Supreme Court" |
| https://law.lis.virginia.gov/constitution/ | FD | TOC |
| https://law.lis.virginia.gov/constitution/article1/ | WF | TOC-ONLY; date "10/8/2026" (render) |
| https://law.lis.virginia.gov/constitutionfull | WF | 144,846 chars; truncated at Art. VII § 9 "No rights of a city or town in and to" |
| https://law.lis.virginia.gov/constitution/article1/section14/ | WF | YES; "That the people have a right to uniform government; and," |
| https://law.lis.virginia.gov/constitution.pdf | FD | 58 pp; "Amended November 5, 2024 – effective January 1, 2025"; LM 6 May 2025 |
| https://law.lis.virginia.gov/api/ConstitutionSectionDetailsJson/1/11 | FD | JSON Body "That no person shall be deprived…" |
| https://law.justia.com/constitution/virginia/constitution.html | WF | Art. I § 11 and VI § 1 present; 138,774 chars; truncated at Art. VIII § 5(c) |

## C. Court rules

| URL | Tool | Result |
|---|---|---|
| https://vacourts.gov/opinions/home → link /static/courts/scv/rulesofcourt.pdf | LN | link found |
| https://www.vacourts.gov/static/courts/scv/rulesofcourt.pdf | FD info/grep | pdf 631 pp, 1,118,593 chars, LM 15 Sep 2026; "Rule 3:20. Motion for Summary Judgment." p. 203; "Rule 5:17. Petition for Appeal." p. 402; "Rule 2:702 TESTIMONY BY EXPERTS" p. 142; 5:1(f)/5A:1(f) "Citing Unpublished Judicial Dispositions" |
| same (plain URL) | WF | PROVENANCE_REQUIRED (gated) |
| https://www.vacourts.gov/static/courts/scv/rulesofcourt.pdf?r=seo (search-sourced) | WF | Rule 1:1(a) present; 3:20 NOT PRESENT; 5:17 NOT PRESENT; stops in Rule 1A:1; "Last amended by Order dated July 17, 2026; effective September 15, 2026." |
| https://vacourts.gov/courts/scv/rules | FD + LN | "Rules of Supreme Court of Virginia as currently effective"; amendment links |

## D. Administrative Code and Register

| URL | Tool | Result |
|---|---|---|
| https://law.lis.virginia.gov/admincode/title9/agency20/chapter60/section10/ | FD | "9VAC20-60-10. (Repealed.)" stub |
| https://law.lis.virginia.gov/admincode/title12/agency5/chapter585/section10/ | FD | repealed stub |
| https://law.lis.virginia.gov/admincode/title9/agency20/chapter60/ | FD | chapter TOC by section number |
| https://law.lis.virginia.gov/api/AdministrativeCodeGetSectionDetailsJson/9/20/60/10/0/0 | FD | JSON, SectionTitle "[Repealed]" |
| https://law.lis.virginia.gov/admincode/title9/agency20/chapter60/section12/ | FD | body "A. Chapter 11.1 (§ 10.1-1182 et seq.) and Chapter 14" |
| https://law.lis.virginia.gov/admincode/title12/agency5/chapter371/section10/ | FD | 17,049 chars; "The following words and terms when used in this chapter" |
| https://law.lis.virginia.gov/admincode/ | FD | "provided online by the Virginia General Assembly" "as a service to the public" |
| https://law.lis.virginia.gov/admincode/title12/agency5/chapter371/section10/ | WF (search-sourced) | YES; last note "Volume 42, Issue 23, eff. August 13, 2026." |
| https://register.dls.virginia.gov/details.aspx?id=8079 | WF | Vol. 36 Iss. 23, July 6, 2020; 12VAC5-371 final; text present; R20-6336 |
| https://register.dls.virginia.gov/robots.txt | FD | 404 |
| https://register.dls.virginia.gov/ | LN | current issue PDF /vol43/iss04/v43i04.pdf; archive.aspx |
| https://register.dls.virginia.gov/vol43/iss04/v43i04.pdf | FD | 98 pp; "VOL. 43 ISS. 4 … October 5, 2026" |
| https://register.dls.virginia.gov/vol36/iss23/v36i23.pdf | FD | 108 pp; 12VAC5-371-10 on p. 59 (columns interleaved) |
| https://register.dls.virginia.gov/issue.aspx?voliss=36:23 | FD | shell page only, no TOC |
| https://register.dls.virginia.gov/archive.aspx | LN | 472 toc.aspx?voliss links, 43:04 back to 25:01 (Sep 15, 2008) |
| https://register.dls.virginia.gov/toc.aspx?voliss=36:23 | FD + LN | lists "12VAC5-371 … (Final Regulation)"; details.aspx?id= links |
| https://www.law.cornell.edu/regulations/virginia/12VAC5-371-10 | FD | 14,923 chars; body present; notes end "Volume 38, Issue 04, eff. 11/11/2021"; "updated quarterly"; LM 7 Aug 2025 |
| https://www.law.cornell.edu/regulations/virginia/9VAC20-60-12 | FD | body present |

## E. Case law

| URL | Tool | Result |
|---|---|---|
| https://www.vacourts.gov/robots.txt | FD | Drupal default; disallows /core/, /profiles/, /admin/, /search/, /user/… |
| https://vacourts.gov/opinions/home | FD + LN | links /scndex "By Date Issued (since 6/9/95)", /wpcap, /wpcau; "Published Opinions (5/2/95 – present)"; "Unpublished Opinions (3/5/02 – present)" |
| https://vacourts.gov/scndex | FD | → webdev.vacourts.gov/dynamic/scndex.htm, 2,020,002 chars, 3,051 PDF links (opinions/opnscvwp/1NNNNNN.pdf; 19 suffixed) |
| https://vacourts.gov/wpcap | FD | → …/wpcap.htm, 1,060,054 chars, 4,148 links |
| https://vacourts.gov/wpcau | FD | → …/wpcau.htm, 3,371,748 chars, 13,542 links |
| https://www.vacourts.gov/opinions/opnscvwp/1241067.pdf | FD | → /static/…; order, "Record No. 241067 Court of Appeals No. 1741-23-3" |
| https://www.vacourts.gov/opinions/opnscvwp/1250701.pdf | FD | 14 pp; "Record No. 250701 … OPINION BY JUSTICE D. ARTHUR KELSEY" |
| https://www.vacourts.gov/opinions/opncavwp/0476251.pdf | FD | 48 pp, 105,801 chars; "Record No. 0476-25-1"; "PUBLISHED OPINION BY" |
| https://www.vacourts.gov/opinions/opncavwp/0139251.pdf | FD | 15 pp; "MEMORANDUM OPINION BY JUDGE KEVIN M. DUFFAN" |
| https://vacourts.gov/opinions/opnscvwp/1240138.pdf | WF (search-sourced) | order, Record No. 240138, Nov. 21, 2024, complete, no own reporter cite |
| https://www.vacourts.gov/opinions/opnscvwp/1151296.pdf | WF | order, Record No. 151296, June 2, 2016, complete |
| https://www.courts.state.va.us/opinions/opncavwp/0956112.pdf | WF | WRONG DOCUMENT: a "Cases Appealed to Supreme Court" list, not Taylor opinion |
| same + https://www.vacourts.gov/opinions/opncavwp/0956112.pdf | FD | 5 pp, LM 8 Jan 2013, list text; wpcap lists 0956112 as "Franklin Taylor … 10/23/2012" |
| https://vacourts.gov/courts/scv/home | LN | links Unpublished Orders, eapps acms-public, cav-public |
| https://vacourts.gov/courts/scv/orders_unpublished/home | FD + LN | "Unpublished orders for cases that were argued before the full court"; years 2026 → 2014 |
| https://vacourts.gov/static/courts/scv/orders_unpublished/250511.pdf | FD | 15 pp; "Record No. 250511 Court of Appeals No. 1973-23-4" |
| WS Justia VA cases | WS | supreme-court/2025/240683.html; court-of-appeals-published/2026/8888-88-1-4.html |
| https://law.justia.com/cases/virginia/supreme-court/2025/240683.html | WF | full body; Record No. 240683; May 29, 2025 |
| https://law.justia.com/cases/virginia/court-of-appeals-published/2025/ | WF | links shown as /court-of-appeals-unpublished/2025/0003-25-4.html …; "Opinions 1 - 500 of 777" |
| https://law.justia.com/cases/virginia/court-of-appeals-published/ | WF | years 1985–2026 |
| https://law.justia.com/cases/virginia/supreme-court/2025/ | WF | /supreme-court/2025/241092.html etc. |
| https://law.justia.com/cases/virginia/court-of-appeals-unpublished/2025/0003-25-4.html | WF | full memorandum opinion, Bailey v. Bailey, complete |

## F. Subsequent history

| URL | Tool | Result |
|---|---|---|
| https://www.vacourts.gov/opinions/opncavwp/8888881.pdf | FD | 2 pp; "DATE: October 6, 2026"; Kuykendall 0577-24-3 → "(250701)"; "Refused (251005)" |
| https://vacourts.gov/wpcap grep 8888881 | FD | "8888881 Cases Appealed to Supreme Court of Virginia 10/06/2026" |
| https://eapps.courts.state.va.us/acms-public | FD | FETCH ERROR HTTP 500 |
| https://eapps.courts.state.va.us/cav-public | FD | HTTP 500 |
| https://eapps.courts.state.va.us/robots.txt | FD | lands on /unavailable/unauthorized.html "Unauthorized Access." |
| https://eapps.courts.state.va.us/acms-public | WF | PROVENANCE_REQUIRED (gated); not retried |

## G. Citation map

The regex was checked locally against every example (all match). `python3 scripts/build.py --check` printed no ERROR or WARN lines.
