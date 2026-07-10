# Living Product Console Rollout

**Status:** ACTIVE  
**Decision source:** `docs/decisions/GITHUB_PROFILE_PUBLIC_POSITIONING.md`  
**Current branch:** `docs/profile__lock-dark-hero`

This file tracks the controlled rollout of the GitHub profile redesign. Each phase should remain reviewable and should preserve the locked public positioning decisions.

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

**Status:** DIRECTION AND EXPORT COMPLETE, REPOSITORY PLACEMENT PENDING

Locked decisions:

- Use the approved dark Living Product Console hero as the only active banner direction.
- Do not produce or publish a light-mode hero for the current release.
- Use Product Designer as the sole title.
- Show Toronto, Ontario, Canada.
- Show the approved tagline.
- Use exactly these metrics: 2 shipped projects, 1 MADS team project, 5 selected certifications.
- Use only Figma, React, Swift, Firebase, Claude, and Codex in the tool row.
- Keep Zeref Memory Engine and PerFin OS as the dominant visual cards.
- PerFin OS must carry the MADS team project cue and must not imply solo ownership.
- Keep one static hero as the approved baseline before any later motion experiment.

Exported asset stem:

`yash-kanadhia-living-product-console-dark`

Prepared formats:

- PNG, high-resolution raster master.
- JPG, high-quality compressed export.
- SVG, raster-faithful placement wrapper. It is not a fully editable vector reconstruction.

Pending repository action:

- Save the approved files under `assets/hero/`.
- Reference the PNG from `README.md`.
- Add descriptive alt text.
- Verify rendered readability at GitHub desktop and mobile widths.
- Remove or archive the superseded banner only after the new asset is confirmed in the rendered README.

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

**Status:** NEXT

Planned:

- Add bounded latest-writing updates from Substack.
- Add selected build or release signals only when they are meaningful and verified.
- Keep generated content inside explicit README markers.
- Do not add vanity counters, streak cards, random quotes, Spotify widgets, or raw commit feeds.

## Phase 5: Quality gates and release

**Status:** PLANNED

Planned:

- Validate internal and external links.
- Validate local asset paths.
- Scan for placeholders, private paths, secrets, and unsupported claims.
- Check alt text and static fallbacks.
- Review the final PR diff.
- Merge only after the visible banner, README copy, metrics, credentials, and project attribution agree.

## Current risks

- The approved dark hero is generated raster artwork. The SVG export is a faithful embedded-image wrapper rather than editable vector paths.
- The connector-visible PR does not yet contain the approved hero PNG, JPG, or SVG under `assets/hero/`.
- Verified product screenshots and recordings remain an enhancement backlog and must not be represented as already published.
