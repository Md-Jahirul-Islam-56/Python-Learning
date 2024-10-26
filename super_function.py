# When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id) #will also store name and id in the employee class and we dont need to make any more variables for name and id
    self.lang = lang

rohan = Employee("Rohan Das", "420")
razon = Programmer("Razon", "2345", "Python")
print(razon.name)
print(razon.id)
print(razon.lang)