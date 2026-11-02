# In Python, a dictionary is a built-in data type that stores data in key-value pairs
d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)

# Creating a dictionary using curly braces
sports_player = {
   "Name": "Sachin Tendulkar",
   "Age": 48,
   "Sport": "Cricket"
}
print ("Dictionary using curly braces:", sports_player)
# Creating a dictionary using the dict() function
student_info = dict(name="Alice", age=21, major="Computer Science")
print("Dictionary using dict():",student_info)

student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}
# Accessing values using square brackets
name = student_info["name"]
print("Name:",name)

# Accessing values using the get() method
age = student_info.get("age")
print("Age:",age)

from collections import defaultdict
# Using int as the default factory to initialize missing keys with 0
d = defaultdict(int)
# Incrementing the value for key 'a'
d["a"] += 1
print(d)

# Using list as the default factory to initialize missing keys with an empty list
d = defaultdict(list)
# Appending to the list for key 'b'
d["b"].append(1)
print(d)

# Using a custom function as the default factory
def default_value():
    return "N/A"

d = defaultdict(default_value)
print(d["c"])


student = {"name": "Alice", "age": 21, "major": "Computer Science"}
for key, value in student.items():
    print(key, value)