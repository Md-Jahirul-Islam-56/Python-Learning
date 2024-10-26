# Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

class employee:
    name = "Jahirul"

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self):
        return f"The name of the employee is {self.name} str"
        
    def __repr__(self):
        return f"Employee('{self.name}')"

    def __call__(self):
        print("Hey I am good")


e = employee()
print(len(e))
print(str(e))
print(repr(e))
e()
#there are many other methods as __gt__,__lt__ used for comparing, etc
