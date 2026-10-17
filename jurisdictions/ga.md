# Georgia (GA) — free legal sources

_Generated from `data/ga.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: the only government-provided O.C.G.A. is the LexisNexis-hosted free annotated code, a JavaScript app that returns no text to either tool; Justia's 2025 Code of Georgia (tier 2, WebFetch only, shell blocked by Cloudflare) is the practical text source, with chapter indexes that show section ranges. Constitution: SOS 'Revised January 2023' PDF (WebFetch ok, truncates in Art. III; shell blocked). Court rules: Court of Appeals rules are per-group HTML pages on gaappeals.gov (script ok); Supreme Court Rules and the current Uniform Superior Court Rules are PDFs under gasupreme.us/wp-content/uploads/, which robots.txt disallows; an older USCR edition (through March 6, 2025) is readable on assets.georgiacourts.gov. Admin code: rules.sos.ga.gov subject pages are constructible and script-readable (per-rule URLs are robots-disallowed), Cornell LII mirrors per rule. Case law: Court of Appeals has a GET date search and GET docket record with efast PDFs (opinions with PDFs from ~2013); Supreme Court publishes yearly opinion lists (2017-) but the PDFs are robots-disallowed, so Justia is the readable route. Cert dispositions: Supreme Court granted/denied lists (2022-) show the Court of Appeals docket in parentheses, and the Court of Appeals docket record names the certiorari number.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Supreme Court of Georgia | `ga (unverified)` | Ga. | Ga., S.E.2d, S.E., S.E.3d | — |
| Court of Appeals of Georgia | `gactapp (unverified)` | Ga. Ct. App. | Ga. App., S.E.2d, S.E., S.E.3d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Official Code of Georgia Annotated | `O.C.G.A. § 9-11-12(b)(6)`; `OCGA § 9-11-12 (b) (6)`; `Ga. Code Ann. § 16-5-1`; `O.C.G.A. §§ 9-11-12 to 9-11-16`; `OCGA § 16-13-30.1`; `Code Section 51-1-6`; `section 9-11-12 of the Official Code of Georgia Annotated` | `ga-code-justia` → `ga-code-lexis` |
| Georgia Laws (session laws) | `Ga. L. 2023, p. 123, § 1`; `Ga. L. 1983, p. 884`; `2023 Ga. Laws 123` | `ga-legis-session-laws` |
| Georgia Constitution of 1983 | `Ga. Const. art. I, § I, para. XII`; `Ga. Const. of 1983, Art. I, Sec. I, Par. XII`; `Ga. Const. art. VI, § VI, ¶ II`; `Article I, Section I, Paragraph XII of the Georgia Constitution`; `Paragraph II of Section VI of Article VI of the Georgia Constitution` | `ga-constitution-sos` → `ga-constitution-justia` |
| Uniform Superior Court Rules | `Uniform Superior Court Rule 6.4`; `USCR 6.4 (B)`; `Ga. Unif. Super. Ct. R. 6.4`; `Rule 6.4 of the Uniform Superior Court Rules`; `Unif. Super. Ct. R. 24.2` | `ga-rules-uscr-assets` → `ga-rules-uscr-gasupreme` |
| Rules of the Supreme Court of Georgia | `Ga. Sup. Ct. R. 45`; `Georgia Supreme Court Rule 22`; `Rule 40 of the Rules of the Supreme Court of Georgia` | `ga-rules-supreme` |
| Rules of the Supreme Court of Georgia (bare "Supreme Court Rule 22") *(only once this jurisdiction is known)* | `Supreme Court Rule 22` | `ga-rules-supreme` |
| Rules of the Court of Appeals of Georgia | `Ga. Ct. App. R. 25`; `Rule 33.2 of the Rules of the Court of Appeals of Georgia` | `ga-rules-coa-html` → `ga-rules-coa-pdf` |
| Rules of the Court of Appeals of Georgia (bare "Court of Appeals Rule") *(only once this jurisdiction is known)* | `Court of Appeals Rule 33.2 (a) (1)`; `COA Rule 30` | `ga-rules-coa-html` → `ga-rules-coa-pdf` |
| Georgia Rules of Professional Conduct (State Bar Rule 4-102(d)) | `Ga. R. Prof'l Conduct 1.7`; `GRPC 1.7`; `Rule 1.7 of the Georgia Rules of Professional Conduct`; `Bar Rule 4-102` | `ga-rules-prof-conduct-gabar` |
| Rules and Regulations of the State of Georgia | `Ga. Comp. R. & Regs. 160-1-3-.04`; `Ga. Comp. R. & Regs. r. 391-3-6-.03`; `Ga. Comp. R. & Regs. R. 345-2-.01`; `Rule 160-1-3-.04` | `ga-admincode-sos` → `ga-admincode-lii` |
| Georgia Rules and Regulations Monthly Bulletin | `Georgia Monthly Bulletin for June 2026`; `Ga. Admin. Bulletin (June 2026)` | `ga-admin-bulletin` |
| Georgia Reports / Georgia Appeals Reports (Ga., Ga. App.) | `Young v. Johnson, 359 Ga. App. 769, 770 (860 SE2d 82) (2021)`; `McBrayer v. Scarbrough, 317 Ga. 387, 388(1) (893 SE2d 660) (2023)`; `Smith v. State, 300 Ga. 532 (796 S.E.2d 666) (2017)` | `ga-cases-justia` → `ga-coa-opinions` → `ga-sc-opinions-list` |
| South Eastern Reporter with a Georgia parenthetical | `893 S.E.2d 660 (Ga. 2023)`; `860 S.E.2d 82 (Ga. Ct. App. 2021)`; `911 S.E.2d 638, 640 (Ga. 2025)` | `ga-cases-justia` → `ga-coa-opinions` → `ga-sc-opinions-list` |
| Georgia appellate docket numbers (Supreme Court S..., Court of Appeals A...) | `S26A0604`; `S25G1446`; `A26A0896`; `Case No. A25A2138`; `S26C1177` | `ga-coa-opinions` → `ga-cases-justia` → `ga-sc-opinions-list` → `ga-sc-docket-pubdoc` |
| Westlaw / Lexis cites for Georgia decisions | `2024 WL 123456 (Ga. Ct. App. Mar. 1, 2024)`; `2025 Ga. LEXIS 123`; `2024 Ga. App. LEXIS 456` | `ga-cases-justia` → `ga-coa-opinions` |
| Georgia certiorari history | `physical precedent only` | `ga-cert-lists` → `ga-coa-docket-cert` |
| Georgia certiorari history ("cert. denied/granted") *(only once this jurisdiction is known)* | `cert. denied (Ga. Oct. 14, 2026)`; `cert. granted, S26G1223` | `ga-cert-lists` → `ga-coa-docket-cert` |

Regexes (case-insensitive):

