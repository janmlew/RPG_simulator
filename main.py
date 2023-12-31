import warhammer40k
from warhammer40k import Creature

creature = Creature()

# print(creature.roll(dice_number=1, dice_sides=100))
# print(creature.roll(2, 6))
# print(creature.roll_history)
creature.generate_random_stats()

print(f"Name: {creature.name}, Kind: {creature.kind}, Level: {creature.level}")
print(f"Characteristics: {creature.characteristics}")
print(f"Origin: {creature.origin}")
print(f"Traits: {creature.traits}")
print(f"Skills: {creature.skills}")
print(f"Talents: {creature.talents}")
print(f"Wounds: {creature.wounds}, Fate: {creature.fate}, Initiative modifier: {creature.initiative_modifier}, Psy "
      f"rating: {creature.psy}")
print(f"Corruption points: {creature.corruption}, Insanity points: {creature.insanity}")
print(f"Profit factor: {creature.profit_factor}")
print(f"Items: {creature.items}")
# skills_table.to_csv('skills_table.csv', sep=';')
# print(f"Dice rolls history: {creature.roll_history}")
# print(items_table)
