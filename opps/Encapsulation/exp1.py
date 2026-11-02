
class Student:
    def __init__(self, name, roll, marks):
        self.__name = name
        self.__roll = roll
        self.__marks = marks
    def studentData(self):
        print(self.__name, self.__roll, self.__marks)

s1 = Student("Ravi", 101, 90)
s1.studentData()

# print(s1.__name) # :-> This will throw an error, because __name is a private variable

# Python's name mangling technique. Using this we can access private variables
print(s1._Student__name) # :-> This will work, because __name is a private variable
