# def double(x):
#   return x*2

def appl(fx, value):
  return 6 + fx(value)
#lambda arguments: expression
print(appl(lambda x: x * x , 2))

double = lambda x: x * 2
print(double(5))

cube = lambda x: x * x * x
print(cube(5))

avg = lambda x, y, z: (x + y + z) / 3
print(avg(3, 5, 10))

# with additional print statement
mult = lambda x, y: print(f'{x} * {y} = {x * y}')
mult(3,4)