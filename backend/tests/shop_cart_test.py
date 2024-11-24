import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.shop_cart import ShopCart


class ShopCartTest(unittest.TestCase):

    def setUp(self):
        self.item_name_one = "Cincuenta sombras de Alan key"
        self.item_name_two = "El secreto de su codigo encapsulado"

        self.catalog = {self.item_name_one: "π", self.item_name_two: "e"}
        self.item_non_catalog = "1984"

        self.cart = ShopCart.with_catalog(self.catalog)

    def test01_new_cart_is_empty(self):
        self.assertTrue(self.cart.is_empty())

    def test02_can_add_item_to_cart(self):
        self.cart.add_item(self.item_name_one, 1)

        self.assertFalse(self.cart.is_empty())
        self.assertTrue(self.cart.contains_item(self.item_name_one))

    def test03_can_add_multiple_items(self):
        self.cart.add_item(self.item_name_one, 1)
        self.cart.add_item(self.item_name_two, 1)

        self.assertFalse(self.cart.is_empty())
        self.assertTrue(self.cart.contains_item(self.item_name_one))
        self.assertTrue(self.cart.contains_item(self.item_name_two))

    def test04_add_non_existing_item_in_catalog_raises_error(self):
        with self.assertRaises(Exception) as context:
            self.cart.add_item(self.item_non_catalog, 1)

        self.assertEqual(
            str(context.exception), ShopCart.item_not_in_catalog_message_error()
        )

    def test05_list_cart_items(self):
        self.cart.add_item(self.item_name_one, 1)
        self.cart.add_item(self.item_name_two, 1)

        self.assertFalse(self.cart.is_empty())
        self.assertEqual(
            [(self.item_name_one, 1), (self.item_name_two, 1)], self.cart.list_items()
        )

    def test06_add_existed_item_sum(self):
        self.cart.add_item(self.item_name_one, 2)
        self.cart.add_item(self.item_name_one, 3)

        self.assertFalse(self.cart.is_empty())
        self.assertEqual([(self.item_name_one, 5)], self.cart.list_items())


if __name__ == "__main__":
    unittest.main()
