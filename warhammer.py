# Imports.

import numpy as np


# import pandas as pd

class DiceThrow:
    def __init__(self, dice_number=1, dice_sides=6):
        self.dice_number = dice_number
        self.dice_sides = dice_sides

    def roll(self):
        return np.random.randint(1, self.dice_sides + 1, self.dice_number)
