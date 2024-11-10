import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.domain.shop_cart import ShopCart, ItemNotInCatalog


class ShopCartTest(unittest.TestCase):

    def setUp(self):
        self.item_name_one = "Cincuenta sombras de Alan key"
        self.item_name_two = "El secreto de su codigo encapsulado"

        self.catalog = set(list(self.item_name_one))
        self.item_non_catalog = "1984"

        self.car = ShopCart()

    def test01_new_cart_is_empty(self):
        self.assertTrue(self.car.is_empty())

    def test02_can_add_item_to_cart(self):
        self.car.add_item(self.item_name_one, 1)

        self.assertFalse(self.car.is_empty())
        self.assertTrue(self.car.contains_item(self.item_name_one))

    def test03_can_add_multiple_items(self):
        self.car.add_item(self.item_name_one, 1)
        self.car.add_item(self.item_name_two, 1)

        self.assertFalse(self.car.is_empty())
        self.assertTrue(self.car.contains_item(self.item_name_one))
        self.assertTrue(self.car.contains_item(self.item_name_two))

    def test04_add_non_existing_cart_in_catalog_raises_error(self):
        car_with_catalog = ShopCart.with_catalog(self.catalog)

        with self.assertRaises(ItemNotInCatalog):
            car_with_catalog.add_item(self.item_non_catalog, 1)

    def test05_list_cart_items(self):
        self.car.add_item(self.item_name_one, 1)
        self.car.add_item(self.item_name_two, 1)

        self.assertFalse(self.car.is_empty())
        self.assertEqual(
            [(self.item_name_one, 1), (self.item_name_two, 1)], self.car.list_items()
        )

    def test06_add_existed_item_sum(self):
        self.car.add_item(self.item_name_one, 2)
        self.car.add_item(self.item_name_one, 3)

        self.assertFalse(self.car.is_empty())
        self.assertEqual([(self.item_name_one, 5)], self.car.list_items())


if __name__ == "__main__":
    unittest.main()
