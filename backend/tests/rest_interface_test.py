import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.domain.rest_interface import RestInterface, BODY
from backend.domain.my_books_app import MyBooksApp


class RestInterfaceTest(unittest.TestCase):

    def test_create_cart_success(self):

        a_rest_interface = RestInterface()

        response = a_rest_interface.create_cart("1", "12345")

        self.assertEqual(response[BODY], "0|OK")

    def test_list_empty_cart(self):

        a_rest_interface = RestInterface()
        a_rest_interface.create_cart("1", "12345")

        self.assertEqual(a_rest_interface.list_cart("1")["body"], "0|")

    def test_add_book_to_cart(self):
        a_rest_interface = RestInterface()

        a_rest_interface.create_cart("1", "12345")

        a_rest_interface.add_to_cart("1", "1", 1)

        self.assertEqual(a_rest_interface.list_cart("1")["body"], "0|1|1")

    def test_try_list_not_created_cart_raise_error(self):
        a_rest_interface = RestInterface()

        self.assertEqual(
            a_rest_interface.list_cart("1")["body"],
            f"1|{MyBooksApp.user_doesnot_exist_message_error().upper()}",
        )

    def test_can_add_book_multiple_times_with_amount(self):
        a_rest_interface = RestInterface()

        a_rest_interface.create_cart("1", "12345")

        a_rest_interface.add_to_cart("1", "1", 2)

        self.assertEqual(a_rest_interface.list_cart("1")["body"], "0|1|2")

    def test_cant_add_non_positive_amount_of_books(self):
        a_rest_interface = RestInterface()

        a_rest_interface.create_cart("1", "12345")

        self.assertEqual(
            a_rest_interface.add_to_cart("1", "1", 0)["body"],
            f"1|{MyBooksApp.cant_add_non_positive_amount_of_books_message_error().upper()}",
        )
        self.assertEqual(a_rest_interface.list_cart("1")["body"], "0|")


if __name__ == "__main__":
    unittest.main()
