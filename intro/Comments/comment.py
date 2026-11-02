# Standalone single line comment is placed here
from intro.operators.WalrusOp.exm1 import result


def greet():
    print("Hello World")
greet()

# => Multi Line Comments (Consecutive Single-Line Comments)

# This function calculates the factorial of a number
# using an iterative approach. The factorial of a number
# n is the product of all positive integers less than or
# equal to n. For example, factorial(5) is 5*4*3*2*1 = 120.

def fact(n):
    if n < 0:
        return "Factorial is not defined for negative number"
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return  result
number = 5
print(f"The Factorial of {number} is {fact(number)}")

print("\n\n\n")
# => Multi Line Comment Using Triple Quoted Strings

"""
This function calculates the greatest common divisor (GCD)
of two numbers using the Euclidean algorithm. The GCD of
two numbers is the largest number that divides both of them
without leaving a remainder.
"""
def gcd(a, b):
    while b:
        a, b = b, a %b
    return a

result = gcd(48, 18)
print(f"The Greatest Common Divisor of 48 and 18 is {result}")


print("\n\n\n")
# Using Comments for Documentation
# Python Docstrings
def greet(name):
   """
   This function greets the person whose name is passed as a parameter.
   Parameters:
   name (str): The name of the person to greet
   Returns:
   None
   """
   print(f"Hello, {name}!")
greet("Alice")
print("\n")
# Accessing Docstrings
# Example: Using the .__doc__ attribute
def greet(name):
    """
    This function greets the person whose name is passed as a parameter.

    Parameters:
    name (str): The name of the person to greet

    Returns:
    None
    """
print(greet.__doc__)
print("\n")
# Example: Using the help() Function
def greet(name):
    """
    This function greets the person whose name is passed as a parameter.
    Parameters:
    name (str): The name of the person to greet
    Returns:
    None
    """
help(greet)