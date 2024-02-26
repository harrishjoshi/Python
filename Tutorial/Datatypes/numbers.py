# Numeric Data Type
print('Numeric Data Type')
num1 = 5
print(num1, 'is of type', type(num1))
num2 = 5.42
print(num2, 'is of type', type(num2))
num3 = 8+2j
print(num3, 'is of type', type(num3))

# Number Systems
"""
Number System	    Prefix
Binary	            0b or 0B
Octal	            0o or 0O
Hexadecimal	        0x or 0X
"""
print('\nNumber System:')
print(0b1101011)  # prints 107
print(0xFB + 0b10)  # prints 253
print(0o15)  # prints 13

# Type Conversion
print('\nType Conversion:')
print(1 + 2.0) # prints 3.0

num1 = int(2.3)
print(num1)  # prints 2

num2 = int(-2.8)
print(num2)  # prints -2

num3 = float(5)
print(num3) # prints 5.0

num4 = complex('3+5j')
print(num4)  # prints (3 + 5j)