age=int(input("Enter your age: "))

if(age==18):
    print("Your age matched!!")
    print("U are good to go")

elif(age<18):
    print("You are too young!!")

else:
    print("You are an adult.")

a=200
b=300
c=400
#One line if else statement..... It is used to write quick code. But if the logic is complicated it is better to go with the usual way.
print("A") if a>b and a>c else print("B") if b>c else print("C")  
print("You are old.") if age>=30 else None