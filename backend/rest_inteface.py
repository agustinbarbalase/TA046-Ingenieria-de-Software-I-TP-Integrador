from unittest import *
from typing import *

class RestInterface:
    def __init__(self):
        pass

    def create_cart(self, user_id: int, password: str) -> Dict:
        response = dict()
        if user_id == 2:
            response["body"] = "1|CART COULD NOT BE CREATED"
        else:
            response["body"] = "0|OK"
        return response
    
    def add_to_cart(self, user_id: int, books_amount: int): 
        pass
    
class RESTInterfaceTest(TestCase):
    
    def test_create_cart_success(self):

        a_rest_interface = RestInterface()

        response = a_rest_interface.create_cart(1, "12345")
        
        self.assertEqual(response["body"], '0|OK')

    def test_create_cart_failure(self):

        a_rest_interface = RestInterface()

        response = a_rest_interface.create_cart(2, "69420")

        self.assertEqual(response["body"], '1|CART COULD NOT BE CREATED')