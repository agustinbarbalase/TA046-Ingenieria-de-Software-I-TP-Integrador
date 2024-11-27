import sys
import os
import unittest

from domain.shop_cart import ShopCart

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ShoppingHistoryTest(unittest.TestCase):

    def setUp(self):

        self.user_one = "Dijkstra"
        self.user_two = "Netwon"

        self.book_isbn_one = "9780387862545"
        self.book_isbn_two = "9780387862546"
        self.catalog = {self.book_isbn_one: "3.14", self.book_isbn_two: "2.71"}

        self.cart = ShopCart.with_catalog(self.catalog)

    def test01(self):
        pass
