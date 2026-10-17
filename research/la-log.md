# Louisiana (la) probe log — 2026-10-17

All probes on 2026-10-17 by `research`. "WF" = WebFetch; "script" = `python3 scripts/fetch_doc.py --research …` (info/read/grep/links). Raw HTML of script-fetched pages was inspected from the script's own cache (no separate downloads). Quoted text ≤ 15 words. WebFetch calls used: 17 of ~55 (one timed out on an approval prompt). No quota/rate failures. No CourtListener tool used.

## Robots / host checks
| URL | Tool | Result |
|---|---|---|
| https://legis.la.gov/robots.txt, https://www.legis.la.gov/robots.txt | script | 404 |
| https://www.lasc.org/robots.txt | script | 200 text/html, 0 chars — the Blazor app shell, no rules |
| https://www.doa.la.gov/robots.txt | script | 404 |
| https://law.justia.com/robots.txt | script | REFUSED: host off for the day (robots.txt challenge earlier today) |
| https://senate.la.gov/robots.txt | script | `User-agent:* Allow:/ Disallow: /private/` |
| https://www.la-fcca.org/robots.txt (and lafcca.hosted2.civiclive.com) | script | `*` disallows /Search/, /WebApi/, /WebServices/, /portal/svc/, some .asmx |
| https://www.la2nd.org/robots.txt | script | Disallow /wp-admin/ only |
| https://www.la3circuit.org/robots.txt | script | redirected to 404 HTML page (no robots file) |
| https://www.la4th.org/robots.txt | script | 404 |
| https://www.fifthcircuit.org/robots.txt | script | only `User-agent: amazon-QBusiness` Disallow: / |
| https://www.law.cornell.edu/regulations/louisiana | script check | allowlisted; robots permits; crawl-delay 10 |
| cdnsm5-hosted2.civiclive.com (redirect target of lafcca …/UniformRulesoCtsofAppeal) | script | REFUSED: robots.txt answered with a bot check |

## A — Statutes
| URL | Tool | Result |
|---|---|---|
| https://legis.la.gov/legis/LawSearch.aspx | script | 200, 6,158 chars; "Laws have been updated through the 2025 First Extraordinary Session."; disclaimer "not official or authoritative"; 'View a Specific Law' = POST form (ddlLawBodies CHC/CC/CCP/CCRP/CE/CA/HRULE/JRULE/CONST/RS/SRULE + Title + Section) |
| https://legis.la.gov/legis/Laws_Toc.aspx?folder=75&level=Parent (RS) | script | 200; TITLE 1…56 are `__doPostBack` links only |
| …Laws_Toc.aspx?folder=72 (Constitution) | script | ARTICLE 1…14 postback links only |
| …Laws_Toc.aspx?folder=67 (Civil Code) | script | 866,866 chars, 5,034 links; 'CC 2315' → Law.aspx?d=109369 |
| …folder=70 (Evidence) | script | 'CE 702' → d=72506 |
| …folder=68 / 69 / 71 | script | 'CCP 966' → d=112309; 'CCRP 894' → d=112888; 'CHC 101' → d=72534 |
| Law.aspx?d=109369 / 72506 / 112309 / 112888 | script | bodies present: "Art. 2315. Liability for acts causing damages A. Every act whatever"; "Art. 702. Testimony by experts"; "Art. 966. Motion for summary judgment; procedure"; "Art. 894. Suspension and deferral of sentence" |
| WebSearch `legis.la.gov Law.aspx "RS 9:2800"` and `site:legis.la.gov "RS 9:2800"` | WebSearch | wrong sections (d=106718 RS 9:1590, d=107045 RS 9:229, d=107760 RS 9:3576.8) |
| Law.aspx?d=106718 / 107045 / 107760 | script | 200, 1.6K chars each; headings as above |
| WebSearch `"9:2800" "Limitation of liability for public bodies" Louisiana Law.aspx` | WebSearch | https://legis.la.gov/Legis/Law.aspx?d=107250; Justia 2006 /123/107250.html |
| https://legis.la.gov/Legis/Law.aspx?d=107250 | script | 4,605 chars; "RS 9:2800 §2800. Limitation of liability for public bodies A. A public entity" |
| same | WF | YES; "A. A public entity is responsible under Civil Code Article"; no currency; not truncated |
| https://legis.la.gov/legis/LawPrint.aspx?d=107250 | script | 3,166 chars, same body |
| WebSearch justia louisiana revised statutes 9:2800 | WebSearch | Justia 2014/2018/2021 links |
| https://law.justia.com/codes/louisiana/2021/civil-code/article-243 | WF | repealed article; newest-version link /codes/louisiana/civil-code/article-243/ "2025 Louisiana Laws" |
| https://law.justia.com/codes/louisiana/civil-code/article-2315/ | WF | YES "Every act whatever of man that causes damage to another"; "2025 Louisiana Laws" |
| https://law.justia.com/codes/louisiana/revised-statutes/title-9/rs-9-2800/ | WF | YES "A public entity is responsible under Civil Code Article 2317"; 2025 |
| https://law.justia.com/codes/louisiana/ | WF | editions 2006, 2009, 2011–2025 |
| https://law.justia.com/codes/louisiana/2025/ | WF | bodies: revised-statutes, children-s-code, civil-code, code-of-civil-procedure, code-of-criminal-procedure, code-of-evidence |
| https://law.justia.com/codes/louisiana/code-of-evidence/article-702/ | WF | YES "A. A witness who is qualified as an expert by"; 2025 |

