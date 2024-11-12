import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.checkout import Checkout
from domain.shop_cart import ShopCart


class CheckOutTest(unittest.TestCase):

    def setUp(self):
        self.card_number = "0101010101010101"
        self.card_expiration_date = "112028"
        self.card_code = "420"

        self.invalid_card_expiration_date = "142024"
        self.card_expirated_date = "112020"

        self.empty_cart = ShopCart()
        self.fully_cart = ShopCart()
        self.fully_cart.add_item("The Lord of the rings", 1)

        self.check_out = Checkout()

    def test_checkout_with_empty_cart(self):
        with self.assertRaises(Exception) as context:
            self.check_out.check_out(
                self.empty_cart,
                {
                    "card_number": self.card_number,
                    "card_expiration_date": self.card_expiration_date,
                    "card_code": self.card_code,
                },
            )

        self.assertEqual(str(context.exception), Checkout.empty_cart_message_error())

    def test_invalid_date(self):
        with self.assertRaises(Exception) as context:
            self.check_out.check_out(
                self.fully_cart,
                {
                    "card_number": self.card_number,
                    "card_expiration_date": self.invalid_card_expiration_date,
                    "card_code": self.card_code,
                },
            )

        self.assertEqual(str(context.exception), Checkout.invalid_date_message_error())

    def test_checkout_with_expired_card(self):
        with self.assertRaises(Exception) as context:
            self.check_out.check_out(
                self.fully_cart,
                {
                    "card_number": self.card_number,
                    "card_expiration_date": self.card_expirated_date,
                    "card_code": self.card_code,
                },
            )

        self.assertEqual(str(context.exception), Checkout.expired_card_message_error())

    def test_checkout_sucessfully(self):
        pass
