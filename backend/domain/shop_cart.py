from typing import *


class ShopCart:

    def __init__(self, catalog: set[str]) -> None:
        self.item: dict[str, int] = dict()
        self.catalog: set[str] = catalog

    @classmethod
    def item_not_in_catalog_message_error(cls):
        return "Item not in catalog"

    def is_empty(self) -> bool:
        return len(self.item) == 0

    def add_item(self, name: str, amount: int):
        if not name in self.catalog:
            raise Exception(ShopCart.item_not_in_catalog_message_error())

        if self.contains_item(name):
            self.item[name] += amount
        else:
            self.item[name] = amount

        return self

    def contains_item(self, name: str) -> bool:
        return name in self.item

    def list_items(self) -> List[Tuple[str, int]]:
        return list(self.item.items())
