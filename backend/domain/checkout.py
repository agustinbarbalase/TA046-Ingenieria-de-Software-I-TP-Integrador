from datetime import datetime


class Checkout:

    def __init__(self):
        self.xyz = None

    def initialize_date(self, date):
        self.month = date

    def initialize_xyz(self, xyz):
        self.xyz = xyz
        return self

    @classmethod
    def with_xyz(cls, xyz):
        return cls().initialize_xyz(xyz)

    @classmethod
    def empty_cart_message_error(cls):
        return "Empty cart"

    @classmethod
    def invalid_date_message_error(cls):
        return "Invalid date"

    @classmethod
    def expired_card_message_error(cls):
        return "Expired card"

    @classmethod
    def with_date(cls, date):
        return cls().initialize_date(date)

    def _check_date(self, date):
        try:
            month, year = date[:2], date[2:]
            expiration_date = datetime(int(year), int(month), 1)
            return expiration_date
        except ValueError:
            raise Exception(Checkout.invalid_date_message_error())

    def _check_empty_cart(self, cart):
        if cart.is_empty():
            raise Exception(Checkout.empty_cart_message_error())

    def _check_expired(self, date):
        if date <= datetime.now():
            raise Exception(Checkout.expired_card_message_error())

    def check_out(self, cart, card):
        expiration_date = self._check_date(card["card_expiration_date"])
        self._check_expired(expiration_date)
        self._check_empty_cart(cart)
        return self.xyz.return_ticket(cart, card)
