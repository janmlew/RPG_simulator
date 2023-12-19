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
        self.characteristics = {"weapon_skill": 0, "ballistic_skill": 0, "strength": 0, "toughness": 0, "agility": 0, "intelligence": 0, "perception": 0, "will_power": 0, "fellowship":0}

    def roll(self, dice_number=1, dice_sides=6):
        for i in range(0, dice_number):
            self.rolls.append(np.random.randint(1, dice_sides + 1))
            print(f"{self.name} rolled {self.rolls[-1]}.")  # <-- This line is here only for testing
        return self.rolls[-dice_number:]

    @property
    def roll_history(self):
        return self.rolls

    def generate_stats(self):
        for key in self.characteristics.keys():
            self.characteristics[key] = sum(self.roll(2, 10)) + 25
            print(key, self.characteristics[key])
