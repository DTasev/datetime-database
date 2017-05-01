from __future__ import absolute_import, division, print_function

import operator
from datetime import datetime


class DatetimeDatabase(object):
    """
    For this class a date or a time MUST be specified on initialisation!

    To use it create a DatetimeDatabase(<date or time>).

    To add new data into the class do:
        db = DatetimeDatabase(<date or time>)
        date = "24/03/2014" -> date MUST be in dd/mm/YYYY format
        db.set(date, <value>) -> value can be ANY object

    This means we can do:
        date_db = DatetimeDatabase(date)
        time_db = DatetimeDatabase(time)
        time = "12:23" -> time MUST be in HH:MM format
        time_db.set(time, <power>)

        date = "12/02/2014"
        date_db.set(date, time_db)

    date_db now contains a date database, which contains a date database with all the power in it per hour

    """

    def __init__(self, date=False, time=False):
        assert date or time, "One of the formats must be specified! Either date or time as a keyword argument."
        if date and time:
            raise AssertionError("You can't have both formats selected!")

        if date:
            self.format_string = "%d/%m/%Y"
        elif time:
            self.format_string = "%H:%M"

        self.dates = {}
        self.sorted_dates = None

    def __str__(self):
        return str(self.dates)

    def __getitem__(self, key):
        if not self.sorted_dates:
            self.sorted_dates = sorted(self.dates.iterkeys())
        return self.sorted_dates[key]

    def set(self, datetime, value):
        """
        :param datetime: If date is specified format must be -> "24/03/2015" (name of format dd/mm/YYYY)
                         if time is specified format must be -> "03:33" (name of format HH:MM)
        :param value: Value which will be assigned to the datetime. This can be any object.
        """
        self.sorted_dates = None
        self.dates[self._get_datetime(datetime)] = value

    def get(self, datetime):
        """
        :param datetime: If date is specified format must be -> "24/03/2015" (name of format dd/mm/YYYY)
                         if time is specified format must be -> "03:33" (name of format HH:MM)
        """
        # TODO add a check to handle datetime objects and strings
        # something like self._handle_date() that will return a datetime always
        return self.dates[self._get_datetime(datetime)]

    def get_after(self, datetime):
        """
        Get any datetime after the specified ones in a list.
        This must match what was passed on initialisation -> date OR time.

        :param datetime: If date is specified format must be -> "24/03/2015" (name of format dd/mm/YYYY)
                         if time is specified format must be -> "03:33" (name of format HH:MM)
        """
        return self._date_comparator(datetime, operator.lt)

    def get_before(self, datetime):
        """
        Get any datetime before the specified ones in a list.
        This must match what was passed on initialisation -> date OR time.

        :param datetime: If date is specified format must be -> "24/03/2015" (name of format dd/mm/YYYY)
                         if time is specified format must be -> "03:33" (name of format HH:MM)
        """
        return self._date_comparator(datetime, operator.gt)

    def _date_comparator(self, datetime, comparator):
        if not self.sorted_dates:
            self.sorted_dates = sorted(self.dates.iterkeys())
        datetime = self._get_datetime(datetime)

        result_list = []
        for dict_date in self.dates.iterkeys():
            if comparator(datetime, dict_date):
                result_list.append(dict_date)
        return result_list

    def _get_datetime(self, date_str):
        return datetime.strptime(date_str, self.format_string)

    def iteritems(self):
        return self.dates.iteritems()

    def itervalues(self):
        return self.dates.itervalues()
