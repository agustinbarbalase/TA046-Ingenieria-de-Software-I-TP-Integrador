import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.cashier import Cashier
from domain.shop_cart import ShopCart
from tests.stub.postnet_stub import PostnetStub
from utils.card import Card
from utils.gregorian_month_of_year import GregorianMonthOfYear


class CheckOutTest(unittest.TestCase):
    """setup"""

    def setUp(self):
        self.user_id = "Einstein"

        self.valid_gregorian_month_of_year = GregorianMonthOfYear.with_month_and_year(
            11, 2028
        )
        self.expired_gregorian_month_of_year = GregorianMonthOfYear.with_month_and_year(
            11, 2023
        )

        self.valid_card = Card.with_number_and_month_of_year(
            1234567891234567, self.valid_gregorian_month_of_year
        )
        self.expired_card = Card.with_number_and_month_of_year(
            1234567891234567, self.expired_gregorian_month_of_year
        )

        self.catalog = {"The Lord of the rings": "3.1415"}
        self.empty_cart = ShopCart.with_catalog(self.catalog)
        self.fully_cart = ShopCart.with_catalog(self.catalog)
        self.fully_cart.add_item("The Lord of the rings", 1)

        self.postnet = PostnetStub()
        self.cashier = Cashier.with_postnet(self.postnet)

    """tests"""

    def test01_checkout_with_empty_cart(self):
        with self.assertRaises(Exception) as context:
            self.cashier.check_out(self.empty_cart, self.valid_card, self.user_id)

        self.assertEqual(str(context.exception), Cashier.empty_cart_message_error())

    def test02_checkout_with_expired_card(self):
        with self.assertRaises(Exception) as context:
            self.cashier.check_out(self.fully_cart, self.expired_card, self.user_id)

        self.assertEqual(str(context.exception), Cashier.expired_card_message_error())

    def test03_checkout_sucessfully(self):
        ticket = self.cashier.check_out(self.fully_cart, self.valid_card, self.user_id)

        self.assertEqual(ticket, "1234")
