class Father:
    def skill1(self):
        print("Father's Skills Gardening")
class Mother:
    def skill2(self):
        print("Mother's Skills Gardening")
class Child(Father, Mother):       # :-> Multiple Inheritance
    pass
c = Child()
c.skill1()
c.skill2()

print()
print(Child.mro())   # :-> Method Resolution Order
print(Child.__mro__) # :-> Method Resolution Order
print(Child.__bases__) # :-> Base Classes
print(Child.__name__) # :-> Class Name
print(Child.__dict__) # :-> Class Dictionary
print(Child.__module__) # :-> Module Name
print(Child.__doc__) # :-> Class Documentation
print(Child.__annotations__) # :-> Class Annotations
print(Child.__weakref__) # :-> Weak Reference
print(Child.__init__)  # :-> Constructor


# Super() Function
super(Child, c).skill1() # :-> Calling Father's Skill
super(Child, c).skill2() # :-> Calling Mother's Skill


print("\n")

class A:
    def show(self):
        print("Calling A's show()")
class B(A):
    def show(self):
        print("Calling B's show()")
        super().show()
class C(A):
    def show(self):
        print("Calling C's show()")
        super().show()
class D(B, C):
    def show(self):
        print("Calling D's show()")
        super().show()
d = D()
d.show()

print("\n")
# Diamond Problem
class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("Class B")
class C(A):
    def show(self):
        print("Class C")
class D(B, C):
    pass

d = D()
d.show()