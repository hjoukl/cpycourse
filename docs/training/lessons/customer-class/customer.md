!!! question "Lesson: Customer Class"
    
    === "Task"

        1. Create the following class hierarchy:
        
            1. ***Class Customer***

                - with a class attribute `number_of_customers` (which should
                  increment with every new class instance)
                - that has an __init__ method with parameters `email`,
                  `employees`
                - that sets its instance attributes (in __init__)
                    - `id` (current value of `number_of_customers`)
                    - `email`
                    - `employees` (number of employees)
                - with an instance method: `get_employees` (returning `employees`)

            1. ***Class Retail(Customer)***

                - with a private class attribute `__type` initialized to 'Retail'
                - that has an __init__ method with parameters `name`, `email`, `employees`
                - that sets its instance attributes (in __init__)
                    - a private instance attribute `__retailname` (initialized
                      with `name`-parameter)
                - with an instance method `getName` (returning the private
                  instance attribute `__retailname`)
                - with an instance-method `getType` (returning the private
                  class attribute `__type`)

            2. ***Class Wholesale(Customer)***

                - with a private class attribute: `__type` initialized to 'Wholesale'
                - that has an __init__ method with parameters `name`, `email`, `employee`
                - that sets its instance attributes (in __init__)
                    - a private instance attribute `__wholesalename`
                      (initialized with `name`-parameter)
                - with an instance method `getName` (returning the private
                  instance attribute `__wholesalename`)
                - with an instance method `getType` (returning the private
                  class attribute `__type`)
        
        2. Create a `list` of Customers of different customer types ('Retail'-
           and 'Wholesale'-customers)
            
        3. Output the attributes `name`, `type`, `id`, `employees` for all
           customers (use a classic loop or a list comprehension)    
      
    === "Hints" 

        - provide a callable interface `__call__()` for the derived classes
          returning the customer's name

    === "Solution" 

        ??? pied-piper "Example Customer-Class Implementation"

            ``` python title="customer.py"
            --8<-- "training/lessons/customer-class/customer.py"
            ```

            [:material-file-download:](customer.py)
