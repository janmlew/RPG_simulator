# Imports.

import numpy as np
import pandas as pd


# import pandas as pd

class Creature:
    def __init__(self, name, kind="Human", level=0):
        self.name = name
        self.kind = kind
        self.level = level
        self.rolls = []
        self.characteristics = pd.DataFrame(index=["weapon_skill", "ballistic_skill", "strength", "toughness",
                                                   "agility", "intelligence", "perception", "will_power",
                                                   "fellowship"], columns=["characteristic", "bonus"])

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
            print(self.characteristics.loc[index, :])
