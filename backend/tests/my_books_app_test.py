from datetime import datetime
import sys
import os
import unittest

from utils.bag import Bag
from utils.gregorian_month_of_year import GregorianMonthOfYear

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.card import Card
from domain.my_books_app import MyBooksApp
from tests.stub.auth_service_stub import AuthServiceStub


class MyBooksAppTest(unittest.TestCase):

    def setUp(self):
        self.user_one = "Dijkstra"
        self.password_one = "O(|E|log|V|)"
        self.user_two = "Turing"
        self.password_two = "M=(Q,Σ,Γ,s,b,F,δ)"
        self.non_existent_user = "Alan Kay"

        self.item_one = "Brand new world"
        self.item_two = "Animal Farm"
        self.catalog = {self.item_one: "π", self.item_two: "e"}

        self.invalid_item = "50 sombras de Grey"

        self.auth = AuthServiceStub.with_users(
            {self.user_one: self.password_one, self.user_two: self.password_two}
        )
        self.app = MyBooksApp.with_catalog_and_auth(self.catalog, self.auth)

        self.valid_card = Card(1234567891234567, GregorianMonthOfYear(11, 2028))
        self.user_creation_date = datetime(2018, 12, 9, 0, 0)
        self.user_action = datetime(2018, 12, 9, 0, 1)
        self.user_expirated_date = datetime(2018, 12, 9, 0, 31)

    def test01_can_create_cart_for_user(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        self.assertTrue(self.app.has_user(self.user_one))

    def test02_user_can_add_items_to_cart(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        self.app.add_book_to_user(self.user_one, self.item_one, 1, self.user_action)
        self.assertTrue(
            self.app.user_has_item(self.user_one, self.item_one, self.user_action)
        )

    def test03_can_create_multiple_carts_and_each_users_add_for_each_cart(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        self.app.add_user(self.user_two, self.password_two, self.user_creation_date)

        self.app.add_book_to_user(self.user_one, self.item_one, 1, self.user_action)
        self.app.add_book_to_user(self.user_two, self.item_two, 1, self.user_action)

        self.assertTrue(
            self.app.user_has_item(self.user_one, self.item_one, self.user_action)
        )
        self.assertTrue(
            self.app.user_has_item(self.user_two, self.item_two, self.user_action)
        )

        self.assertFalse(
            self.app.user_has_item(self.user_one, self.item_two, self.user_action)
        )
        self.assertFalse(
            self.app.user_has_item(self.user_two, self.item_one, self.user_action)
        )

    def test04_can_list_items_from_cart(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        self.app.add_book_to_user(self.user_one, self.item_one, 1, self.user_action)
        self.assertEqual(
            self.app.get_user_shop_list(self.user_one, self.user_action),
            [(self.item_one, 1)],
        )

    def test05_cannot_add_books_for_non_existent_user(self):
        with self.assertRaises(Exception) as context:
            self.app.add_book_to_user(
                self.non_existent_user, self.item_one, 1, self.user_action
            )

        self.assertEqual(
            str(context.exception), MyBooksApp.user_doesnot_exist_message_error()
        )

    def test06_cannot_check_items_for_non_existent_user(self):
        with self.assertRaises(Exception) as context:
            self.app.user_has_item(
                self.non_existent_user, self.item_one, self.user_action
            )

        self.assertEqual(
            str(context.exception), MyBooksApp.user_doesnot_exist_message_error()
        )

    def test07_can_add_multiple_items_to_cart(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        self.app.add_book_to_user(self.user_one, self.item_one, 2, self.user_action)
        self.assertEqual(
            self.app.get_user_shop_list(self.user_one, self.user_action),
            [(self.item_one, 2)],
        )

    def test08_user_session_is_expired_when_list_cart(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        with self.assertRaises(Exception) as ctx:
            self.app.get_user_shop_list(self.user_one, self.user_expirated_date)

        self.assertEqual(
            str(ctx.exception), MyBooksApp.user_expired_session_message_error()
        )

    def test09_user_session_is_not_expired_when_list_cart(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        self.app.get_user_shop_list(self.user_one, self.user_action)

    def test10_user_session_is_expired_when_try_add_item_in_cart(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        self.app.add_book_to_user(self.user_one, self.item_one, 1, self.user_action)

        with self.assertRaises(Exception) as ctx:
            self.app.add_book_to_user(
                self.user_one, self.item_one, 1, self.user_expirated_date
            )

        self.assertEqual(
            str(ctx.exception), MyBooksApp.user_expired_session_message_error()
        )

    def test11_user_session_is_expired_when_try_add_item_in_cart(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        self.app.add_book_to_user(self.user_one, self.item_one, 1, self.user_action)

        with self.assertRaises(Exception) as ctx:
            self.app.checkout(self.user_one, self.valid_card, self.user_expirated_date)

        self.assertEqual(
            str(ctx.exception), MyBooksApp.user_expired_session_message_error()
        )

    def test12_new_user_shows_empty_buy_history(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        self.assertEqual(self.app.user_shop_history(self.user_one), [])

    def test13_after_shopping_two_times_the_user_has_shopping_history(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        self.app.add_book_to_user(self.user_one, self.item_one, 1, self.user_action)
        self.app.checkout(self.user_one, self.valid_card, self.user_action)

        self.app.add_book_to_user(self.user_one, self.item_two, 1, self.user_action)
        self.app.checkout(self.user_one, self.valid_card, self.user_action)

        history = Bag()
        history.add_with_amount(self.item_one, 1)
        history.add_with_amount(self.item_two, 1)
        list_items = history.list_items()

        self.assertEqual(self.app.user_shop_history(self.user_one), list_items)

    def test14_shopping_the_same_book_counts_in_a_single_registration(self):
        self.app.add_user(self.user_one, self.password_one, self.user_creation_date)
        self.app.add_book_to_user(self.user_one, self.item_one, 1, self.user_action)
        self.app.checkout(self.user_one, self.valid_card, self.user_action)

        self.app.add_book_to_user(self.user_one, self.item_one, 4, self.user_action)
        self.app.checkout(self.user_one, self.valid_card, self.user_action)

        history = Bag()
        history.add_with_amount(self.item_one, 5)
        list_items = history.list_items()

        self.assertEqual(self.app.user_shop_history(self.user_one), list_items)


if __name__ == "__main__":
    unittest.main()
