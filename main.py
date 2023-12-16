from warhammer40k import Creature

creature = Creature(name="Ktul")

print(creature.roll(dice_number=1, dice_sides=100), creature.roll(2, 6))
