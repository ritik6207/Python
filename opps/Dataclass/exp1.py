'''
Syntax of Dataclass
    @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)

The @dataclass decorator can take these options:-

init (default: True) − Automatically creates an __init__() method for initializing class instances.
repr (default: True) − Automatically creates a __repr__() method to provide a readable string representation of the object.
eq (default: True) − Generates an __eq__() method for comparing objects using the == operator.
order (default: False) − If set to True, comparison methods (like < and >) are generated for sorting objects.
unsafe_hash (default: False) − If false, it produces a default __hash__() method based on how equality and mutability are defined.
frozen (default: False) − Creates immutable instances (they can’t be changed after creation).
'''

# Creating a Dataclass
from dataclasses import dataclass, field, FrozenInstanceError, asdict
from typing import List


@dataclass()
class Student:
    name: str
    age: int
    roll: int

s1 = Student("Ritik", 21, 101)
s2 = Student("Alx", 24, 103)
print(s1)
print(s2)
print(s1 == s2)

print("\n\n")

# Example without Dataclass
class Student:
    def __init__(self, name:str, age:int, roll:int):
        self.name = name
        self.age = age
        self.roll = roll
    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, roll={self.roll})"
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name and self.age == other.age and self.roll == other.roll

s1 = Student("Alice", 20, 25)
s2 = Student("Bob", 22, 86)
print(s1)
print(s1 == s2)

print("\n\n")

# Default Values in Dataclass
@dataclass
class Student:
    name: str
    age: int
    percent: float = 0.0  # Default value for percent
s1 = Student("Alice", 20)
s2 = Student("Bob", 22, 85.5)
print(s1)
print(s2)

print("\n\n")
# Dataclass with Mutable Default Values
@dataclass()
class Course:
    name: str
    students: List[str] = field(default_factory=list) # Mutable Default Value
course1 = Course("Math")
course2 = Course("Science", ["Alice", "Bob"])
course1.students.append("Charlie")
print(course1)
print(course2)

print("\n\n")
# Immuatable/Frozen Dataclasses
@dataclass(frozen=True)
class Point:
    x: int
    y: int
p = Point(1, 2)
print(p)
try:
    p.x = 10  # This will raise an error
except FrozenInstanceError as e:
    print(e)


print("\n\n")
# Setting Up Post-Initialization
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = 0.0  # This will be calculated in __post_init__
    def __post_init__(self):
        self.area = self.width * self.height  # Calculate area after initialization
r = Rectangle(5.0, 10.0)
print(r)
print(f"Area of the rectangle: {r.area}")

print("\n\n")
# Convert Dataclass to Dictionary
@dataclass
class Student:
    name: str
    age: int
    grades: List[float]
student = Student("Alice", 20, [88.5, 92.0, 79.5])
student_dict = asdict(student)
print(student_dict)