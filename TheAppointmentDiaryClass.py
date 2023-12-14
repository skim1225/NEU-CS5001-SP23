# Sooji Kim
# kim.sooji1@northeastern.edu
# TheAppointmentDiaryClass.py
# 28 November 2023

from TheAppointmentClass import *

class AppointmentDiary:
    """
    A class that represents a user's appointments. Supports adding, removing, and changing appointments.

    Attributes:
        appointments: an ordered list containing a user's appointment objects [list]
    """
    def __init__(self):
        """ Returns a new appointment diary for a user as an empty list
        """
        self.appointments = []
