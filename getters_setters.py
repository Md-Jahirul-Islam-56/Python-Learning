# Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator.

# It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter

# while direct access is possible in Python (because Python relies on convention rather than strict enforcement of private variables), getters and setters provide flexibility, safety, and future-proofing in larger or more complex systems.

class MyClass:
  def __init__(self, value):
      self._value = value
    
  def show(self):
    print(f"Value is {self._value}")
    
  @property
  def ten_value(self):
      return 10* self._value
    
  @ten_value.setter
  def ten_value(self, new_value):
      self._value = new_value/10

obj = MyClass(10)
print(obj.ten_value) 
obj.show()
obj.ten_value = 67
obj.show()
