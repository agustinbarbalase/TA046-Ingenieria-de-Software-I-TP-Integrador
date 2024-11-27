from datetime import datetime, timedelta
import sys
import os
import unittest

from utils.clock import Clock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ClockTest(unittest.TestCase):
    """setup"""

    def setUp(self):
        # "Time is relative" - Albert Einstein

        self.einstein_birthday = datetime(1879, 3, 14, 0, 0, 0)
        self.einstein_birthday_29_seconds_later = datetime(1879, 3, 14, 0, 0, 29)
        self.einstein_birthday_30_seconds_later = datetime(1879, 3, 14, 0, 0, 30)

    """tests"""

    def test01_step_a_number_of_seconds_give_later_date(self):
        clock = Clock.with_current_time(self.einstein_birthday)

        clock.step_seconds(30)

        self.assertTrue(clock.is_later_that(self.einstein_birthday_29_seconds_later))
        self.assertFalse(clock.is_later_that(self.einstein_birthday_30_seconds_later))

    def test02_step_to_now_then_current_date_is_not_late(self):
        clock = Clock.with_time_now()

        clock.step_to_current_time()

        self.assertFalse(clock.is_later_that(datetime.now()))

    def test03_give_a_date_later(self):
        clock = Clock.with_current_time(self.einstein_birthday)

        later_date = clock.later_date_to_seconds(29)

        self.assertEqual(self.einstein_birthday_29_seconds_later, later_date)
