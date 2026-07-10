# Project Media Manifest

**Status:** STAGED INTERACTIVE BUILT-PRODUCT SYSTEM  
**Applies to:** GitHub profile media under `assets/hero/` and `assets/projects/`  
**Decision sources:** `docs/decisions/GITHUB_PROFILE_PUBLIC_POSITIONING.md` and `docs/decisions/GITHUB_PROFILE_INTERACTIVE_IA.md`

This manifest separates the active identity hero, finished metadata covers, honest media-capture states, retained legacy boards, and future verified product captures.

## Active identity pair

| Active motion asset | Static alternative | Scope | Placement |
|---|---|---|---|
| `assets/hero/yash-kanadhia-living-product-console-dark-motion.svg` | `assets/hero/yash-kanadhia-living-product-console-dark.png` | Profile identity, title, metrics, tools, and existing console project references | First visual in the README |

The hero remains unchanged during the staged built-products release. It must retain its directly accessible static alternative.

## Active project covers and media states

| Project | Visible cover | Drawer media state | Public scope |
|---|---|---|---|
| PerFin OS | `assets/projects/perfin-os/cover.svg` | `assets/projects/perfin-os/media-pending.svg` | MADS team ownership, React Native and Firebase platform, verified development evidence |
| For Rent | `assets/projects/for-rent/cover.svg` | `assets/projects/for-rent/media-pending.svg` | SwiftUI rental marketplace, deterministic demo mode, Firebase clean mode, explicit release limitations |
| StreamNexus | `assets/projects/streamnexus/cover.svg` | `assets/projects/streamnexus/media-pending.svg` | Full-stack streaming-rental prototype, role workflows, tests, security, simulated checkout |

Each cover is a finished editorial asset. It uses verified metadata and does not imitate a product screenshot.

Each media state reserves space for reviewed runtime media. It must remain clearly labeled and cannot be described as product proof.

## Visual consistency contract

Active covers and media states use:

- dark charcoal and near-black foundations;
- off-white primary text;
- military olive signal accents;
- restrained deep crimson limitation or ownership accents;
- editorial serif headings and readable sans-serif support text;
- fine system grids and borders;
- clear project type, platform, ownership, and status labels;
- no fake product interface;
- no implied runtime activity, deployment, users, or metrics.

## Placement rules

- Keep the motion hero first.
- Keep the static hero alternative directly accessible after the motion hero.
- Show each project cover before its matching case-file drawer.
- Keep media-capture states inside collapsed project drawers.
- Do not show all media states above the fold.
- Do not use a decorative asset as the only source of project facts.
- Preserve the active project order: PerFin OS, For Rent, StreamNexus.

## Source discipline

### PerFin OS

Current public media may show:

- MADS final team project attribution;
- Yash Kanadhia, Alexis Gorospe, and Sarmad Tariq as the team;
- React Native and Firebase platform context;
- guest and authenticated workspace boundaries;
- reviewed contribution and pull-request evidence;
- media pending team and privacy review.

Do not imply solo ownership, bank connectivity, payment processing, financial advice, or completed public deployment.

### For Rent

Current public media may show:

- SwiftUI rental marketplace scope;
- renter, landlord, and guest journeys;
- deterministic demo mode;
- Firebase clean mode;
- feature-oriented MVVM;
- accessibility support and automated checks.

Do not claim an App Store release or deployed production backend.

### StreamNexus

Current public media may show:

- separate administrator and streamer journeys;
- session authentication and role authorization;
- Express, MongoDB, EJS, tests, security middleware, and CI;
- simulated checkout and rental completion.

Do not claim production OTT operation, real payments, media playback, subscriptions, real users, or compliance certification.

## Media-capture rules

- Final walkthroughs should last approximately 8 to 15 seconds.
- Show one coherent workflow.
- Avoid rapid cuts, flashing, loading filler, and purposeless cursor movement.
- Preserve readable interface text.
- Loop cleanly when GIF is used.
- Include a static poster or equivalent still.
- Remove private data, credentials, local paths, real addresses, and internal-only information.
- Preserve ownership and limitation wording in surrounding text.
- Do not fabricate demonstrations from static mockups.

## Future final-media contract

When verified media is approved, each active project may migrate to:

```text
assets/projects/<project-slug>/
├── cover.svg
├── walkthrough.gif
├── poster.png
├── snapshot-01.png
├── snapshot-02.png
├── snapshot-03.png
└── architecture.png
```

`architecture.png` is optional when the README includes a verified and readable Mermaid system map.

## Parked project media

The current stage does not create or expand media for:

- Arthenticate
- DriveDeal
- Zeref Memory Engine

Their future media must follow the same source, accessibility, ownership, limitation, and replacement controls when those modules resume.

## Retained legacy boards

The following files remain in the repository for history and potential comparison but are not active README surfaces in the staged release:

- `assets/projects/flagship-systems-motion.svg`
- `assets/projects/flagship-systems.svg`
- `assets/projects/built-product-proof-motion.svg`
- `assets/projects/built-product-proof.svg`
- `assets/projects/product-design-studies-motion.svg`
- `assets/projects/product-design-studies.svg`

Do not delete or restore these to the README without a separate reviewed decision.

## Replacement policy

A media-capture state may be replaced only when the new media:

1. Comes from a verified product runtime or approved source.
2. Preserves ownership and limitation wording.
3. Includes descriptive alt text.
4. Includes a still equivalent when motion is used.
5. Does not expose private paths, credentials, personal data, or unsupported metrics.
6. Remains readable at narrow GitHub widths.
7. Passes profile quality, link, secret, accessibility, and public-claim review.
8. Passes GitHub light, dark, desktop, and mobile review.
