# @classmethod Decorator
class counter:
   count=0
   def __init__(self):
      print ("init called by ", self)
      counter.count=counter.count+1
      print ("count=",counter.count)
   @classmethod
   def showcount(cls):
      print ("called by ",cls)
      print ("count=",cls.count)

c1=counter()
c2=counter()
print ("class method called by object")
c1.showcount()
print ("class method called by class")
counter.showcount()

print("\n\n")

# @staticmethod Decorator
class counter:
   count=0
   def __init__(self):
      print ("init called by ", self)
      counter.count=counter.count+1
      print ("count=",counter.count)
   @staticmethod
   def showcount():
      print ("count=",counter.count)

c1=counter()
c2=counter()
print ("class method called by object")
c1.showcount()
print ("class method called by class")
counter.showcount()

print("\n\n")

# @property Decorator
'''
@property − Declares the method as a property.
@<property-name>.setter: − Specifies the setter method for a property that sets the value to a property.
@<property-name>.deleter − Specifies the delete method as a property that deletes a property.

property(fget=None, fset=None, fdel=None, doc=None)

Syntax:- 
The property() object's setter and getter may also be assigned with the following syntax also.

speed = property()
speed=speed.getter(speed, get_speed)
speed=speed.setter(speed, set_speed)

'''
class car:
   def __init__(self, speed=40):
      self._speed=speed
      return
   @property
   def speed(self):
      return self._speed
   @speed.setter
   def speed(self, speed):
      if speed<0 or speed>100:
         print ("speed limit 0 to 100")
         return
      self._speed=speed
      return

c1=car()
print (c1.speed) #calls getter
c1.speed=600 #calls setter