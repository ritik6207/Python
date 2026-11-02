import mymodule

mymodule.SayHello("Ritik")

print(dir(mymodule))

from mymodule import sum, power

print("Sum: ", sum(20, 20))
print("Power: ", power(4, 2))

import mymodule as x
print("Average: ", x.average(4, 6))

print ("__file__ attribute:", mymodule.__file__)
print ("__doc__ attribute:", mymodule.__doc__)
print ("__name__ attribute:", mymodule.__name__)
# print ("__dict__ attribute:", mymodule.__dict__)
# print ("__package__ attribute:", mymodule.__package__)

# dir() function
# The dir() built-in function returns a sorted list of strings containing the names defined by a module.
import math
print("math.sqrt(): ", math.sqrt(2))
print(dir(math))