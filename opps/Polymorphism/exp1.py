# Ways of implementing Polymorphism in Python
'''
1. Duck Typing
2. Operator Overloading
3. Method Overloading
4. Method Overriding
'''
from unittest import result


# Using Duck Typing
class Duck:
    def sound(self):
        return "Quack, Quack"
class AnotherBird:
    def sound(self):
        return "I'm similar to duck"
def makeSound(duck):
    print(duck.sound())

makeSound(Duck())
makeSound(AnotherBird())

print("\n")

# Using Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Vector ({self.x}, {self.y})"
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)

print("\n")

# Using Method Overloading
def add(*nums):
    return sum(nums)

result1 = add(10, 23)
result2 = add(10, 23, 45)
print(result1)
print(result2)

print("\n")

# Method Overriding
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def draw(self):
       "Abstract method"
       return
class Circle(Shape):
    def draw(self):
        super().draw()
        print("Draw a circle")
        return
class Rectangle(Shape):
    def draw(self):
        super().draw()
        print("Draw a rectangle")
        return

shapes = [Circle(), Rectangle()]
for shp in shapes:
    shp.draw()