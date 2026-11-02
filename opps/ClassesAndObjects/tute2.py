# class Methods
'''
There are Two way create class Method
1. Using classmethod() Function:
        syntax->  "classmethod(instance_method)"
2. Using @classmethod Decorator:
    syntax->
        @classmethod
        def method_name():
            # your code
'''

# Using classMethod() Funtion
class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Employee.empCount += 1
    def showCount(self):
        print(self.empCount)
    # counter = classmethod(showCount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
# e1.showcount()
# Employee.counter()

# Using @classmethod Decorator
class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1

    @classmethod
    def showcount(cls):
        print (cls.empCount)

    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e4 = Employee.newemployee("Anil", 21)

Employee.showcount()

class Cloths:
    price = 4000
    @classmethod
    def showPrice(cls):
        return cls.price

print(Cloths.showPrice())

# Dynamically Add Class Method to a Class
class Cloths:
    pass
@classmethod
def brandName(cls):
    print("Name of the brand is Raymond")

# Adding Dynamically
setattr(Cloths, "brand_name", brandName)
newObj = Cloths()
newObj.brand_name()

print("\n")

# Dynamically Delete Class Methods
class Cloth:
   # class method
   @classmethod
   def brandName(cls):
      print("Name of the brand is Raymond")

# deleting dynamically
del Cloth.brandName
print("Method deleted")