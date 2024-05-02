# Working With Memgraph to Help With Necromunda data and data analysis

To help with the data analysis of Necromunda, we can use Memgraph to store and query the data. This will allow us to create a graph database that can represent the relationships between the various entities in the game, such as gangs, gang members, territories, factions, and battles.


## Create a Gang in memgraph
To get started, we can create a gang in Memgraph using the following Cypher query. This query creates a gang node with properties such as name, type, rating, campaign, credits, meat, reputation, wealth, alignment, and allegiance.  We will later link the gang to its members and other entities in the game.


```cypher
CREATE (gang:Gang {
  gang_id: '486120',
  name: 'Blood Brothers',
  type: 'Genestealer Cult',
  rating: '1000',
  campaign: 'The Outlands Testing Ground',
  credits: '0',
  meat: '0',
  reputation: '1',
  wealth: '1000',
  alignment: 'Law Abiding',
  allegiance: 'Order'
});
```

## Create a Gang Member in memgraph
```cypher

CREATE (ganger1:Ganger {
  ganger_id: '3274119',
  name: 'Xavier',
  type: 'Cult Adept',
  M: 4,
  WS: 4,
  BS: 4,
  S: 3,
  T: 3,
  W: 2,
  I: 3,
  A: 2,
  Ld: 3,
  Cl: 5,
  Wil: 5,
  Int: 4,
  cost: '215',
  xp: '0',
  kills: '0',
  advance_count: '0'
});


CREATE (ganger2:Ganger {
  ganger_id: '3274120',
  name: 'Zuka',
  type: 'Aberrant',
  M: 5,
  WS: 3,
  BS: 6,
  S: 5,
  T: 4,
  W: 2,
  I: 5,
  A: 2,
  Ld: 9,
  Cl: 4,
  Wil: 6,
  Int: 10,
  cost: '150',
  xp: '0',
  kills: '0',
  advance_count: '0'
});

CREATE (ganger3:Ganger {
  ganger_id: '3274121',
  name: 'Kerras',
  type: 'Neophyte Hybrid',
  M: 4,
  WS: 4,
  BS: 4,
  S: 3,
  T: 3,
  W: 1,
  I: 4,
  A: 1,
  Ld: 7,
  Cl: 5,
  Wil: 6,
  Int: 8,
  cost: '85',
  xp: '0',
  kills: '0',
  advance_count: '0'
});

CREATE (ganger4:Ganger {
  ganger_id: '3274122',
  name: 'Marduk',
  type: 'Neophyte Hybrid',
  M: 4,
  WS: 4,
  BS: 4,
  S: 3,
  T: 3,
  W: 1,
  I: 4,
  A: 1,
  Ld: 7,
  Cl: 5,
  Wil: 6,
  Int: 8,
  cost: '115',
  xp: '0',
  kills: '0',
  advance_count: '0'
});

CREATE (ganger5:Ganger {
  ganger_id: '3274123',
  name: 'Crazy Thom',
  type: 'Neophyte Hybrid',
  M: 4,
  WS: 4,
  BS: 4,
  S: 3,
  T: 3,
  W: 1,
  I: 4,
  A: 1,
  Ld: 7,
  Cl: 5,
  Wil: 6,
  Int: 8,
  cost: '100',
  xp: '0',
  kills: '0',
  advance_count: '0'
});

CREATE (ganger6:Ganger {
  ganger_id: '3274124',
  name: 'Larry',
  type: 'Hybrid Acolyte Early Gen',
  M: 4,
  WS: 3,
  BS: 3,
  S: 3,
  T: 3,
  W: 1,
  I: 3,
  A: 2,
  Ld: 4,
  Cl: 5,
  Wil: 7,
  Int: 6,
  cost: '335',
  xp: '0',
  kills: '0',
  advance_count: '0'
});


WITH ganger1, ganger2, ganger3, ganger4, ganger5, ganger6
MATCH (gang:Gang { name: 'Blood Brothers'})
CREATE (gang)-[:HAS_MEMBER]->(ganger1),
       (gang)-[:HAS_MEMBER]->(ganger2),
       (gang)-[:HAS_MEMBER]->(ganger3),
       (gang)-[:HAS_MEMBER]->(ganger4),
       (gang)-[:HAS_MEMBER]->(ganger5),
       (gang)-[:HAS_MEMBER]->(ganger6);


```

