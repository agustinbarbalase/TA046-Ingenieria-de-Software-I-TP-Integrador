from copy import copy
from datetime import datetime
from typing import List
from domain.checkout import Checkout
from utils.card import Card
from utils.bag import Bag
from domain.shop_cart import ShopCart


class UserSession:
    """Initialization"""

    def __init__(self, catalog: dict[str, str], expiration_date: datetime):
        self.cart: ShopCart = ShopCart.with_catalog(catalog)
        self.expiration_date = expiration_date

    """Main protocol"""

    def is_expired(self, current_date: datetime):
        print(self.expiration_date)
        print(current_date)
        print(self.expiration_date < current_date)
        return self.expiration_date < current_date

    def has_item(self, item: str):
        return self.cart.contains_item(item)

    def get_user_shop_list(self) -> list:
        return self.cart.list_items()

    def add_book(self, isbn: str, amount: int):
        return self.cart.add_item(isbn, amount)

    def user_cart(self):
        return copy(self.cart)
