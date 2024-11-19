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

    @classmethod
    def cant_send_empty_params_message_error(cls):
        return "Can't send empty params"

    @classmethod
    def cant_send_request_with_abstent_params_message_error(self):
        return "Can't sent request with abstent params"

    def _return_response(self, closure) -> Response:
        try:
            return closure()
        except Exception as error:
            return Response(f"1|{str(error).upper()}", 422)

    def _check_empty_params(self, value: str):
        if len(value) == 0:
            raise Exception(RestInterface.cant_send_empty_params_message_error())

    def _check_abstent_params(self, expected_param: str, params: dict[str, str]):
        if expected_param not in params:
            raise Exception(
                RestInterface.cant_send_request_with_abstent_params_message_error()
            )

    def _validate_params(self, params: dict[str, str], expected_params: list[str]):
        for expected_param in expected_params:
            self._check_abstent_params(expected_param, params)
        for key in params:
            self._check_empty_params(params[key])

    def create_cart(self, params: dict[str, str]) -> Response:
        def closure():
            self._validate_params(params, ["userId", "password"])
            self.book_app.add_user(params["userId"], params["password"])
            return Response("0|OK", 200)

        return self._return_response(closure)

    def list_cart(self, params: dict[str, str]) -> Response:
        def closure():
            self._validate_params(params, ["userId"])
            book_list = self.book_app.get_user_shop_list(params["userId"])
            result = ["0"]

            for element in book_list:
                result.append(element[0])
                result.append(str(element[1]))

            return Response("|".join(result) + ("|" if len(result) == 1 else ""), 200)

        return self._return_response(closure)

    def add_to_cart(self, params: dict[str, str]) -> Response:
        def closure():
            self._validate_params(params, ["userId", "bookIsbn", "bookQuantity"])
            self.book_app.add_book_to_user(
                params["userId"], params["bookIsbn"], int(params["bookQuantity"])
            )
            return Response("0|OK", 200)

        return self._return_response(closure)

    def checkout(self, params: dict[str, str]) -> Response:
        def closure():
            self._validate_params(params, ["userId", "ccn", "cced", "cco"])
            return Response(
                self.book_app.checkout(
                    params["userId"], params["ccn"], params["cced"], params["cco"]
                ),
                200,
            )

        return self._return_response(closure)
