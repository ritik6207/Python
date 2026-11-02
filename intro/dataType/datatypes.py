#1. Python Numeric Data Types

# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))
# boolean variable.
b=True
print("The type of variable having value", b, " is ", type(b))
# float variable.
c=20.345
print("The type of variable having value", c, " is ", type(c))
# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))

#2. Python String Data Type
print(type("Welcome To TutorialsPoint"))
str = 'Hello World!'
print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

# 3. Python Sequence Data Types

# (a) Python List Data Type -> enclosed with [...]
print(type([2023, "Python", 3.11, 5+6j, 1.23E-4]))
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

# (b) Python Tuple Data Type -> enclosed with (...)
print(type((2023, "Python", 3.11, 5+6j, 1.23E-4)))
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

# (c) Python Range Data Type
# range(start, stop, step)
for i in range(5):
    print(i)
# Now let's modify above program to print the number starting from 2 instead of 0 −
print()
for i in range(2, 5):
    print(i)
# Again, let's modify the program to print the number starting from 1 but with an increment of 2 instead of 1:
print()
for i in range(1, 5, 2):
    print(i)

print("\n\n")
# 4. Python Binary Data Types

# (a) Python Bytes Data Type
b1 = bytes([65, 66, 67, 68, 69])
print(b1)
# Using prefix 'b' to create bytes
b2 = b'Hello'
print(b2)
# (b) Python Bytearray Data Type
# Creating a bytearray from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])
print(value)
# Creating a bytearray by encoding a string
val = bytearray("Hello", 'utf-8')
print(val)
# (c) Python Memoryview Data Type
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)

print("\n\n")
# 5. Python Dictionary Data Type
print(type({1:'one', 2:'two', 3:'three'}))
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

print("\n\n")
# 6. Python Set Data Type
print(type({2023, "Python", 3.11, 5+6j, 1.23E-4}))

print("\n\n")
# 7. Python None Type
# Declaring a variable
# And, assigning a Null value (None)
x = None
# Printing its value and type
print("x = ", x)
print("type of x = ", type(x))