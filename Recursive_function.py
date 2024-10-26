#finding factorial of a number:
def factorial(num):
    if (num == 1 or num == 0):
        return  1
    else:
        return (num * factorial(num-1))
    
num=5
print(num)
print(factorial(num))

#fibonacci number:
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage to print the first 6 Fibonacci numbers:
for i in range(6):
    print(fibonacci(i))
