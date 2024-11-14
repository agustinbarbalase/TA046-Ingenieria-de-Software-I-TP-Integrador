from typing import *
from domain.auth.auth_service import AuthService
from domain.shop_cart import ShopCart


class MyBooksApp:

    def __init__(self, catalog: set[str]):
        self.users_ids: dict[str, ShopCart] = dict()
        self.catalog: set[str] = catalog
        self.auth = None

    @classmethod
    def with_auth(cls, catalog: set[str], auth: AuthService):
        return cls(catalog).initialize_with_auth(auth)

    def initialize_with_auth(self, auth):
        self.auth = auth
        return self

    @classmethod
    def user_doesnot_exist_message_error(self):
        return "The user doesn't exist"

    @classmethod
    def cant_add_non_positive_amount_of_books_message_error(self):
        return "Can't add non positive amount of books"

    def user_doesnot_exist_validation(self, user_id: str):
        if not user_id in self.users_ids:
            raise Exception(MyBooksApp.user_doesnot_exist_message_error())

    def cant_add_non_positive_amount_of_books_validation(self, amount: int):
        if amount <= 0:
            raise Exception(
                MyBooksApp.cant_add_non_positive_amount_of_books_message_error()
            )

    def add_user(self, user_id: str, password: str):
        if self.auth:
            self.auth.autenticate_user(user_id, password)
        self.users_ids[user_id] = ShopCart(self.catalog)

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
        self.cant_add_non_positive_amount_of_books_validation(amount)
        return self.users_ids[user_id].add_item(isbn, amount)
