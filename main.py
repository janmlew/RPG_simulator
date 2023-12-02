import numpy as np
import pandas as pd

creature_list = ['Balrog', 'Dragon', 'Elemental', 'Ent', 'Tree', 'Giant',
                 'Hero', 'Lycanthrope', 'Roc', 'Super Hero', 'Troll', 'Ogre',
                 'Wight', 'Ghoul', 'Wizard', 'Wraith']
enemy_dict = {
    'Balrog': [7, 6, 10, 12, 12, 9, 11, 10, 12, 9, 10, 10, 12, 12, 7, 10],
    'Dragon': [11, 8, 10, 12, 12, 9, 12, 12, 12, 10, 12, 12, 12, 12, 9, 12],
    'Elemental': [11, 10, 11, 12, 12, 10, 10, 12, 12, 8, 11, 11, 12, 12, 6, 7],
    'Ent': [8, 6, 7, 7, 7, 7, 12, 12, 9, 11, 10, 10, 12, 12, 10, 12],
    'Tree': [8, 6, 7, 7, 7, 7, 12, 12, 9, 11, 10, 10, 12, 12, 10, 12],
    'Giant': [8, 9, 9, 8, 8, 9, 11, 10, 10, 9, 9, 9, 11, 11, 11, 12],
    'Hero': [4, 5, 4, 4, 4, 6, 7, 7, 5, 5, 8, 8, 9, 9, 8, 8],
    'Lycanthrope': [6, 4, 4, 4, 4, 5, 8, 9, 6, 6, 8, 8, 8, 8, 7, 9],
    'Roc': [10, 8, 7, 11, 11, 7, 10, 10, 9, 8, 9, 9, 11, 11, 9, 10],
    'Super Hero': [7, 8, 7, 7, 7, 9, 10, 10, 8, 8, 11, 11, 12, 12, 10, 10],
    'Troll': [6, 5, 7, 7, 7, 6, 9, 8, 6, 5, 7, 7, 9, 9, 8, 9],
    'Ogre': [6, 5, 7, 7, 7, 6, 9, 8, 6, 5, 7, 7, 9, 9, 8, 9],
    'Wight': [4, 2, 2, 3, 3, 4, 6, 6, 5, 4, 10, 10, 8, 8, 6, 11],
    'Ghoul': [4, 2, 2, 3, 3, 4, 6, 6, 5, 4, 10, 10, 8, 8, 6, 11],
    'Wizard': [8, 10, 11, 10, 10, 10, 11, 10, 10, 9, 11, 11, 10, 10, 10, 12],
    'Wraith': [11, 7, 10, 10, 10, 10, 11, 12, 9, 8, 12, 12, 7, 7, 5, 7],
}
combat_table = pd.DataFrame(enemy_dict, index=creature_list)

print(combat_table)


class Creature:
    def __init__(self, name, hp=None, die=None, kind="Hero"):
        self.name = name
        self.hp = hp
        self.die = die
        self.kind = kind

    def is_alive(self):
        if self.hp < 0:
            return False
        else:
            return True


# combat_lookup returns the successful attack roll threshold
def combat_lookup(cre1, cre2):  # cre1 is an attacker
    return combat_table.loc[cre1.kind, cre2.kind]


bargol = Creature(name="Zły", hp=100, kind="Balrog")
hadrian_sandberg = Creature(name="Hadrian Sandberg", hp=31, kind="Dragon")

print(combat_lookup(bargol, hadrian_sandberg),
      combat_lookup(hadrian_sandberg, bargol))


