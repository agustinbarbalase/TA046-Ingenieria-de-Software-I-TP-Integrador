from datetime import datetime
from domain.shop_cart import ShopCart
from utils.card import Card
from utils.gregorian_month_of_year import GregorianMonthOfYear


class Checkout:

    def __init__(self, postnet):
        self.postnet = postnet

    @classmethod
    def empty_cart_message_error(cls):
        return "Empty cart"

    @classmethod
    def expired_card_message_error(cls):
        return "Expired card"

    def _check_empty_cart(self, cart):
        if cart.is_empty():
            raise Exception(Checkout.empty_cart_message_error())

    def _check_expired(self, card):
        if card.is_expired(GregorianMonthOfYear.current()):
            raise Exception(Checkout.expired_card_message_error())

    def check_out(self, cart: ShopCart, card: Card):
        self._check_expired(card)
        self._check_empty_cart(cart)
        return self.postnet.return_ticket(cart, card)
