# Function Arguments
print('Function Arguments:')

def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)

add_numbers(2, 3)

# Function Argument with Default Values
print('\nFunction Argument with Default Values:')

def add_numbers(a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)

# function call with two arguments
add_numbers(2, 3)
#  function call with one argument
add_numbers(a = 2)
# function call with no arguments
add_numbers()

# Keyword Argument
print('\nKeyword Argument:')
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info('Eric', 'Cantona')
display_info(last_name = 'Cantona', first_name = 'Eric')

# Function With Arbitrary Arguments
print('\nFunction With Arbitrary Arguments:')

# program to find sum of multiple numbers 
def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)