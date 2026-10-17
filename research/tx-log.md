# Texas (tx) probe log — 2026-10-16

All probes on 2026-10-16 by `research`. "WF" = WebFetch; "script" = `python3 scripts/fetch_doc.py --research …`; "curl" = plain GET from this workspace through the agent proxy (robots files, headers, JS bundles, index pages on hosts with no refusal). Quoted text ≤ 15 words. WebFetch calls used: 36 of ~55. No WebFetch failure for quota/rate reasons.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://statutes.capitol.texas.gov/robots.txt | script, curl | 200 text/html — the Angular app shell ("Texas Constitution and Statutes"), no robots file |
| https://tcss.legis.texas.gov/robots.txt | curl | 404 |
| https://search.txcourts.gov/robots.txt | curl | 200: `User-Agent: *` / `Disallow: /` |
| https://www.txcourts.gov/robots.txt (= txcourts.gov) | curl | 200: `*` disallows /umbraco/, /data/, /scripts/ etc. and ~6 named /media PDFs; `# Crawl-delay: 720` commented out; Scooter disallowed |
| https://texas.public.law/robots.txt | curl | 200: `*` disallows /admin, /api, /data, /demo, /images, /users |
| https://texreg.sos.state.tx.us/robots.txt | curl | 200: no `*` group; Disallow / for FacebookExternalHit, bingbot, GPTBot, ChatGPT-User, OAI-SearchBot, Googlebot, AhrefsBot, meta-externalagent, DataForSeoBot |
| https://www.sos.state.tx.us/robots.txt | curl | 200, empty |
| https://texas-sos.appianportalsgov.com/robots.txt | curl | 404 HTML page |
| https://lrl.texas.gov/robots.txt | curl | 200: Disallow / for anthropic-ai, Claude-Web, ClaudeBot (and GPTBot, CCBot, PerplexityBot, …); `*` disallows /lrlstaff, /cfide → treated as BLOCKED |
| https://capitol.texas.gov/robots.txt | curl | 200: `*` disallows only system paths (/_vti_*, /aspnet_client, …) |
| law.justia.com (any URL) | script | REFUSED: "law.justia.com refused automated access earlier (robots.txt challenge)" |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://statutes.capitol.texas.gov/Docs/CP/htm/CP.16.htm | script | 200, 1,402 chars, same sha256 as /robots.txt and /Docs/PE/htm/PE.19.htm — app shell (code list only) |
| https://statutes.capitol.texas.gov/Docs/CP/htm/CP.16.htm#16.003 | WF | NOT PRESENT — "only navigation and an app shell" |
| https://statutes.capitol.texas.gov/ + main-6BSFENBJ.js, polyfills, chunk-*.js | curl | JS config: `FileServerPath:"https://tcss.legis.texas.gov/resources"`, `TCASCore:"https://tcss.legis.texas.gov/api/"`; doc path `/${code}/htm/${chapter}.htm#${sec}`; CN section path `/CN/htm/CN.1/CN.1.19.htm` |
| https://statutes.capitol.texas.gov/assets/StatuteCodes.json, QuickCodes.json, StatuteCodeDownloads.json, StatuteCodeTree.json | curl | 200 JSON: code keys (CN, AG, AL, WL, BC, BO, CP, CR, ED, EL, ES, FA, FI, GV, HS, HR, IN, I1, LA, LG, NR, OC, PW, PE, PR, SD, TX, TN, UT, WA, CV); download paths /Zips/{CODE}.htm.zip, /SDocs/{NAME}.pdf |
| https://tcss.legis.texas.gov/api/GetProperty/StatutesCurrentMsg | curl | 200: "current through the 89th 2nd Called Legislative Session, 2025"; constitution "through the amendments approved by voters in November 2025" |
| https://tcss.legis.texas.gov/api/GetProperty/StatutesByDateSessionInfo | curl | 200: "Statutes are available from 2004 through the 89th 2nd Called Legislative Session, 2025" |
| https://tcss.legis.texas.gov/api/StatuteTree/GetStatuteTree/6/0 (and /6/1, /CP/0) | curl | 404 JSON (parameters unknown) |
| https://tcss.legis.texas.gov/resources/CP/htm/CP.16.htm | script | 200 html 55,505 chars, last-modified 9 Apr 2026; grep "Sec. 16.003." found; verify OK; anchors `<a name="16.003">` |
| same | WF | YES "Except as provided by Sections 16.010, 16.0031, and 16.0045, a"; no currency; last section 16.073 |
| https://tcss.legis.texas.gov/resources/PE/htm/PE.19.htm | script | 200, 8,861 chars; grep "Sec. 19.02." found; verify OK |
| same | WF | YES (b) "A person commits an offense if the person: (1) intentionally"; ends § 19.06 |
| https://tcss.legis.texas.gov/resources/CP/pdf/CP.16.pdf | script | 200 PDF, 30 pp, 66,241 chars |
| https://tcss.legis.texas.gov/resources/CR/htm/CR.38.htm | script | 154,645 chars; grep "Art. 38.23." found ("EVIDENCE NOT TO BE USED") |
| …/GV/htm/GV.552.htm | script | 346,626 chars; grep § 552.325 found at offset 321,421 |
| same | WF | § 552.325 NOT PRESENT; last § 552.113; "[Content truncated due to length...]"; tool says text 103,481 chars |
| same, offset=100000 | WF | NOT PRESENT; fragment only (cross-refs 552.021…552.110) |
| …/FA/htm/FA.261.htm, TX/htm/TX.151.htm, HS/htm/HS.481.htm | script | 161,619 / 433,914 / 295,160 chars |
| …/GV/htm/GV.2001.htm, CR/htm/CR.2A.htm, BC/htm/BC.2.htm, FA/htm/FA.153.htm | curl | 200 (176,648 / 156,151 / 172,328 / 215,405 bytes) |
| …/CP/htm/CP.16/CP.16.003.htm, …/CP/htm/CP.16/16.003.htm, …/CP/htm/CP.16.003.htm, …/PE/htm/PE.19/PE.19.02.htm | script/curl | 404 — no per-section statute files |
| https://tcss.legis.texas.gov/resources/Zips/CP.htm.zip | curl -I | 200 application/x-zip-compressed, 655,256 bytes, last-modified 14 May 2026 |
| https://tcss.legis.texas.gov/resources/SDocs/CIVILPRACTICEANDREMEDIESCODE.pdf | curl -I | 200 application/pdf, 1,838,678 bytes |
| https://tcss.legis.texas.gov/Zips/CP.htm.zip | curl -I | 404 (needs /resources prefix) |
| https://texas.public.law/statutes/tex._civ._practice_and_remedies_code_section_16.003 | WF | YES "Except as provided by Sections 16.010 (Misappropriation of Trade Secrets)"; "Up to date", "Verified: May 26, 2025"; "Trust but verify." |
| same | script | 200, 5,173 chars, last-modified 11 May 2025; "Verified: May 26, 2025" |
| https://texas.public.law/statutes | script | "Texas Statutes Updated May 26, 2025" (unchanged — stale) |
| https://texas.public.law/statutes/tex._penal_code_section_19.02 | script | 200; "(b) A person commits an offense if the person" |
| https://law.justia.com/codes/texas/civil-practice-and-remedies-code/title-2/subtitle-b/chapter-16/subchapter-a/section-16-003/ | WF | YES; "2025 Texas Statutes"; "TX Civ Prac & Rem Code § 16.003 (2025)" |
| https://law.justia.com/codes/texas/penal-code/title-5/chapter-19/section-19-02/ | WF | YES; "2025 Texas Statutes"; also 2024, 2023 editions |
| https://law.justia.com/codes/texas/penal-code/title-5/chapter-19/section-19-02/ | script | REFUSED (challenge) |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| https://tcss.legis.texas.gov/resources/CN/htm/CN.1.htm | script | 28,718 chars; anchors name="1.1"; § 19 found |
| same | WF | YES "No citizen of this State shall be deprived of life"; through Sec. 37, not truncated |
| https://tcss.legis.texas.gov/resources/CN/htm/CN.1/CN.1.19.htm | script/curl | 200, 339 chars: art. 1 § 19 only |
| https://tcss.legis.texas.gov/resources/CN/htm/CN.5.htm | script | Sec. 1 "The judicial power of this State shall be vested in one Supreme Court" |
| https://tcss.legis.texas.gov/resources/CN/htm/CN.5/CN.5.1.htm | script | 200, 715 chars |
| https://law.justia.com/constitution/texas/ | WF | per-article links only; Art. 1 → /constitution/texas/articles/cn000100.html; "This Constitution may not be the most recent version." |
| https://law.justia.com/constitution/texas/articles/cn000100.html | WF | § 19 body NOT PRESENT (title only); section list ends Sec. 32 |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.txcourts.gov/rules-forms/rules-standards/ | curl | 200; "most current version approved by the Supreme Court of Texas"; Last Amended: TRCP Oct. 1, 2026; TRAP Feb. 6, 2026; TRE July 2, 2026; TRJA July 1, 2026; TDRPC Mar. 7, 2025; links /media/{id}/… |
| https://www.txcourts.gov/media/1463426/texas-rules-of-civil-procedure.pdf | script | PDF 369 pp, 998,155 chars; "RULE 91a." body p. 69; verify Rule 13 OK |
| same | WF | Rule 13 YES "The signatures of attorneys or parties constitute a certificate by"; Rule 91a.1 NOT PRESENT; truncated in Rule 21(f)(7) |
| https://www.txcourts.gov/media/1463134/texas-rules-of-appellate-procedure-02062026.pdf | script | 147 pp, 641,559 chars; two-column interleaving at 47.7; "Updated with Amendments Effective February 6, 2026"; verify 9.4 OK (reading-order) |
| same | WF | Rule 9.4 YES "Except for the record, a document filed with an appellate court, including"; 47.7 NOT PRESENT; truncated at 14.3 |
| https://www.txcourts.gov/media/1463074/texas-rules-of-evidence-updated-with-amendments-effective-07022026.pdf | script | 62 pp, 144,658 chars; "Rule 702. Testimony by Expert Witnesses" p. 44; verify 401 OK |
| same | WF | 401 YES; 702 YES "A witness who is qualified as an expert by knowledge,"; truncated mid-803(10); cover "Effective July 2, 2026" |
| https://www.txcourts.gov/media/1459244/texas-disciplinary-rules-of-professional-conduct-pdf.pdf | script | 118 pp, 370,680 chars; "(Effective March 7, 2025)"; Rule 1.06 p. 28; verify OK |

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://texreg.sos.state.tx.us/public/readtac$ext.TacPage?sl=R&app=9&p_dir=&p_rloc=&p_tloc=&p_ploc=&pg=1&p_tac=&ti=16&pt=1&ch=3&rl=1 | script, curl | 200, 204 chars "This Site Has Moved" → https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=LANDING_PAGE |
| https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=LANDING_PAGE | script | 200, 0 chars of text |
| same | WF | "no readable body content"; title "Rules & Meetings" — JS shell |
| WebSearch "texas-sos.appianportalsgov.com rules-and-meetings VIEW_TAC …" | search | SOS guide view-search-TAC.pdf |
| https://www.sos.texas.gov/texreg/guides/view-search-TAC.pdf | script | 2 pp; navigation by drop-downs; "Last Revised: December 2024" |
| https://www.law.cornell.edu/regulations/texas/16-Tex-Admin-Code-SS-3-1 | script | 200, 18,286 chars, last-modified 7 Aug 2025; verify "Filing requirements." OK |
| same | WF | YES "Filing requirements. (1) Except as provided under subsection (e) of"; "State regulations are updated quarterly; we currently have two versions available."; "50 TexReg 0835, eff. 2/18/2025" |
| https://www.sos.state.tx.us/texreg/index.shtml | curl | links: current issue HTML/PDF, /texreg/pdf/backview/index.shtml, /texreg/archive/index.shtml, Appian search |
| https://www.sos.state.tx.us/texreg/pdf/currview/index.shtml | curl | /texreg/pdf/backview/1016/1016is.pdf, 1016con.pdf, 1016prop.pdf … |
| https://www.sos.state.tx.us/texreg/pdf/backview/index.shtml | curl | issues Oct. 9, 2026 "Pages 6983-7090" back to Nov. 7, 2025 |
| https://www.sos.state.tx.us/texreg/pdf/backview/1016/1016is.pdf | script | 112 pp, 734,516 chars; "Volume 51 Number 42 October 16, 2026 Pages 7091 - 7200" |
| same | WF | cover line matches; truncated after 51 TexReg 7113 |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://search.txcourts.gov/CaseSearch.aspx?coa=cossup | script | REFUSED: "robots.txt on search.txcourts.gov disallows … (rule: Disallow: /)". Not fetched by any other tool. |
| https://www.txcourts.gov/supreme/orders-opinions/ | script, curl | 200; year links 2014-2026 only |
| https://www.txcourts.gov/supreme/orders-opinions/2026/ | script, curl | day links Jan. 5 … Oct. 16, 2026 |
| …/2000/, /2004/, /2005/, /2008/, /2010/, /2012/, /2013/ | curl | 404 |
| …/2014/ | curl | 21 day links, Oct.-Dec. 2014 |
| …/2015/june/june-5,12,19,26-2015/, 2018 & 2021 June pages | curl | opinions on /media/: e.g. /media/996482/130047.pdf, /media/1008502/12-0657c1.pdf, /media/1441776/160505.pdf |
| https://www.txcourts.gov/supreme/orders-opinions/2026/may/may-29-2026/ | curl | opinion PDFs 240205.pdf, 240205c.pdf, 240286.pdf/c/d, 241057.pdf; "View Electronic Briefs" → search.txcourts.gov; print PDF supreme-court-of-texas-orders-05-29-2026.pdf |
| https://www.txcourts.gov/media/1462796/240205.pdf | script | PDF 15 pp, 24,992 chars; "JUSTICE LEHRMANN delivered the opinion of the Court."; verify OK |
| same | WF | YES; slip pagination; no S.W.3d cite for itself; not truncated |
| https://www.txcourts.gov/14thcoa/, /15thcoa/, /cca/ | curl | "Released Orders & Opinions"/"Hand Downs" link only to search.txcourts.gov |
| https://www.txcourts.gov/businesscourt/ | curl | link /businesscourt/opinions/ |
| https://www.txcourts.gov/businesscourt/opinions/ | curl | 141 /media links; cites 2026 Tex. Bus. 73 … 2024 Tex. Bus. 1 |
| same | WF | first entries "FSTI v. PVS Minibulk, 2026 Tex. Bus. 73 (3d Div.)", "Crain v. Northern, 2026 Tex. Bus. 72"; "prefers citations to paragraph numbers"; truncated at 2025 Tex. Bus. 23 |
| https://www.txcourts.gov/media/1463443/25-bc08a-0014-crain-v-northern-26-tex-bus-72.pdf | script | 19 pp, 35,257 chars; "2026 Tex. Bus. 72", "Cause No. 25-BC08A-0014", "¶1" |
| https://law.justia.com/cases/texas/ | WF | 18 courts incl. fifteenth-court-of-appeals, special-court-of-review; no Business Court |
| https://law.justia.com/cases/texas/fifth-court-of-appeals/2024/05-23-00190-cv.html | WF | YES; Aug. 21, 2024; "This appeal arises from a dispute between homeowners regarding whether"; complete |
| https://law.justia.com/cases/texas/supreme-court/2026/24-0205.html | WF | YES; May 29, 2026; concurrence text not on page |
| https://law.justia.com/cases/texas/court-of-criminal-appeals/2026/ | WF | slugs ap-77-122, pd-0643-25(-0,-1), wr-97-760-01 |
| https://law.justia.com/cases/texas/court-of-criminal-appeals/2026/ap-77-122.html | WF | YES; Oct. 8, 2026; "Do Not Publish"; complete |
| https://law.justia.com/cases/texas/fifteenth-court-of-appeals/2025/ | WF | 15-24-00132-cv.html …; 15-25-00116-cv-0.html (concurrence); earliest Jan. 14, 2025 |
| https://law.justia.com/cases/texas/fourteenth-court-of-appeals/ | WF | years 1985-2026 |
| https://law.justia.com/cases/texas/supreme-court/ | WF | years 1942, 1949-2026 |
| https://law.justia.com/cases/texas/supreme-court/2026/24-0205.html | script | REFUSED (challenge) |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| https://www.txcourts.gov/supreme/orders-opinions/2026/may/may-29-2026/ | WF | Petitions denied: 24-0289 (02-22-00347-CV …), 24-0824 (05-23-00190-CV, ___ SW3d ___, 08-21-24), 25-0202 (14-22-00856-CV …) |
| same | script | verify "05-23-00190-CV" OK |
| WebSearch `"05-23-00190-CV" site:txcourts.gov` | search | unrelated orders pages (2018-2023) — docket search via web search does not work |
| https://www.txcourts.gov/cca/issues-granted/ | script, curl | 5,153 chars; link /media/1462832/pdrissues10-15-26.pdf |
| https://www.txcourts.gov/media/1462832/pdrissues10-15-26.pdf | script | 14 pp; "PDR GRANTED ISSUES"; "NO ISSUES GRANTED OCTOBER 15, 2026"; grants only |
| TAMES case pages / CCA hand-downs | — | not fetched (robots Disallow: /) |

## G — Citation map
Regexes tested locally (python `re`, IGNORECASE as build.py uses) against all examples plus guards: "Cal. Penal Code § 187", "section 12022.53 of the Penal Code", "Code of Civil Procedure section 425.16", "section 2305.10 of the Revised Code", "Ohio Rev. Code § 2305.10", "N.Y. Penal Law § 125.25" → no match. "Tex. Civ. Prac. & Rem. Code §§ 16.003-.004" → section 16.003. `python3 scripts/build.py --check`: no ERROR/WARN lines for tx.json.
