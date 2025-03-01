# A Curious Python Course: Tutorial

A little introduction to the language mainly by example, to show (some of)
Python's main features.

This tutorial refers to Python version 3.

## Python Documentation

If you need information way beyond what we can show you here, the (great!)
official Python documentation can be found here:
<https://docs.python.org/3/index.html>

## Getting a Python

See here for hints on [Python installation](../main-course/installation.md).

## Starting the Python interpreter

For an **interactive interpreter session** simply type `python` or `python3` in
a console/shell of your computer (`$`-shell prompt on \*nix-based systems).

This is how this could look like on a Linux system:

``` bash
$ python
Python 3.9.21 (main, Dec  5 2024, 00:00:00)
[GCC 11.5.0 20240719 (Red Hat 11.5.0-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

You can also use a qualified interpreter version, depending on what's available
on your machine:

``` bash
$ /usr/bin/python3.12
Python 3.12.5 (main, Dec  3 2024, 00:00:00)
[GCC 11.5.0 20240719 (Red Hat 11.5.0-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Depending on where Python is installed on your system (and if it is found in
the places your OS searches for executables - e.g. your `PATH` on a Unix
system) you may want or need the fully qualified path to the Python
interpreter:

=== "Linux"

    ```bash
    $ /usr/bin/python3.12
    ```

=== "Windows"

    ```
    # & "C:/Program Files/Python/3.12/python.exe"
    ```

On interpreter startup, the first lines show the interpreter version, some
information about the build environment of the interpreter (compiler version
and platform) and the copyright information.

The Python *prompt* `>>>` is signaling that the interpreter awaits user input.

Such an interactive mode is sometimes called "Read-Eval-Print-Loop" ("REPL")
and a great way to explore Python and try out code snippets..

The version and copyright information on startup can be suppressed using the
"quiet" option `-q`.

``` bash
$ python -q
>>>
```

**Note:**
From now on, whenever you see `>>> ...`-lines this means an example in an
interactive Python session.

Start the interpreter as shown and type in your 1.st Python statement. After
pressing the `<Enter>`-key the interpreter will execute the statement, and in
this case will show the result:

(Note: `print(...)`is Python's output function)

```python
>>> print("Hello, world!")
Hello, world!
>>>
```

After finishing the execution of the statement, the interpreter comes back to
the prompt, awaiting the next input.

If you enter a simple expression at the prompt (e.g. an integer or string
[literal](../main-course/grasping-python.md/literals) and press `<Enter>` a
*string representation* of the result gets printed:

``` python
>>> "Hello, world!"
'Hello, world!'
>>> 42
42
>>> 
```

An interactive interpreter session can be stopped by pressing `Ctrl-d` (Linux)
or `Ctrl-z` (plus `Enter`, Windows).

A **summary of the Python interpreter's commandline options** can be listed
with its help option `-h`. This will display the **usage**, the available
options and **environment variables** controlling the interpreter.
Here's the output of a Python 3 interpreter on Linux:

```
$ python3.12 -h
usage: python3.12 [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options (and corresponding environment variables):
-b     : issue warnings about converting bytes/bytearray to str and comparing
         bytes/bytearray with str or bytes with int. (-bb: issue errors)
-B     : don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : turn on parser debugging output (for experts only, only works on
         debug builds); also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also -? or --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-I     : isolate Python from the user's environment (implies -E and -s)
-m mod : run library module as a script (terminates option list)
-O     : remove assert and __debug__-dependent statements; add .opt-1 before
         .pyc extension; also PYTHONOPTIMIZE=x
-OO    : do -O changes and also discard docstrings; add .opt-2 before
         .pyc extension
-P     : don't prepend a potentially unsafe path to sys.path; also
         PYTHONSAFEPATH
-q     : don't print version and copyright messages on interactive startup
-s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE=x
-S     : don't imply 'import site' on initialization
-u     : force the stdout and stderr streams to be unbuffered;
         this option has no effect on stdin; also PYTHONUNBUFFERED=x
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
         when given twice, print more information about the build
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-X opt : set implementation-specific option
--check-hash-based-pycs always|default|never:
         control how Python invalidates hash-based .pyc files
--help-env: print help about Python environment variables and exit
--help-xoptions: print help about implementation-specific -X options and exit
--help-all: print complete help information and exit

Arguments:
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]
```

## Getting Help

In an interactive session/REPL you can access Python's built-in help using
`help()`:

``` python
>>> help()
Welcome to Python 3.12's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.12/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q" or "quit".
```

Python's `help()` function also takes parameters. So you can get help on
basically any object:

``` python
>>> help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
```

--8<--
training/lessons/repl/repl.md
--8<--

--8<--
training/lessons/command-line-calculation/command-line-calculation.md
--8<--

## Running a Python program

A program is built up of a sequence of Python statements (i.e. the "program
code" or "code"). This code can be

- entered at the Python prompt, in interactive mode,
- provided as a command line argument or
- stored in module files with the `.py`-extension.

For simple, short ad-hoc one-liners it can be very handy to use command line
string arguments:

``` bash
$ python -c "print('Hello'); print('World')"
Hello
World
$
```

As shown you can use the semicolon to separate multiple statements.

But typically, code is placed into Python source files named `<module name>.py`
, in our case [helloworld.py](../../src/helloworld.py):

``` python
--8<--
src/helloworld.py
--8<--
```

The code can then be executed running the following command:

``` bash
$ python helloworld.py
Hello, world!
$
```

### Python Program Building Blocks

A program is built as a sequence of instructions. The basic building blocks of
a Python program are:

1. [Operands and
   Operators](../main-course/grasping-python.md#operands-and-operators): e.g.
`1 + 2`
2. [Expressions](../main-course/grasping-python.md#expressions): e.g.
`len("some interesting string")`
1. [Statements](../main-course/grasping-python.md#statements): e.g.
`string_size = len("some interesting string")`
1. [Comments](../main-course/grasping-python.md#comments): e.g.
`# This is a comment.`
`

So

- a program is a sequence of comments and statements
- (informally) a statement "does something", an expression "evaluates to a
value"
- an expression is built up from identifiers, literals and operators
- an expression can act as and be part of a statement; a statement (e.g. an
assignment like `x = 1`) is not an expression

### Program Execution

Running a program can be described as a top-down, line-by-line processing:
evaluation of expressions and execution of statements.

### A Sample Python Program

Here's a simple Python program that calculates the present value of
a series of cashflows:

!!! example

    === "Code"

        ```python
        --8<--
        src/present_value.py
        --8<--
        ```

    === "Hints"

        The present value (PV) of a series of cash flows represents the current
        value of an expected future income stream.

        Think of it like this: if I receive an amount in the future - what 
        would it be worth today?

        Often, the net present value (NPV) of some initial investment
        (principal, at time t=0) and then a series of discounted revenues over
        time (t=1, t=2, ...) is calculated to support investment decisions: an
        NPV > 0 promises an expected net gain or an investment with a higher
        NPV would preferrable to one with a lower NPV.

        The basic PV formula/model assumes a fixed "market" interest rate over
        time. This is a simplification, of course: in reality the future cash
        flows and/or the interest rates are usually uncertain or at least
        there's the potential risk of them changing or not materializing.
        Any model needs to simplify reality, anything that deals with the
        unknown future needs to make assumptions or expectations.

Running this program yields the following output:

```
$ python3 src/present_value.py
Present value for [-100, -2, 3, 6, 8, 110] and interest rate 0.03:
    pv = 8.371752776288233
```

So according to net present value (NPV) model assumptions this looks like a
worthwile investment. :wink:

## Variables and Assignments

Variables are one of the key elements of programming languages. Although
the implementations may differ, the key concept is the same:
Providing named access to an object in memory.

In Python a variable is a name referencing an object in memory (i.e. there's
"names and values").

You can create a variable with an assignment statement:

``` python
>>> a = 5  # variable 'a' is a name for the value 5 (an object)
```

Python variables can be rebound by further assignments. At different points
in time, the variable may refer to different objects, with different values
and types of value. This makes Python a dynamically typed language.

``` python
>>> a = 5 # create variable 'a' which is bound to integer object 5
>>> a     # named access to object
5
>>> type(a) # the object named 'a' is of type 'int'
<class 'int'>
>>> a = 'foo' # rebind the variable (name) 'a' to a different object
>>> a
'foo'
>>> type(a) # 'a' is now the name for an object of type 'str'
<class 'str'>
>>>
```

## It's all about data: Python Data Types and Python Objects

[Python provides a bunch of popular data types.](../main-course/builtin-types.md)

All data is represented as an object and has a type:

``` python
>>> 'foo'
'foo'
>>> type('foo')  # type built-in function returns an object's type
<class 'str'>
>>> isinstance('foo', str)  # isinstance tests if an object is of a certain type
True
>>>
```

You can access an object's attributes with the `.`-operator:

``` python
>>> "foo".upper  # Attribute access: give me the "upper" attribute of str "foo"
<built-in method upper of str object at 0x7f2342e6f8f0>
>>> 
```

If such an attribute is *callable* (a "method") then you can invoke it:

``` python
>>> "foo".upper()  # call a method like <method_name>()
'FOO'
>>> 
```

### Strings - `str`

Strings are essential for handling text data:

``` python
>>> 'Python knows text'
'Python knows text'
>>> "Python knows text"  # double-quoted is also allowed
'Python knows text'
>>> # triple quoted text can span lines
>>> """Python
... knows
... text"""
'Python\nknows\ntext'
>>> 
```

Strings conveniently support many useful operations:

``` python
>>> ''.join(('foo', 'bar'))  # string concatenation using builtin method 'join()'
'foobar'
>>> 'foo' + 'bar'            # string concatenation using '+' operator
'foobar'
>>> 'foobar'.upper()         # copy of string in all-uppercase letters
'FOOBAR'
>>> 'foo bar'.title()        # copy of string in "title case"
'Foo Bar'
```

``` python
Strings are *sequences* of characters indexed by integer values. You can use
indexes to access the individual characters:

>>> 'foo bar'[0]  # 1st character
'f'
>>> 'foo bar'[-1]  # last character
'r'
>>> 'foo bar'[2:5]  # slice of characters
'o b'
>>> 
```

Like for any other sequence types in Python indexing is zero-based i.e. the
first character in a string is indexed with `0`.

Strings have powerful formatting support. In modern Python you usually use
"f-strings". These allow for embedding expressions that get replaced with their
values:

``` python
>>> name, says = 'Patti', 'yo'
>>> f'{name} says {says}'
'Patti says yo'
>>> 
```

Older style formatting is done with the `str.format` method:

```python
>>> '{} says {}'.format('Peter', 'hi')
'Peter says hi'
>>> '{person} says {statement}'.format(person='Mary', statement='hey')
'Mary says hey'
>>>
```

The `str.format`variant is especially useful when you want a string *template*
rather than evaluating at once.

Even more oldschool:

``` python
>>> '%s says %s' % ('Paul', 'ho')
'Paul says ho'
```

See <https://pyformat.info/> for concise information on these topics.

--8<--
training/lessons/hello-world/hello-world.md
--8<--

### Numeric Data Types

Numeric data types represent numeric values. Python has the built-in numeric
data types `int` and `float` that support the usual arithmetic operations.

`int` is used for integers or "whole" numbers:

``` python
>>> 1
1
>>> type(1)
<class 'int'>
```

Some basic integer operations:

``` python
>>> 1 + 2
3
>>> (1 + 2) * 3
9
>>> 2**5
32
>>> 
```

Fractional numbers are represented by `float`:

``` python
>>> 1.2
1.2
>>> type(1.2)
<class 'float'>
```

Example `float` operations:

``` python
>>> 1.1 + 1.2
2.3
>>> (1.1 + 1.2) * 3.0
6.8999999999999995
>>> 1.1**2
1.2100000000000002
>>> 
```

As you'll have noticed `float` is
[not an exact data type](https://docs.python.org/3/tutorial/floatingpoint.html)
.

If you need more accuracy than `float`  arithmetic supports the Python
standard library also features a
[Decimal data type](https://docs.python.org/3/library/decimal.html).

Since Python 3.0 Python uses "true division". That means that integer division
will result in float values:

``` python
>>> 4 / 2
2.0
>>> 3 / 2
1.5
```

Depending on your needs you can also use "floor" division:

``` python
>>> 4 // 2
2
>>> 3 // 2
1
>>> 
```

Using floor division ensures that the resulting data type is an integer.

### Lists - `list`

A Python list is an array of unnamed objects of (potentially) different types.

``` python
>>> [1, 'foo', 3.14]
[1, 'foo', 3.14]
>>> type([1,'foo', 3.14])
<class 'list'>
```

Similar to `str` list supports many useful sequence operations:

``` python
>>> [1, 'foo', 3.14] # list of 3 elements
[1, 'foo', 3.14]
>>> [1, 'foo', 3.14] + ['bar']
[1, 'foo', 3.14, 'bar']
>>> type([1, 'foo', 3.14] + ['bar'])
<class 'list'>
>>> len([1, 'foo', 3.14]) # get length of a list
3
>>> my_list = [1, 'foo', 3.14]
>>> my_list[0]
1
>>> my_list[-1]
3.14
>>> my_list[0:1]
[1]
>>> my_list[0:2]
[1, 'foo']
>>> my_list[1:]
['foo', 3.14]
>>> my_list.insert(2, 'bar')
>>> my_list
[1, 'foo', 'bar', 3.14]
>>> my_list.pop()
3.14
>>> my_list.index('foo')
1
>>> del my_list[0]
>>> my_list
['foo', 'bar']
>>> my_list[0] = 'bea'
>>> my_list
['bea', 'bar']
>>> 
```

--8<--
training/lessons/list-modification/list-modification.md
--8<--

### Tuples - `tuple`

Tuples are pretty similar to lists. They can store unnamed objects of different
type but opposed to Python lists, they are unchangeable. I.e. elements can't be
inserted, substituted or removed:

``` python
>>> (1, 'foo', 3.14)
(1, 'foo', 3.14)
>>> type((1, 'foo', 3.14))
<class 'tuple'>
```

Example tuple operations:

``` python
>>> len((1, 'foo', 3.14)) # length of a tuple
3
>>> my_tuple = (1, 'foo', 3.14)
>>> my_tuple[0]
1
>>> my_tuple[-1]
3.14
>>> my_tuple[0:2]
(1, 'foo')
>>> my_tuple + (42, )  # create a new extended tuple by concatenation
(1, 'foo', 3.14, 42)
>>> del my_tuple[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion
>>> my_tuple[0] = 'more'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment
>>> 
```

### Dictionaries - `dict`

Dictionaries are a nearly ubiquituous data type in Python. Dictionaries are a
"mapping" data type storing key-value data:

``` python
>>> {'name': 'Paul', 'age': 26, 'profession': 'author'}
{'name': 'Paul', 'age': 26, 'profession': 'author'}
>>> type({'name': 'Paul', 'age': 26, 'profession': 'author'})
<class 'dict'>
>>>
```

Example `dict` operations:

``` python
>>> dct = {'name': 'Paul', 'age': 26, 'profession': 'author'}
>>> dct['name']
'Paul'
>>> dct['age'] = 27
>>> list(dct.items())
[('name', 'Paul'), ('age', 27), ('profession', 'author')]
>>> list(dct.keys())
['name', 'age', 'profession']
>>> list(dct.values())
['Paul', 27, 'author']
>>> del dct['age']
>>> dct
{'name': 'Paul', 'profession': 'author'}
>>> dct.popitem()
('profession', 'author')
>>> dct
{'name': 'Paul'}
>>> 

```

### Sets - `set`

The Python `set` is a datatype similar to a mathematical set. It's a collection
of unique objects, (potentially) of different types, and supports set
operations like `union`, `intersection` and others.

``` python
>>> {1, 2, 'foo'}
{1, 2, 'foo'}
>>> set([1, 2, 'foo'])  # create set from a list
{1, 2, 'foo'}
>>> set((1, 2,'foo'))  # create set from a tuple
{1, 2, 'foo'}
>>> type({1, 2, 'foo'})
<class 'set'>
>>> 
```

Some set operations examples:

``` python
>>> set([1, 2, 'foo', 'foo'])  # set from a list with a duplicate element
{1, 2, 'foo'}
>>> set([1, 2,'foo']) & set([1, 2]) # intersection of 2 sets using '&'-operator
{1, 2}
>>>
>>> {1, 2, 3}.difference({1, 2})
{3}
>>> {1, 2, 3}.union({1, 2, 4})
{1, 2, 3, 4}
>>> {1, 2, 3}.intersection({1, 2, 4})
{1, 2}
>>> 
```

### None - `None`

The Python `None` object is a built-in singleton (there's only ever one unique
`None` object in a Python process) and frequently used as a "null" object to
denote the absence of a value.

A very common use is as a default function argument.

``` python
>>> None
>>> type(None)
<class 'NoneType'>
>>>
```

### Boolean - `bool`

The Python `bool` type has two built-in values named `False` and `True`:

``` python
>>> True
True
>>> type(True)
>>> <class 'bool'>
>>> False
False
>>> type(False)
>>> <class 'bool'>
>>> 
```

For historical reasons (early Python didn't have a dedicated boolean type),
`bool` is derived from int:

``` python
>>> True + 1
2
>>>
```

## Input and Output

Programs serve a purpose (hopefully). Typically they follow the IPO model:

Input - Processing - Output

I.e. programs consume information (input), do some work (based on that input)
and produce information (output).

Program input information can be "raw data"" or "commands" (which tell the
program what to do with the data).

The output information will be computed data. Which may be simple status
information describing the state of (individual) processing steps, more/other
"raw data", or follow-up "commands" (possibly as input to other programs).

Programs can consume and produce information from and to different channels.
Two very important channels are often referred to (in unixy terms) as
"standard input" (aka stdin) and "standard output" (aka stdout).

These enable us to provide input to and retrieve output from a program, e.g.
for interactive user input or output to the terminal/screen.

In Python the builtin functions `input()` and `print()` perform these basic
tasks.

Input examples:

``` python
>>> # just echo the input
>>> input('Please enter your name: ')
Please enter your name: Idefix
'Idefix'
>>>
```  

``` python
>>> # store the input
>>> name = input('Please enter your name: ')
Please enter your name: Idefix
>>> 
```

Output examples:

``` python
>>> # print the previously stored input
>>> print('Hello %s' % name)
Hello Idefix
>>> 
```

You can also directly reuse an input invocation result for output:

``` python
>>> print(f"Hello {input('Please enter your name: ')}")
Please enter your name: Idefix
Hello Idefix
>>>
```

## Control Flow

[Wikipedia](https://en.wikipedia.org/wiki/Control_flow) describes control flow
as follows:

"In computer science, control flow (or flow of control) is the order in which
individual statements, instructions or function calls of an imperative program
are executed or evaluated. The emphasis on explicit control flow distinguishes
an imperative programming language from a declarative programming language."

Python provides two kinds of explicit controls affecting the order of
execution:

1. Choices
2. Loops

### Choices

Choices are conditional controls, affecting the branches of execution according
to a boolean condition.

#### if Statements

Python provides different variations of `if` statements:

Simple `if` example:

``` python
>>> a = 1
>>> if a == 1:
...     print('a is 1')
... 
a is 1
>>> 
```

`if-elif` example:

``` python
>>> a = 2
>>> if a == 1:
...     print('a is 1')
... elif a == 2:
...     print('a is 2')
... 
a is 2
>>>
```

`if-elif-else` example:

``` python
>>> a = 4
>>> if a == 1:
...     print('a is 1')
... elif a == 2:
...     print('a is 2')
... elif a == 3:
...     print('a is 3')
... else:
...     print('a is neither 1, 2 nor 3')
... 
a is neither 1, 2 nor 3
>>>
```

If you don't want to do anything in a choice execution branch the `pass`
statement comes in handy:

``` python
>>> today = "Saturday"
>>> if today in ("Monday", "Tuesday", "Wednesdy", "Thursday", "Friday"):
...     print("Working hard!")
... else:
...     pass  # Really do nothing. :-)
... 
>>> 
```

`pass` is basically a "no-op".

#### match Statements

Python 3.10 introduced the `match` statement. It's a powerful
"structural pattern matching" construct that can be used to choose code
branch execution depending on the structure of an object and also bind values
to variable names.

In that sense, it can also be viewed as a choice construct. Superficially it
looks similar to switch-case constructs in other languages, and it can also
be used to implement simple `if-elif-else` logic:

``` python
>>> a = 4
>>> match a:
...     case 1:
...         print('a is 1')
...     case 2:
...         print('a is 2')
...     case 3:
...         print('a is 3')
...     case _:
...         print('a is neither 1, 2 nor 3')
... 
a is neither 1, 2 nor 3
```

However you'd probably stick with `if-elif-else` for such simple cases.

--8<--
training/lessons/check-user-input-evenness/check-user-input-evenness.md
--8<--

#### Conditional Expressions

Python also supports
[Conditional expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions):

``` python
>>> 1 if True else 0  # Read: <result expr> if <condition> else <else expr>
1
>>> 
```

Being an expression, a conditional expression can be written on the right hand
side of an assignment:

``` python
>>> a = 3
>>> result = 'a is 1' if a == 1 else 'a is not 1'
>>> print(result)
a is not 1
>>>
```

### Loops

Loops are repetitive controls, affecting the number of times (iterations) a
code block is executed.

#### for Statement

The Python `for` statement is a representative of what Wikipedia calls a
[count-controlled-loop](https://en.wikipedia.org/wiki/Control_flow#Count-controlled_loops).
The number of repetitions in a `for` loop is defined by the number elements of
a (probably dynamically generated) "iterable".

Example:

``` python
>>> for elem in [1, 2, 3]:  # number of elements in the list defines the number of repetitions
...     print(elem)
... 
1
2
3
>>>
```

`for` loops operate on *iterables* - something which can be iterated on, for
example sequences (e.g. lists, tuples, strings).

Regularly, `for` loops are used with `range` objects. These are iterables that
are convenient for expressing a count:

``` python
>>> for elem in range(3):  # range(3) "produces" values 0, 1, 2 for iteration
...     print(elem)
... 
0
1
2
>>>
```

#### while Statement

The Python `while` statement is a representative of what Wikipedia calls a
[condition-controlled-loop](https://en.wikipedia.org/wiki/Control_flow#Condition-controlled_loops).
In a `while` loop a condition variable is usually set before and changed within
the `while` loop.

Example:

``` python
>>> a = 1
>>> while a < 4:
...     print(a)
...     a += 1   # change the condition variable
... 
1
2
3
>>>
```

--8<--
training/lessons/roll-the-dice/roll-the-dice.md
--8<--

## Functions

Functions are **named code blocks** providing a dedicated task (procedure) or
"calculation" (function). Functions *can* have input parameters and return
values, i.e. result values returned to the caller.

A function is defined using the `def` statement:

``` python
>>> # function definition
>>> def echo(text):   # (1) function header
...    # (2) function body
...    print(text)    # 1.st statement
...
>>>
```

A function definition consists of (1) a function-header and (2) a function
body. The function header begins with the `def` keyword followed by the
function name and a (potentially empty) list of comma-separated input
parameters in parentheses, followed by a colon `:`.

The function body consists of an indented code-block of statements. In an
interactive session the `...` ellipsis show that a (multi-line) code block is
ongoing.

A function is called simply using its function name followed by a list of
comma-separated call arguments in parentheses:

``` python
>>> # function call (positional arguments)
>>> echo("Hello, world!")
Hello, world!
>>>
```

Functions can also be called using named (or keyword) arguments:

``` python
>>> # function call (named or keyword arguments)
>>> echo(text="Hello, world!")
Hello, world!
>>>
```

Functions can return values and function parameters can have default arguments:

``` python
>>> def greeting(name, greet="Hello"):
...     return greet + " " + name
...
>>> greets = greeting("Mick")  # Using the default greet text.
>>> greets  # the returned value
'Hello Mick'
>>> greets = greeting("Elvis", greet="Calling")  # Prefer a custom greet text.
>>> greets  # the returned value
'Calling Elvis'
>>>
```

A function without an explicit return statement implicitly returns `None`:

``` python
>>> echo_return_value = echo("Hello, world!")
Hello, world!
>>> print(echo_return_value)
None
>>>
```

Functions can be called repeatedly and therefore are an essential building
block of reusable code in programming languages.

--8<--
training/lessons/add-function/add-function.md
--8<--

## Classes and Instances

Python allows user-defined data types called **classes**. Classes are type
definitions which include data - so called **attributes** - and **methods** -
functions that define the type-specific behaviour. **Instances** are objects
created from classes.

The following example demonstrates a simple `class` definition,
class instantiations and common operations on class instances like attribute
access and method call using the `.` (dot) operator.

**class definition**:

``` python
>>> class Dog:
...     def __init__(self, name):   # class constructor
...         self.name = name        # instance attribute
...     def bark(self):             # instance method
...         print(f"{self.name} says wuff")
... 
>>> 
```

**class instances and attribute/method access**:

``` python
>>> my_dog = Dog("Django")  # create class instance
>>> my_dog.name             # access instance attribute with '.'-dot operator
'Django'
>>> my_dog.bark()           # call instance method using '.'-dot operator
Django says wuff
>>>
```

--8<--
training/lessons/classy-animals/classy-animals.md
--8<--

## Exceptions

Python uses exceptions to communicate invalid (or impossible) operations aka
runtime errors:

``` python
>>> 1 + "1"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Such exceptions can be caught and handled:

``` python
>>> try:
...     myfile = open('myfile.txt', 'r')
... except FileNotFoundError as exc:
...     print('caught', exc)
...     # ... (do some sensible handling of this situation here)
... 
caught [Errno 2] No such file or directory: 'myfile.txt'
>>> 
```

An exception will "travel" up the call stack until caught, or otherwise
interrupt the running program.

--8<--
training/lessons/exceptional-behaviour/exceptional-behaviour.md
--8<--

## Modules & Packages

In addition to Python's built-ins, standard library and 3rd party libraries
can be used through Python's import mechanism:

``` python
>>> import os
>>> os.listdir()
['README.md', '.git', '.gitignore', 'LICENSE', 'mkdocs.yml', 'docs', '.github',
'site']
>>> 
```

You can modularize your own code using modules (files) and packages
(directories of module files):

``` python
--8<--
src/mymodule.py
--8<--
```

Now you can **reuse** this modularized functionality:

``` python
>>> import mymodule
>>> mymodule.myfunc("I just called")
I just called
42
>>> 
```

## Generators

A callable that doesn't return a single value but generates - possibly
unlimited - values is called a generator. Generators *yield* values instead
of returning values:

``` python
>>> def gen(limit=-1):
...     if limit < 0:
...         val = 0
...         while True:
...             yield val
...             val += 1
...     else:
...         for val in range(limit):
...             yield val
... 
>>> for i in gen(5):
...     print(i)
... 
0
1
2
3
4
```

Note how generators look like functions but have a `yield` in their body.

For memory efficiency, these generated values are created on demand, in each
iteration step, as opposed to pre-populating e.g. a large list.

Essentially, a generator's  processing gets suspended when `yield`ing (and
resumed later, to get at next yield values).

A generator function can delegate to other generators using the `yield from`
expression:

``` python
>>> def gen_func():
...     for value in range(5):
...         yield value
... 
>>> def other_gen_func():
...     yield from gen_func()
... 
>>> for i in other_gen_func():
...     print(i)
... 
0
1
2
3
4
>>> 
```

--8<--
training/lessons/generate-un-even-numbers/generate-un-even-numbers.md
--8<--

## Comprehensions and Generator Expressions

### List Comprehensions

**List comprehensions** are an elegant and powerful feature to populate lists
using a syntax that very much feels like a mathematical set notation:

``` python
>>> import os  # operating system (OS) routines
>>> dirs = [entry for entry in os.listdir() if os.path.isdir(entry)]
>>> dirs
['.git', 'docs', '.github', 'site']
>>> 
```

Compare this to a "traditional" `for` loop solution:

``` python
>>> import os
>>> dirs = []
>>> for entry in os.listdir():
...     if os.path.isdir(entry):
...         dirs.append(entry)
...
>>> dirs
['includes', 'docs', '.git', '.github']
>>> 
```

### Generator Expressions

Similarly, one can use **generator expressions** that do not pre-populate a
data structure but yield elements on demand:

``` python
>>> import os
>>> generate_dirs = (entry for entry in os.listdir() if os.path.isdir(entry))
>>> generate_dirs
<generator object <genexpr> at 0x7fc61861de60>
>>> list(generate_dirs)
['.git', 'docs', '.github', 'site']
>>> list(generate_dirs)  # watch out: the generator has been "exhausted"
[]
```

### Dict Comprehensions

A **dict comprehension** can be used to create a dictionary:

``` python
>>> import os
>>> {entry: 'link' if os.path.islink(entry) else
...         'dir' if os.path.isdir(entry) else
...         'file' if os.path.isfile(entry) else
...         'other'
...  for entry in os.listdir()}
{'README.md': 'file', '.git': 'dir', '.gitignore': 'file', 'LICENSE': 'file',
'mkdocs.yml': 'file', 'docs': 'dir', '.github': 'dir', 'site': 'dir'}
>>> 
```

--8<--
training/lessons/rewrite-dict-comprehension/rewrite-dict-comprehension.md
--8<--

### Set Comprehensions

A **set comprehension** can be used to create a set from an iterable:

``` python
>>> {elem for elem in [1, 2, 3, 1, 2]}
{1, 2, 3}
>>> 
```

## Wrapping Up

Congratulations! You've pretty much made it through the tutorial. Reward
yourself by sending a friendly little electronic letter to yourself, or
Donald. :wink:

--8<--
training/lessons/sendmail-2-donald/sendmail-2-donald.md
--8<--

--8<--
training/lessons/send-mail/send-mail.md
--8<--

## Conclusion

This concludes the tutorial material! While not having touched on each and
every language feature and detail the essential Python building blocks have
been introduced.

Find more material in the [Main Course...](../main-course/main-course.md)
