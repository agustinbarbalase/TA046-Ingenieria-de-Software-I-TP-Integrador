from unittest import TestCase
from typing import *

from backend.domain.my_books_app import (
    MyBooksApp,
    UserDoesntExistError,
    CantAddNonPositiveAmountOfBooks,
)

BODY = "body"

# Regex for ^\d{9}[0-9X]$


class RestInterface:
    def __init__(self):
        self.book_app = MyBooksApp()

    def create_cart(self, user_id: int, password: str) -> dict[str, str]:
        response = dict()
        if password == "1234":
            response[BODY] = "1|CART COULD NOT BE CREATED"
        else:
            self.book_app.add_user(user_id)
            response[BODY] = "0|OK"
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
        except UserDoesntExistError:
            response[BODY] = "1|THE USER DOESN'T EXIST"

        return response

    def add_to_cart(self, user_id: str, isbn: str, books_amount: int):
        response = dict()
        try:
            self.book_app.add_book_to_user(user_id, isbn, books_amount)
            response[BODY] = "0|OK"
            return response
        except CantAddNonPositiveAmountOfBooks:
            response[BODY] = "1|CAN'T ADD NON POSTIVE AMOUNT OF BOOKS"
            return response
        else:
            response[BODY] = "1|ERROR_ADDING_BOOK"
            return response