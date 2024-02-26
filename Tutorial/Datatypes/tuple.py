
"""
Create a Tuple
"""
numbers = (1, 2, -5)
print(numbers)

# Create a Tuple Using Tuple Constructor
tuple_constructor = tuple(('Jack', 'Maria', 'David'))
print(tuple_constructor)

# create an empty tuple
empty_tuple = ()
print(empty_tuple)

# Tuple of different data types
# tuple of string types
names = ('James', 'Jack', 'Eva')
print (names)

# tuple of float types
float_values = (1.2, 3.4, 2.1)
print(float_values)

# Tuple of mixed data types
# tuple including string and integer
mixed_tuple = (2, 'Hello', 'Python')
print(mixed_tuple)

"""
Access Tuple Items
"""
# Access Items Using Index
languages = ('Python', 'Java', 'JavaScript')

# access the first item
print(languages[0])   # Python

# access the third item
print(languages[2])   # JavaScript

# Tuple Length
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
print('Total cars:', len(cars)) 

# Iterate Through a Tuple
for car in cars:
    print(car)

# Check if an Item Exists in the Tuple
colors = ('red', 'orange', 'blue')

print('yellow' in colors)    # False
print('red' in colors)       # True

# Change Tuple Items
fruits = ('apple', 'cherry', 'orange')
# trying to change the second item to 'banana'
"""
fruits[1] = 'banana'
# Output: TypeError: 'tuple' object does not support item assignment
"""

# Delete tuple
animals = ('dog', 'cat', 'rat')
print(animals)
# deleting the tuple
del animals

# Create a Tuple With One Item
var = ('Hello')
print(type(var)) # string

var = ('Hello',) 
print(type(var))  # tuple