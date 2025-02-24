# roll_the_dice_extended.py
import random

# Retrieve input from the user.
continue_dicing = True
while continue_dicing:
    user_input = input(
        'How many times do you want to roll the dice [x to exit]: ')

    if user_input != 'x':
        dice_rolls_no = int(user_input)
        roll_results = []
        for idx in range(dice_rolls_no):
            roll_result = random.randint(1, 6)
            roll_results.append(roll_result)

        print('Your dice roll results are ', roll_results)
    else:
        continue_dicing = False
        print('Exiting the dice rolling game...')