- Official Code of Georgia Annotated: `(?:(?:O\.?\s*C\.?\s*G\.?\s*A\.?|Ga\.\s*Code\s*Ann\.?|Code\s+Section)\s*§*\s*|(?:sec(?:tion|\.)|§)\s*(?=\d{1,2}-\d{1,3}[A-Z]?-\d+(?:\.\d+)?(?:\s*\([a-zA-Z0-9]+\))*\s+of\s+the\s+(?:Official\s+Code\s+of\s+Georgia|O\.?C\.?G\.?A)))(?P<title>\d{1,2})-(?P<chapter>\d{1,3}[A-Z]?)-(?P<section>\d+(?:\.\d+)?)(?![\d-])`
- Georgia Laws (session laws): `Ga\.\s*L\.\s*(?P<year>(?:18|19|20)\d\d),\s*p\.\s*(?P<page>\d+)|(?P<year2>(?:18|19|20)\d\d)\s+Ga\.\s*Laws\s+(?P<page2>\d+)`
- Georgia Constitution of 1983: `Ga\.\s*Const\.(?:\s*of\s*1983)?,?\s*art\.?\s*(?P<article>[IVXL]+),?\s*(?:§|Sec\.?)\s*(?P<section>[IVXL]+),?\s*(?:para\.?|Par\.?|¶)\s*(?P<paragraph>[IVXL]+(?:-[A-Z])?)|Article\s+(?P<article2>[IVXL]+),\s*Section\s+(?P<section2>[IVXL]+),\s*Paragraph\s+(?P<paragraph2>[IVXL]+)\s+of\s+the\s+(?:Georgia\s+Constitution|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Georgia)|Paragraph\s+(?P<paragraph3>[IVXL]+(?:-[A-Z])?)\s+of\s+Section\s+(?P<section3>[IVXL]+)\s+of\s+Article\s+(?P<article3>[IVXL]+)\s+of\s+the\s+(?:Georgia\s+Constitution|Constitution\s+of\s+(?:the\s+State\s+of\s+)?Georgia)`
- Uniform Superior Court Rules: `(?:Uniform\s+Superior\s+Court\s+Rule|USCR|(?:Ga\.\s*)?Unif(?:orm|\.)\s*Super(?:ior|\.)\s*C(?:our)?t\.?\s*R\.)\s*(?P<rule>\d{1,3}(?:\.\d+)*)|Rule\s+(?P<rule2>\d{1,3}(?:\.\d+)*)(?:\s*\([A-Za-z0-9]+\))*\s+of\s+the\s+Uniform\s+Superior\s+Court\s+Rules`
- Rules of the Supreme Court of Georgia: `(?:Ga\.\s*Sup\.\s*Ct\.\s*R\.|Georgia\s+Supreme\s+Court\s+Rule)\s*(?P<rule>\d{1,3}(?:\.\d+)?)|Rule\s+(?P<rule2>\d{1,3}(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Rules\s+of\s+the\s+Supreme\s+Court\s+of\s+(?:the\s+State\s+of\s+)?Georgia`
- Rules of the Supreme Court of Georgia (bare "Supreme Court Rule 22"): `Supreme\s+Court\s+Rule\s*(?P<rule>\d{1,3}(?:\.\d+)?)`
- Rules of the Court of Appeals of Georgia: `(?:Ga\.\s*Ct\.\s*App\.\s*R\.|Georgia\s+Court\s+of\s+Appeals\s+Rule)\s*(?P<rule>\d{1,2}(?:\.\d+)?)|Rule\s+(?P<rule2>\d{1,2}(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+(?:Rules\s+of\s+the\s+)?Court\s+of\s+Appeals\s+of\s+Georgia`
- Rules of the Court of Appeals of Georgia (bare "Court of Appeals Rule"): `(?:Court\s+of\s+Appeals|COA)\s+Rule\s*(?P<rule>\d{1,2}(?:\.\d+)?)`
- Georgia Rules of Professional Conduct (State Bar Rule 4-102(d)): `(?:Ga\.\s*R\.\s*Prof'?l\s*Conduct|GRPC)\s*(?P<rule>\d\.\d+)|Rule\s+(?P<rule2>\d\.\d+)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Georgia\s+Rules\s+of\s+Professional\s+Conduct|Bar\s+Rule\s+(?P<barrule>\d-\d{3}(?:\.\d+)?)`
- Rules and Regulations of the State of Georgia: `(?:Ga\.\s*Comp\.\s*R\.\s*&\s*Regs\.\s*(?:[rR]\.\s*)?|Rule\s+)(?P<rule>(?P<subject>\d{2,3}-\d{1,3}(?:-\d{1,3})?)-\.(?P<number>\d{2,3}))`
- Georgia Rules and Regulations Monthly Bulletin: `(?:Georgia\s+Monthly\s+Bulletin\s+for|Ga\.\s*Admin\.\s*Bulletin\s*\()\s*(?P<month>[A-Z][a-z]+)\s+(?P<year>(?:19|20)\d\d)`
- Georgia Reports / Georgia Appeals Reports (Ga., Ga. App.): `(?P<volume>\d{1,3})\s+Ga\.(?:\s*(?P<app>App)\.)?\s+(?P<page>\d{1,4})(?!\d)`
- South Eastern Reporter with a Georgia parenthetical: `(?P<volume>\d{1,4})\s+S\.?\s*E\.?\s*(?P<series>[23]d)?\s+(?P<page>\d{1,5})(?:,\s*\d+)?\s*\((?P<court>Ga\.(?:\s*Ct\.\s*App\.)?)\s*(?P<year>\d{4})\)`
- Georgia appellate docket numbers (Supreme Court S..., Court of Appeals A...): `\b(?P<docket>(?P<court>[SA])(?P<yy>\d{2})(?P<kind>[A-Z])(?P<number>\d{4}))\b`
- Westlaw / Lexis cites for Georgia decisions: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Ga\.|Ga\.\s*(?:(?P<lexapp>App\.)\s*)?LEXIS\s+(?P<lexis>\d+))`
- Georgia certiorari history: `(?P<physical>physical\s+precedent\s+only)`
- Georgia certiorari history ("cert. denied/granted"): `cert\.\s*(?P<disposition>denied|granted|dismissed)`

Short forms → URL key:

O.C.G.A. → `ocga`; OCGA → `ocga`; Ga. Code Ann. → `ocga`; Ga. Code → `ocga`; Code Section → `ocga`; Official Code of Georgia Annotated → `ocga`; CPA → `ocga 9-11`; Civil Practice Act → `ocga 9-11`; Georgia Evidence Code → `ocga title 24`; USCR → `uscr`; Unif. Super. Ct. R. → `uscr`; Ga. Comp. R. & Regs. → `gac`; GRPC → `grpc`; Ga. R. Prof'l Conduct → `grpc`

Georgia's own court style omits periods in the regional reporter and puts it in parentheses after the official cite: 'Young v. Johnson, 359 Ga. App. 769, 770 (860 SE2d 82) (2021)', and writes subsections with spaces: 'OCGA § 9-11-12 (b) (6)'. There is no public-domain citation format. O.C.G.A. sections are always title-chapter-section (with optional decimals, e.g. 16-13-30.1); 'Code Section' in Georgia acts means O.C.G.A. A '§§ 9-11-12 to 9-11-16' or '§§ 9-11-12 - 9-11-16' range is two sections: the regex takes the first and refuses a following hyphen-digit. Bare 'Rule 33.2' or 'Rule 22' must not route here without 'Court of Appeals' / 'Supreme Court' / 'Georgia' context; 'Code Section' also needs Georgia context. 'Rule NNN-N-N-.NN' with the '-.' separator is distinctive of the Georgia administrative code. Georgia's Civil Practice Act (O.C.G.A. § 9-11-1 et seq.) and Evidence Code (Title 24) are statutes, not court rules, so 'Rule 12(b)(6)' arguments in Georgia cite O.C.G.A. § 9-11-12 (b) (6). Docket prefixes: Supreme Court S{yy}A appeal, S{yy}C certiorari petition, S{yy}G certiorari granted, S{yy}D discretionary application, S{yy}I interlocutory application, S{yy}Q certified question, S{yy}Y bar discipline, S{yy}Z judicial discipline; Court of Appeals A{yy}A appeal, A{yy}D discretionary, A{yy}I interlocutory, A{yy}E emergency (from listing observation and memory). Court of Appeals Rule 33.2: opinions decided before Aug. 1, 2020 with special concurrences or concurrences in judgment only are 'physical precedent only' and must be marked so when cited; unreported decisions (Rule 34) and Rule 36 affirmances have no precedential value. 'cert. denied' entries route here only with Georgia context. CourtListener ids ga / gactapp are from memory, unverified. Docket-number regex must be used only with Georgia context: S/A + 2-digit year + letter + 4 digits can collide with other courts' styles. 'Unif. Super. Ct. R.' without a 'Ga.' prefix routes here: no other state uses 'Uniform Superior Court Rules', but route only with Georgia context if another state's 'Unif. Super. Ct. R.' turns up.

## A. Statutes / code

### `ga-code-lexis` — Official Code of Georgia Annotated (free public access, LexisNexis)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · State of Georgia (Code Revision Commission) / LexisNexis · text: **link-only** · official: official
- **Coverage:** Entire O.C.G.A. with annotations, on the Lexis Advance free-access container.
- **Access:** `link-only` · format html
  - Placeholders: No per-section URL; the free container is navigated interactively (TOC link at top left).
  - Index: `https://advance.lexis.com/container?config=00JAAzZDgzNzU2ZC05MDA0LTRmMDItYjkzMS0xOGY3MjE3OWNlODIKAFBvZENhdGFsb2fcIFfJnJ2IC8XZi1AYM4Ne&crid=201b1720-1ebe-46e4-9504-f2dd7251f381&prid=32ba624a-aa70-40c3-ba64-d4997b64b7ba`
  - Navigation: Human only: open container → TOC → title → chapter → section. No text reachable by either tool.
