# from win10toast import ToastNotifier

# notify = ToastNotifier()

# notify.show_toast("Are You Thirsty?", "It's time to drink water.", icon_path = "D:\\Python\\water_drinking_reminder.ico", duration=5, threaded=True)

#threaded=True: Displays the notification in a separate thread, allowing the main program to continue executing.
# threaded=False: Displays the notification in the main thread, causing the program to wait until the notification duration is complete.

#______________Above code not working in my pc because of threaded ________________



from plyer import notification
import datetime
import time 
import logging

logging.basicConfig(filename='water_reminder.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def send_notification():
    # code without icon 
    # notification.notify(
    #     title="Are You Thirsty?",
    #     message="It's time to drink water.",
    #     timeout=10
    # )

    # code with icon
    notification.notify(
        title="Are You Thirsty?",
        message="It's time to drink water.",
        app_icon="D:\\Python\\water_drinking_reminder.ico",
        timeout=10
    )
    logging.info("Notification sent.")


date_time=datetime.datetime.now()
if(date_time.hour>=18 or date_time.hour<=2):
    print(date_time.minute)
    if date_time.minute % 2 == 0:
        send_notification()
        time.sleep(10)  
