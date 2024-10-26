# The default values of the class are class variable and instances are unique to each object or temporary replacement of the class variables

class MyClass:

    age = 30 #class variable

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

obj1 = MyClass("John") #instance
obj2 = MyClass("Jane") #instance
print(obj1.age) #from class variable
obj1.age = 40 #instance
obj1.print_name() # Output: John
print(obj1.age) # Output: 40
obj2.print_name() # Output: Jane
