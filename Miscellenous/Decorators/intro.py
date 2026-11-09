'''
#  definition of a decorator function

def decorator(arg_function): #arg_function to be decorated
   def nested_function():
      #this wraps the arg_function and extends its behaviour
      #call arg_function
      arg_function()
   return nested_function

'''

# Examples of Python Decorators
def my_function(x):
    print("The number is=",x)
def my_decorator(some_function, num):
    def wrapper(num):
        print("Inside Wrapper check odd/enve")
        if num % 2 == 0:
            ret = "Even"
        else:
            ret = "Odd!"
        some_function(num)
        return ret
    print("Wrapper function is called")
    return wrapper
no = 10
my_function = my_decorator(my_function, no)
print("It is ", my_function(no))

print("\n\n")

def my_decorator(some_function):
   def wrapper(num):
      print("Inside wrapper to check odd/even")
      if num%2 == 0:
         ret= "Even"
      else:
         ret= "Odd!"
      some_function(num)
      return ret
   print ("wrapper function is called")
   return wrapper

@my_decorator
def my_function(x):
   print("The number is=",x)
no=10
print ("It is ",my_function(no))