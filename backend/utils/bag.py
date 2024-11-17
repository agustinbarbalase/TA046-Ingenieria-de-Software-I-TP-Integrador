class Bag:

    def __init__(self):
        self.items = dict()

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
