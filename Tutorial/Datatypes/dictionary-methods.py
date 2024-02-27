# pop(): Removes the item with the specified key.
marks = {'Physics': 67, 'Chemistry': 72, 'Math': 89}
print(marks)
element = marks.pop('Chemistry')
print('Popped Marks:', element)

# update():	Adds or changes dictionary items.
internal_marks = {'Math': 81}
marks.update(internal_marks)
print(marks)

# clear(): Remove all the items from the dictionary.
numbers = {1: "one", 2: "two"}
# removes all the items from the dictionary
numbers.clear()
print(numbers)

# keys(): Returns all the dictionary's keys.
marks_keys = marks.keys()
print(marks_keys)

# values(): Returns all the dictionary's values.
marks_values = marks.values()
print(marks_values)

# get(): Returns the value of the specified key.
math_marks = marks.get('Math')
print(math_marks)

# popitem(): Returns the last inserted key and value as a tuple.
result = marks.popitem()
print(result)

# copy(): Returns a copy of the dictionary.
copied_marks = marks.copy()
print('Original Marks:', marks)
print('Copied Marks:', copied_marks)