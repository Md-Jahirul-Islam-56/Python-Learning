#To avoid an error we use this method. Whenever any error occurs in the program, we show an error message or change the course of the| execution .

a= input("Enter a number:")

print(f"The multiplication of {a} is: ")

try:
    for i in range(1,11):
        print(f"{a} x {i} = {int(a)*i}")
except:
    print("Invalid Input!")

def sum():
    try:
        a= input("Enter First Number:")
        b= input("Enter Second Number:")
        return (int(a)+int(b))
    except:
        print("Invalid Input!!")
    finally:
        print("Sum function works or not, I will work!!") #This line will execute even if the function returns its calling

print(sum())


