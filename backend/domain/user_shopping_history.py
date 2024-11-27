from utils.bag import Bag
from domain.shop_cart import ShopCart


class UserShoppingHistory:
    """Instance creation - class"""

    @classmethod
    def new(cls):
        return cls()

    """Initialization"""

    def __init__(self):
        self.books: Bag = Bag.new()
        self.total_amount: int = 0
        self.total_successfull_transaction: int = 0

    """visitor"""

    def visit_items(self, items: Bag):
        self.books.merge(items)

    """Main protocol"""

    def register_purcharse_for_user(self, cart: ShopCart):
        cart.accept_visitor(self)
        self.total_amount += cart.total_amount()
        self.total_successfull_transaction += 1

    def history(self):
        if self.total_successfull_transaction < 2:
            return (0, [])
        return (float("%.2f" % self.total_amount), self.books.list_items())
