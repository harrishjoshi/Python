# upper(): Converts the string to uppercase
langauge = 'Python is fun'
print('upper()', langauge.upper())

# lower(): Converts the string to lowercase
print('lower()', langauge.lower())

# partition(): Returns a tuple
print('partition()', langauge.partition(' '))
print('partition()', langauge.partition('is'))

# replace(): Replaces substring inside
print('replace()', langauge.replace('fun', 'good'))

# find(): Returns the index of the first occurrence of substring
print('find()', langauge.find('is'))

# rstrip(): Removes trailing characters
print('rstrip()', '"' + 'Python is fun    '.rstrip() + '"')

# split(): Splits string from left
print('split()', 'Python, is, fun'.split(','))

# startswith(): Checks if string starts with the specified string
print('startswith()', langauge.startswith('Python'))
print('startswith()', langauge.startswith('python'))

# isnumeric(): Checks numeric characters
print('isnumeric()', '512'.isnumeric())
print('isnumeric()', 'string'.isnumeric())

# index(): Returns index of substring
print('index()', langauge.index('Python'))
"""
print('index()', langauge.index('Java'))
ValueError: substring not found
"""