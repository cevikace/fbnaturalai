# Meadow Glide — Nature-Themed Flappy Experience

## Overview
Meadow Glide keeps the side-scrolling, tap-to-fly rhythm of Flappy Bird while wrapping it in a serene, nature-first aesthetic. Players guide a lively pollinator through wind-brushed fields, dodging organic obstacles and collecting nectar as the landscape shifts from dawn to dusk.

- **Platform and engine**: Designed for a Python codebase using Pygame or Arcade for straightforward sprite handling and parallax scrolling.
- **Core loop**: Tap/press to gain altitude, release to descend; collisions end the run; collectible nectar adds score and unlocks soft visual flourishes.
- **Tone**: Peaceful, colorful, and softly animated—aimed at creating focus without stress.

## Main Character Options
- **Butterfly (default)**: Gradient wings with soft translucency, subtle wing-trail particles of pollen dust. Idle animation gently rocks with wind.
- **Bee (variant)**: Rounder silhouette with fuzzy edges; a tiny saddlebag for nectar visually swells as score climbs.
- **Chickadee (variant)**: Small bird with leaf-accented tail feathers; quick flutter animation.

## Obstacles & World Elements
- **Vine archways**: Twisting vines with leaves and dew drops form the classic gate gaps; occasional blossoms protrude, requiring micro-adjustments.
- **Tree branches**: Horizontal limbs with moss and mushrooms; some carry resting ladybugs that lightly glow at night.
- **Floating flower stems**: Tall stems sway with wind; flowers open/close slightly as you pass.
- **Rolling hedgerows (advanced stages)**: Ground-level bumps that narrow the vertical play space, encouraging tight timing.

## Background & Environment Layers
- **Parallax fields**: Foreground grass blades sway; midground has wildflower clusters (poppies, daisies, roses); distant hills fade into pastel skies.
- **Bloom events**: Random background flowers briefly bloom when the player passes milestones, adding color bursts without affecting difficulty.
- **Sky variations**: Gradient skies shift through dawn pinks, noon blues, golden hours, and starry nights.

## Art Style
- **Palette**: Warm greens, rose reds, sunflower yellows, and sky blues; soft shadows and painterly highlights.
- **Line work**: Minimal outlines; rely on color contrast and subtle texture brushes to separate forms.
- **Animation**: Gentle squash-and-stretch for flight; leaves and petals use sinusoidal sway driven by a global wind value.

## Sound & Music
- **Ambient bed**: Soft wind, distant birdsong, and occasional rustling leaves; layered at low volume.
- **UI cues**: Taps trigger a light chime; scoring a nectar adds a soft bell and tiny pollen burst; collisions use a muted thud and leaf fall effect.
- **Music**: Calming acoustic/lofi loops that adapt to day-night cycle; add subtle crickets at night.

## UI & HUD
- **Minimal overlay**: Top-left score (nectar count), top-right best run; translucent leaf-backplate for readability.
- **Pause/Settings**: Leaf-shaped pause button; settings panel toggles music/ambience balance and colorblind-friendly palettes.
- **Onboarding**: One-screen illustration shows tap-to-fly and obstacle avoidance using character silhouettes.

## Mechanics & Difficulty
- **Gravity and lift**: Matches Flappy Bird responsiveness but tuned slightly softer for a calmer feel. Wind gust events temporarily alter gravity for variety.
- **Obstacle cadence**: Start with wide vine gaps; gradually introduce swaying stems and branches; hedgerows appear after a score threshold.
- **Dynamic gap sizing**: Gaps shrink slowly as score increases; occasional “breather” sections with wider gaps restore flow.
- **Day-night cycle** (optional): Every set distance advances time-of-day; lighting, sky gradients, and ambient SFX adjust accordingly.

## Power-Ups (Optional)
- **Nectar rush**: Brief invulnerability with sparkling wing trail; doubles score for its duration.
- **Petal glide**: Reduces gravity for a few seconds, adding hang time; petals swirl around the character.
- **Bloom beacon**: Reveals upcoming obstacle gaps with glowing fireflies.

## Progression & Rewards
- **Milestone blooms**: At scores 10, 25, 50, trigger background bloom animations and color shifts.
- **Cosmetic unlocks**: Earn new wing patterns, flower crowns, or leaf trails by reaching score goals.
- **Relaxed mode**: Optional setting with slower scroll speed and no score penalties, focusing on scenery.

## Suggested Implementation Notes (Python)
- **Framework**: Pygame/Arcade for sprite batching, parallax layers, and collision masks.
- **Structure**: Separate modules for `scene`, `player`, `obstacles`, `parallax`, and `audio`; use dataclasses for configuration (gravity, flap impulse, gap sizes).
- **Animation cues**: Use sine-based offsets for plant sway; particle emitters for pollen bursts and leaf fall on collisions.
- **Audio mix**: Channel ambient and music separately; expose sliders in settings menu.
- **Testing**: Add config-driven difficulty curves and debug overlays (hitboxes, gap predictions) toggled by a key.
