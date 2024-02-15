################### Arithmetic Operators ##########################
print('################### Arithmetic Operators ##########################')
a = 7
b = 2

# addition
print('Sum: ', a + b)

# subtraction
print('Subtraction: ', a - b)

# multiplication
print('Multiplication: ', a * b)

# division
print('division: ', a / b)

# floor division
print('Floor divison: ', a // b)

# addition
print('Sum: ', a + b)

# Module
print('Module: ', a % b)

# a to the power b 
print('Power: ', a ** b)

################# Assignment Operators #################
print('\n################# Assignment Operators #################')
# assign 10 to a
a = 10

# assign 5 to b
b = 5 

# assign the sum of a and b to a
a += b     # a = a + b

print('a += b: ', a)

################ Comparison Operators ##################
print('\n################ Comparison Operators ##################')
a = 5
b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)

################ Logical Operators ################
print('\n################ Logical Operators ################')
# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False

############## Bitwise operators ################
print('\n############## Bitwise operators ################')
x = 10
y = 4
print('Bitwise AND: ', x & y)
print('Bitwise OR: ', x | y)
print('Bitwise NOT: ', ~x)
print('Bitwise XOR: ', x ^ y)
print('Bitwise right shift: ', x >> 2)
print('Bitwise left shift: ', x << 2)

############## Special operators #################
print('\n############## Special operators #################')
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print('x1 is not y1: ', x1 is not y1)  # prints False
print('x2 is y2: ', x2 is y2)  # prints True
print('x3 is y3: ', x3 is y3)  # prints False

############# Membership operators ################
print('\n############# Membership operators ################')
message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False