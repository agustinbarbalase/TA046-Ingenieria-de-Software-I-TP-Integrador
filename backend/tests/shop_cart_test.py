import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.domain.shop_cart import ShopCart


class ShopCartTest(unittest.TestCase):

    def test01_new_cart_is_empty(self):
        car = ShopCart()
        self.assertTrue(car.is_empty())

    def test02_can_add_item_to_cart(self):
        car = ShopCart()
        new_item = ("cincuenta sombras de Alan key", 1)

        car.add_item(new_item[0], new_item[1])

        self.assertFalse(car.is_empty())
        self.assertTrue(car.contains_item(new_item[0]))

    def test03_can_add_multiple_items(self):
        car = ShopCart()

        new_item_one = ("cincuenta sombras de Alan key", 1)
        new_item_two = ("el secreto de su codigo encapsulado", 2)

        car.add_item(new_item_one[0], new_item_one[1])
        car.add_item(new_item_two[0], new_item_two[1])

        self.assertFalse(car.is_empty())
        self.assertTrue(car.contains_item(new_item_one[0]))
        self.assertTrue(car.contains_item(new_item_two[0]))

    def test04_add_non_existing_cart_in_catalog_raises_error(self):
        new_catalog = set()

        name_item_in_catalog = "cincuenta sombras de Alan key"
        name_item_random = "1984"

        new_catalog.add(name_item_in_catalog)

        car = ShopCart.with_catalog(new_catalog)

        with self.assertRaises(Exception) as context:
            car.add_item(name_item_random, 1)

        self.assertEqual(
            str(context.exception), ShopCart.item_not_in_catalog_message_error()
        )

    def test05_list_cart_items(self):
        car = ShopCart()

        new_item_one = ("cincuenta sombras de Alan key", 1)
        new_item_two = ("el secreto de su codigo encapsulado", 2)

        car.add_item(new_item_one[0], new_item_one[1])
        car.add_item(new_item_two[0], new_item_two[1])

        self.assertFalse(car.is_empty())
        self.assertEqual([new_item_one, new_item_two], car.list_items())

    def test06_add_existed_item_sum(self):
        car = ShopCart()

        new_item = "cincuenta sombras de Alan key"

        car.add_item(new_item, 2)
        car.add_item(new_item, 3)

        self.assertFalse(car.is_empty())
        self.assertEqual([(new_item, 5)], car.list_items())


if __name__ == "__main__":
    unittest.main()
