import re
from utils.gregorian_month_of_year import GregorianMonthOfYear


class Card:
    """Instance creation - class"""

    @classmethod
    def with_number_and_month_of_year(
        cls, number: int, gregorian_month_of_year: GregorianMonthOfYear
    ):
        return cls(number, gregorian_month_of_year)

    """Error messages - class"""

    @classmethod
    def cannot_create_card_with_invalid_number_message_error(cls):
        return "Card with invalid number can not be created"

    """Initialization"""

    def __init__(self, number: int, gregorian_month_of_year: GregorianMonthOfYear):
        if not re.match(r"^\d{16}$", str(number)):
            raise Exception(Card.cannot_create_card_with_invalid_number_message_error())

        self.number = number
        self.gregorian_month_of_year = gregorian_month_of_year

    """Main protocol"""

    def is_expired(self, date):
        return self.gregorian_month_of_year <= date

    def get_number_card(self):
        return self.number
