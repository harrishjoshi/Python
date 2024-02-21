# Example of a recursive function
print('Example of a recursive function:')

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))

"""The Python interpreter limits the depths of recursion to help avoid infinite recursions, resulting in stack overflows.
By default, the maximum depth of recursion is 1000. If the limit is crossed, it results in RecursionError. Let's look at one such condition."""
def recursor():
    recursor()
recursor()
# Output
"""Traceback (most recent call last):
   ...
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded"""