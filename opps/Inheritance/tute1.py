'''
class SubClassName (ParentClass1[, ParentClass2, ...]):
   {sub class body}
'''

# Type or Inheritance
'''
Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance
'''

# Ex->
class Parent:
    @classmethod
    def parentMethod(self):
        print("Calling Parent Method")
class Child(Parent):
    @classmethod
    def childMethod(self):
        print("Calling Child Method")

obj = Child()
obj.parentMethod()
obj.childMethod()

