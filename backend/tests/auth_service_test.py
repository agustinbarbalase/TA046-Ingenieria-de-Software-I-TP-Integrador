from datetime import datetime, timedelta
import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.my_books_app import MyBooksApp
from domain.shopping_history_book import ShopingHistoryBook
from tests.stub.clock_stub import ClockStub
from tests.stub.auth_service_stub import AuthServiceStub
from tests.stub.postnet_stub import PostnetStub


class AuthServiceTest(unittest.TestCase):
    """setup"""

    def setUp(self):
        self.user = "Alan Turing"
        self.password = "M=(Q,Σ,Γ,s,b,F,δ)"
        self.invalid_password = "NP⊆P"

        self.invalid_user = "Sigmund Freud"
        self.invalid_user_password = "Edipo"

        self.users = {self.user: self.password}
        self.auth = AuthServiceStub.with_users({self.user: self.password})

        self.catalog = {"9781530959334": "π"}
        self.clock = ClockStub.with_current_time(datetime(2023, 1, 1, 0, 0))

        self.user_creation_date = datetime(2018, 12, 9, 0, 0)
        self.user_action = datetime(2018, 12, 9, 0, 1)
        self.user_expirated_date = datetime(2018, 12, 9, 0, 31)

        self.shopping_history = ShopingHistoryBook.new()
        self.postnet = PostnetStub.new()

        self.app = MyBooksApp.with_dependencies(
            self.catalog, self.auth, self.clock, 30, self.shopping_history, self.postnet
        )

    """tests"""

    def test01_invalid_user_cannot_create_a_cart(self):
        with self.assertRaises(Exception) as context:
            self.app.add_user(self.invalid_user, self.invalid_user_password)

        self.assertEqual(
            str(context.exception), AuthServiceStub.invalid_user_message_error()
        )

    def test02_valid_user_with_invalid_password_cannot_create_a_cart(self):
        with self.assertRaises(Exception) as context:
            self.app.add_user(self.user, self.invalid_password)

        self.assertEqual(
            str(context.exception), AuthServiceStub.invalid_password_message_error()
        )

    def test03_valid_user_can_create_and_list_cart(self):
        self.app.add_user(self.user, self.password)
        self.assertEqual(self.app.get_user_shop_list(self.user), [])
