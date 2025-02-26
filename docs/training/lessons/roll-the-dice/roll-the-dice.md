!!! question "Lesson: Roll the Dice"

    === "Task"
        
        Create a Python program that repeatedly rolls the dice for the user.

        The program shall ask the user how many times the dice should
        get rolled and print the result of each round.

        Our dice has 6 sides. Calculate a random dice roll result
        using `random.randint(1, 6)`.

        You need to *import* `random` to use it in your program.
        (We'll learn more about importing later on in the modules section.)

        Bonus task: Extend the program to repeat dice rolling. Aks the user if
        she'd like to continue, if yes ask again for the number of rolls.
        Repaeat until the user doesn't want to continue any more.


    === "Hints"
        
        Remember that the `input()` function returns text - to use
        number operations you will need to convert the resulting user
        input (how many times should the dice get rolled) to an `int`.

        Use a `for` or a `while` loop to repeat the dice roll according
        to the user's input.

    === "Solution"

        ??? example "*Really* take a peek now?"

            ``` python title="roll_the_dice.py"
            --8<-- "training/lessons/roll-the-dice/roll_the_dice.py"
            ```

            [:material-file-download:](roll_the_dice.py)

            ``` python title="roll_the_dice_extended.py"
            --8<-- "training/lessons/roll-the-dice/roll_the_dice_extended.py"
            ```

            [:material-file-download:](roll_the_dice_extended.py)
