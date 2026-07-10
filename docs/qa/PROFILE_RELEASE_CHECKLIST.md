# GitHub Profile Release Checklist

**Status:** AUTOMATED GATES PASS, MANUAL RENDER AND FINAL APPROVAL OPEN  
**Release surface:** `kanadhiayash/kanadhiayash` profile README  
**Quality gate:** `.github/workflows/profile-quality.yml`

## Release rule

Do not merge or call the Living Product Console released until every remaining manual blocking item is complete.

## Automated blocking checks

The release validator checks:

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

The following files are present under the locked path:

```text
assets/hero/yash-kanadhia-living-product-console-dark.png
assets/hero/yash-kanadhia-living-product-console-dark.jpg
assets/hero/yash-kanadhia-living-product-console-dark.svg
```

The PNG is the primary README asset.

Verified requirements:

- PNG dimensions are at least 1600 by 700 pixels.
- The PNG uses the approved wide aspect ratio.
- The JPG has a valid JPEG signature.
- The SVG wrapper contains an SVG root and `role="img"`.
- `README.md` references the approved PNG once.
- Hero alt text identifies:
  - Yash Kanadhia
  - Product Designer
  - Zeref Memory Engine
  - PerFin OS
  - MADS team project

## Current automated status

### PASS: profile foundation

- Code and configuration whitespace passed.
- All profile scripts compiled.
- The dynamic updater passed its structural checks.
- Locked copy, attribution, metrics, credentials, tools, local assets, anchors, alt text, placeholders, private paths, and secret-pattern checks passed.

### PASS: release readiness

- The approved hero bundle is present under `assets/hero/`.
- The README hero reference and descriptive alt text passed.
- The approved hero dimensions and aspect ratio passed.
- The superseded banner files were removed from the Phase 5 branch.

### PASS: online link gate

- The definitive external-link scan passed.
- The unpublished Zeref GitHub Release URL was replaced with the verified `docs/RELEASE_LOG.md` record.
- LinkedIn and Substack access restrictions remain warnings because those public profile pages do not provide reliable automated HEAD or unauthenticated GET responses.
- The workflow publishes `profile-link-report` as a review artifact.

## Remaining manual blocking checks

Review the rendered README in GitHub:

- [ ] Desktop width in GitHub light appearance.
- [ ] Desktop width in GitHub dark appearance.
- [ ] Narrow mobile width.
- [ ] Name, title, location, and tagline remain readable.
- [ ] Hero metrics and tool labels remain legible without zooming.
- [ ] Zeref and PerFin remain visually dominant.
- [ ] PerFin is visibly identified as a team project.
- [ ] All three project media boards render without clipping.
- [ ] Dynamic modules do not overpower selected work.
- [ ] The page remains understandable when images fail to load because alt text and written project sections remain complete.

## Dynamic-module operational check

After Phase 5 is merged:

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
python3 -m py_compile scripts/validate_profile_foundation.py
python3 -m py_compile scripts/validate_profile_links.py
python3 scripts/update_dynamic_modules.py --check
python3 scripts/validate_profile_foundation.py
python3 scripts/validate_profile_release.py
python3 scripts/validate_profile_links.py
git diff --check
```

## Release approval record

```text
Automated quality gate: PASS
Online link gate: PASS
GitHub light render: BLOCKED
GitHub dark render: BLOCKED
Mobile render: BLOCKED
Profile Refresh review PR: BLOCKED
Final public-claim review: BLOCKED
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
