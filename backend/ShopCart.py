from unittest import *
from typing import *

class ShopCart:

    def __init__(self) -> None:
        self.item = []
        self.catalog = dict()

    def initialize_with_catalog(self, catalog: dict) -> Self:
        self.catalog = catalog
        return self

    @classmethod
    def with_catalog(cls, catalog: dict) -> Self:
        return cls().initialize_with_catalog(catalog)
    
    def is_empty(self) -> bool:
        return len(self.item) == 0
    
    def add_item(self, name: str, amount: int) -> Self:
        if self.catalog:
            if not name in self.catalog:
                raise ItemNotInCatalog
        self.item.append((name, amount))
        return self         

    def contains_item(self, name: str, amount: int) -> bool:
        return (name, amount) in self.item
    
    def list_items(self) -> List[Tuple[str, int]]:
        return list(self.item)

class ItemNotInCatalog(Exception):
    pass

class ShopCartTest(TestCase):
    
    def test01_new_cart_is_empty(self):
        car = ShopCart()
        self.assertTrue(car.is_empty())

    def test02_can_add_item_to_cart(self):
        car = ShopCart()
        new_item = ("cincuenta sombras de Alan key", 1)
        
        car.add_item(new_item[0], new_item[1])

        self.assertFalse(car.is_empty())
        self.assertTrue(car.contains_item(new_item[0], new_item[1]))

    def test03_can_add_multiple_items(self):
        car = ShopCart()
        
        new_item_one = ("cincuenta sombras de Alan key", 1)
        new_item_two = ("el secreto de su codigo encapsulado", 2)

        car.add_item(new_item_one[0], new_item_one[1])
        car.add_item(new_item_two[0], new_item_two[1])

        self.assertFalse(car.is_empty())
        self.assertTrue(car.contains_item(new_item_one[0], new_item_one[1]))
        self.assertTrue(car.contains_item(new_item_two[0], new_item_two[1]))

    def test04(self):
        pass

    def test05_add_non_existing_cart_in_catalog_raises_error(self):
        new_catalog = set()

        name_item_in_catalog = "cincuenta sombras de Alan key"
        name_item_random = "1984"

        new_catalog.add(name_item_in_catalog)

        car = ShopCart.with_catalog(new_catalog)

        with self.assertRaises(ItemNotInCatalog):
            car.add_item(name_item_random, 1)

    
    def test06_list_cart_items(self):
        car = ShopCart()
        
        new_item_one = ("cincuenta sombras de Alan key", 1)
        new_item_two = ("el secreto de su codigo encapsulado", 2)

        car.add_item(new_item_one[0], new_item_one[1])
        car.add_item(new_item_two[0], new_item_two[1])

        self.assertFalse(car.is_empty())
        self.assertEqual([new_item_one, new_item_two], car.list_items())        
