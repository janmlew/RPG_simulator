# Imports.

import numpy as np
import pandas as pd


class Creature:
    def __init__(self, name, kind="Human", level=0):
        self.name = name
        self.kind = kind
        self.level = level
        self.rolls = []
        self.characteristics = pd.DataFrame(index=["weapon_skill", "ballistic_skill", "strength", "toughness",
                                                   "agility", "intelligence", "perception", "will_power",
                                                   "fellowship"], columns=["characteristic", "bonus"])
        origins_data = [[np.NaN, "Death World", "Void Born", "Forge World", "Hive World", "Imperial World",
                         "Noble Born", np.NaN],
                        [np.NaN, "Scavenger", "Scapegrace", "Stubjack", "Child of the Creed", "Savant", "Vaunted",
                         np.NaN],
                        [np.NaN, "Tainted", "Criminal", "Renegade", "Duty Bound", "Zealot", "Chosen by Destiny",
                         np.NaN],
                        [np.NaN, "The Hand of War", "Press-Ganged", "Calamity", "Ship-Lorn", "Dark Voyage",
                         "High Vendetta", np.NaN],
                        [np.NaN, "Endurance", "Fortune", "Vengeance", "Renown", "Pride", "Prestige", np.NaN],
                        ["Astropath Transcendent", "Arch-Mutant", "Void-Master", "Explorator", "Missionary",
                         "Seneschal", "Navigator", "Rogue Trader"]]
        self.origins = pd.DataFrame(index=["Home World", "Birthright", "Lure of the Void", "Trails and Travails",
                                           "Motivation", "Career"], columns=range(0, 8), data=origins_data)
        print(self.origins)

    def roll(self, dice_number=1, dice_sides=6):
        for i in range(0, dice_number):
            self.rolls.append(np.random.randint(1, dice_sides + 1))
            print(f"{self.name} rolled {self.rolls[-1]}.")  # <-- This line is here only for testing
        return self.rolls[-dice_number:]

    @property
    def roll_history(self):
        return self.rolls

    def generate_stats(self):
        for index in self.characteristics.index:
            self.characteristics.loc[index, "characteristic"] = sum(self.roll(2, 10)) + 25
            self.characteristics.loc[index, "bonus"] = np.trunc(self.characteristics.loc[index, "characteristic"]/10).astype(int)
            # print(self.characteristics.loc[index, :]) Test line.

        origins_dim_x =
        for x in range(0, len(self.origins.index)):
            for y in range(0, len(self.origins.columns)):
                if self.origins.iloc[x, y] == np.NaN:

                print(f"{self.origins.index[x]}: {self.origins.iloc[x, y]}")
