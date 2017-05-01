from __future__ import absolute_import, division, print_function

import datetime_database
import unittest


class DatetimeDatabaseTest(unittest.TestCase):
    def setUp(self):
        self.database = datetime_database.DatetimeDatabase(date=True)
        self.time_database = datetime_database.DatetimeDatabase(time=True)

    def test_set_date(self):
        self.database.set("24/03/2015", 1)
        self.database.set("23/03/2015", 1)
        self.database.set("25/03/2015", 1)

        self.assertEqual(len(self.database.dates), 3)

    def test_get_date(self):
        self.database.set("25/03/2015", 1)
        tt = self.database.get("25/03/2015")

        self.assertNotEqual(tt, None)

    def test_get_after_date(self):
        self.database.set("24/03/2015", 1)
        self.database.set("23/03/2015", 1)
        self.database.set("25/03/2015", 1)
        self.database.set("26/03/2015", 1)
        self.assertEqual(len(self.database.get_after("24/03/2015")), 2)
        self.assertEqual(len(self.database.get_after("25/03/2015")), 1)

    def test_get_before_date(self):
        self.database.set("24/03/2015", 1)
        self.database.set("23/03/2015", 1)
        self.database.set("25/03/2015", 1)
        self.database.set("26/03/2015", 1)
        self.assertEqual(len(self.database.get_before("24/03/2015")), 1)
        self.assertEqual(len(self.database.get_before("23/03/2015")), 0)

    def test_set_time(self):
        self.time_database.set("14:30", 1)
        self.time_database.set("16:30", 1)
        self.time_database.set("15:30", 1)

        self.assertEqual(len(self.time_database.dates), 3)

    def test_get_time(self):
        self.time_database.set("19:29", 1)
        tt = self.time_database.get("19:29")

        self.assertNotEqual(tt, None)

    def test_get_after_time(self):
        self.time_database.set("14:30", 1)
        self.time_database.set("13:30", 1)
        self.time_database.set("15:30", 1)
        self.time_database.set("16:30", 1)
        self.assertEqual(len(self.time_database.get_after("14:30")), 2)
        self.assertEqual(len(self.time_database.get_after("15:30")), 1)

    def test_get_before_time(self):
        self.time_database.set("14:30", 1)
        self.time_database.set("13:30", 1)
        self.time_database.set("15:30", 1)
        self.time_database.set("16:30", 1)
        self.assertEqual(len(self.time_database.get_before("14:30")), 1)
        self.assertEqual(len(self.time_database.get_before("13:30")), 0)


if __name__ == "__main__":
    unittest.main()
