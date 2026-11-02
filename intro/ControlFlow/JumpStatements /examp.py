for letter in 'Python':
   if letter == 'h':
      break
   print ("Current Letter :", letter)
print ("Good bye!")

print()

no = 33
numbers = [11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
   if num == no:
      print ('number found in list')
      break
else:
   print ('number not found in list')

# continue
print("\n\n")

num = 60
print ("Prime factors for: ", num)
d=2
while num > 1:
   if num%d==0:
      print (d)
      num=num/d
      continue
   d=d+1

print("\n\n")
#  pass Statement
for letter in 'Python':
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)
print ("Good bye!")