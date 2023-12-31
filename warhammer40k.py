# Imports.

import numpy as np
import pandas as pd

# Local data setup:
male_names = pd.DataFrame(
    columns=['Roll', 'Primitive', 'Low', 'High', 'Archaic', 'Informal'],
    data=[[7, 'Artho', 'Aubray', 'Alessaunder', 'Aestaban', 'Alt'],
          [13, 'Bron', 'Cort', 'Aphesius', 'Casmirre', 'Blade'],
          [19, 'Carno', 'Emil', 'Cornelius', 'Gillam', 'Cutter'],
          [25, 'Hob', 'Harmon', 'Darrius', 'Haddon', 'Echo'],
          [31, 'Gil', 'Jace', 'Fortunus', 'Jonstonne', 'Gant'],
          [37, 'Jorn', 'Lucius', 'Godwinne', 'Kennoch', 'Hal'],
          [43, 'Kerghan', 'Malakai', 'Holt', 'Mordechai', 'Jak'],
          [49, 'Lok', 'Nathin', 'Jarrion', 'Orthesian', 'Mord'],
          [55, 'Marn', 'Remi', 'Macharius', 'Patronius', 'Notch'],
          [61, 'Pak', 'Roland', 'Quinilli', 'Ramirez', 'Rook'],
          [67, 'Quinn', 'Solar', 'Regias', 'Sebastion', 'Sawyer'],
          [73, 'Stiehr', 'Theodore', 'Sarvus', 'Siegmund', 'Serge'],
          [79, 'Thale', 'Vorgen', 'Tristan', 'Torian', 'Stubbs'],
          [85, 'Vir', 'Ysarille', 'Victris', 'Vendigroth', 'Torque'],
          [91, 'Ziel', 'Zacharie', 'Xanatov', 'Yorke', 'Veche']]
)
female_names = pd.DataFrame(
    columns=['Roll', 'Primitive', 'Low', 'High', 'Archaic', 'Informal'],
    data=[[7, 'Attie', 'Barbaretta', 'Anarette', 'Anastasia', 'Astra'],
          [13, 'Besse', 'Cynthia', 'Carnelia', 'Cymbry', 'Blur'],
          [19, 'Flur', 'Diane', 'Dominique', 'Esailla', 'Ceile'],
          [25, 'Halia', 'Dorath', 'Faydra', 'Iioneyse', 'Crimson'],
          [31, 'Jessie', 'Elisabet', 'Inessa', 'Janelle', 'Flora'],
          [37, 'Karina', 'Faye', 'Janthine', 'Lorayne', 'Guile'],
          [43, 'Marra', 'Genevie', 'Lucretia', 'Katyaina', 'Luna'],
          [49, 'Narine', 'Isabelle', 'Marcella', 'Miriam', 'Mia'],
          [55, 'Ovina', 'Jayne', 'Jama', 'Nadeyse', 'Poise'],
          [61, 'Ralle', 'Josette', 'Noradine', 'Petriam', 'Rosa'],
          [67, 'Salia', 'Noemi', 'Regina', 'Serafina', 'Sola'],
          [73, 'Tassa', 'Odette', 'Symonne', 'Tarvanna', 'Trenne'],
          [79, 'Unna', 'Shandra', 'Winter', 'Undynne', 'Val'],
          [85, 'Vyn', 'Tanda', 'Yolande', 'Victrix', 'Xandra'],
          [91, 'Yasha', 'Zolla', 'Zamora', 'Zephyr', 'Zelle']]
)
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
                                   "Pilot (Flyers)", "Pilot (Space Craft)", "Scholastic Lore (Archaic)",
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
skills_table = pd.concat([skills_table, skill_groups])
skills_table.sort_index(inplace=True)
items_table = pd.DataFrame(
    index=["Heirloom (Archeotech Laspistol)", "Heirloom (Angevin Era Chainsword)", "Heirloom (Ancestral Seal)",
           "Heirloom (Saint-Blessed Carapace Armour)", "Heirloom (Reliquary of Saint Drusus)"],
    columns=["count", "state", "description"],
    data=[[1, 'Best-Craftsmanship', 'archeotech laspistol'],
          [1, 'Best-Craftsmanship', 'chainsword'],
          [1, None, '+10 to all Interaction Tests when showing the seal to Imperial citizens and organizations'],
          [1, 'Best-Craftsmanship', 'set od carapace armour'],
          [1, None, '+20 to all Interaction Tests when showing the reliquary to members of the Ministorum']]
)
enemy_groups = ["Academics", "Adepta Sororitas", "Adeptus Arbites", "Adeptus Mechanicus", "Administratum", "Astropaths",
                "Ecclesiarchy", "Government", "Imperial Guard", "Imperial Navy", "Inquisition", "Military",
                "Navigators", "Nobility", "Rogue Trader", "Underworld", "Workers"]
good_rep_groups = ["Academics", "Adeptus Arbites", "Adeptus Mechanicus", "Administratum", "Astropaths", "Ecclesiarchy",
                   "Feral Worlders", "Government", "Hivers", "Imperial Guard", "Imperial Navy", "Inquisition",
                   "Middle Classes", "Nobility", "the Insane", "Underworld", "Void Born", "Workers"]
hatred_groups = ["Criminals", "Rogue Trader (specific)", "Pirates", "Xeno (specific)", "Psykers", "Mutants"]
peer_groups = ["Academics", "Adeptus Arbites", "Adeptus Mechanicus", "Administratum", "Astropaths", "Ecclesiarchy",
               "Feral Worlders", "Government", "Hivers", "Inquisition", "Middle Classes", "Military", "Nobility",
               "the Insane", "Underworld", "Void Born", "Workers"]
rival_groups = ["Academics", "Adepta Sororitas", "Adeptus Arbites", "Adeptus Mechanicus", "Administratum", "Astropaths",
                "Ecclesiarchy", "Government", "Imperial Guard", "Imperial Navy", "Inquisition", "Middle Classes",
                "Military", "Navigators", "Nobility", "Rogue Traders", "Underworld", "Workers"]
