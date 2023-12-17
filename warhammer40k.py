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
        self.characteristics = pd.DataFrame(data=np.zeros(9), index=["weapon_skill", "ballistic_skill", "strength",
                                                                     "toughness", "agility", "intelligence",
                                                                     "perception", "will_power", "fellowship"])

    def roll(self, dice_number=1, dice_sides=6):
        for i in range(0, dice_number):
            self.rolls.append(np.random.randint(1, dice_sides + 1))
            print(f"{self.name} rolled {self.rolls[-1]}.")
        return self.rolls[-1 + dice_number:]

    @property
    def roll_history(self):
        print(self.characteristics)
        return self.rolls
