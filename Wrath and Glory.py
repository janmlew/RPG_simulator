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


def analyze_throw(dice_list: list, difficulty_number: int = 0):
    """
    This function reads a list of thrown dice.
    :param dice_list: self-explanatory
    :param difficulty_number: This number is subtracted from dice sum to determine success / failure.
    :return: Wrath dice result ("Critical!" v "Complication!" v "Emperor protects!") and the number of possible shifts.
    """
    shifts_count = 0
    throw_result = 0
    # This loop sums up the results discounted for DN. If the result is > 0 then the test is successful.
    for die in dice_list:
        if die == 6:
            throw_result += 2
        elif die > 3:
            throw_result += 1
    throw_result_shifted = throw_result
    # This loop checks whether there are some shifts possible.
    for die in dice_list:
        if (die == 6) & (throw_result_shifted-2 >= difficulty_number):
            shifts_count += 1
            throw_result_shifted -= 2
    print(f"Sum = {sum(dice_list)}, Result = {throw_result}, Shifts = {shifts_count}, Result after shifts = "
          f"{throw_result_shifted}.")
    # Wrath die result check.
    match dice_list[0]:
        case 6:
            wrath_result = "Critical!"
        case 1:
            wrath_result = "Complication!"
        case _:
            wrath_result = "Emperor protects!"
    return wrath_result, shifts_count


critical_hit_names = ["Strzał w głowę", "Paskudna rana", "Mordercze cięcie", "Bezlitosny cios", "Dziki atak",
                      "Bezwzględna wiwisekcja", "Wybebeszenie", "Morderczy atak", "Przełamujący cios", "Szkarłatny pył",
                      "Zmiażdżenie kości", "Niepojęta rzeź", "Przerażająca detonacja", "Makabryczna amputacja"]
critical_hit_dice_ranges = [[1, 6], [2, 3], [2, 6], [3, 3], [3, 6],
                            [4, 3], [4, 5], [4, 6], [5, 3], [5, 5], [5, 6], [6, 3], [6, 5], [6, 6]]
critical_hit_effects = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

first_throw = throw_dice(6)
print(first_throw)
result, shifts = analyze_throw(first_throw, 3)
print(result, shifts)
