from __future__ import absolute_import, division, print_function

import datetime_database
import unittest


class DatetimeDatabaseTestPerformance(unittest.TestCase):
    def setUp(self):
        self.database = datetime_database.DatetimeDatabase(date=True)
        self.time_database = datetime_database.DatetimeDatabase(time=True)

    def test_performance(self):
        for year in xrange(1600, 2020, 1):
            syear = str(year)
            for month in xrange(1, 13, 1):
                smonth = str(month)
                for day in xrange(1, 28, 1):
                    final_date = str(day) + '/' + smonth + '/' + syear
                    self.database.set(final_date, 1)
        x = self.database.get_after("23/02/1950")
        assert len(
            x) == 22630, "database.get_after is not getting as much values as expected!"

        x = self.database.get_before("23/02/1950")
        assert len(
            x) == 113449, "database.get_before is not getting as much values as expected!"

    # def test_with_time_performance(self):
    #     import time
    #     s1 = time.time()
    #     for year in xrange(2000, 2020, 1):
    #         syear = str(year)
    #         for month in xrange(1, 13, 1):
    #             smonth = str(month)
    #             for day in xrange(1, 28, 1):
    #                 final_date = str(day) + '/' + smonth + '/' + syear
    #                 for hours in range(0, 12, 1):
    #                     shours = str(hours)
    #                     for minutes in range(0, 10, 1):
    #                         sminutes = str(minutes)
    #                         self.time_database.set(shours + ':' + sminutes, 10)

    #                 self.database.set(final_date, self.time_database)
    #                 # clear database
    #                 self.time_database = datetime_database.DatetimeDatabase(
    #                     time=True)
    #     e1 = time.time()

    #     s2 = time.time()
    #     x = self.database.get_after("23/02/2010")
    #     e2 = time.time()
    #     s3 = time.time()
    #     y = self.database.get_before("23/02/2010")
    #     e3 = time.time()
    #     assert len(
    # x) == 22630, str(len(self.database)) + " " + str(len(x)) + " " +
    # str(len(y)) + " " + str(e1 - s1) + " " + str(e2 - s2) + " " + str(e3 -
    # s3)


if __name__ == "__main__":
    unittest.main()
