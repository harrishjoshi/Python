import random

print(random.randrange(10, 20))

list = ['a', 'b', 'c', 'd', 'e']

# get random item from list
print(random.choice(list))

# Shuffle list
random.shuffle(list)

# Print the shuffled list
print(list)

# Print random element
print(random.random())