import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rest_interface import RestInterface, BODY


class RestInterfaceTest(unittest.TestCase):

    def test_create_cart_success(self):

        a_rest_interface = RestInterface()

        response = a_rest_interface.create_cart("1", "12345")

        self.assertEqual(response[BODY], "0|OK")

    def test_list_empty_cart(self):

        a_rest_interface = RestInterface()
        a_rest_interface.create_cart("1", "12345")
        
        self.assertEqual(a_rest_interface.list_cart("1"), "0|")
    
    def test_add_book_to_cart(self):
        a_rest_interface = RestInterface()

        a_rest_interface.create_cart("1", "12345")
        
        a_rest_interface.add_to_cart("1", "1", 1)

        self.assertEqual(a_rest_interface.list_cart("1"), "0|1|1")
    

if __name__ == "__main__":
    unittest.main()
