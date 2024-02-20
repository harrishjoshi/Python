# Converting integer to float
integer_num = 123
float_num = 1.23
new_number = integer_num + float_num
print('Integer to float example')
print('Value: ', new_number)
print('Data Type: ', type(new_number))

# Explicit Type Conversion
# users convert the data type of an object to required data type
# We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion
# Addition of string and integer Using Explicit Conversion
num_str = '12'
num_int = 23
# explict conversion
print('\nExplicit Type Conversion Example')
print('Data Type before casting: ', type(num_str))
num_str = int(num_str)
print('Data Type after casting: ', type(num_str))
num_sum = num_int + num_str
print('Sum: ', num_sum)
print('Data Type of num_sum: ', type(num_sum))