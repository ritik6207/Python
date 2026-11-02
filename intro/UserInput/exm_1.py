# Using input() Function
from IPython.testing import ipunittest

name = input()
city = input()
print("Hello My name is : ", name)
print("My city is : ", city)

name = input("Enter Your name: ")
city = input("Enter Your City: ")
print("Hello My name is : ", name)
print("My city is : ", city)

# The raw_input() Function

# name = raw_input("Eneter your name - ")
# city = raw_input("Enter city name - ")
# print ("Hello My name is", name)
# print ("I am from ", city)

# Taking Numeric Input in Python

width = input("Enter the width: ")
height = input("Enter the height: ")
area = width * height
print ("Area of rectangle = ", area)

"""
Traceback (most recent call last):
  File "/mnt/work/py/intro/UserInput/exm_1.py", line 24, in <module>
    area = width * height
           ~~~~~~^~~~~~~~
TypeError: can't multiply sequence by non-int of type 'str'
"""

w = input("Enter the width: ")
width = int(w)
h = input("Enter the height: ")
height = int(h)
area = width * height
print ("Area of rectangle = ", area)

width = int(input("Enter width : "))
height = int(input("Enter height : "))


# The print() Function
city="Hyderabad"
state="Telangana"
country="India"
print(city, state, country, sep=',')  # comma, sep

city="Hyderabad"
state="Telangana"
country="India"
print("City:", city, end=" ") #in one line with space(" ")
print("State:", state)