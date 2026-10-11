# Motion delivery

Start with the desired effect, user purpose, trigger and target platform. Distinguish a coded interaction, procedural animation, embedded scene and pre-rendered media. Inspect a moving reference through playback; do not infer timing from a still frame.

## Decide what to build

- CSS, SVG, Web Animations API or the project's existing motion library can handle many transitions, loading indicators, reveals and interactive sequences. Implement these directly when requested and within capability.
- Procedural canvas/WebGL/3D work may also be authored with available tools. Assess scene and asset requirements before claiming it needs an external designer.
- A specific authored film, branded character rig, proprietary scene or existing Lottie/Rive/video file may require user-supplied material or a supported creation tool. Check available tools before declaring inability.
- When a source file is essential, explain exactly what is missing, its required format and how it will be integrated. Offer an achievable coded approximation or static fallback, clearly labelled, if helpful. Do not require an uploaded animation merely because the user requested motion.

Explain capabilities concretely in the user's language: what you can create, what you can embed/control, and which specific asset the user needs to provide if any. Never claim that embedding a placeholder is completed animation production.

## Specify and verify

Record trigger, states, animated properties, duration/easing rationale, interrupt/replay behavior, responsive behavior and reduced-motion alternative. Loading must reflect real work; do not fabricate progress or delay usable content for theatrical effect. Essential content stays available when animation fails or is disabled.

Prefer explicit properties and inexpensive transforms/opacity when appropriate. Avoid animating layout unnecessarily. Check cleanup, focus continuity, keyboard access, touch behavior, rendering stability and playback in the target browser. Measure performance before making frame-rate claims. Do not apply decorative particles, cursor effects or text reveals by default.

Source roles: loading.dev for loading components; Kugiri for text segmentation, not a full animation engine; Magic UI and Beautiful UI for candidate components; Details, Morphin and UI Sections for observed patterns; Interfaces for craft reading. Verify the exact component documentation, license, dependencies and accessibility before adoption. Optional tools do not determine the product's visual identity.
