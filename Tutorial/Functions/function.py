# Function Call
print('Function Call:')

def greet():
    print('Hello World!')

# call the function
greet()
print('Outside function')

# Function Arguments
print('\nFunction Arguments:')

def greet(name):
    print("Hello", name)

# pass argument
greet("Harish")

# Function to Add Two Numbers
print('\nFunction to Add Two Numbers:')

def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)

# Parameters and Arguments
print('\nParameters and Arguments:')

def print_age(age):  # age is a parameter
    print(age)

print_age(25)  # 25 is an argument

# The return Statement
print('\nThe return Statement:')

# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)
print('Square: ', square)

# The pass Statement
print('\nThe pass Statement:')

def future_function():
    pass

# this will execute without any action or error
future_function()  

# Default Arguments in Functions
print('\nDefault Arguments in Functions:')

def greet(name, message = "Hello"):
    print(message, name)

# calling function with both arguments
greet("Alice", "Good Morning")
# calling function with only one argument
greet("Bob")

# Using *args and **kwargs in Functions
print('\nUsing *args and **kwargs in Functions:')
# function to sum any number of arguments
# Using *args allows a function to take any number of positional arguments
print('Using *args:')

def add_all(*numbers):
    return sum(numbers)

# pass any number of arguments
print(add_all(1, 2, 3, 4)) 

# Using **kwargs allows the function to accept any number of keyword arguments
print('Using **kwargs: ')

# function to print keyword arguments
def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")

# pass any number of keyword arguments
greet(name="John", greeting="Hello")