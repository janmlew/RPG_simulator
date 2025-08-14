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

acrobat_drives = {}
acrobat_catalysts = {}
acrobat_friends = {}
acrobat_assets = {}
acrobat_items = {}
acrobat_antagonists = {}
acrobat_rivals = {}
acrobat_locs = {}
acrobat_monsters = {}
acrobat_plot_hooks = {}

animal_whisperer_drives = {}
animal_whisperer_catalysts = {}
animal_whisperer_friends = {}
animal_whisperer_assets = {}
animal_whisperer_items = {}
animal_whisperer_antagonists = {}
animal_whisperer_rivals = {}
animal_whisperer_locs = {}
animal_whisperer_monsters = {}
animal_whisperer_plot_hooks = {}

archivist_drives = {}
archivist_catalysts = {}
archivist_friends = {}
archivist_assets = {}
archivist_items = {}
archivist_antagonists = {}
archivist_rivals = {}
archivist_locs = {}
archivist_monsters = {}
archivist_plot_hooks = {}

artisan_drives = {}
artisan_catalysts = {}
artisan_friends = {}
artisan_assets = {}
artisan_items = {}
artisan_antagonists = {}
artisan_rivals = {}
artisan_locs = {}
artisan_monsters = {}
artisan_plot_hooks = {}

artist_drives = {}
artist_catalysts = {}
artist_friends = {}
artist_assets = {}
artist_items = {}
artist_antagonists = {}
artist_rivals = {}
artist_locs = {}
artist_monsters = {}
artist_plot_hooks = {}

barkeep_drives = {}
barkeep_catalysts = {}
barkeep_friends = {}
barkeep_assets = {}
barkeep_items = {}
barkeep_antagonists = {}
barkeep_rivals = {}
barkeep_locs = {}
barkeep_monsters = {}
barkeep_plot_hooks = {}

barrister_drives = {}
barrister_catalysts = {}
barrister_friends = {}
barrister_assets = {}
barrister_items = {}
barrister_antagonists = {}
barrister_rivals = {}
barrister_locs = {}
barrister_monsters = {}
barrister_plot_hooks = {}

bounty_hunter_drives = {}
bounty_hunter_catalysts = {}
bounty_hunter_friends = {}
bounty_hunter_assets = {}
bounty_hunter_items = {}
bounty_hunter_antagonists = {}
bounty_hunter_rivals = {}
bounty_hunter_locs = {}
bounty_hunter_monsters = {}
bounty_hunter_plot_hooks = {}

charlatan_drives = {}
charlatan_catalysts = {}
charlatan_friends = {}
charlatan_assets = {}
charlatan_items = {}
charlatan_antagonists = {}
charlatan_rivals = {}
charlatan_locs = {}
charlatan_monsters = {}
charlatan_plot_hooks = {}

cook_drives = {}
cook_catalysts = {}
cook_friends = {}
cook_assets = {}
cook_items = {}
cook_antagonists = {}
cook_rivals = {}
cook_locs = {}
cook_monsters = {}
cook_plot_hooks = {}

criminal_drives = {}
criminal_catalysts = {}
criminal_friends = {}
criminal_assets = {}
criminal_items = {}
criminal_antagonists = {}
criminal_rivals = {}
criminal_locs = {}
criminal_monsters = {}
criminal_plot_hooks = {}

cultist_drives = {}
cultist_catalysts = {}
cultist_friends = {}
cultist_assets = {}
cultist_items = {}
cultist_antagonists = {}
cultist_rivals = {}
cultist_locs = {}
cultist_monsters = {}
cultist_plot_hooks = {}

detective_drives = {}
detective_catalysts = {}
detective_friends = {}
detective_assets = {}
detective_items = {}
detective_antagonists = {}
detective_rivals = {}
detective_locs = {}
detective_monsters = {}
detective_plot_hooks = {}

emmissary_drives = {}
emmissary_catalysts = {}
emmissary_friends = {}
emmissary_assets = {}
emmissary_items = {}
emmissary_antagonists = {}
emmissary_rivals = {}
emmissary_locs = {}
emmissary_monsters = {}
emmissary_plot_hooks = {}

entertainer_drives = {}
entertainer_catalysts = {}
entertainer_friends = {}
entertainer_assets = {}
entertainer_items = {}
entertainer_antagonists = {}
entertainer_rivals = {}
entertainer_locs = {}
entertainer_monsters = {}
entertainer_plot_hooks = {}

exile_drives = {}
exile_catalysts = {}
exile_friends = {}
exile_assets = {}
exile_items = {}
exile_antagonists = {}
exile_rivals = {}
exile_locs = {}
exile_monsters = {}
exile_plot_hooks = {}

