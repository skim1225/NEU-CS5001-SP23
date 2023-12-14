# Sooji Kim
# kim.sooji1@northeastern.edu
# TheDateClass.py
# 28 November 2023

class Date:
    """
    A class that represents a date in YYYY-MM-DD format.

    Attributes:
        year = the year [int]
        month = the month [int]
        day = the day [int]
    """
    def __init__(self, year, month, day):
        """ Returns a reference to a Date object.

        PreC: year, month, and day are valid years, months, and days.
        """
        self.year = year
        self.month = month
        self.day = day

    def __eq__(self, other):
        """ Returns whether self and equals represent the same date.

        PreC: self and other a valid Date objects.
        """
        return self.year == other.year and self.month == other.month and self.day == other.day
