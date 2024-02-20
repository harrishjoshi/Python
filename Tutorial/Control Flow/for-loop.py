
# Loop through list
languages = ['Java', 'Python', 'Rust']
print('Loop through List: ')
# access elements of the list one by one
for i in languages:
    print(i)

# Loop Through a String
print('\nLoop Through a String: ')
language = 'Python'
for l in language:
    print(l)

# for Loop with range()
print('\nfor Loop with range(): ')
# iterate from i = 0 to i = 3
for i in range(4):
    print(i)

# for loop with else clause
print('\nfor loop with else clause: ')
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left.")

# for loop without accessing items
print('\nfor loop without accessing items: ')
for i in digits:
    print('Hello')

# Nested for loops
print('\nNested for loops: ')
# outer loop 
for i in range(2):
    # inner loop
    for j in range(2): 
        print(f"i = {i}, j = {j}")