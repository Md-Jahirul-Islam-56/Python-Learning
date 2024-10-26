import time

# init = time.time() # gives the time from when this module is made
# for i in range(50000):
#     print(i)
# # print(init) 
# print(f"The execution time of the for loop is: {time.time()-init}s")

# printing local time
print(time.localtime())

t = time.localtime()

formatted_time = time.strftime("Year: %Y \nMonth: %m\nDay: %d\nHour: %H\nMinute: %M\nSecond: %S\nTimezone from UTC: %z\nLocal Weekday: %a\nFull Local Weekday: %A\nAbbreviated month: %b\nAbbreviated month (full name): %B\nDate and Time: %c\nTime in 12 hour format: %I\nAM or PM: %p", t)

print(formatted_time)