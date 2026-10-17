# Upgrading the deep-legal-research skill

This folder always holds the newest release of the skill:

| File | What it is |
|---|---|
| `latest.json` | Version, release date, summary, sha256 and file list. The skill checks this file. |
| `deep-legal-research.zip` | The newest release, **minus the GovInfo API key** (see below). |

## How you'll hear about a new version

At the start of every research run, the skill (v10.4 and later) runs
`scripts/update_check.py`. When this folder holds a newer version than the
one you have installed, the skill does three things:

1. It hands you a file named `deep-legal-research-v<X.Y>.zip`. That file is
   ready to upload, with your GovInfo key already copied in from your
   current installation.
2. It lists the steps below.
3. It carries on with your research on the version you have.

## Steps

1. Download the zip the skill gave you.
2. In Claude, open **Customize → Skills**.
3. Find **deep-legal-research**, switch it off, click the **…** next to the
   toggle, choose **Delete** and confirm. An uploaded skill can't be
   replaced in place.
4. Click **+**, then **+ Create skill**, then **Upload a skill**, and choose
   the downloaded zip.
5. Switch the new skill on and start a new chat.

**Team / Enterprise.** If your organization provisions this skill for you,
send the zip to your Claude organization owner instead. They publish the
new version for everyone.

Source: Claude Help Center, [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
and [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills),
read 2026-10-17.

## Why the public zip has no API key

The skill bundles an api.data.gov key (`scripts/govinfo.key`) for GovInfo.
The key may be shared with colleagues but must never be posted publicly, and
this repository is public. So:

- `scripts/release_skill.py` leaves the key out of
  `deep-legal-research.zip` and lists it in `latest.json` under
  `preserve_local`.
- The update check copies the key from your installed skill into the zip it
  hands you.

**Do not upload `deep-legal-research.zip` from this folder directly.** It has
no key, so GovInfo lookups would fail. For a **first** install, get the full
zip from a colleague who already has the skill.

## Publishing a new release (maintainer)

1. Finish the release in a copy of the complete skill folder, including the
   skill's own checklist in `CHANGELOG.md`.
2. From the repo root, run:
   `python3 scripts/release_skill.py <path-to>/deep-legal-research --summary "one line"`
3. Commit `skill/latest.json` and `skill/deep-legal-research.zip`, then
   push to `main`.

The script refuses to publish if:
- the version isn't higher than the one already published;
- a file from the previous release is missing;
- a remaining file looks like it holds a credential.
