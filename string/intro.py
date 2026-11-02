var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')

print ("My name is %s and weight is %d kg!" % ('Zara', 21))

var = 'Welcome to "Python Tutorial" from TutorialsPoint'
print ("var:", var)

var = '''Welcome to TutorialsPoint'''
print ("var:", var)

var = '''
Welcome To
Python Tutorial
from TutorialsPoint
'''
print ("var:", var)

var = "Welcome To TutorialsPoint"
print (type(var))

s1="WORD"
print ("original string:", s1)
l1=list(s1)

l1.insert(3,"L")

print (l1)

s1=''.join(l1)
print ("Modified string:", s1)

name = "Tutorialspoint"
print("Welcome to %s!" % name)

str = "Welcome to {}"
print(str.format("Tutorialspoint"))

item1_price = 2500
item2_price = 300
total = f'Total: {item1_price + item2_price}'
print(total)


from string import Template

# Defining template string
str = "Hello and Welcome to $name !"

# Creating Template object
templateObj = Template(str)

# now provide values
new_str = templateObj.substitute(name="Tutorialspoint")
print(new_str)