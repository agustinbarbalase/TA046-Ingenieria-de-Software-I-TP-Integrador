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

    def create_cart(self, params: dict[str, str]) -> Response:
        def closure():
            self.book_app.add_user(params["userId"], params["password"])
            return Response("0|OK", 200)

        return self._return_response(closure)

    def list_cart(self, params: dict[str, str]) -> Response:
        def closure():
            book_list = self.book_app.get_user_shop_list(params["userId"])
            result = ["0"]

            for element in book_list:
                result.append(element[0])
                result.append(str(element[1]))

            return Response("|".join(result) + ("|" if len(result) == 1 else ""), 200)

        return self._return_response(closure)

    def add_to_cart(self, params: dict[str, str]) -> Response:
        def closure():
            self.book_app.add_book_to_user(
                params["userId"], params["isbn"], int(params["amount"])
            )
            return Response("0|OK", 200)

        return self._return_response(closure)