- **Automation:** WebFetch fail · shell http-error · robots: script robots check passed for the container URL
  - WebFetch: empty content (JavaScript app). fetch_doc.py: HTML with 0 characters of text.
- **Currency:** none observed (app did not render)
- **Official status:** The O.C.G.A. is the official code; dbf.georgia.gov/laws-regulations-rulings-publications/georgia-laws-title-7 says access to the entire Code is provided by LexisNexis from the General Assembly's website. Georgia v. Public.Resource.Org (2020) held the annotations uncopyrightable; Georgia announced free annotated access on Lexis in March 2022 (ABA Journal).
- **Hazard:** JavaScript-only app
- **Hazard:** no per-section URLs
- **Hazard:** session-specific crid/prid parameters may expire
- **Probe:** O.C.G.A. (container) → `https://advance.lexis.com/container?config=00JAAzZDgzNzU2ZC05MDA0LTRmMDItYjkzMS0xOGY3MjE3OWNlODIKAFBvZENhdGFsb2fcIFfJnJ2IC8XZi1AYM4Ne&crid=201b1720-1ebe-46e4-9504-f2dd7251f381&prid=32ba624a-aa70-40c3-ba64-d4997b64b7ba`
- **Evidence (2026-10-16):** Link taken from dbf.georgia.gov 'Go to the Code'. WebFetch: page content empty. Script: kind=html chars=0.
- **Notes:** legis.ga.gov (where the link officially lives) is itself a JavaScript shell (script: 113 chars). No government source offers unannotated O.C.G.A. text in fetchable form; Public.Resource.Org's copy (law.resource.org) is a non-vetted third party and not allowed.

### `ga-legis-session-laws` — Georgia General Assembly — legislation and Acts

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Georgia General Assembly · text: **link-only** · official: unknown
- **Coverage:** Bills and enacted Acts by session (expected).
- **Access:** `search-only` · format html
  - Index: `https://www.legis.ga.gov/`
  - Navigation: Human only: legislation search by session and bill number; no text reaches either tool.
- **Automation:** WebFetch untested · shell http-error · robots: script robots check: permits
  - fetch_doc.py: home page is a 113-character JavaScript shell. WebFetch of https://www.legis.ga.gov/ was refused by the session's URL-provenance gate (permission request unanswered), not by the site.
- **Currency:** none observed
- **Official status:** Not reached (JavaScript application).
- **Hazard:** JavaScript-only app
- **Probe:** legis.ga.gov home → `https://www.legis.ga.gov/`
- **Evidence (2026-10-16):** Script: kind=html chars=113 (JS shell); last-modified Sat, 15 Aug 2026.
- **Notes:** Bound 'Georgia Laws' volumes are reported to be digitized by the Digital Library of Georgia (dlg.usg.edu); not probed.

### `ga-code-justia` — Justia — Code of Georgia (2025)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Code of Georgia 2025 edition (unversioned URLs), earlier editions under /codes/georgia/{year}/ (2023, 2024 seen; 2022 in search results). Pages include the annotations (Judicial Decisions etc.) after the section text.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://law.justia.com/codes/georgia/title-{title}/chapter-{chapter}/[article-{article}/][part-{part}/]section-{title}-{chapter}-{section_dot_to_hyphen}/`
  - Placeholders: Title and chapter as plain integers from the citation (9-11-12 → title-9/chapter-11). Article (and part, where a chapter has parts) is NOT in the citation: read it from the chapter index, whose link texts show section ranges, e.g. 'Article 3 - Pleadings and Motions (§§ 9-11-7 — 9-11-16)'. Chapters without articles omit the segment (51-1-6 → /title-51/chapter-1/section-51-1-6/). Decimal sections: '.' becomes '-' (16-13-30.1 → section-16-13-30-1, verified at /title-16/chapter-13/article-2/part-1/section-16-13-30-1/). Year-specific: insert /{year}/ after /georgia/.
  - Index: `https://law.justia.com/codes/georgia/title-{title}/chapter-{chapter}/`
  - Navigation: chapter index (article links with §§ ranges, em dash) → if an article link shows 'Pts.' instead of §§ (e.g. 'Article 2 - Regulation of Controlled Substances (Pts. 1 — 2)'), open the article page and choose the part by its §§ range (two index hops) → section page. Verified: 9-11-12 → /title-9/chapter-11/article-3/section-9-11-12/; 16-5-1 → /title-16/chapter-5/article-1/section-16-5-1/; 51-1-6 → /title-51/chapter-1/section-51-1-6/; 24-8-801 → /title-24/chapter-8/article-1/section-24-8-801/; 16-13-30.1 → /title-16/chapter-13/article-2/part-1/section-16-13-30-1/.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable: robots.txt answered with a bot check (fetch_doc.py REFUSED)
  - Pages with long annotations exceed the ~100K WebFetch window (16-5-1: 103,619 chars) but the statute text comes first, so it is always inside window 1.
- **Currency:** page header and Universal Citation line — observed: "2025 Code of Georgia; 'GA Code § 9-11-12 (2025)'"
- **Official status:** Universal Citation line notes the media-neutral cite 'is not necessarily the official citation'; third-party compilation.
- **Hazard:** article/part level not derivable from the citation (index hop)
- **Hazard:** edition lags the session laws (2026 Acts not reflected)
- **Hazard:** shell blocked by Cloudflare: WebFetch only
- **Hazard:** annotations follow the statute text; do not quote annotations as statute
- **Hazard:** articles divided into parts show 'Pts.' ranges on the chapter index: one more hop to the article page
- **Probe:** O.C.G.A. § 9-11-12 → `https://law.justia.com/codes/georgia/title-9/chapter-11/article-3/section-9-11-12/` — expect: "(a) When answer presented. (1) Except as provided in paragraph"
- **Evidence (2026-10-16):** WebFetch: body (a)-(j)(5) present, '2025 Code of Georgia'; truncated only inside annotations. Also 16-5-1 '(a) A person commits the offense of murder when he'; 51-1-6 'When the law requires a person to perform an act'. | Independent check 2026-10-16: WebFetch: '(a) When answer presented. (1) Except as provided in paragraph'; '2025 Code of Georgia'; second citation O.C.G.A. § 24-8-801; also O.C.G.A. § 16-13-30.1 ok
- **Notes:** This is the only text source for the O.C.G.A. reachable by the skill. Two-fetch rule: a second fetch of the same Justia page, or of a different-year Justia edition, is not independent of the first; quotes from Georgia statutes should be flagged as single-source tier 2.

