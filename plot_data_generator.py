from __future__ import absolute_import, division, print_function

from datetime_database import DatetimeDatabase

ERROR_MSG = "datetime_database MUST be an instance of core.datetime_database.DatetimeDatabase"


def generate_hourly(date, datetime_database):
    """
    Generate the hourly correspondence between time and value for the specified date.

    :param date: The date for which X (time) and Y (values) will be generated
    :param datetime_database: The datetime_database that will be processed.
    :return: x and y as lists
    """
    assert isinstance(datetime_database, DatetimeDatabase), ERROR_MSG
    x = []  # x is the hour
    y = []  # y is the value for the hour
    day = datetime_database.get(date)
    for time, value in day.iteritems():
        x.append(time)
        y.append(value)

    return x, y


def generate_daily(datetime_database):
    """
    Generate the compound value for each day.
    X will be the date for the day.
    Y will be the compound value for each day.

    :param datetime_database: The datetime_database that will be processed.
    :return: x and y as lists
    """
    assert isinstance(datetime_database, DatetimeDatabase), ERROR_MSG

    x = []  # x is the day
    y = []  # y is the total value for the day
    for date, v in datetime_database.iteritems():
        x.append(date)
        y.append(sum(v.itervalues()))

    return x, y
