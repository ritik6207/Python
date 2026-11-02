class Employee:
    "Common base class for all employee"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, " , Salary: ", self.salary)


# Built-In Class Attributes in Python
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

emp1 = Employee("Ritik", 15000)
emp2 = Employee("Nidhi", 2000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

#  access attributes
print(hasattr(emp1, "age"))
print(getattr(emp1, "empCount"))
print(setattr(emp1, "empCount", 20))
del emp1.empCount
print(getattr(emp1, "empCount"))

# Built-in Class of Python datatypes
num = 20
print (type(num))
num1 = 55.50
print (type(num1))
s = "TutorialsPoint"
print (type(s))
dct = {'a':1,'b':2,'c':3}
print (type(dct))
def SayHello():
   print ("Hello World")
   return
print (type(SayHello))

# Data Hiding in Python

class JustCounter:
    __countValue = 0

    def counter(self):
        self.__countValue += 1
        print(self.__countValue)

count = JustCounter()
count.counter()
count.counter()
# print(count.__countValue)  -> you can't access outside of class
print()
print(count._JustCounter__countValue)