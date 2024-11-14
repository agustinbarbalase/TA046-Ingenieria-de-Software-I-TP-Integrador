import re
from utils.gregorian_month_of_year import GregorianMonthOfYear


class Card:

    def __init__(self, number: int, gregorian_month_of_year):
        if gregorian_month_of_year <= GregorianMonthOfYear.current():
            raise Exception(Card.cannot_create_expired_card_message())
        if not re.match(r"^\d{16}$", str(number)):
            raise Exception(Card.cannot_create_card_with_invalid_number_message_error())

        self.number = number
        self.gregorian_month_of_year = gregorian_month_of_year

    @classmethod
    def cannot_create_expired_card_message(cls):
        return "Card date is expired can not be created"

    @classmethod
    def cannot_create_card_with_invalid_number_message_error(cls):
        return "Card with invalid number can not be created"

    def is_expired(self):
        return self.gregorian_month_of_year <= GregorianMonthOfYear.current()
