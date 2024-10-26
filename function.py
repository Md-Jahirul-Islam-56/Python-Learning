def add(a,b,c=15):
    ''' Here in c we have putted default value as 15. That means if we do not give any value for c, it will consider c=15''' #and this process of writing comments of a function is called docstring. It should be written just under the function declaration.
    return a+b+c

print(add.__doc__) #we can print docstring 
sum1=add(3,4,5)
print(sum1)

sum2=add(3,4) #used default value of c
print(sum2)

def sub(a,b):
    pass #we can keep function to declare later using pass

def average(*num): #with this we can put any numbers of argument in a function
    sum3 = 0
    for i in num:
        sum3= sum3 + i
    print("Average is:", sum3 / len(num) )

average(34,56,76,12) #with 4 arguments
average(34,56) #with 2 arguments

def name(**name): #we can use this as dictionary with **
    print("Hello", name["first_name"], name["middle_name"], name["last_name"])

name(first_name='Md.',middle_name="\bJahirul", last_name="Islam")