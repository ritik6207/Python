'''
Syntax:-

try:
   You do your operations here
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.


# The except Clause with Multiple Exceptions

try:
   You do your operations here;
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   If there is any exception from the given exception list,
   then execute this block.
   ......................
else:
   If there is no exception then execute this block.
'''


def KelvinToFarhenheit(Temperature):
    assert (Temperature >= 0), "Colder then absolute zero"
    return (Temperature - 273.15) * 9/5 + 32
print(KelvinToFarhenheit(273))
print(KelvinToFarhenheit(505.78))
# print(KelvinToFarhenheit(-1)) # AssertionError: Colder then absolute zero
print(KelvinToFarhenheit(0))
# print(KelvinToFarhenheit(-5)) # AssertionError: Colder then absolute zero
