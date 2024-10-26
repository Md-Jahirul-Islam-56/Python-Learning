import datetime

date_time=datetime.datetime.now()
print("Hour:",date_time.hour,"Minute:",date_time.minute,"Second:",date_time.second)

if(date_time.hour>=12 and date_time.hour<=18):
    print("Good Afternoon!!")
elif(date_time.hour>18 and date_time.hour<=20):
    print("Good Evening!!")
elif(date_time.hour>=6 and date_time.hour<12):
    print("Good Morning!!")
else:
    print("Good Night!!")

