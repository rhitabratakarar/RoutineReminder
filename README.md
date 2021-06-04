# RoutineReminder

A Simple application that will start when the system will start and will provide reminders based on the entries setup in the database.

# Installation

1. Git clone (make sure git is installed):

        git clone: https://github.com/rhitabratakarar/RoutineReminder.git

2. Move into the cloned directory.

3. Run this Command 

        pip3 install -r requirements.txt

# About the Database:

__Note:__ Database used: Flat File Database

There will be a file called **routine.txt**. That is the database. Edit that file and save if done.

**Format:**

Time (24-hr Format), Work, Message

Time (24-hr Format), Work, Message

Time (24-hr Format), Work, Message

...

**Examples:**

13:17, First Test, Done

13:18, Second Test, Done

13:19, Third Test, Done

...

__Note:__ The time must be in 24-hr format.