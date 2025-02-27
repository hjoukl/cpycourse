# roll_the_dice.py
import random

# Retrieve input from the user.
user_input = input('How many times do you want to roll the dice: ')
dice_rolls_no = int(user_input)

roll_results = []
for idx in range(dice_rolls_no):
    roll_result = random.randint(1, 6)
    roll_results.append(roll_result)

print('Your dice roll results are ', roll_results)
