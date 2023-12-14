# Sooji Kim
# kim.sooji1@northeastern.edu
# TheTimeClass.py
# 28 November 2023

class Time:
    """
    A class that represents a valid time in the format HH:MM AM/PM.

    Attributes:
        hours: the hours of the time [int >= 0 and <= 12]
        mins: the minutes of the time [int >=0 and <= 59]
        tod: short for time of day, whether it is AM or PM [str]
    """
    def __init__(self, hours, mins, tod):
        """ Returns a reference to a Time object

        PreC: hours, mins, and tod are valid hours, minutes, and time of day
        """
        self.hours = hours
        self.mins = mins
        self.tod = tod

    def __lt__(self, other):
        """ Returns whether the self time is temporally before the given time.

        PreC: self and other are both valid time objects
        """  
        if self.tod == 'AM' and other.tod == 'PM':
            return True
        elif self.tod == 'PM' and other.tod == 'AM':
            return False
        else:
            if self.hours % 12 < other.hours % 12:
                return True
            elif self.hours % 12 > other.hours % 12:
                return False
            else:
                if self.mins < other.mins:
                    return True
                else:
                    return False

    def __gt__(self, other):
        """ Returns whether the self time is temporally before the given time.

        PreC: self and other are both valid Time objects
        """
        return not self < other

    def __eq__(self, other):
        """ Returns whether self and other represent the same time.

        PreC: self and other are both valid Time objects.
        """
        return self.hours == other.hours and self.mins == other.mins and self.tod == other.tod
        

        
