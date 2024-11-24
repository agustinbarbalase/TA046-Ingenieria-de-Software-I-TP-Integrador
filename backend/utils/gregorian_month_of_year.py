from datetime import datetime as dt


class GregorianMonthOfYear:
    """Instance creation - class"""

    @classmethod
    def with_month_and_year(cls, month: int, year: int):
        return cls(month, year)

    @classmethod
    def current(cls):
        today = dt.now()
        return cls(today.month, today.year)

    """Error messages - class"""

    @classmethod
    def invalid_month_message_error(cls) -> str:
        return "Invalid month"

    """Initialization"""

    def __init__(self, month: int, year: int):
        if month < 1 or month > 12:
            raise Exception(GregorianMonthOfYear.invalid_month_message_error())

        self.month = month
        self.year = year

    """Main protocol"""

    def __le__(self, other) -> bool:
        return self.year <= other.year or (
            self.year == other.year and self.month <= other.month
        )
