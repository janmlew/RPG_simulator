# Imports.

import numpy as np
import pandas as pd

# Global data setup.
origins_data = [["Death World", "Void Born", "Forge World", "Hive World", "Imperial World", "Noble Born"],
                ["Scavenger", "Scapegrace", "Stubjack", "Child of the Creed", "Savant", "Vaunted"],
                ["Tainted", "Criminal", "Renegade", "Duty Bound", "Zealot", "Chosen by Destiny"],
                ["The Hand of War", "Press-Ganged", "Calamity", "Ship-Lorn", "Dark Voyage", "High Vendetta"],
                ["Endurance", "Fortune", "Vengeance", "Renown", "Pride", "Prestige"],
                ["Astropath Transcendent", "Arch-Mutant", "Void-Master", "Explorator", "Missionary", "Seneschal",
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
                                                   "agility", "intelligence", "perception", "will_power",
                                                   "fellowship"], columns=["characteristic", "bonus"])
        self.origin: list = []

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
            # print(self.characteristics.loc[index, :]) Test line.

        random_origin: int = 0
        random_step: int = 0
        old_state: int = 0
        new_state: int = 0

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

        print(f"The new path is: {self.origin}")
