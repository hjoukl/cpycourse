!!! question "Lesson: Command Line Calculation"

    === "Task"
    
        Use Python as a "command line calculator" to calculate repayment plus
        compound interest for 

        - a yearly interest of 3%,
        - a duration of 3 years and
        - an investment of 91514.17 €.

        What will be the total amount after 3 years?

        Remember how interest calculation works:

        If I own 100 EUR today and I get 3% interest per year in a savings 
        account, I will have 103 EUR in one year. If I keep the money in the
        bank for another year, I will then have 106.09 EUR.

        Python uses the `*`operator for multiplication and the `**` operator
        for exponentiation.


    === "Hints"

        Perform the task in an interative Python session (the "REPL"), on the
        command line or e.g. in Jupyter.

    === "Solution"

        ??? example "*Really* take a peek now?"

            ```
            >>> 91514.17 * 1.03**3
            100000.00444159
            ```

            Alternative:

            ```
            >>> 91514.17 * 1.03 * 1.03 * 1.03
            100000.00444159
            ```

            Explanation:
            
            ```
            >>> principal = 91514.17
            >>> interest_rate = 0.03 
            >>> q = 1 + interest_rate  # factor
            >>> t = 3  # time interval in years
            >>> accumulated_value = principal * q**t
            >>> accumulated_value
            100000.00444159
            ```
