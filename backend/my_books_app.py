from unittest import TestCase
from typing import *

from shop_cart import ShopCart


class MyBooksApp:

    def __init__(self):
        self.users_ids = dict()

    def add_user(self, user_id: str):
        if not user_id in self.users_ids:
            return self
        self.users_ids[user_id] = ShopCart()
        return self

    def has_user(self, user_id: str) -> bool:
        return user_id in self.users_ids

    def user_add_item(self, user_id: str, item: str):
        if not user_id in self.users_ids:
            return
        self.users_ids[user_id].add_item(item, 1)
        return self

    def user_has_item(self, user_id: str, item: str) -> bool:
        if not user_id in self.users_ids:
            return False
        return item in self.users_ids[user_id]

    def get_user_shop_list(self, user_id: str) -> list:
        if not user_id in self.users_ids:
            return []
        return self.users_ids[user_id].list_items()

    def add_book_to_user(self, user_id: str, isbn: str, amount: int ):
        if not user_id in self.users_ids:
            return []
        return self.users_ids[user_id].add_item(isbn, 1)
            
        