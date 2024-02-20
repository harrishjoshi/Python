# Data Types | Classes | Description
# Numeric | int, float, complex | holds numberic values
# String | str | holds sequence of characters
# Sequence | list, tuple, range | holds collection of items
# Mapping | dict | holds data in key-value pair form
# Boolean | bool | holds either True or False
# Set | set, frozeenset | holds collection of unique items

# Numeric Data Type examples
num1 = 5
num2 = 5.0
num3 = 5 + 5j
print('Numeric Data Type examples')
print(num1, ' is of type ', type(num1))
print(num2, ' is of type ', type(num2))
print(num3, ' is of type ', type(num3))

# List Data Type example
languages = ["Java", "Python", "JS"]
print('\nList Data Type example')
print(languages[2])

# Tuple Data Type example
product = ('MacBook', 999.99)
print('\nTuple Data Type example')
print(product[0])
print(product[1])

# String Data Type example
name = 'Harish'
message = 'Python for beginners'
print('\nString Data Type example')
print(name)
print(message)

# Set Data Type example
student_id = {101, 102, 103, 104, 105}
print('\nSet Data Type example')
print(student_id)
print(type(student_id))

# Dictionary Data Type example
capital_city = {'Nepal': 'Kathmandu', 'England': 'London', 'Italy': 'Rome'}
print('\nDictionary Data Type example')
print(capital_city)
print(capital_city['Nepal'])
# thorws error message
#print(capital_city['Kathmandu'])

