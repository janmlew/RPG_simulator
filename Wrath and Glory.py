import numpy as np
import pandas as pd


def throw_dice(number_of_dice: int = 1, sides: int = 6, difficulty: int = 0):
    """
    :param number_of_dice: How many dice to dice_list.
    :param sides: Defaults to a 6-sided die.
    :param difficulty: Usual difficulty is ST = 3.
    :return: Returns a list of thrown dice.
    """
    dice_list: list = []
    dice_list = [np.random.randint(1, sides+1) for die in range(1, number_of_dice+1)]
    return dice_list


def analyze_throw(dice_list: list, st:int = 0):
    icon_list= []
    wrath_result = "Emperor protects!"
    shifts_count = 0
    for die in dice_list:
        if die == 6:
            icon_list.append(2)
            shifts_count += 1
        elif die > 3:
            icon_list.append(1)
    if icon_list[0] == 1:
        wrath_result = "Complication!"
    elif icon_list[0] == 6:
        wrath_result = "Critical!"
    for icon in
    print(f"Sum = {sum(icon_list)}, ")



print(throw_dice(6))
