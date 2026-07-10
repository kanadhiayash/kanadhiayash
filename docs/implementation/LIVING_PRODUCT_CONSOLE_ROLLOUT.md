# Living Product Console Rollout

**Status:** ACTIVE  
**Decision source:** `docs/decisions/GITHUB_PROFILE_PUBLIC_POSITIONING.md`  
**Current branch:** `feat/profile__quality-gates-release`

This file tracks the controlled rollout of the GitHub profile redesign. Each phase remains reviewable and preserves the locked public positioning decisions.

## Phase 1: Information architecture and copy

**Status:** COMPLETE

Delivered:

- Product Designer remains the sole public title.
- Toronto, Ontario, Canada remains the public location.
- The approved tagline leads the profile.
- Selected work is the primary internal CTA.
- LinkedIn is the primary external CTA.
- Zeref Memory Engine and PerFin OS are the two flagship anchors.
- PerFin OS is credited to Yash Kanadhia, Alexis Gorospe, and Sarmad Tariq.
- For Rent and StreamNexus form the built-product support lane.
- Arthenticate and DriveDeal form the Figma product-design lane.
- Five selected credentials are shown.
- Six Sigma Yellow Belt is excluded.
- The approved tool row is Figma, React, Swift, Firebase, Claude, and Codex.
- Development and AI-assisted execution remain supporting proof.

## Phase 2: Hero visual system

**Status:** COMPLETE, MANUAL RENDER REVIEW OPEN

Locked decisions:

- Use the approved dark Living Product Console hero as the only active banner direction.
- Do not publish a light-mode hero for the current release.
- Use Product Designer as the sole title.
- Show Toronto, Ontario, Canada.
- Show the approved tagline.
- Use exactly these metrics: 2 shipped projects, 1 MADS team project, 5 selected certifications.
- Use only Figma, React, Swift, Firebase, Claude, and Codex in the tool row.
- Keep Zeref Memory Engine and PerFin OS as the dominant visual cards.
- PerFin OS must carry the MADS team project cue and must not imply solo ownership.
- Keep one static hero as the approved baseline before any later motion experiment.

Approved asset stem:

`yash-kanadhia-living-product-console-dark`

Delivered repository files:

- `assets/hero/yash-kanadhia-living-product-console-dark.png`
- `assets/hero/yash-kanadhia-living-product-console-dark.jpg`
- `assets/hero/yash-kanadhia-living-product-console-dark.svg`

Verified:

- The README references the approved PNG.
- Hero alt text identifies the role, flagship systems, and MADS team attribution.
- File signatures, PNG dimensions, and the approved wide aspect ratio pass.
- Superseded banner assets were removed from the Phase 5 branch.

Open manual check:

- Review desktop light appearance, desktop dark appearance, and narrow mobile rendering.

## Phase 3: Project media

**Status:** STATIC RELEASE COMPLETE, VERIFIED CAPTURE ENHANCEMENTS OPEN

Delivered:

- Added `assets/projects/flagship-systems.svg` for Zeref Memory Engine and PerFin OS.
- Added `assets/projects/built-product-proof.svg` for For Rent and StreamNexus.
- Added `assets/projects/product-design-studies.svg` for Arthenticate and DriveDeal.
- Integrated all three boards into the README with descriptive alt text.
- Preserved independent and team ownership boundaries.
- Preserved product limitations and avoided deployment claims.
- Added `docs/media/PROJECT_MEDIA_MANIFEST.md` as the source and replacement policy.
- Avoided StreamNexus placeholder screenshots as final public proof.
- Kept Arthenticate and DriveDeal labeled as interactive Figma studies with public case-study packaging in progress.

Open enhancement backlog:

- Add a short Zeref product-system motion loop with a static equivalent.
- Add verified PerFin OS screenshots and a short workflow recording.
- Add verified For Rent renter and landlord captures.
- Replace StreamNexus repository placeholders with verified runtime captures.
- Add approved Arthenticate and DriveDeal prototype media.

The enhancement backlog does not block the static Phase 3 release. It remains required before claiming a media-complete portfolio.

## Phase 4: Controlled dynamic modules

**Status:** COMPLETE

Delivered:

- Added bounded latest-writing and selected-build-signal regions to `README.md`.
- Added explicit start and end markers for both generated regions.
- Added `data/profile_sources.json` as the reviewed source allowlist.
- Added `scripts/update_dynamic_modules.py` using only the Python standard library.
- Limited writing output to three public Substack entries.
- Limited build output to two signals from Zeref Memory Engine and PerFin OS.
- Added HTTPS and host allowlists for Substack and GitHub.
- Preserved the last reviewed README content when a source fails.
- Added offline marker and configuration validation.
- Added `.github/workflows/profile-refresh.yml` for weekly and manual refreshes.
- Configured automation to open or update `automation/profile-refresh` instead of committing directly to `main`.
- Added `docs/automation/PROFILE_DYNAMIC_MODULES.md` as the operating and review guide.
- Excluded vanity counters, streak cards, random quotes, Spotify widgets, and raw commit feeds.

Post-merge operational check still required:

- Run Profile Refresh manually.
- Review the resulting automation pull request if content changes.
- Confirm generated changes stay inside the two marker regions.
- Confirm a source failure preserves the previous reviewed content.

## Phase 5: Quality gates and release

**Status:** AUTOMATED GATES COMPLETE, MANUAL APPROVAL OPEN

Delivered:

- Added `scripts/validate_profile_release.py` as the deterministic release validator.
- Added `scripts/validate_profile_foundation.py` to verify non-hero release conditions independently.
- Added `scripts/validate_profile_links.py` with GET confirmation for unreliable HEAD responses.
- Added `.github/workflows/profile-quality.yml` as the pull-request, main-branch, and manual quality gate.
- Added `docs/qa/PROFILE_RELEASE_CHECKLIST.md` as the final automated and manual review record.
- Added checks for locked copy, project attribution, selected credentials, approved tools, metrics, and dynamic markers.
- Added checks for local assets, internal anchors, HTTPS links, alt text, placeholders, private paths, and common secret patterns.
- Added hero file, dimension, aspect-ratio, README-reference, and alt-text requirements.
- Added a downloadable `profile-link-report` workflow artifact.
- Replaced the unpublished Zeref GitHub Release URL with the verified repository release record.

Verified automated results:

- Profile foundation: PASS.
- Release readiness: PASS.
- Online link gate: PASS.
- LinkedIn and Substack access restrictions are warnings, not confirmed broken links.

Remaining release blockers:

- GitHub light appearance render review.
- GitHub dark appearance render review.
- Narrow mobile render review.
- Manual Profile Refresh run and review after merge.
- Final public-claim and ownership review.
- Explicit merge approval.

Release decision:

Do not call the profile released until the manual checklist is complete and merge is explicitly approved.

## Current risks

- The approved dark hero is generated raster artwork. The SVG export is a faithful embedded-image wrapper rather than editable vector paths.
- Verified product screenshots and recordings remain an enhancement backlog and must not be represented as already published.
- Substack feed availability still requires a live manual Profile Refresh run.
