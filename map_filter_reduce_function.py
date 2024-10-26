# ________________ MAP________________
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. 

def cube(x):
  return x * x * x
# print(cube(2))

#with a loop
l = [1, 2, 4, 6, 4, 3]
newl = []
for item in l:
  newl.append(cube(item))
print("With loop:",newl)

#with map function:
new2 = list(map(lambda x: x*x*x, l))
print("With map function:",new2)

# ___________________FILTER____________

# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate.

def filter_function(a):
  return a>2
  
newnewl = list(filter(filter_function, l))
print(newnewl)

#________________reduce________________

# The reduce function is a higher-order function that applies a function to a sequence and returns a single value

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 
  
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)