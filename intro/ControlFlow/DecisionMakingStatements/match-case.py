def weekday(n):
   match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(7))
print("\n\n")

# Combined Cases in Match Statement
def access(user):
    match user:
        case "admin" | "manager" : return "Full Access"
        case "guest" : return "Limited Access"
        case _: return "No Access"
print(access("admin"))
print(access("manager"))
print(access("guest"))
print (access("Ravi"))

print("\n\n")
# List as the Argument in Match Case Statement
'''
Since Python can match the expression against any literal, you can use a list as a case value.
Moreover, for variable number of items in the list, they can be parsed to a sequence with "*" operator.
'''
def greeting(details):
   match details:
      case [time, name]:
         return f'Good {time} {name}!'
      case [time, *names]:
         msg=''
         for name in names:
            msg+=f'Good {time} {name}!\n'
         return msg
print (greeting(["Morning", "Ravi"]))
print (greeting(["Afternoon","Guest"]))
print (greeting(["Evening", "Kajal", "Praveen", "Lata"]))

print("\n\n")
# Using "if" in "Case" Clause
def intr(details):
   match details:
      case [amt, duration] if amt<10000:
         return amt*10*duration/100
      case [amt, duration] if amt>=10000:
         return amt*15*duration/100
print ("Interest = ", intr([5000,5]))
print ("Interest = ", intr([15000,3]))
