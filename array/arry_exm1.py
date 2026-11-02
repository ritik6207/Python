import array as arr

a = arr.array('i', [1,2,3,4,5])
print(type(a), a)

# creating an array with char type
b = arr.array('u', 'BAT')
print (type(b), b)

# creating an array with float type
# c = arr.array('c', [1.1, 2.2, 3.3])
# print (type(c), c)

d = arr.array('i', [10, 20, 30])


print(a[0])
print(a[1])
print()
a.insert(1, 10)
for x in a:
    print(x)
a.remove(3)
print(a)
print(a.index(10))
a[2] = 60
print(a)

a.append(74)
print(a)

a.extend(d)
print(a)


import array as arr

# creating an array
numericArray = arr.array('i', [10,5,15,4,6,20,9])
print("Array before reversing:", numericArray)

# converting the array into list
newArray = numericArray.tolist()

# reversing the list
newArray.reverse()

# creating a new array from reversed list
revArray = arr.array('i', newArray)
print ("Array after reversing:",revArray)

a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i')
for i in range(len(a)-1, -1, -1):
   b.append(a[i])
print(a)
print(b)