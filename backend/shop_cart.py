from unittest import TestCase
from typing import *


class ShopCart:

    def __init__(self) -> None:
        self.item: dict[str, int] = dict()
        self.catalog: dict[str, bool] = dict()

    def initialize_with_catalog(self, catalog: dict):
        self.catalog = catalog
        return self

    @classmethod
    def with_catalog(cls, catalog: dict[str, bool]):
        return cls().initialize_with_catalog(catalog)

    def is_empty(self) -> bool:
        return len(self.item) == 0

    def add_item(self, name: str, amount: int):
        if self.catalog and not name in self.catalog:
            raise ItemNotInCatalog()

        if self.contains_item(name):
            self.item[name] += amount
        else:
            self.item[name] = amount

        return self

    def contains_item(self, name: str) -> bool:
        return name in self.item

    def list_items(self) -> List[Tuple[str, int]]:
        return list(self.item.items())


class ItemNotInCatalog(Exception):
    pass
