from copy import copy
from datetime import datetime
from typing import List
from domain.checkout import Checkout
from utils.card import Card
from utils.bag import Bag
from domain.shop_cart import ShopCart


class User:

    def __init__(self, catalog: set[str], expiration_date: datetime):
        self.cart: ShopCart = ShopCart(catalog)
        self.expiration_date = expiration_date
        self.shop_history: Bag = Bag()
        self.succesful_transactions: int = 0

    def is_expired(self, current_date: datetime):
        return self.expiration_date < current_date

    def has_item(self, item: str):
        return self.cart.contains_item(item)

    def get_user_shop_list(self) -> list:
        return self.cart.list_items()

    def add_book(self, isbn: str, amount: int):
        return self.cart.add_item(isbn, amount)

    def user_cart(self):
        return copy(self.cart)

    def check_out_user(self, checkout: Checkout, card: Card):
        ## To do: revisar que pasa cuando la compra no sea correcta
        shop_ticket = checkout.check_out(self.cart, card)
        self.shop_history.add_list(self.cart.list_items())
        self.cart = ShopCart(self.cart.catalog)
        self.succesful_transactions += 1
        return shop_ticket

    def shop_history_list(self):
        if self.succesful_transactions < 2:
            return []
        return self.shop_history.list_items()
