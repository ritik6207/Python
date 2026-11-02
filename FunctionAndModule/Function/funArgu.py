# Positional or Required Arguments
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;
# Now you can call printme function
# printme()

print("\n\n")
# Keyword Arguments
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;
# Now you can call printme function
printme( str = "My string")

print("\n\n")
# Default Arguments
# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;
# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )

print("\n\n")
# Positional-only arguments
def posFun(x, y, /, z):
    print(x + y + z)
print("Evaluating positional-only arguments: ")
posFun(33, 22, z=11)

print("\n\n")
# Keyword-only arguments
def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)
print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5)

print("\n\n")
# Arbitrary or Variable-length Arguments
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;
# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )


print("\n\n")
# Python Function with Return Value
def add(x,y):
   z=x+y
   return z
a=10
b=20
result = add(a,b)
print ("a = {} b = {} a+b = {}".format(a, b, result))

print("\n\n")
# The Anonymous Functions
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2
# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))