---
sidebar_position: 15
---

# Resolve Hits

:::info
You are viewing the archived rules from before the 2023 Core books. Use the menu to navigate to the current rules.
:::

When a model is hit by an attack, follow these steps:

1. Wound roll
2. Save roll
3. Inflict Damage

## 1. Wound Roll

Roll a D6 and compare the weapon’s Strength with the target’s Toughness on the table below.

| Strength vs Toughness     | D6  |
| ------------------------- | --- |
| Strength >= 2 x Toughness | 2+  |
| Strength > Toughness      | 3+  |
| Strength = Toughness      | 4+  |
| Strength < Toughness      | 5+  |
| Strength <= ½ x Toughness | 6+  |

Vehicles: Every hit must be resolved against a facing (source of the attack) to determine the Toughness. If in doubt, use the highest Toughness.

## 2. Save Roll

If the hit results in a successful wound roll, or leads to an Injury roll being made against the model for any reason, the model may be able to make a save roll.

Only one save roll may be made for each hit that successfully wounds, or leads to an Injury roll being made.

Armour saves are made either:

- After the Wound roll but before the model suffers the Wound. If successful, the Wound is ‘saved’ and ignored.
- If the attack has a Damage ‘-’ characteristic and causes an Injury/Damage dice to be rolled against the model for any reason, a save roll is made before any Injury dice are rolled.

Note that some weapon traits ignore save rolls. In such cases no save roll can be made (regardless of any modifiers).

#### Armour Penetration

If the AP characteristic is greater than the save roll granted by the model's armour, the save roll is cancelled.

#### Positive Save Modifiers

If a model's save would be improved, the positive modifier is added to any normal save roll (some armour are however unmodifiable).

If a model without armour benefits from a positive save modifier, treat their save as 7+ for the purposes of modification.

## 3. Inflict Damage

How damage is inflicted depends of the type of the model.

### Fighters

Damage is inflicted following a successful unsaved wound roll, as follows:

1. Each point of Damage caused by a weapon removes one Wound from the target.
2. When a model is reduced to 0 Wounds by Damage from an attack, immediately roll one Injury dice and apply the result to the fighter.
3. If the weapon causes additional Damage points after the last Wound has been removed, immediately roll an additional Injury dice for each and apply the result.

### Injuries

Any inflicted Injury dice stacks and are applied as follows:

- **Flesh Wound:** Suffer a Flesh Wound (-1T). If Toughness is reduced to 0, go Out of Action.
- **Serious Injury:** Become Prone (can attempt to recover in the End phase). If this injury was inflicted in close combat, the fighter may be vulnerable to Coup de Grace.
- **Out of Action:** The fighter is removed from the battlefield.

:::info Lasting Injuries

