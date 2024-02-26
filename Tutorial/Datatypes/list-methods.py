# List methods
languages = ['Python', 'Java', 'JavaScript']

# The append() method adds an item to the end of the list
languages.append('Rust')
print('List after append():', languages)

# The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list
other_languages = ['C', 'C++']
languages.extend(other_languages)
print('List after extend():', languages)

# The insert() method inserts an element to the list at the specified index
languages.insert(6, 'C#')
print('List after insert():', languages)

# The remove() method removes the first matching element (which is passed as an argument) from the list
languages.remove('C#')
print('List after remove():', languages)

# The list pop() method removes the item at the specified index. The method also returns the removed item
# remove the element at index 4
removed_element = languages.pop(4)
print('Popped Element:', removed_element)
print('List after pop():', languages)

# The index() method returns the index of the specified element in the list
index_of_c_plus_plus = languages.index('C++')
print('Index of c++:', index_of_c_plus_plus)

# The count() method returns the number of times the specified element appears in the list
print('Count of Java:', languages.count('Java'))

# The sort() method sorts the elements in ascending order
languages.sort()
print('Sorted List:', languages)

# The reverse() method reverses the elements of the list
languages.reverse()
print('Reversed List:', languages)

# The copy() method returns a shallow copy of the list
languages_copy = languages.copy()
print('Copied List:', languages_copy)

# The clear() method removes all items from the list
languages.clear()
print('List after clear():', languages)