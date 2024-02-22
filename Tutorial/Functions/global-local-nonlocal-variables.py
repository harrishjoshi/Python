# Local Variables
print('Local Variables:')
def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()
"""
# try to access message variable 
# outside greet() function
print(message)
# Output: NameError: name 'message' is not defined
"""

# Global Variables
# declare global variable
print('\nGlobal Variables:')
message = 'Hello'

def greet():
    # declare local variable
    print('Inside function', message)

greet()
print('Outside function', message)

# Nonlocal Variables
print('\nNonlocal Variables:')
# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()