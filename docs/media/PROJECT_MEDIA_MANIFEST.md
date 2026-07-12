# GitHub Profile Media Manifest

**Status:** ORGANIC ALIENTECH ASSET SYSTEM UNDER REVIEW
**Applies to:** profile hero and evidence-drawer media
**Decision source:** `docs/decisions/GITHUB_PROFILE_ORGANIC_ALIENTECH_ASSET_SYSTEM.md`

## Active identity pair

| Motion asset | Static alternative | Placement |
|---|---|---|
| `assets/hero/yash-kanadhia-alientech-motion.svg` | `assets/hero/yash-kanadhia-alientech-static.svg` | First visual in the README |

The hero remains the only default-visible large visual.

## Reserved evidence media

| Evidence drawer | Parked evidence path |
|---|---|
| Zeref Memory Engine | `assets/profile-media/zeref-product-proof.gif` |
| PerFin OS | `assets/profile-media/perfin-os-product-proof.gif` |
| For Rent | `assets/profile-media/for-rent-product-proof.gif` |
| StreamNexus | `assets/profile-media/streamnexus-product-proof.gif` |

Each slot:

- remains out of scope for this asset pass;
- must not be fabricated;
- may be replaced only with reviewed public-safe runtime media.

Static parked project-portal placeholders live under `assets/project-portals/` and may be used outside the README evidence GIF paths.

## Upload targets

Approved future media should use these paths:

```text
assets/profile-media/
├── zeref-poster.png
├── zeref-walkthrough.gif
├── perfin-os-poster.png
├── perfin-os-walkthrough.gif
├── for-rent-poster.png
├── for-rent-walkthrough.gif
├── streamnexus-poster.png
└── streamnexus-walkthrough.gif
```

A GIF must have a static poster equivalent. Static captures may be used without motion.

## Replacement conditions

A reserved slot may be replaced only when the new media:

1. Comes from a verified runtime or approved source.
2. Is cleared for public use and contains no private data, credentials, local paths, or real addresses.
3. Preserves team ownership and project boundaries in surrounding text.
4. Includes useful alt text.
5. Remains readable at narrow GitHub widths.
6. Uses one coherent workflow rather than a montage of unrelated states.
7. Passes light, dark, desktop, mobile, link, secret, accessibility, and public-claim review.

## Legacy assets

The following older assets remain in repository history or storage but are not active README surfaces:

- `assets/projects/perfin-os/cover.svg`
- `assets/projects/perfin-os/media-pending.svg`
- `assets/projects/for-rent/cover.svg`
- `assets/projects/for-rent/media-pending.svg`
- `assets/projects/streamnexus/cover.svg`
- `assets/projects/streamnexus/media-pending.svg`

Do not restore them to the profile README without a new reviewed decision.
