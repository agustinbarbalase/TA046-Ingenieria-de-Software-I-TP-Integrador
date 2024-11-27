from datetime import datetime, timedelta
import sys
import os
import unittest

from utils.clock import Clock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ClockTest(unittest.TestCase):

    def test01_clock_give_me_current_time(self):
        clock = Clock(lambda: datetime(2023, 1, 1, 0, 0), lambda: timedelta(seconds=0))
        self.assertEqual(clock.current(), datetime(2023, 1, 1, 0, 0))

    def test02_clock_give_correct_limit_date(self):
        clock = Clock(lambda: datetime(2023, 1, 1, 0, 0), lambda: timedelta(seconds=10))
        print(clock.limit_date())
        self.assertEqual(clock.limit_date(), datetime(2023, 1, 1, 0, 0, 10))
