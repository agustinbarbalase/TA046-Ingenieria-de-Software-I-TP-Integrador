from unittest import TestCase
from typing import *


class MyBooksApp:

    def __init__(self):
        self.users_ids = dict()

    def add_user(self, user_id: str):
        self.users_ids[user_id] = set()
        return self

    def has_user(self, user_id: str) -> bool:
        return user_id in self.users_ids

    def user_add_item(self, user_id: str, item: str):
        if not user_id in self.users_ids:
            return
        self.users_ids[user_id].add(item)
        return self

    def user_has_item(self, user_id: str, item: str) -> bool:
        if not user_id in self.users_ids:
            return False
        return item in self.users_ids[user_id]

    def get_user_shop_list(self, user_id: str) -> list:
        return list(self.users_ids[user_id])
