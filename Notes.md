# To do
Short term:
- Verify information in CardData (Ascenders Bane should have special rarity)
- identify cards which
  - give strength or dex as a buff
  - subtract strength or dex as a debuff
- Implement Card Effects:
  - Parse for Damage, Block, Poison, Orbs, other common effects
  - Create csv specifying unique card effects for each card 
- Aggregate Strikes and Defends

Long term:
- Separate upgraded and unupgraded cards 

Problems:
- There are multiple copies of strike and defend

# Notes
Cards which exhaust other cards: Havoc, True Grit, Burning Pact, Second Wind, Sever Soul, Corruption, Fire Fiend, Omniscience
Cards that interact with exhaust: Dark Embrance, Feel No Pain, Sentinel, Exhume
Cards which retain other cards: Well-Laid Plans, Equilibruim, Meditate, 
Cards that interact with retain: Perseverance, Sands of Time, Windmill, Establishment

# Desired Card Information

### Ver 0
*For now, combine attributes of upgraded and unupgraded versions of each card* <br>
**id**: Unique identifier (arbitrarily labelled) <br>
**Name**: 365 unique card names <br>
**Color**: Red, Green, Blue, Purple, Colorless, Curse <br>
**Rarity**: Basic, Common, Uncommon, Rare, Special, Curse <br>
**Type**: Attack, Skill, Power, Status, Curse <br>
**Cost**: 0, 1, 2, 3, 4, 5, X, Unplayable <br>
**Text**: some random text <br>

### Ver 1
**id**: Unique identifier (arbitrarily labelled) <br>
**Name**: 365 unique card names <br>
**Color**: Red, Green, Blue, Purple, Colorless, Curse <br>
**Rarity**: Basic, Common, Uncommon, Rare, Special, Curse <br>
**Type**: Attack, Skill, Power, Status, Curse
**Cost**: 0, 1, 2, 3, 4, 5, X, Unplayable <br>
**Card Traits**: Innate, Exhaust, Ethereal, Retain, Unplayable <br>
**Debuffs**: Weaken, Frail, Vulnerable <br>
**Buffs**: Intangible <br>
**Effect**: <br>

### Ver 2
\+ **Debuffs**: Minus Strength, Minus Dexterity <br>
\+ **Buffs**: Plus Strength, Plus Dexterity, Plated Armor <br>

### Goal
*We would like to make an additional entry for every single upgraded card* <br>
**id**: Unique identifier (arbitrarily labelled) <br>
**Name**: About 700 unique card names (upgraded and unupgraded copies) <br>
**Color**: Red, Green, Blue, Purple, Colorless, Curse <br>
**Rarity**: Basic, Common, Uncommon, Rare, Special, Curse <br>
**Type**: Attack, Skill, Power, Status, Curse
**Cost**: 0, 1, 2, 3, 4, 5, X, unplayable <br>
**Card Traits**: Innate, Exhaust, Ethereal, Retain, Unplayable <br>
**Debuffs**: Weaken, Frail, Vulnerable, Minus Strength, Minus Dexterity <br>
**Buffs**: Plus Strength, Plus Dexterity, Intangible, Plated Armor <br>
**Effect**: Damage, Block, Poison, Discard a card, Exhaust a card <br>

### 100% complete
**id**: Unique identifier (arbitrarily labelled) <br>
**Name**: About 700 unique card names (upgraded and unupgraded copies) <br>
**Color**: Red, Green, Blue, Purple, Colorless, Curse <br>
**Rarity**: Basic, Common, Uncommon, Rare, Special, Curse <br>
**Type**: Attack, Skill, Power, Status, Curse
**Cost**: 0, 1, 2, 3, 4, 5, X, unplayable <br>
**Card Traits**: Innate, Exhaust, Ethereal, Retain, Unplayable <br>
**Debuffs**: Weaken, Frail, Vulnerable, Minus Strength, Minus Dexterity, etc. <br>
**Buffs**: Plus Strength, Plus Dexterity, Intangible, Plated Armor, etc.<br>
**Effect**: Damage, Block, Poison, Discard a card, Exhaust a card, Retain a card, Orbs, Stances, and all other possible effects (e.g. burst, phantasmal killer) <br>