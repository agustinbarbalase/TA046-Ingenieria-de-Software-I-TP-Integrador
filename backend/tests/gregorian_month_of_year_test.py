import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.gregorian_month_of_year import GregorianMonthOfYear


class GregorianMonthOfYearTest(unittest.TestCase):

    def test_initialize_with_valid_month_and_year(self):
        instance = GregorianMonthOfYear(5, 2023)
        self.assertEqual(instance.month, 5)
        self.assertEqual(instance.year, 2023)

    def test_initialize_with_invalid_month(self):
        with self.assertRaises(Exception) as context:
            GregorianMonthOfYear(13, 2023)
        self.assertEqual(
            str(context.exception), GregorianMonthOfYear.invalid_month_error()
        )

    def test_is_greater_than_today(self):
        future_instance = GregorianMonthOfYear(5, 2023)
        today = GregorianMonthOfYear.current_month_of_year()

        self.assertFalse(today <= future_instance)

    def test_is_not_greater_than_today(self):
        future_instance = GregorianMonthOfYear(5, 2028)
        today = GregorianMonthOfYear.current_month_of_year()

        self.assertTrue(today <= future_instance)


if __name__ == "__main__":
    unittest.main()
