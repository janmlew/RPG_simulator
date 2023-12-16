# Imports.

import numpy as np


# import pandas as pd

class Creature:
    def __init__(self, name, kind="Human", dice_number=1, dice_sides=6):
        self.dice_number = dice_number
        self.dice_sides = dice_sides

    def roll(dice_number=1, dice_sides=6):
        rolls = []
        for i in range(0, dice_number):
            rolls.append(np.random.randint(1, dice_sides + 1))
        return rolls
