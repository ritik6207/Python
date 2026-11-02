zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
    if char not in 'aeiou':
        print(char, end='')

print("\n\n")
# Python for Loop with Tuples
numbers = (34,54,67,21,78,97,45,44,80,19)
total = 0
for num in numbers:
    total += num
print('Total =',total)

print("\n\n")
# Python for Loop with Lists
numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0
for num in numbers:
    if num % 2 == 0:
       print(num, end=' , ')

print("\n\n")
# Python for Loop with Range Objects
# range(start, stop, step)
'''
Start − Starting value of the range. Optional. Default is 0
Stop − The range goes upto stop-1
Step − Integers in the range increment by the step value. Option, default is 1.
'''
for num in range(5):
   print (num, end=' ')
print()
for num in range(10, 20):
   print (num, end=' ')
print()
for num in range(1, 10, 2):
   print (num, end=' ')

print("\n\n")
# Python for Loop with Dictionaries
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
    # print(x, end=' ')
    print(x, ":", numbers[x])
print()
for x in numbers.items():
    print(x)

print("\n\n")
# Using else Statement with For Loop

#For loop to iterate between 10 to 20
for num in range(10, 20):
   #For loop to iterate on the factors
   for i in range(2,num):
      #If statement to determine the first factor
      if num%i == 0:
         #To calculate the second factor
         j=num/i
         print ("%d equals %d * %d" % (num,i,j))
         #To move to the next number
         break
      else:
         print (num, "is a prime number")
         break

print("\n\n")
# For-Else with break statement and if conditions

# creating a function to check whether the list item is a positive
# or a negative number
def positive_or_negative():
   # traversing in a list
   for i in [5,6,7]:
   # checking whether the list element is greater than 0
      if i>=0:
         # printing positive number if it is greater than or equal to 0
         print ("Positive number")
      else:
         # Else printing Negative number and breaking the loop
         print ("Negative number")
         break
   # Else statement of the for loop
   else:
      # Statement inside the else block
      print ("Loop-else Executed")
# Calling the above-created function
positive_or_negative()

print("\n\n")
# While Loops
count=0
while count<5:
   count+=1
   print ("Iteration no. {}".format(count))
else:
   print ("While loop over. Now in else block")
print ("End of while loop")