# while Loop
print('While Loop: ')
number = 1
while number <= 3:
    print(number)
    number = number + 1

# while loop with break statement
print('\nwhile loop with break statement: ')
while True:
    user_input = input('Enter your name: ')
    # terminate the loop when user enters end
    if user_input == 'end':
        print(f'The loop is ended')
        break  
    print(f'Hi {user_input}')

# while loop with an else clause
print('\nwhile loop with an else clause: ')
counter = 0
while counter  <  2:
    print('This is inside loop')
    counter = counter + 1
else:
    print('This is inside else block')

