from collections import namedtuple
Vertex = namedtuple('Vertex', ['x', 'y'])
v = Vertex(19, 12)

# Access fields
print("Vertex-1:", v.x)
print("Vertex-2:", v.y)

import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])

# Adding values
S = Student('farhan', '23', '2541997')

# initializing iterable
li = ['nishu', '19', '411997']

# initializing dict
di = {'name': "ravi", 'age': 24, 'DOB': '1391997'}

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))
