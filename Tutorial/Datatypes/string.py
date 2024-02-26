# create a string using double quotes
string1 = "Python programming"

# create a string using single quotes
string2 = 'Python programming'

# Access String Characters
greet = 'hello'

# access 1st index element
print(greet[1]) # "e"

# access with negative indexing
print(greet[-4]) # "e"

# access character with slicing (from 1st index to 3rd index)
print(greet[1:4])  # "ell"

# Note: If we try to access an index out of the range or use numbers other than an integer, we will get errors.

# Strings are Immutable
message = 'Hola Amigos'
"""
message[0] = 'H'
TypeError: 'str' object does not support item assignment
"""

# However, we can assign the variable name to a new string
message = 'Hola Amigos'

# assign new string to message variable
message = 'Hello Friends'

print(message);

# Multiline string
message = """
This is multiline
string.
"""
print(message)

# String Operations
# Compare Two Strings
str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)

# Join Two or More Strings
greet = "Hello, "
name = "Jack"

# using + operator
result = greet + name
print(result)

# Iterate Through a String
greet = 'Hello'
for letter in greet:
    print(letter)

# String Length
# count length of greet string
print(len(greet))

# String Membership Test
print('a' in 'program') # True
print('at' not in 'battle') # False