# Method overloading
# Not able to achieve method overloading in Python
class example:
   def add(self, a, b):
      x = a+b
      return x
   def add(self, a, b, c):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20,30))
# print (obj.add(10,20)) # :-> This will throw an error, because last method will be called

print("\n")

# Achieving method overloading this way
class example:
   def add(self, a = None, b = None, c = None):
      x=0
      if a !=None and b != None and c != None:
         x = a+b+c
      elif a !=None and b != None and c == None:
         x = a+b
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))

print("\n\n")

# Implement Method Overloading Using MultipleDispatch
'''
pip install multipledispatch
'''

from multipledispatch import dispatch

class Example:
   @dispatch(int, int)
   def add(self, a, b):
      x = a + b
      return x
   @dispatch(int, int, int)
   def add(self, a, b, c):
      x = a + b + c
      return x
obj = Example()
print(obj.add(10,20,30))
print(obj.add(10,20))

