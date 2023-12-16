# Imports.

import numpy as np


# import pandas as pd

class Creature:
    def __init__(self, name, kind="Human", level=0):
        self.name = name
        self.kind = kind
        self.level = level

    def roll(self, dice_number=1, dice_sides=6):
        rolls = []
        for i in range(0, dice_number):
            rolls.append(np.random.randint(1, dice_sides + 1))
            print(self.name, "rolled", rolls[-1])
        return rolls
