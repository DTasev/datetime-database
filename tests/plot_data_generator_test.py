from __future__ import absolute_import, division, print_function

import unittest

import datetime_database
import plot_data_generator as pdg


class PlotDataGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.database = datetime_database.DatetimeDatabase(date=True)
        self.time_database = datetime_database.DatetimeDatabase(time=True)
        self.time_database.set("14:30", 14)
        self.time_database.set("16:30", 14)
        self.time_database.set("15:30", 14)
        self.database.set("24/03/2015", self.time_database)
        self.database.set("23/03/2015", self.time_database)
        self.database.set("25/03/2015", self.time_database)

    def test_plot_daily(self):
        x, y = pdg.generate_daily(self.database)

        self.assertEqual(len(x), 3)
        self.assertEqual(len(y), 3)

        for val in y:
            self.assertEqual(val, 42)

    def test_plot_hourly(self):
        x, y = pdg.generate_hourly("23/03/2015", self.database)
        self.assertEqual(len(x), 3)
        self.assertEqual(len(y), 3)

        for val in y:
            self.assertEqual(val, 14)


if __name__ == "__main__":
    unittest.main()
