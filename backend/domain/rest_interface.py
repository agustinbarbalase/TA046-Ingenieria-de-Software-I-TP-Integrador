from unittest import TestCase
from typing import *

from domain.my_books_app import MyBooksApp

BODY = "body"
STATUS_CODE = "status_code"

# Regex for ^\d{9}[0-9X]$


class RestInterface:
    def __init__(self, app):
        self.book_app = app

    def create_cart(self, user_id: int, password: str) -> dict[str, str]:
        response = dict()
        if password == "1234":
            response[BODY] = "1|CART COULD NOT BE CREATED"
            response[STATUS_CODE] = "422"
        else:
            self.book_app.add_user(user_id)
            response[BODY] = "0|OK"
            response[STATUS_CODE] = "200"
        return response

    def list_cart(self, user_id: str):
        response = dict()

        try:
            book_list = self.book_app.get_user_shop_list(user_id)
            result = ["0"]

            for element in book_list:
                result.append(element[0])
                result.append(str(element[1]))

            response[BODY] = "|".join(result) + ("|" if len(result) == 1 else "")
            response[STATUS_CODE] = "200"

        except Exception as error:
            response[BODY] = f"1|{str(error).upper()}"
            response[STATUS_CODE] = "422"

        return response

    def add_to_cart(self, user_id: str, isbn: str, books_amount: int):
        response = dict()
        try:
            self.book_app.add_book_to_user(user_id, isbn, books_amount)
            response[BODY] = "0|OK"
            response[STATUS_CODE] = "200"
        except Exception as error:
            response[BODY] = f"1|{str(error).upper()}"
            response[STATUS_CODE] = "422"

        return response
