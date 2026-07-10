# GitHub Profile Release Checklist

**Status:** MOTION BRANCH AUTOMATED GATES PENDING, MANUAL RENDER AND FINAL APPROVAL OPEN  
**Release surface:** `kanadhiayash/kanadhiayash` profile README  
**Quality gate:** `.github/workflows/profile-quality.yml`

## Release rule

Do not merge or call the Living Product Console motion layer released until every automated and remaining manual blocking item is complete.

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

The following files must remain under the locked path:

```text
assets/hero/yash-kanadhia-living-product-console-dark-motion.svg
assets/hero/yash-kanadhia-living-product-console-dark.png
assets/hero/yash-kanadhia-living-product-console-dark.jpg
assets/hero/yash-kanadhia-living-product-console-dark.svg
```

The animated SVG is the primary README asset. The PNG is the directly accessible static alternative.

Required motion checks:

- The animated SVG contains an SVG root and `role="img"`.
- The SVG has a title and description.
- Motion remains slow and ambient.
- No rapid flashing, hard strobing, or large jumps are present.
- No claim or project fact exists only in motion.
- The README references the animated SVG once.
- The README references the static PNG once inside the accessible alternative.
- Both hero references contain descriptive alt text identifying:
  - Yash Kanadhia
  - Product Designer
  - Zeref Memory Engine
  - PerFin OS
  - MADS team project

Required static checks:

- PNG dimensions are at least 1600 by 700 pixels.
- The PNG uses the approved wide aspect ratio.
- The JPG has a valid JPEG signature.
- The static SVG wrapper contains an SVG root and `role="img"`.

## Previously verified automated status

### PASS: profile foundation

- Code and configuration whitespace passed.
- All profile scripts compiled.
- The dynamic updater passed its structural checks.
- Locked copy, attribution, metrics, credentials, tools, local assets, anchors, alt text, placeholders, private paths, and secret-pattern checks passed.

### PASS: release readiness

- The approved static hero bundle is present under `assets/hero/`.
- The static hero dimensions and aspect ratio passed.
- The superseded banner files were removed.

### PASS: online link gate

- The definitive external-link scan passed.
- The unpublished Zeref GitHub Release URL was replaced with the verified `docs/RELEASE_LOG.md` record.
- LinkedIn and Substack access restrictions remain warnings because those public profile pages do not provide reliable automated HEAD or unauthenticated GET responses.
- The workflow publishes `profile-link-report` as a review artifact.

## Motion-branch verification

After the motion pull request runs:

- [ ] Profile foundation passes.
- [ ] Release readiness passes.
- [ ] Online link gate passes.
- [ ] Animated SVG resolves through GitHub.
- [ ] Static PNG alternative resolves through GitHub.
- [ ] No locked title, metric, tool, credential, attribution, or dynamic-marker value drifts.

## Remaining manual blocking checks

Review the rendered README in GitHub:

- [ ] Desktop width in GitHub light appearance.
- [ ] Desktop width in GitHub dark appearance.
- [ ] Narrow mobile width.
- [ ] The SVG animation actually plays through GitHub or its image proxy.
- [ ] The scan, pulses, orbit, and lower signal remain subtle.
- [ ] No motion flashes or distracts from the profile content.
- [ ] Name, title, location, and tagline remain readable.
- [ ] Hero metrics and tool labels remain legible without zooming.
- [ ] Zeref and PerFin remain visually dominant.
- [ ] PerFin is visibly identified as a team project.
- [ ] The expandable static hero renders correctly.
- [ ] All three project media boards render without clipping.
- [ ] Dynamic modules do not overpower selected work.
- [ ] The page remains understandable when images fail to load because alt text and written project sections remain complete.

## Dynamic-module operational check

1. Run **Profile Refresh** manually from GitHub Actions.
2. Confirm it creates or updates `automation/profile-refresh` only when content changes.
3. Review the generated pull request.
4. Confirm changes stay inside the two marker regions.
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
Automated quality gate: PENDING
Online link gate: PENDING
GitHub light motion render: BLOCKED
GitHub dark motion render: BLOCKED
Mobile motion render: BLOCKED
Static alternative render: BLOCKED
Profile Refresh review PR: BLOCKED
Final public-claim review: BLOCKED
Approved by: ____________________
Approval date: __________________
Release commit: _________________
```

## Non-blocking enhancement backlog

These items improve the portfolio but do not block the Living Product Console motion release:

- Zeref product demonstration loop beyond the profile hero, with a still equivalent.
- Verified PerFin OS screenshots and workflow recording.
- Verified For Rent renter and landlord captures.
- Verified StreamNexus runtime captures.
- Approved Arthenticate and DriveDeal prototype media.

Do not describe the profile as media-complete until that enhancement backlog is finished.
