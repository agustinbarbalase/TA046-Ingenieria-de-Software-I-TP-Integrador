from typing import *

from utils.bag import Bag


class ShopCart:
    """Instance creation - class"""

    @classmethod
    def with_catalog(cls, catalog: dict[str, str]):
        return cls(catalog)

    """Error messages - class"""

    @classmethod
    def item_not_in_catalog_message_error(cls):
        return "Item not in catalog"

    """Initialization"""

    def __init__(self, catalog: dict[str, str]):
        self.item: Bag = Bag.new()
        self.catalog: dict[str, str] = catalog

    """Main protocol"""

    def is_empty(self) -> bool:
        return self.item.is_empty()

    def add_item(self, name: str, amount: int):
        if not name in self.catalog:
            raise Exception(ShopCart.item_not_in_catalog_message_error())
        self.item.add_with_amount(name, amount)
        return self

    def contains_item(self, name: str) -> bool:
        return self.item.contains(name)

    def list_items(self) -> List[Tuple[str, int]]:
        return list(self.item.list_items())
