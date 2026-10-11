# Project design-system lifecycle

Every site built or redesigned with this skill receives a persistent design-system module inside its own project. Reuse an existing system and its conventions rather than creating a competing one. Do not put client-specific styles in the global skill. An isolated advisory answer need not scaffold a project.

## Establish after direction selection

Record the brief, approved direction, source links, dated research, selected and rejected traits, visual constraints and reasons. Initialize the module when the direction is chosen; evolve it while implementing, rather than documenting only at the end.

Use the project's framework and existing structure. A suitable default is:

- `design-system/README.md`: entry point, approved direction, module map, canonical token/component locations, usage and validation instructions.
- `design-system/decisions.md`: dated decisions, approval/delegation context, changes and reasons.
- `design-system/references.md`: source URLs, evidence dates, inspected states and specific adaptations.
- Canonical tokens in the actual theme/CSS/config consumed by the application: semantic color roles, typography, spacing, layout widths, breakpoints, radii, borders, shadows and motion values where needed. Link to those files rather than duplicate their values in an unused JSON file.
- Reusable components in the application's component library: variants, states and usage guidance. Link to the implementation instead of maintaining parallel copies.
- A project-local component showcase or existing Storybook equivalent: representative typography, colors, controls, forms, navigation and relevant loading/empty/error/success states. Make it easy to review; do not expose internal documentation publicly without a deployment requirement.

Document keyboard/focus behavior, responsive rules, reduced motion, content voice and imagery direction alongside the applicable components or guidelines. Reference only relevant UX principles and accessibility checks. Distinguish implemented behavior from a desired future rule.

## Keep changes synchronized

Before editing a site, read its module and locate the actual source of truth. Classify the change as content-only, component-specific, page-specific or system-wide.

- System-wide visual/behavior changes: update canonical tokens or shared components first, then affected usage and the showcase.
- Component changes: update the implementation, applicable state/usage guidance and consuming screens.
- Intentional page exceptions: scope them locally and record their reason; do not silently alter the whole site's style.
- Content-only changes: check for layout implications; do not invent a token revision when no system decision changed.

Update impacted design-system records in the same change as the site. Record meaningful decision changes, keeping the user's selected direction stable unless they authorize a new direction. Propagate shared changes to consumers and inspect representative screens/states for drift. Use existing project checks, adding focused checks only where they establish meaningful behavior.

At handoff, link the module and showcase, identify what changed and report actual validation. If system work remains, state it as incomplete rather than claiming the website is fully handed over. Use the project's version control when available; never imply persistence beyond the saved files and actual history.

This synchronization applies whenever the agent edits the project. External/manual changes do not automatically update documentation unless a real watcher or CI mechanism has separately been implemented. Do not promise background monitoring.
