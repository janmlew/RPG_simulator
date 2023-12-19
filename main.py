from warhammer40k import Creature

creature = Creature(name="Ktul")

# print(creature.roll(dice_number=1, dice_sides=100))
# print(creature.roll(2, 6))
# print(creature.roll_history)
creature.generate_stats()
