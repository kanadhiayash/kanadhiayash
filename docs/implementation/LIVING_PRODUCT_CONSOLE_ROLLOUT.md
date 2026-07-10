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

**Status:** COMPLETE, ASSET PLACEMENT PENDING

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

**Status:** NEXT

Planned:

- Add Zeref product-system visual or motion proof.
- Add PerFin OS verified screenshots and a short workflow recording.
- Add For Rent verified product media.
- Replace StreamNexus placeholder media with verified captures.
- Add Arthenticate and DriveDeal Figma presentation media.
- Keep all motion slow, optional, and understandable without animation.

## Phase 4: Controlled dynamic modules

**Status:** PLANNED

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

## Current risk

The approved dark hero is generated raster artwork. The SVG export is a faithful embedded-image wrapper rather than editable vector paths. A manually reconstructed vector source would be a separate design task.
