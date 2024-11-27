from datetime import datetime, timedelta
from typing import *
from utils.clock import Clock
from domain.auth.auth_service_interface import AuthServiceInterface
from domain.user_session import UserSession
from domain.checkout import Checkout

from domain.postnet.postnet import Postnet
from utils.card import Card
from domain.auth.auth_service import AuthService
from domain.shop_cart import ShopCart

SESSION_DURATION_IN_SECONDS = 60


class MyBooksApp:
    """Instance creation - class"""

    @classmethod
    def with_catalog_and_auth(
        cls, catalog: dict[str, str], auth: AuthServiceInterface, clock: Clock
    ):
        return cls(catalog, auth, clock)

    """Error messages - class"""

    @classmethod
    def user_doesnot_exist_message_error(self):
        return "The user doesn't exist"

    @classmethod
    def cant_add_non_positive_amount_of_books_message_error(self):
        return "Can't add non positive amount of books"

    @classmethod
    def user_expired_session_message_error(cls):
        return "User session expired"

    """Initialization"""

    def __init__(
        self, catalog: dict[str, str], auth: AuthServiceInterface, clock: Clock
    ):
        self.users_ids: dict[str, UserSession] = dict()
        self.catalog: dict[str, str] = catalog
        self.auth = auth
        self.checkout_instance = Checkout.with_postnet(Postnet())
        self.clock = clock

    def user_does_not_exist_error(self):
        raise Exception(MyBooksApp.user_doesnot_exist_message_error())

    def user_doesnot_exist_validation(self, user_id: str):
        if not user_id in self.users_ids:
            self.user_does_not_exist_error()

    """Private - validations"""

    def _cant_add_non_positive_amount_of_books_validation(self, amount: int):
        if amount <= 0:
            raise Exception(
                MyBooksApp.cant_add_non_positive_amount_of_books_message_error()
            )

    def _validate_user_expired_session(self, user_id: str, current_time: datetime):
        user = self.users_ids.get(user_id, self.user_doesnot_exist_validation(user_id))
        if user is None:
            self.user_does_not_exist_error()
        if user.is_expired(current_time):
            raise Exception(MyBooksApp.user_expired_session_message_error())

    """Main protocol"""

    def add_user(self, user_id: str, password: str):
        if self.auth:
            self.auth.autenticate_user(user_id, password)
        duration = timedelta(seconds=SESSION_DURATION_IN_SECONDS)
        new_user = UserSession(self.catalog, datetime.now())
        self.users_ids[user_id] = self.users_ids.get(user_id, new_user)

    def has_user(self, user_id: str) -> bool:
        return user_id in self.users_ids

    def user_has_item(self, user_id: str, item: str) -> bool:
        user = self.users_ids.get(user_id, self.user_doesnot_exist_validation(user_id))
        if user is None:
            self.user_does_not_exist_error()
        user = self.users_ids.get(user_id)
        return user.has_item(item)

    def get_user_shop_list(self, user_id: str) -> list:
        user = self.users_ids.get(user_id, self.user_doesnot_exist_validation(user_id))
        if user is None:
            self.user_does_not_exist_error()
        user = self.users_ids.get(user_id)
        return user.get_user_shop_list()

    def add_book_to_user(self, user_id: str, isbn: str, amount: int):
        user = self.users_ids.get(user_id, self.user_doesnot_exist_validation(user_id))
        if user is None:
            self.user_does_not_exist_error()
        self._cant_add_non_positive_amount_of_books_validation(amount)
        return user.add_book(isbn, amount)

    def checkout(self, user_id: str, card: Card):
        user = self.users_ids.get(user_id, self.user_doesnot_exist_validation(user_id))
        if user is None:
            self.user_does_not_exist_error()

        user_cart = user.user_cart()
        ticket = self.checkout_instance.check_out(user_cart, card)
        user.register_purcharse(user_cart.list_items())
        return ticket

    def user_shop_history(self, user_id: str):
        user = self.users_ids.get(user_id, self.user_doesnot_exist_validation(user_id))
        if user is None:
            self.user_does_not_exist_error()
        return user.shop_history_list()
