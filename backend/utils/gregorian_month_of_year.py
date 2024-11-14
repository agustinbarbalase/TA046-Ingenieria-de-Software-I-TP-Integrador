from datetime import datetime as dt


class GregorianMonthOfYear:

    def __init__(self, month: int, year: int):
        if month < 1 or month > 12:
            raise Exception(GregorianMonthOfYear.invalid_month_error())

        self.month = month
        self.year = year

    @classmethod
    def invalid_month_error(cls) -> str:
        return "Invalid month"

    @classmethod
    def current(cls):
        today = dt.now()
        return cls(today.month, today.year)

    def __le__(self, other) -> bool:
        return self.year <= other.year or (
            self.year == other.year and self.month <= other.month
        )
