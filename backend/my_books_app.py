from unittest import TestCase
from typing import *


class MyBooksApp:

    def __init__(self):
        self.users = dict()

    def add_user(self, user: str) -> None:
        self.users[user] = set()
        return self

    def has_user(self, user: str) -> bool:
        return user in self.users

    def user_add_item(self, user: str, item: str) -> None:
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
