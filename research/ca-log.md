# California (ca) probe log, 2026-10-16

Tools: shell = curl from the research workspace (through the agent proxy); WF = WebFetch. All dates are 2026-10-16.

## Shell status sweep
| URL | Result |
|---|---|
| leginfo.legislature.ca.gov/robots.txt | 403, cf-mitigated: challenge |
| leginfo .../codes_displaySection.xhtml?lawCode=CIV&sectionNum=1714 | 403, cf-mitigated: challenge |
| california.public.law/robots.txt | 200. Disallows /admin /api /data /demo /images /users |
| california.public.law/codes/ca_civ_code_section_1714 | 301 to /codes/civil_code_section_1714 |
| california.public.law/codes/{penal_code_section_187, evidence_code_section_1200, vehicle_code_section_23152, business_and_professions_code_section_17200, government_code_section_12940, civil_code_section_1798.100, welfare_and_institutions_code_section_5150} | 200 each; titles e.g. "California Penal Code section 187 (2025)" |
| california.public.law/california_constitution, /constitution | 404 |
| law.justia.com/robots.txt | 403, cf-mitigated: challenge |
| courts.ca.gov/robots.txt | 200. Drupal default; Disallow /core/ /profiles/ /search* /cjer etc. Nothing about opinions or PDFs |
| www.courts.ca.gov/opinions.htm | 301 to courts.ca.gov/opinions.htm |
| courts.ca.gov/opinions/publishedcitable-opinions | 200 (379 KB), 50 PDF links, ?page=N, filter selects |
| ...?field_opinion_source_target_id=103 | 200, S-docket PDFs (S295866...) |
| ...?field_case_number_plain_value=B347548 | 200, single B347548.PDF |
| courts.ca.gov/opinions/unpublishednon-citable-opinions | 200, links /opinions/nonpub/B353460.PDF... |
| courts.ca.gov/opinions/published-opinions-older-120-days | 200, links /opinions/archive/*.PDF and appellatecases dockets |
| courts.ca.gov/opinions/published-opinions-review-granted | 200, rows linking to appellatecases dockets |
| www.courts.ca.gov/opinions/documents/F089182.PDF | 301 to courts.ca.gov, then 301 to www4.courts.ca.gov, then 200 application/pdf. Text begins "Filed 9/17/26; Certified for Publicatoin 10/15/26" |
| archive PDFs A169697N, A170226, A170727, A170985, A171271 | 200 pdf. B340734, A170747, S126387 archive: 404 |
| www4.courts.ca.gov/robots.txt | 403 Cloudflare "Just a moment..." challenge |
| appellatecases.courtinfo.ca.gov/robots.txt | 403, cf-mitigated: challenge |
| govt.westlaw.com/robots.txt | 403. /calregs/index 403 Cf-Mitigated: challenge |
| oal.ca.gov/robots.txt | 200. Disallow /wp-admin/, Crawl-delay: 10 |
| www.lexisnexis.com/clients/CACourts/ | 301 to advance.lexis.com (not followed). lexisnexis.com robots: Disallow: /clients/ |
| www.law.cornell.edu/robots.txt | 200. Crawl-delay: 10; disallows /search/, /user/, admin paths |
| law.cornell.edu/regulations/california | 200, title-1..title-N links |
| law.cornell.edu/regulations/california/Cal-Code-Regs-Tit-8-SS-3203 | 200 but no section body (soft 404) |
| law.cornell.edu/regulations/california/title-8/.../group-1/article-1 | 200, section link form /regulations/california/8-CCR-3207 |
| law.cornell.edu/regulations/california/2-CCR-11009 | 200, "§ 11009 - Principles of Employment Discrimination" |
| law.cornell.edu/states/california | 200; links out to leginfo for statutes |
| supreme.courts.ca.gov/robots.txt | 200. Disallow /profiles/ |
| supreme.courts.ca.gov/case-information/weekly-conference-results | 200, 107 pdf links |
| supreme.courts.ca.gov/.../conference%20results%20-%20071526%20-%20R.pdf | 200 pdf, "Results from the petition conference of 7/15/2026" |
| courts.ca.gov/sitemap.xml | 200 |

## WebFetch probes
| # | URL | Result |
|---|---|---|
| 1 | leginfo .../codes_displaySection.xhtml?lawCode=CIV&sectionNum=1714 | CLIENT_ERROR |
| 2 | leginfo.legislature.ca.gov/robots.txt | CLIENT_ERROR |
| 3 | california.public.law/codes/civil_code_section_1714 | YES. "Everyone is responsible, not only for the result of his". "Verified: Oct. 12, 2026". Not truncated |
| 4 | leginfo .../codes.xhtml | CLIENT_ERROR |
| 5 | california.public.law/codes/code_of_civil_procedure_section_437c | YES. "A party may move for summary judgment in an action". Reaches subd. (u) |
| 6 | california.public.law/codes | 29 code slugs. "Updated October 5, 2026" |
| 7 | leginfo ...lawCode=CONS&article=I&sectionNum=1. | CLIENT_ERROR |
| 8 | law.justia.com/codes/california/code-civ/division-3/part-2/title-1/chapter-2/section-1714/ (guessed) | CLIENT_ERROR |
| 9 | law.justia.com/codes/california/ | editions 2005-2025, no disclaimer |
| 10 | law.justia.com/codes/california/2025/ | 29 links /codes/california/code-{abbr}/. Disclaimer "These codes may not be the most recent version." |
| 11 | WebSearch: leginfo lawCode=CONS | public.law and Justia results only |
| 12 | law.justia.com/codes/california/code-civ/ | "2025 California Code" heading |
| 13 | california.public.law/california_constitution | CLIENT_ERROR (shell 404) |
| 14 | law.justia.com/codes/california/code-civ/ (divisions) | division-1..4 |
| 15 | WebSearch: public.law constitution | Justia /constitution/california/ only |
| 16 | law.justia.com/constitution/california/article-i/ | TOC only. Section links /article-i/section-N/ |
| 17 | law.justia.com/codes/california/code-civ/division-3/ | part-1..4 |
| 18 | .../code-civ/division-3/part-3/ | section links incl. section-1714/ |
| 19 | law.justia.com/constitution/california/article-i/section-1/ | YES. "All people are by nature free and independent and have" |
| 20 | .../code-civ/division-3/part-3/section-1714/ | YES. Same first words as #3. "2025 California Code" |
| 21 | WebSearch: Cal. Const. public.law | Justia only |
| 22 | law.cornell.edu/regulations/california/Cal-Code-Regs-Tit-8-SS-3203 | NOT PRESENT |
| 23 | govt.westlaw.com/calregs/Index | SITE_BLOCKED, "Access to this website has been blocked" |
| 24 | courts.ca.gov/opinions.htm | Opinions landing page. Links to published/unpublished/older-120/review-granted |
| 25 | law.cornell.edu/regulations/california/8-CCR-3203 | YES. "(a) Effective July 1, 1991, every employer shall establish, implement". "State regulations are updated quarterly" |
| 26 | courts.ca.gov/opinions/publishedcitable-opinions | Oct 15, 2026 entries (F089182, C104172M, B347548). "Slip opinions from the last 120 days are posted" |
| 27 | www.courts.ca.gov/opinions/documents/F089182.PDF | ROBOTS_DISALLOWED |
| 28 | appellatecases ...query_caseNumber=S287285 | ROBOTS_DISALLOWED |
| 29 | WebSearch: Rules of Court 8.500 | courts.ca.gov/cms/rules/index/eight/rule8_N |
| 30 | courts.ca.gov/opinions/documents/F089182.PDF | ROBOTS_DISALLOWED |
| 31 | www.courts.ca.gov/cms/rules/index/eight/rule8_500 | YES. "(a) Right to file a petition, answer, or reply (1) A party". "California Rules of Court 2026" |
| 32 | courts.ca.gov/rules-forms/rules-court | title index URLs and title PDFs. Local Rules link |
| 33 | www.courts.ca.gov/opinions/archive/A170226.PDF | ROBOTS_DISALLOWED |
| 34 | courts.ca.gov/cms/rules/index/three/rule3_1350 | YES. "(a) Definitions As used in this rule: (1) \"Motion\" refers to" |
| 35 | courts.ca.gov/forms-rules/rules-court/local-rules | county index with effective dates (Alameda Eff. July 1, 2026) |
| 36 | courts.ca.gov/robots.txt | no PDF/opinion disallows; User-agent * only |
| 37 | courts.ca.gov/system/files?file=file/roc-title-8_0.pdf | Title 8 text, truncated |
| 38 | law.justia.com/cases/california/supreme-court/ | 1853-2026. Pattern /{year}/s{docket}.html |
| 39 | www.lexisnexis.com/clients/CACourts/ | ROBOTS_DISALLOWED |
| 40 | courts.ca.gov/opinions/official-reports-opinions (guessed) | CLIENT_ERROR |
| 41 | law.justia.com/cases/california/supreme-court/2026/s287946.html | YES, full text. "Generally, the right to recover costs at the conclusion of". Slip pagination, no Cal.5th cite |
| 42 | law.justia.com/cases/california/court-of-appeal/ | 1897-2026. Pattern /{year}/{docket}.html |
| 43 | WebSearch: Official Reports | listing page states "This no-fee service is provided by LexisNexis" |
| 44 | WebSearch: conference results | supreme.courts.ca.gov PDF URLs |
| 45 | supreme.courts.ca.gov/case-information/weekly-conference-results | latest Sept 30, 2026; years 2024-2026; "generally made available on Thursday mornings" |
| 46 | ...conference%20results%20-%20071526%20-%20R.pdf | heading plus rows S287285 (Opinion Modification: Denied), S296637 (Petition for Review: Granted) |
| 47 | oal.ca.gov/publications/notice_register/ | links to online issues page and schedule PDF |
| 48 | oal.ca.gov/california_regulatory_notice_online/ | monthly pages from Jan 1, 2018. Latest two are ?page_id=...&preview=true |
| 49 | oal.ca.gov/publications/ccr/ | OAL "contracts with Barclays... free online version of the Official CCR" (Westlaw) |
| 50 | oal.ca.gov/august-2026-california-regulatory-notice-registers/ | PDFs No. 32-Z (Aug 7), 33-Z (Aug 14) |
| 51 | leginfo.legislature.ca.gov/ (home) | content returned (welcome notice), no challenge |
| 52 | california.public.law/codes/civil_code | divisions. "Civil Code. Refreshed: 2025-05-12" |
| 53 | leginfo ...sectionNum=1714.&lawCode=CIV | CLIENT_ERROR |
| 54 | leginfo .../codes.xhtml (retry) | CLIENT_ERROR |
| 55 | leginfo ...lawCode=PEN&sectionNum=187. | CLIENT_ERROR |
| 56 | leginfo .../faqs.xhtml | CLIENT_ERROR |
| 57 | law.justia.com/cases/california/court-of-appeal/2026/a172398.html | YES, full text. "This case involves a dispute over the denial of a". No Cal.App.5th cite |
| 58 | courts.ca.gov/cms/rules/index/eight | rule links rule8_500, rule8_1105, rule8_1115. "Current as of July 1, 2025" |
| 59 | WebSearch: Justia rules of court | no Justia CA Rules of Court pages found |

## Notes
- leginfo: The home page fetched once, but every deep page failed under WF and the shell got a Cloudflare challenge. Recorded as blocked.
- Opinion PDFs: the shell gets them only because the proxy passed the www4 hop. WF reports ROBOTS_DISALLOWED. Recorded as blocked, no workaround.
- No CourtListener tools were used. The court IDs come from memory.
