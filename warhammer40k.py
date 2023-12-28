# Imports.

import numpy as np
import pandas as pd

# Local data setup:
origins_data = [["Death World", "Void Born", "Forge World", "Hive World", "Imperial World", "Noble Born"],
                ["Scavenger", "Scapegrace", "Stubjack", "Child of the Creed", "Savant", "Vaunted"],
                ["Tainted", "Criminal", "Renegade", "Duty Bound", "Zealot", "Chosen by Destiny"],
                ["The Hand of War", "Press-Ganged", "Calamity", "Ship-Lorn", "Dark Voyage", "High Vendetta"],
                ["Endurance", "Fortune", "Vengeance", "Renown", "Pride", "Prestige"],
                ["Astropath Transcendent", "Arch-Militant", "Void-Master", "Explorator", "Missionary", "Seneschal",
                 "Navigator", "Rogue Trader"]]
origins = pd.DataFrame(index=["Home World", "Birthright", "Lure of the Void", "Trails and Travails", "Motivation",
                              "Career"], columns=range(0, 8), data=origins_data)
origins_index = len(origins.index)
origins_columns = len(origins.columns)
mutations = ["Grotesque", "Tough Hide", "Misshapen", "Feels No Pain", "Brute", "Nightsider", "Mental Regressive",
             "Malformed Hands", "Tox Blood", "Hulking", "Wyrdling", "Vile Deformity", "Aberration", "Degenerate Mind",
             "Ravaged Body", "Clawed/Fanged", "Necrophage", "Corrupted Flesh", "Venomous", "Hideous Strength",
             "Multiple Appendages", "Worm", "Nightmarish", "Malleable", "Winged", "Corpulent", "Shadow Kin",
             "Corrosive Bile", "Hellspawn"]