## B — Constitution
| URL | Tool | Result |
|---|---|---|
| WebSearch `legis.la.gov Law.aspx "Const. Art. I, §22"` | WebSearch | Law.aspx?d=206288 ("CONST 1 22"); senate.la.gov constitution PDFs |
| https://legis.la.gov/legis/Law.aspx?d=206288 | script | "CONST 1 22 §22. Access to Courts Section 22. All courts shall be open" |
| https://senate.la.gov/Documents/LAConstitution.pdf | script | PDF 108 pp, 682,983 chars, LM 30 Jan 2024; cover "(As amended through calendar year 2023)"; Art. I § 22 found p. 15, columns interleaved |
| https://senate.la.gov/Documents/Constitution/constitution.pdf | script | PDF 133 pp, LM 29 Oct 2019 (older edition) |
| https://law.justia.com/constitution/louisiana/ | WF | TOC only; "This Constitution may not be the most recent version." |
| https://law.justia.com/constitution/louisiana/Article1.html | WF | YES "All courts shall be open, and every person shall have an adequate"; complete |

## C — Court rules
| URL | Tool | Result |
|---|---|---|
| https://www.fifthcircuit.org/uniform.aspx | script | rule text in HTML; link "Download the Uniform Rules … (PDF)" |
| https://www.fifthcircuit.org/pdf/URCA_eff07012026.pdf | script | 32 pp, 74,989 chars, LM 13 Jul 2026; "(As amended, with amendments effective as of July 1, 2026)"; Rule 2-18.1 p. 22 |
| https://lafcca.hosted2.civiclive.com/clerks_office/UniformRulesoCtsofAppeal | script | REFUSED (redirect to cdnsm5-hosted2.civiclive.com, bot-checked robots) |
| https://www.la2nd.org/ | script | links local rules page and Rule 9 / 9.1 PDFs (not probed) |
| WebSearch for lasc.org Supreme Court Rules / District Court Rules | WebSearch | only courtrules.net / vlex (non-vetted; not used) |

## D — Admin code and register
| URL | Tool | Result |
|---|---|---|
| https://www.doa.la.gov/doa/osr/louisiana-administrative-code/ | script | 43,708 chars; title links are .docx (/media/{slug}/31.docx, 33v03.docx …); "Last Amended Date" table (Title 4 August 2026) |
| https://www.doa.la.gov/media/tyynhk5m/31.docx | script | 200, LM 30 Jan 2026; parsed as HTML → raw ZIP bytes ("PK … [Content_Types].xml") |
| same | WF | "[binary data]" — NO |
| https://www.law.cornell.edu/regulations/louisiana (→ title-33 → part-III → chapter-5) | script | links; "Chapter 5 - Permit Procedures (§ III-501 to III-551)" |
| https://www.law.cornell.edu/regulations/louisiana/La-Admin-Code-tit-33-SS-III-501 | script | 36,299 chars; "The provisions of this Chapter apply to the owner and operator"; "State regulations are updated quarterly" |
| https://www.law.cornell.edu/regulations/louisiana/La-Admin-Code-tit-28-SS-I-101 | script | 200, 2,736 chars, LM 2 Aug 2025 |
| https://www.doa.la.gov/doa/osr/louisiana-register/ | script | January–October 2026 Edition links (2601.docx … 2610.docx); no archive link found |
| https://www.doa.la.gov/doa/osr/ | script | no register archive link |