## Link the Gang Member to the Gang And Add Equipment
```cypher

// Repeat CREATE statements for other gangers as needed...

// Then we link Xavier to his equipment
WITH ganger1
CREATE (ganger1)-[:EQUIPPED_WITH]->(:Equipment { name: 'Power Sword' }),
       (ganger1)-[:EQUIPPED_WITH]->(:Equipment { name: 'Hand Flamer' }),
       (ganger1)-[:EQUIPPED_WITH]->(:Equipment { name: 'Bio-booster' }),
       (ganger1)-[:EQUIPPED_WITH]->(:Equipment { name: 'Mesh Armor' }),
       (ganger1)-[:EQUIPPED_WITH]->(:Equipment { name: 'Psychic Familiar' });

// Repeat WITH and CREATE statements for other gangers and their equipment as needed...

```

> Note: The above queries are just examples and may need to be modified based on the actual data and relationships in your game.
> In this example, I created a Genestealers Gang and added 6 gang members to it. I also added some equipment to one of the gang members (Xavier) and linked them together. You can repeat the process for other gang members and their equipment as needed.


```cypher

// Finally, we link the gangers to their gang
WITH ganger1, ganger2, ganger3, ganger4, ganger5, ganger6
MATCH (gang:Gang { name: 'Copy of Blood Brothers' })
CREATE (gang)-[:HAS_MEMBER]->(ganger1),
       (gang)-[:HAS_MEMBER]->(ganger2),
       (gang)-[:HAS_MEMBER]->(ganger3),
       (gang)-[:HAS_MEMBER]->(ganger4),
       (gang)-[:HAS_MEMBER]->(ganger5),
       (gang)-[:HAS_MEMBER]->(ganger6);

```

> Note: The above queries are just examples and may need to be modified based on the actual data and relationships in your game.


## Do This as a Batch
Generally, it is easier to do this in a batch rather than one at a time.  This is an example of how you can do this in a batch.


```cypher
CREATE (gang:Gang {
  gang_id: '486120',
  name: 'Blood Brothers',
  type: 'Genestealer Cult',
  rating: '1000',
  campaign: 'The Outlands Testing Ground',
  credits: '0',
  meat: '0',
  reputation: '1',
  wealth: '1000',
  alignment: 'Law Abiding',
  allegiance: 'Order'
})
CREATE (ganger1:Ganger {
  ganger_id: '3274119',
  name: 'Xavier',
  type: 'Cult Adept',
  M: 4,
  WS: 4,
  BS: 4,
  S: 3,
  T: 3,
  W: 2,
  I: 3,
  A: 2,
  Ld: 3,
  Cl: 5,
  Wil: 5,
  Int: 4,
  cost: '215',
  xp: '0',
  kills: '0',
  advance_count: '0'
})
CREATE (ganger2:Ganger {
  ganger_id: '3274120',
  name: 'Zuka',
  type: 'Aberrant',
  M: 5,
  WS: 3,
  BS: 6,
  S: 5,
  T: 4,
  W: 2,
  I: 5,
  A: 2,
  Ld: 9,
  Cl: 4,
  Wil: 6,
  Int: 10,
  cost: '150',
  xp: '0',
  kills: '0',
  advance_count: '0'
})
CREATE (ganger3:Ganger {
  ganger_id: '3274121',
  name: 'Kerras',
  type: 'Neophyte Hybrid',
  M: 4,
  WS: 4,
  BS: 4,
  S: 3,
  T: 3,
  W: 1,
  I: 4,
  A: 1,
  Ld: 7,
  Cl: 5,
  Wil: 6,
  Int: 8,
  cost: '85',
  xp: '0',
  kills: '0',
  advance_count: '0'
})
CREATE (ganger4:Ganger {
  ganger_id: '3274122',
  name: 'Marduk',
  type: 'Neophyte Hybrid',
  M: 4,
  WS: 4,
  BS: 4,
  S: 3,
  T: 3,
  W: 1,
  I: 4,
  A: 1,
  Ld: 7,
  Cl: 5,
  Wil: 6,
  Int: 8,
  cost: '115',
  xp: '0',
  kills: '0',
  advance_count: '0'
})
CREATE (ganger5:Ganger {
  ganger_id: '3274123',
  name: 'Crazy Thom',
  type: 'Neophyte Hybrid',
  M: 4,
  WS: 4,
  BS: 4,
  S: 3,
  T: 3,
  W: 1,
  I: 4,
  A: 1,
  Ld: 7,
  Cl: 5,
  Wil: 6,
  Int: 8,
  cost: '100',
  xp: '0',
  kills: '0',
  advance_count: '0'
})
CREATE (ganger6:Ganger {
  ganger_id: '3274124',
  name: 'Larry',
  type: 'Hybrid Acolyte Early Gen',
  M: 4,
  WS: 3,
  BS: 3,
  S: 3,
  T: 3,
  W: 1,
  I: 3,
  A: 2,
  Ld: 4,
  Cl: 5,
  Wil: 7,
  Int: 6,
  cost: '335',
  xp: '0',
  kills: '0',
  advance_count: '0'
})
WITH ganger1, ganger2, ganger3, ganger4, ganger5, ganger6
MATCH (gang:Gang { name: 'Blood Brothers'})
CREATE (gang)-[:HAS_MEMBER]->(ganger1),
       (gang)-[:HAS_MEMBER]->(ganger2),
       (gang)-[:HAS_MEMBER]->(ganger3),
       (gang)-[:HAS_MEMBER]->(ganger4),
       (gang)-[:HAS_MEMBER]->(ganger5),
       (gang)-[:HAS_MEMBER]->(ganger6);
       
```

