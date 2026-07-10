# GitHub Profile Media Manifest

**Status:** DUAL-LAYER MEDIA SLOTS UNDER REVIEW  
**Applies to:** profile hero and evidence-drawer media  
**Decision source:** `docs/decisions/GITHUB_PROFILE_INTERACTIVE_IA.md`

## Active identity pair

| Motion asset | Static alternative | Placement |
|---|---|---|
| `assets/hero/yash-kanadhia-living-product-console-dark-motion.svg` | `assets/hero/yash-kanadhia-living-product-console-dark.png` | First visual in the README |

The hero remains the only default-visible large visual.

## Reserved evidence media

| Evidence drawer | Active slot |
|---|---|
| Zeref Memory Engine | `assets/profile-media/zeref-media-slot.svg` |
| PerFin OS | `assets/profile-media/perfin-os-media-slot.svg` |
| For Rent | `assets/profile-media/for-rent-media-slot.svg` |
| StreamNexus | `assets/profile-media/streamnexus-media-slot.svg` |

Each slot:

- uses a 16:9 frame;
- contains minimal text;
- states that verified public-safe media will be added later;
- appears once, inside its matching evidence drawer;
- cannot be described as product proof or a runtime screenshot.

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
