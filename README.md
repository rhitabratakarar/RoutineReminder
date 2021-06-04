# RoutineReminder

A Simple application that will start when the system will start and will provide reminders based on the entries setup in the database.

# Installation

1. Git clone (make sure git is installed):

        git clone: https://github.com/rhitabratakarar/RoutineReminder.git

2. Move into the cloned directory.

3. Run this Command 

    for Ubuntu: 

        pip3 install -r requirements.txt

    for Windows:

        pip install -r requirements.txt

# About the Database:

__Note:__ Database used: Flat File Database

There will be a file called **routine.txt**. That is the database. Edit that file and save if done.

**Format:**

Work,Message,Time (24-hr Format)

Work,Message,Time (24-hr Format)

Work,Message,Time (24-hr Format)

...

**Examples:**

Test1,03:00,First Test

Test2,00:00,Second Test

Test3,12:59,Third Test

...

__Note:__ The time must be in 24-hr format. Also check there is no space after comma while separating work, message and time. 