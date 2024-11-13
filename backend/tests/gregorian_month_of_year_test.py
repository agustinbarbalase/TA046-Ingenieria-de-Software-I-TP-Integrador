import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.gregorian_month_of_year import GregorianMonthOfYear


class GregorianMonthOfYearTest(unittest.TestCase):

    def test_initialize_with_invalid_month(self):
        with self.assertRaises(Exception) as context:
            GregorianMonthOfYear.initialize_with_month_and_year(13, 2023)
        self.assertEqual(
            str(context.exception), GregorianMonthOfYear.invalid_month_error()
        )

    def test_is_greater_than_today(self):
        future_instance = GregorianMonthOfYear(5, 2023)
        self.assertFalse(future_instance.is_greater_than_today())

    def test_is_not_greater_than_today(self):
        future_instance = GregorianMonthOfYear(5, 2028)
        self.assertTrue(future_instance.is_greater_than_today())
