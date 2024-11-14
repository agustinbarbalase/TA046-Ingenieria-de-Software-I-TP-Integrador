from unittest import TestCase
from typing import *

from domain.my_books_app import MyBooksApp

# Regex for ^\d{9}[0-9X]$


class Response(NamedTuple):
    body: str
    status_code: int


class RestInterface:
    def __init__(self, app):
        self.book_app = app

    def _return_response(self, closure) -> Response:
        try:
            return closure()
        except Exception as error:
            return Response(f"1|{str(error).upper()}", 422)

    def create_cart(self, user_id: int, password: str) -> Response:
        def closure():
            self.book_app.add_user(user_id, password)
            return Response("0|OK", 200)

        return self._return_response(closure)

    def list_cart(self, user_id: str) -> Response:
        def closure():
            book_list = self.book_app.get_user_shop_list(user_id)
            result = ["0"]

            for element in book_list:
                result.append(element[0])
                result.append(str(element[1]))

            return Response("|".join(result) + ("|" if len(result) == 1 else ""), 200)

        return self._return_response(closure)

    def add_to_cart(self, user_id: str, isbn: str, books_amount: int) -> Response:
        def closure():
            self.book_app.add_book_to_user(user_id, isbn, books_amount)
            return Response("0|OK", 200)

        return self._return_response(closure)