## B. Constitution

### `ga-constitution-sos` — Georgia Constitution — Electronic Version (Secretary of State PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Georgia Secretary of State · text: **fetch-and-quote** · official: unknown
- **Coverage:** Constitution of 1983 as amended; cover says revised January 2023; TOC lists Article XI at p. 89. Readable by WebFetch only through Art. VI § I.
- **Read via (in order):** **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://sos.ga.gov/sites/default/files/2023-08/Georgia Constitution - Electronic Version - January%2C 2023.pdf`
  - Placeholders: Single fixed PDF; file path changes when SOS re-issues the document.
  - Index: `https://sos.ga.gov/page/proposed-georgia-constitution-amendments`
  - Navigation: Found via web search; the SOS amendments page links only to proposed-amendment booklets (2014-2026), not to this PDF.
- **Automation:** WebFetch ok · shell blocked-challenge · robots: sos.ga.gov answers robots.txt with a bot check (fetch_doc.py REFUSED)
  - WebFetch extracts only 133,449 characters in total: window 1 ends in Art. III § IX; offset=100000 ends mid-Art. VI § I ¶ X; offset=200000 returns 'Nothing left to read'. Art. VI § II through Art. XI are unreachable on this source (shell blocked too): route them to ga-constitution-justia.
- **Currency:** PDF cover — observed: "Revised January 2023"
- **Official status:** Published by the Secretary of State; no official/unofficial statement seen in the fetched window.
- **Hazard:** January 2023 revision predates amendments ratified Nov. 2024 (check the SOS amendment booklets)
- **Hazard:** shell blocked by bot check
- **Hazard:** WebFetch reaches only Art. I through Art. VI § I (133,449 chars total); Art. VI § II onward unreachable here — second citation Ga. Const. art. VI, § VI, para. II failed; use ga-constitution-justia
- **Probe:** Ga. Const. art. I, § I, para. XII → `https://sos.ga.gov/sites/default/files/2023-08/Georgia Constitution - Electronic Version - January%2C 2023.pdf` — expect: "No person shall be deprived of the right to prosecute"
- **Evidence (2026-10-16):** WebFetch: Art. I § I ¶ XII present 'No person shall be deprived of the right to prosecute'; cover 'Revised January 2023'; truncated in Art. III § IX. | Independent check 2026-10-16: WebFetch: 'No person shall be deprived of the right to prosecute'; 'Revised January 2023'
- **Notes:** Cornell LII's Georgia page still links an older 2013 SOS constitution PDF.

### `ga-constitution-justia` — Justia — Georgia Constitution

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-article pages conart1.html … ; age of text unknown.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/georgia/conart{article_arabic}.html`
  - Placeholders: article_arabic = article number as Arabic numeral (Art. I → conart1, Art. II → conart2). No per-section anchors.
  - Index: `https://law.justia.com/constitution/georgia/`
  - Navigation: index is a table of contents only
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (bot check)
- **Currency:** index page — observed: "This Constitution may not be the most recent version."
- **Official status:** Page states 'This Constitution may not be the most recent version.'
- **Hazard:** possibly stale text
- **Hazard:** shell blocked
- **Probe:** Ga. Const. art. I, § I, para. XII → `https://law.justia.com/constitution/georgia/conart1.html` — expect: "No person shall be deprived of the right to prosecute"
- **Evidence (2026-10-16):** WebFetch: ¶ XII present 'No person shall be deprived of the right to prosecute'; page runs through Art. I § III ¶ III, not truncated. | Independent check 2026-10-16: WebFetch: ¶ XII 'No person shall be deprived of the right to prosecute'; 'may not be the most recent version'; second citation Ga. Const. art. VI, § VI, para. II ok
- **Notes:** Matches the SOS text for ¶ XII. The only reachable source for Art. VI § II onward (the SOS PDF stops at Art. VI § I for WebFetch and is shell-blocked); conart6 verified for Art. VI § VI ¶ II.

## C. Court rules

### `ga-rules-coa-html` — Rules of the Court of Appeals of Georgia (HTML, by rule group)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Court of Appeals of Georgia · text: **fetch-and-quote** · official: unknown
- **Coverage:** All rules, effective March 26, 2026, split across group pages.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.gaappeals.gov/{group_slug}/`
  - Placeholders: group_slug by rule number: 1-8 → rules-1-8; 9-10 → rules-9-10; 11-15 → rules-11-15; 16 → rule-16; 17-21 → rules-17-21; 22 → rule-22 (reserved); 23-27 → rules-23-27; 28-29 → rules-28-29; 30 → rule-30; 31 → rule-31; 32 → rule-32; 33-36 (incl. 33.1-33.3) → rules-33-36; 37-46 → rule-{n} (rule-37 … rule-46).
  - Index: `https://www.gaappeals.gov/rules-1-8/`
  - Navigation: Any rules page carries the full rules menu.
- **Automation:** WebFetch untested · shell ok · robots: gaappeals.gov: Disallow /wp-admin/ only
  - WebFetch not run: gaappeals.gov URLs were not reachable through the session's URL-provenance gate. Old host gaappeals.us now serves links.gaappeals.us, a moved-site notice pointing to gaappeals.gov.
- **Currency:** top of each rules page — observed: "These rules are effective on March 26, 2026."
- **Official status:** Published by the Court; no official/unofficial statement.
- **Hazard:** group pages, not one page per rule
- **Probe:** Ga. Ct. App. R. 33.2 → `https://www.gaappeals.gov/rules-33-36/` — expect: "Rule 33.2. Judgment as Precedent. (a) Effective Dates."
- **Evidence (2026-10-16):** fetch_doc.py grep: 'Rule 33.2. Judgment as Precedent. (a) Effective Dates.' and 'physical precedent only'; rules-1-8 has Rule 1 and Rule 8 text. | Independent check 2026-10-16: script grep: 'Rule 33.2. Judgment as Precedent. (a) Effective Dates.'; 'effective on March 26, 2026'; second citation Ga. Ct. App. R. 16 (a) ok
- **Notes:** Rule 33.2 defines binding vs. physical precedent; Rule 34 reporting; Rule 36 affirmance without opinion; Rule 38 certiorari.

### `ga-rules-coa-pdf` — Rules of the Court of Appeals of Georgia (complete PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Court of Appeals of Georgia · text: **fetch-and-quote** · official: unknown
- **Coverage:** Complete rules, effective March 26, 2026; 53 pages.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.gaappeals.gov/wp-content/uploads/2026/03/COA-Rules-Complete-Eff-26-March-26.pdf`
  - Placeholders: Fixed upload path; changes on re-issue — confirm from the 'Download Rules … (PDF)' link on any rules page.
  - Index: `https://www.gaappeals.gov/rules-1-8/`
  - Navigation: rules page → 'Download Rules - Effective March 26, 2026 (PDF)'
- **Automation:** WebFetch untested · shell ok · robots: allowed
  - 118,679 characters of text: expect WebFetch to cut off near the end.
- **Currency:** rules page link text — observed: "Download Rules - Effective March 26, 2026 (PDF)"
- **Official status:** Published by the Court.
- **Hazard:** upload path changes on re-issue
- **Hazard:** likely WebFetch truncation (118K chars)
- **Probe:** Ga. Ct. App. R. (complete) → `https://www.gaappeals.gov/wp-content/uploads/2026/03/COA-Rules-Complete-Eff-26-March-26.pdf`
- **Evidence (2026-10-16):** fetch_doc.py info: kind=pdf pages=53 chars=118679, last-modified 25 Mar 2026. | Independent check 2026-10-16: script: pdf 53 pp, 118,679 chars, last-modified 25 Mar 2026; 'Rule 36. Affirmance without Opinion'; second citation Ga. Ct. App. R. 36 ok
- **Notes:** A Spanish translation PDF is also linked.

