# Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.

class Shape:
    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self): #the number and type of arguments, as well as the return type, must be the same.
        print("Calculating area of a circle...")
        super().area()
        return 3.14 * self.radius * self.radius
    
c1 = Circle(4.5)
print(c1.area()) #will print area of circle (derived class)