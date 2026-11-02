'''
In languages like Java and Go, there is keyword called interface which is used to define an interface.
Python doesn't have it or any similar keyword.
It uses abstract base classes (in short ABC module) and @abstractmethod decorator to create interfaces.

NOTE: In Python, abstract classes are also created using ABC module.
'''

# Ways to implement Interfaces in Python
'''
Formal Interface
Informal Interface
'''
# Formal Interface
from abc import ABC, abstractmethod

class DemoInterface:
    @abstractmethod
    def method1(self):
        print("Abstract method1")
        return
    @abstractmethod
    def method2(self):
        print("Abstract method2")
        return
# class implementing the above interface
class concreteClass(DemoInterface):
    def method1(self):
        print("Concrete method1")
        return
    def method2(self):
        print("Concrete method2")
        return

obj = concreteClass()
obj.method1()
obj.method2()

print("\n\n")

# Informal Interface
class demoInterface:
    def displayMsg(self):
        pass
class newClass(demoInterface):
    def displayMsg(self):
        print("This is my message")

# creating instance
obj = newClass()
# method call
obj.displayMsg()