## Query the Gang and Gang Members
Now that we have created the gang and its members, we can query the graph to retrieve information about them. For example, to get the gang and its members, you can use the following Cypher query:


```cypher
MATCH (gang:Gang { name: 'Blood Brothers' })-[:HAS_MEMBER]->(ganger)
RETURN gang, ganger;
```


# Adding Weapons, Armorn and Equipment to the Gang Members
To add weapons, armor, and equipment to the gang members, you can create nodes for each item and then link them to the gang members. For example, to add a lasgun and mesh armor to Xavier, you can use the following Cypher query:

```cypher

// Create weapons with their respective properties
CREATE (lasgun:Weapon {name: 'Lasgun', range: '24', strength: '3', damage: '1', traits: 'Rapid Fire', cost: '55'})
CREATE (shotgun:Weapon {name: 'Shotgun', range: '12', strength: '4', damage: '1', traits: 'Solid Shot, Scatter Shot', cost: '40'})
CREATE (powersword:Weapon {name: 'Power Sword', range: 'Melee', strength: 'User', damage: '2', traits: 'Power, Melee', cost: '75'})

// Create armor with their respective properties
CREATE (flakarmor:Armor {name: 'Flak Armor', save: '6+', traits: 'None', cost: '10'})
CREATE (mesharmor:Armor {name: 'Mesh Armor', save: '5+', traits: 'None', cost: '25'})

// If you want to establish which gang or ganger has which equipment, you would use a MATCH statement followed by CREATE to connect them
// For example, if Xavier from earlier owns a Lasgun and wears Mesh Armor, you would do something like this:

MATCH (ganger:Ganger {name: 'Xavier'}), (weapon:Weapon {name: 'Lasgun'}), (armor:Armor {name: 'Mesh Armor'})
CREATE (ganger)-[:EQUIPPED_WITH]->(weapon)
CREATE (ganger)-[:WEARING]->(armor);

```



