import random
def roll_4_d6():
	#d6 created 
	d6 = list(range(1,7))
	#4d6 rolled and placed in a list 
	all_dice_rolls = [random.choice(d6),random.choice(d6),random.choice(d6),random.choice(d6)]  
	#The contents of the list are then added together
	sum_of_dice_rolls = sum(all_dice_rolls)
	#The smallest value of said list is assigned to a variable 
	min_of_dice_rolls = min(all_dice_rolls)
	#The smallest value is subtracted from the sum of all rolls in the list
	difference_of_dice_rolls = int(sum_of_dice_rolls - min_of_dice_rolls)
	#Printing sum, min, and difference to make sure operation is done properly
	modifier = int(((difference_of_dice_rolls)-10) /2)
	return difference_of_dice_rolls

def roll_Barbarian_HP(constitution):
    #d12 created
    d12_sides = list(range(7,13))
    d12 = random.choice(d12_sides)
    HP = d12 + constitution 
    return HP