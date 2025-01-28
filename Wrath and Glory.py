import numpy as np
import pandas as pd


def input_number(prompt: str):
    try:
        number = int(input(prompt))
        return number
    except ValueError: pass


def throw_dice(number_of_dice: int = 1, sides: int = 6):
    """
    :param number_of_dice: How many dice to dice_list.
    :param sides: Defaults to a 6-sided die.
    :return: Returns a list of thrown dice.
    """
    number_of_dice: int = 1 if number_of_dice is None else number_of_dice  # Catch nulls.
    sides: int = 6 if sides is None else sides  # Catch nulls.

    dice_list = [np.random.randint(1, sides+1) for die in range(1, number_of_dice+1)]
    return dice_list


def analyze_throw(dice_list: list, dn: int = 0):
    """
    This function reads a list of thrown dice.
    :param dice_list: self-explanatory
    :param dn: This number is subtracted from dice sum to determine success / failure.
    :return: Wrath dice result ("Critical!" v "Complication!" v "Emperor protects!") and the number of possible shifts.
    """
    dn: int = 0 if dn is None else dn  # Catch nulls.
    shifts_count = 0
    throw_result = 0

    # This loop sums up the results discounted for Difficulty Number (DN). Result > 0 means the test is successful.
    for die in dice_list:
        if die == 6:
            throw_result += 2
        elif die > 3:
            throw_result += 1
    throw_result_shifted = throw_result
    # This loop checks whether there are some shifts possible.
    for die in dice_list:
        if (die == 6) & (throw_result_shifted - 2 >= dn):
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


# Important variables and states:
critical_hit_names = ["Strzał w głowę", "Paskudna rana", "Mordercze cięcie", "Bezlitosny cios", "Dziki atak",
                      "Bezwzględna wiwisekcja", "Wybebeszenie", "Morderczy atak", "Przełamujący cios", "Szkarłatny pył",
                      "Zmiażdżenie kości", "Niepojęta rzeź", "Przerażająca detonacja", "Makabryczna amputacja"]
critical_hit_dice_ranges = [[1, 6], [2, 3], [2, 6], [3, 3], [3, 6],
                            [4, 3], [4, 5], [4, 6], [5, 3], [5, 5], [5, 6], [6, 3], [6, 5], [6, 6]]
# critical_hit_effects = [, , , , , , , , , , , , , , , , , , , , , , , ]
player_states = ["Groza", "Krwawienie", "Odsłonięcie", "Oślepienie", "Oszołomienie", "Podpalenie", "Powalenie",
                 "Przygwożdżenie", "Strach", "Szał bojowy", "Unieruchomienie", "Wycieńczenie", "Zatrucie",
                 "Zdezorientowanie"]
effect_states = ["Rana", "Rana śmiertelna", "Trauma",
                 "Jeśli przeżyje Trafienie krytyczne, natychmiast otrzymuje Trwały uraz",
                 "Każda postać będąca w Zwarciu z celem musi wykonać Test Zręczności o ST 3",
                 "Jeśli cel miał przy sobie jakiekolwiek materiały wybuchowe (np. granaty lub amunicję), następuje "
                 "detonacja, wywołująca dodatkowo 1k3 Ran śmiertelnych"]
glory_states = ["Rana", "Rana śmiertelna", "Trauma",
                "Trafienie krytyczne wpływa na jeden dodatkowy cel w zasięgu 10 metrów"]

dice_count = input_number("How many dice? ")
sides_count = input_number("How many sides to dice? ")
difficulty_number = input_number("Input DN, please: ")

first_throw = throw_dice(dice_count, sides_count)
print(first_throw)
result, shifts = analyze_throw(first_throw, difficulty_number)
print(result, shifts)
