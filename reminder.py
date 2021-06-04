import time, notify2, gc
from itertools import cycle

reminder_list = list()
notify2.init("Test Reminder")

with open("routine.txt") as tasks:
    # open the routine.txt in read mode.
    for task in tasks:
        show_time, work, message = task.split(",")
        show_time = show_time.strip(" ")
        work = work.strip(" ")
        message = message.strip(" ")
        if message.endswith("\n"):
            # remove the next line from the end
            message = message[:-1]
        # append the tasks to reminder list
        reminder_list.append([show_time, work, message])

reminder_list = sorted(reminder_list, key=lambda x: x[0])
done_list = list()

for task in cycle(reminder_list):
    # get the localtime from the system
    t = time.localtime()
    # fetch the current time in Hour:Minute.
    current_time = time.strftime("%H:%M:%S", t)
    # time left to reach the next minute.
    left_time = 60 - int(current_time[-2:])
    time.sleep(1)
    if left_time == 1:
        # reset the done list after 60 seconds.
        done_list = []
    
    time_to_display, summary, message = task
    # if the time to display from routine matches with current time
    # and task is not in notified list, append it and do the execution.
    if time_to_display == current_time[:5] and task not in done_list:
        done_list.append(task)
        # if the time defined in routine.txt matches with notification.
        notification = notify2.Notification(summary, message)
        # show the notification
        notification.show()
        del notification
    # remove the values to stop memory overflow.
    del t, current_time
    del time_to_display, summary, message
    # force the garbage collector to collect the non usable objects.
    gc.collect()
