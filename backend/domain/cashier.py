from datetime import datetime
from domain.shop_cart import ShopCart
from utils.card import Card
from utils.gregorian_month_of_year import GregorianMonthOfYear
from domain.postnet.postnet_interface import PostnetInterface


class Cashier:
    """Instance creation - class"""

    @classmethod
    def with_postnet(cls, postnet: PostnetInterface):
        return cls(postnet)

    """Error messages - class"""

    @classmethod
    def empty_cart_message_error(cls):
        return "Empty cart"

    @classmethod
    def expired_card_message_error(cls):
        return "Expired card"

    """Initialization"""

    def __init__(self, postnet):
        self.postnet = postnet

    """Private - checks"""

    def _check_empty_cart(self, cart):
        if cart.is_empty():
            raise Exception(Cashier.empty_cart_message_error())

    def _check_expired(self, card):
        if card.is_expired(GregorianMonthOfYear.current()):
            raise Exception(Cashier.expired_card_message_error())

    """Main Protocol"""

    def check_out(self, cart: ShopCart, card: Card):
        self._check_expired(card)
        self._check_empty_cart(cart)
        print(cart.total_amount())
        return self.postnet.return_ticket(card, cart.total_amount())
