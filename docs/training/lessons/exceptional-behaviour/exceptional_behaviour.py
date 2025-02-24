# exceptional_behaviour.py
import random

# Retrieve input from the user.
# Since we do not know what the user will enter we must safeguard the
# text to int conversion.
dice_rolls_no = -1
while dice_rolls_no < 0: 
    user_input = input('How many times do you want to roll the dice: ')
    try:
        dice_rolls_no = int(user_input)
    except ValueError as exc:
        print(f'Please provide integer input (Exception: {exc}).')

roll_results = []
for idx in range(dice_rolls_no):
    roll_result = random.randint(1, 6)
    roll_results.append(roll_result)

print('Your dice roll results are ', roll_results)
