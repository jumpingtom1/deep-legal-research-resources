# Research brief: one jurisdiction, families A–G (v2, after the CA/DE/NY pilot)

You are compiling the free-source record for ONE US jurisdiction for the
`deep-legal-research` skill. The repo root is
`/home/claude/deep-legal-research-resources`, and all paths below are relative
to it.

Read these first:
- `SCHEMA.md`
- `data/de.json`, as a worked example of a finished record. Look at its
  shape, `access.navigation` / `pattern_rules`, `hazards`, `law_aliases` and
  its prose citation regexes. Don't copy its content.

## Deliverables

1. `data/<xx>.json`: the record, valid JSON with no comments, conforming to
   `SCHEMA.md`.
2. `research/<xx>-log.md`: the probe log. List every URL you fetched, the tool
   used, the date, and what came back (HTTP code, first words, refusal
   message). Keep quoted page text to 15 words or fewer per entry.
3. Run `python3 scripts/build.py --check`. It must print **no ERROR and no
   WARN lines for `<xx>.json`**. Then run `python3 scripts/build.py --cross`:
   it must print **no CROSS line that starts with `<xx>:` or names `<xx>` as
   the matching state**. Fix it one of two ways: give distinctive patterns
   this state's marker ("Tex.", "of the Ohio Rules …"), or mark a genuinely
   generic form (bare "Rule 1:1", bare docket number, regional reporter,
   "cert. denied") with `"context_required": true`.
  **Never drop or reword one of your own real citation examples to clear a
  CROSS line.** If another state's pattern claims your citation, the fix
  belongs in that state's pattern. Leave your example as it is and name the
  conflict in your final message. Use `--check` only: other agents are
   building in parallel, so never run `build.py` without it.

## What the skill needs from each source

The skill quotes statutes and rules only after two independent fetches agree.
It verifies quotes from opinions, and it cites official page numbers where it
can. So for every source, answer these questions:

- **Can a citation be turned into a URL deterministically?** Prove it on at
  least two real citations from different codes or titles. If it can't, write
  `navigation` as exact hops. Say whether the index pages show section ranges;
  the pilot found indexes that don't, which forced guessing.
- **Does the fetch tool (WebFetch) return the body text**, not a table of
  contents or a JavaScript shell? For long pages and PDFs, record where the
  text stops (the tool keeps about 100K characters). Every such document is a
  **`corpus_candidates`** entry.
- **Does the script route work?** Test it with
  `python3 scripts/fetch_doc.py --research info <url>`, then `grep` or
  `verify` against it. Set `automation.shell` from what it reports:
  - `ok`
  - REFUSED by robots → `blocked-robots`
  - REFUSED by challenge or 403 → `blocked-challenge`
  - TLS certificate failure → `tls-error`
  - other failures → `http-error`

  It obeys robots.txt and bot checks for you. **Never** use curl or anything
  else to get around a refusal.
- **Currency.** Record the literal edition or "current through" string, and
  where on the page it appears.
- **Official status.** Look for the publisher's disclaimer, or a UELMA
  authentication statement.
- **Case law:**
  - coverage years;
  - HTML or PDF;
  - official reporter pagination vs. slip pagination;
  - how to find an opinion from (court, docket, date): a listing page, or a
    search that works as a **plain GET URL** (test this; the pilot found a
    "POST-only" form that also accepted GET);
  - any JSON API or bulk download, which goes in `script_candidates`;
  - **public-domain / vendor-neutral citation formats**, if the state has one
    (e.g. `2023 IL 128004`, `2020-Ohio-1234`, `2019 ND 55`).
- **Subsequent history:** where review, leave or cert dispositions are
  published, and how to find them from the decision below. Say plainly if
  they can only be found by party name.
- **Bulk statute data.** Look for an official bulk download or API (XML,
  JSON, zip). Record it in `corpus_candidates[].bulk` or `script_candidates`.

## Citation map: lessons from the pilot (all three states needed fixes)

- **Include prose forms** in `examples` and make the regex match them:
  "section 1714 of the Civil Code", "Article I, Section 9 of the X
  Constitution", "Rule 61 of the Superior Court Criminal Rules".
- **Guard bare code names shared with other states.** "Penal Code",
  "Government Code", "Civil Code" and bare "Rule 12" must not route here
  without this state's prefix or context. Say so in `citation_map.notes`.
- **Section ranges** ("§§ 10001-10007") must not be read as one hyphenated
  section number.
- Add **`law_aliases`** whenever URLs need a code key. Map every common
  abbreviation (Bluebook, the state's own style, practitioner short forms)
  to that key.
- Cover the state's **court-rule citation styles** and **unreported-opinion
  forms**.
- Set `courtlistener_id` from your knowledge, with
  `"courtlistener_id_unverified": true`.

## Rules

- **Tier 1** is official or government sources. **Tier 2** is public.law,
  Justia (law.justia.com) and Cornell LII only. Record tier-2 rows for every
  family where they exist; they are the fallback. Use no other third parties.
- **Follow the robots and refusal policy table in `SCHEMA.md`.** In
  particular, an explicit robots `Disallow` that covers the path means the
  row is `blocked` for **every** route, the fetch tool included.
- **Never work around a block:** robots.txt, a bot challenge, a login, "site
  blocked", or a TLS failure. Record it with its evidence and move on.
- **Do not use any CourtListener tool.**
- **Do not reproduce statute or opinion text** beyond evidence snippets of 15
  words or fewer.
- **WebFetch prompts:** ask narrowly ("Does this page contain the body text of
  section X? Answer YES/NO, then the first 10 words of the body, then any
  currency/edition statement verbatim, then whether the page appears
  truncated"). For long pages, add: "do not infer text from a heading; if the
  body text of X is not actually present, answer exactly NOT PRESENT".
- **WebSearch** is fine for discovery. Confirm every URL by fetching it; a URL
  you didn't fetch is at most `reported`.
- **Budget:** about 55 WebFetch calls. Script-route tests don't count against
  it, but stay polite; the script rate-limits for you.
  - Priority order: A (statutes), E (case law), G (citation map), C (court
    rules), F (subsequent history), B (constitution), D (admin code and
    register).
  - If you run low, record the remaining items as `reported`, each with an
    `open_questions` entry.
- **If WebFetch starts failing for quota or rate reasons** (not a site
  refusal), stop fetching. Finish the record with what you have and say so
  in your final message.
- **WebFetch may need approval for URLs you built yourself.** URLs that came
  from a search result or a fetched page usually go through. A URL built from
  a pattern can wait on a permission prompt or time out, and nobody may be
  there to answer it.
  - Don't retry the call.
  - Verify the row with `python3 scripts/fetch_doc.py --research` instead. A
    script probe that returns the body text is enough to mark the row
    `verified`; record the script output as the evidence.
  - Set `automation.webfetch` to `gated` and add a note.
- **Dates:** today is the date in your environment (2026-10-16 when this
  brief was written). Use it for every `date` field. `verification.by` is
  `"research"`.
- **Files:** don't touch any file except your two deliverables.

## Finish

Your final message must be 150 words or fewer:
- counts of verified, reported, blocked and absent rows;
- the 3 most important findings, especially anything blocked or surprising;
- the corpus candidates;
- any schema field that didn't fit.