# Note that group skills are indicated by 1 in "group" column (0 otherwise).
skill_groups = pd.DataFrame(index=["Ciphers (Rogue Trader)", "Ciphers (Mercenary Cant)", "Ciphers (Nobilite Family)",
                                   "Ciphers (Astropath Sign)", "Ciphers (Underworld)", "Drive (Ground Vehicle)",
                                   "Drive (Skimmer/Hover)", "Drive (Walker)", "Common Lore (Adeptus Arbites)",
                                   "Common Lore (Adeptus Astra Telepathica)", "Common Lore (Adeptus Mechanicus)",
                                   "Common Lore (Administratum)", "Common Lore (Ecclesiarchy)",
                                   "Common Lore (Imperial Creed)", "Common Lore (Imperial Guard)",
                                   "Common Lore (Imperial Navy)", "Common Lore (Imperium)",
                                   "Common Lore (Koronous Expanse)", "Common Lore (Machine Cult)",
                                   "Common Lore (Navis Nobilite)", "Common Lore (Rogue Traders)", "Common Lore (Tech)",
                                   "Common Lore (War)", "Forbidden Lore (Adeptus Mechanicus)",
                                   "Forbidden Lore (Archeotech)", "Forbidden Lore (Daemonology)",
                                   "Forbidden Lore (Heresy)", "Forbidden Lore (the Inquisition)",
                                   "Forbidden Lore (Mutants)", "Forbidden Lore (Navigators)",
                                   "Forbidden Lore (Pirates)", "Forbidden Lore (Psykers)", "Forbidden Lore (the Warp)",
                                   "Forbidden Lore (Xenos)", "Navigation (Surface)", "Navigation (Stellar)",
                                   "Navigation (Warp)", "Performer (Dancer)", "Performer (Musician)",
                                   "Performer (Singer)", "Performer (Storyteller)", "Pilot (Personal)",
                                   "Pilot (Flyers)", "Pilot (Spacecraft)", "Scholastic Lore (Archaic)",
                                   "Scholastic Lore (Astromancy)", "Scholastic Lore (Beasts)",
                                   "Scholastic Lore (Bureaucracy)", "Scholastic Lore (Chymistry)",
                                   "Scholastic Lore (Cryptology)", "Scholastic Lore (Heraldry)",
                                   "Scholastic Lore (Imperial Warrants)", "Scholastic Lore (Imperial Creed)",
                                   "Scholastic Lore (Judgement)", "Scholastic Lore (Legend)",
                                   "Scholastic Lore (Navis Nobilite)", "Scholastic Lore (Numerology)",
                                   "Scholastic Lore (Occult)", "Scholastic Lore (Philosophy)",
                                   "Scholastic Lore (Tactica Imperialis)", "Secret Tongue (Administratum)",
                                   "Secret Tongue (Ecclesiarchy)", "Secret Tongue (Military)",
                                   "Secret Tongue (Navigator)", "Secret Tongue (Rogue Trader)", "Secret Tongue (Tech)",
                                   "Secret Tongue (Underdeck)", "Speak Language (Eldar)",
                                   "Speak Language (Explorator Binary)", "Speak Language (High Gothic)",
                                   "Speak Language (Hive Dialect)", "Speak Language (Low Gothic)",
                                   "Speak Language (Ork)", "Speak Language (Ship Dialect)",
                                   "Speak Language (Techna-Lingua)", "Speak Language (Trader's Cant)",
                                   "Trade (Archaelogist)", "Trade (Armourer)", "Trade (Astrographer)",
                                   "Trade (Chymist)", "Trade (Cryptographer)", "Trade (Explorator)", "Trade (Linguist)",
                                   "Trade (Remembrancer, Ag)", "Trade (Remembrancer, Int)", "Trade (Shipwright)",
                                   "Trade (Soothsayer)", "Trade (Technomat)", "Trade (Trader)", "Trade (Voidfarer)"],
                            columns=["type", "characteristic", "descriptor1", "descriptor2", "group"],
                            data=[['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Agility', 'Operator', None, 0],
                                  ['Advanced', 'Agility', 'Operator', None, 0],
                                  ['Advanced', 'Agility', 'Operator', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Exploration', None, 0],
                                  ['Advanced', 'Intelligence', 'Exploration', None, 0],
                                  ['Advanced', 'Intelligence', 'Exploration', None, 0],
                                  ['Advanced', 'Fellowship', None, None, 0],
                                  ['Advanced', 'Fellowship', None, None, 0],
                                  ['Advanced', 'Fellowship', None, None, 0],
                                  ['Advanced', 'Fellowship', None, None, 0],
                                  ['Advanced', 'Agility', "Operator", None, 0],
                                  ['Advanced', 'Agility', "Operator", None, 0],
                                  ['Advanced', 'Agility', "Operator", None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Agility', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Agility', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Intelligence', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Intelligence', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Intelligence', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Intelligence', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Agility', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Intelligence', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Intelligence', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Fellowship', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Intelligence', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Fellowship', 'Crafting', 'Exploration', 0],
                                  ['Advanced', 'Agility', 'Crafting', 'Exploration', 0]
                                  ])

skills_table = pd.DataFrame(index=["Acrobatics", "Awareness", "Barter", "Blather", "Carouse", "Charm", "Chem-Use",
                                   "Ciphers", "Climb", "Commerce", "Command", "Common Lore", "Concealment",
                                   "Contortionist", "Deceive", "Demolition", "Disguise", "Dodge", "Drive", "Evaluate",
                                   "Forbidden Lore", "Gamble", "Inquiry", "Interrogation", "Intimidate", "Invocation",
                                   "Literacy", "Logic", "Medicae", "Navigation", "Performer", "Pilot",
                                   "Psyniscience", "Scholastic Lore", "Scrutiny", "Search", "Secret Tongue",
                                   "Security", "Shadowing", "Silent Move", "Sleight of Hand", "Speak Language",
                                   "Survival", "Swim", "Tech-Use", "Tracking", "Trade", "Wrangling"],
                            columns=["type", "characteristic", "descriptor1", "descriptor2", "group"],
                            data=[['Advanced', 'Agility', 'Movement', None, 0],
                                  ['Basic', 'Perception', 'Exploration', None, 0],
                                  ['Basic', 'Fellowship', 'Interaction', None, 0],
                                  ['Advanced', 'Fellowship', 'Interaction', None, 0],
                                  ['Basic', 'Toughness', None, None, 0],
                                  ['Basic', 'Fellowship', 'Interaction', None, 0],
                                  ['Advanced', 'Intelligence', 'Crafting', 'Investigation', 0],
                                  ['Advanced', 'Intelligence', None, None, 1],
                                  ['Basic', 'Strength', 'Movement', None, 0],
                                  ['Advanced', 'Fellowship', None, None, 0],
                                  ['Basic', 'Fellowship', 'Interaction', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 1],
                                  ['Basic', 'Agility', None, None, 0],
                                  ['Basic', 'Agility', 'Movement', None, 0],
                                  ['Basic', 'Fellowship', 'Interaction', None, 0],
                                  ['Advanced', 'Intelligence', 'Crafting', None, 0],
                                  ['Basic', 'Fellowship', None, None, 0],
                                  ['Basic', 'Agility', None, None, 0],
                                  ['Advanced', 'Agility', 'Operator', None, 1],
                                  ['Basic', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 1],
                                  ['Basic', 'Intelligence', None, None, 0],
                                  ['Basic', 'Fellowship', 'Investigation', None, 0],
                                  ['Advanced', 'Willpower', 'Investigation', None, 0],
                                  ['Basic', 'Strength', 'Interaction', None, 0],
                                  ['Advanced', 'Willpower', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Basic', 'Intelligence', 'Investigation', None, 0],
                                  ['Advanced', 'Intelligence', None, None, 0],
                                  ['Advanced', 'Intelligence', 'Exploration', None, 1],
                                  ['Advanced', 'Fellowship', None, None, 1],
                                  ['Advanced', 'Agility', 'Operator', None, 1],
                                  ['Advanced', 'Perception', None, None, 0],
                                  ['Advanced', 'Intelligence', 'Investigation', None, 1],
                                  ['Basic', 'Perception', None, None, 0],
                                  ['Basic', 'Perception', 'Exploration', None, 0],
                                  ['Advanced', 'Intelligence', None, None, 1],
                                  ['Advanced', 'Agility', 'Exploration', None, 0],
                                  ['Advanced', 'Agility', None, None, 0],
                                  ['Basic', 'Agility', 'Movement', None, 0],
                                  ['Advanced', 'Agility', None, None, 0],
                                  ['Advanced', 'Intelligence', None, None, 1],
                                  ['Advanced', 'Intelligence', 'Exploration', None, 0],
                                  ['Basic', 'Strength', 'Movement', None, 0],
                                  ['Advanced', 'Intelligence', 'Exploration', None, 0],
                                  ['Advanced', 'Intelligence', 'Exploration', None, 0],
                                  ['Advanced', 'Intelligence', 'Crafting', 'Exploration', 1],
                                  ['Advanced', 'Intelligence', None, None, 0]
                                  ])
skills_table = pd.concat([skills_table, skill_groups], sort=True)
skills_table.sort_index(inplace=True)


class Creature:
    def __init__(self, name: str, kind: str = "Human", level: int = 0):
        self.name = name
        self.kind = kind
        self.level = level
        self.rolls: list = []
        self.characteristics = pd.DataFrame(index=["Weapon Skill", "Ballistic Skill", "Strength", "Toughness",
                                                   "Agility", "Intelligence", "Perception", "Willpower",
                                                   "Fellowship"], columns=["characteristic", "bonus",
                                                                           "bonus_multiplier"])
        self.origin: list = []
        self.skills = pd.DataFrame(index=None, columns=['training', 'type', 'level'])
        self.talents: list = []
        self.traits: list = []
        self.wounds: int = 0
        self.fate: int = 0
        self.initiative_modifier: int = 0
        self.profit_factor: int = 0
        self.corruption: int = 0
        self.insanity: int = 0
        self.psy = 0

    def roll(self, dice_number: int = 1, dice_sides: int = 6):
        for i in range(0, dice_number):
            self.rolls.append(np.random.randint(1, dice_sides + 1))
            # print(f"{self.name} rolled {self.rolls[-1]}.")  # <-- This line is here only for testing
        return self.rolls[-dice_number:]

    @property
    def roll_history(self):
        return self.rolls

    def generate_home_world_stats(self):
        if self.origin[0] == "Death World":
            self.characteristics.loc["Strength", "characteristic"] += 5
            self.characteristics.loc["Toughness", "characteristic"] += 5
            self.characteristics.loc["Willpower", "characteristic"] += 5
            self.characteristics.loc["Fellowship", "characteristic"] -= 5
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Survival"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[[None, skills_table.loc['Survival', ['type']],
                                                                      None]])])
            if np.random.randint(0, 2) == 0:
                self.traits.append("Hardened")
                self.talents.append("Jaded")
            else:
                self.traits.append("Hardened")
                self.talents.append("Resistance (Poisons)")
            self.traits.append("If It Bleeds, I Can Kill It")
            self.talents.append("Melee Weapon Training (Primitive)")
            self.traits.append("Paranoid")
            self.talents.append("-10 to all Interaction Skill Tests in formal surroundings")
            self.traits.append("Survivor")
            self.talents.append("+10 to all Tests to resist Pinning and Shock")
            self.wounds += sum(self.roll(1, 5)) + 2
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            self.roll(1, 10)
            if self.roll_history[-1] < 6:
                self.fate = 2
            else:
                self.fate = 3
        if self.origin[0] == "Void Born":
            self.characteristics.loc["Strength", "characteristic"] -= 5
            self.characteristics.loc["Willpower", "characteristic"] += 5
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Speak Language (Ship Dialect)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[[None,
                                                                      skills_table.loc['Speak Language (Ship Dialect)',
                                                                                       ['type']], None]])])
            self.traits.append("Charmed")
            self.talents.append("Roll natural 9 on 1d10 when spending Fate Point => FP NOT spent")
            self.traits.append("Ill-Omened")
            self.talents.append("-5 to all Fellowship Tests interacting with non-void born humans")
            self.traits.append("Shipwise")
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Navigation (Stellar)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Untrained',
                                                                     skills_table.loc['Navigation (Stellar)', ['type']],
                                                                     'Basic']])])
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Pilot (Spacecraft)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Untrained',
                                                                     skills_table.loc['Pilot (Spacecraft)', ['type']],
                                                                     'Basic']])])
            self.traits.append("Void Accustomed")
            self.talents.append("Immune to space travel sickness")
            self.talents.append("Zero- & low-gravity environments => NOT Difficult Terrain")
            self.wounds += sum(self.roll(1, 5))
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            self.roll(1, 10)
            if self.roll_history[-1] < 6:
                self.fate = 3
            else:
                self.fate = 4
        if self.origin[0] == "Forge World":
            self.characteristics.loc["Weapon Skill", "characteristic"] -= 5
            self.characteristics.loc["Intelligence", "characteristic"] += 5
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Common Lore (Tech)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Untrained',
                                                                      skills_table.loc['Common Lore (Tech)', ['type']],
                                                                     'Basic']])])
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Common Lore (Machine Cult)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Untrained',
                                                                      skills_table.loc['Common Lore (Machine Cult)',
                                                                                       ['type']], 'Basic']])])
            self.traits.append("Credo Omnissiah")
            self.talents.append("Technical Knock")
            self.traits.append("Fit for Purpose")
            chosen_chr = np.random.randint(0, 9)
            self.talents.append(f"+3 to a chosen Characteristic: {self.characteristics.index[chosen_chr]}")
            self.characteristics.iloc[chosen_chr, 0] += 3
            self.traits.append("Stranger to the Cult")
            self.talents.append("-10 to all Tests involving knowledge of the Imperial Creed")
            self.talents.append("-5 to all Fellowship Tests interacting with Ecclesiarchy in formal settings")
            self.wounds += sum(self.roll(1, 5)) + 1
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            self.roll(1, 10)
            if self.roll_history[-1] < 6:
                self.fate = 2
            elif self.roll_history[-1] < 10:
                self.fate = 3
            else:
                self.fate = 4
        if self.origin[0] == "Hive World":
            self.characteristics.loc["Toughness", "characteristic"] -= 5
            self.characteristics.loc["Fellowship", "characteristic"] += 5
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Speak Language (Hive Dialect)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Untrained',
                                                                      skills_table.loc['Speak Language (Hive Dialect)',
                                                                      ['type']], 'Basic']])])
            self.traits.append("Accustomed to Crowds")
            self.talents.append("Crowds => NOT Difficult Terrain")
            self.talents.append("Running or Charging through dense crowd => NO penalty to Agility Tests to keep "
                                "creature's feet")
            self.traits.append("Caves of Steel")
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Tech-Use"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Untrained',
                                                                      skills_table.loc['Tech-Use', ['type']],
                                                                      'Basic']])])
            self.traits.append("Hivebound")
            self.talents.append("-10 to all Survival (Int) Tests while NOT in \"Proper Habitat\"")
            self.talents.append("-5 to all Intelligence Tests while NOT in \"Proper Habitat\"")
            self.traits.append("Wary")
            self.initiative_modifier += 1
            self.wounds += sum(self.roll(1, 5)) + 1
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            self.roll(1, 10)
            if self.roll_history[-1] < 6:
                self.fate = 2
            elif self.roll_history[-1] < 9:
                self.fate = 3
            else:
                self.fate = 4
        if self.origin[0] == "Imperial World":
            self.characteristics.loc["Willpower", "characteristic"] += 3
            self.traits.append("Blessed Ignorance")
            self.talents.append("-5 to Forbidden Lore (Int) Tests")
            self.traits.append("Hagiography")
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Common Lore (Imperial Creed)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[[None,
                                                                      skills_table.loc['Common Lore (Imperial Creed)',
                                                                                       ['type']], None]])])
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Common Lore (Imperium)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[[None, skills_table.loc['Common Lore (Imperium)',
                                                                                             ['type']], None]])])
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Common Lore (War)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[[None, skills_table.loc['Common Lore (War)',
                                                                                             ['type']], None]])])
            self.traits.append("Liturgical Familiarity")
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Literacy"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Untrained',
                                                                      skills_table.loc['Literacy', ['type']],
                                                                      'Basic']])])
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Speak Language (High Gothic)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Untrained',
                                                                      skills_table.loc['Speak Language (High Gothic)',
                                                                                       ['type']], 'Basic']])])
            self.wounds += sum(self.roll(1, 5))
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            self.roll(1, 10)
            if self.roll_history[-1] < 9:
                self.fate = 3
            else:
                self.fate = 4
        if self.origin[0] == "Noble Born":
            self.characteristics.loc["Willpower", "characteristic"] -= 5
            self.characteristics.loc["Fellowship", "characteristic"] += 5
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Literacy"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Untrained',
                                                                      skills_table.loc['Literacy', ['type']],
                                                                      'Basic']])])
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Speak Language (High Gothic)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Untrained',
                                                                      skills_table.loc['Speak Language (High Gothic)',
                                                                                       ['type']], 'Basic']])])
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Speak Language (Low Gothic)"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Untrained',
                                                                      skills_table.loc['Speak Language (Low Gothic)',
                                                                                       ['type']], 'Basic']])])
            self.traits.append("Etiquette")
            self.talents.append("+10 to Interaction Tests when dealing with authority and in formal situations")
            self.traits.append("Legacy of Wealth")
            self.profit_factor = 1
            # Supremely Connected Trait
            supremely_connected = "Peer ("
            supremely_connected += [
                "Academics", "Adeptus Mechanicus", "Administratum", "Astropaths", "Ecclesiarchy", "Government",
                "Mercantile", "Military", "Underworld"][np.random.randint(0, 9)]
            supremely_connected += ")"
            self.traits.append("Supremely Connected")
            self.talents.append("Peer (Nobility)")
            self.talents.append(supremely_connected)
            self.traits.append("Vendetta")
            self.talents.append("Powerful enemies to be defined by Player & GM")
            self.wounds += sum(self.roll(1, 5))
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            self.roll(1, 10)
            if self.roll_history[-1] < 4:
                self.fate = 2
            elif self.roll_history[-1] < 10:
                self.fate = 3
            else:
                self.fate = 4

    def generate_birthright_stats(self):
        if self.origin[1] == "Scavenger":
            if np.random.randint(0, 2) == 0:
                self.talents.append("Unremarkable")
            else:
                self.talents.append("Resistance (Fear)")
            if np.random.randint(0, 2) == 0:
                self.characteristics.loc["Willpower", "characteristic"] += 3
            else:
                self.characteristics.loc["Agility", "characteristic"] += 3
            if np.random.randint(0, 2) == 0:
                self.corruption += self.roll(1, 5)
            else:
                self.insanity += self.roll(1, 5)
        if self.origin[1] == "Scapegrace":
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Sleight of Hand"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Trained',
                                                                      skills_table.loc['Sleight of Hand', ['type']],
                                                                      'Basic']])])
            if np.random.randint(0, 2) == 0:
                self.characteristics.loc["Intelligence", "characteristic"] += 3
            else:
                self.characteristics.loc["Perception", "characteristic"] += 3
            if np.random.randint(0, 2) == 0:
                self.corruption += self.roll(1, 5)
            else:
                self.insanity += self.roll(1, 5)
        if self.origin[1] == "Stubjack":
            self.talents.append("Quick Draw")
            self.skills = pd.concat([self.skills, pd.DataFrame(index=["Intimidate"],
                                                               columns=['training', 'type', 'level'],
                                                               data=[['Trained',
                                                                      skills_table.loc['Intimidate', ['type']],
                                                                      'Basic']])])
            if np.random.randint(0, 2) == 0:
                self.characteristics.loc["Weapon Skill", "characteristic"] += 5
            else:
                self.characteristics.loc["Ballistic Skill", "characteristic"] += 5
            self.characteristics.loc["Fellowship", "characteristic"] -= 5
            self.insanity += self.roll(1, 5)
        if self.origin[1] == "Child of the Creed":
            self.talents.append("Unshakeable Faith")
            if np.random.randint(0, 2) == 0:
                self.characteristics.loc["Willpower", "characteristic"] += 3
            else:
                self.characteristics.loc["Fellowship", "characteristic"] += 3
            self.characteristics.loc["Weapon Skill", "characteristic"] -= 3
        if self.origin[1] == "Savant":
            if np.random.randint(0, 2) == 0:
                self.skills = pd.concat([self.skills, pd.DataFrame(index=["Logic"],
                                                                   columns=['training', 'type', 'level'],
                                                                   data=[['Trained',
                                                                          skills_table.loc['Logic', ['type']],
                                                                          'Basic']])])
            else:
                self.talents.append("Peer (Academic)")
            if np.random.randint(0, 2) == 0:
                self.characteristics.loc["Intelligence", "characteristic"] += 3
            else:
                self.characteristics.loc["Fellowship", "characteristic"] += 3
            self.characteristics.loc["Toughness", "characteristic"] -= 3
        if self.origin[1] == "Vaunted":
            self.talents.append("Decadence")
            if np.random.randint(0, 2) == 0:
                self.characteristics.loc["Agility", "characteristic"] += 3
            else:
                self.characteristics.loc["Fellowship", "characteristic"] += 3
            self.characteristics.loc["Perception", "characteristic"] -= 3
            self.corruption += self.roll(1, 5)

    def generate_mutations(self):
        mutant_roll: int = sum(self.roll(1, 100))
        if mutant_roll < 6:
            self.traits.append(f"Mutant: {mutations[0]}")
            self.talents.append("-20 to Fellowship Tests to interact with \'Normals\'")
            self.talents.append("+10 to Intimidate Tests")
        elif mutant_roll < 11:
            self.traits.append(f"Mutant: {mutations[1]}")
            self.talents.append("Natural Armour 2")
        elif mutant_roll < 16:
            self.traits.append(f"Mutant: {mutations[2]}")
            self.talents.append("Cannot take Run action")
            self.characteristics.loc["Agility", "characteristic"] -= sum(self.roll(2, 10))
        elif mutant_roll < 21:
            self.traits.append(f"Mutant: {mutations[3]}")
            self.talents.append("Iron Jaw")
            self.wounds += 5
        elif mutant_roll < 26:
            self.traits.append(f"Mutant: {mutations[4]}")
            self.characteristics.loc["Strength", "characteristic"] += 10
            self.characteristics.loc["Toughness", "characteristic"] += 10
        elif mutant_roll < 31:
            self.traits.append(f"Mutant: {mutations[5]}")
            self.talents.append("Dark Sight Trait")
            self.talents.append("-10 to all Tests when in bright light unless eyes shielded & skin covered")
        elif mutant_roll < 36:
            self.traits.append(f"Mutant: {mutations[6]}")
            self.roll(4, 10)
            rolls = self.roll_history[-4:]
            for roll in range(-4, 0):
                if rolls[roll] < 6:
                    self.characteristics.iloc[roll, 2] -= sum(self.roll(1, 10))
                elif rolls[roll] < 8:
                    characteristic = self.characteristics.iloc[roll, 0] + self.characteristics.iloc[roll, 2]
                    characteristic = int(characteristic / 2)
                    self.characteristics.iloc[roll, 2] -= characteristic
                elif rolls[roll] < 10:
                    pass
                else:
                    characteristic = self.characteristics.iloc[roll, 0] + self.characteristics.iloc[roll, 2]
                    self.characteristics.iloc[roll, 2] -= characteristic - 5
            self.insanity += sum(self.roll(1, 10))
        elif mutant_roll < 41:
            self.traits.append(f"Mutant: {mutations[7]}")
            self.characteristics.loc["Weapon Skill", "characteristic"] -= 10
            self.characteristics.loc["Ballistic Skill", "characteristic"] -= 10
            self.talents.append("-20 to all Tests involving fine physical manipulation")
        elif mutant_roll < 46:
            self.traits.append(f"Mutant: {mutations[8]}")
            self.talents.append("+20 to Toughness Tests to resist poison")
            self.characteristics.loc["Toughness", "characteristic"] -= sum(self.roll(1, 10))
            self.characteristics.loc["Intelligence", "characteristic"] -= self.roll(1, 10)
            self.talents.append("1d10 damage ignoring Armour & Toughness to any creature that fails a "
                                "difficult (-10) Toughness Test when coming into contact with the Mutant's blood")
        elif mutant_roll < 51:
            self.traits.append(f"Mutant: {mutations[9]}")
            self.talents.append("Hulking Size Trait")
            self.characteristics.loc["Strength", "characteristic"] -= sum(self.roll(1, 10))
            self.wounds += 5
        elif mutant_roll < 56:
            self.traits.append(f"Mutant: {mutations[10]}")
            self.talents.append("Psy Rating 2")
            if self.psy >= 2:
                # Check later how psy works! Modify if needed.
                self.psy += 1  # Should gain "next highest Psy Rating Talent that it doesn't have."
            # Gain TWO Psychic Techniques of his choice from the discipline of his choice.
            #
            # Check PSY later!
        elif mutant_roll < 60:
            self.traits.append(f"Mutant: {mutations[11]}")
            self.talents.append("Fear 1 Trait")
        elif mutant_roll < 64:
            self.traits.append(f"Mutant: {mutations[12]}")
            self.characteristics.loc["Strength", "characteristic"] += 10
            self.characteristics.loc["Agility", "characteristic"] += 10
            self.characteristics.loc["Intelligence", "characteristic"] -= sum(self.roll(1, 10))
            self.characteristics.loc["Fellowship", "characteristic"] -= 10
        elif mutant_roll < 68:
            self.traits.append(f"Mutant: {mutations[13]}")
            self.characteristics.loc["Intelligence", "characteristic"] -= sum(self.roll(1, 10))
            self.characteristics.loc["Fellowship", "characteristic"] -= sum(self.roll(1, 10))
            roll = self.roll(1, 10)
            if roll < 4:
                self.talents.append("Frenzy")
            elif roll < 8:
                self.talents.append("Fearless")
            else:
                self.talents.append("From Beyond Trait")
        elif mutant_roll < 71:
            self.traits.append(f"Mutant: {mutations[14]}")
            ravaged_roll = sum(self.roll(1, 5))
            for i in range(0, ravaged_roll + 1):
                self.generate_mutations()
            self.talents.append("Obvious touch of Chaos regardless of the nature of mutations")
        elif mutant_roll < 75:
            self.traits.append(f"Mutant: {mutations[15]}")
            if np.random.randint(0, 2) == 0:
                self.talents.append("Natural Weapon 1 Trait (I damage)")
            else:
                self.talents.append("Natural Weapon 1 Trait (R damage)")
        elif mutant_roll < 79:
            self.traits.append(f"Mutant: {mutations[16]}")
            self.characteristics.loc["Toughness", "characteristic"] += 10
            self.talents.append("Regeneration Trait")
            self.talents.append("Must eat copious amounts of raw meat or starve")
        elif mutant_roll < 82:
            self.traits.append(f"Mutant: {mutations[17]}")
            self.talents.append("Fear 2 for the round when critical damage was taken by the Mutant")
        elif mutant_roll < 86:
            self.traits.append(f"Mutant: {mutations[18]}")
            self.talents.append("Toxic Trait")
        elif mutant_roll < 90:
            self.traits.append(f"Mutant: {mutations[19]}")
            self.talents.append("Unnatural Strength Trait")
        elif mutant_roll < 92:
            self.traits.append(f"Mutant: {mutations[20]}")
            self.talents.append("Ambidexterous")
            self.talents.append("Two Weapon Wielder")
            self.talents.append("+10 Climb Tests")
            self.talents.append("+10 Grapple Attacks")  # Check grapple attacks later.
        elif mutant_roll < 94:
            self.traits.append(f"Mutant: {mutations[21]}")
            self.wounds += 5
            self.talents.append("Crawler Trait")
        elif mutant_roll == 94:
            self.traits.append(f"Mutant: {mutations[22]}")
            self.talents.append("Fear 3 Trait")
        elif mutant_roll == 95:
            self.traits.append(f"Mutant: {mutations[23]}")
            self.characteristics.loc["Agility", "characteristic"] += 10
            self.talents.append("+20 Climb Tests")
            self.talents.append("+20 Grapple Attacks")  # Check grapple attacks later.
            self.talents.append("Can fit through spaces 1/4 its usual dimensions")
        elif mutant_roll == 96:
            self.traits.append(f"Mutant: {mutations[24]}")
            self.talents.append("Flyer Trait at a rate equal to its AB*2")  # Check what AB is...
        elif mutant_roll == 97:
            self.traits.append(f"Mutant: {mutations[25]}")
            self.talents.append("Unnatural Toughness Trait")
            self.talents.append("Cannot take Run action")
        elif mutant_roll == 98:
            self.traits.append(f"Mutant: {mutations[26]}")
            self.talents.append("Phase Trait")
            self.characteristics.loc["Strength", "characteristic"] -= 10
            self.characteristics.loc["Toughness", "characteristic"] -= 10
        elif mutant_roll == 99:
            self.traits.append(f"Mutant: {mutations[27]}")
            self.talents.append("1d10+2 R (or E) Tearing Damage close combat attack using full action, attacker must "
                                "test Ballistic Skill to use; may be dodged, but not parried")  # Check attacks
        else:
            self.traits.append(f"Mutant: {mutations[-1]}")
            self.talents.append("Deamonic Trait")
            self.talents.append("Fear 2 Trait")
            self.talents.append("From Beyond Trait")

    def generate_lure_stats(self):
        if self.origin[2] == "Tainted":
            lure_random = np.random.randint(0, 3)
            if lure_random < 1:
                self.generate_mutations()
            elif lure_random < 2:
                self.traits.append("Insane")
                if np.random.randint(0, 2) == 0:
                    self.characteristics.loc["Fellowship", "characteristic"] -= 3
                else:
                    self.fate -= 1
                self.characteristics.loc["Toughness", "characteristic"] += 3
                self.talents.append("Peer (The Insane)")
            else:
                self.traits.append("Deviant Philosophy")
                self.characteristics.loc["Willpower", "characteristic"] += 3
                self.talents.append("Enemy (Ecclesiarchy)")
        if self.origin[2] == "Criminal":
            lure_random = np.random.randint(0, 3)
            if lure_random < 1:
                self.traits.append("Wanted Fugitive")
                self.talents.append("Enemy (Ecclesiarchy)")
                self.talents.append("Peer (Underworld)")
            elif lure_random < 2:
                self.traits.append("Wanted by a Crime Baron")
                self.characteristics.loc["Perception", "characteristic"] += 3
                self.talents.append("Enemy (Underworld)")
            else:
                self.traits.append("Judged and Found Wanting")
                self.characteristics.loc["Fellowship", "characteristic"] -= 5
                self.talents.append("poor-Craftsmanship Bionic Limb or Implant (upgrades: -200XP/-300XP => common/good")
        if self.origin[2] == "Renegade":
            lure_random = np.random.randint(0, 3)
            if lure_random < 1:
                self.traits.append("Recidivist")
                self.talents.append("Enemy (Adeptus Arbites)")
                self.talents.append("Resistance (Interrogation)")
                self.skills = pd.concat([self.skills, pd.DataFrame(index=["Concealment"],
                                                                   columns=['training', 'type', 'level'],
                                                                   data=[['Trained',
                                                                         skills_table.loc['Concealment', ['type']],
                                                                         'Basic']])])
            elif lure_random < 2:
                self.traits.append("")
                pass
            else:
                self.traits.append("")
                pass
        if self.origin[2] == "Duty Bound":
            lure_random = np.random.randint(0, 3)
            if lure_random < 1:
                self.traits.append("")
                pass
            elif lure_random < 2:
                self.traits.append("")
                pass
            else:
                self.traits.append("")
                pass
        if self.origin[2] == "Zealot":
            lure_random = np.random.randint(0, 3)
            if lure_random < 1:
                self.traits.append("")
                pass
            elif lure_random < 2:
                self.traits.append("")
                pass
            else:
                self.traits.append("")
                pass
        if self.origin[2] == "Chosen by Destiny":
            lure_random = np.random.randint(0, 3)
            if lure_random < 1:
                self.traits.append("")
                pass
            elif lure_random < 2:
                self.traits.append("")
                pass
            else:
                self.traits.append("")
                pass

    def generate_trials_stats(self):
        if self.origin[3] == "The Hand of War":
            pass
        if self.origin[3] == "Press-Ganged":
            pass
        if self.origin[3] == "Calamity":
            pass
        if self.origin[3] == "Ship-Lorn":
            pass
        if self.origin[3] == "Dark Voyage":
            pass
        if self.origin[3] == "High Vendetta":
            pass

    def generate_motivation_stats(self):
        if self.origin[4] == "Endurance":
            pass
        if self.origin[4] == "Fortune":
            pass
        if self.origin[4] == "Vengeance":
            pass
        if self.origin[4] == "Renown":
            pass
        if self.origin[4] == "Pride":
            pass
        if self.origin[4] == "Prestige":
            pass

    def generate_career_stats(self):
        if self.origin[5] == "x":
            pass
        if self.origin[5] == "x":
            pass
        if self.origin[5] == "x":
            pass
        if self.origin[5] == "x":
            pass
        if self.origin[5] == "x":
            pass
        if self.origin[5] == "x":
            pass

    def recalc_stats(self):
        for index in self.characteristics.index:
            self.characteristics.loc[index, "bonus"]: int = np.trunc(
                self.characteristics.loc[index, "characteristic"] / 10).astype(int)

    def generate_stats(self):
        for index in self.characteristics.index:
            self.characteristics.loc[index, "characteristic"] = sum(self.roll(2, 10)) + 25
            self.characteristics.loc[index, "bonus_multiplier"]: float = 1.0

        old_state: int = 0
        for x in range(0, origins_index):

            origin_row: list = []
            for y in range(0, origins_columns):
                if origins.iloc[x, y] is not None:
                    origin_row.append(origins.iloc[x, y])

            if x == 0:
                old_state = np.random.randint(0, len(origin_row))
                # Add first row of origin:
                self.origin.append(origin_row[old_state])
            elif x < (origins_index - 1):
                new_state = old_state
                if new_state == 0:
                    new_state += np.random.randint(0, 2)
                    old_state = new_state
                elif new_state == len(origin_row) - 1:
                    new_state -= np.random.randint(0, 2)
                    old_state = new_state
                else:
                    new_state += np.random.randint(low=-1, high=2)
                    old_state = new_state
                self.origin.append(origin_row[new_state])
            else:
                old_state += np.random.randint(low=0, high=3)
                self.origin.append(origin_row[old_state])
        self.generate_home_world_stats()
        self.generate_lure_stats()
        self.generate_trials_stats()
        self.generate_motivation_stats()
        self.generate_career_stats()
        self.recalc_stats()

    @property
    def show_stats(self):
        print(f"Name: {self.name}, Kind: {self.kind}, Level: {self.level}")
        print(f"Characteristics: {self.characteristics}")
        print(f"Origin: {self.origin}")
        print(f"Traits: {self.traits}")
        print(f"Skills: {self.skills}")
        print(f"Talents: {self.talents}")
        print(f"Wounds: {self.wounds}, Fate: {self.fate}, Initiative modifier: {self.initiative_modifier}, Psy rating: "
              f"{self.psy}")
        print(f"Corruption points: {self.corruption}, Insanity points: {self.insanity}")
        print(f"Profit factor: {self.profit_factor}")
        # skills_table.to_csv('skills_table.csv', sep=';')
        # print(f"Dice rolls history: {self.roll_history}")
        return None
