from datetime import datetime as dt


class GregorianMonthOfYear:
    """Initialization"""

    def __init__(self, month: int, year: int):
        if month < 1 or month > 12:
            raise Exception(GregorianMonthOfYear.invalid_month_message_error())

        self.month = month
        self.year = year

    """Error messages"""

    @classmethod
    def invalid_month_message_error(cls) -> str:
        return "Invalid month"

    """Instance creation"""

    @classmethod
    def current(cls):
        today = dt.now()
        return cls(today.month, today.year)

    """Main protocol"""

    def __le__(self, other) -> bool:
        return self.year <= other.year or (
            self.year == other.year and self.month <= other.month
        )
