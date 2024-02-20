import constant

# assign value to site_name variable
site_name = 'python.org'

# Output: python.org
print(site_name)

# assigning a new value to site_name
site_name = 'apple.com'
print(site_name)

#Assigning multiple values to multiple variables
a, b, c = 5, 3.2, 'Hello'

print(a)  # prints 5
print(b)  # prints 3.2
print(c)  # prints Hello 

site1 = site2  = 'python.com'

print(site1)  # prints python.com
print(site2)  # prints python.com

#Rules for Naming Variables
#Constant and variable names should have a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_)
#Examples:
# snake_case
# MACRO_CASE
# camelCase
# CapWords

my_name = 'Harish Joshi'
current_salary = 25
print(my_name)
print(current_salary)

#Constants
print("Value of PI: ", constant.PI)
# print Gravity value
print("Value of Gravity: ", constant.GRAVITY)

#Literals
language = 'Python'
print(language)

#Numeric Literals
x = 42
print(type(x))  # <class 'int'>
y = 3.14
print(type(y))  # <class 'float'>
z = 1 + 2j
print(type(z))  # <class 'complex'>

# Boolean Literals
resutl1 = True
resutl2 = False
print(resutl1)
print(resutl2)

#Special Literal
#Use to specify a null variable
student = None
print(student) # Output: None

#Literal Collections
# list literal
fruits = ["Apple", "Mango", "Orange"]
print(fruits)

# tuple literal
numbers = (1, 2, 3)
print(numbers)

# dictionary literal
alphabets = {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}
print(alphabets)

# set literal
vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels) 