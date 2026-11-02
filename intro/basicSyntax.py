# This intro
print("Hello World")

# Python Lines and Indentation
if True:
    print("True")
else:
    print("False")

# Python Multi-Line Statements
item_one = 'One'
item_two = 'Two'
item_three = 'Three'
total = item_one + \
        item_two + \
        item_three
print(total)
# within the [], {}, or () brackets Multi-Line Statements
total = (
    10 + 20 +
    30 + 40
)
print(total)
fruits = [
    "Apple",
    "Banana",
    "Mango"
]
print(fruits)
student = {
    "name": "Ritik",
    "age": 24,
    "course": "Python"
}
print(student)

# Quotations in Python -> Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.
word = 'word'
sentence = "This is sentance"
paragraph = """This is Paragraph is should be contain 
multiple line """
print(word, sentence, paragraph, sep="\n")

# Comments in Python

# First Comment
print(8-4) # second Comment

# You can comment multiple lines as follows −

# This is a comment.
# This is a comment, too.
# This is a comment, too.
# I said that already.

# Following triple-quoted string is also ignored by Python interpreter and can be used as a multiline comments:
'''
This is a multiline
comment.
'''

# Waiting for the User
#!/usr/bin/python
# input("\n\nPress the Enter key to exit.")

# Multiple Statement Groups as Suites
if (5 > 2):
    print("5 is greater than 2")
elif (5 > 2):
    print("5 is greater than 2")
else:
    print("5 is not greater than 2")