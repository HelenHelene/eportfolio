# Activity: Using Linters to Achieve Python Code Quality

## Introduction
This activity request us to run the code against a variety of linters to test the code quality. 

<br>

### _code_with_lint.py_

```python
import io
from math import *


from time import time

some_global_var = 'GLOBAL VAR NAMES SHOULD BE IN ALL_CAPS_WITH_UNDERSCOES'

def multiply(x, y):
    """
    This returns the result of a multiplation of the inputs
    """
    some_global_var = 'this is actually a local variable...'
    result = x* y
    return result
    if result == 777:
        print("jackpot!")

def is_sum_lucky(x, y):
    """This returns a string describing whether or not the sum of input is lucky
    This function first makes sure the inputs are valid and then calculates the
    sum. Then, it will determine a message to return based on whether or not
    that sum should be considered "lucky"
    """
    if x != None:
        if y is not None:
            result = x+y;
            if result == 7:
                return 'a lucky number!'
            else:
                return( 'an unlucky number!')

            return ('just a normal number')

class SomeClass:

    def __init__(self, some_arg,  some_other_arg, verbose = False):
        self.some_other_arg  =  some_other_arg
        self.some_arg        =  some_arg
        list_comprehension = [((100/value)*pi) for value in some_arg if value != 0]
        time = time()
        from datetime import datetime
        date_and_time = datetime.now()
        return
```
Code source: https://realpython.com/python-code-quality/

<br>


### Pylint
 - Provides comprehensive feedback, covering both logical and stylistic issues.
 - Reports unused imports, variable naming conventions, and unreachable code.
 - Tends to be verbose but thorough.
   
**pylint _code_with_lint.py_** <br>
```python
code_with_lint.py:1:0: C0114: Missing module docstring (missing-module-docstring)
code_with_lint.py:2:0: W0614: Unused import pi from wildcard import (unused-wildcard-import)
code_with_lint.py:5:0: W0611: Unused import io (unused-import)
code_with_lint.py:8:0: C0103: Constant name "some_global_var" doesn't conform to UPPER_CASE naming style (invalid-name)
code_with_lint.py:12:4: C0103: Variable name "some_global_var" doesn't conform to snake_case naming style (invalid-name)
code_with_lint.py:13:19: C0326: No space allowed after star operator (bad-whitespace)
code_with_lint.py:15:4: R1711: Useless return at end of function or method (useless-return)
code_with_lint.py:16:4: W0101: Unreachable code (unreachable)
code_with_lint.py:23:15: C0121: Comparison to None should be 'if cond is not None:' (singleton-comparison)
code_with_lint.py:26:22: C0321: More than one statement on a single line (multiple-statements)
code_with_lint.py:28:24: W0101: Unreachable code (unreachable)
code_with_lint.py:37:8: W0621: Redefining name 'time' from outer scope (redefined-outer-name)
```

### Pyflakes
 - Focuses on logical errors, such as unused imports and variables.
 - Does not emphasize style issues, making it faster but less comprehensive for style checks.
   
**pyflakes _code_with_lint.py_** <br>
```python
code_with_lint.py:1:1 'io' imported but unused
code_with_lint.py:2:1 'from math import *' used; unable to detect undefined names
code_with_lint.py:12:5 local variable 'some_global_var' is assigned to but never used
code_with_lint.py:39:44 'pi' may be undefined, or defined from star imports: math
code_with_lint.py:39:9 local variable 'list_comprehension' is assigned to but never used
code_with_lint.py:40:16 local variable 'time' defined in enclosing scope on line 4 referenced before assignment
code_with_lint.py:40:9 local variable 'time' is assigned to but never used
code_with_lint.py:42:9 local variable 'date_and_time' is assigned to but never used
```

### Pycodestyle
 - Concentrates on PEP 8 style violations.
 - Highlights formatting issues like spacing and line length.
 - Useful for enforcing consistent code style.
   
**pycodestyle _code_with_lint.py_** <br>
```python
code_with_lint.py:8:1: E302 expected 2 blank lines, found 1
code_with_lint.py:13:15: E225 missing whitespace around operator
code_with_lint.py:18:1: E302 expected 2 blank lines, found 1
code_with_lint.py:19:80: E501 line too long (80 > 79 characters)
code_with_lint.py:24:10: E711 comparison to None should be 'if cond is not None:'
code_with_lint.py:26:25: E703 statement ends with a semicolon
code_with_lint.py:30:24: E201 whitespace after '('
code_with_lint.py:34:1: E302 expected 2 blank lines, found 1
code_with_lint.py:36:58: E251 unexpected spaces around keyword / parameter equals
code_with_lint.py:36:60: E251 unexpected spaces around keyword / parameter equals
code_with_lint.py:37:28: E221 multiple spaces before operator
code_with_lint.py:37:31: E222 multiple spaces after operator
code_with_lint.py:38:22: E221 multiple spaces before operator
code_with_lint.py:38:31: E222 multiple spaces after operator
code_with_lint.py:39:80: E501 line too long (83 > 79 characters)
code_with_lint.py:43:15: W292 no newline at end of file
```
### Pydocstyle
 - Checks compliance with PEP 257 for docstrings.
 - Identifies missing or incorrectly formatted docstrings.
 - Important for maintaining documentation consistency.
   
**pydocstyle _code_with_lint.py_** <br>
```python
code_with_lint.py:1:1: D100: Missing docstring in public module
code_with_lint.py:10:1: D103: Missing docstring in public function
code_with_lint.py:19:1: D103: Missing docstring in public function
code_with_lint.py:31:1: D101: Missing docstring in public class
```

## Conclusion
Each linter has its strengths:

 - **Pylint** is the most comprehensive, catching a wide range of issues but can be overwhelming due to verbosity.
 - **Pyflakes** is efficient for detecting logical errors without concerning style, making it faster.
 - **Pycodestyle** is essential for ensuring code adheres to style guidelines, promoting readability.
 - **Pydocstyle** is crucial for maintaining proper documentation practices.

Using a combination of these tools provides a balanced approach to improving both the logical correctness and stylistic consistency of Python code.


<br><br>

## Reflections
In this activity, I learned the importance of using linters like Pylint, Pyflakes, Pycodestyle, and Pydocstyle to improve code quality. They help identify logical errors, style violations, and documentation inconsistencies, ensuring cleaner, more maintainable code.

In future assignments, I'll use these tools to enforce consistent coding styles and integrate linter checks into my workflow to catch errors early. Setting up continuous integration pipelines will help maintain code quality in team projects, and using Pydocstyle will ensure my code is well-documented. These practices will enhance the overall robustness and efficiency of my code.

<br><br>

---

## Reference
Jupter. (N.D.) Try Jupyter. Available from: https://jupyter.org/try

VanTol, A. (N.D.) Python Code Quality: Tools & Best Practices. Available from: https://realpython.com/python-code-quality/

<br><br>

---

[Return to Module 5 Unit 10](SEPM_Unit10.md)
