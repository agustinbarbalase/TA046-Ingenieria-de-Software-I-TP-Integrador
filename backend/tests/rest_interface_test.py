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

    def test01_create_cart_success(self):
        params = {"userId": self.user_id, "password": self.password}
        response = self.rest_interface.create_cart(params)

        self.assertEqual(response.body, "0|OK")
        self.assertEqual(response.status_code, 200)

    def test02_list_empty_cart(self):
        params_for_create_cart = {"userId": self.user_id, "password": self.password}
        params_for_list_cart = {"userId": self.user_id}

        self.rest_interface.create_cart(params_for_create_cart)
        response = self.rest_interface.list_cart(params_for_list_cart)

        self.assertEqual(response.body, "0|")
        self.assertEqual(response.status_code, 200)

    def test03_add_book_to_cart(self):
        params_for_create_cart = {"userId": self.user_id, "password": self.password}
        params_for_add_to_cart = {
            "userId": self.user_id,
            "isbn": self.isbn,
            "amount": "1",
        }
        params_for_list_cart = {"userId": self.user_id}

        self.rest_interface.create_cart(params_for_create_cart)
        self.rest_interface.add_to_cart(params_for_add_to_cart)
        response = self.rest_interface.list_cart(params_for_list_cart)

        self.assertEqual(response.body, f"0|{self.isbn}|1")
        self.assertEqual(response.status_code, 200)

    def test04_try_list_not_created_cart_raise_error(self):
        params_for_list_cart = {"userId": self.user_id}
        response = self.rest_interface.list_cart(params_for_list_cart)

        self.assertEqual(
            response.body,
            f"1|{MyBooksApp.user_doesnot_exist_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)

    def test05_can_add_book_multiple_times_with_amount(self):
        params_for_create_cart = {"userId": self.user_id, "password": self.password}
        params_for_add_to_cart = {
            "userId": self.user_id,
            "isbn": self.isbn,
            "amount": "2",
        }
        params_for_list_cart = {"userId": self.user_id}

        self.rest_interface.create_cart(params_for_create_cart)
        self.rest_interface.add_to_cart(params_for_add_to_cart)
        response = self.rest_interface.list_cart(params_for_list_cart)

        self.assertEqual(response.body, f"0|{self.isbn}|2")
        self.assertEqual(response.status_code, 200)

    def test06_cant_add_non_positive_amount_of_books(self):
        params_for_create_cart = {"userId": self.user_id, "password": self.password}
        params_for_add_to_cart = {
            "userId": self.user_id,
            "isbn": self.isbn,
            "amount": "0",
        }
        params_for_list_cart = {"userId": self.user_id}

        self.rest_interface.create_cart(params_for_create_cart)
        response = self.rest_interface.add_to_cart(params_for_add_to_cart)

        self.assertEqual(
            response.body,
            f"1|{MyBooksApp.cant_add_non_positive_amount_of_books_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)
        self.assertEqual(self.rest_interface.list_cart(params_for_list_cart).body, "0|")

    def test07_validate_empty_params_in_create_cart(self):
        params_for_create_cart = {"userId": "", "password": ""}

        response = self.rest_interface.create_cart(params_for_create_cart)

        self.assertEqual(
            response.body,
            f"1|{RestInterface.cant_send_empty_params_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)

    def test08_validate_empty_params_in_list_cart(self):
        params_for_list_cart = {"userId": ""}

        response = self.rest_interface.list_cart(params_for_list_cart)

        self.assertEqual(
            response.body,
            f"1|{RestInterface.cant_send_empty_params_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)

    def test09_validate_empty_params_in_add_to_cart(self):
        params_for_add_to_cart = {
            "userId": "",
            "isbn": "",
            "amount": "",
        }

        response = self.rest_interface.add_to_cart(params_for_add_to_cart)

        self.assertEqual(
            response.body,
            f"1|{RestInterface.cant_send_empty_params_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
