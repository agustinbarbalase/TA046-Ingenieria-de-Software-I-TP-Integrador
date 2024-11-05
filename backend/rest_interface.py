from unittest import TestCase
from typing import *

BODY = "body"


class RestInterface:
    def __init__(self):
        pass

    def create_cart(self, user_id: int, password: str) -> dict[str, str]:
        response = dict()
        if user_id == 2:
            response[BODY] = "1|CART COULD NOT BE CREATED"
        else:
            response[BODY] = "0|OK"
        return response

    def add_to_cart(self, user_id: int, books_amount: int):
        pass
