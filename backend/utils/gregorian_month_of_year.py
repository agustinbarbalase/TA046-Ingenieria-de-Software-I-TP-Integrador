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
    def current_month_of_year(cls):
        today = dt.now()
        return cls(today.month, today.year)

    def _year(self) -> int:
        return self.year

    def _month(self) -> int:
        return self.month

    def __le__(self, other) -> bool:
        return self.year <= other._year() or self.month <= other._month()
