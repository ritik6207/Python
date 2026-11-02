list1 = ['physics', 'chemistry', 1997, 2000]
print (list1)
del list1[2]
print ("After deleting value at index 2 : ")
print (list1)


lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
for i in indices:
   print ("lst[{}]: ".format(i), lst[i])


# Iterate using List Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print (squared_numbers)

# Iterate using the enumerate() Function
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
   print(index, fruit)