# Create Territory and Link to Gang
Next, we can create territories in Memgraph and link them to the gang. For example, to create a territory called "Chempit" and link it to the "Blood Brothers" gang, you can use the following Cypher query:
```cypher
CREATE (chempit:Territory {
  name: 'Chempit',
  description: 'A hazardous but resource-rich chemical mine.',
  type: 'Industrial',
  benefits: 'Income, Resources'
})
CREATE (drinkinghole:Territory {
  name: 'The Drinking Hole',
  description: 'A popular gathering place that can be a source of information and recruits.',
  type: 'Social',
  benefits: 'Recruitment, Intelligence'
})
CREATE (gamblingden:Territory {
  name: 'Gambling Den',
  description: 'A den of vice that brings in extra credits through gambling.',
  type: 'Recreational',
  benefits: 'Credits, Black Market Access'
})
CREATE (scraptown:Territory {
  name: 'Scraptown',
  description: 'A sprawling junkyard that can be picked for valuable scrap.',
  type: 'Scavenging',
  benefits: 'Equipment, Trade Goods'
});
```

> Note: The above queries are just examples and may need to be modified based on the actual data and relationships in your game.  We will want to update these later to incude the dice that need to be rolled to get the benefits or income.




## And then to link:

```cypher


MATCH (gang:Gang {name: 'Blood Brothers'}), (territory:Territory {name: 'Chempit'})
CREATE (gang)-[:CONTROLS]->(territory);
```


# Create Factions and Link to Gang
```cypher
CREATE (:Faction {name: 'House Orlock', description: 'The Iron Lords of Necromunda, known for their mining and craftsmanship.'})
CREATE (:Faction {name: 'House Escher', description: 'The matriarchal rulers of chem and pharm production, known for their speed and dexterity.'})
CREATE (:Faction {name: 'House Goliath', description: 'The muscle-bound giants of Necromunda, known for their brute force.'})
CREATE (:Faction {name: 'House Van Saar', description: 'The tech-savvy masters of energy and weaponry.'})
CREATE (:Faction {name: 'House Cawdor', description: 'The zealous and devout scavengers, known for their fanaticism.'})
CREATE (:Faction {name: 'House Delaque', description: 'The masters of espionage and information, lurking in the shadows.'})
CREATE (:Faction {name: 'Chaos Cults', description: 'Worshippers of the dark gods, seeking power and corruption.'})
CREATE (:Faction {name: 'Genestealer Cults', description: 'Infiltrators from the stars, spreading their influence in secret.'})
CREATE (:Faction {name: 'Outlaws', description: 'Rogue elements and mercenaries, operating outside the law.'})
CREATE (:Faction {name: 'Enforcers', description: 'The enforcers of the law, maintaining order in the underhive.'})
CREATE (:Faction {name: 'Corpse Guild', description: 'The undertakers and body harvesters of Necromunda, dealing in death.'})
CREATE (:Faction {name: 'Venator Gangs', description: 'Bounty hunters and hired guns, seeking their fortune in the underhive.'})
CREATE (:Faction {name: 'Scavvies', description: 'The mutated and degenerate survivors of the underhive, living off the scraps.'})
CREATE (:Faction {name: 'Ratskins', description: 'The tribal natives of the underhive, connected to the land and spirits.'})
CREATE (:Faction {name: 'Redemptionists', description: 'Firebrand zealots seeking to cleanse the underhive with flame.'})
CREATE (:Faction {name: 'Spyre Hunters', description: 'The elite agents of House Spyre, hunting down threats to the spire.'})
CREATE (:Faction {name: 'Venators', description: 'The hired guns and mercenaries of the underhive, seeking their fortune.'})
CREATE (:Faction {name: 'Hive Scum', description: 'The lowlifes and scoundrels of the underhive, willing to do anything for credits.'})
CREATE (:Faction {name: 'Hive Outcasts', description: 'The rejects and outcasts of Necromunda, surviving on the fringes.'})
CREATE (:Faction {name: 'Hive Mutants', description: 'The twisted and deformed inhabitants of the underhive, shunned by society.'})
CREATE (:Faction {name: 'Hive Gangs', description: 'The various gangs and factions that vie for control of the underhive.'})
CREATE (:Faction {name: 'Hive Nobility', description: 'The ruling elite of Necromunda, living in luxury and power.'})
CREATE (:Faction {name: 'Hive Merchants', description: 'The traders and merchants of the underhive, dealing in goods and services.'})
CREATE (:Faction {name: 'Hive Workers', description: 'The laborers and workers of Necromunda, toiling in the factories and mines.'})
CREATE (:Faction {name: 'Hive Criminals', description: 'The underworld bosses and crime lords of the underhive, controlling the shadows.'})
CREATE (:Faction {name: 'Hive Law', description: 'The enforcers and arbitrators of Necromunda, maintaining order and justice.'})
CREATE (:Faction {name: 'Hive Guilds', description: 'The various guilds and organizations that operate in the underhive, providing services and support.'})
CREATE (:Faction {name: 'Hive Cults', description: 'The religious sects and cults of Necromunda, worshiping the dark gods and seeking power.'})
CREATE (:Faction {name: 'Hive Tech', description: 'The tech-priests and engineers of the underhive, maintaining the machines and technology.'})
CREATE (:Faction {name: 'Hive Spire', description: 'The towering spires of Necromunda, home to the elite and powerful.'})
CREATE (:Faction {name: 'Hive Underhive', description: 'The dark and dangerous depths of Necromunda, home to the outcasts and mutants.'})
CREATE (:Faction {name: 'Hive Ash Waste', description: 'The desolate wastelands surrounding Necromunda, home to scavengers and nomads.'})
```


