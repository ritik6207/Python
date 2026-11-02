from enum import Enum, unique


class Subject(Enum):
    MATH = 1
    SCIENCE = 2
    HISTORY = 3
obj = Subject.MATH

print(type(obj))
print(obj)
print(obj.name)
print(obj.value)

print("\n\n")

@unique  # ValueError: duplicate values for key SANSKRIT: 2
class subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   GEOGRAPHY = 3
   # SANSKRIT = 2   # ValueError: duplicate values for key SANSKRIT: 2

print("\n\n")

subjects = Enum("subjects", "ENGLISH MATHS SCIENCE SANSKRIT")
print(subjects.ENGLISH)
print(subjects.MATHS)
print(subjects.SCIENCE)
print(subjects.SANSKRIT)

print("\n\n")

# Accessing Modes in Enums
class subjects(Enum):
   ENGLISH = "E"
   MATHS = "M"
   GEOGRAPHY = "G"
   SANSKRIT = "S"
obj = subjects.SANSKRIT
print(type(obj))
print(obj.name)
print(obj.value)

print("\n\n")
# Iterating through Enums
for sub in subjects:
   print (sub.name, sub.value)