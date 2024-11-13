import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.my_books_app import MyBooksApp


class MyBooksAppTest(unittest.TestCase):

    def test01(self):
        user = "Dijkstra"
        my_app = MyBooksApp()
        my_app.add_user(user)
        self.assertTrue(my_app.has_user(user))

    def test02(self):
        my_app = MyBooksApp()
        user = "Dijkstra"
        my_app.add_user(user)
        item = "Brand new world"

        my_app.add_book_to_user(user, item, 1)

        self.assertTrue(my_app.user_has_item(user, item))

    def test03(self):
        my_app = MyBooksApp()
        user1 = "Dijkstra"
        my_app.add_user(user1)
        user2 = "Turing"
        my_app.add_user(user2)

        item1 = "Brand new world"
        item2 = "animal farm"
        my_app.add_book_to_user(user1, item1, 1)
        my_app.add_book_to_user(user2, item2, 1)

        self.assertTrue(my_app.user_has_item(user1, item1))
        self.assertTrue(my_app.user_has_item(user2, item2))
        self.assertFalse(my_app.user_has_item(user1, item2))
        self.assertFalse(my_app.user_has_item(user2, item1))

    def test04(self):
        my_app = MyBooksApp()
        user = "Dijkstra"
        my_app.add_user(user)

        item = "Brand new world"
        my_app.add_book_to_user(user, item, 1)

        self.assertEqual(my_app.get_user_shop_list(user), [(item, 1)])

    def test05(self):
        my_app = MyBooksApp()
        user = "Dijkstra"
        my_app.add_user(user)

        nonexistent_user = "Alan Kay"

        item = "50 sombras de grey"

        with self.assertRaises(Exception) as context:
            my_app.add_book_to_user(nonexistent_user, item, 1)

        self.assertEqual(
            str(context.exception), my_app.user_doesnot_exist_message_error()
        )

    def test06(self):
        my_app = MyBooksApp()
        user = "Dijkstra"
        my_app.add_user(user)

        nonexistent_user = "Alan Kay"

        item = "50 sombras de grey"

        with self.assertRaises(Exception) as context:
            my_app.user_has_item(nonexistent_user, item)

        self.assertEqual(
            str(context.exception), my_app.user_doesnot_exist_message_error()
        )

    def test07(self):
        my_app = MyBooksApp()
        user = "Dijkstra"
        my_app.add_user(user)

        item = "Brand new world"
        my_app.add_book_to_user(user, item, 2)

        self.assertEqual(my_app.get_user_shop_list(user), [(item, 2)])


if __name__ == "__main__":
    unittest.main()
