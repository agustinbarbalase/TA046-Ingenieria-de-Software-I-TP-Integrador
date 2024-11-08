from typing import *
from shop_cart import ShopCart


class UserDoesntExistError(Exception):
    pass


class CantAddNonPositiveAmountOfBooks(Exception):
    pass


class MyBooksApp:

    def __init__(self):
        self.users_ids = dict()

    def user_doesnot_exist_validation(self, user_id: str):
        if not user_id in self.users_ids:
            raise UserDoesntExistError

    def cant_add_non_positive_amount_of_books(self, amount: int):
        if amount <= 0:
            raise CantAddNonPositiveAmountOfBooks

    def add_user(self, user_id: str):
        if user_id in self.users_ids:
            return self
        self.users_ids[user_id] = ShopCart()
        return self

    def has_user(self, user_id: str) -> bool:
        return user_id in self.users_ids

    def user_has_item(self, user_id: str, item: str) -> bool:
        self.user_doesnot_exist_validation(user_id)
        return self.users_ids[user_id].contains_item(item)

    def get_user_shop_list(self, user_id: str) -> list:
        self.user_doesnot_exist_validation(user_id)
        return self.users_ids[user_id].list_items()

    def add_book_to_user(self, user_id: str, isbn: str, amount: int):
        self.user_doesnot_exist_validation(user_id)
        self.cant_add_non_positive_amount_of_books(amount)
        return self.users_ids[user_id].add_item(isbn, amount)
