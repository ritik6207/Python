# The __prepare__() method should be implemented as a classmethod.


class MyMetaClass(type):
    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        print(f'Preparing namespace for {name}')
        # Customize the namespace preparation here
        custom_namespace = super().__prepare__(name, bases, **kwargs)
        custom_namespace['CONSTANT_VALUE'] = 100
        return custom_namespace

# Define a class using the custom metaclass
class MyClass(metaclass=MyMetaClass):
    def __init__(self, value):
        self.value = value
    def display(self):
        print(f"Value: {self.value}, Constant: {self.__class__.CONSTANT_VALUE}")

# Instantiate the class
obj = MyClass(42)
obj.display()