import random

# When rolling 4 D6s, important values are the sum and the minimum
# Then, find the difference
# Certain use cases require a stat bonus (ex. strength + 1) this has to be included as an input to calculate the modifier
def roll_4_D6(bonus=0):
	d6 = range(1,7)
	all_dice_rolls = [random.choice(d6),random.choice(d6),random.choice(d6),random.choice(d6)]
	sum_of_dice_rolls = sum(all_dice_rolls)
	min_of_dice_rolls = min(all_dice_rolls)
	difference_of_dice_rolls = int(sum_of_dice_rolls - min_of_dice_rolls)

	difference_of_dice_rolls += bonus# stat bonuses

	modifier = int((difference_of_dice_rolls - 10) / 2)

	return difference_of_dice_rolls, modifier
