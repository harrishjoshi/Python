#if…else Statement
print('if…else Statement Example: ')
number = 10
if number > 0:
    print('Positive number')
else:
    print('Negative number')

#if…elif…else Statement
print('\nif…elif…else  Statement Example: ')
number = 0
if number > 0:
    print('Positive number')
elif number < 0:
    print('Negative number')
else:
    print('Zero')

#Nested if Statements
print('\nNested if Statements Example: ')
number = 5
# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
      print('Number is 0')
    # inner else statement
    else:
        print('Number is positive')
# outer else statement
else:
    print('Number is negative')