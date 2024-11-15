import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.rest_interface import RestInterface
from domain.my_books_app import MyBooksApp


class RestInterfaceTest(unittest.TestCase):

    def setUp(self):
        self.user_id = "Gauss"
        self.password = "30-04-1777"

        self.isbn = "9780387862545"
        self.catalog = set([self.isbn])

        self.app = MyBooksApp(self.catalog)
        self.rest_interface = RestInterface(self.app)

    def test_create_cart_success(self):
        response = self.rest_interface.create_cart(self.user_id, self.password)

        self.assertEqual(response.body, "0|OK")
        self.assertEqual(response.status_code, 200)

    def test_list_empty_cart(self):
        self.rest_interface.create_cart(self.user_id, self.password)
        response = self.rest_interface.list_cart(self.user_id)

        self.assertEqual(response.body, "0|")
        self.assertEqual(response.status_code, 200)

    def test_add_book_to_cart(self):
        self.rest_interface.create_cart(self.user_id, self.password)
        self.rest_interface.add_to_cart(self.user_id, self.isbn, 1)
        response = self.rest_interface.list_cart(self.user_id)

        self.assertEqual(response.body, f"0|{self.isbn}|1")
        self.assertEqual(response.status_code, 200)

    def test_try_list_not_created_cart_raise_error(self):
        response = self.rest_interface.list_cart(self.user_id)

        self.assertEqual(
            response.body,
            f"1|{MyBooksApp.user_doesnot_exist_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)

    def test_can_add_book_multiple_times_with_amount(self):
        self.rest_interface.create_cart(self.user_id, self.password)
        self.rest_interface.add_to_cart(self.user_id, self.isbn, 2)
        response = self.rest_interface.list_cart(self.user_id)

        self.assertEqual(response.body, f"0|{self.isbn}|2")
        self.assertEqual(response.status_code, 200)

    def test_cant_add_non_positive_amount_of_books(self):
        self.rest_interface.create_cart(self.user_id, self.password)
        response = self.rest_interface.add_to_cart(self.user_id, self.isbn, 0)

        self.assertEqual(
            response.body,
            f"1|{MyBooksApp.cant_add_non_positive_amount_of_books_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)
        self.assertEqual(self.rest_interface.list_cart(self.user_id).body, "0|")


if __name__ == "__main__":
    unittest.main()
