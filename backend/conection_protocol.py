from unittest import *
from typing import *

class XXX:
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
    
class XXXTest(TestCase):
    
    def test01(self):

        un_XXX = XXX()

        response = un_XXX.create_cart(1, "12345")  ## Aca es user id y password
        
        self.assertEqual(response["body"], '0|OK')

    def test02(self):

        un_XXX = XXX()

        response = un_XXX.create_cart(2, "69420")

        self.assertEqual(response["body"], '1|CART COULD NOT BE CREATED')


    # def test03(self):
    #     un_XXX = XXX()

    #     response = un_XXX.add_to_cart(1, "12345")  ## Aca es user id y password
        
    #     self.assertEqual(response["body"], '0|OK')

    # def test04(self):

    #     un_XXX = XXX()

    #     response = un_XXX.add_to_cart(2, "69420")

    #     self.assertEqual(response["body"], '1|CART COULD NOT BE CREATED')