## Link the Gang to a Faction
```cypher
MATCH (gang:Gang {name: 'Blood Brothers'}), (faction:Faction {name: 'Genestealer Cults'})
CREATE (gang)-[:ALIGNED_WITH]->(faction);

```



# Add a Campaign and Link to Gang
Now to add a campaign and link it to the gang, you can use the following Cypher query:
```cypher
CREATE (campaign:Campaign {
  name: 'The Outlands Testing Ground',
  description: 'A dangerous proving ground for new gangs and recruits.',
  start_date: '2024-04-01',
  campaign_id: "1",
  campaign_type: "Ash Wastes",
  starting_credits: 1000,
  starting_meat: 0,
  starting_reputation: 1,
  starting_wealth: 1000

})
```
## Link the Campaign to the Gang
```cypher
MATCH (gang:Gang {name: 'Blood Brothers'}), (campaign:Campaign {name: 'The Outlands Testing Ground'})
CREATE (gang)-[:PARTICIPATING_IN]->(campaign);
```

## Add Battles and Link to Gangs
We'll need to create battles and link them to the gangs involved. For example, to create a battle called "Skirmish at the Sump" and link it to the "Blood Brothers" and "Rust Rats" gangs, you can use the following Cypher query:

```cypher
CREATE (battle1:Battle {
  name: 'Skirmish at the Sump',
  description: 'A violent confrontation over the rights to a chem spill in the underhive.',
  date: '2024-04-30',
  location: 'Sump City',
  outcome: 'Undecided'
})
CREATE (battle2:Battle {
  name: 'Raid on Guilder Caravan',
  description: 'An ambush set to rob a wealthy caravan passing through the Ash Wastes.',
  date: '2024-05-05',
  location: 'Ash Wastes',
  outcome: 'Undecided'
})
CREATE (battle3:Battle {
  name: 'Siege of the Steel Fortress',
  description: 'A prolonged siege of a fortified settlement held by the Steel Skulls.',
  date: '2024-05-10',
  location: 'Fortress of Solitude',
  outcome: 'Undecided'
});
// Add additional battles as necessary
```
## Link the battles to the gangs involved
```cypher
MATCH (battle1:Battle {name: 'Skirmish at the Sump'}), (gang1:Gang {name: 'Blood Brothers'}), (gang2:Gang {name: 'Rust Rats'})
CREATE (battle1)-[:INVOLVED]->(gang1)
CREATE (battle1)-[:INVOLVED]->(gang2)
```


# Add a Scenario and Link to a Campaign
Now to add a scenario and link it to the campaign, you can use the following Cypher query:
```cypher
CREATE (scenario:Scenario {
  name: 'The Great Heist',
  description: 'A daring raid on the Hive Spire to steal a priceless artifact.'
})
MATCH (scenario:Scenario {name: 'The Great Heist'}), (campaign:Campaign {name: 'The Outlands Testing Ground'})
CREATE (scenario)-[:PART_OF]->(campaign);
```