demeanours = dict(Bilious="Suspicious, bitter, and angry, yet very watchful and aware.",
                  Cardinal="Seeks careful balance in all things, yet often struggles to make a vital choice rapidly.",
                  Choleric="Always active and taking charge, yet easy to provoke to anger.",
                  Fixed="Solid, unyielding, and definitive in all things. Considered and settled of opinion.",
                  Melancholic="Thoughtful, introspective, and prone to fits of gloom.",
                  Mutable="Unpredictable, undisciplined, and rebellious, defined by opposition to ideals.",
                  Phlegmatic="Practical and careful, yet very serious and reserved.",
                  Sanguine="Confident and optimistic, but prone to visions and flights of whimsy.",
                  Supine="Loyal, devout, and easily led.")
profit_ship = pd.DataFrame(columns=['Roll', 'Profit Factor', 'Ship Points'],
                           data=[[2, 60, 30],
                                 [4, 50, 40],
                                 [8, 40, 50],
                                 [10, 30, 60],
                                 [11, 20, 70]])


class Creature:
    def __init__(self):
        self.sex = 'Male'
        self.name = male_names.iloc[0, 1]
        self.kind = "Human"
        self.rank = 1
        self.rolls: list = []
        self.characteristics = pd.DataFrame(index=["Weapon Skill", "Ballistic Skill", "Strength", "Toughness",
                                                   "Agility", "Intelligence", "Perception", "Willpower",
                                                   "Fellowship"],
                                            columns=["characteristic", "bonus", "bonus_multiplier"])
        self.origin: list = []
        self.skills = pd.DataFrame(index=None, columns=['training', 'rank'])
        self.talents: list = []
        self.traits: list = []
        self.demeanour: dict = {}
        self.wounds: int = 0
        self.fate: int = 0
        self.initiative_modifier: int = 0
        self.profit_factor: int = 0
        self.ship_points: int = 0
        self.corruption: int = 0
        self.insanity: int = 0
        self.psy = 0
        self.items = pd.DataFrame(columns=["count", "state", "description"])
        self.xp = dict(left=5000, spent=0)

    def roll(self, dice_number: int = 1, dice_sides: int = 6):
        roll = []
        for i in range(0, dice_number):
            roll.append(np.random.randint(1, dice_sides + 1))
        self.rolls.append(roll)
        return sum(self.rolls[-1])

    def generate_random_name(self, sex='Male'):
        name_roll = self.roll(1, 100)
        random_col = np.random.randint(1, len(male_names.iloc[0]))
        if sex == 'Male':
            if name_roll > 90:
                return self.generate_random_name(sex='Female')
            else:
                name_roll = (name_roll - 1) // 6
                random_name = male_names.iloc[name_roll, random_col]
        else:
            if name_roll > 90:
                return self.generate_random_name()
            else:
                name_roll = (name_roll - 1) // 6
                random_name = female_names.iloc[name_roll, random_col]
        return random_name

    def add_skill(self, skill_name: str, training: str = 'Trained', skill_type=None, upgrade=True):
        # Prevent from adding an existing skill
        if skill_name not in self.skills.index:
            self.skills.loc[skill_name] = [training, skill_type]
        elif upgrade:
            if self.skills.loc[skill_name, 'training'] == 'Untrained':
                self.skills.loc[skill_name] = ['trained', skill_type]
            elif self.skills.loc[skill_name, 'training'] == 'Trained':
                self.skills.loc[skill_name] = ['Mastery I', skill_type]
            else:
                self.skills.loc[skill_name] = ['Mastery II', skill_type]

    def generate_home_world_stats(self):
        if self.origin[0] == "Death World":
            self.characteristics.loc["Strength", "characteristic"] += 5
            self.characteristics.loc["Toughness", "characteristic"] += 5
            self.characteristics.loc["Willpower", "characteristic"] -= 5
            self.characteristics.loc["Fellowship", "characteristic"] -= 5
            self.add_skill('Survival')
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
            self.wounds += self.roll(1, 5) + 2
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            roll = self.roll(1, 10)
            if roll < 6:
                self.fate = 2
            else:
                self.fate = 3
        elif self.origin[0] == "Void Born":
            self.characteristics.loc["Strength", "characteristic"] -= 5
            self.characteristics.loc["Willpower", "characteristic"] += 5
            self.add_skill("Speak Language (Ship Dialect)")
            self.traits.append("Charmed")
            self.talents.append("Roll natural 9 on 1d10 when spending Fate Point => FP NOT spent")
            self.traits.append("Ill-Omened")
            self.talents.append("-5 to all Fellowship Tests interacting with non-void born humans")
            self.traits.append("Shipwise")
            self.add_skill("Navigation (Stellar)", 'Untrained', 'Basic')
            self.add_skill("Pilot (Space Craft)", 'Untrained', 'Basic')
            self.traits.append("Void Accustomed")
            self.talents.append("Immune to space travel sickness")
            self.talents.append("Zero- & low-gravity environments => NOT Difficult Terrain")
            self.wounds += self.roll(1, 5)
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            roll = self.roll(1, 10)
            if roll < 6:
                self.fate = 3
            else:
                self.fate = 4
        elif self.origin[0] == "Forge World":
            self.characteristics.loc["Weapon Skill", "characteristic"] -= 5
            self.characteristics.loc["Intelligence", "characteristic"] += 5
            self.add_skill("Common Lore (Tech)", 'Untrained', 'Basic')
            self.add_skill("Common Lore (Machine Cult)", 'Untrained', 'Basic')
            self.traits.append("Credo Omnissiah")
            self.talents.append("Technical Knock")
            self.traits.append("Fit for Purpose")
            chosen_chr = np.random.randint(0, 9)
            self.talents.append(f"+3 to a chosen Characteristic: {self.characteristics.index[chosen_chr]}")
            self.characteristics.iloc[chosen_chr, 0] += 3
            self.traits.append("Stranger to the Cult")
            self.talents.append("-10 to all Tests involving knowledge of the Imperial Creed")
            self.talents.append("-5 to all Fellowship Tests interacting with Ecclesiarchy in formal settings")
            self.wounds += self.roll(1, 5) + 1
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            roll = self.roll(1, 10)
            if roll < 6:
                self.fate = 2
            elif roll < 10:
                self.fate = 3
            else:
                self.fate = 4
        elif self.origin[0] == "Hive World":
            self.characteristics.loc["Toughness", "characteristic"] -= 5
            self.characteristics.loc["Fellowship", "characteristic"] += 5
            self.add_skill("Speak Language (Hive Dialect)", 'Untrained', 'Basic')
            self.traits.append("Accustomed to Crowds")
            self.talents.append("Crowds => NOT Difficult Terrain")
            self.talents.append("Running or Charging through dense crowd => NO penalty to Agility Tests to keep "
                                "creature's feet")
            self.traits.append("Caves of Steel")
            self.add_skill("Tech-Use", 'Untrained', 'Basic')
            self.traits.append("Hivebound")
            self.talents.append("-10 to all Survival (Int) Tests while NOT in \"Proper Habitat\"")
            self.talents.append("-5 to all Intelligence Tests while NOT in \"Proper Habitat\"")
            self.traits.append("Wary")
            self.initiative_modifier += 1
            self.wounds += self.roll(1, 5) + 1
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            roll = self.roll(1, 10)
            if roll < 6:
                self.fate = 2
            elif roll < 9:
                self.fate = 3
            else:
                self.fate = 4
        elif self.origin[0] == "Imperial World":
            self.characteristics.loc["Willpower", "characteristic"] += 3
            self.traits.append("Blessed Ignorance")
            self.talents.append("-5 to Forbidden Lore (Int) Tests")
            self.traits.append("Hagiography")
            self.add_skill("Common Lore (Imperial Creed)")
            self.add_skill("Common Lore (Imperium)")
            self.add_skill("Common Lore (War)")
            self.traits.append("Liturgical Familiarity")
            self.add_skill("Literacy", 'Untrained', 'Basic')
            self.add_skill("Speak Language (High Gothic)", 'Untrained', 'Basic')
            self.wounds += self.roll(1, 5)
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            roll = self.roll(1, 10)
            if roll < 9:
                self.fate = 3
            else:
                self.fate = 4
        else:
            self.characteristics.loc["Willpower", "characteristic"] -= 5
            self.characteristics.loc["Fellowship", "characteristic"] += 5
            self.add_skill("Literacy", 'Untrained', 'Basic')
            self.add_skill("Speak Language (High Gothic)", 'Untrained', 'Basic')
            self.add_skill("Speak Language (Low Gothic)", 'Untrained', 'Basic')
            self.traits.append("Etiquette")
            self.talents.append("+10 to Interaction Tests when dealing with authority and in formal situations")
            self.traits.append("Legacy of Wealth")
            self.profit_factor += 1
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
            self.wounds += self.roll(1, 5)
            self.characteristics.loc["Toughness", "bonus_multiplier"]: float = 2.0
            # Determine fate points:
            roll = self.roll(1, 10)
            if roll < 4:
                self.fate = 2
            elif roll < 10:
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
        elif self.origin[1] == "Scapegrace":
            self.add_skill("Sleight of Hand", 'Trained', 'Basic')
            if np.random.randint(0, 2) == 0:
                self.characteristics.loc["Intelligence", "characteristic"] += 3
            else:
                self.characteristics.loc["Perception", "characteristic"] += 3
            if np.random.randint(0, 2) == 0:
                self.corruption += self.roll(1, 5)
            else:
                self.insanity += self.roll(1, 5)
        elif self.origin[1] == "Stubjack":
            self.talents.append("Quick Draw")
            self.add_skill("Intimidate", 'Trained', 'Basic')
            if np.random.randint(0, 2) == 0:
                self.characteristics.loc["Weapon Skill", "characteristic"] += 5
            else:
                self.characteristics.loc["Ballistic Skill", "characteristic"] += 5
            self.characteristics.loc["Fellowship", "characteristic"] -= 5
            self.insanity += self.roll(1, 5)
        elif self.origin[1] == "Child of the Creed":
            self.talents.append("Unshakeable Faith")
            if np.random.randint(0, 2) == 0:
                self.characteristics.loc["Willpower", "characteristic"] += 3
            else:
                self.characteristics.loc["Fellowship", "characteristic"] += 3
            self.characteristics.loc["Weapon Skill", "characteristic"] -= 3
        elif self.origin[1] == "Savant":
            if np.random.randint(0, 2) == 0:
                self.add_skill("Logic", 'Trained', 'Basic')
            else:
                self.talents.append("Peer (Academic)")
            if np.random.randint(0, 2) == 0:
                self.characteristics.loc["Intelligence", "characteristic"] += 3
            else:
                self.characteristics.loc["Fellowship", "characteristic"] += 3
            self.characteristics.loc["Toughness", "characteristic"] -= 3
        else:
            self.talents.append("Decadence")
            if np.random.randint(0, 2) == 0:
                self.characteristics.loc["Agility", "characteristic"] += 3
            else:
                self.characteristics.loc["Fellowship", "characteristic"] += 3
            self.characteristics.loc["Perception", "characteristic"] -= 3
            self.corruption += self.roll(1, 5)

    def generate_mutations(self):
        mutant_roll: int = self.roll(1, 100)
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
            self.characteristics.loc["Agility", "characteristic"] -= self.roll(2, 10)
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
            rolls = self.rolls[-1]
            for roll in range(0, 4):
                if rolls[roll] < 6:
                    self.characteristics.iloc[roll, 2] -= self.roll(1, 10)
                elif rolls[roll] < 8:
                    characteristic = self.characteristics.iloc[roll, 0] + self.characteristics.iloc[roll, 2]
                    characteristic = int(characteristic / 2)
                    self.characteristics.iloc[roll, 2] -= characteristic
                elif rolls[roll] < 10:
                    pass
                else:
                    characteristic = self.characteristics.iloc[roll, 0] + self.characteristics.iloc[roll, 2]
                    self.characteristics.iloc[roll, 2] -= characteristic - 5
            self.insanity += self.roll(1, 10)
        elif mutant_roll < 41:
            self.traits.append(f"Mutant: {mutations[7]}")
            self.characteristics.loc["Weapon Skill", "characteristic"] -= 10
            self.characteristics.loc["Ballistic Skill", "characteristic"] -= 10
            self.talents.append("-20 to all Tests involving fine physical manipulation")
        elif mutant_roll < 46:
            self.traits.append(f"Mutant: {mutations[8]}")
            self.talents.append("+20 to Toughness Tests to resist poison")
            self.characteristics.loc["Toughness", "characteristic"] -= self.roll(1, 10)
            self.characteristics.loc["Intelligence", "characteristic"] -= self.roll(1, 10)
            self.talents.append("1d10 damage ignoring Armour & Toughness to any creature that fails a "
                                "difficult (-10) Toughness Test when coming into contact with the Mutant's blood")
        elif mutant_roll < 51:
            self.traits.append(f"Mutant: {mutations[9]}")
            self.talents.append("Hulking Size Trait")
            self.characteristics.loc["Strength", "characteristic"] -= self.roll(1, 10)
            self.wounds += 5
        elif mutant_roll < 56:
            self.traits.append(f"Mutant: {mutations[10]}")
            self.talents.append("Psy Rating 2")
            if self.psy >= 2:
                # TODO: Check later how psy works! Modify if needed.
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
            self.characteristics.loc["Intelligence", "characteristic"] -= self.roll(1, 10)
            self.characteristics.loc["Fellowship", "characteristic"] -= 10
        elif mutant_roll < 68:
            self.traits.append(f"Mutant: {mutations[13]}")
            self.characteristics.loc["Intelligence", "characteristic"] -= self.roll(1, 10)
            self.characteristics.loc["Fellowship", "characteristic"] -= self.roll(1, 10)
            roll = self.roll(1, 10)
            if roll < 4:
                self.talents.append("Frenzy")
            elif roll < 8:
                self.talents.append("Fearless")
            else:
                self.talents.append("From Beyond Trait")
        elif mutant_roll < 71:
            self.traits.append(f"Mutant: {mutations[14]}")
            ravaged_roll = self.roll(1, 5)
            for i in range(0, ravaged_roll):
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
            self.talents.append("+10 Grapple Attacks")  # TODO: Check grapple attacks later.
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
            self.talents.append("+20 Grapple Attacks")  # TODO: Check grapple attacks later.
            self.talents.append("Can fit through spaces 1/4 its usual dimensions")
        elif mutant_roll == 96:
            self.traits.append(f"Mutant: {mutations[24]}")
            self.talents.append("Flyer Trait at a rate equal to its AB*2")  # TODO: Check what AB is...
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
                                "test Ballistic Skill to use; may be dodged, but not parried")  # TODO: Check attacks
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
        elif self.origin[2] == "Criminal":
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
        elif self.origin[2] == "Renegade":
            lure_random = np.random.randint(0, 3)
            if lure_random < 1:
                self.traits.append("Recidivist")
                self.talents.append("Enemy (Adeptus Arbites)")
                self.talents.append("Resistance (Interrogation)")
                self.add_skill("Concealment", 'Trained', 'Basic')
            elif lure_random < 2:
                self.traits.append("Free-thinker")
                if np.random.randint(0, 2) == 0:
                    self.characteristics.loc["Intelligence", "characteristic"] += 3
                else:
                    self.characteristics.loc["Perception", "characteristic"] += 3
            else:
                self.traits.append("Dark Visionary")
                if np.random.randint(0, 2) == 0:
                    self.corruption += self.roll(1, 5) + 1
                else:
                    self.insanity += self.roll(1, 5) + 1
                self.talents.append("Dark Soul")
                # This picks a random skill from a group of Forbidden Lore skills.
                forbidden_index = []
                for index in skills_table.index:
                    n = 0
                    if len(index) > 16:
                        for i in range(0, 16):
                            if index[i] == "Forbidden Lore ("[i]:
                                n += 1
                        if n > 14:
                            forbidden_index.append(index)
                forbidden_random = forbidden_index[np.random.randint(0, len(forbidden_index))]
                self.add_skill(forbidden_random, 'Trained', 'Basic')
        elif self.origin[2] == "Duty Bound":
            lure_random = np.random.randint(0, 3)
            if lure_random < 1:
                self.traits.append("Duty to the Throne")
                self.characteristics.loc['Willpower', 'characteristic'] += 3
                if self.characteristics.loc['Willpower', 'characteristic'] >= 40:
                    self.talents.append("Armour of Contempt")
                self.talents.append("-10 to Interaction Skill Tests with sources outside of the Imperium")
            elif lure_random < 2:
                self.traits.append("Duty to Humanity")
                if np.random.randint(0, 2) == 0:
                    self.characteristics.loc['Perception', 'characteristic'] += 3
                else:
                    self.characteristics.loc['Intelligence', 'characteristic'] += 3
                self.profit_factor -= 1
            else:
                self.traits.append("Duty to Your Dynasty")
                self.talents.append("Rival (Rogue Trader family")
                self.characteristics.loc['Toughness', 'characteristic'] -= 3
                self.profit_factor += 1
        elif self.origin[2] == "Zealot":
            lure_random = np.random.randint(0, 3)
            if lure_random < 1:
                self.traits.append("Blessed Scars")
                self.talents.append("+10 to Intimidate Tests")
                self.talents.append("-10 to Charm Tests")
                self.talents.append("poor-Craftsmanship Bionic Limb or Implant (upgrades: -200XP/-300XP => common/good")
            elif lure_random < 2:
                self.traits.append("Unnerving Clarity")
                self.characteristics.loc['Willpower', 'characteristic'] += 5
                if np.random.randint(0, 2) == 0:
                    self.characteristics.loc['Fellowship', 'characteristic'] -= 5
                else:
                    self.insanity += self.roll(1, 10)
            else:
                self.traits.append("Favoured of the Faithful")
                self.characteristics.loc['Fellowship', 'characteristic'] += 5
                self.talents.append("Peer (Ecclesiarchy)")
                self.characteristics.loc['Toughness', 'characteristic'] -= 5
        else:
            lure_random = np.random.randint(0, 3)
            if lure_random < 1:
                self.traits.append("Seeker of Truth")
                self.talents.append("Foresight")
                self.talents.append("Enemy (Academics of Ecclesiarchy)")
                self.characteristics.loc['Willpower', 'characteristic'] -= 3
            elif lure_random < 2:
                self.traits.append("Xenophile")
                self.talents.append("+10 to Fellowship Tests with alien races or cultures")
                self.talents.append("-10 to Willpower Tests involving alien artifacts and alien psychic powers")
            else:
                self.traits.append("Fated for Greatness")
                self.fate += 1
                self.insanity += self.roll(1, 10)

    def generate_trials_stats(self):
        if self.origin[3] == "The Hand of War":
            self.traits.append("The Ashes of War")
            if np.random.randint(0, 2) == 0:
                self.talents.append("Weapon Training (choice)")  # TODO: Check these weapon training talents later.
            else:
                self.talents.append("The Leap Up")
            hatred = "Hatred ("
            hatred_random = np.random.randint(0, 7)
            if hatred_random == 0:
                hatred += "Orks)"
            elif hatred_random == 1:
                hatred += "Eldar)"
            elif hatred_random == 2:
                hatred += "mutants)"
            elif hatred_random == 3:
                hatred += "Chaos worshipers)"
            elif hatred_random == 4:
                hatred += "the Imperial Guard)"
            elif hatred_random == 5:
                hatred += "the Imperial Navy)"
            else:
                hatred += "void pirates)"
            self.talents.append(hatred)
            self.traits.append("The Face of the Enemy")
            self.talents.append("-10 to all Fellowship Tests involving sworn enemies")
            self.talents.append("Slightest provocation from sworn enemies results in violent reaction save successful "
                                "Willpower Test (modified by the provocation and consequences of the reaction")
        elif self.origin[3] == "Press-Ganged":
            # May gain skill if it has "no prerequisites". TODO: Add prerequisites and character progression.
            self.traits.append("Unwilling Accomplice")
            press_ganged = skills_table.index.values.tolist()
            for index in self.skills.index.values.tolist():
                press_ganged.remove(index)
            press_ganged = press_ganged[np.random.randint(0, len(press_ganged))]
            self.add_skill(press_ganged)
            # This picks a random skill from a group of Common Lore skills.
            common_lore_index = []
            for index in skills_table.index:
                n = 0
                if len(index) > 13:
                    for i in range(0, 13):
                        if index[i] == "Common Lore ("[i]:
                            n += 1
                    if n > 11:
                        common_lore_index.append(index)
            common_random = common_lore_index[np.random.randint(0, len(common_lore_index))]
            self.add_skill(common_random)
            self.traits.append("Jealous Freedom")
            self.talents.append("Prospect of imprisonment or loss of freedom results in violent reaction save "
                                "successful Willpower Test (modified by the provocation and consequences of the "
                                "reaction")
        elif self.origin[3] == "Calamity":
            self.traits.append("Inured to Adversity")
            self.talents.append("Light Sleeper")
            if np.random.randint(0, 2) == 0:
                self.talents.append("Hardy")
            else:
                self.talents.append("Nerves of Steel")
            self.traits.append("Echo of Hard Times")
            self.profit_factor -= 1
        elif self.origin[3] == "Ship-Lorn":
            self.traits.append("Against All Odds")
            if np.random.randint(0, 2):
                self.add_skill("Survival")
            else:
                self.talents.append("Dark Soul")
            self.talents.append("May re-roll the dice when spending Fate Points to recover Wounds, but must accept "
                                "the result")
            self.traits.append("Ill-Starred")
            self.fate -= 1
            self.talents.append("-5 on Fellowship Tests interacting with Void Born, Rogue Traders, and other "
                                "voidfarers who are not personal friends and know the background and reputation")
        elif self.origin[3] == "Dark Voyage":
            self.traits.append("Things Man Was Not Meant to Know")
            if np.random.randint(0, 2):
                # This picks a random skill from a group of Forbidden Lore skills.
                forbidden_index = []
                for index in skills_table.index:
                    n = 0
                    if len(index) > 16:
                        for i in range(0, 16):
                            if index[i] == "Forbidden Lore ("[i]:
                                n += 1
                        if n > 14:
                            forbidden_index.append(index)
                forbidden_random = forbidden_index[np.random.randint(0, len(forbidden_index))]
                self.add_skill(forbidden_random, 'Trained', 'Basic', upgrade=True)
            else:
                self.talents.append("Resistance (Fear)")
            self.traits.append("Marked by Darkness")
            self.insanity += self.roll(1, 5)
        else:
            self.traits.append("Blood Will Have Blood")
            if np.random.randint(0, 2):
                self.talents.append("Die Hard")
            else:
                self.talents.append("Paranoia")
            self.add_skill("Inquiry", upgrade=True)
            self.traits.append("Brook No Insult")
            self.talents.append("Offence to honour and person or those under creature's protection results in violent "
                                "reaction save successful Willpower Test (modified by the provocation and "
                                "consequences of the reaction")

    def generate_motivation_stats(self):
        if self.origin[4] == "Endurance":
            self.wounds += 1
        elif self.origin[4] == "Fortune":
            self.fate += 1
        elif self.origin[4] == "Vengeance":
            self.talents.append(f"Hatred ({hatred_groups[np.random.randint(0, len(hatred_groups))]})")
        elif self.origin[4] == "Renown":
            if np.random.randint(0, 2) == 0:
                self.talents.append("Air of Authority")
            else:
                self.talents.append(f"Peer ({peer_groups[np.random.randint(0, len(peer_groups))]})")
        elif self.origin[4] == "Pride":
            roll = self.roll(1, 100)
            if roll < 21:
                self.items.loc[items_table.index[0]] = items_table.iloc[0]
            elif roll < 41:
                self.items.loc[items_table.index[1]] = items_table.iloc[1]
            elif roll < 61:
                self.items.loc[items_table.index[2]] = items_table.iloc[2]
            elif roll < 81:
                self.items.loc[items_table.index[3]] = items_table.iloc[3]
            else:
                self.items.loc[items_table.index[4]] = items_table.iloc[4]
        else:
            if np.random.randint(0, 2) == 0:
                skill_names_list = skills_table.index.values.tolist()
                self.talents.append(f"Talented ({skill_names_list[np.random.randint(0, len(skill_names_list))]})")
            else:
                self.talents.append(f"Peer ({peer_groups[np.random.randint(0, len(peer_groups))]})")

    # TODO: Selecting a Starship

    # TODO: Selecting equipment

    def generate_career_stats(self):
        """
        Note: This function ignores the possibility of gaining an Elite Advance.
        Progression possibilities:
        1. Characteristic Advance (+5 to the characteristic each):
           Simple (250 xp) -> Intermediate (500 xp) -> Trained (750 xp) -> Expert (1000 xp)
        2. Rank Increase:
           Rank xp level
           1    5000-6999
           2    7000-9999
           3    10000-12999
           4    13000-16999
           5    17000-20999
           6    21000-24999
           7    25000-29999
           8    30000-34999
        3. Skill or Talent Advance
        """
        if self.origin[5] == "Astropath Transcendent":
            self.add_skill("Awareness")
            self.add_skill("Common Lore (Adeptus Astra Telepathica)")
            self.add_skill("Forbidden Lore (Psykers)")
            self.add_skill("Invocation")
            self.add_skill("Psyniscience")
            self.add_skill("Scholastic Lore (Cryptology)")
            self.add_skill("Speak Language (High Gothic)")
            self.add_skill("Speak Language (Low Gothic)")
            self.talents.append("Pistol Weapon Training (Universal)")
            self.talents.append("Heightened Senses")
            self.talents.append("Melee Weapon Training (Universal)")
            self.psy += 2
            weapon = np.random.choice(['laspistol', 'stub automatic'])
            if weapon == 'laspistol':
                self.items.loc["Laspistol"] = [1, 'Best-Craftsmanship', weapon]
            else:
                self.items.loc["Stub Automatic"] = [1, 'Best-Craftsmanship', weapon]
            weapon = np.random.choice(['mono-sword', 'shock staff'])
            if weapon == 'mono-sword':
                self.items.loc["Mono-Sword"] = [1, 'Best-Craftsmanship', weapon]
            else:
                self.items.loc["Shock Staff"] = [1, 'Common-Craftsmanship', weapon]
            self.items.loc["Guard Flak Armour"] = [1, None, 'guard flak armour']
            self.items.loc["Charm"] = [1, None, 'charm']
            self.items.loc["Void Suit"] = [1, None, 'void suit']
            self.items.loc["Micro-Bead"] = [1, None, 'micro-bead']
            self.items.loc["Psy-Focus"] = [1, None, 'psy-focus']

        elif self.origin[5] == "Arch-Militant":
            self.add_skill("Common Lore (War)")
            self.add_skill("Dodge")
            self.add_skill("Intimidate")
            self.add_skill("Scholastic Lore (Tactica Imperialis)")
            self.add_skill("Secret Tongue (Military)")
            self.add_skill("Speak Language (Low Gothic)")
            self.talents.append("Basic Weapon Training (Universal)")
            self.talents.append("Pistol Weapon Training (Universal)")
            self.talents.append("Melee Weapon Training (Universal)")
            self.talents.append("Thrown Weapon Training (Universal)")
            self.talents.append("Sound Constitution")
            weapon = np.random.choice(['hellgun', 'hunting rifle', 'bolt pistol'])
            if weapon == 'hellgun':
                self.items.loc["Hellgun"] = [1, 'Good-Craftsmanship', weapon]
            elif weapon == 'hunting rifle':
                self.items.loc["Hunting Rifle"] = [1, 'Best-Craftsmanship', weapon]
            else:
                self.items.loc["Bolt Pistol"] = [2, 'Best-Craftsmanship', weapon]
            self.items.loc["Primitive Melee Weapon (of choice)"] = [1, 'Good-Craftsmanship',
                                                                    'primitive melee weapon + mono upgrade']
            loot = np.random.choice(['wanted bounties', 'arms coffer', 'stimm'])
            if loot == 'wanted bounties':
                self.items.loc["Data-Slate Full of Wanted Bounties"] = [1, None, 'lots of wanted bounties']
            elif loot == 'arms coffer':
                self.items.loc["Arms Coffer"] = [1, None, 'arms coffer']
            else:
                self.items.loc["Stimm Doses"] = [3, None, 'stimm']
            self.items.loc["Micro-Bead"] = [1, None, 'micro-bead']
            self.items.loc["Void Suit"] = [1, None, 'void suit']
            self.items.loc['Enforcer Light Carapace Armour'] = [1, None, 'armour']
            self.items.loc["Bolt Shell Keepsake"] = [1, None, 'keepsake']
            self.items.loc["Medikit"] = [1, None, 'medikit']
            self.items.loc["Manacles"] = [1, None, 'manacles']

        elif self.origin[5] == "Void-Master":
            self.add_skill("Common Lore (Imperial Navy)")
            self.add_skill("Forbidden Lore (Xenos)")
            self.add_skill("Navigation (Stellar)")
            self.add_skill("Pilot (Space Craft)")
            self.add_skill("Pilot (Flyers)")
            self.add_skill("Scholastic Lore (Astromancy)")
            self.add_skill("Speak Language (Low Gothic)")
            self.talents.append("Pistol Weapon Training (Universal)")
            self.talents.append("Melee Weapon Training (Universal)")
            self.talents.append("Nerves of Steel")
            weapon = np.random.choice(['mono-sword', 'power sword'])
            if weapon == 'power sword':
                self.items.loc["Power Sword"] = [1, 'Common-Craftsmanship', weapon]
            else:
                self.items.loc["Mono-Sword"] = [1, 'Best-Craftsmanship', weapon]
            weapon = np.random.choice(['hand cannon', 'bolt pistol'])
            if weapon == 'hand cannon':
                self.items.loc["Hand Cannon"] = [1, 'Best-Craftsmanship', weapon]
            else:
                self.items.loc["Bolt Pistol"] = [1, 'Common-Craftsmanship', weapon]
            self.items.loc['Guard Flak Armour'] = [1, None, 'armour']
            self.items.loc["Micro-Bead"] = [1, None, 'micro-bead']
            self.items.loc["Void Suit"] = [1, None, 'void suit']
            self.items.loc["Blessed Ship Token"] = [1, None, 'ship token']
            self.items.loc["Re-Breather"] = [1, None, 're-breather']
            clothing = np.random.choice(['uniform', 'cloak'])
            if clothing == 'uniform':
                self.items.loc["Imperial Navy Uniform"] = [1, None, clothing]
            else:
                self.items.loc["Beggar's Cloak"] = [1, None, clothing]
            self.items.loc["Bottle of Amasec"] = [2, None, 'amasec']
            self.items.loc["Pict-Recorder"] = [1, None, 'pict-recorder']
            self.items.loc["Vox-Caster"] = [1, None, 'vox-caster']

        elif self.origin[5] == "Explorator":
            self.add_skill("Common Lore (Machine Cult)")
            self.add_skill("Common Lore (Tech)")
            self.add_skill("Forbidden Lore (Archeotech)")
            self.add_skill("Forbidden Lore (Adeptus Mechanicus)")
            self.add_skill("Literacy")
            self.add_skill("Logic")
            self.add_skill("Speak Language (Explorator Binary)")
            self.add_skill("Speak Language (Low Gothic)")
            self.add_skill("Speak Language (Techna-Lingua)")
            self.add_skill("Tech-Use")
            self.add_skill("Trade (Technomat)")
            self.traits.append("Mechanicus Implants")  # TODO: See p. 366.
            self.talents.append("Basic Weapon Training (Universal)")
            self.talents.append("Melee Weapon Training (Universal)")
            self.talents.append("Logis Implant")
            weapon = np.random.choice(['boltgun', 'lasgun', 'hellgun'])
            if weapon == 'hellgun':
                self.items.loc["Hellgun"] = [1, 'Good-Craftsmanship', weapon]
            elif weapon == 'lasgun':
                self.items.loc["Lasgun"] = [1, 'Best-Craftsmanship', weapon]
            else:
                self.items.loc["Boltgun"] = [1, None, weapon]
            weapon = np.random.choice(['shock staff', 'power axe'])
            if weapon == 'shock staff':
                self.items.loc["Shock Staff"] = [1, 'Good-Craftsmanship', weapon]
            else:
                self.items.loc["Power Axe"] = [1, 'Good-Craftsmanship', weapon]
            self.items.loc['Enforcer Light Carapace Armour'] = [1, None, 'armour']
            self.items.loc["Multikey"] = [1, None, 'multikey']
            self.items.loc["Void Suit"] = [1, None, 'void suit']
            self.items.loc["Micro-Bead"] = [1, None, 'micro-bead']
            self.items.loc["Injector"] = [1, None, 'injector']
            self.items.loc["Sacred Unguents"] = [1, None, 'sacred unguents']
            self.items.loc["Combi-Tool"] = [1, None, 'combi-tool']
            self.items.loc["Dataslate"] = [1, None, 'dataslate']
            self.items.loc["Servo-Skull Familiar"] = [1, None, 'familiar']  # TODO: See p. 375.

        elif self.origin[5] == "Missionary":
            self.add_skill("Common Lore (Imperial Creed)")
            self.add_skill("Common Lore (Imperium)")
            self.add_skill("Forbidden Lore (Heresy)")
            self.add_skill("Medicae")
            self.add_skill("Scholastic Lore (Imperial Creed)")
            self.add_skill("Speak Language (High Gothic)")
            self.add_skill("Speak Language (Low Gothic)")
            self.talents.append("Basic Weapon Training (Universal)")
            self.talents.append("Melee Weapon Training (Universal)")
            self.talents.append("Pure Faith")
            self.talents.append("Unshakeable Faith")
            weapon = np.random.choice(['flamer', 'lasgun'])
            if weapon == 'flamer':
                self.items.loc["Flamer"] = [1, 'Good-Craftsmanship', weapon]
            else:
                self.items.loc["Lasgun"] = [1, 'Best-Craftsmanship', weapon]
            weapon = np.random.choice(['chainsword', 'staff'])
            if weapon == 'staff':
                self.items.loc["Staff"] = [1, 'Best-Craftsmanship', weapon]
            else:
                self.items.loc["Chainsword"] = [1, 'Good-Craftsmanship', weapon]
            self.items.loc['Guard Flak Armour'] = [1, 'Best-Craftsmanship', 'armour']
            self.items.loc["Ecclesiarchal Robes"] = [1, None, 'robes']
            self.items.loc["Aquila Pendant"] = [1, None, 'pendant']
            self.items.loc["Sepulchre"] = [1, None, 'sepulchre']
            self.items.loc["Censer and Incense"] = [1, None, 'censer and incense']
            self.items.loc["Micro-Bead"] = [1, None, 'micro-bead']

        elif self.origin[5] == "Seneschal":
            self.add_skill("Barter")
            self.add_skill("Commerce")
            self.add_skill("Common Lore (Underworld)")
            self.add_skill("Deceive")
            self.add_skill("Evaluate")
            self.add_skill("Forbidden Lore (Archeotech)")
            self.add_skill("Inquiry")
            self.add_skill("Literacy")
            self.add_skill("Speak Language (Low Gothic)")
            self.add_skill("Speak Language (Trader's Cant)")
            self.talents.append("Basic Weapon Training (Universal)")
            self.talents.append("Pistol Weapon Training (Universal)")
            weapon = np.random.choice(['inferno pistol', 'hellpistol'])
            if weapon == 'inferno pistol':
                self.items.loc["Inferno Pistol"] = [1, 'Common-Craftsmanship', weapon]
            else:
                self.items.loc["Hellpistol"] = [1, 'Best-Craftsmanship', weapon]
            weapon = np.random.choice(['hellgun', 'boltgun'])
            if weapon == 'hellgun':
                self.items.loc["Hellgun"] = [1, 'Best-Craftsmanship', weapon]
            else:
                self.items.loc["Boltgun"] = [1, 'Common-Craftsmanship', weapon]
            self.items.loc['Xeno-Mesh Armour'] = [1, None, 'armour']
            self.items.loc["Autoquill"] = [1, None, 'autoquill']
            self.items.loc["Dataslate"] = [1, None, 'dataslate']
            self.items.loc["Micro-Bead"] = [1, None, 'micro-bead']
            self.items.loc["Multikey"] = [1, None, 'multikey']
            self.items.loc["Robes"] = [2, None, 'robes']
            self.items.loc["Synskin"] = [1, None, 'synskin']
            self.items.loc["Chrono"] = [1, None, 'chrono']
            self.items.loc["Cameleoline Cloak"] = [1, None, 'cloak']

        elif self.origin[5] == "Navigator":
            self.add_skill("Common Lore (Navis Nobilite)")
            self.add_skill("Forbidden Lore (Navigators)")
            self.add_skill("Forbidden Lore (Warp)")
            self.add_skill("Literacy")
            self.add_skill("Navigation (Stellar)")
            self.add_skill("Navigation (Warp)")
            self.add_skill("Psyniscience")
            self.add_skill("Scholastic Lore (Astromancy)")
            self.add_skill("Speak Language (High Gothic)")
            self.add_skill("Speak Language (Low Gothic)")
            self.talents.append("Navigator")
            self.talents.append("Pistol Weapon Training (Universal)")
            weapon = np.random.choice(['hellpistol', 'hand cannon'])
            if weapon == 'hand cannon':
                self.items.loc["Hand Cannon"] = [1, 'Good-Craftsmanship', weapon]
            else:
                self.items.loc["Hellpistol"] = [1, 'Best-Craftsmanship', weapon]
            self.items.loc["Metal Staff"] = [1, 'Best-Craftsmanship', weapon]
            self.items.loc['Xeno-Mesh Armour'] = [1, 'Best-Craftsmanship', 'armour']
            self.items.loc["Emperor's Tarot Deck"] = [1, None, 'tarot deck']
            self.items.loc["Silk Headscarf"] = [1, None, 'headscarf']
            self.items.loc["Nobilite Robes"] = [1, None, 'robes']
            self.items.loc["Charm"] = [1, None, 'charm']
            self.items.loc["Micro-Bead"] = [1, None, 'micro-bead']

        else:
            self.add_skill("Command")
            self.add_skill("Commerce")
            self.add_skill("Charm")
            self.add_skill("Common Lore (Imperium)")
            self.add_skill("Evaluate")
            self.add_skill("Literacy")
            self.add_skill("Scholastic Lore (Astromancy)")
            self.add_skill("Speak Language (High Gothic)")
            self.add_skill("Speak Language (Low Gothic)")
            self.talents.append("Air of Authority")
            self.talents.append("Pistol Weapon Training (Universal)")
            self.talents.append("Melee Weapon Training (Universal)")
            weapon = np.random.choice(['laspistol', 'hand cannon', 'plasma pistol'])
            if weapon == 'laspistol':
                self.items.loc["Laspistol"] = [1, 'Best-Craftsmanship', weapon]
            elif weapon == 'hand cannon':
                self.items.loc["Hand Cannon"] = [1, 'Good-Craftsmanship', weapon]
            else:
                self.items.loc["Plasma Pistol"] = [1, 'Common-Craftsmanship', weapon]
            weapon = np.random.choice(['mono-sword', 'power sword'])
            if weapon == 'mono-sword':
                self.items.loc["Mono-Sword"] = [1, 'Best-Craftsmanship', weapon]
            else:
                self.items.loc["Power Sword"] = [1, 'Common-Craftsmanship', weapon]
            armour = np.random.choice(['enforcer light carapace', 'storm trooper carapace'])
            if armour == 'enforcer light carapace':
                self.items.loc["Enforcer Light Carapace"] = [1, 'Best-Craftsmanship', armour]
            else:
                self.items.loc["Storm Trooper Carapace"] = [1, 'Best-Craftsmanship', armour]
            self.items.loc["Micro-Bead"] = [1, None, 'micro-bead']
            self.items.loc["Void Suit"] = [1, None, 'void suit']
            self.items.loc["Set of Fine Clothing"] = [1, None, 'clothing']
            self.items.loc["Xeno-Pelt Cloak"] = [1, None, 'cloak']

    def recalc_stats(self):
        for index in self.characteristics.index:
            self.characteristics.loc[index, "bonus"]: int = np.trunc(
                self.characteristics.loc[index, "characteristic"] / 10).astype(int)

    def generate_random_stats(self):
        self.sex = np.random.choice(['Male', 'Female'])
        self.name = self.generate_random_name(sex=self.sex)
        self.demeanour = demeanours[np.random.choice(["Bilious", "Cardinal", "Choleric", "Fixed", "Melancholic",
                                                      "Mutable", "Phlegmatic", "Sanguine", "Supine"])]

        roll = self.roll(1, 10)
        if roll < profit_ship.iloc[0, 0]:
            self.profit_factor += profit_ship.iloc[0, 1]
            self.ship_points += profit_ship.iloc[0, 2]
        elif roll < profit_ship.iloc[1, 0]:
            self.profit_factor += profit_ship.iloc[1, 1]
            self.ship_points += profit_ship.iloc[1, 2]
        elif roll < profit_ship.iloc[2, 0]:
            self.profit_factor += profit_ship.iloc[2, 1]
            self.ship_points += profit_ship.iloc[2, 2]
        elif roll < profit_ship.iloc[3, 0]:
            self.profit_factor += profit_ship.iloc[3, 1]
            self.ship_points += profit_ship.iloc[3, 2]
        else:
            self.profit_factor += profit_ship.iloc[4, 1]
            self.ship_points += profit_ship.iloc[4, 2]

        for index in self.characteristics.index:
            self.characteristics.loc[index, "characteristic"] = self.roll(2, 10) + 25
            self.characteristics.loc[index, "bonus_multiplier"]: float = 1.0

        random_walk: int = 0
        for x in range(0, origins_index):

            # This part creates a list of current row's contents. That's it. ;)
            origin_row: list = []
            for y in range(0, origins_columns):
                if origins.iloc[x, y] is not None:
                    origin_row.append(origins.iloc[x, y])
            origin_len = len(origin_row)

            if x == 0:
                random_walk = np.random.randint(0, origin_len)  # Starting point for the random walk.
                # Add first row of origin:
                self.origin.append(origin_row[random_walk])

            elif x < (origins_index - 1):
                if random_walk == 0:
                    random_walk += np.random.randint(0, 2)
                elif random_walk == origin_len - 1:
                    random_walk -= np.random.randint(0, 2)
                else:
                    random_walk += np.random.randint(low=-1, high=2)
                self.origin.append(origin_row[random_walk])
                origin_len = len(origin_row)
            else:
                random_walk += np.random.randint(low=0, high=3)
                self.origin.append(origin_row[random_walk])

        self.generate_home_world_stats()
        self.generate_birthright_stats()
        self.generate_lure_stats()
        self.generate_trials_stats()
        self.generate_motivation_stats()
        self.generate_career_stats()

        self.skills.sort_index(inplace=True)
        self.items.sort_index(inplace=True)
        self.recalc_stats()
