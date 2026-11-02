'''
type() Function
isinstance() Function
issubclass() Function
callable() Function
getattr() Function
setattr() Function
hasattr() Function
dir() Function
'''

print (type(10))
print (type(2.56))
print (type(2+3j))
print (type("Hello World"))
print (type([1,2,3]))
print (type({1:'one', 2:'two'}))

print("\n\n")

# Syntax:- isinstance(obj, class)
print (isinstance(10, int))
print (isinstance(2.56, float))
print (isinstance(2+3j, complex))
print (isinstance("Hello World", str))
print (isinstance([1,2,3], tuple))
print (isinstance({1:'one', 2:'two'}, set))

print("\n\n")


def test():
    pass
print(callable("Hello"))
print(callable(abs))
print(callable(list.clear([1, 2])))
print(callable(test))


class test:
    def __init__(self):
        pass
    def __call__(self):
        print("Hello")
obj = test()
obj()
print("obj is callable?", callable(obj))


print("\n\n")


class test:
    def __init__(self):
        self.name = "Manav"
obj = test()
print(hasattr(obj, "age"))
print(hasattr(obj, "name"))