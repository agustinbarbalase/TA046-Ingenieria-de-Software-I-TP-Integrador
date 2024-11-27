import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.card import Card
from tests.stub.postnet_stub import PostnetStub
from utils.gregorian_month_of_year import GregorianMonthOfYear


class PostNetTest(unittest.TestCase):
    """setup"""

    def setUp(self):
        self.valid_gregorian_month_of_year = GregorianMonthOfYear.with_month_and_year(
            11, 2028
        )

        self.valid_card = Card.with_number_and_month_of_year(
            1234567891234567, self.valid_gregorian_month_of_year
        )
        self.invalid_card = Card.with_number_and_month_of_year(
            6969696969696969, self.valid_gregorian_month_of_year
        )

        self.postnet = PostnetStub.new()

    """tests"""

    def test01_valid_card_created_valid_ticket_id(self):
        self.assertEqual(self.postnet.return_ticket(self.valid_card, 1000), "1234")

    def test02_invalid_card_raise_error(self):
        with self.assertRaises(Exception) as context:
            self.postnet.return_ticket(self.invalid_card, 1000)

        self.assertEqual(
            str(context.exception), PostnetStub.reject_card_message_error()
        )
