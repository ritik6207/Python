# Function Annotations
def myfunction(a: int, b: int):
    c = a + b
    return c
print(myfunction(1, 2))
print(myfunction("Hello ", "World"))


print("\n\n")
# Function Annotations With Return Type
def myfunction(a: int, b: int) -> int:
    c = a + b
    return c
print(myfunction(10, 20))
print(myfunction.__annotations__)


print("\n\n")
# Function Annotations With Expression
def total(x: "marks in Physics", y: "marks in Maths"):
    return x + y
print(total(45,56))
print(total.__annotations__)


print("\n\n")
# Function Annotations With Default Arguments
# 1 ->
def myfun(a: "physics", b: "Maths" = 20) -> int:
    c = a + b
    return c
print(myfun(50))
print(dir(myfun))
