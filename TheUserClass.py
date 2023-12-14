# Sooji Kim
# kim.sooji1@northeastern.edu
# TheUserClass.py
# 28 November 2023

from TheAppointmentDiaryClass import *

class User:
    """
    A class that represents a user in the appointment scheduler.

    Attributes:
        username: the username [str]
        diary: the user's appointment diary object [obj]

        A valid username contains only alphanumeric, _, and . chars.
    """
    def __init__(self, username):
        """ Returns a reference to a User object with the given name and a appointment diary.

        PreC: username is a valid username
        """
        self.username = username
        self.diary = AppointmentDiary()
        

