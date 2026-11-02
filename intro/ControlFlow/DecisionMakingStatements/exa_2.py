x = int(input("Enter your age: "))
y = input("Are you a citizen (yes/no)? ")
if x >= 18:
    if y.lower() == "yes":
        print("Eligible to vote.")
    else:
        print("Must be a Citizen to vote.")
else:
    print("Must be at least 18 years old to vote.")