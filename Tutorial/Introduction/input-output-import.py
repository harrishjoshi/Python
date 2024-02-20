print('Python is powerful')
# Syntax of print()
# print(object= separator= end= file= flush=)
# object - value(s) to be printed
# sep (optional) - allows us to separate multiple objects inside print()
# end (optional) - allows us to add add specific values like new line "\n", tab "\t"
# file (optional) - where the values are printed. It's default value is sys.stdout (screen)
# flush (optional) - boolean specifying if the output is flushed or buffered. Default: False

# Example 1: Python Print Statement
print('\nGood Morning!')
print('It is rainy today')

# Example 2: Python print() with end Parameter
print('\nGood Morning!', end= ' ')
print('It is rainy today')

# Example 3: Python print() with sep parameter
print('\nNew Year', 2024, 'See you soon!', sep= '. ')

# Example: Print Concatenated Strings
print('Python is ' + 'powerful.')

# Output formatting
x = 5
y =10
print('\nThe value of x is {} and y is {}'.format(x, y))

# Example: User Input
# using input() to take user input
num = input('Enter a number: ')
print('You Entered:', num)
print('Data type of num:', type(num))
num1 = int(input('Enter a number: '))
print("Int value: ", num1)