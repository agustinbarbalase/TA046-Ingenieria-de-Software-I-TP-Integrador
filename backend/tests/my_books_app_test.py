from time import sleep
import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.my_books_app import MyBooksApp


class MyBooksAppTest(unittest.TestCase):

    def setUp(self):
        self.user_one = "Dijkstra"
        self.user_two = "Turing"
        self.non_existent_user = "Alan Kay"

        self.item_one = "Brand new world"
        self.item_two = "Animal Farm"
        self.catalog = set([self.item_one, self.item_two])

        self.invalid_item = "50 sombras de Grey"

        self.app = MyBooksApp(self.catalog)

    def test01_can_create_cart_for_user(self):
        self.app.add_user(self.user_one, "")
        self.assertTrue(self.app.has_user(self.user_one))

    def test02_user_can_add_items_to_cart(self):
        self.app.add_user(self.user_one, "")
        self.app.add_book_to_user(self.user_one, self.item_one, 1)
        self.assertTrue(self.app.user_has_item(self.user_one, self.item_one))

    def test03_can_create_multiple_carts_and_each_users_add_for_each_cart(self):
        self.app.add_user(self.user_one, "")
        self.app.add_user(self.user_two, "")

        self.app.add_book_to_user(self.user_one, self.item_one, 1)
        self.app.add_book_to_user(self.user_two, self.item_two, 1)

        self.assertTrue(self.app.user_has_item(self.user_one, self.item_one))
        self.assertTrue(self.app.user_has_item(self.user_two, self.item_two))

        self.assertFalse(self.app.user_has_item(self.user_one, self.item_two))
        self.assertFalse(self.app.user_has_item(self.user_two, self.item_one))

    def test04_can_list_items_from_cart(self):
        self.app.add_user(self.user_one, "")
        self.app.add_book_to_user(self.user_one, self.item_one, 1)
        self.assertEqual(
            self.app.get_user_shop_list(self.user_one), [(self.item_one, 1)]
        )

    def test05_cannot_add_books_for_non_existent_user(self):
        with self.assertRaises(Exception) as context:
            self.app.add_book_to_user(self.non_existent_user, self.item_one, 1)

        self.assertEqual(
            str(context.exception), MyBooksApp.user_doesnot_exist_message_error()
        )

    def test06_cannot_check_items_for_non_existent_user(self):
        with self.assertRaises(Exception) as context:
            self.app.user_has_item(self.non_existent_user, self.item_one)

        self.assertEqual(
            str(context.exception), MyBooksApp.user_doesnot_exist_message_error()
        )

    def test07_can_add_multiple_items_to_cart(self):
        self.app.add_user(self.user_one, "")
        self.app.add_book_to_user(self.user_one, self.item_one, 2)
        self.assertEqual(
            self.app.get_user_shop_list(self.user_one), [(self.item_one, 2)]
        )

    def test08_user_session_is_expired(self):
        self.app.add_user(self.user_one, "")
        sleep(4)
        with self.assertRaises(Exception) as ctx:
            self.app.get_user_shop_list(self.user_one)

        self.assertEqual(
            str(ctx.exception), MyBooksApp.user_expired_session_message_error()
        )

    def test08_user_session_is_not_expired(self):
        self.app.add_user(self.user_one, "")
        sleep(1)
        self.app.get_user_shop_list(self.user_one)


if __name__ == "__main__":
    unittest.main()
