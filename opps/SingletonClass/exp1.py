# We can create and implement singleton classes in Python using the following ways −
'''
using __init__
using __new__
'''

# Using __init__
class SingleTon:
    __uniqueInstance = None

    @staticmethod
    def createInstance():
        if SingleTon.__uniqueInstance == None:
            SingleTon()
        return SingleTon.__uniqueInstance
    def __init__(self):
        if SingleTon.__uniqueInstance != None:
            raise Exception("This class is a singleton!")
        else:
            SingleTon.__uniqueInstance = self
obj1 = SingleTon.createInstance()
print(obj1)
obj2 = SingleTon.createInstance()
print(obj2)
print(obj1 == obj2)

print("\n\n")

# Using __new__
class SingletonClass:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the Object")
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance
obj1 = SingletonClass()
print(obj1)
obj2 = SingletonClass()
print(obj2)
print(obj1 == obj2)
