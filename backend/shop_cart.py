from unittest import TestCase
from typing import *


class ShopCart:

    def __init__(self) -> None:
        self.item = []
        self.catalog = dict()

    def initialize_with_catalog(self, catalog: dict) -> None:
        self.catalog = catalog
        return self

    @classmethod
    def with_catalog(cls, catalog: dict) -> None:
        return cls().initialize_with_catalog(catalog)

    def is_empty(self) -> bool:
        return len(self.item) == 0

    def add_item(self, name: str, amount: int) -> None:
        if self.catalog and not name in self.catalog:
            raise ItemNotInCatalog()
        self.item.append((name, amount))
        return self

    def contains_item(self, name: str, amount: int) -> bool:
        return (name, amount) in self.item

    def list_items(self) -> List[Tuple[str, int]]:
        return list(self.item)


class ItemNotInCatalog(Exception):
    pass
