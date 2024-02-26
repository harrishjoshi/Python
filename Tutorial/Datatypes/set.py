
"""
Create a Set
"""
# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)
# Note: When you run this code, you might get output in a different order. This is because the set has no particular order

"""
Create an Empty Set
"""
# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = { }

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary:', type(empty_dictionary))

"""
Duplicate Items in a Set
"""
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # {8, 2, 4, 6}
# We can see there are no duplicate items in the set as a set cannot contain duplicates

"""
Add and Update Set Items
"""
# Add Items to a Set
numbers = {21, 34, 54, 12}

print('Initial Set:', numbers)

# using add() method
numbers.add(32)

print('Updated Set:', numbers) 

# Update Set
companies = {'Zara', 'LV'}
tech_companies = ['Apple', 'Google', 'Apple']

# using update() method
companies.update(tech_companies)

print(companies)

# Remove an Element from a Set
languages = {'Python', 'Java', 'JavaScript'}

print('Initial Set:', languages)

# remove 'JavaScript' from a set
languages.discard('JavaScript')

print('Set after remove():', languages)

# Iterate Over a Set
for language in languages:
    print(language)

"""
Set Operations
"""
# Union of Two Sets
# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using |
print('Union using |:', A | B)

# perform union operation using union()
print('Union using union():', A.union(B)) 

# Set Intersection
# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform intersection operation using &
print('Intersection using &:', A & B)

# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B)) 

# Difference between Two Sets
# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('Difference using &:', A - B)

# perform difference operation using difference()
print('Difference using difference():', A.difference(B)) 

# Set Symmetric Difference
# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('using ^:', A ^ B)

# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))

# Check if two sets are equal
# first set
A = {1, 3, 5}

# second set
B = {3, 5, 1}

# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')