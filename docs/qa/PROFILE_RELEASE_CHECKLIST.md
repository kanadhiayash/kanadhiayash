# GitHub Profile Release Checklist

**Status:** MOTION BRANCH AUTOMATED GATES PASS, MANUAL RENDER AND FINAL APPROVAL OPEN  
**Release surface:** `kanadhiayash/kanadhiayash` profile README  
**Quality gate:** `.github/workflows/profile-quality.yml`

## Release rule

Do not merge or call the Living Product Console motion layer released until every remaining manual blocking item is complete.

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

## Required motion and static pairs

The following files must remain under the locked paths:

```text
assets/hero/yash-kanadhia-living-product-console-dark-motion.svg
assets/hero/yash-kanadhia-living-product-console-dark.png
assets/projects/flagship-systems-motion.svg
assets/projects/flagship-systems.svg
assets/projects/built-product-proof-motion.svg
assets/projects/built-product-proof.svg
assets/projects/product-design-studies-motion.svg
assets/projects/product-design-studies.svg
```

The animated SVGs are the primary README visuals. Their paired static assets are directly accessible through collapsed alternatives.

Required motion checks:

- Each animated SVG contains an SVG root and `role="img"`.
- Each animated SVG has a title and description.
- Motion remains slow and ambient.
- No rapid flashing, hard strobing, or large jumps are present.
- No claim or project fact exists only in motion.
- The README references each motion asset exactly once.
- The README references each static alternative exactly once.
- Each static alternative follows its motion asset.
- The README order remains hero, flagship systems, built product proof, product design studies.
- Alt text preserves role, project, attribution, and limitation context.

Required static checks:

- Hero PNG dimensions are at least 1600 by 700 pixels.
- The hero PNG uses the approved wide aspect ratio.
- The hero JPG has a valid JPEG signature.
- The static SVG files contain SVG roots and image roles.

## Verified automated status

### PASS: profile foundation

- Code and configuration whitespace passed.
- All profile scripts compiled.
- The dynamic updater passed its structural checks.
- The motion validator passed all four motion surfaces and all four static alternatives.
- Locked copy, attribution, metrics, credentials, tools, local assets, anchors, alt text, placeholders, private paths, and secret-pattern checks passed.

### PASS: release readiness

- The complete hero bundle remains present under `assets/hero/`.
- The hero dimensions and aspect ratio passed.
- The motion and static README references passed.
- The superseded banner files remain removed.

### PASS: online link gate

- The definitive external-link scan passed.
- The unpublished Zeref GitHub Release URL remains replaced by the verified `docs/RELEASE_LOG.md` record.
- LinkedIn and Substack access restrictions remain warnings because those public profile pages do not provide reliable automated HEAD or unauthenticated GET responses.
- The workflow publishes `profile-link-report` as a review artifact.

## Motion-branch verification

- [x] Profile foundation passes.
- [x] Motion consistency gate passes.
- [x] Release readiness passes.
- [x] Online link gate passes.
- [x] All four animated SVG files resolve as local repository assets.
- [x] All four static alternatives resolve as local repository assets.
- [x] No locked title, metric, tool, credential, attribution, or dynamic-marker value drifted.

## Remaining manual blocking checks

Review the rendered README in GitHub:

- [ ] Desktop width in GitHub light appearance.
- [ ] Desktop width in GitHub dark appearance.
- [ ] Narrow mobile width.
- [ ] The SVG animations actually play through GitHub or its image proxy.
- [ ] The scan, pulses, orbit, and lower signals remain subtle.
- [ ] No motion flashes or distracts from the profile content.
- [ ] Name, title, location, and tagline remain readable.
- [ ] Hero metrics and tool labels remain legible without zooming.
- [ ] Zeref and PerFin remain visually dominant.
- [ ] PerFin is visibly identified as a team project.
- [ ] All four expandable static alternatives render correctly.
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
python3 -m py_compile scripts/validate_profile_motion.py
python3 scripts/update_dynamic_modules.py --check
python3 scripts/validate_profile_motion.py
python3 scripts/validate_profile_foundation.py
python3 scripts/validate_profile_release.py
python3 scripts/validate_profile_links.py
git diff --check
```

## Release approval record

```text
Automated quality gate: PASS
Motion consistency gate: PASS
Online link gate: PASS
GitHub light motion render: BLOCKED
GitHub dark motion render: BLOCKED
Mobile motion render: BLOCKED
Static alternatives render: BLOCKED
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
