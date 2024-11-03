from unittest import TestCase
from typing import *

class MyBooksApp:

    def __init__(self):
        self.users = dict()

    def add_user(self, user: str) -> Self:
        self.users[user] = set()
        return self

    def has_user(self, user: str) -> bool:
        return user in self.users

    def user_add_item(self, user: str, item: str) -> Self:
        if not user in self.users:
            return
        self.users[user].add(item)
        return self
    
    def user_has_item(self, user: str, item: str) -> bool:
        if not user in self.users:
            return False
        return item in self.users[user]
    
    def get_user_shop_list(self, user: str) -> list:
        return list(self.users[user])

class MyBooksAppTest(TestCase):

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
        
        self.assertEqual(my_app.get_user_shop_list(user), [item])