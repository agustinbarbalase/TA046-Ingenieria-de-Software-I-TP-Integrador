from utils.gregorian_month_of_year import GregorianMonthOfYear


class Card:

    def __init__(self, number, gregorian_month_of_year):
        self.number = number

        self.gregorian_month_of_year = gregorian_month_of_year

    @classmethod
    def initialize_with_number_and_month_and_year(
        cls, number: int, month: int, year: int
    ):
        gregorian_month_of_year = GregorianMonthOfYear(month, year)
        cls.cannot_create_expired_card(number, gregorian_month_of_year)
        return cls(number, gregorian_month_of_year)

    @classmethod
    def cannot_create_expired_card_message(cls):
        return "Card date is expired can not be created"

    @classmethod
    def cannot_create_expired_card(cls, number, gregorian_month_of_year):
        if gregorian_month_of_year.is_greater_than_today():
            raise Exception(Card.cannot_create_expired_card_message())
        return cls(number, gregorian_month_of_year)

    def is_expired(self):
        return self.gregorian_month_of_year.is_greater_than_today()