### `ga-rules-prof-conduct-gabar` — Georgia Rules of Professional Conduct (State Bar Handbook, Rule 4-102(d))

- **Status:** REPORTED 2026-10-16 · **Tier 1** · State Bar of Georgia · text: **link-only** · official: unknown
- **Coverage:** Part IV, Chapter 1 of the Bar Rules; per-rule handbook pages.
- **Access:** `index-anchored` · format html
  - Pattern: `https://www.gabar.org/handbook?rule={handbook_id}`
  - Placeholders: handbook_id is an internal id (Rule 1.7 → rule58, Rule 1.6 → rule57, Bar Rule 4-102 → rule89); take it from the index.
  - Index: `https://www.gabar.org/general-counsel/georgia-rules-of-professional-conduct`
  - Navigation: index lists every rule with handbook?rule=ruleNN link
- **Automation:** WebFetch untested · shell http-error · robots: permits; crawl-delay 2
  - fetch_doc.py on handbook?rule=rule58 returns only the site chrome (5,528 chars); the rule text is injected by JavaScript.
- **Currency:** none observed
- **Official status:** State Bar Handbook; no statement seen.
- **Hazard:** JS-injected rule text
- **Hazard:** id-based URLs
- **Probe:** Ga. R. Prof'l Conduct 1.7 → `https://www.gabar.org/handbook?rule=rule58`
- **Evidence (2026-10-16):** Index lists 'Rule 1.7 Conflict of Interest: General Rule' → /handbook?rule=rule58; rule page has no rule text in HTML.

### `ga-rules-supreme` — Rules of the Supreme Court of Georgia (PDF)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Supreme Court of Georgia · text: **link-only** · official: unknown
- **Coverage:** Supreme Court Rules effective July 2, 2026.
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.gasupreme.us/wp-content/uploads/2026/07/SupremeCourtRules_eff-July-2-2026.pdf`
  - Placeholders: Fixed upload path from the rules page.
  - Index: `https://www.gasupreme.us/rules/`
  - Navigation: rules page → SupremeCourtRules PDF link
- **Automation:** WebFetch untested · shell blocked-robots · robots: www.gasupreme.us: User-agent * Disallow /wp-content/uploads/ and /readme.html
  - Every PDF on gasupreme.us (rules, opinions, uniform rules) is under the disallowed /wp-content/uploads/ path.
- **Currency:** PDF filename — observed: "SupremeCourtRules_eff-July-2-2026.pdf"
- **Official status:** Published by the Court on gasupreme.us/rules/.
- **Hazard:** robots-disallowed
- **Probe:** Ga. Sup. Ct. R. → `https://www.gasupreme.us/wp-content/uploads/2026/07/SupremeCourtRules_eff-July-2-2026.pdf`
- **Evidence (2026-10-16):** Link read from gasupreme.us/rules/ HTML; robots.txt 'Disallow: /wp-content/uploads/' covers the PDF.
- **Notes:** No other official copy found; third-party mirrors are not permitted.

### `ga-rules-uscr-assets` — Uniform Superior Court Rules (Judicial Council copy, through March 6, 2025)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Judicial Council / Administrative Office of the Courts of Georgia · text: **fetch-and-quote** · official: unknown
- **Coverage:** USCR including amendments received through March 6, 2025; 145 pages, Rules 1-49.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://assets.georgiacourts.gov/4/wp-content/uploads/2025/05/03170432/UNIFORM-SUPERIOR-COURT-RULES-2025_03_06.pdf`
  - Placeholders: Fixed upload path (found by web search); no index page located.
  - Index: `https://assets.georgiacourts.gov/4/wp-content/uploads/2025/05/03170432/UNIFORM-SUPERIOR-COURT-RULES-2025_03_06.pdf`
  - Navigation: Direct PDF; the current edition is on gasupreme.us (robots-disallowed).
- **Automation:** WebFetch ok · shell ok · robots: assets.georgiacourts.gov/robots.txt returns S3 AccessDenied XML (treated as none); script check permits
  - WebFetch window 1 ends in Rule 9.1(D)(11)(d); Rules 10-49 need offsets or the script (351,798 chars).
- **Currency:** PDF cover — observed: "Including Amendments Received Through March 6, 2025"
- **Official status:** Hosted on the judicial branch's assets.georgiacourts.gov; no statement.
- **Hazard:** stale: current edition is 2026-04-09
- **Hazard:** WebFetch truncation after Rule 9.1
- **Hazard:** grep for 'Rule N.N' first hits the table of contents (pp. 1-6): grep the heading with its title (e.g. 'Rule 24.2. Financial Data Required') or use 'section --start' and take a match after page 6
- **Probe:** Uniform Superior Court Rule 6.4 → `https://assets.georgiacourts.gov/4/wp-content/uploads/2025/05/03170432/UNIFORM-SUPERIOR-COURT-RULES-2025_03_06.pdf` — expect: "(A) Motions to compel discovery in accordance with OCGA § 9-11-37 shall:"
- **Evidence (2026-10-16):** WebFetch and fetch_doc.py: Rule 6.4 '(A) Motions to compel discovery in accordance with OCGA § 9-11-37 shall:'; pdf 145 pp. | Independent check 2026-10-16: script grep: 'Rule 6.4 ... (A) Motions to compel discovery in accordance with OCGA § 9-11-37 shall:'; second citation Uniform Superior Court Rule 24.2 ok

### `ga-rules-uscr-gasupreme` — Uniform Superior Court Rules and other uniform rules (current PDFs on gasupreme.us)

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Supreme Court of Georgia · text: **link-only** · official: unknown
- **Coverage:** Uniform Superior (2026-04-09), State (2024-01-18), Juvenile (2026-09-03), Probate (2023-06-01), Magistrate (2023-04-01), Municipal (2024-12-12) Court Rules, Statewide Business Court Rules (2026-06-11).
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.gasupreme.us/wp-content/uploads/2026/04/UNIFORM-SUPERIOR-COURT-RULES-2026_04_09.pdf`
  - Placeholders: Upload paths change on each amendment; take them from the index.
  - Index: `https://www.gasupreme.us/other-court-rules/`
  - Navigation: Other Court Rules page → 'Rules' link for each court
- **Automation:** WebFetch untested · shell blocked-robots · robots: Disallow /wp-content/uploads/
- **Currency:** PDF filename — observed: "UNIFORM-SUPERIOR-COURT-RULES-2026_04_09.pdf"
- **Official status:** Published by the Court on its 'Other Court Rules' page.
- **Hazard:** robots-disallowed
- **Probe:** USCR (current) → `https://www.gasupreme.us/wp-content/uploads/2026/04/UNIFORM-SUPERIOR-COURT-RULES-2026_04_09.pdf`
- **Evidence (2026-10-16):** Links read from /other-court-rules/ HTML; all under robots-disallowed /wp-content/uploads/.
- **Notes:** Use as a link; read text from ga-rules-uscr-assets and warn that it is the March 2025 edition.

## D. Administrative code

### `ga-admincode-sos` — Rules and Regulations of the State of Georgia (rules.sos.ga.gov)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Georgia Secretary of State, Administrative Procedure Division (Fastcase platform) · text: **fetch-and-quote** · official: unknown
- **Coverage:** All departments; one page per subject (or chapter where there are no subjects) holding the full text of every rule in it, with administrative history.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://rules.sos.ga.gov/gac/{subject}`
  - Placeholders: subject = the rule number with its final '-.NN' removed: 160-1-3-.04 → /gac/160-1-3; 391-3-6-.03 → /gac/391-3-6; 345-2-.01 → /gac/345-2 (chapter-level). Department index: /gac/{dept}. Per-rule URLs (/gac/160-1-3-.04) are robots-disallowed ('Disallow: /gac/*-.*'); never use them. Find the rule inside the page by the heading 'Rule {number} {title}'.
  - Index: `https://rules.sos.ga.gov/gac/`
