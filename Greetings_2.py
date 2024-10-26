import time

present_time=time.strftime("Hour:%H Minute:%M Second:%S")

print(present_time)

present_hour=int(time.strftime("%H"))

if(present_hour>=12 and present_hour<=18):
    print("Good Afternoon!!")
elif(present_hour>18 and present_hour<=20):
    print("Good Evening!!")
elif(present_hour>=6 and present_hour<12):
    print("Good Morning!!")
else:
    print("Good Night!!")