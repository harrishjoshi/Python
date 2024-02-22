# import addition module
import addition

# use add function from addition module
sum = addition.add(1, 2)
print('Sum:', sum)

# Standard Library Modules
# import standard math module 
import math
# use math.pi to get value of pi
print("The value of pi is", math.pi)

# import with Renaming
# import module by renaming it
import math as m

print('PI:', m.pi)

# from...import statement
# import only pi from math module
from math import pi

print('Value of PI:', pi)

# Import all names
# import all names from the standard module math
from math import *

print("The value of pi is:", pi)

# The dir() built-in function
print(dir(addition))
print(addition.__name__)