# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call the function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

print("\n\n")
# Pass by Reference vs Value ->  we are checking the id() of a variable.
def testfunction(arg):
   print ("ID inside the function:", id(arg))
var = "Hello"
print ("ID before passing:", id(var))
testfunction(var)
