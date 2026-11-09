'''
Syntax:-
    lambda parameters: expression
ex:- Normal method
    def add(a, b):
        return a + b
Use Lambda:-
    add = lambda a, b: a + b

lambda − It indicates the keyword.
parameters − They are the inputs, just like function arguments.
expression − It indicates the expression to gets evaluated and returned.
'''

# Examples of Using Lambda Expressions
array = [1, 2, 3]
result = list(map(lambda x: x ** 2, array))
print(result)

print("\n")

array = [5,10,15,20]
result = list(filter(lambda x: x % 2 == 0, array))
print(result)

print("\n")

array = ['Ravi', 'Ram', 'Ravan', 'Richel']
result = sorted(array, key=lambda x : len(x))
print(result)