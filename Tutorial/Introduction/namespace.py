#Scope and Namespace
# global_var is in the global namespace
global_var = 10

def outer_function():
    #  outer_var is in the local namespace 
    outer_var = 20

    def inner_function():
        #  inner_var is in the nested local namespace 
        inner_var = 30

        print('Inner: ', inner_var)

    print('Outer: ', outer_var)

    inner_function()

# print the value of the global variable
print('Global: ', global_var)

# call the outer function and print local and nested local variables
outer_function()

#Use of global Keyword
# define global variable 
global_val = 10

def my_function():
    # define local variable
    local_val = 20

    # modify global variable value 
    global global_val
    global_val = global_val + local_val

# print global variable value
print('Global Val Before Modification: ', global_val)

# call the function and modify the global variable
my_function()

# print the modified value of the global variable
print('Global Val After Modification: ', global_val)