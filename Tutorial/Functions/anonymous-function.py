# Lambda Function Declaration
"""
    syntax: lambda argument(s) : expression 
"""
print('lambda Function without an Argument: ')
# declare a lambda function
greet = lambda : print('Hello World!')

# call the lambda
greet()

# lambda Function with an Argument
print('\nlambda Function with an Argument: ')
# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Harish')