import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from my_books_app import MyBooksApp


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

        my_app.user_add_item(user, item)

        self.assertTrue(my_app.user_has_item(user, item))

    def test03(self):
        my_app = MyBooksApp()
        user1 = "Dijkstra"
        my_app.add_user(user1)
        user2 = "Turing"
        my_app.add_user(user2)

        item1 = "Brand new world"
        item2 = "animal farm"
        my_app.user_add_item(user1, item1)
        my_app.user_add_item(user2, item2)

        self.assertTrue(my_app.user_has_item(user1, item1))
        self.assertTrue(my_app.user_has_item(user2, item2))
        self.assertFalse(my_app.user_has_item(user1, item2))
        self.assertFalse(my_app.user_has_item(user2, item1))

    def test04(self):
        my_app = MyBooksApp()
        user = "Dijkstra"
        my_app.add_user(user)

        item = "Brand new world"
        my_app.user_add_item(user, item)

        self.assertEqual(my_app.get_user_shop_list(user), [(item, 1)])


if __name__ == "__main__":
    unittest.main()
