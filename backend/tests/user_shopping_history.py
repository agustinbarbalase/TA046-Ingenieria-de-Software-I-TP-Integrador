import sys
import os
import unittest

from domain.shop_cart import ShopCart
from domain.user_shopping_history import UserShoppingHistory

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ShoppingHistoryTest(unittest.TestCase):
    """setup"""

    def setUp(self):

        self.book_isbn_one = "9780387862545"
        self.book_isbn_two = "9780387862546"
        self.catalog = {self.book_isbn_one: "3.14", self.book_isbn_two: "2.71"}

        self.cart_one = ShopCart.with_catalog(self.catalog)
        self.cart_two = ShopCart.with_catalog(self.catalog)

        self.user_shopping_history = UserShoppingHistory.new()

    """tests"""

    def test01_a_recent_created_user_shopping_history_is_empty(self):
        self.assertEqual(self.user_shopping_history.history(), (0, []))

    def test02_for_see_history_needs_two_purcharse(self):

        self.cart_one.add_item(self.book_isbn_one, 2)
        self.cart_two.add_item(self.book_isbn_one, 1)
        self.cart_two.add_item(self.book_isbn_two, 1)

        self.user_shopping_history.register_purcharse_for_user(self.cart_one)
        self.user_shopping_history.register_purcharse_for_user(self.cart_two)

        self.assertEqual(
            self.user_shopping_history.history(),
            (
                12.13,
                [(self.book_isbn_one, 3), (self.book_isbn_two, 1)],
            ),
        )
