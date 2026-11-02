# Traditional Way
print("Using Traditional Way:-")
stack = [1, 2, 3, 4, 5]
n = len(stack)
while len(stack)  > 0:
    print(stack.pop(), end=" ")
print("\n\n")

# Simplify using walrus operator
print("Using walrus operator")
stack = [1, 2, 3, 4, 5]
while (n := len(stack)) > 0:
    print(stack.pop(), end=" ")

print("\n\n\n")

# Walrus Operator for List Comprehensions
print("Using Traditional Way")
result = []
for x in range(10):
    y = x * x
    if y > 20:
        result.append(y)
print(result, "\n")

print("Using Walrus operator")
result = [y for x in range(10) if (y := x * x) > 20]
print(result, "\n")
