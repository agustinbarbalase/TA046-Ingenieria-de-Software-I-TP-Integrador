from datetime import datetime, timedelta
from typing import *
from utils.clock.clock_interface import ClockInterface
from domain.auth.auth_service_interface import AuthServiceInterface
from domain.user_session import UserSession
from domain.cashier import Cashier

from domain.postnet.postnet_interface import PostnetInterface
from domain.shopping_history_book import ShopingHistoryBook
from utils.card import Card
from domain.auth.auth_service import AuthService
from domain.shop_cart import ShopCart


class MyBooksApp:
    """Instance creation - class"""

    @classmethod
    def with_dependencies(
        cls,
        catalog: dict[str, str],
        auth: AuthServiceInterface,
        clock: ClockInterface,
        user_session_time: int,
        shopping_history: ShopingHistoryBook,
        postnet: PostnetInterface,
    ):
        return cls(catalog, auth, clock, user_session_time, shopping_history, postnet)

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
        self,
        catalog: dict[str, str],
        auth: AuthServiceInterface,
        clock: ClockInterface,
        user_session_time: int,
        shopping_history: ShopingHistoryBook,
        postnet: PostnetInterface,
    ):
        self.users_ids: dict[str, UserSession] = dict()
        self.catalog: dict[str, str] = catalog
        self.auth = auth
        self.shopping_history = ShopingHistoryBook.new()
        self.cashier = Cashier.with_postnet_and_shopping_history(
            postnet, self.shopping_history
        )
        self.clock = clock
        self.user_session_time = user_session_time

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

    def _validate_user_expired_session(self, user_id: str):
        user_session = self.users_ids.get(
            user_id, self.user_doesnot_exist_validation(user_id)
        )
        if user_session is None:
            self.user_does_not_exist_error()
        if user_session.is_expired(self.clock):
            raise Exception(MyBooksApp.user_expired_session_message_error())

    """Main protocol"""

    def add_user(self, user_id: str, password: str):
        if self.auth:
            self.auth.autenticate_user(user_id, password)
        new_user = UserSession.with_catalog_and_expiration_date(
            self.catalog, self.clock.later_date_to_seconds(self.user_session_time)
        )
        self.users_ids[user_id] = new_user

    def has_user(self, user_id: str) -> bool:
        return user_id in self.users_ids

    def user_has_item(self, user_id: str, item: str) -> bool:
        user = self.users_ids.get(user_id, self.user_doesnot_exist_validation(user_id))
        if user is None:
            self.user_does_not_exist_error()
        user = self.users_ids.get(user_id)
        return user.has_item(item)

    def get_user_shop_list(self, user_id: str) -> list:
        user_session = self.users_ids.get(
            user_id, self.user_doesnot_exist_validation(user_id)
        )
        if user_session is None:
            self.user_does_not_exist_error()
        self._validate_user_expired_session(user_id)
        user_session = self.users_ids.get(user_id)
        return user_session.get_user_shop_list()

    def add_book_to_user(self, user_id: str, isbn: str, amount: int):
        user_session = self.users_ids.get(
            user_id, self.user_doesnot_exist_validation(user_id)
        )
        if user_session is None:
            self.user_does_not_exist_error()
        self._validate_user_expired_session(user_id)
        self._cant_add_non_positive_amount_of_books_validation(amount)
        return user_session.add_book(isbn, amount)

    def checkout(self, user_id: str, card: Card):
        self._validate_user_expired_session(user_id)

        user_session = self.users_ids.get(
            user_id, self.user_doesnot_exist_validation(user_id)
        )
        if user_session is None:
            self.user_does_not_exist_error()

        user_cart = user_session.user_cart()
        ticket = self.cashier.check_out(user_cart, card, user_id)
        user_session.empty_cart()

        return ticket

    def user_shop_history(self, user_id: str, password: str):
        if self.auth:
            self.auth.autenticate_user(user_id, password)
        try:
            shop_history = self.shopping_history.history_for_user(user_id)
            return shop_history.history()
        except Exception as err:
            return (0, [])
