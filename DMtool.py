import numpy as np


def input_number(prompt: str):
    try:
        number = int(input(prompt))
        return number
    except ValueError:
        pass


def throw_dice(number_of_dice: int = 1, sides: int = 6):
    """
    :param number_of_dice: How many dice to dice_list. None is captured.
    :param sides: Defaults to a 6-sided die. None is captured.
    :return: Returns a list of thrown dice.
    """
    number_of_dice: int = 1 if number_of_dice is None else number_of_dice  # Catch nulls.
    sides: int = 6 if sides is None else sides  # Catch nulls.

    dice_list = [np.random.randint(1, sides + 1) for die in range(1, number_of_dice + 1)]
    return dice_list


character_setup_list = ["Motywacje postaci",
                        "Zaczyn łazikowania",
                        "Rozwój postaci",
                        "Przyjazne frakcje",
                        "Aktywa i sprzymierzeńcy",
                        "Przedmioty magiczne i znaczące",
                        "Organizacje przeciwne",
                        "Rywale i wrogowie",
                        "Miejsca pobudzające wyobraźnię",
                        "Tematyczne potwory",
                        "Haczyki narracyjne i ziarna opowieści"]

archetype_list = ["Acolyte", "Acrobat", "Animal Whisperer", "Archivist", "Artisan", "Artist", "Barkeep", "Barrister",
                  "Bounty Hunter", "Charlatan", "Cook", "Criminal", "Cultist", "Detective", "Emissary", "Entertainer",
                  "Exile", "Explorer", "Farmer", "Folk Hero", "Fortune Teller", "Gambler", "Gladiator", "Gravedigger",
                  "Guard", "Herbalist", "Hermit", "Hunter", "Knight", "Laborer", "Martial Disciple", "Merchant",
                  "Medic", "Miner", "Noble", "Nomad", "Outlander", "Pirate", "Pilgrim", "Prisoner", "Sage / Scholar",
                  "Sailor", "Scholar", "Scout", "Soldier", "Spy", "Teacher", "Tinker", "Urchin", "Warrior", "Weirdo"]

continue_prompt = ""  # Initialize a loop continuation variable.
while continue_prompt!="q":
    dice_count = input_number("How many dice? ")
    sides_count = input_number("How many sides to dice? ")
    dice_list = throw_dice(dice_count, sides_count)
    print(f"List of the dice thrown: {dice_list}.")
    print("Press enter to continue or type 'q' to quit.")
    continue_prompt = input()
