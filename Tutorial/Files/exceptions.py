# Exception Handling Using try...except
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Catching Specific Exceptions
try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound.")

# try with else clause
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print('Not not an even number!')
else:
    print(f'{num} is even number!')

# try...finally
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")