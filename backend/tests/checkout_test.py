import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.checkout import Checkout
from domain.shop_cart import ShopCart
from tests.stub.postnet_stub import PostNetStub
from utils.card import Card
from utils.gregorian_month_of_year import GregorianMonthOfYear


class CheckOutTest(unittest.TestCase):

    def setUp(self):
        self.valid_card = Card(1234567891234567, GregorianMonthOfYear(11, 2028))
        self.expired_card = Card(1234567891234567, GregorianMonthOfYear(11, 2023))

        self.catalog = set(["The Lord of the rings"])
        self.empty_cart = ShopCart(self.catalog)
        self.fully_cart = ShopCart(self.catalog)
        self.fully_cart.add_item("The Lord of the rings", 1)

        self.xyz = PostNetStub()
        self.check_out = Checkout(self.xyz)

    def test_checkout_with_empty_cart(self):
        with self.assertRaises(Exception) as context:
            self.check_out.check_out(self.empty_cart, self.valid_card)

        self.assertEqual(str(context.exception), Checkout.empty_cart_message_error())

    def test_checkout_with_expired_card(self):
        with self.assertRaises(Exception) as context:
            self.check_out.check_out(self.fully_cart, self.expired_card)

        self.assertEqual(str(context.exception), Checkout.expired_card_message_error())

    def test_checkout_sucessfully(self):
        ticket = self.check_out.check_out(self.fully_cart, self.valid_card)

        self.assertEqual(ticket, "Sucessfully sell")