When playing a campaign, it is standard practice to roll for lasting injuries as soon as a fighter goes out of action. This is rolled against the [injury table](/docs/old-campaigns/lasting-injuries-and-damage#injury-tables).

:::

:::note

## Damage ‘-’ Weapons

Weapons with Damage characteristic of ‘-’ does not cause Damage in the usual way and will not cause a fighter to lose a Wound.

Consequently, if any Injury dice are rolled against a fighter as the result of an attack made by a Damage ‘-’ weapon, the result(s) of the Injury dice are applied as normal. No Wounds are removed from the fighter.
:::

### Falling

If a model falls 3" or more, suffer a hit based on the distance (rounded up to the nearest inch).

#### Vehicles

Damage is inflicted following an unsaved successful wound roll as follows:

- Location roll.
- Damage roll.

Some hits can result in multiple dice (of a single type). This can be done in 2 separate ways (depending on the situation):

- Choose one result, discard the rest (this is the default).
- Apply all results.

If the roll requires to choose one result and discard the rest, by default the attacker will choose the result, but some exceptions can specify that the vehicle can choose instead.

If it is impossible for a certain location to be hit, simply re-roll the Location dice.

Roll a number of Damage dice equal to the Damage stat of the weapon (regardless of how many Wounds the vehicle has remaining).

Examples:

- A Boltgun (Rapid Fire) inflicts 2 unsaved D2 hits. Each hit results in a roll consisting of:
  - 1 Location dice.
  - 2 Damage dice (attacker chooses 1 to resolve and discards the other).
- A close combat attack inflicts 2 unsaved D2 hits. Each hit results in a roll consisting of:
  - 2 Location dice because close combat grants +1 Location dice (attacker chooses 1 to resolve and discards the other).
  - 2 Damage dice (attacker chooses 1 to resolve and discards the other)

## Out of Action

### Fighters

After going Out of Action (for any reason), suffer a Lasting Injury roll.

### Vehicles (Wrecked)

Vehicles are wrecked (Out of Action) in any of the following situations:

- Reduced to 0 Wounds.
- Rolling over (from Losing Control).

The vehicle is treated as a flimsy structure (terrain) for the rest of the battle.

The vehicle and crew suffer 2 separate rolls (one of each):

- Crew: Crew Lasting Injury roll (only 1 roll regardless of how many crew members the vehicle has).
- Vehicle: Lasting Damage roll (suffer 2 rolls if reduced to 0 Wounds and rolling over at the same time).

#### Claiming Scrap

After the battle, if only one gang remained on the battlefield, gain D3x10 credits per wrecked enemy vehicle (the vehicles are then reclaimed by their owners).

#### Thrown Clear

Any fighters aboard a wrecked vehicle are Thrown Clear:

- Placed within 2".
- Pass an Initiative test or suffer the following:
  - Become Pinned.
  - Suffer a hit as if Falling.
    - If the vehicle was Mobile when wrecked, increase Strength, AP and Damage by 1

## Nerve Tests

Models must take a Nerve test when a friendly model is damaged:

- Fighter: Seriously Injured or Out of Action.
- Vehicle: Out of Action.

| Modal (taking Nerve Test) | Friendly Model (injured) | Within range: |
| ------------------------- | ------------------------ | ------------- |
| Fighter                   | Fighter                  | 3"            |
| Fighter                   | Vehicle                  | 6"            |
| Vehicle                   | Fighter                  | Ignore        |
| Vehicle                   | Vehicle                  | 6"            |

All models must test regardless of Status and Secondary Status (unless immune to Nerve tests).

:::note
No Nerve test is required when a Juve (Specialist) is taken Out of Action, except for other Juve (Specialists).
:::

Nerve test:

- Cool test.
- +1 modifiers per friendly model of the same type (fighter / vehicle) within the following ranges:
  - Fighter: Other friendly fighters within 3" (not Broken or Seriously Injured).
  - Vehicle: Other friendly vehicles within 6".

If failed, the model becomes Broken.

### Broken

When becoming Broken (or activating while Broken), immediately lose any Ready marker and activate (even if already activated this round) as follows:

- Fighter: Running for Cover (Double).
- Vehicle:
  - Mobile: Break For Air (Double) action.
  - Stationary: Burn Out (Double) action.

Broken models can attempt to rally in the End phase.

If Engaged, Broken fighters suffer a -2 modifier to Reaction attacks.

### Fighter: Running for Cover (Double)

- Active: Move 2D6”.
- Prone (Pinned or Seriously Injured): Half Move.

Attempt to end the move in the following order of priority:

1. More than 3” away from enemy models.
2. Out of line of sight of enemy models.
3. In partial or full cover.
4. As far away from any enemy fighters as possible.

If Engaged when activated, use same rules as when Retreating:

1. Make an Initiative test. If failed, the action ends.
2. If passed, any Engaged enemies can try to pass an Initiative test in order to make Reaction attacks against the retreating fighter.
3. If still standing, move 2D6", or half Movement if Seriously Injured when trying to Retreat.

### Mobile Vehicle: Break for Air (Double)

Move 3D6" with any number of pivots.

Attempt to end the move in the following order of priority:

1. More than 3” away from enemy models.
2. Out of line of sight of enemy models.
3. In partial or full cover.
4. As far away from any enemy models as possible.

### Stationary Vehicle: Burn Out (Double)

- Place D3 Smoke Blasts (5") anywhere within 1".
- -1 modifier to the Restart test (in end phase) per Smoke marker
