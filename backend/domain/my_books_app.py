from datetime import datetime, timedelta
from typing import *
from domain.user import User
from domain.checkout import Checkout

from domain.postnet.postnet import Postnet
from utils.card import Card
from domain.auth.auth_service import AuthService
from domain.shop_cart import ShopCart

SESSION_DURATION_IN_SECONDS = 2


class MyBooksApp:

    def __init__(self, catalog: set[str]):
        self.users_ids: dict[str, User] = dict()
        self.catalog: set[str] = catalog
        self.auth = None
        self.checkout_instance = Checkout(Postnet())

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

    @classmethod
    def user_expired_session_message_error(cls):
        return "User session expired"

    def user_doesnot_exist_validation(self, user_id: str):
        if not user_id in self.users_ids:
            raise Exception(MyBooksApp.user_doesnot_exist_message_error())
        if self.users_ids.get(user_id) is None:
            raise Exception(MyBooksApp.user_doesnot_exist_message_error())

    def cant_add_non_positive_amount_of_books_validation(self, amount: int):
        if amount <= 0:
            raise Exception(
                MyBooksApp.cant_add_non_positive_amount_of_books_message_error()
            )

    def validate_user_expired_session(self, user_id: str):
        user_data = self.users_ids.get(user_id)
        if user_data.is_expired(datetime.now()):
            raise Exception(MyBooksApp.user_expired_session_message_error())

    def add_user(self, user_id: str, password: str):
        if self.auth:
            self.auth.autenticate_user(user_id, password)
        duration = timedelta(seconds=SESSION_DURATION_IN_SECONDS)
        new_user = User(self.catalog, datetime.now() + duration)
        self.users_ids[user_id] = self.users_ids.get(user_id, new_user)

    def has_user(self, user_id: str) -> bool:
        return user_id in self.users_ids

    def user_has_item(self, user_id: str, item: str) -> bool:
        self.user_doesnot_exist_validation(user_id)
        user = self.users_ids.get(user_id)
        return user.has_item(item)

    def get_user_shop_list(self, user_id: str) -> list:
        self.user_doesnot_exist_validation(user_id)
        self.validate_user_expired_session(user_id)
        user = self.users_ids.get(user_id)
        return user.get_user_shop_list()

    def add_book_to_user(self, user_id: str, isbn: str, amount: int):
        self.user_doesnot_exist_validation(user_id)
        self.cant_add_non_positive_amount_of_books_validation(amount)
        self.validate_user_expired_session(user_id)
        user = self.users_ids.get(user_id)
        return user.add_book(isbn, amount)

    def checkout(self, user_id: str, card: Card):
        self.user_doesnot_exist_validation(user_id)
        self.validate_user_expired_session(user_id)
        user = self.users_ids.get(user_id)
        if user is None:
            raise Exception()
        user_shop_cart = user.user_cart()
        return self.checkout_instance.check_out(user_shop_cart, card)
