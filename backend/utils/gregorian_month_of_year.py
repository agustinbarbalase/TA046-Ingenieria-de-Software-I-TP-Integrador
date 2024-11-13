# from datetime import datetime as dt


# class GregorianMonthOfYear:

#     def __init__(self, month: int, year: int):
#         self.month = month
#         self.year = year

#     @classmethod
#     def invalid_month_error(cls):
#         return "Invalid month"

#     @classmethod
#     def initialize_with_month_and_year(cls, month: int, year: int):
#         if month < 1 or month > 12:
#             raise Exception(GregorianMonthOfYear.invalid_month_error())
#         return cls(month, year)

#     def is_greater_than_today(self):
#         today = dt.today()
#         return (self.year > today.year) or (
#             self.year == today.year and self.month > today.month
#         )
