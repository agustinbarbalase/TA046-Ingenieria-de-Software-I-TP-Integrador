import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.stub.auth_service_stub import AuthServiceStub
from domain.my_books_app import MyBooksApp


class AuthServiceTest(unittest.TestCase):

    def setUp(self):
        self.user = "Alan Turing"
        self.password = "M=(Q,Σ,Γ,s,b,F,δ)"
        self.invalid_password = "NP⊆P"

        self.invalid_user = "Sigmund Freud"
        self.invalid_user_password = "Edipo"

        self.users = {self.user: self.password}
        self.auth = AuthServiceStub(self.users)

        self.catalog = set(["9781530959334"])
        self.app = MyBooksApp.with_auth(self.catalog, self.auth)

    def test_invalid_user_cannot_create_a_cart(self):
        with self.assertRaises(Exception) as context:
            self.app.add_user(self.invalid_user, self.invalid_user_password)

        self.assertEqual(
            str(context.exception), AuthServiceStub.invalid_user_message_error()
        )

    def test_valid_user_with_invalid_password_cannot_create_a_cart(self):
        with self.assertRaises(Exception) as context:
            self.app.add_user(self.user, self.invalid_password)

        self.assertEqual(
            str(context.exception), AuthServiceStub.invalid_password_message_error()
        )

    def test_valid_user_can_create_and_list_cart(self):
        self.app.add_user(self.user, self.password)
        self.assertEqual(self.app.get_user_shop_list(self.user), [])
