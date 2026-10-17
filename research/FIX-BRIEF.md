# Fix brief: apply an independent check to your record

A separate agent checked your jurisdiction cold, working only from the
generated instructions. Its results are in `research/<xx>-verify.json`. The
repo root is `/home/claude/deep-legal-research-resources`.

## For each row in the verify file

**`confirmed` or `discrepancy`, on a row that is `verified` in your record:**
- Apply the `suggested_fix` and the `instruction_problems` to the record.
  That covers patterns, navigation, hazards, probe `expect` strings and
  currency strings.
- Set `verification.by` to `"independent"` and `verification.date` to today.
- Append to `verification.evidence`:
  ` | Independent check <date>: <probe_evidence>; second citation <generalised_citation> ok`.
  Leave out the second-citation part if `generalised_outcome` isn't `ok`.
- If the second citation **failed**, the row stays `verified`, but add a
  hazard describing the failure.

**`failed`:**
- If the source really doesn't work as recorded, downgrade it to `reported`
  and add a hazard plus an `open_questions` entry.
- If the instructions were just wrong, fix them. Leave `by` as `"research"`
  until someone re-checks the row.

**`still-blocked`:**
- Append ` | Re-confirmed blocked <date>: …` to the evidence.

**`unblocked`:**
- Don't promote the row. Add an `open_questions` entry and leave it blocked
  until a deliberate re-research.

## Regex tests

For every `regex_tests` entry where `matched_label` is not the expected label:
- **A miss:** extend the regex and add the citation to that pattern's
  `examples`.
- **A false route:** tighten the regex (for example with a negative
  lookbehind for another state's prefix) and note it in
  `citation_map.notes`.

Then run `python3 scripts/build.py --check`. It must print **no ERROR and no
WARN lines for `<xx>.json`**. Use `--check` only, never a full build.

## Finish

Edit only `data/<xx>.json`. Your final message must be 60 words or fewer:
- rows marked independent;
- rows downgraded;
- regex fixes made.
