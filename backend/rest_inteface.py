from unittest import *
from typing import *

BODY = "body"

class RestInterface:
    def __init__(self):
        pass

    def create_cart(self, user_id: int, password: str) -> Dict[str, str]:
        response = dict()
        if user_id == 2:
            response[BODY] = "1|CART COULD NOT BE CREATED"
        else:
            response[BODY] = "0|OK"
        return response
    
    def add_to_cart(self, user_id: int, books_amount: int): 
        pass
    
class RestInterfaceTest(TestCase):
    
    def test_create_cart_success(self):

        a_rest_interface = RestInterface()

        response = a_rest_interface.create_cart(1, "12345")
        
        self.assertEqual(response[BODY], '0|OK')

    def test_create_cart_failure(self):

        a_rest_interface = RestInterface()

        response = a_rest_interface.create_cart(2, "69420")

        self.assertEqual(response[BODY], '1|CART COULD NOT BE CREATED')