# 1. Python Assertions

## Definition & Purpose
Assertions are  statements that you can use to set sanity checks during the development process. Assertions allow you to test the correctness of your code by checking if some specific conditions remain true, which can come in handy while you’re debugging code.

The assertion condition should always be true unless you have a bug in your program. If the condition turns out to be false, then the assertion raises an exception and terminates the execution of your program.

Assertions are mainly for debugging. They’ll help you **ensure that you don’t introduce new bugs while adding features and fixing other bugs in your code**.


## Basic Example
*q33* here is the python file that contains the functions *mystery*.

```.pycon
from q33 import mystery
import pytest

def test_mystery():
    assert mystery([1,2,3,4,5],[3,4,5,7,6])==[3,4,5]
    assert mystery([1, 2, 3, 4, 5], [5, 7, 6,2,4]) == [5]
```

Here, the result is:
```pycon
============================= test session starts ==============================
collecting ... collected 1 item

test_q33.py::test_mystery FAILED                                         [100%]
test_q33.py:3 (test_mystery)
[2, 4, 5] != [3, 4, 5]

Expected :[3, 4, 5]
Actual   :[2, 4, 5]
```
**So even if you put 2 asserts in one function, it will only return the last one**


## Common Assertion Formats
[Real Python: Python Assertion Statements](https://realpython.com/python-assert-statement/#getting-to-know-assertions-in-python)
### Comparison Assertions
### Membership Assertions
### Identity Assertions
### Type Check Assertions