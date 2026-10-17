# Delaware (DE) — free legal sources

_Generated from `data/de.json` (compiled 2026-10-16, schema v1). Do not edit by hand._

**Rules.** Use only the sources below for this jurisdiction. Never construct a URL that is not a `constructible` pattern here; for `index-anchored` sources fetch the index and follow real links. Quote only from rows marked VERIFIED, and only under the skill's two-fetch rule. Tier 2 text must be disclosed in the report with its currency string. A BLOCKED host is never fetched by any route.

**Read routes**, tried in the order each row lists them: **corpus** — `corpus.py get|resolve|search|verify` reads a pre-built, integrity-checked extraction of the official document (state its capture date; run `corpus.py check` if STALE/EXPIRED); **script** — `fetch_doc.py read|grep|section|verify|links <url>` reads the live official file as exact text with no truncation (needs the host reachable from your sandbox; exit 3 = refused, never retry another way); **fetch tool** — WebFetch: summarised and cut at ~100K characters, so use it to locate and link, and quote from it only under the two-fetch rule.

## Summary

Statutes: delcode.delaware.gov (official) — section text sits on the subchapter page, or on the chapter page when a chapter has no subchapters; Justia 2025 is a constructible tier-2 fallback. Constitution: delcode.delaware.gov per-article pages. Court rules are full-set PDFs on courts.delaware.gov that the fetch tool cuts off after ~100K characters; read them from the corpus (Superior Court Criminal Rules ingested 2026-10-16) or with fetch_doc.py. Admin Code: regulations.delaware.gov is a JavaScript app (the fetch tool gets an empty shell) with a public JSON API and PDF downloads; Cornell LII mirrors it per section. Case law: the courts.delaware.gov opinion database (Supreme Court from 1998, Chancery and Superior from 2000) is searchable by a plain GET URL and serves slip-opinion PDFs that fetch_doc.py reads in full; Justia covers older Supreme Court and Chancery opinions.

## G. Citation map

| Court | CourtListener id | Bluebook | Reporters | Public-domain cite |
|---|---|---|---|---|
| Delaware Supreme Court | `del (unverified)` | Del. | A.3d, A.2d, A., Del. | — |
| Delaware Court of Chancery | `delch (unverified)` | Del. Ch. | A.3d, A.2d, A., Del. Ch. | — |
| Delaware Superior Court | `delsuperct (unverified)` | Del. Super. Ct. | A.3d, A.2d, A. | — |
| Delaware Family Court | `delfamct (unverified)` | Del. Fam. Ct. | A.3d, A.2d | — |
| Delaware Court of Common Pleas | `delctcompl (unverified)` | Del. Com. Pl. | A.3d, A.2d | — |
| Court on the Judiciary of Delaware | `deljudct (unverified)` | Del. Jud. | A.3d, A.2d | — |

| Recognise | Examples | Route to (in order) |
|---|---|---|
| Delaware Code | `6 Del. C. § 18-101`; `Del. Code Ann. tit. 8, § 141`; `8 Del. C. § 102(b)(7)`; `10 Del. C. § 8106`; `Title 5, Section 952 of the Delaware Code`; `section 102(b)(7) of the Delaware General Corporation Law` | `de-code-delcode` → `de-code-justia` |
| Delaware Code (bare 'Section N of Title T') *(only once this jurisdiction is known)* | `Section 141(k) of Title 8` | `de-code-delcode` → `de-code-justia` |
| Laws of Delaware (session laws) | `85 Del. Laws c. 518`; `66 Del. Laws, c. 141` | `de-session-laws` |
| Delaware Constitution | `Del. Const. art. I, § 9`; `Del. Const. art. IV, § 11`; `Article I, Section 9 of the Delaware Constitution` | `de-constitution-delcode` → `de-constitution-justia` |
| Court of Chancery Rules | `Ct. Ch. R. 23.1`; `Court of Chancery Rule 12(b)(6)`; `Del. Ch. Ct. R. 174` | `de-rules-chancery` |
| Superior Court Civil Rules | `Del. Super. Ct. Civ. R. 56`; `Rule 12(b)(6) of the Delaware Superior Court Civil Rules` | `de-rules-superior-civil` |
| Superior Court Civil Rules (bare, no "Del.") *(only once this jurisdiction is known)* | `Super. Ct. Civ. R. 12(b)(6)`; `Superior Court Civil Rule 60(b)` | `de-rules-superior-civil` |
| Superior Court Criminal Rules | `Del. Super. Ct. Crim. R. 61`; `Rule 61 of the Delaware Superior Court Criminal Rules` | `de-rules-superior-criminal` |
| Superior Court Criminal Rules (bare, no "Del.") *(only once this jurisdiction is known)* | `Super. Ct. Crim. R. 61`; `Superior Court Criminal Rule 35(a)`; `Rule 61 of the Superior Court Criminal Rules`; `Rule 35(b) of the Superior Court Criminal Rules`; `Super. Ct. Crim. R. 35A` | `de-rules-superior-criminal` |
| Supreme Court Rules | `Supr. Ct. R. 42`; `Del. Supr. Ct. R. 14(g)`; `Delaware Supreme Court Rule 41` | `de-rules-supreme` |
| Supreme Court Rules (bare "Supreme Court Rule 41") *(only once this jurisdiction is known)* | `Supreme Court Rule 41` | `de-rules-supreme` |
| Delaware Rules of Evidence | `D.R.E. 702`; `Del. R. Evid. 401`; `Delaware Uniform Rule of Evidence 803(6)` | `de-rules-evidence` |
| Delaware Lawyers' Rules of Professional Conduct | `Del. Lawyers' R. Prof'l Conduct 1.7`; `DLRPC 1.15` | `de-rules-professional-conduct` |
| Delaware Administrative Code | `14 Del. Admin. Code § 101-1.0`; `14 DE Admin. Code 101`; `7 Del. Admin. Code 1102` | `de-admincode-api` → `de-admincode-lii` |
| Delaware Register of Regulations | `28 DE Reg. 220 (9/1/2024)`; `30 Del. Reg. 145` | `de-register-api` |
| Reported Delaware cases (Atlantic Reporter) | `Melson v. Allman, 244 A.2d 85 (Del. 1968)`; `Prince v. Bensinger, 244 A.2d 89 (Del. Ch. 1968)`; `Corwin v. KKR Fin. Holdings LLC, 125 A.3d 304 (Del. 2015)` | `de-opinions-courts` → `de-cases-justia` |
| Old official state reporters | `30 Del. Ch. 115`; `45 Del. 123` | `de-cases-justia` |
| Unreported Chancery / Superior decisions by civil action number | `C.A. No. 2023-0309-JTL`; `2022-1045-LWW`; `C.A. No. 2019-0123-JTL, slip op. at 12 (Del. Ch. Feb. 12, 2024)`; `N25C-12-630 SKR CCLD` | `de-opinions-courts` → `de-cases-justia` |
| Supreme Court docket / Delaware unreported form (Supr. Ct. R. 14(g)(ii)) | `No. 340, 2024`; `Fox v. Fox, Del., No. 510, 1997, Berger, J. (May 14, 1998)` | `de-opinions-courts` → `de-cases-justia` |
| Westlaw / Lexis unreported cites | `2024 WL 747180 (Del. Ch. Feb. 23, 2024)`; `1998 Del. LEXIS 179 (Del. May 15, 1998)`; `2019 Del. Ch. LEXIS 123` | `de-opinions-courts` → `de-cases-justia` |