explorer_drives = {}
explorer_catalysts = {}
explorer_friends = {}
explorer_assets = {}
explorer_items = {}
explorer_antagonists = {}
explorer_rivals = {}
explorer_locs = {}
explorer_monsters = {}
explorer_plot_hooks = {}

farmer_drives = {}
farmer_catalysts = {}
farmer_friends = {}
farmer_assets = {}
farmer_items = {}
farmer_antagonists = {}
farmer_rivals = {}
farmer_locs = {}
farmer_monsters = {}
farmer_plot_hooks = {}

folk_hero_drives = {}
folk_hero_catalysts = {}
folk_hero_friends = {}
folk_hero_assets = {}
folk_hero_items = {}
folk_hero_antagonists = {}
folk_hero_rivals = {}
folk_hero_locs = {}
folk_hero_monsters = {}
folk_hero_plot_hooks = {}

fortune_teller_drives = {}
fortune_teller_catalysts = {}
fortune_teller_friends = {}
fortune_teller_assets = {}
fortune_teller_items = {}
fortune_teller_antagonists = {}
fortune_teller_rivals = {}
fortune_teller_locs = {}
fortune_teller_monsters = {}
fortune_teller_plot_hooks = {}

gambler_drives = {}
gambler_catalysts = {}
gambler_friends = {}
gambler_assets = {}
gambler_items = {}
gambler_antagonists = {}
gambler_rivals = {}
gambler_locs = {}
gambler_monsters = {}
gambler_plot_hooks = {}

gladiator_drives = {}
gladiator_catalysts = {}
gladiator_friends = {}
gladiator_assets = {}
gladiator_items = {}
gladiator_antagonists = {}
gladiator_rivals = {}
gladiator_locs = {}
gladiator_monsters = {}
gladiator_plot_hooks = {}

gravedigger_drives = {}
gravedigger_catalysts = {}
gravedigger_friends = {}
gravedigger_assets = {}
gravedigger_items = {}
gravedigger_antagonists = {}
gravedigger_rivals = {}
gravedigger_locs = {}
gravedigger_monsters = {}
gravedigger_plot_hooks = {}

guard_drives = {}
guard_catalysts = {}
guard_friends = {}
guard_assets = {}
guard_items = {}
guard_antagonists = {}
guard_rivals = {}
guard_locs = {}
guard_monsters = {}
guard_plot_hooks = {}

herbalist_drives = {}
herbalist_catalysts = {}
herbalist_friends = {}
herbalist_assets = {}
herbalist_items = {}
herbalist_antagonists = {}
herbalist_rivals = {}
herbalist_locs = {}
herbalist_monsters = {}
herbalist_plot_hooks = {}

hunter_drives = {}
hunter_catalysts = {}
hunter_friends = {}
hunter_assets = {}
hunter_items = {}
hunter_antagonists = {}
hunter_rivals = {}
hunter_locs = {}
hunter_monsters = {}
hunter_plot_hooks = {}

knight_drives = {}
knight_catalysts = {}
knight_friends = {}
knight_assets = {}
knight_items = {}
knight_antagonists = {}
knight_rivals = {}
knight_locs = {}
knight_monsters = {}
knight_plot_hooks = {}

laborer_drives = {}
laborer_catalysts = {}
laborer_friends = {}
laborer_assets = {}
laborer_items = {}
laborer_antagonists = {}
laborer_rivals = {}
laborer_locs = {}
laborer_monsters = {}
laborer_plot_hooks = {}

martial_disciple_drives = {}
martial_disciple_catalysts = {}
martial_disciple_friends = {}
martial_disciple_assets = {}
martial_disciple_items = {}
martial_disciple_antagonists = {}
martial_disciple_rivals = {}
martial_disciple_locs = {}
martial_disciple_monsters = {}
martial_disciple_plot_hooks = {}

merchant_drives = {}
merchant_catalysts = {}
merchant_friends = {}
merchant_assets = {}
merchant_items = {}
merchant_antagonists = {}
merchant_rivals = {}
merchant_locs = {}
merchant_monsters = {}
merchant_plot_hooks = {}

medic_drives = {}
medic_catalysts = {}
medic_friends = {}
medic_assets = {}
medic_items = {}
medic_antagonists = {}
medic_rivals = {}
medic_locs = {}
medic_monsters = {}
medic_plot_hooks = {}

miner_drives = {}
miner_catalysts = {}
miner_friends = {}
miner_assets = {}
miner_items = {}
miner_antagonists = {}
miner_rivals = {}
miner_locs = {}
miner_monsters = {}
miner_plot_hooks = {}

noble_drives = {}
noble_catalysts = {}
noble_friends = {}
noble_assets = {}
noble_items = {}
noble_antagonists = {}
noble_rivals = {}
noble_locs = {}
noble_monsters = {}
noble_plot_hooks = {}

