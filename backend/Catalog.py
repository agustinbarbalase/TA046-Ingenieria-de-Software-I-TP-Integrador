from unittest import *
from typing import *

### DEjo por si se complejiza la implementacion 

class Catalog:

    ## Esto no es literalmente un wrapper de un diccionario?

    def __init__(self):
        self.item = {}

    def has_item(self, name: str) -> bool:
        return name in self.item
    
    def add_item(self, name: str) -> None:
        self.item[name] = True

class CatalogTest(TestCase):

    def test01(self):
        new_catalog = Catalog()
        self.assertFalse(new_catalog.has_item("1984"))

    def test02(self):
        new_catalog = Catalog()

        new_catalog.add_item("1984")

        self.assertTrue(new_catalog.has_item("1984"))

    def test03(self):
        new_catalog = Catalog()

        new_catalog.add_item("1984")
        new_catalog.add_item("Rebelion en la granja")

        self.assertTrue(new_catalog.has_item("1984"))
        self.assertTrue(new_catalog.has_item("Rebelion en la granja"))