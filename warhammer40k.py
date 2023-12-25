# Imports.

import numpy as np
import pandas as pd

# Global data setup.
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


class Creature:
    def __init__(self, name: str, kind: str = "Human", level: int = 0):
        self.name = name
        self.kind = kind
        self.level = level
        self.rolls: list = []
        self.characteristics = pd.DataFrame(index=["weapon_skill", "ballistic_skill", "strength", "toughness",
                                                   "agility", "intelligence", "perception", "willpower",
                                                   "fellowship"], columns=["characteristic", "bonus", "modifier"])
        self.origin: list = []
        self.skills: list = []
        self.talents_traits: dict = {}
        self.wounds: int = 0
        self.fate: int = 0

    def roll(self, dice_number: int = 1, dice_sides: int = 6):
        for i in range(0, dice_number):
            self.rolls.append(np.random.randint(1, dice_sides + 1))
            # print(f"{self.name} rolled {self.rolls[-1]}.")  # <-- This line is here only for testing
        return self.rolls[-dice_number:]

    @property
    def roll_history(self):
        return self.rolls

    def generate_stats(self):
        for index in self.characteristics.index:
            self.characteristics.loc[index, "characteristic"] = sum(self.roll(2, 10)) + 25
            self.characteristics.loc[index, "bonus"] = np.trunc(
                self.characteristics.loc[index, "characteristic"] / 10).astype(int)
            self.characteristics.loc[index, "modifier"]: int = 0

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
                if self.origin[-1] == "Death World":
                    self.characteristics.loc["strength", "modifier"] += 5
                    self.characteristics.loc["toughness", "modifier"] += 5
                    self.characteristics.loc["willpower", "modifier"] += 5
                    self.characteristics.loc["fellowship", "modifier"] -= 5
                    self.skills.append("Survival")
                    if np.random.randint(0, 1) == 0:
                        self.talents_traits["Hardened"] = "Jaded"
                    else:
                        self.talents_traits["Hardened"] = "Resistance (Poisons)"
                    self.talents_traits["If It Bleeds, I Can Kill It"] = "Melee Weapon Training (Primitive) Talent"
                    self.talents_traits["Paranoid"] = "-10 to all Interaction Skill Tests in formal surroundings"
                    self.talents_traits["Survivor"] = "+10 to all Tests to resist Pinning and Shock"
                    self.wounds += sum(self.roll(1, 5) + 2)
                    self.characteristics.loc["toughness", "bonus"] *= 2
                    # Determine fate points:
                    self.roll(1, 10)
                    if self.roll_history[-1] < 6:
                        self.fate = 2
                    else:
                        self.fate = 3
                if self.origin[-1] == "Void Born":
                    self.characteristics.loc["strength", "modifier"] -= 5
                    self.characteristics.loc["willpower", "modifier"] += 5
                    self.skills.append("Speak Language (Ship Dialect)")
                    self.talents_traits["Charmed"] = "Roll natural 9 on 1d10 when spending Fate Point => FP NOT spent"
                    self.talents_traits["Ill-Omened"] = ("-5 to all Fellowship Tests interacting with non-void born "
                                                         "humans")
                    self.talents_traits["Shipwise"] = ("Navigation (Stellar)(Int) and Pilot (Spacecraft)(Ag) => "
                                                       "Untrained Basic Skill")
                    self.talents_traits["Void Accustomed"] = ("Immune to space travel sickness + zero- & low-gravity "
                                                              "environments => NOT Difficult Terrain")
                    self.wounds += sum(self.roll(1, 5))
                    self.characteristics.loc["toughness", "bonus"] *= 2
                    # Determine fate points:
                    self.roll(1, 10)
                    if self.roll_history[-1] < 6:
                        self.fate = 3
                    else:
                        self.fate = 4
                if self.origin[-1] == "Forge World":
                    self.characteristics.loc["weapon_skill", "modifier"] -= 5
                    self.characteristics.loc["intelligence", "modifier"] += 5
                    self.skills.append("Common Lore (Tech)(Int) => Untrained Basic Skill")
                    self.skills.append("Common Lore (Machine Cult)(Int) => Untrained Basic Skill")
                    self.talents_traits["Credo Omnissiah"] = "Technical Knock Talent"
                    self.talents_traits["Fit for Purpose"] = "+3 to a chosen Characteristic"
                    self.characteristics.iloc[np.random.randint(0, 9), 0] += 3
                    self.talents_traits["Stranger to the Cult"] = ("-10 to all Tests involving knowledge of the "
                                                                   "Imperial Creed & -5 to all Fellowship Tests "
                                                                   "interacting with members of Ecclesiarchy in formal "
                                                                   "settings")
                    self.wounds += sum(self.roll(1, 5)) + 1
                    self.characteristics.loc["toughness", "bonus"] *= 2
                    # Determine fate points:
                    self.roll(1, 10)
                    if self.roll_history[-1] < 6:
                        self.fate = 2
                    elif self.roll_history[-1] < 10:
                        self.fate = 3
                    else:
                        self.fate = 4
                if self.origin[-1] == "Hive World":
                    self.characteristics.loc["toughness", "modifier"] -= 5
                    self.characteristics.loc["fellowship", "modifier"] += 5
                    self.skills.append("Common Lore (Tech)(Int) => Untrained Basic Skill")
                    self.skills.append("Common Lore (Machine Cult)(Int) => Untrained Basic Skill")
                    self.talents_traits["Credo Omnissiah"] = "Technical Knock Talent"
                    self.talents_traits["Fit for Purpose"] = "+3 to a chosen Characteristic"
                    self.characteristics.iloc[np.random.randint(0, 9), 0] += 3
                    self.talents_traits["Stranger to the Cult"] = ("-10 to all Tests involving knowledge of the "
                                                                   "Imperial Creed & -5 to all Fellowship Tests "
                                                                   "interacting with members of Ecclesiarchy in formal "
                                                                   "settings")
                    self.wounds += sum(self.roll(1, 5)) + 1
                    self.characteristics.loc["toughness", "bonus"] *= 2
                    # Determine fate points:
                    self.roll(1, 10)
                    if self.roll_history[-1] < 6:
                        self.fate = 2
                    elif self.roll_history[-1] < 10:
                        self.fate = 3
                    else:
                        self.fate = 4

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
