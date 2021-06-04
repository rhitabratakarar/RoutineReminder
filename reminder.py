import time
import notify2
from itertools import cycle
import gc

reminder_list = list()
notify2.init("Test Reminder")

with open("routine.txt") as tasks:
    # open the routine.txt in read mode.
    for task in tasks:
        show_time, work, message = task.split(",")
        if message.endswith("\n"):
            # remove the next line from the end
            message = message[:-1]
        # append the tasks to reminder list
        reminder_list.append([show_time, work, message])

reminder_list = sorted(reminder_list, key=lambda x: x[0])
done_list = list()
counter = 0

#Todo: Check for the previous task times that the person might have missed.
#? scan through the list of tasks defined in routine.py and check for the 
#? previous task times that is less than the current time.
#? Then prompt the user with the missed notifications.

for task in cycle(reminder_list):
    counter += 1
    if counter >= 59:
        # reset the done list after 60 seconds.
        counter = 0
        done_list = [] 
    # get the localtime from the system
    t = time.localtime()
    # fetch the current time in Hour:Minute.
    current_time = time.strftime("%H:%M", t)
    time_to_display, summary, message = task
    # if the time to display from routine matches with current time
    # and task is not in notified list, append it and do the execution.
    if time_to_display == current_time and task not in done_list:
        done_list.append(task)
        # separate lists into 3 variables.
        # if the time defined in routine.txt matches with notification.
        notification = notify2.Notification(summary, message)
        # show the notification
        notification.show()
        del notification
    # remove the values to stop memory overflow.
    time.sleep(1)
    del t, current_time
    del time_to_display, summary, message
    # force the garbage collector to collect the non usable objects.
    gc.collect()
