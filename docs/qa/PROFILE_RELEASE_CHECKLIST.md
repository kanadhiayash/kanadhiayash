# GitHub Profile Release Checklist

**Status:** BLOCKED UNTIL HERO ASSET PLACEMENT AND FINAL RENDER REVIEW  
**Release surface:** `kanadhiayash/kanadhiayash` profile README  
**Quality gate:** `.github/workflows/profile-quality.yml`

## Release rule

Do not merge or call the Living Product Console released until every blocking item below is complete.

## Automated blocking checks

The release validator must pass all of these checks:

- `README.md` exists and is valid UTF-8 text.
- Product Designer remains the sole hero title.
- Toronto, Ontario, Canada remains the public location.
- The approved tagline remains unchanged.
- The metric row remains exactly:
  - 2 shipped projects
  - 1 MADS team project
  - 5 selected certifications
- The tool row remains exactly:
  - Figma
  - React
  - Swift
  - Firebase
  - Claude
  - Codex
- Zeref Memory Engine and PerFin OS remain the flagship systems.
- PerFin OS remains credited to Yash Kanadhia, Alexis Gorospe, and Sarmad Tariq.
- The five selected credentials remain present.
- Six Sigma Yellow Belt remains excluded from the GitHub profile.
- The four dynamic-module markers each appear exactly once.
- Every README local image and local link resolves inside the repository.
- Every README image has non-empty alt text.
- Every README internal anchor resolves.
- External links use HTTPS.
- Definitive external 404 and 410 responses block release.
- Temporary rate limits, access restrictions, and network failures produce warnings rather than false release failures.
- README placeholders are absent.
- Public text files contain no detected credentials, private keys, credentialed MongoDB URIs, or private workstation paths.
- The superseded banner is not referenced by the README.

## Required hero bundle

These files are blocking release requirements:

```text
assets/hero/yash-kanadhia-living-product-console-dark.png
assets/hero/yash-kanadhia-living-product-console-dark.jpg
assets/hero/yash-kanadhia-living-product-console-dark.svg
```

The PNG is the primary README asset.

The validator requires:

- PNG dimensions of at least 1600 by 700 pixels.
- A wide aspect ratio between 2.2 and 2.5.
- A valid JPG signature.
- An SVG root with `role="img"`.
- One README reference to the approved PNG.
- Hero alt text that identifies:
  - Yash Kanadhia
  - Product Designer
  - Zeref Memory Engine
  - PerFin OS
  - MADS team project

## Current automated status

### Passing foundations

- Phase 1 positioning and copy are merged.
- Phase 3 static project boards are merged and referenced.
- Phase 4 dynamic markers and updater are merged.
- The dynamic updater compiles and passes its structural checks.
- The project boards have descriptive alt text.
- PerFin OS ownership boundaries remain explicit.

### Blocking findings

- The approved dark hero files are not present under `assets/hero/` in the connector-visible repository.
- `README.md` does not reference the approved hero PNG.
- A manual Profile Refresh workflow run has not yet produced a review pull request.

## Manual render checks

After the hero files are committed and automated checks pass, review the rendered README in GitHub:

- Desktop width in GitHub light appearance.
- Desktop width in GitHub dark appearance.
- Narrow mobile width.
- Name, title, location, and tagline remain readable.
- Hero metrics and tool labels remain legible without zooming.
- Zeref and PerFin remain visually dominant.
- PerFin is visibly identified as a team project.
- All three project media boards render without clipping.
- Dynamic modules do not overpower selected work.
- The page remains understandable when images fail to load because alt text and written project sections remain complete.

## Dynamic-module release check

After Phase 4 is on `main`:

1. Run **Profile Refresh** manually from GitHub Actions.
2. Confirm it creates or updates `automation/profile-refresh` only when content changes.
3. Review the generated pull request.
4. Confirm changes stay inside the two dynamic marker regions.
5. Confirm a failed Substack source preserves the previous reviewed content.
6. Merge the automation pull request only after titles, URLs, dates, attribution, and relevance are verified.

## Local verification commands

```bash
python3 -m py_compile scripts/update_dynamic_modules.py
python3 -m py_compile scripts/validate_profile_release.py
python3 scripts/update_dynamic_modules.py --check
python3 scripts/validate_profile_release.py
python3 scripts/validate_profile_release.py --online
git diff --check
```

## Release approval record

Complete this section only after every gate passes:

```text
Automated quality gate: PASS / BLOCKED
Online link gate: PASS / BLOCKED
GitHub light render: PASS / BLOCKED
GitHub dark render: PASS / BLOCKED
Mobile render: PASS / BLOCKED
Profile Refresh review PR: PASS / BLOCKED
Final public-claim review: PASS / BLOCKED
Approved by: ____________________
Approval date: __________________
Release commit: _________________
```

## Non-blocking enhancement backlog

These items improve the portfolio but do not block the current static release:

- Zeref motion proof with a still equivalent.
- Verified PerFin OS screenshots and workflow recording.
- Verified For Rent renter and landlord captures.
- Verified StreamNexus runtime captures.
- Approved Arthenticate and DriveDeal prototype media.

Do not describe the profile as media-complete until that enhancement backlog is finished.
