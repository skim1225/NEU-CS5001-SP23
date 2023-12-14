# Sooji Kim
# kim.sooji1@northeastern.edu
# TheAppointmentClass.py
# 28 November 2023

from TheDateClass import *
from TheTimeClass import *

class Appointment:
    """
    A class that represents a single appointment for a user.

    Attributes:
        date: the date of the appointment [obj]
        startTime: the time the appointment starts [obj]
        endTime: the time the appointment ends [obj]
        purpose: the purpose of the appointment [str]

        date, startTime, and endTime are valid dates and times
    """
    def __init__(self, date, startTime, endTime, purpose):
        """ Returns a reference to an Appointment object.

        PreC: date and time are valid dates and times
        """
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.purpose = purpose

