import sys
import os
import unittest

from domain.shop_cart import ShopCart
from domain.shopping_history_book import ShopingHistoryBook

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ShoppingHistoryTest(unittest.TestCase):

    def setUp(self):

        self.user_one = "Dijkstra"
        self.user_two = "Netwon"

        self.book_isbn_one = "9780387862545"
        self.book_isbn_two = "9780387862546"
        self.catalog = {self.book_isbn_one: "3.14", self.book_isbn_two: "2.71"}

        self.cart_one = ShopCart.with_catalog(self.catalog)
        self.cart_two = ShopCart.with_catalog(self.catalog)

        self.cart_one.add_item(self.book_isbn_one, 1)
        self.cart_two.add_item(self.book_isbn_two, 1)

        self.shopping_history_book = ShopingHistoryBook.new()

    def test01(self):
        with self.assertRaises(Exception) as ctx:
            self.shopping_history_book.user_shopping_history(self.user_one)

        self.assertEqual(
            str(ctx.exception), ShopingHistoryBook.invalid_user_message_error()
        )

    def test02(self):
        self.shopping_history_book.register_purcharse(self.user_one, self.cart_one)
        self.shopping_history_book.register_purcharse(self.user_one, self.cart_one)

        user_shopping_history = self.shopping_history_book.user_shopping_history(
            self.user_one
        )

        self.assertEqual(
            user_shopping_history.history(),
            (
                6.28,
                [(self.book_isbn_one, 2)],
            ),
        )

    def test03(self):
        self.shopping_history_book.register_purcharse(self.user_one, self.cart_one)
        self.shopping_history_book.register_purcharse(self.user_one, self.cart_one)

        self.shopping_history_book.register_purcharse(self.user_two, self.cart_two)
        self.shopping_history_book.register_purcharse(self.user_two, self.cart_two)

        user_shopping_history_one = self.shopping_history_book.user_shopping_history(
            self.user_one
        )

        user_shopping_history_two = self.shopping_history_book.user_shopping_history(
            self.user_two
        )

        self.assertEqual(
            user_shopping_history_one.history(),
            (
                6.28,
                [(self.book_isbn_one, 2)],
            ),
        )

        self.assertEqual(
            user_shopping_history_two.history(),
            (
                5.42,
                [(self.book_isbn_two, 2)],
            ),
        )
