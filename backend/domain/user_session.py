from copy import copy
from datetime import datetime
from typing import List
from domain.cashier import Cashier
from utils.card import Card
from utils.clock.clock_interface import ClockInterface
from utils.bag import Bag
from domain.shop_cart import ShopCart


class UserSession:
    """Instance creation - class"""

    @classmethod
    def with_catalog_and_expiration_date(
        cls, catalog: dict[str, str], expiration_date: datetime
    ):
        return cls(catalog, expiration_date)

    """Initialization"""

    def __init__(self, catalog: dict[str, str], expiration_date: datetime):
        self.catalog: dict[str, str] = catalog
        self.cart: ShopCart = ShopCart.with_catalog(catalog)
        self.expiration_date = expiration_date

    """Main protocol"""

    def is_expired(self, clock: ClockInterface):
        return clock.is_later_that(self.expiration_date)

    def has_item(self, item: str):
        return self.cart.contains_item(item)

    def get_user_shop_list(self) -> list:
        return self.cart.list_items()

    def add_book(self, isbn: str, amount: int):
        return self.cart.add_item(isbn, amount)

    def user_cart(self):
        return copy(self.cart)

    def shop_history_list(self):
        return []

    def empty_cart(self):
        self.cart = ShopCart.with_catalog(self.catalog)
