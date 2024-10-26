a = None
b = None

print(a is b) # exact location of object in memory
print(a is None) # exact location of object in memory
print(a == b) # value

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

a = "hello"
b = "hello"

print(a == b)  # True 
print(a is b)  # True because python saves the same data once and if multiple variables are created then they are exactly same this

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True