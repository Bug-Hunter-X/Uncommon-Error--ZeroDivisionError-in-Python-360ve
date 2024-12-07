# Uncommon Error: ZeroDivisionError in Python

This repository demonstrates a subtle bug that results in a `ZeroDivisionError` in Python.  The error arises from a conditional statement that isn't robust enough to handle edge cases like division by zero.

## The Bug

The `bug.py` file contains a function `function_with_uncommon_error` that attempts to divide by a variable that can potentially be zero.  If the input `x` is 0, the code raises a `ZeroDivisionError`.  This error can be difficult to identify in larger, more complex programs.

## The Solution

The `bugSolution.py` file contains a corrected version of the function that explicitly checks for the case where `x` is zero, thereby preventing the `ZeroDivisionError`. It uses a `try-except` block to handle the potential exception gracefully.

## How to Reproduce

1. Clone this repository.
2. Run `bug.py` using a Python interpreter.  Observe the `ZeroDivisionError`.
3. Run `bugSolution.py` using a Python interpreter.  Observe that the error is handled gracefully and the program doesn't crash.

This example highlights the importance of thorough error handling in software development and that edge cases must be properly addressed to avoid such unexpected crashes.