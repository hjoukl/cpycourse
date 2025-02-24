!!! question "Lesson: Exceptional Behaviour"

    === "Task"

        Remember the "roll the dice" lesson?

        What happens if you enter a non-integer value when asked how many times
        the dice should be rolled?

        Extend the program to make it safe against such user input.


    === "Hints"

        You can find out what happens if you try to convert an incompatible
        input value to an `int` in the REPL.

        This gives you information about the exception type(s) you need to
        "catch" to keep from erroring out.

    === "Solution"

        ??? example "*Really* take a peek now?"

            ``` python title="exceptional_behaviour.py"
            --8<-- "training/lessons/exceptional-behaviour/exceptional_behaviour.py"
            ```

            [:material-file-download:](exceptional_behaviour.py)
