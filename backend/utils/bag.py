class Bag:
    """Instance creation - class"""

    @classmethod
    def new(cls):
        return cls()

    """Initialization"""

    def __init__(self):
        self.items = dict()

    """Main protocol"""

    def is_empty(self):
        return len(self.items) == 0

    def add(self, item: str) -> None:
        self.items[item] = self.items.get(item, 0) + 1

    def contains(self, item: str) -> bool:
        return item in self.items

    def amount_of(self, item: str) -> int:
        return self.items.get(item, 0)

    def add_with_amount(self, item: str, amount: int) -> None:
        self.items[item] = self.items.get(item, 0) + amount

    def list_items(self) -> list:
        return list(self.items.items())

    def __len__(self):
        return len(self.items)

    def add_list(self, items: list):
        for item in items:
            self.add_with_amount(item[0], item[1])
