# Sooji Kim
# kim.sooji1@northeastern.edu
# Scheduler.py
# 28 November 2023

""" This program is a scheduling tool that allows users to create usernames and schedule appointments.
    It supports dates from 2023-01-01 to 2024-12-31 in YYYY-MM-DD format and times in HH:MM AM/PM format.
    It supports various operations with Users such as creating and deleting Users.
    It also supports various operations with Appointments such as creating, deleting, rescheduling, and reading.
"""

# IMPORT DEPENDENCIES

from TheTimeClass import *
from TheDateClass import *
from TheUserClass import *
from TheAppointmentClass import *


# GLOBAL VARS

# valid chars for usernames
ValidChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._'
# List of all user objects in the scheduling system
Users = []

def addUser():
    """ Gets a username from the user and adds a new User object to the scheduler with that username
        if the given username is valid and does not already exist in the system. Else, informs the
        user that the given username is either invalid or already exists.
    """
    username = input('Enter user: ').lower() # username for new user to be added
    if not userExists(username):
        if validUsername(username):
            Users.append(User(username))
            Users.sort(key=lambda x: x.username)
            print(username, 'has been added to users.')
        else:
            print('Enter a valid username. Valid usernames can contain letters, numbers, . or _')
    else:
        print('This user already exists.')
    

def deleteUser():
    """ Gets a username from the user and deletes the given user from the system if they exist.
        Else, informs the user that the username does not exist.
    """
    username = input('Enter the user to delete: ').lower() # username for new user to be added
    user = userExists(username) # User object with the given username
    if user:
        Users.remove(user)
        print('User sucessfully deleted.')
    else:
        print('User does not exist! Try again.')

def listUsers():
    """ Lists the usernames of all of the users in the scheduler in alphabetical order.
    """
    for user in Users:
        print(user.username)


def scheduleAppt():
    """ Schedules a new appointment for a given user if there is no time conflict with existing
        appointments. Else, informs the user there is a time conflict.
    """
    user, date, start, end = getInput('schedule') # the User, Date, and Time objects for the appointment to be scheduled  for
    if user:
        purpose = input('Enter purpose: ') # the purpose for the appointment
        newAppt = Appointment(date, start, end, purpose)
        if scheduleConflict(user, newAppt):
            print('Appointment already exists at this time.')
        else:
            user.diary.appointments.append(newAppt)
            print('Appointment has been added.')
        

def cancelAppt():
    """ Cancels an existing appointment if one exists at the given date and start time.
        Else, informs the user the appointment does not exist.
    """
    user, appt = findAppt() # the User and Appointment objects for the appointment to cancel
    if appt:
        user.diary.appointments.remove(appt)
        print('Appointment has been canceled.')
    else:
        print('Appointment does not exist.')


def findAppt():
    """ Prints whether an appointment exists for a given user, date, and time. If one exists, returns
        the user and appointment. Else, returns None by default.
    """
    user, date, start = getInput('find') # the User, Date, and Time objects for the appointment to find
    if user:
        appt = apptExists(user, date, start)
        if appt:
            print('Appointment found.')
            return user, appt
        else:
            print('No appointment found.')

def getPurpose():
    """ If an appointment exists for a given user at a given date and start time, prints the purpose
        of the appointment. Else, prints that the appointment does not exist.
    """
    user, date, start = getInput('find') # the User, Date, and Time objects for the appointment to find
    if user:
        appt = apptExists(user, date, start)
        if appt:
            print('Purpose: ', appt.purpose)
        else:
            print('No appointment found.')
        

def reschedule():
    """ If an appointment exists for a given user at a given date and start time, asks the user for
        the new date and times for the appointment. If the new appointment does not conflict with another
        appointment for that user, changes the date and times for the appointment to the new dates and times.
        Else, informs the user that there is a time conflict.
    """
    user, oldAppt = findAppt() # the User and Appointment objects for the appointment to reschedule
    if oldAppt:
        newDate = input('Enter new date (YYYY-MM-DD): ') # the new Date object for the appointment
        if validDate(newDate):
            newStart = input('Enter new start time (HH:MM AM/PM): ') # the new start Time for the appointment
            newEnd = input('Enter new end time (HH:MM AM/PM): ') # the new end Time for the appointment
            if validTime(newStartTime) and validTime(newEndTime):
                newAppt = Appointment(newDate, newStart, newEnd, oldAppt.purpose) # the new Appointment object with updated times
                if scheduleConflict(user, newAppt):
                    print('Time conflict with another appointment.')
                else:
                    oldAppt = newAppt
                    print('Appointment has been rescheduled.')
            else:
                print('Invalid time.')
        else:
            print('Invalid date.')   
    else:
        print('No appointment found.')


            
# HELPER METHODS

    
def userExists(username):
    """ If a User object with the given username exists in the scheduling system, returns the User.
            Else, returns None by default.

        PreC: username is a string
    """
    for user in Users:
        if username == user.username:
            return user


def apptExists(user, date, startTime):
    """ If an appointment at the given date and start time exists for a given user, returns the appointment.
        Else, returns None by default.

        PreC: user, date, and startTime are valid User, Date, and Time objects, respectively.
    """
    for appt in user.diary.appointments:
        if appt.date == date and appt.startTime == startTime:
            return appt



