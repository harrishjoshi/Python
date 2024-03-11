"""
Iterating Through an Iterator
"""
# define a list
my_list = [4, 7, 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator)) # prints 4

# get the second element of the iterator
print(next(iterator)) # prints 7

# get the second element of the iterator
print(next(iterator)) # prints 0

"""
Using for Loop
"""
for element in my_list:
    print(element)

"""
Working of for loop for Iterators
"""
iterator1 = iter(my_list)
#  iterate through the elements of the iterator
for element in iterator1:
    # print each element
    print(element)

"""
Infinite Iterators
"""
from itertools import count

# create an infinite iterator that starts at 1 and increments by 1 each time
infinite_iterator = count(1)

# print the first 5 elements of the infinite iterator
for i in range(5):
    print(next(infinite_iterator))