nomad_drives = {}
nomad_catalysts = {}
nomad_friends = {}
nomad_assets = {}
nomad_items = {}
nomad_antagonists = {}
nomad_rivals = {}
nomad_locs = {}
nomad_monsters = {}
nomad_plot_hooks = {}

outlander_drives = {}
outlander_catalysts = {}
outlander_friends = {}
outlander_assets = {}
outlander_items = {}
outlander_antagonists = {}
outlander_rivals = {}
outlander_locs = {}
outlander_monsters = {}
outlander_plot_hooks = {}

pirate_drives = {}
pirate_catalysts = {}
pirate_friends = {}
pirate_assets = {}
pirate_items = {}
pirate_antagonists = {}
pirate_rivals = {}
pirate_locs = {}
pirate_monsters = {}
pirate_plot_hooks = {}

pilgrim_drives = {}
pilgrim_catalysts = {}
pilgrim_friends = {}
pilgrim_assets = {}
pilgrim_items = {}
pilgrim_antagonists = {}
pilgrim_rivals = {}
pilgrim_locs = {}
pilgrim_monsters = {}
pilgrim_plot_hooks = {}

prisoner_drives = {}
prisoner_catalysts = {}
prisoner_friends = {}
prisoner_assets = {}
prisoner_items = {}
prisoner_antagonists = {}
prisoner_rivals = {}
prisoner_locs = {}
prisoner_monsters = {}
prisoner_plot_hooks = {}

sage_scholar_drives = {}
sage_scholar_catalysts = {}
sage_scholar_friends = {}
sage_scholar_assets = {}
sage_scholar_items = {}
sage_scholar_antagonists = {}
sage_scholar_rivals = {}
sage_scholar_locs = {}
sage_scholar_monsters = {}
sage_scholar_plot_hooks = {}

sailor_drives = {}
sailor_catalysts = {}
sailor_friends = {}
sailor_assets = {}
sailor_items = {}
sailor_antagonists = {}
sailor_rivals = {}
sailor_locs = {}
sailor_monsters = {}
sailor_plot_hooks = {}

scout_drives = {}
scout_catalysts = {}
scout_friends = {}
scout_assets = {}
scout_items = {}
scout_antagonists = {}
scout_rivals = {}
scout_locs = {}
scout_monsters = {}
scout_plot_hooks = {}

soldier_drives = {}
soldier_catalysts = {}
soldier_friends = {}
soldier_assets = {}
soldier_items = {}
soldier_antagonists = {}
soldier_rivals = {}
soldier_locs = {}
soldier_monsters = {}
soldier_plot_hooks = {}

spy_drives = {}
spy_catalysts = {}
spy_friends = {}
spy_assets = {}
spy_items = {}
spy_antagonists = {}
spy_rivals = {}
spy_locs = {}
spy_monsters = {}
spy_plot_hooks = {}

teacher_drives = {}
teacher_catalysts = {}
teacher_friends = {}
teacher_assets = {}
teacher_items = {}
teacher_antagonists = {}
teacher_rivals = {}
teacher_locs = {}
teacher_monsters = {}
teacher_plot_hooks = {}

tinker_drives = {}
tinker_catalysts = {}
tinker_friends = {}
tinker_assets = {}
tinker_items = {}
tinker_antagonists = {}
tinker_rivals = {}
tinker_locs = {}
tinker_monsters = {}
tinker_plot_hooks = {}

urchin_drives = {}
urchin_catalysts = {}
urchin_friends = {}
urchin_assets = {}
urchin_items = {}
urchin_antagonists = {}
urchin_rivals = {}
urchin_locs = {}
urchin_monsters = {}
urchin_plot_hooks = {}

warrior_drives = {}
warrior_catalysts = {}
warrior_friends = {}
warrior_assets = {}
warrior_items = {}
warrior_antagonists = {}
warrior_rivals = {}
warrior_locs = {}
warrior_monsters = {}
warrior_plot_hooks = {}

weirdo_drives = {}
weirdo_catalysts = {}
weirdo_friends = {}
weirdo_assets = {}
weirdo_items = {}
weirdo_antagonists = {}
weirdo_rivals = {}
weirdo_locs = {}
weirdo_monsters = {}
weirdo_plot_hooks = {}

continue_prompt = ""  # Initialize a loop continuation variable.
while continue_prompt!="q":
    dice_count = input_number("How many dice? ")
    sides_count = input_number("How many sides to dice? ")
    dice_list = throw_dice(dice_count, sides_count)
    print(f"List of the dice thrown: {dice_list}.")
    print("Press enter to continue or type 'q' to quit.")
    continue_prompt = input()
