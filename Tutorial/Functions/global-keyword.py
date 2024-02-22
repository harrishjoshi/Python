# Access and Modify Python Global Variable
c = 1 # global variable

def add():
    print(c)

add()

# Changing Global Variable From Inside a Function using global
c = 1 

def add():
    """
        Without the use of a global keyword, the following error will be thrown:
        UnboundLocalError: local variable 'c' referenced before assignment
    """
    # use of global keyword
    global c

     # increment c by 2
    c = c + 2
    print(c)

add()

# Global in Nested Functions
def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25
        print('Inside inner inner_function()', num)
    
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)

outer_function()
print("Outside both function: ", num)