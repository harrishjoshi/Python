"""
`+` Operator Overloading
"""
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        
        return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 + p2)

"""
Overloading Comparison Operators
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Overload `<` operator
    def __lt__(self, other):
        return self.age < other.age
    
p1 = Person("Bob", 18)
p2 = Person("Alice", 20)
print(p1 < p2)
print(p2 < p1)
