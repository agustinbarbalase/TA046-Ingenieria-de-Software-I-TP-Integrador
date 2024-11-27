from datetime import datetime
import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.rest_interface import RestInterface
from domain.my_books_app import MyBooksApp
from tests.stub.auth_service_stub import AuthServiceStub


class RestInterfaceTest(unittest.TestCase):
    """setup"""

    def setUp(self):
        self.user_id = "Gauss"
        self.password = "30-04-1777"

        self.book_isbn_one = "9780387862545"
        self.book_isbn_two = "9780387862546"
        self.catalog = {self.book_isbn_one: "π", self.book_isbn_two: "e"}

        self.auth = AuthServiceStub.with_users({self.user_id: self.password})
        self.app = MyBooksApp.with_catalog_and_auth(self.catalog, self.auth)

        self.rest_interface = RestInterface.with_app(self.app)

        self.user_creation_date = datetime(2018, 12, 9, 0, 0)
        self.user_action = datetime(2018, 12, 9, 0, 1)
        self.user_expirated_date = datetime(2018, 12, 9, 0, 31)

    """tests - main protocol"""

    def test01_create_cart_success(self):
        params = {"userId": self.user_id, "password": self.password}
        response = self.rest_interface.create_cart(params, self.user_creation_date)

        self.assertEqual(response.body, "0|OK")
        self.assertEqual(response.status_code, 200)

    def test02_list_empty_cart(self):
        params_for_create_cart = {"userId": self.user_id, "password": self.password}
        params_for_list_cart = {"userId": self.user_id}

        self.rest_interface.create_cart(params_for_create_cart, self.user_creation_date)
        response = self.rest_interface.list_cart(params_for_list_cart, self.user_action)

        self.assertEqual(response.body, "0|")
        self.assertEqual(response.status_code, 200)

    def test03_add_book_to_cart(self):
        params_for_create_cart = {"userId": self.user_id, "password": self.password}
        params_for_add_to_cart = {
            "userId": self.user_id,
            "bookIsbn": self.book_isbn_one,
            "bookQuantity": "1",
        }
        params_for_list_cart = {"userId": self.user_id}

        self.rest_interface.create_cart(params_for_create_cart, self.user_creation_date)
        self.rest_interface.add_to_cart(params_for_add_to_cart, self.user_action)
        response = self.rest_interface.list_cart(params_for_list_cart, self.user_action)

        self.assertEqual(response.body, f"0|{self.book_isbn_one}|1")
        self.assertEqual(response.status_code, 200)

    def test04_try_list_not_created_cart_raise_error(self):
        params_for_list_cart = {"userId": self.user_id}
        response = self.rest_interface.list_cart(params_for_list_cart, self.user_action)

        self.assertEqual(
            response.body,
            f"1|{MyBooksApp.user_doesnot_exist_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)

    def test05_can_add_book_multiple_times_with_bookQuantity(self):
        params_for_create_cart = {"userId": self.user_id, "password": self.password}
        params_for_add_to_cart = {
            "userId": self.user_id,
            "bookIsbn": self.book_isbn_one,
            "bookQuantity": "2",
        }
        params_for_list_cart = {"userId": self.user_id}

        self.rest_interface.create_cart(params_for_create_cart, self.user_creation_date)
        self.rest_interface.add_to_cart(params_for_add_to_cart, self.user_action)
        response = self.rest_interface.list_cart(params_for_list_cart, self.user_action)

        self.assertEqual(response.body, f"0|{self.book_isbn_one}|2")
        self.assertEqual(response.status_code, 200)

    def test06_cant_add_non_positive_bookQuantity_of_books(self):
        params_for_create_cart = {"userId": self.user_id, "password": self.password}
        params_for_add_to_cart = {
            "userId": self.user_id,
            "bookIsbn": self.book_isbn_one,
            "bookQuantity": "0",
        }
        params_for_list_cart = {"userId": self.user_id}

        self.rest_interface.create_cart(params_for_create_cart, self.user_creation_date)
        response = self.rest_interface.add_to_cart(
            params_for_add_to_cart, self.user_action
        )

        self.assertEqual(
            response.body,
            f"1|{MyBooksApp.cant_add_non_positive_amount_of_books_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)
        self.assertEqual(
            self.rest_interface.list_cart(params_for_list_cart, self.user_action).body,
            "0|",
        )

    """tests - validation"""

    def test07_validate_empty_params_in_create_cart(self):
        params_for_create_cart = {"userId": "", "password": ""}

        response = self.rest_interface.create_cart(
            params_for_create_cart, self.user_creation_date
        )

        self.assertEqual(
            response.body,
            f"1|{RestInterface.cant_send_empty_params_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)

    def test08_validate_empty_params_in_list_cart(self):
        params_for_list_cart = {"userId": ""}

        response = self.rest_interface.list_cart(params_for_list_cart, self.user_action)

        self.assertEqual(
            response.body,
            f"1|{RestInterface.cant_send_empty_params_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)

    def test09_validate_empty_params_in_add_to_cart(self):
        params_for_add_to_cart = {
            "userId": "",
            "bookIsbn": "",
            "bookQuantity": "",
        }

        response = self.rest_interface.add_to_cart(
            params_for_add_to_cart, self.user_action
        )

        self.assertEqual(
            response.body,
            f"1|{RestInterface.cant_send_empty_params_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)

    def test10_validate_abstent_params_in_create_cart(self):
        params_for_create_cart = {"userId": ""}

        response = self.rest_interface.create_cart(
            params_for_create_cart, self.user_creation_date
        )

        self.assertEqual(
            response.body,
            f"1|{RestInterface.cant_send_request_with_abstent_params_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)

    def test11_validate_abstent_params_in_list_cart(self):
        params_for_list_cart: dict[str, str] = {}

        response = self.rest_interface.list_cart(params_for_list_cart, self.user_action)

        self.assertEqual(
            response.body,
            f"1|{RestInterface.cant_send_request_with_abstent_params_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)

    def test12_validate_abstent_params_in_add_to_cart(self):
        params_for_add_to_cart = {
            "userId": "",
            "bookQuantity": "",
        }

        response = self.rest_interface.add_to_cart(
            params_for_add_to_cart, self.user_action
        )

        self.assertEqual(
            response.body,
            f"1|{RestInterface.cant_send_request_with_abstent_params_message_error().upper()}",
        )
        self.assertEqual(response.status_code, 422)

    """tests - checkout"""

    def test13_user_successfull_checkout(self):
        create_card_params = {"userId": self.user_id, "password": self.password}
        self.rest_interface.create_cart(create_card_params, self.user_creation_date)
        params_for_add_to_cart = {
            "userId": self.user_id,
            "bookIsbn": self.book_isbn_one,
            "bookQuantity": "1",
        }

        self.rest_interface.add_to_cart(params_for_add_to_cart, self.user_action)
        card_number = "1234567890123456"
        card_expiry = "122025"
        card_name = self.user_id

        check_out_params = {
            "userId": self.user_id,
            "ccn": card_number,
            "cced": card_expiry,
            "cco": card_name,
        }

        response = self.rest_interface.checkout(check_out_params, self.user_action)

        self.assertEqual(response.body, "0|1234")

    def test14_checkout_using_invalid_card_number(self):
        create_card_params = {"userId": self.user_id, "password": self.password}
        self.rest_interface.create_cart(create_card_params, self.user_creation_date)
        params_for_add_to_cart = {
            "userId": self.user_id,
            "bookIsbn": self.book_isbn_one,
            "bookQuantity": "1",
        }

        self.rest_interface.add_to_cart(params_for_add_to_cart, self.user_action)
        card_number = "123456789012346"
        card_expiry = "122025"
        card_name = self.user_id

        check_out_params = {
            "userId": self.user_id,
            "ccn": card_number,
            "cced": card_expiry,
            "cco": card_name,
        }

        response = self.rest_interface.checkout(check_out_params, self.user_action)

        self.assertEqual(response.body, "1|CARD WITH INVALID NUMBER CAN NOT BE CREATED")

    def test15_checkout_using_expired_card(self):
        create_card_params = {"userId": self.user_id, "password": self.password}
        self.rest_interface.create_cart(create_card_params, self.user_creation_date)
        params_for_add_to_cart = {
            "userId": self.user_id,
            "bookIsbn": self.book_isbn_one,
            "bookQuantity": "1",
        }

        self.rest_interface.add_to_cart(params_for_add_to_cart, self.user_action)
        card_number = "1234567890123461"
        card_expiry = "122023"
        card_name = self.user_id

        check_out_params = {
            "userId": self.user_id,
            "ccn": card_number,
            "cced": card_expiry,
            "cco": card_name,
        }

        response = self.rest_interface.checkout(check_out_params, self.user_action)

        self.assertEqual(response.body, "1|EXPIRED CARD")

    def test16_checkout_with_empty_card(self):
        create_card_params = {"userId": self.user_id, "password": self.password}
        self.rest_interface.create_cart(create_card_params, self.user_creation_date)

        card_number = "1234567890123461"
        card_expiry = "122025"
        card_name = self.user_id

        check_out_params = {
            "userId": self.user_id,
            "ccn": card_number,
            "cced": card_expiry,
            "cco": card_name,
        }

        response = self.rest_interface.checkout(check_out_params, self.user_action)

        self.assertEqual(response.body, "1|EMPTY CART")

    def test17_checkout_empty_card_name(self):
        create_card_params = {"userId": self.user_id, "password": self.password}
        self.rest_interface.create_cart(create_card_params, self.user_creation_date)
        params_for_add_to_cart = {
            "userId": self.user_id,
            "bookIsbn": self.book_isbn_one,
            "bookQuantity": "1",
        }

        self.rest_interface.add_to_cart(params_for_add_to_cart, self.user_action)
        card_number = "1234567890123456"
        card_expiry = "122025"
        card_name = ""

        check_out_params = {
            "userId": self.user_id,
            "ccn": card_number,
            "cced": card_expiry,
            "cco": card_name,
        }

        response = self.rest_interface.checkout(check_out_params, self.user_action)

        self.assertEqual(response.body, "1|CAN'T SEND EMPTY PARAMS")

    def test18_misssing_parameter_checking_out(self):
        create_card_params = {"userId": self.user_id, "password": self.password}
        self.rest_interface.create_cart(create_card_params, self.user_creation_date)
        params_for_add_to_cart = {
            "userId": self.user_id,
            "bookIsbn": self.book_isbn_one,
            "bookQuantity": "1",
        }

        self.rest_interface.add_to_cart(params_for_add_to_cart, self.user_action)
        card_number = "1234567890123456"
        card_expiry = "122025"
        card_name = self.user_id

        check_out_params = {
            "userId": self.user_id,
            "ccn": card_number,
            "cced": card_expiry,
        }

        response = self.rest_interface.checkout(check_out_params, self.user_action)

        self.assertEqual(response.body, "1|CAN'T SENT REQUEST WITH ABSTENT PARAMS")

    """tests - user history"""

    # def test19_shop_cart_list(self):
    #     create_card_params = {"userId": self.user_id, "password": self.password}
    #     self.rest_interface.create_cart(create_card_params, self.user_creation_date)
    #     params_for_add_to_cart = {
    #         "userId": self.user_id,
    #         "bookIsbn": self.book_isbn_one,
    #         "bookQuantity": "1",
    #     }

    #     self.rest_interface.add_to_cart(params_for_add_to_cart, self.user_action)
    #     card_number = "1234567890123456"
    #     card_expiry = "122025"
    #     card_name = self.user_id

    #     check_out_params = {
    #         "userId": self.user_id,
    #         "ccn": card_number,
    #         "cced": card_expiry,
    #         "cco": card_name,
    #     }

    #     response = self.rest_interface.checkout(check_out_params, self.user_action)

    #     self.rest_interface.create_cart(create_card_params, self.user_creation_date)
    #     params_for_add_to_cart = {
    #         "userId": self.user_id,
    #         "bookIsbn": self.book_isbn_two,
    #         "bookQuantity": "1",
    #     }

    #     self.rest_interface.add_to_cart(params_for_add_to_cart, self.user_action)
    #     card_number = "1234567890123456"
    #     card_expiry = "122025"
    #     card_name = self.user_id

    #     check_out_params = {
    #         "userId": self.user_id,
    #         "ccn": card_number,
    #         "cced": card_expiry,
    #         "cco": card_name,
    #     }

    #     response = self.rest_interface.checkout(check_out_params, self.user_action)

    #     response = self.rest_interface.user_shop_history(
    #         {"userId": self.user_id, "password": self.password}
    #     )

    #     self.assertEqual(
    #         response.body, f"0|{self.book_isbn_one}|{1}|{self.book_isbn_two}|{1}"
    #     )


if __name__ == "__main__":
    unittest.main()
