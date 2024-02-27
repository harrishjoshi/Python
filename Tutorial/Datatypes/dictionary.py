"""
Create a Dictionary
"""
# creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London",
  "Nepal": "Kathmandu"
}

"""
Valid and Invalid Dictionaries
"""
# Note: Keys of a dictionary must be immutable
# valid dictionary
# integer as a key
my_dict = {1: "one", 2: "two", 3: "three"}

# valid dictionary
# tuple as a key
my_dict = {(1, 2): "one two", 3: "three"}

# invalid dictionary
# Error: using a list as a key is not allowed
"""
my_dict = {1: "Hello", [1, 2]: "Hello Hi"}
"""

# valid dictionary
# string as a key, list as a value
my_dict = {"USA": ["Chicago", "California", "New York"]}

# Keys of a dictionary must be unique
hogwarts_houses = {
    "Harry Potter": "Gryffindor",
    "Hermione Granger": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    # duplicate key with a different house
    "Harry Potter": "Slytherin"
}

print(hogwarts_houses)
# As duplicate keys are not allowed in a dictionary, the last entry overwrites the previous value.

# access the value of keys
print(country_capitals)
print(country_capitals["Germany"]) 
print(country_capitals["England"])
# Note: We can also use the get() method to access dictionary items.
print(country_capitals.get('Nepal'))

# Add Items to a Dictionary
# add an item with "Italy" as key and "Rome" as its value
country_capitals["Italy"] = "Rome"
print(country_capitals)

# Remove Dictionary Items
# delete item having "Germany" key
del country_capitals["Germany"]
print(country_capitals)

# Note: We can also use the pop() method to remove an item from a dictionary.
country_capitals.pop('Canada')
print(country_capitals)

# Change Dictionary Items
# change the value of "Italy" key to "Naples"
country_capitals["Italy"] = "Naples"
print(country_capitals)
country_capitals["Italy"] = "Rome"

# Iterate Through a Dictionary
# print dictionary keys one by one
for country in country_capitals:
    print('Key ->', country)

print()

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print('Value ->', capital)

"""
Dictionary Membership Test
"""
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# use of in and not in operators
print(".pdf" in file_types)
print(".mp3" in file_types)
print(".mp3" not in file_types)