Regexes (case-insensitive):

- Delaware Code: `(?:(?:(?P<title>\d{1,2})\s+Del\.\s*C(?:ode)?\.?(?:\s+Ann\.)?\s*§+\s*(?P<section>\d{1,3}[A-Za-z]?-\d+[A-Za-z]?|\d+[A-Za-z]?)(?!\d)|Del\.\s*Code\s+Ann\.\s*tit\.\s*(?P<title2>\d{1,2}),?\s*§+\s*(?P<section2>\d{1,3}[A-Za-z]?-\d+[A-Za-z]?|\d+[A-Za-z]?)(?!\d))|Title\s+(?P<title3>\d{1,2}),?\s+(?:Section|§)\s*(?P<section3>\d+[A-Za-z]?(?:-\d+[A-Za-z]?)?)\s+of\s+the\s+Delaware\s+Code)|(?:sec(?:tion|\.)|§)\s*(?P<section4>\d+[A-Za-z]?(?:-\d+[A-Za-z]?)?)(?:\([a-z0-9]+\))*\s+of\s+(?:the\s+)?(?:Delaware\s+General\s+Corporation\s+Law|DGCL)|(?:sec(?:tion|\.)|§)\s*(?P<section5>\d+[A-Za-z]?(?:-\d+[A-Za-z]?)?)(?:\([a-z0-9]+\))*\s+of\s+Title\s+(?P<title5>\d{1,2})(?!\d)\s+of\s+the\s+Delaware\s+Code`
- Delaware Code (bare 'Section N of Title T'): `(?:sec(?:tion|\.)|§)\s*(?P<section5>\d+[A-Za-z]?(?:-\d+[A-Za-z]?)?)(?:\([a-z0-9]+\))*\s+of\s+Title\s+(?P<title5>\d{1,2})(?!\d)(?!\s+of\s+the\s)`
- Laws of Delaware (session laws): `(?P<volume>\d{1,3})\s+Del\.\s*Laws,?\s*c(?:h)?\.\s*(?P<chapter>\d+)`
- Delaware Constitution: `Del\.\s*Const\.\s*art\.\s*(?P<article>[IVXL]+),?\s*§\s*(?P<section>\d+[A-Za-z]?)|Article\s+(?P<article2>[IVXL]+),?\s+Section\s+(?P<section2>\d+[A-Za-z]?)\s+of\s+the\s+Delaware\s+Constitution`
- Court of Chancery Rules: `(?:Ct\.\s*Ch\.\s*R\.|Del\.\s*Ch\.\s*Ct\.\s*R\.|Ch(?:ancery)?\.?\s*(?:Court\s+)?R(?:ule)?\.?|Court of Chancery Rule)\s*(?P<rule>\d+(?:\.\d+)?[A-Za-z-]*)`
- Superior Court Civil Rules: `Del(?:\.|aware)\s*Super(?:ior)?\.?\s*C(?:our)?t\.?\s*Civ(?:il)?\.?\s*R(?:ule)?\.?\s*(?P<rule>\d+[A-Z]?(?:\.\d+)?)|Rule\s+(?P<rule2>\d+[A-Z]?(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Delaware\s+Superior\s+Court\s+Civil\s+Rules`
- Superior Court Civil Rules (bare, no "Del."): `Super(?:ior)?\.?\s*C(?:our)?t\.?\s*Civ(?:il)?\.?\s*R(?:ule)?\.?\s*(?P<rule>\d+[A-Z]?(?:\.\d+)?)|Rule\s+(?P<rule2>\d+[A-Z]?(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Superior\s+Court\s+Civil\s+Rules`
- Superior Court Criminal Rules: `Del(?:\.|aware)\s*Super(?:ior)?\.?\s*C(?:our)?t\.?\s*Crim(?:inal)?\.?\s*R(?:ule)?\.?\s*(?P<rule>\d+[A-Z]?(?:\.\d+)?)|Rule\s+(?P<rule2>\d+[A-Z]?(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Delaware\s+Superior\s+Court\s+Criminal\s+Rules`
- Superior Court Criminal Rules (bare, no "Del."): `Super(?:ior)?\.?\s*C(?:our)?t\.?\s*Crim(?:inal)?\.?\s*R(?:ule)?\.?\s*(?P<rule>\d+[A-Z]?(?:\.\d+)?)|Rule\s+(?P<rule2>\d+[A-Z]?(?:\.\d+)?)(?:\s*\([a-z0-9]+\))*\s+of\s+the\s+Superior\s+Court\s+Criminal\s+Rules`
- Supreme Court Rules: `(?:Del(?:\.|aware)\s*Supr(?:eme)?\.?\s*C(?:our)?t\.?\s*R(?:ule)?\.?|(?<![\w.])Supr\.\s*Ct\.\s*R\.)\s*(?P<rule>\d+)`
- Supreme Court Rules (bare "Supreme Court Rule 41"): `Supreme\s+Court\s+Rule\s*(?P<rule>\d+)`
- Delaware Rules of Evidence: `(?:D\.\s*R\.\s*E\.|Del\.\s*R\.\s*Evid\.|Delaware (?:Uniform )?Rules? of Evidence)\s*(?P<rule>\d{3,4})`
- Delaware Lawyers' Rules of Professional Conduct: `(?:Del\.\s*Lawyers'?\s*R\.\s*Prof'?l\s*Conduct|DLRPC|Delaware Lawyers'? Rules? of Professional Conduct)\s*(?P<rule>\d\.\d+)`
- Delaware Administrative Code: `(?P<title>\d{1,2})\s+(?:Del\.|DE)\s*Admin\.?\s*Code\s*(?:§+\s*)?(?P<regulation>\d+[A-Z]?)(?:-(?P<section>\d+\.\d+))?`
- Delaware Register of Regulations: `(?P<volume>\d{1,2})\s+(?:DE|Del\.)\s*Reg\.\s*(?P<page>\d+)`
- Reported Delaware cases (Atlantic Reporter): `(?P<volume>\d{1,4})\s+A\.(?:\s*(?P<series>[23])d)?\s+(?P<page>\d{1,5})\s*(?:,\s*\d+)?\s*\((?P<court>Del\.(?:\s*(?:Ch|Super\.\s*Ct|Fam\.\s*Ct|Com\.\s*Pl)\.?)?)\s*(?P<year>\d{4})\)`
- Old official state reporters: `(?P<volume>\d{1,3})\s+Del\.(?:\s*(?P<ch>Ch)\.)?\s+(?P<page>\d{1,4})`
- Unreported Chancery / Superior decisions by civil action number: `(?:C\.A\.\s*No\.\s*)?(?P<year>(?:19|20)\d\d)-(?P<seq>\d{4})-(?P<judge>[A-Z]{2,4})|(?P<superior>[NKS]\d{2}[A-Z]-\d{2}-\d{3,4}\s+[A-Z]{2,4}(?:\s+CCLD)?)`
- Supreme Court docket / Delaware unreported form (Supr. Ct. R. 14(g)(ii)): `No\.\s*(?P<number>\d{1,4}),\s*(?P<year>(?:19|20)\d\d)`
- Westlaw / Lexis unreported cites: `(?P<year>(?:19|20)\d\d)\s+(?:WL\s+(?P<wl>\d+)(?:,\s*at\s*\*\d+)?\s*\(Del\.|Del\.\s*(?:(?P<lexch>Ch\.|Super\.)\s*)?LEXIS\s+(?P<lexis>\d+))`

Supr. Ct. R. 14(g) mandates Bluebook form with no parallel state-reporter cite (A.2d/A.3d only) and gives the Delaware unreported form 'Name, Del., No. N, YYYY, Judge, J. (date)'. Del. and Del. Ch. official reporters ended long ago (Del. Ch. vol. 43, 1968; Del. vol. 59, 1966, per memory); modern Delaware cases are cited to A.2d/A.3d or WL/LEXIS. Many Chancery and Superior decisions are never in A.3d and are cited by WL number plus C.A. No.; a WL number cannot be resolved to a free URL: search by party name in the courts.delaware.gov database or Justia instead. Chancery C.A. Nos. take the form YYYY-NNNN-XXX (judge initials suffix, sometimes omitted). Supreme Court dockets take the form 'No. N, YYYY' (filing year). CourtListener court ids are from memory and unverified. Routing caution: 'No. N, YYYY' and bare C.A. numbers are Delaware forms but can collide with other courts' docket styles; route on them only with Delaware context. Westlaw cites route here only with a '(Del.' parenthetical. DGCL = Title 8, chapter 1 (8 Del. C. § 101 et seq.). A '§§ a-b' range is a span of sections, not a hyphenated section: the regex refuses it, so take the first section. Bare 'Section N of Title T' is context_required: Maine uses the same prose form (split 2026-10-17).

## A. Statutes / code

### `de-code-delcode` — Delaware Code Online

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Delaware Code Revisors / Division of Legislative Services (prepared with LexisNexis) · text: **fetch-and-quote** · official: official
- **Coverage:** All 31 titles of the Delaware Code; per-title authenticated PDFs; HTML by chapter/subchapter.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format html
  - Pattern: `https://delcode.delaware.gov/title{title}/c{chapter:03d}{suffix}/[sc{subchapter:02d}/]index.html#{section}`
  - Placeholders: title = plain integer, no padding (title5, title10, title29). Chapter folder = 'c' + 3-digit zero-padded chapter number + lower-case letter suffix if any (c018, c081, c002a, c012d); some odd slugs exist (title6 'c012_1' = Chapter 12 False Claims Act, 'c000a' = UCC Article A) so always confirm via the title index. Hyphenated sections give the chapter directly (6 Del. C. § 18-101 → c018). Non-hyphenated sections (8 Del. C. § 141, 5 Del. C. § 952, 10 Del. C. § 8106) do not encode the chapter: the title and chapter index pages show NO section ranges. Infer the chapter from the section's leading digits — sections numbered NNN or NNNN sit in chapter floor(section/100) (5 § 952 → c009, 8 § 141 → c001, 10 § 8106 → c081, 19 § 710 → c007) — then open that chapter page and confirm the anchor id="{section}" exists (on the chapter page or one of its subchapter pages). If it is not there, use de-code-justia's chapter listing, which does show section ranges, to find the right chapter; never keep guessing. If a chapter has subchapters, the chapter index.html is navigation-only and lists sc01..scNN links (two-digit, Arabic, even though headings say Subchapter IV); the subchapter page holds the text. If a chapter has NO subchapters (e.g. title10/c081), the chapter index.html itself holds the section text. Sections are anchored by id equal to the section number (id="18-101", id="141", id="8106").
  - Index: `https://delcode.delaware.gov/title{title}/index.html`
  - Navigation: title index → chapter link (cNNN) → if the page lists sc links, follow the subchapter covering the section → section text with anchor #{section}. Examples verified: 6 Del. C. § 18-101 → /title6/c018/sc01/index.html; 5 Del. C. § 952 → /title5/c009/sc02/index.html; 8 Del. C. § 141 → /title8/c001/sc04/index.html; 10 Del. C. § 8106 → /title10/c081/index.html (no subchapters).
- **Automation:** WebFetch ok · shell ok · robots: none (404)
  - WebFetch truncates at ~100,000 characters with '[Content truncated due to length...]'; large subchapter pages (e.g. 11 Del. C. ch. 5 subch. II, ~154K chars of text, §§ 601-792) lose later sections: § 791 NOT PRESENT even with offset=100000 (that window ended at § 778). For such pages use the shell (curl + strip tags, anchor id) or Justia's per-section page.
- **Currency:** Home page 'Notice' paragraph only; no currency line on chapter/subchapter pages — observed: "includes all acts enacted as of September 10, 2026, up to … 85 Del. Laws, c. 518"
- **Official status:** Home page notice (https://delcode.delaware.gov/index.html) says the online Code 'is considered an official version of the State of Delaware statutory code'; UELMA-authenticated per-title PDFs (e.g. /title8/title8.pdf) also available.
- **Hazard:** chapter not derivable from non-hyphenated section numbers (index hop)
- **Hazard:** chapter index navigation-only when subchapters exist
- **Hazard:** WebFetch truncation at ~100K chars on large subchapter pages
- **Hazard:** irregular chapter slugs (c012_1, c000a)
- **Hazard:** WebFetch reads ~100K characters per page; on very large subchapter pages later sections can be unreachable even with offset (11 Del. C. § 791) — use de-code-justia's per-section page for those.
- **Probe:** 6 Del. C. § 18-101 → `https://delcode.delaware.gov/title6/c018/sc01/index.html` — expect: "As used in this chapter unless the context otherwise requires"
- **Evidence (2026-10-16):** WebFetch: § 18-101 body present ('As used in this chapter unless the context otherwise requires'), page complete through § 18-113. Also verified: 5 Del. C. § 952 at /title5/c009/sc02 ('Unless the agreement governing a revolving credit plan otherwise provides'); 8 Del. C. § 141 & § 145 at /title8/c001/sc04; 10 Del. C. § 8106 at /title10/c081/index.html ('(a) No action to recover damages for trespass'). curl 200 on all. | Independent check 2026-10-16: § 18-101: 'As used in this chapter unless the context otherwise requires'; complete, no currency line; second citation 19 Del. C. § 710 ok
- **Notes:** Answers to carried-over questions: (1) chapters without subchapters ARE served with text at …/cNNN/index.html (title10/c081 verified, 46 sections); (2) zero-padding is always 3 digits for chapters (c001, c018, c081) and 2 digits for subchapters (sc01..sc18); (3) titles > 9 are unpadded (title10, title29). Per-title authenticated PDF at https://delcode.delaware.gov/title{title}/title{title}.pdf (title8.pdf 1.0 MB, HTTP 200), constitution at /constitution/constitution.pdf.

### `de-session-laws` — Laws of Delaware (session laws)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Delaware General Assembly · text: **fetch-and-quote** · official: unknown
- **Coverage:** Session law chapters; per-chapter HTML pages keyed by an internal id, grouped by volume.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format html
  - Placeholders: Per-chapter URL uses an internal id (Chapter?id=22385), not the volume/chapter number. Volume listing: /SessionLaws/Chapters?volume={volume}.
  - Index: `https://legis.delaware.gov/SessionLaws`
  - Navigation: SessionLaws index → row whose first number is the Del. Laws volume ('NN - NNNth GA - years') → its Chapters?volume=<internal id> link (no formula: 84→165, 85→166, 83→48, 66→42) → chapter. Large volume listings truncate in WebFetch (vol. 84 at ch. 317) — use offset.
- **Automation:** WebFetch ok · shell ok · robots: none (robots.txt 302-redirects to a 404 page)
- **Currency:** none stated
- **Official status:** delcode home page says UELMA-authenticated PDFs of the Laws of Delaware are available; the HTML chapter page shows no authentication statement.
- **Hazard:** id-based URLs not derivable from citation
- **Probe:** 66 Del. Laws c. 141 (Chapter 141, S.B. 105, 134th G.A.) → `https://legis.delaware.gov/SessionLaws/Chapter?id=22385` — expect: "AN ACT TO AMEND CHAPTER 27, TITLE 11 OF THE"
- **Evidence (2026-10-16):** WebFetch: body text present, 'Approved July 9, 1987'; page links to Chapters?volume=42 (volume number of the listing, not confirmed as Del. Laws vol.). | Independent check 2026-10-16: 'AN ACT TO AMEND CHAPTER 27, TITLE 11 OF THE DELAWARE CODE'; approved July 9, 1987; second citation 84 Del. Laws c. 100 ok
- **Notes:** Low priority; found via search result, only one chapter probed. The volume parameter (42) does not obviously equal the Del. Laws volume (66) — treat volume navigation as unverified.

### `de-code-justia` — Justia — Delaware Code (2025)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Delaware Code editions 2006, 2010-2012, 2014-2025; unversioned URL serves the 2025 edition.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/codes/delaware/title-{title}/chapter-{chapter}/[subchapter-{subchapter_roman_lower}/]section-{section}/`
  - Placeholders: title and chapter unpadded integers (chapter-1, chapter-18, chapter-81); subchapter as lower-case Roman numeral (subchapter-i, subchapter-iv, subchapter-ii) and omitted when the chapter has none (10 Del. C. § 8106 → /title-10/chapter-81/section-8106/); section verbatim incl. hyphen (section-18-101). Chapter and subchapter must still be learned from the official index (same hop as delcode). Year-specific: insert /{year}/ after /delaware/.
  - Index: `https://law.justia.com/codes/delaware/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: could not read: robots.txt itself returns 403 to the shell
  - Shell gets HTTP 403 with 'cf-mitigated: challenge' (Cloudflare) on every law.justia.com URL; WebFetch succeeds. Use WebFetch only, never the shell.
- **Currency:** page header and Universal Citation line — observed: "2025 Delaware Code; '8 DE Code § 141 (2025)'"
- **Official status:** Page states 'These codes may not be the most recent version' and disclaims warranties of accuracy.
- **Hazard:** edition lags official text by up to a year
- **Hazard:** shell blocked by Cloudflare
- **Probe:** 8 Del. C. § 141 → `https://law.justia.com/codes/delaware/title-8/chapter-1/subchapter-iv/section-141/` — expect: "(a) The business and affairs of every corporation organized under"
- **Evidence (2026-10-16):** WebFetch: body present, '2025 Delaware Code'. Also 6 Del. C. § 18-101 (/title-6/chapter-18/subchapter-i/section-18-101/), 10 Del. C. § 8106 (/title-10/chapter-81/section-8106/), 11 Del. C. § 791 (/title-11/chapter-5/subchapter-ii/section-791/) all body present. | Independent check 2026-10-16: '(a) The business and affairs of every corporation organized under'; '2025 Delaware Code'; second citation 19 Del. C. § 710 ok
- **Notes:** Per-section pages make Justia the practical second fetch for sections beyond delcode's WebFetch truncation point (e.g. 11 Del. C. § 791). Correction to prior skill belief: a tier-2 for the Delaware Code exists (Justia); public.law and Cornell LII do not host it.

## B. Constitution

### `de-constitution-delcode` — Delaware Constitution (Delaware Code Online)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Delaware Code Revisors / Division of Legislative Services · text: **fetch-and-quote** · official: official
- **Coverage:** Constitution of 1897 as amended; one page per article.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://delcode.delaware.gov/constitution/constitution-{page:02d}.html`
  - Placeholders: page = article number (Arabic) + 1: 01 = Preamble, 02 = Art. I, 03 = Art. II, 04 = Art. III, 05 = Art. IV (Judiciary), … 18 = Art. XVII, 19 = Schedule. The index links use .shtml, which 301-redirects to .html.
  - Index: `https://delcode.delaware.gov/constitution/index.html`
  - Navigation: index is TOC only (no body text)
- **Automation:** WebFetch ok · shell ok · robots: none (404)
- **Currency:** constitution index page header — observed: "with Amendments made subsequently thereto, through July 1, 2025."
- **Official status:** Hosted on delcode.delaware.gov; home page says UELMA-authenticated PDF of the Constitution is available (/constitution/constitution.pdf).
- **Hazard:** index page has no text
- **Hazard:** .shtml → .html redirect
- **Probe:** Del. Const. art. I, § 9 → `https://delcode.delaware.gov/constitution/constitution-02.shtml` — expect: "All courts shall be open; and every individual for an"
- **Evidence (2026-10-16):** WebFetch: Art. I §§ 1 and 9 body present, article complete. Index page: currency string above, body NOT PRESENT. | Independent check 2026-10-16: Art. I § 9 'All courts shall be open; and every individual for an'; second citation Del. Const. art. IV, § 11 ok

### `de-constitution-justia` — Justia — Delaware Constitution

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Whole constitution on one page with #artNN anchors.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/constitution/delaware/#art{article:02d}`
  - Placeholders: single page; anchor art01..
  - Index: `https://law.justia.com/constitution/delaware/`
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (403 Cloudflare)
  - Page is ~134K chars; WebFetch reads 100K per call, use offset=100000 for later articles.
- **Currency:** none stated
- **Official status:** Third-party compilation; no currency date.
- **Hazard:** outdated text: Art. I § 1 reads 'all men' where official reads 'all persons'
- **Hazard:** Article XII marked NOT CURRENTLY AVAILABLE
- **Hazard:** page exceeds WebFetch window
- **Hazard:** The #artNN anchor does not change what WebFetch reads (always from character 0); later articles need offset=100000.
- **Probe:** Del. Const. art. I, § 1 → `https://law.justia.com/constitution/delaware/` — expect: "Although it is the duty of all men frequently to"
- **Evidence (2026-10-16):** WebFetch: body present; text differs from official (gender-neutral amendment not reflected) — evidence that this copy is stale. Use only as last resort. | Independent check 2026-10-16: 'Although it is the duty of all men frequently to'; Art. XII 'NOT CURRENTLY AVAILABLE'; 133,919 chars; second citation Del. Const. art. IV, § 11 ok

## C. Court rules

### `de-rules-chancery` — Rules of the Court of Chancery (full set PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Delaware Court of Chancery / Delaware Courts · text: **fetch-and-quote** · official: unknown
- **Coverage:** Full Chancery rule set, 231 pages.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.delaware.gov/forms/download.aspx?id=160908`
  - Placeholders: Fixed document id; it may change on re-publication. Re-confirm from the rules index.
  - Index: `https://courts.delaware.gov/rules/`
  - Navigation: rules index → 'Court of Chancery Rules' download link
- **Automation:** WebFetch ok · shell ok · robots: courts.delaware.gov: User-agent * — disallows /_declt, one admin-order PDF and ~10 specific /opinions/download.aspx?ID=… items; /rules and /forms allowed
  - WebFetch reads ~100K chars per call; Rule 23.1 visible in window 1, window 2 (offset=100000) covers Rules 23.2–26 only. Later rules (e.g. Rule 174) need many offsets: prefer shell curl + pdftotext (439K chars total).
- **Currency:** rules index page next to the link (not inside the PDF) — observed: "Current as of June 1, 2026"
- **Official status:** Published by the courts on courts.delaware.gov/rules; no official/unofficial statement in the PDF.
- **Hazard:** WebFetch truncation (~100K chars per window)
- **Hazard:** id may change when the set is re-issued
- **Hazard:** WebFetch window 1 ends mid-Rule 23.1(d); later rules need offset=100000 or shell pdftotext; Rule 174 unreachable by WebFetch.
- **Probe:** Ct. Ch. R. 23.1 → `https://courts.delaware.gov/forms/download.aspx?id=160908` — expect: "(a) Pleading Requirements. The complaint in a derivative action must:"
- **Evidence (2026-10-16):** curl: application/pdf, filename 'full set of chancery rules (6.1.2026).pdf', 231 pp. WebFetch: Rule 23.1 present, Rule 174 NOT PRESENT (truncated). | Independent check 2026-10-16: Rule 23.1 '(a) Pleading Requirements. The complaint in a derivative action must:'; truncated in 23.1(d); second citation Ct. Ch. R. 12(b) ok

### `de-rules-evidence` — Delaware Uniform Rules of Evidence (PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Delaware Supreme Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** D.R.E. with comments, 75 pp.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.delaware.gov/forms/download.aspx?id=39388`
  - Placeholders: Fixed document id; re-confirm from rules index.
  - Index: `https://courts.delaware.gov/rules/`
  - Navigation: rules index → 'Delaware Uniform Rules of Evidence'
- **Automation:** WebFetch ok · shell ok · robots: allowed
  - WebFetch window 1 ends at Rule 614; Rule 702 needs offset=100000 or shell (164K chars).
- **Currency:** none stated (index gives no date; filename suggests May 2018 amendments) — observed: "drewithmay2018amend.pdf"
- **Official status:** Published on courts.delaware.gov/rules.
- **Hazard:** WebFetch truncation
- **Hazard:** no currency statement
- **Probe:** D.R.E. 401 → `https://courts.delaware.gov/forms/download.aspx?id=39388` — expect: "Evidence is relevant if: (a) it has any tendency to"
- **Evidence (2026-10-16):** WebFetch: Rule 401 present; Rule 702 NOT PRESENT (truncated at 614). curl: 75 pp PDF, pdftotext finds 'Rule 702. Testimony by Expert Witnesses.' | Independent check 2026-10-16: Rule 401 'Evidence is relevant if: (a) it has any tendency to'; truncated at Rule 614; second citation D.R.E. 501 ok

### `de-rules-professional-conduct` — Delaware Lawyers' Rules of Professional Conduct (with comments, PDF)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Delaware Supreme Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** 390 pp. with comments.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.delaware.gov/forms/download.aspx?id=160568`
  - Placeholders: Fixed document id; re-confirm from rules index.
  - Index: `https://courts.delaware.gov/rules/`
  - Navigation: rules index → 'Delaware Lawyers' Rules of Professional Conduct'
- **Automation:** WebFetch ok (truncated) · shell ok · robots: allowed
  - 750K chars of text — WebFetch would need ~8 windows; use shell pdftotext.
- **Currency:** rules index page; PDF filename — observed: "current through November 18, 2025"
- **Official status:** Published on courts.delaware.gov/rules.
- **Hazard:** very long PDF; WebFetch truncation
- **Hazard:** WebFetch window 1 ends in Rule 1.5's notes; Rules 1.6 onward (incl. 1.7) are not reachable by WebFetch — shell pdftotext only.
- **Probe:** DLRPC 1.7 → `https://courts.delaware.gov/forms/download.aspx?id=160568`
- **Evidence (2026-10-16):** curl: application/pdf 'lawyers’ rules of professional conduct_as amended through 11-18-25.pdf', 390 pp; WebFetch not run on this document. | Independent check 2026-10-16: PDF reached; WebFetch window 1 ends in Rule 1.5's notes; Rules 1.6 onward (incl. 1.7) are not reachable by WebFetch — shell pdftotext only.
- **Notes:** Other rule sets on the same index (Family Court Civil/Criminal, Court of Common Pleas Civil/Criminal, JP Court, Disciplinary Procedure, CLE, Rapid Arbitration, Code of Judicial Conduct) follow the same download.aspx?id= pattern; ids recorded in the log.

### `de-rules-superior-civil` — Superior Court Civil Rules (2026 edition PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Delaware Superior Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** Superior Court Rules of Civil Procedure, 117 pp.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.delaware.gov/forms/download.aspx?id=304488`
  - Placeholders: Fixed document id; re-confirm from rules index.
  - Index: `https://courts.delaware.gov/rules/`
  - Navigation: rules index → 'Superior Court Rules of Civil Procedure'
- **Automation:** WebFetch ok · shell ok · robots: allowed (see de-rules-chancery)
  - WebFetch window 1 ends inside Rule 16.1; Rule 56(c) NOT PRESENT in window 1. Use shell pdftotext (429K chars) or offsets.
- **Currency:** rules index page — observed: "2026 Edition"
- **Official status:** Published on courts.delaware.gov/rules; no official statement.
- **Hazard:** WebFetch truncation
- **Probe:** Super. Ct. Civ. R. 12(b) → `https://courts.delaware.gov/forms/download.aspx?id=304488` — expect: "Every defense, in law or fact, to a claim for"
- **Evidence (2026-10-16):** curl: application/pdf 'del_super_ct_civ_02052026.pdf'; WebFetch: Rule 12(b) present, 56(c) NOT PRESENT (truncated at 16.1). | Independent check 2026-10-16: Rule 12(b) 'Every defense, in law or fact, to a claim for relief'; truncated in 16.1(c); second citation Super. Ct. Civ. R. 8(a) ok

### `de-rules-superior-criminal` — Superior Court Criminal Rules (2026 edition PDF)

- **Status:** REPORTED 2026-10-16 · **Tier 1** · Delaware Superior Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** Superior Court Rules of Criminal Procedure.
- **Read via (in order):** **corpus** `de/super-ct-crim-r` (85 units, captured 2026-10-16) → **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.delaware.gov/forms/download.aspx?id=304498`
  - Placeholders: Fixed document id; re-confirm from rules index.
  - Index: `https://courts.delaware.gov/rules/`
  - Navigation: rules index → 'Superior Court Rules of Criminal Procedure'
- **Automation:** WebFetch ok (truncated) · shell ok · robots: allowed
  - Expect the same ~100K WebFetch window as the civil rules. Shell download verified 2026-10-16 (619,227-byte PDF, 68 pages; robots.txt permits /forms/).
- **Currency:** rules index page — observed: "2026 Edition"
- **Official status:** Published on courts.delaware.gov/rules.
- **Hazard:** WebFetch truncation (expected)
- **Hazard:** WebFetch window 1 ends in Rule 29(a); Rules 30 onward (incl. 35, 61) are not reachable by WebFetch — shell pdftotext only.
- **Probe:** Super. Ct. Crim. R. 61 → `https://courts.delaware.gov/forms/download.aspx?id=304498`
- **Evidence (2026-10-16):** Link and currency string read from the rules index via WebFetch; document itself not fetched. | Independent check 2026-10-16: PDF reached; WebFetch window 1 ends in Rule 29(a); Rules 30 onward (incl. 35, 61) are not reachable by WebFetch — shell pdftotext only.

### `de-rules-supreme` — Rules of the Supreme Court of Delaware (PDF)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Delaware Supreme Court · text: **fetch-and-quote** · official: unknown
- **Coverage:** Supreme Court Rules, 67 pp., as amended through 2-2-26.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://courts.delaware.gov/forms/download.aspx?id=174928`
  - Placeholders: Fixed document id; re-confirm from rules index.
  - Index: `https://courts.delaware.gov/rules/`
  - Navigation: rules index → 'Supreme Court Rules'
- **Automation:** WebFetch ok · shell ok · robots: allowed
  - WebFetch window 1 ends inside Rule 26; Rule 42 (interlocutory appeals) NOT PRESENT in window 1 — use offset or shell pdftotext (369K chars).
- **Currency:** rules index page; PDF filename — observed: "Current through February 2, 2026"
- **Official status:** Published on courts.delaware.gov/rules.
- **Hazard:** WebFetch truncation
- **Probe:** Del. Supr. Ct. R. 14(g) → `https://courts.delaware.gov/forms/download.aspx?id=174928` — expect: "The following shall be the form of citations: (i) Reported"
- **Evidence (2026-10-16):** curl: application/pdf 'sc rules_as amended through 2-2-26.pdf', 67 pp. WebFetch: 14(g) present; Rule 42 NOT PRESENT (truncated in Rule 26(j)). | Independent check 2026-10-16: 14(g) 'The following shall be the form of citations: (i) Reported Opinions'; truncated Rule 26(j); second citation Supr. Ct. R. 6(a) ok
- **Notes:** Rule 14(g) is the Delaware citation-form rule (see citation_map.notes).

## D. Administrative code

### `de-admincode-api` — Delaware Administrative Code (regulations.delaware.gov)

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Delaware Division of Research / Registrar of Regulations · text: **fetch-and-quote** · official: unknown
- **Coverage:** All Admin Code titles; each regulation as HTML (via API) and PDF.
- **Read via (in order):** **script**
- **Access:** `index-anchored` · format json
  - Pattern: `https://regulations.delaware.gov/AdminCode/title{title}/{regulation}  (human URL; SPA) ; PDF: https://regulations.delaware.gov/api/file/download/{pdfId}`
  - Placeholders: Human page URL is constructible (/AdminCode/title14/101) but is an Angular shell. Text route: POST https://regulations.delaware.gov/api/AdminCode/regulation with JSON {"regulationUrl":"/AdminCode/title{title}/{regulation}"} → JSON {titleName, regulationName, pdfId, htmlBody}. Then GET /api/file/download/{pdfId} → PDF (WebFetch-readable). Title listing: POST /api/AdminCode/title {"regulationUrl":"/AdminCode/title{title}"}; all titles: GET /api/AdminCode/titles.
  - Index: `https://regulations.delaware.gov/api/AdminCode/titles`
  - Navigation: shell: POST /api/AdminCode/regulation → pdfId → WebFetch the PDF URL
- **Automation:** WebFetch fail · shell ok · robots: robots.txt path returns the SPA HTML (no robots file) — treat as none
  - WebFetch on /AdminCode/title14/101 returns only the SPA head ('Delaware Regulations'); body NOT PRESENT. WebFetch cannot POST, so the skill must get pdfId via shell, then WebFetch the PDF (works).
- **Currency:** none stated on regulation or PDF
- **Official status:** delcode home page says UELMA-authenticated PDFs of the Administrative Code are available; the regulation pages themselves carry no statement.
- **Hazard:** JS-only SPA
- **Hazard:** POST-only API for text lookup
- **Hazard:** no currency statement
- **Hazard:** POST body must be {regulationUrl:'/AdminCode/title{T}/{reg}'} with no part segment; '/AdminCode/title7/1100/1102' returns all-null JSON (no error) — that means a wrong path, not a missing regulation. Take the path from the title listing's publicSiteRegulationUniqueUrl.
- **Probe:** 14 DE Admin. Code 101 → `https://regulations.delaware.gov/api/file/download/d3e6e76e-8b82-4f26-b6eb-a74d0b57c6fe` — expect: "The purpose of this regulation is to outline the procedures,"
- **Evidence (2026-10-16):** curl POST /api/AdminCode/regulation → 200 JSON, regulationName '101 State Assessment System', pdfId d3e6e76e…; GET PDF 200 application/pdf 9 pp; WebFetch of PDF: 1.1 body present, not truncated. | Independent check 2026-10-16: 1.1 'The purpose of this regulation is to outline the procedures,'; 9 pp not truncated; second citation 7 DE Admin. Code 1102 ok
- **Notes:** pdfId may change when a regulation is amended; never store it — look it up each time.

### `de-admincode-lii` — Cornell LII — Delaware Administrative Code

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Legal Information Institute, Cornell Law School · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Admin Code titles (index shows 20 titles; some numbers absent), per-section pages with register history notes.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://www.law.cornell.edu/regulations/delaware/{title}-Del-Admin-Code-SS-{regulation}-{section}`
  - Placeholders: section = top-level section with '.0' (101-1.0, 101-2.0). Subsections (1.1) live on the X.0 page. Browse: /regulations/delaware/title-{title}/{part_hundreds}/{regulation} (e.g. title-14/100/101).
  - Index: `https://www.law.cornell.edu/regulations/delaware`
- **Automation:** WebFetch ok · shell ok · robots: Crawl-delay: 10; disallows /search/, /user/, admin paths; /regulations allowed
  - Respect 10-second crawl delay.
- **Currency:** page header and Notes — observed: "State regulations are updated quarterly; Notes '28 DE Reg. 220 (9/1/2024) (Final)'"
- **Official status:** Third-party mirror; 'State regulations are updated quarterly'.
- **Hazard:** quarterly lag
- **Hazard:** Cornell index lists only some titles
- **Hazard:** LII notes can omit recent Register amendments (7 Del. Admin. Code 1102 showed only 06/11/2006 while the official PDF cites 26 DE Reg. 118 (08/01/22)); compare the latest DE Reg. cite with de-admincode-api before quoting.
- **Probe:** 14 Del. Admin. Code § 101-1.0 → `https://www.law.cornell.edu/regulations/delaware/14-Del-Admin-Code-SS-101-1.0` — expect: "The purpose of this regulation is to outline the procedures,"
- **Evidence (2026-10-16):** WebFetch: 1.1 body present; currency string and register note recorded. Note: /14-Del-Admin-Code-SS-101 (no section) returns the top-level index, not a 404. | Independent check 2026-10-16: 'The purpose of this regulation is to outline the procedures,'; 'State regulations are updated quarterly'; second citation 7 Del. Admin. Code § 1102-1.0 ok
- **Notes:** Being WebFetch-readable without POST, LII is the practical second-fetch source for Admin Code quotes.

## D. Administrative register

### `de-register-api` — Delaware Register of Regulations

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Delaware Registrar of Regulations · text: **fetch-and-quote** · official: unknown
- **Coverage:** Monthly issues Vol. 1 (July 1997) to Vol. 30 Issue 4 (October 2026); PDF and text file per issue.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `index-anchored` · format pdf
  - Pattern: `https://regulations.delaware.gov/api/file/download/{pdfFileId}`
  - Placeholders: GET https://regulations.delaware.gov/api/register/monthlyRegister → JSON array of volumes → issues[] with registerName, relativeUrlPath (e.g. October2026), pdfFileId, textFileId. Volume = DE Reg. volume; locate the issue by month, then the page within the PDF.
  - Index: `https://regulations.delaware.gov/api/register/monthlyRegister`
  - Navigation: shell: GET monthlyRegister JSON → pdfFileId → WebFetch/curl the PDF
- **Automation:** WebFetch ok · shell ok · robots: none
  - WebFetch of the monthlyRegister JSON (107 KB) truncates mid-array (reached only Vol. 19) — use the shell for the JSON. WebFetch of an issue PDF truncates near p. 209 of 239. RSS: GET /api/register/regs-rss.xml (application/xml).
- **Currency:** issue PDF running header — observed: "DELAWARE REGISTER OF REGULATIONS, VOL. 30, ISSUE 4, THURSDAY, OCTOBER 1, 2026"
- **Official status:** Official state publication; no statement on the PDF about online official status.
- **Hazard:** SPA front-end
- **Hazard:** long issue PDFs truncate in WebFetch
- **Hazard:** JSON index too big for WebFetch
- **Hazard:** WebFetch extracts only ~123K characters of an issue PDF and offsets cannot go further (28 DE Reg. 220 unreachable); use shell pdftotext. Issue PDFs begin mid-volume, so register page ≠ PDF page.
- **Probe:** 30 DE Reg. (October 2026 issue) → `https://regulations.delaware.gov/api/file/download/458675cb-fefa-4292-b134-6487303cda9d` — expect: "DELAWARE REGISTER OF REGULATIONS, VOL. 30, ISSUE 4"
- **Evidence (2026-10-16):** curl monthlyRegister 200 JSON, 30 volumes; WebFetch of Oct 2026 PDF: header matches, truncated ~p. 209/239. | Independent check 2026-10-16: 'DELAWARE REGISTER OF REGULATIONS, VOL. 30, ISSUE 4, THURSDAY, OCTOBER 1, 2026'; truncated ~p.209; second citation 28 DE Reg. 220 (9/1/2024) FAILED by WebFetch (see hazards)

## E. Case law

### `de-opinions-courts` — Delaware Courts — Opinions and Orders database

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Delaware Judiciary (Administrative Office of the Courts) · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court from 1998 (1998: 18 items; 2000: 445; 2025: 506); Court of Chancery from 2000 (none in 1998-1999; 2000: 107; 2025: 337); Superior Court from 2000 (2001: 478); Court of Common Pleas sparse early (2001: 3; 2005: 85); Family Court sparse (2015: 3; 2025: 45). Year selector offers 1983-2026 but pre-1998 years return nothing. Includes Supreme Court orders (affirmances by order) as well as opinions.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `constructible` · format pdf
  - Pattern: `https://courts.delaware.gov/opinions/index.aspx?ag={court}&period=year&year={YYYY}&results=25&ss={search}&page=1`
  - Placeholders: Search by GET (verified by WebFetch and shell 2026-10-16): https://courts.delaware.gov/opinions/index.aspx?ag={court}&period=year&year={YYYY}&results=25&ss={search}&page=1 — court = 'Supreme Court' | 'Court of Chancery' | 'Superior Court' | 'Family Court' | 'Court of Common Pleas' | 'All Courts' (URL-encode spaces); search is a substring match on party name or docket and is limited to the chosen year. Rows give case name, date, docket (Supreme 'N, YYYY'; Chancery 'C.A. No. YYYY-NNNN-XXX'), court below, judge, and the download id; the PDF is https://courts.delaware.gov/opinions/download.aspx?id={id}. The id is not derivable — take it from the result row. The ASP.NET POST form also works but is unnecessary.
  - Index: `https://courts.delaware.gov/opinions/index.aspx`
  - Navigation: GET search URL → result row → download.aspx?id={id} PDF
- **Automation:** WebFetch ok · shell ok · robots: User-agent * — Disallow ~10 specific /opinions/download.aspx?ID=… documents (144670, 135640, 80280, 160340, 213920, 71240, 206330, 203680, 237150) plus /_declt; check each id against this list before fetching
  - Occasional 'Connection reset by peer' from the shell; a single retry succeeded.
- **Currency:** none stated; listing updated daily (newest item dated 10/16/2026)
- **Official status:** Slip opinions; Supr. Ct. R. 14(g) requires citation to A.2d/A.3d for reported cases, so these PDFs are not the official reported text.
- **Hazard:** slip pagination only — no A.3d page numbers
- **Hazard:** search is POST-only with ASP.NET viewstate
- **Hazard:** lower-court C.A. No. search does not find the Supreme Court appeal (Supreme rows carry their own docket)
- **Hazard:** robots disallows specific opinion ids
- **Hazard:** Family Court / CCP coverage sparse
- **Probe:** Moelis & Co. v. West Palm Beach Firefighters' Pension Fund, No. 340, 2024 (Del. Jan. 20, 2026) → `https://courts.delaware.gov/opinions/download.aspx?id=390230` — expect: "TRAYNOR, Justice: In the Court of Chancery, a stockholder sought a declaratory judgment"
- **Evidence (2026-10-16):** POST search (Supreme Court, 2026, 'Moelis') → 1 row id 390230, '340, 2024', '(Court of Chancery)'. curl: application/pdf '340, 2024 final opinion.pdf', 45 pp. WebFetch: body present, not truncated, no reporter cite, slip pagination. Chancery probe: id 402240 (C.A. No. 2026-0508-JTL) 30 pp PDF, body begins 'LASTER, V.C.' | Independent check 2026-10-16: 'TRAYNOR, Justice: In the Court of Chancery, a stockholder sought a declaratory judgment'; 45 pp, no A.3d; second citation Techno-X USA Inc. v. Spartan Forge LLC, C.A. No. 2024-1313-LWW (Del. Ch. Oct. 15, 2026) ok
- **Notes:** The 45-page Moelis opinion fit in one WebFetch window; very long Chancery post-trial opinions (100+ pp) will exceed it — use offset or shell pdftotext.

### `de-cases-justia` — Justia — Delaware case law

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 2** · Justia · text: **fetch-and-quote** · official: unofficial
- **Coverage:** Supreme Court 1793-2026; Court of Chancery 1950-2026; Superior Court, Court of Common Pleas, Court on the Judiciary, Court of Errors and Appeals (ranges not checked). No Family Court listing.
- **Read via (in order):** **fetch tool**
- **Access:** `constructible` · format html
  - Pattern: `https://law.justia.com/cases/delaware/{court-slug}/{year}/{docket-slug}.html`
  - Placeholders: court-slug: supreme-court | court-of-chancery | superior-court | court-of-common-pleas. year = decision year. Supreme Court docket 'No. 340, 2024' → '340-2024'. Chancery 'C.A. No. 2023-0309-JTL' → 'c-a-no-2023-0309-jtl' OR '2023-0309-jtl' (both forms occur — check the year listing https://law.justia.com/cases/delaware/{court-slug}/{year}/ if the first guess 404s). Multiple decisions on one docket may get suffixed slugs (unverified).
  - Index: `https://law.justia.com/cases/delaware/`
  - Navigation: year listing page lists every decision with link
- **Automation:** WebFetch ok · shell blocked-challenge · robots: unreadable (403 Cloudflare challenge)
  - Shell: HTTP 403, cf-mitigated: challenge. WebFetch only.
- **Currency:** none
- **Official status:** Justia notes AI-assisted metadata/summaries 'can produce inaccuracies'.
- **Hazard:** docket-slug variants
- **Hazard:** shell blocked
- **Hazard:** slip text, no reporter pagination
- **Probe:** Moelis & Co. v. West Palm Beach Firefighters' Pension Fund, No. 340, 2024 (Del. 2026) → `https://law.justia.com/cases/delaware/supreme-court/2026/340-2024.html` — expect: "In the Court of Chancery, a stockholder sought a declaratory judgment that"
- **Evidence (2026-10-16):** WebFetch: body present, complete through fn. 111. Chancery: /court-of-chancery/2024/c-a-no-2023-0309-jtl.html → West Palm Beach v. Moelis (Feb. 12, 2024), body present. | Independent check 2026-10-16: 'In the Court of Chancery, a stockholder sought a declaratory judgment that'; complete; second citation Techno-X USA Inc. v. Spartan Forge LLC, C.A. No. 2024-1313-LWW (Del. Ch. 2026); also Turner v. Lam Research, No. 149, 2026 ok
- **Notes:** Justia's 2024 c-a-no-2023-0309-jtl page served the Feb. 12 opinion; the Feb. 23 opinion on the same docket must use a different slug — find it via the year listing.

## F. Subsequent history

### `de-subsequent-history-supreme` — Delaware Supreme Court appeals in the Opinions and Orders database

- **Status:** VERIFIED 2026-10-16 (independent) · **Tier 1** · Delaware Judiciary · text: **fetch-and-quote** · official: unofficial
- **Coverage:** The Delaware Supreme Court is the only appellate court (no intermediate court; Chancery and Superior appeals go directly to it as of right). Affirmances by order and opinions both appear in the opinions database with a '(Court of Chancery)' / '(Superior Court)' court-below tag. US Supreme Court certiorari is the only further review.
- **Read via (in order):** **script** → **fetch tool**
- **Access:** `search-only` · format pdf
  - Pattern: `https://courts.delaware.gov/opinions/index.aspx?ag={court}&period=year&year={YYYY}&results=25&ss={search}&page=1`
  - Placeholders: Search by GET (verified by WebFetch and shell 2026-10-16): https://courts.delaware.gov/opinions/index.aspx?ag={court}&period=year&year={YYYY}&results=25&ss={search}&page=1 — court = 'Supreme Court' | 'Court of Chancery' | 'Superior Court' | 'Family Court' | 'Court of Common Pleas' | 'All Courts' (URL-encode spaces); search is a substring match on party name or docket and is limited to the chosen year. Rows give case name, date, docket (Supreme 'N, YYYY'; Chancery 'C.A. No. YYYY-NNNN-XXX'), court below, judge, and the download id; the PDF is https://courts.delaware.gov/opinions/download.aspx?id={id}. The id is not derivable — take it from the result row. Searching a trial-court C.A. number does not find the Supreme Court appeal: search the party name in the Supreme Court for the year(s) after the trial decision; the order/opinion names the court below and its C.A. No. Substring search also returns unrelated parties sharing a word — confirm the C.A. No. in the PDF.
  - Index: `https://courts.delaware.gov/opinions/index.aspx`
  - Navigation: GET search URL → result row → download.aspx?id={id} PDF
- **Automation:** WebFetch ok · shell ok · robots: see de-opinions-courts
- **Currency:** none stated
- **Official status:** Slip opinions and orders.
- **Hazard:** party-name search only; parties often reversed on appeal (appellant first)
- **Hazard:** docket search on lower C.A. No. fails
- **Hazard:** Justia lists only opinions/orders it has ingested
- **Probe:** West Palm Beach Firefighters' Pension Fund v. Moelis & Co., C.A. No. 2023-0309-JTL (Del. Ch. 2024) → appeal No. 340, 2024 → `https://courts.delaware.gov/opinions/download.aspx?id=390230` — expect: "Upon appeal from the Court of Chancery. REVERSED."
- **Evidence (2026-10-16):** Chancery 2024 search 'Moelis' → ids 360460 (2/23/2024) and 360010 (2/12/2024), C.A. No. 2023-0309-JTL; Supreme 2026 search 'Moelis' → id 390230, '340, 2024', '(Court of Chancery)'; PDF caption 'Court Below: Court of Chancery … C.A. No. 2023-0309', 'REVERSED'. | Independent check 2026-10-16: Caption 'Upon appeal from the Court of Chancery. REVERSED.' present in id=390230; second citation Turner v. Lam Research Corp., C.A. No. 2024-1308 (Del. Ch.) -> No. 149, 2026 ok
- **Notes:** Delaware also accepts certified questions (Supr. Ct. R. 41) and interlocutory appeals (Supr. Ct. R. 42); both are decided by the Supreme Court and appear in the same database. Interlocutory-appeal refusals are issued as orders.

## Not available (do not look for these again)

- **statutes** — public.law edition of the Delaware Code: public.law home page lists only CA, CO, FL, NV, NY, OR, TX; delaware.public.law fails at the proxy (CONNECT 502). (2026-10-16)
- **statutes** — Cornell LII Delaware Code / Constitution / opinions: https://www.law.cornell.edu/states/delaware links out to delcode.delaware.gov and courts.delaware.gov; LII hosts only the Delaware Administrative Code. (2026-10-16)
- **case_law** — Free official reporter (A.3d) pagination for Delaware opinions: Court PDFs carry slip pagination only (Moelis: no A.3d cite); Supr. Ct. R. 14(g) cites A.2d/A.3d, which are West reporters. (2026-10-16)
- **case_law** — courts.delaware.gov opinions before 1998 (Supreme) / 2000 (Chancery, Superior): POST search by year: Supreme 1998 is the earliest year with rows (18; 1999: 2; a 1995 request fell back to current-year rows); Chancery 1998 and 1999 returned 0 rows, 2000 returned 107. (2026-10-16)
- **case_law** — Public-domain (vendor-neutral) citation format: Supr. Ct. R. 14(g) specifies Bluebook / WL / LEXIS / Fastcase / docket forms only. (2026-10-16)

## Open questions

- Superior Court Criminal Rules and Lawyers' Rules of Professional Conduct PDFs not WebFetch-probed (reported only).
- Exact Del. Laws volume ↔ legis.delaware.gov 'Chapters?volume=' parameter mapping not established (probe showed volume=42 for a 66 Del. Laws chapter).
- Justia Chancery slug for a second decision on the same docket (e.g. Moelis Feb. 23, 2024) not determined.
- CourtListener court ids (del, delch, delsuperct, delfamct, delctcompl, deljudct) unverified.
- Whether the regulations.delaware.gov SPA honours any robots policy: /robots.txt returns the SPA HTML (no real file).
