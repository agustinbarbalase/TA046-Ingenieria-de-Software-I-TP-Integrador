import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.checkout import Checkout
from domain.shop_cart import ShopCart


class CheckOutTest(unittest.TestCase):

    def test_checkout_with_empty_cart(self):
        card_number = "0101010101010101"
        card_expiration_date = "112028"
        card_code = "420"

        cart = ShopCart()
        check_out = Checkout()

        with self.assertRaises(Exception) as context:
            check_out.check_out(
                cart,
                {
                    "card_number": card_number,
                    "card_expiration_date": card_expiration_date,
                    "card_code": card_code,
                },
            )

        print(context.exception)
        self.assertEqual(str(context.exception), Checkout.empty_cart_message_error())

    def test_invalid_date(self):
        card_number = "0101010101010101"
        invalid_card_expiration_date = "142024"
        card_code = "420"

        cart = ShopCart()
        check_out = Checkout()

        with self.assertRaises(Exception) as context:
            check_out.check_out(
                cart,
                {
                    "card_number": card_number,
                    "card_expiration_date": invalid_card_expiration_date,
                    "card_code": card_code,
                },
            )

        self.assertEqual(str(context.exception), Checkout.invalid_date_message_error())

    def test_checkout_with_expired_card(self):
        card_number = "0101010101010101"
        invalid_card_expiration_date = "112020"
        card_code = "420"

        cart = ShopCart()
        check_out = Checkout()

        with self.assertRaises(Exception) as context:
            check_out.check_out(
                cart,
                {
                    "card_number": card_number,
                    "card_expiration_date": invalid_card_expiration_date,
                    "card_code": card_code,
                },
            )

        self.assertEqual(str(context.exception), Checkout.expired_card_message_error())