def checkConflict(appt1, appt2):
    """ Returns whether 2 appointments have overlapping times.

        PreC: appt1 and appt2 are valid Appointment objects with valid start and end Times.
    """
    start1 = appt1.startTime # start time for 1st appt
    end1 = appt1.endTime # end time for 1st appt
    start2 = appt2.startTime # start time for 2nd appt
    end2 = appt2.endTime # end time for 2nd appt
    return (start2 > start1 and start2 < end1) or (end2 > start1 and end2 < end1) or (start1 == start2)


def scheduleConflict(user, newAppt):
    """ For a given User, returns whether a given appointment has a time conflict with any of the existing
        appointments in the User's appointmentDiary.

        PreC: user is a valid and existing user object, newAppt is a valid Appointment object.
    """
    for appt in user.diary.appointments:
        if checkConflict(appt, newAppt):
            return True
    return False


def validDate(date):
    """ Determines whether a given date is in a valid format (YYYY-MM-DD) and is a valid date.
        If the date is valid, returns a Date object representing the date. Else, returns None.
        
        PreC: date is a string representation of a date.
    """
    if len(date) != 10:
        return False
    date = date.split('-') # given date as a list
    year = int(date[0]) # given year
    month = int(date[1]) # given month
    day = int(date[2]) # given day
    validYear = year == 2023 or year == 2024 # whether the given year is 2023 or 2024
    validMonth = month >= 1 and month <= 12 # whether the given month is valid
    validDay = False # whether the given day is valid
    longMonths = [1,3,5,7,8,10,12]
    if year == 2024 and month == 2:
        validDay = day <= 29 and day >= 1
    else:
        if month == 2:
            validDay = day <= 28 and day >= 1
        elif month in longMonths:
            validDay = day >=1 and validDay <= 31
        else:
            validDay = day >=1 and validDay <= 30
    if validYear and validMonth and validDay:
        return Date(year, month, day)


def validTime(time):
    """ Determines whether a given time is in a valid format (HH:MM AM/PM) and is a valid time.
        If the time is valid, returns a Time object representing the time. Else, returns None.
        
        PreC: time is a string representation of a time.
    """
    if len(time) != 8:
        return False
    hours = int(time[0:2]) # given hours
    mins = int(time[3:5]) # given mins
    tod = time[6:] # given time of day
    validHours = hours >= 0 and hours <= 12 # whether the given hours is valid
    validMins = mins >= 0 and mins <= 59 # whether the given mins is valid
    validTod = tod == 'AM' or tod == 'PM' # whether the given time of day is valid
    if validHours and validMins and validTod:
        return Time(hours, mins, tod)


def validUsername(username):
    """ Returns whether the given username is valid (contains only alphanum, ., or _.

        PreC: username is a string
    """
    valid = True # whether the given username is valid
    for char in username:
        if char not in ValidChars:
            valid = False
    return valid


def getInput(method):
    """ Collects and validates username, date, and time data from the user and returns these objects
        as appropriate for the function that called it.
        
        PreC: method is a string representing which function called this helper function.
    """
    username = input('Enter username: ').lower() # username to be collected
    user = userExists(username) # user object for given username
    if user:
        date = input('Enter date (YYYY-MM-DD): ') # given date of appointment
        date = validDate(date) # Date object representing given date string
        if date:
            startTime = input('Enter start time (HH:MM AM/PM): ') # given start time of appt
            startTime = validTime(startTime) # Time obj representing given start time
            if method == 'schedule':
                endTime = input('Enter end time (HH:MM AM/PM): ') # given end time of appt
                endTime = validTime(endTime) # Time obj representing given end time
                if startTime and endTime:
                    return user, date, startTime, endTime
                else:
                    print('Invalid time.')
                    return (None, None, None, None)
            elif method == 'find':
                if startTime:
                    return user, date, startTime
                else:
                    print('Invalid time.')
                    return (None, None, None)
        else:
            print('Invalid date.')
            if method == 'schedule':
                return (None, None, None, None)
            else:
                return (None, None, None)
    else:
        print('User does not exist.')
        if method == 'schedule':
            return (None, None, None, None)
        else:
            return (None, None, None)
    


# MAIN METHOD

if __name__ == '__main__':
    """ Presents the user with a menu of options to choose from until the user exits the program
        by entering 'x'.
    """
    while True:
        print('Welcome to Appointment Management System! What would you like to do?')
        print('[a] Add new user')
        print('[d] Delete an existing user')
        print('[l] List existing users')
        print('[s] Schedule an appointment')
        print('[c] Cancel an appointment')
        print('[f] Check for appointment on certain date and time')
        print('[p] Retrieve purpose of an appointment')
        print('[r] Reschedule an existing appointment')
        print('[x] Exit the system')
        choice = input('Enter choice: ') # the user's menu selection
        match choice:
            case 'a':
                addUser()
            case 'd':
                deleteUser()
            case 'l':
                listUsers()
            case 's':
                scheduleAppt()
            case 'c':
                cancelAppt()
            case 'f':
                findAppt()
            case 'p':
                getPurpose()
            case 'r':
                reschedule()
            case 'x':
                print('Goodbye!')
                break
            case _:
                print('Invalid option')
