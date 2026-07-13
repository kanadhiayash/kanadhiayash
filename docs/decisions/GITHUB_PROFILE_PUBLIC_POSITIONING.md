# GitHub Profile Public Positioning

**Status:** LOCKED  
**Effective date:** 2026-07-10  
**Last revised:** 2026-07-10  
**Applies to:** GitHub profile README, profile banner, hero copy, motion behaviour, project attribution, credential selection, and future Living Product Console work.

This file is the canonical decision record for the public GitHub profile. Later changes require an explicit replacement decision.

**2026-07-12 supersession note:** the active README asset-family direction is now defined by `docs/decisions/GITHUB_PROFILE_ORGANIC_ALIENTECH_ASSET_SYSTEM.md`, based on the approved Organic AlienTech execution handoff. The public title, tagline, metrics, selected credentials, PerFin attribution, and public-copy guardrails in this file remain active unless that newer decision explicitly replaces them.

The locked future README structure is defined in `docs/decisions/GITHUB_PROFILE_INTERACTIVE_IA.md`. That decision explicitly excludes a profile changelog, memorabilia section, public version-history timeline, and decorative activity archive.

## Primary public title

Use:

> Product Designer

Do not use **AI Product & UX Systems Designer** in the GitHub banner or profile heading for now.

Do not add **UX Systems** as a hero label.

Do not use **Product Strategy** as a hero label. Where that slot exists in a future visual, replace it with **Product Designer** or remove the secondary label so the title remains simply **Product Designer**.

## Public positioning

Lead with product design.

Use development and AI-assisted execution as supporting proof, not as the main title.

Target roles remain:

- Product Designer
- AI Product Designer
- Design Technologist
- Product-engineering-adjacent roles

## Approved tagline

> I design and build systems that connect people to outcomes.

## Public location

> Toronto, Ontario, Canada.

## Banner metrics

Use exactly:

- 2 shipped projects
- 1 MADS team project
- 5 selected certifications

The banner metric refers to five selected credentials, not the complete credential count.

## Team-project attribution

PerFin OS is a MADS final team project.

Credit:

- Yash Kanadhia
- Alexis Gorospe
- Sarmad Tariq

Do not imply solo ownership.

## Selected certifications shown publicly

1. AI Fluency: Framework & Foundations
2. Claude Code in Action
3. Introduction to Claude Cowork
4. Claude Code 101
5. Scrum Fundamentals Certified

Do not show **Six Sigma Yellow Belt** in the GitHub banner, profile heading, or selected-credentials section.

## Additional credential

Claude 101 remains completed and may be listed separately on LinkedIn or in the README.

## Approved tool row

Use only:

- Figma
- React
- Swift
- Firebase
- Claude
- Codex

Do not include ChatGPT in the banner tool row.

## Phase 2 hero visual and motion direction

**Decision status:** LOCKED

Use the approved **dark Living Product Console** as the only GitHub profile hero direction for the current release.

The light variation is not part of the active profile asset set.

### Active presentation

- The animated SVG is the primary README hero.
- The approved PNG remains the static and reduced-motion alternative.
- The JPG remains a compressed distribution or preview asset.
- The original static SVG wrapper may remain for archival placement use.
- Do not place another large animation above the fold.

Active animated asset:

`assets/hero/yash-kanadhia-living-product-console-dark-motion.svg`

Static alternative:

`assets/hero/yash-kanadhia-living-product-console-dark.png`

### Required visual characteristics

- Dark charcoal and near-black canvas.
- Restrained glass panels and system-line details.
- Off-white primary text.
- Military olive signal accents.
- Deep crimson accents used sparingly.
- Editorial typography with clear recruiter-readable hierarchy.
- Zeref Memory Engine and PerFin OS as the dominant project cards.
- Zeref Memory Engine may carry a shipped or flagship cue.
- PerFin OS must carry the **MADS team project** cue and must not imply solo ownership.
- Do not create or publish a light-mode banner unless a later explicit decision reopens that direction.

### Required motion characteristics

- Slow ambient motion rather than decorative spectacle.
- Soft card-border breathing and project-state pulses.
- A restrained scanning light across the console.
- Slow orbital motion inside the PerFin project indicator.
- A moving signal along the lower console rail.
- No rapid flashes, hard strobing, large jumps, or aggressive looping.
- Motion must not communicate information unavailable in the static hero or written README.
- The static alternative must remain directly accessible from the README.
- The hero must remain understandable when animation is blocked or ignored.

### Profile personality guardrail

The motion layer is the profile's primary memorable signature. It should feel like an active product console rather than generic developer decoration.

Do not add a separate profile changelog, memorabilia section, public version-history timeline, or decorative activity archive.

Do not add:

- Contribution snakes or Pacman as a primary profile visual.
- Spotify widgets.
- Random quote animations.
- Multiple typing-title animations.
- Live clocks.
- Visitor, follower, streak, repository, or credential counters.
- Decorative motion that competes with selected work.

## Approved asset family

Base stem:

`yash-kanadhia-living-product-console-dark`

Preferred repository location:

`assets/hero/`

Approved files:

- `yash-kanadhia-living-product-console-dark-motion.svg`, active animated README hero.
- `yash-kanadhia-living-product-console-dark.png`, static alternative.
- `yash-kanadhia-living-product-console-dark.jpg`, compressed preview.
- `yash-kanadhia-living-product-console-dark.svg`, static placement wrapper.

The static SVG wrapper contains embedded raster artwork and must not be described as a fully editable vector source. The animated SVG is a separately reconstructed vector presentation.

## Public-copy guardrails

- Keep **Product Designer** as the sole profile title.
- Do not use **UX Systems** in the hero.
- Do not use **Product Strategy** as a hero category.
- Development and AI-assisted execution support the product-design narrative.
- Keep PerFin OS attribution collaborative and explicit.
- Show five selected certifications on GitHub.
- Exclude Six Sigma Yellow Belt from GitHub profile presentation.
- Do not turn selected credential counts into a claim about the complete credential inventory.
- Use the dark Living Product Console hero for the current release.
- Follow the locked future IA in `docs/decisions/GITHUB_PROFILE_INTERACTIVE_IA.md`.
- Preserve exact project, role, location, metric, credential, tool, hero-direction, motion, and future-IA wording from these decision records unless a later explicit decision replaces them.
