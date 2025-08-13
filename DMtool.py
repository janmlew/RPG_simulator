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

archetype_list = ["Akolita", "Akrobata", "Zaklinacz zwierząt", "Archiwista", "Rzemieślnik", "Artysta", "Barman",
                  "Adwokat", "Łowca nagród", "Szarlatan", "Kucharz", "Przestępca", "Kultysta", "Detektyw", "Wysłannik",
                  "Artysta estradowy", "Wygnaniec", "Odkrywca", "Rolnik", "Bohater ludowy", "Wróżbita", "Hazardzista",
                  "Gladiator", "Grabarz", "Strażnik", "Zielarz", "Pustelnik", "Myśliwy", "Rycerz", "Robotnik",
                  "Uczeń sztuk walki", "Kupiec", "Medyk", "Górnik", "Szlachcic", "Koczownik", "Obcy", "Pirat",
                  "Pielgrzym", "Więzień", "Mędrzec / uczony", "Marynarz", "Uczony", "Zwiadowca", "Żołnierz", "Szpieg",
                  "Nauczyciel", "Majsterkowicz", "Ulicznik", "Wojownik", "Dziwak"]

acolyte_drives = {1: "Spread the beneficence of their deity",
                  2: "Rise to a leadership position in their order",
                  3: "Found a temple to spread their god's reach",
                  4: "Take a pilgrimage to a lost sacred site",
                  5: "Convert others to the fold through acts",
                  6: "Work miracles in the name of their deity",
                  7: "Leave a legacy like the saints in their texts",
                  8: "Preserve the faith by combating corruption",
                  9: "Embody the teachings, become an avatar",
                  10: "Unravel the mysteries of their faith",
                  11: "Forge connections with other religions",
                  12: "Shape the direction of their faith",
                  13: "Protect creation from corruption",
                  14: "Confront the sworn enemies of their god",
                  15: "Be fiercely loyal to their faith's principles",
                  16: "Redeem themselves for their past",
                  17: "Fulfill the prophecy, O chosen e",
                  18: "Retrieve the Sacred Relics or Artifacts",
                  19: "Strengthen their connection to the divine",
                  20: "Prove their worth in the eyes of their god",}
acolyte_catalysts = {1: "Divine vision in dreams or meditation",
                     2: "A sacred messenger came calling",
                     3: "Ancient text holding suppressed knowledge",
                     4: "Signs and portents hint at prophecy",
                     5: "Divine power implies worldly responsibility",
                     6: "Heretical sect just might be onto something",
                     7: "Fanaticism threatens to define their faith",
                     8: "Assigned a mission by the elders",
                     9: "Ritualistically initiated into a secret order",
                     10: "Internal corruption threatens their faith",
                     11: "Entrusted with a significant relic",
                     12: "A distraught pilgrim begs for their help",}
acolyte_friends = {1: "The Gardens of Serenity: Vineyard & Abbey keeping a vow of silence and a powerful secret",
                   2: "Shields of Faith: Holy warriors who devote themselves to martial arts and the deity's ways",
                   3: "The Wayfarer's Star: A merchant's guild promoting and profiting from a pilgrimage path",
                   4: "Shadows of the Sacred Flame: Spies who infiltrate and monitor secular organizations",}
acolyte_assets = {1: "Elahandra of the Radiant Veil: Wise and benevolent leader weary of internal politics",
                  2: "Brother Galen: An ancient acolyte who never advanced, brimming with rumors",
                  3: "Atticus the Elder: Bespectacled Scribe with encyclopedic knowledge of the faith's history",
                  4: "Marcum Veldar: A noble who supports the order to compensate for personal debauchery",
                  5: "Orek the Wanderer: Splintered from the authorities, walks the world healing people",
                  6: "Sister Isolde: Eccentric, slightly scattered, and kindly devotee with erratic gift of prophecy",}
acolyte_items = {1: "Well-worn Journal or Annotated Scripture: written by mentor or an historical figure",
                 2: "Vestments of Authority: Symbolic outfit that will greatly impress some and anger others",
                 3: "Chalice of the Faithful: Removes poison from any liquid put within it, once per day",
                 4: "Clarifying Lens: Piece of stained glass from ancient temple that can pierce illusions",
                 5: "Beads of Answered Prayers: Increases odds of successful divine intervention",
                 6: "Pealing Retribution: Inscribed bell or singing bowl, deafens all others in range",
                 7: "Holier Symbol: Improves potency of any magic under the deity's divine domain",
                 8: "Staff of the Hierophant: Summons an allied celestial creature for aid, once per week",
                 9: "Crown of Blessings: When activated hovers like a halo and gives off light as candle or torch",
                 10: "Angelic Amulet: Made of mysterious material, reduces damage of specific types",}
acolyte_antagonists = {1: "House of Blessed Respite: Posing as a hospice, but collecting dead for nefarious reasons",
                       2: "The Salted Earth: Clandestinely disrupting rituals and undermining faith to “clear the way”",
                       3: "Cult of the Stranger: Worship a forgotten god unaware it is a well-known demon",
                       4: "Serpentine Sect: Corrupt clergy who use their influence for personal gain and pleasure",
                       5: "The Reliquary Raiders: Dungeoneers who find and loot ancient holy sites for profit",
                       6: "The Prophet's Children: A splinter sect thought to be harmless which proves to be anything but",}
acolyte_rivals = {}
acolyte_locs = {}
acolyte_monsters = {}
acolyte_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

_drives = {}
_catalysts = {}
_friends = {}
_assets = {}
_items = {}
_antagonists = {}
_rivals = {}
_locs = {}
_monsters = {}
_plot_hooks = {}

continue_prompt = ""  # Initialize a loop continuation variable.
while continue_prompt!="q":
    dice_count = input_number("How many dice? ")
    sides_count = input_number("How many sides to dice? ")
    dice_list = throw_dice(dice_count, sides_count)
    print(f"List of the dice thrown: {dice_list}.")
    print("Press enter to continue or type 'q' to quit.")
    continue_prompt = input()