## E — Case law
| URL | Tool | Result |
|---|---|---|
| https://www.lasc.org/ , /Opinions, /opinions/2024, /Actions, /News_Releases, /court_actions | script | each 200 text/html, 0 extractable chars (Blazor Server prerender markers) |
| https://www.lasc.org/js/blazorinterop.js, /manifest.json | script | no endpoint URLs |
| https://www.lasc.org/ | WF | ERROR: permission request not answered in time (not retried) |
| WebSearch (5 queries) for lasc.org opinion / news-release PDFs | WebSearch | none found |
| https://law.justia.com/cases/louisiana/supreme-court/2023/ | WF | entries e.g. 2022-K-01824 Dec 8 2023 → /2023/2022-k-01824.html |
| https://law.justia.com/cases/louisiana/supreme-court/2023/2022-k-01824.html | WF | YES "We granted the State's application to consider whether defendant's claim"; PDF cases.justia.com/…/2023-2022-k-01824.pdf |
| https://cases.justia.com/louisiana/supreme-court/2023-2022-k-01824.pdf?ts=1702055071 | script | 11 pp; "FOR IMMEDIATE NEWS RELEASE NEWS RELEASE #054 FROM: CLERK OF SUPREME COURT"; cites "2006-2346 (La. 10/26/07), 968 So.2d 131" |
| https://law.justia.com/cases/louisiana/ | WF | Supreme Court + First–Fifth Circuit listings |
| https://law.justia.com/cases/louisiana/supreme-court/ | WF | years 1885–2026 |
| https://law.justia.com/cases/louisiana/supreme-court/2026/ | WF | 27 entries Mar 6–Jul 31 2026; no writ-action lists |
| https://law.justia.com/cases/louisiana/first-circuit-court-of-appeal/ | WF | years 1991–2026; latest 2026CW0629 Aug 28 2026 |
| https://law.justia.com/cases/louisiana/first-circuit-court-of-appeal/2026/2026cw0629.html | WF | NO body text; PDF link only |
| https://cases.justia.com/louisiana/first-circuit-court-of-appeal/2026-2026cw0629.pdf?ts=1787930178 | script | 2 pp, 1 char (image scan) |
| https://www.la-fcca.org/decisions | script | year links 2008–2026 to lafcca.hosted2.civiclive.com |
| https://lafcca.hosted2.civiclive.com/decisions/o_p_i_n_i_o_n_s_2026 ; cms/One.aspx?portalId=161585&pageId=219768 (2024) | script | 200, body "Loading..." — JS file manager, no links |
| https://www.la2nd.org/opinions/ | script | 30,236 chars; table date / case no. / name / judge / disposition; PDFs /wp-content/uploads/2026/10/57066ca.pdf … |
| https://www.la2nd.org/opinions/?opinion_year=2025 / 2010 / 2009 | script | 780 / 1,005 / 1,095 links |
| …?opinion_year=2008 / 2006 / 2004 / 2002 / 2000 | script | 0 links |
| https://www.la2nd.org/wp-content/uploads/2026/10/57066ca.pdf | script | 13 pp; "Judgment rendered October 14, 2026. Application for rehearing may be filed" |
| https://www.la3circuit.org/ , /Cases/Opinions.aspx, /Cases/OpinionNewsletter.aspx | script | search/calendar are `__doPostBack` only |
| https://www.la4th.org/ , /Search.aspx | script | opinion search = WebForm_DoPostBack; case years 1992–2026 |
| https://www.fifthcircuit.org/ , /searchopinions.aspx, /searchArchives.aspx, /news.aspx | script | home lists recent decisions with /dmzdocs/… PDF links; searches are POST |
| https://www.fifthcircuit.org/dmzdocs/OI/PO/2026/3BEA2644-D02C-48BF-953E-91C9B93E8536.pdf | script | 8 pp; "Fifth Circuit Court of Appeal State of Louisiana No. 26-CA-27" |
| …/dmzdocs/WI/Writ Disposition/2026/180FED6E-….pdf (raw space) | script | error "URL can't contain control characters" |
| same with %20 | script | 3 pp; "No. 26-C-483 … APPLYING FOR SUPERVISORY WRIT" |
| WebSearch for la3circuit / la4th / la-fcca opinion PDF URLs | WebSearch | none found |

## F — Subsequent history
| URL | Tool | Result |
|---|---|---|
| lasc.org (see E) | script/WF | unreadable / gated |
| https://law.justia.com/cases/louisiana/supreme-court/2026/ | WF | no writ grant/denial lists |

## Build
- `python3 scripts/build.py --check`: no ERROR/WARN lines.
- `python3 scripts/build.py --cross`: "0 cross-jurisdiction match(es)".
