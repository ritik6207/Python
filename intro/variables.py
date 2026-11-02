# *Memory Addresses* Python's built-in id() function returns the address where the object is stored.
month = "May"
age = 18
print(id(month))
print(id(age))

# Creating Python Variables
counter = 100          # Creates an integer variable
miles   = 1000.0       # Creates a floating point variable
name    = "Zara Ali"   # Creates a string variable
print (counter)
print (miles)
print (name)

# Deleting Python Variables
# del counter
# print(counter)

# Getting Type of a Variable
print(type(counter))
print(type(miles))
print(type(name))

# Casting Python Variables
x = str(10)    # x will be '10'
y = int(10)    # y will be 10
z = float(10)  # z will be 10.0

print( "x =", x )
print( "y =", y )
print( "z =", z )

# Case-Sensitivity of Python Variables
age = 20
Age = 30
print( "age =", age )
print( "Age =", Age )

# Python Variables - Multiple Assignment
a=b=c=10
print(a, b, c)
a,b,c = 10, 20, 30
print(a, b, c)
a = b = c = 100
print(a, b, c, sep="\n")
a,b,c = 1,2,"Zara Ali"
print (a)
print (b)
print (c)

# Python Variables - Naming Convention
counter = 100
_count  = 100
name1 = "Zara"
name2 = "Nuha"
Age  = 20
zara_salary = 100000

print (counter)
print (_count)
print (name1)
print (name2)
print (Age)
print (zara_salary)

# Python Local Variables
def sum(x, y):
    sum = x + y   # Here 'sum' is local variables
    return sum
print('Sum of ', sum(10, 20))

# Python Global Variables
x = 20
y = 50
def sum():
    sum = x + y
    return sum
print(sum())

# Python's identity operator "is" returns True if both the operands have same id() value.
a = b = 10
print(a is b)
print(id(a),id(b))

# Defining Private Variables in Python
'''
double underscore (__) -> private 
single underscore (_) -> protected
'''
class MyClass:
    def __init__(self):
        self.__private_var = "I am Private"
    def show_private(self):
        return self.__private_var
obj = MyClass()
# print(obj.__private_var) # ✗ AttributeError
print(obj.show_private())

# Name Mangling for Private Variables
print(obj._MyClass__private_var)

# Private Methods in Python
class MyMainClass:
    def __init__(self):
        self.__private_var = "I am Private"
    def __private_method(self):
        return "This is Private Method"
    def show_private(self):
        return self.__private_var + " and " + self.__private_method()

obj1 = MyMainClass()
print(obj1.show_private())
print(obj1._MyMainClass__private_method())

# Real World Example of Private Variables for Banking
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        return self.__balance
    def get_balance(self):
        return self.__balance

account = BankAccount("12345", 1000)

try:
    account.__balance += 500
except AttributeError:
    print("Direct Access to private variable fails")

print("Your Account Balance is: ", account.get_balance())
account.deposit(500)
print("Your account balance after deposit is: ", account.get_balance())
account.withdraw(200)
print("Your account balance after withdraw is: ", account.get_balance())