- **Automation:** WebFetch untested · shell ok · robots: User-agent * Crawl-delay 2; Disallow /docs/, /gac/*-.*, /gac/page/, /search/, /pages/ and others; ClaudeBot, GPTBot etc. fully disallowed by name
  - Subject pages can be huge (391-3-6: 710,038 chars) — far beyond WebFetch's window; use fetch_doc.py grep/section. WebFetch not run (URL-provenance gate).
- **Currency:** home page and Download page header — observed: "Current through Rules and Regulations filed through September 17, 2026"
- **Official status:** Home page: SOS 'provides this electronic version'; 'Fastcase is the designated publisher'. No authentication statement.
- **Hazard:** per-rule URLs robots-disallowed
- **Hazard:** very long subject pages
- **Hazard:** named AI-crawler user-agents disallowed site-wide
- **Probe:** Ga. Comp. R. & Regs. 160-1-3-.04 → `https://rules.sos.ga.gov/gac/160-1-3` — expect: "(1) Purpose. The purpose of this rule is to specify the procedures"
- **Evidence (2026-10-16):** fetch_doc.py grep: 'Rule 160-1-3-.04 School Law Tribunals and Appeals (1) Purpose.' (37,725 chars). Also /gac/391-3-6 'Rule 391-3-6-.03 Designated Uses and Water Quality Standards'. | Independent check 2026-10-16: script: 'Rule 160-1-3-.04 School Law Tribunals and Appeals (1) Purpose.'; 'filed through September 17, 2026'; second citation Ga. Comp. R. & Regs. 111-8-62-.01 ok
- **Notes:** Whole-department PDFs: https://rules.sos.ga.gov/Download_pdf.aspx?st=GASOS&year=2026&dept=Departments&pdf=Department%20{n}%20{DEPARTMENT NAME} (Dept 20 = 90-page PDF).

### `ga-admincode-lii` — Cornell LII — Georgia Compiled Rules and Regulations

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Per-rule pages with history notes; department/chapter/subject browse pages.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/georgia/Ga-Comp-R-Regs-R-{rule}`
  - Placeholders: rule verbatim incl. '-.': 160-1-3-.04 → Ga-Comp-R-Regs-R-160-1-3-.04. A variant slug 'Ga-Comp-R--Regs-R-' (double hyphen) also appears in search results; if the first 404s, browse /regulations/georgia/department-{dept}.
  - Index: `https://www.law.cornell.edu/regulations/georgia`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay 10; /regulations allowed
- **Currency:** page header — observed: "State regulations are updated quarterly; we currently have two versions available."
- **Official status:** Third-party mirror; 'State regulations are updated quarterly'.
- **Hazard:** quarterly lag behind rules.sos.ga.gov
- **Hazard:** long rules (391-3-6-.03, ~111K chars) exceed one WebFetch window; prefer the script
- **Probe:** Ga. Comp. R. & Regs. 160-1-3-.04 → `https://www.law.cornell.edu/regulations/georgia/Ga-Comp-R-Regs-R-160-1-3-.04` — expect: "(1) Purpose. The purpose of this rule is to specify the procedures"
- **Evidence (2026-10-16):** WebFetch and fetch_doc.py: body present '(1) Purpose. The purpose of this rule is to specify the procedures'; history f. May 26, 1998. Script also 391-3-6-.03 ok. | Independent check 2026-10-16: WebFetch+script: '(1) Purpose. The purpose of this rule is to specify the procedures'; second citation Ga. Comp. R. & Regs. 111-8-62-.01 (script); 391-3-6-.03 (WebFetch) ok
- **Notes:** Per-rule pages make LII the practical WebFetch route and an independent second fetch for rules.sos.ga.gov text.

## D. Administrative register

### `ga-admin-bulletin` — Georgia Rules and Regulations Monthly Bulletin

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Georgia Secretary of State, Administrative Procedure Division · text: **fetch-and-quote** · official: unknown
- **Coverage:** Monthly bulletins of final rules filed, January 2020 to June 2026 (listed on the Download page).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://rules.sos.ga.gov/Download_pdf.aspx?st=GASOS&dept=Bulletins&pdf={YYYY}-{MM}%20Georgia%20Monthly%20Bulletin%20for%20{Month}%20{YYYY}`
  - Placeholders: MM zero-padded month number, Month full English name (2026-06 … June 2026). Confirm availability on the Download page's Bulletins list.
  - Index: `https://rules.sos.ga.gov/Download_pdf.aspx`
  - Navigation: Download page → Bulletins → month
- **Automation:** WebFetch untested · shell ok · robots: Download_pdf.aspx not disallowed
  - June 2026 bulletin: 130 pp, 384K chars — beyond WebFetch's window.
- **Currency:** Bulletins list on Download page — observed: "latest listed: 2026-06 Georgia Monthly Bulletin for June 2026"
- **Official status:** Published by SOS; Fastcase named as designated publisher.
- **Hazard:** long PDFs
- **Hazard:** bulletins lag several months
- **Probe:** Georgia Monthly Bulletin for June 2026 → `https://rules.sos.ga.gov/Download_pdf.aspx?st=GASOS&dept=Bulletins&pdf=2026-06%20Georgia%20Monthly%20Bulletin%20for%20June%202026` — expect: "Georgia Rules and Regulations Administrative Bulletin for June 2026"
- **Evidence (2026-10-16):** fetch_doc.py: pdf 130 pp; begins 'Georgia Rules and Regulations Administrative Bulletin for June 2026'. | Independent check 2026-10-16: script: pdf 130 pp; 'Georgia Rules and Regulations Administrative Bulletin for June 2026'; second citation Georgia Monthly Bulletin for November 2025 ok
- **Notes:** Georgia has no register of proposed rules in this series; proposed-rule notices are on the SOS 'Rules Watch' service (services.georgia.gov/sos/sos-rw/searchHome.do, not probed).

## E. Case law

### `ga-coa-opinions` — Court of Appeals of Georgia — opinion search by date, docket records and opinion PDFs

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Court of Appeals of Georgia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Date search returns dispositions from 1998 (1996-1997: 0 results; 1998-1999: 428; 2000: 2,594). PDF links are empty before ~2013 (spot checks: 2010-2012 empty, March 2013 onward present).
- **Read via (in order):** **script**
- **Access:** `constructible` · format pdf
  - Pattern: `https://www.gaappeals.gov/wp-content/themes/benjamin/docket/results_one_record.php?docr_case_num={docket}`
  - Placeholders: Docket record by GET: docr_case_num = docket as written (A26A0896). It shows trial court, judgment and date, and 'Opinion/Order View'. Opinion list by GET date range: https://www.gaappeals.gov/wp-content/themes/benjamin/docket/docketdate/results_all.php?OPstartDate={YYYY-MM-DD}&OPendDate={YYYY-MM-DD}&submit=Start+Opinions+Search — rows give docket, style, judgment date, ruling, and a PDF link https://efast.gaappeals.gov/download?filingId={uuid} (not derivable; get it with fetch_doc.py links, see navigation). Party-name search by GET: https://www.gaappeals.gov/wp-content/themes/benjamin/docket/results_all.php?searchterm={term}&submit=Start+Docket+Search.
  - Index: `https://www.gaappeals.gov/opinion-search/`
  - Navigation: Get the PDF link with `fetch_doc.py links <url> efast` (read/grep output drops hrefs). Best: docket record results_one_record.php?docr_case_num={docket} → `links … efast` returns the single 'View' link https://efast.gaappeals.gov/download?filingId={uuid}. From a date search, `links <results_all.php?OPstartDate…> filingId` lists one 'View PDF File' link per row in row order (match by position, or narrow the date range); the 'Open Record' href is ../results_one_record.php?docr_case_num={docket}.
  - Read via: PDFs on efast.gaappeals.gov (script ok)
- **Automation:** WebFetch untested · shell ok · robots: gaappeals.gov: Disallow /wp-admin/ only; efast.gaappeals.gov: no robots file; script check permits
  - WebFetch not run (URL-provenance gate). The visible forms are GET forms; no POST needed.
- **Currency:** none; date search returns same-week decisions — observed: "18 Results for dates 10-14-2026 thru 10-14-2026"
- **Official status:** Slip opinions (reconsideration notice on page 1); Ga. App. bound volumes are the official reports.
- **Hazard:** slip pagination only
- **Hazard:** no PDFs before ~2013
- **Hazard:** filingId not derivable
- **Hazard:** old host gaappeals.us is a moved-site notice
- **Probe:** Moultrie-Colquitt County Parks & Recreation Auth. v. Dekle, A26A0896 (Ga. Ct. App. Oct. 14, 2026) → `https://efast.gaappeals.gov/download?filingId=f49ddd90-c64b-4f9e-b707-416661ddffae` — expect: "After Mack Dekle was injured on a bike path maintained by the"
- **Evidence (2026-10-16):** fetch_doc.py: date search 10/14/2026 → 18 rows incl. A26A0896 'REVERSED'; PDF 11 pp, 'MARKLE, Judge. After Mack Dekle was injured on a bike path'; docket record shows trial court Thomas County. | Independent check 2026-10-16: script: PDF 11 pp, 'MARKLE, Judge. After Mack Dekle was injured on a bike path'; second citation Morrow GA Investors, LLC v. 1590 Adamson, LLC, A26A0857 (Ga. Ct. App. Oct. 7, 2026) ok

### `ga-sc-docket-pubdoc` — Supreme Court of Georgia — docket search (pubdoc)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Supreme Court of Georgia · text: **link-only** · official: unofficial
- **Coverage:** Docket search embedded in gasupreme.us/docket-search/ as an iframe.
- **Access:** `search-only` · format html
  - Index: `https://pubdoc.gasupreme.gov/`
  - Navigation: Human only: JavaScript app at /ui/.
- **Automation:** WebFetch untested · shell http-error · robots: no robots file ('Not found'); script check permits
  - pubdoc.gasupreme.gov redirects to /ui/: 49 characters of text, a Vue app plus an obfuscated bot-fingerprint script setting x-bni cookies. Not probed further.
- **Currency:** none
- **Official status:** Docket system.
- **Hazard:** JavaScript app with bot fingerprinting
- **Probe:** docket search → `https://pubdoc.gasupreme.gov/`
- **Evidence (2026-10-16):** fetch_doc.py: /ui/ kind=html chars=49.

### `ga-sc-opinion-pdfs` — Supreme Court of Georgia — slip opinion PDFs

- **Status:** BLOCKED 2026-10-16 · **Tier 1** · Supreme Court of Georgia · text: **link-only** · official: unofficial
- **Coverage:** Opinion PDFs linked from the year listings.
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://www.gasupreme.us/wp-content/uploads/{YYYY}/{MM}/{docket_lower}.pdf`
  - Placeholders: YYYY/MM = upload month (not always the decision month).
  - Index: `https://www.gasupreme.us/2026-opinions/`
  - Navigation: year listing → PDF link
- **Automation:** WebFetch untested · shell blocked-robots · robots: Disallow: /wp-content/uploads/
  - fetch_doc.py REFUSED s26a0699.pdf (rule Disallow: /wp-content/uploads/).
- **Currency:** none
- **Official status:** Slip opinions; see ga-sc-opinions-list.
- **Hazard:** robots-disallowed
- **Probe:** Chatham County v. Smith, S26A0699 (Ga. Oct. 14, 2026) → `https://www.gasupreme.us/wp-content/uploads/2026/10/s26a0699.pdf`
- **Evidence (2026-10-16):** fetch_doc.py: REFUSED: robots.txt on www.gasupreme.us disallows /wp-content/uploads/2026/10/s26a0699.pdf.

### `ga-sc-opinions-list` — Supreme Court of Georgia — opinions by year (listing pages)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Supreme Court of Georgia · text: **link-only** · official: unofficial
- **Coverage:** Year pages 2017-2026 (/2017-opinions/ … /2026-opinions/), grouped by release date with docket number and case name.
- **Access:** `constructible` · format html
  - Pattern: `https://www.gasupreme.us/{YYYY}-opinions/`
  - Placeholders: YYYY = decision year (2017-2026). Rows read 'S26A0604. WARE v. THE STATE' under a date heading. Each row links to /wp-content/uploads/{YYYY}/{MM}/{docket_lower}.pdf (e.g. /2026/10/s26a0699.pdf), which robots.txt disallows — use the row only to confirm docket, name and date, then read the text from ga-cases-justia.
  - Index: `https://www.gasupreme.us/2026-opinions/`
  - Navigation: year page → date heading → docket row
  - Read via: script (fetch_doc.py); WebFetch untested on gasupreme.us
- **Automation:** WebFetch untested · shell ok · robots: Disallow /wp-content/uploads/ (all opinion PDFs) and /readme.html
  - WebFetch not run: gasupreme.us URLs were not reachable through the session's URL-provenance gate. gasupreme.gov (new e-mail domain since March 2026) returns 404 for these pages.
- **Currency:** listing page; newest date heading — observed: "October 14, 2026"
- **Official status:** Listing page: slip opinions are subject to modification; the Georgia Reports 'Final Copy' replaces prior versions, and bound volumes are the official text.
- **Hazard:** opinion PDFs robots-disallowed
- **Hazard:** slip pagination only
- **Hazard:** pre-2017 opinions not listed
- **Probe:** Ware v. State, S26A0604 (Ga. Sept. 22, 2026) → `https://www.gasupreme.us/2026-opinions/` — expect: "S26A0604. WARE v. THE STATE"
- **Evidence (2026-10-16):** fetch_doc.py: html 14,629 chars; 'September 22, 2026' heading with 'S26A0604. WARE v. THE STATE'; 2017 page lists 'S17A1412. CARTER v. THE STATE'. | Independent check 2026-10-16: script: 'September 22, 2026 ... S26A0604. WARE v. THE STATE'; newest heading October 14, 2026; second citation 2019 Supreme Court of Georgia opinions ok

### `ga-cases-justia` — Justia — Georgia Supreme Court and Court of Appeals opinions

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1850-2026; Court of Appeals 1910-2026. Latest Supreme Court item seen: Sept. 22, 2026 (Oct. 14 releases not yet posted).
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/georgia/{court-slug}/{year}/{docket_lower}.html`
  - Placeholders: court-slug: supreme-court | court-of-appeals. year = decision year. docket_lower = first docket number lower-cased (S26A0604 → s26a0604; consolidated cases use the first). Duplicates may get a '-0' suffix (s26a0374-0.html) — check the year listing https://law.justia.com/cases/georgia/{court-slug}/{year}/ if the guess fails.
  - Index: `https://law.justia.com/cases/georgia/`
  - Navigation: year listing → decision link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (bot check)
  - WebFetch only.
- **Currency:** none
- **Official status:** Justia notes AI-assisted metadata may contain inaccuracies; reproduces the Court's slip-opinion notice.
- **Hazard:** posting lag of weeks
- **Hazard:** slip pagination, no Ga./S.E.2d star paging
- **Hazard:** shell blocked
- **Hazard:** Justia 'Date Decided' can be off by a day (A26A0857: Oct. 6 vs. Oct. 7, 2026 in the opinion header and court listing) — take the date from the opinion or the court listing
- **Probe:** Ware v. State, S26A0604 (Ga. 2026) → `https://law.justia.com/cases/georgia/supreme-court/2026/s26a0604.html` — expect: "Appellant Sterling Ware challenges his 2024 convictions for malice murder"
- **Evidence (2026-10-16):** WebFetch: full body 'Appellant Sterling Ware challenges his 2024 convictions for malice murder'; no reporter cite. Also /court-of-appeals/2026/a26a0896.html body 'After Mack Dekle was injured on a bike path'. | Independent check 2026-10-16: WebFetch: 'LAGRUA, Justice. Appellant Sterling Ware challenges his 2024 convictions for malice'; second citation Morrow GA Investors, LLC v. 1590 Adamson, LLC, A26A0857 (Ga. Ct. App. 2026) ok
- **Notes:** The readable route for Supreme Court of Georgia text, since the Court's PDFs are robots-disallowed.

## F. Subsequent history

### `ga-cert-lists` — Supreme Court of Georgia — certiorari petitions granted and denied (yearly lists)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Supreme Court of Georgia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Granted and Denied pages for 2022-2026, by disposition date; each row gives the Supreme Court docket, case name and the Court of Appeals docket in parentheses. Also /2026-discretionary/ and /2026-interlocutory/ (applications granted).
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.gasupreme.us/{YYYY}-{granted|denied}/`
  - Placeholders: Search the page text for the Court of Appeals docket (e.g. 'A25A2138') — no party-name guessing needed. Try the decision year and the following year.
  - Index: `https://www.gasupreme.us/2026-granted/`
- **Automation:** WebFetch untested · shell ok · robots: pages allowed (only /wp-content/uploads/ disallowed)
- **Currency:** page metadata line — observed: "2026 Denied … 2026-10-14"
- **Official status:** Court website listings.
- **Hazard:** only 2022 onward
- **Hazard:** pre-2022 cert history must come from the Court of Appeals docket record
- **Probe:** Vincent v. State Farm, A25A2138 → S26C1177 → `https://www.gasupreme.us/2026-denied/` — expect: "S26C1177. VINCENT v. STATE FARM MUTUAL AUTOMOBILE INSURANCE COMPANY (A25A2138)"
- **Evidence (2026-10-16):** fetch_doc.py: 2026-denied (23,660 chars) lists 'S26C1177. VINCENT v. STATE FARM MUTUAL AUTOMOBILE INSURANCE COMPANY (A25A2138)' under October 14, 2026. | Independent check 2026-10-16: script: 'S26C1177. VINCENT v. STATE FARM ... (A25A2138)' under October 14, 2026; second citation Jackson v. Stevenson, A24A1853 -> S25G0922 (cert. granted Aug. 12, 2025) ok

### `ga-coa-docket-cert` — Court of Appeals docket record — 'Supreme Court Information' block

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Court of Appeals of Georgia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Each Court of Appeals docket record lists any notice of intent, cert application date, certiorari number, disposition and remittitur; also 'Supreme Court Transfer'.
- **Read via (in order):** **script**
- **Access:** `constructible` · format html
  - Pattern: `https://www.gaappeals.gov/wp-content/themes/benjamin/docket/results_one_record.php?docr_case_num={docket}`
  - Placeholders: docket = Court of Appeals docket (A25A2138).
  - Index: `https://www.gaappeals.gov/docket-search/`
- **Automation:** WebFetch untested · shell ok · robots: allowed
- **Currency:** none
- **Official status:** Docket system.
- **Hazard:** Disposition field lags: S26C1177 denied Oct. 14, 2026 still blank on Oct. 16
- **Probe:** A25A2138 → `https://www.gaappeals.gov/wp-content/themes/benjamin/docket/results_one_record.php?docr_case_num=A25A2138` — expect: "Certiorari Number S26C1177"
- **Evidence (2026-10-16):** fetch_doc.py grep: 'Notice of Intent March 25, 2026 Application Date April 6, 2026 Certiorari Number S26C1177'; Disposition blank. | Independent check 2026-10-16: script: 'Notice of Intent March 25, 2026 ... Certiorari Number S26C1177'; Disposition blank; second citation A24A1853 ok
- **Notes:** Gives the cert number deterministically from the Court of Appeals docket; confirm the disposition on ga-cert-lists. On grant the record shows the G number with 'Disposition Granted' and date (A24A1853 → S25G0922, Aug. 12, 2025).

## Not available (do not look for these again)

- **statutes** — public.law edition of the Georgia Code: public.law lists only CA, CO, FL, NV, NY, OR, TX; georgia.public.law fails at the proxy (CONNECT 502). (2026-10-16)
- **statutes** — Cornell LII Georgia Code / Constitution / opinions: law.cornell.edu/states/georgia links out to LexisNexis, sos.ga.gov, gasupreme.us, gaappeals.us; LII hosts only the Georgia regulations. (2026-10-16)
- **statutes** — Government-hosted O.C.G.A. text readable by tools, or official bulk download: Only the LexisNexis free container (JS app, empty to both tools); legis.ga.gov is a JS shell. No bulk file found. (2026-10-16)
- **case_law** — Public-domain (vendor-neutral) citation format: Georgia courts cite Ga./Ga. App. with parallel SE2d (e.g. '359 Ga. App. 769, 770 (860 SE2d 82) (2021)' in the Dekle slip opinion). (2026-10-16)
- **case_law** — Free official reporter (Ga., Ga. App.) pagination: Court PDFs and Justia pages carry slip pagination only; Supreme Court says the bound Georgia Reports hold the official text. (2026-10-16)

## Corpus candidates (maintainers)

- `ga-rules-uscr-assets` — 145 pp, 351,798 chars; WebFetch stops in Rule 9.1 of 49. Edition is through March 6, 2025; the current 2026-04-09 edition is robots-disallowed on gasupreme.us.
- `ga-rules-coa-pdf` — 53 pp, 118,679 chars — slightly beyond one WebFetch window; HTML group pages are an alternative.
- `ga-constitution-sos` — WebFetch stops in Art. III § IX; but sos.ga.gov answers robots.txt with a bot check, so ingest.py cannot download it — not ingestable unless that changes.
- `ga-admincode-sos` — Subject pages up to ~710K chars; WebFetch cannot reach later rules. · bulk: https://rules.sos.ga.gov/Download_pdf.aspx (per-department PDFs)

## Open questions

- WebFetch was not tested on gasupreme.us, gaappeals.gov, efast.gaappeals.gov, rules.sos.ga.gov or legis.ga.gov: the session's URL-provenance gate refused those URLs (permission request unanswered). All are script-verified (or refused by robots); the independent pass should run WebFetch on them.
- Whether the Supreme Court 'Final Copy' replacements (advance-sheet versions) carry Ga. Reports pagination — not checkable (PDFs robots-disallowed).
- Whether SOS has published a constitution revised after the November 2024 amendments; only the January 2023 PDF was found.
- Supreme Court of Georgia opinions before 2017 on the Court's site: year pages exist only for 2017-2026.
- Georgia Laws (session laws) text route not established: legis.ga.gov is a JS app; Digital Library of Georgia copy not probed.
- Exact year the Court of Appeals PDFs begin (spot checks: none 2010-2012, present March 2013).
- CourtListener court ids ga / gactapp unverified.
- Rows ga-legis-session-laws, ga-rules-prof-conduct-gabar, ga-sc-docket-pubdoc (reported) and ga-rules-supreme, ga-rules-uscr-gasupreme, ga-sc-opinion-pdfs (blocked) were not re-observed by the independent check: its WebFetch attempts waited on the session's URL-approval prompt (not site behaviour). Re-check them in a session without that gate; the robots blocks were observed by the script in the research pass.
