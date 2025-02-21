!!! question "Lesson: Command Line Calculation"

    === "Task"
    
        Explore the Python "REPL" and its `help()`function.

        Can you find out how to read interactive user input? Try to ask and
        read the user's name.

    === "Hints"

        Perform the task in an interative Python session (the "REPL"), on the
        command line.

        Taking user input is built-in Python functionality. Try `builtins` in
        help mode, or `help(builtins)`.

        This is quite a long help documentation page. It is "paged" and you can
        move inside the document. Use blank/space to move forward, and `b` to
        move back. To search for a specific text use  `/` followed by the text,
        plus `Enter`. You can also use `q` to quit the help system.

    === "Solution"

        ??? example "*Really* take a peek now?"

            ```
            >>> help()
            ...
            help> builtins
            ...
            # Use / to search for "input" and Enter
            ...
            # Use q to quit builtins help

            help> q
            >>>
            >>> input("Please enter your name: ")
            Please enter your name: 
            ```
