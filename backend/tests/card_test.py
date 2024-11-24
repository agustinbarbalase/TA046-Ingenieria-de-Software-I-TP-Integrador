import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.card import Card
from utils.gregorian_month_of_year import GregorianMonthOfYear


class CardTest(unittest.TestCase):

    def setUp(self):
        self.valid_number = 1234567890123456
        self.invalid_number = 4302820348032403209402340
        self.valid_month_of_year = GregorianMonthOfYear.with_month_and_year(12, 2028)
        self.expired_month_of_year = GregorianMonthOfYear.with_month_and_year(12, 2023)

    def test01_recently_created_card_is_not_expired(self):
        card = Card.with_number_and_month_of_year(
            self.valid_number, self.valid_month_of_year
        )
        self.assertFalse(card.is_expired(GregorianMonthOfYear.current()))

    def test02_cannot_create_a_expired_card(self):
        expired_card = Card.with_number_and_month_of_year(
            self.valid_number, self.expired_month_of_year
        )
        self.assertTrue(expired_card.is_expired(GregorianMonthOfYear.current()))

    def test03_cannot_create_card_with_invalid_number(self):
        with self.assertRaises(Exception) as context:
            Card.with_number_and_month_of_year(
                self.invalid_number, self.valid_month_of_year
            )

        self.assertEqual(
            str(context.exception),
            Card.cannot_create_card_with_invalid_number_message_error(),
        )
