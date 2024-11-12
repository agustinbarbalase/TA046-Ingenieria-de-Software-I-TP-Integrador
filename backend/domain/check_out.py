from datetime import datetime


class CheckOut:

    def __init__(self):
        pass

    def initialize_date(self, date):
        self.month = date

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
            expiration_date = date(int(year), int(month), 1)
            return expiration_date
        except ValueError:
            raise Exception(CheckOut.invalid_date_message_error())

    def _check_empty_cart(self, cart):
        if cart.is_empty():
            raise Exception(CheckOut.empty_cart_message_error())

    def _check_expired(self, date):
        if date <= datetime.now():
            raise Exception(CheckOut.expired_card_message_error())

    def check_out(self, cart, card):
        expiration_date = self._check_date(card["card_expiration_date"])
        self._check_expired(expiration_date)
        self._check_empty_cart(cart)
