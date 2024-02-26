"""
Create Lists
"""
print('Create Lists:')
# create an empty list
empty_list = []
print(empty_list)

# a list of three elements
ages = [19, 26, 29]
print(ages)

# list of string types
names = ['James', 'Jack', 'Eva']
print (names)

# list of float types
float_values = [1.2, 3.4, 2.1]
print(float_values)

# list including string and integer
student = ['Jack', 32, 'Computer Science']
print(student)

"""
Access List Elements
"""
print('\nAccess List Elements:')
languages = ['Python', 'JavaScript', 'Java']

# access the first element
print(languages[0])   # Python

# access the third element
print(languages[2])   # Java

# Negative Indexing in Python
# access item at index 0
print(languages[-3]) # Java

# access item at index 2
print(languages[-1]) # Java

# Note: If the specified index does not exist in a list, Python throws the IndexError exception.

"""
Slicing of a List in Python
"""
print('\nSlicing of a List in Python:')
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])

"""
Add Elements to a List
"""
print('\nAdd Elements to a List:')
fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)

# using append method 
fruits.append('cherry')

print('Updated List:', fruits)

# Add Element at Specific Index
print('\nAdd Element at Specific Index:')
fruits = ['apple', 'banana', 'orange']
print("Original List:", fruits) 

# insert 'cherry' at index 2
fruits.insert(2, 'cherry')

print("Updated List:", fruits)

# Add Elements to a List From Other Iterables
print('\nAdd Elements to a List From Other Iterables:')
odd_numbers = [1, 3, 5]
print('Odd Numbers:', odd_numbers)

even_numbers  = [2, 4, 6]
print('Even Numbers:', even_numbers)

# adding elements of one list to another
odd_numbers.extend(even_numbers)

print('Numbers:', odd_numbers) 

# Change List Items
print('\nChange List Items:')
colors = ['Red', 'Black', 'Green']
print('Original List:', colors)

# changing the third item to 'Blue'
colors[2] = 'Blue'

print('Updated List:', colors)

# Note: Unlike tuples, lists are mutable, meaning we can change the items in the list.

# Remove an Item From a List
print('\nRemove an Item From a List:')
numbers = [2,4,7,9]

# remove 4 from the list
numbers.remove(4)

print(numbers)

# Remove One or More Elements of a List
print('\nRemove One or More Elements of a List:')
names = ['John', 'Eva', 'Laura', 'Nick']

# deleting the second item
del names[1]
print(names)

# deleting the first item 
del names[0:1]
print(names)

names = ['John', 'Eva', 'Laura', 'Nick']

# Note: We can also delete the entire list by using the del statement
# deleting the entire list
del names

# List Length
print('\nList Length:')
cars = ['BMW', 'Mercedes', 'Tesla']

print('Total Cars: ', len(cars)) 

# Iterating Through a List
print('\nIterating Through a List:')
# iterate through the list
for car in cars:
    print(car)