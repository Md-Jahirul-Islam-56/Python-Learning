for i in range(1,11,1): #range(start,stop-1,step)
    print(i,end=" ")

print("")

numbers=[23,45,67,87,24,12]

for i in numbers:
    print(i,end=" ")

print("")

i=1
while(i<11):
    print(i,end=" ")
    i=i+1
else:
    print("End of while loop") #else will run because there is no break

print("")

i = 1
while i < 11:
    if i == 5:
        break
    print(i, end=" ")
    i = i + 1
else:
    print("End of while loop") #else statement will not run because we have used break in the while loop
#So the conclusion is that if the loop is incomplete then the else block will execute. We can use else with for loop also in the same manner. 


print("")

for i in range(13):
    if(i==0):
        continue 
    if(i==11):
        break
    print("7 X",i,"=",7*i)

print("")

#using while as do while because there is no do while in python:
while True:
    number = int(input("Input a positive number: ")) #before checking condition the loop will run atleast once which we see in do while loop
    print(number)
    if not number > 0: #here is the condition
        print("You have entered a negative number")
        break


