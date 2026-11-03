def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

try:
    result = divide(10, 2)
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)

# Raising Custom Exceptions
class MyCustomError(Exception):
    pass
def risky_function():
    raise MyCustomError("Something went wrong!")
try:
    risky_function()
except MyCustomError as e:
    print(e)


# Creating Custom Exceptions
class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 18 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)
def set_age(age):
   if age < 18 or age > 100:
      raise InvalidAgeError(age)
   print(f"Age is set to {age}")
try:
   set_age(5)
except InvalidAgeError as e:
   print(f"Invalid age: {e.age}. {e.message}")