def strike(cre1, cre2, cre1_initiative, cre2_initiative):
    # No surprise attacks implemented yet, so both creatures try to hit.
    first_roll = np.random.randint(1, 7, 2).sum()
    second_roll = np.random.randint(1, 7, 2).sum()

    if cre1_initiative > cre2_initiative:
        print(cre1.name, "have rolled", first_roll, "on its attack roll.")
        if first_roll < combat_lookup(cre1, cre2):
            print(cre1.name, "missed!")
        else:
            print("Hit!")
            # Creatures roll 1d6 for damage.
            hit1 = np.random.randint(1, 7)
            print(cre1.name, "hits for", hit1, "damage.")
            cre2.hp -= hit1
        # Checks whether the second creature has a chance to counter
        if cre2.is_alive():
            print(cre2.name, "have rolled", second_roll, "on its attack roll.")
            if second_roll < combat_lookup(cre2, cre1):
                print(cre2.name, "missed!")
            else:
                print("Hit!")
                # Creatures roll 1d6 for damage.
                hit2 = np.random.randint(1, 7)
                print(cre2.name, "hits for", hit2, "damage.")
                cre1.hp -= hit2
    elif cre1_initiative == cre2_initiative:
        print(cre1.name, "have rolled", first_roll, "on its attack roll.")
        if first_roll < combat_lookup(cre1, cre2):
            print(cre1.name, "missed!")
        else:
            print("Hit!")
            # Creatures roll 1d6 for damage.
            hit1 = np.random.randint(1, 7)
            print(cre1.name, "hits for", hit1, "damage.")
            cre2.hp -= hit1
        print(cre2.name, "have rolled", second_roll, "on its attack roll.")
        if second_roll < combat_lookup(cre2, cre1):
            print(cre2.name, "missed!")
        else:
            print("Hit!")
            # Creatures roll 1d6 for damage.
            hit2 = np.random.randint(1, 7)
            print(cre2.name, "hits for", hit2, "damage.")
            cre1.hp -= hit2
    else:
        print(cre2.name, "have rolled", first_roll, "on its attack roll.")
        if first_roll < combat_lookup(cre2, cre1):
            print(cre2.name, "missed!")
        else:
            print("Hit!")
            # Creatures roll 1d6 for damage.
            hit1 = np.random.randint(1, 7)
            print(cre2.name, "hits for", hit1, "damage.")
            cre1.hp -= hit1
        # Checks whether the first creature has a chance to counter
        if cre1.is_alive():
            print(cre1.name, "have rolled", second_roll, "on its attack roll.")
            if second_roll < combat_lookup(cre1, cre2):
                print(cre1.name, "missed!")
            else:
                print("Hit!")
                # Creatures roll 1d6 for damage.
                hit2 = np.random.randint(1, 7)
                print(cre1.name, "hits for", hit2, "damage.")
                cre2.hp -= hit2


def combat(cre1, cre2):
    print(cre1.name, "has", cre1.hp, "HPs, while", cre2.name, "has", cre2.hp,
          "HPs before the fight.")
    # Checks whether creatures can participate in a fight.
    if not (cre1.is_alive() and cre2.is_alive()):
        print("Dead creatures cannot fight! Choose living contestants.")
        return None

    # Initiative checks. Simultaneous fight is effectively treated like an
    # initiative roll in favor of cre1.
    cre1_initiative = np.random.randint(1, 7)
    print(cre1.name, "have rolled", cre1_initiative, "on initiative roll.")
    cre2_initiative = np.random.randint(1, 7)
    print(cre2.name, "have rolled", cre2_initiative, "on initiative roll.")
    if cre1_initiative == cre2_initiative:
        print("Both creatures strike at the same time!")
    elif cre1_initiative > cre2_initiative:
        print(cre1.name, "strikes first in combat!")
    else:
        print(cre2.name, "strikes first in combat!")

    while cre1.is_alive() and cre2.is_alive():
        strike(cre1, cre2, cre1_initiative, cre2_initiative)

    if (not cre1.is_alive()) and (not cre2.is_alive()):
        print(cre1.name, "and", cre2.name, "killed themselves!")
        print(cre1.name, "has", cre1.hp, "HPs, while", cre2.name, "has", cre2.hp,
              "HPs after the fight.")
    elif not cre1.is_alive():
        print(cre1.name, "killed", cre2.name + ".")
        print("After the fight,", cre1.name, "has", cre1.hp, "HPs, while", cre2.name, "has", cre2.hp,
              "HPs.")
    else:
        print(cre2.name, "killed", cre1.name + ".")
        print("After the fight,", cre1.name, "has", cre1.hp, "HPs, while", cre2.name, "has", cre2.hp,
              "HPs.")


combat(hadrian_sandberg, bargol)
