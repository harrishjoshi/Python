# Using pass With Conditional Statement
n = 10
# use pass inside if statement
if n > 10:
    pass
print('Hello')

"""
Suppose we didn't use pass or just put a comment as:
if n > 10:
    # write code later
print('Hello')
Here, we will get an error message: IndentationError: expected an indented block
"""

# Using pass with Function
def do_something(args):
    pass

# Using pass with Class
class Example:
    pass