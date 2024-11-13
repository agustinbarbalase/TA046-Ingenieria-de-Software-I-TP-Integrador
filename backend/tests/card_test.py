import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.card import Card
import sys
import os
import unittest
from utils.gregorian_month_of_year import GregorianMonthOfYear


class CardTest(unittest.TestCase):

    def setUp(self):
        self.number = 1234567890123456
        self.month = 12
        self.year = 2025

    def test_cannot_create_expired_card(self):
        expired_month = 1
        expired_year = 2020
        with self.assertRaises(Exception) as context:
            Card.initialize_with_number_and_month_and_year(
                self.number, expired_month, expired_year
            )
        self.assertEqual(
            str(context.exception), Card.cannot_create_expired_card_message()
        )
