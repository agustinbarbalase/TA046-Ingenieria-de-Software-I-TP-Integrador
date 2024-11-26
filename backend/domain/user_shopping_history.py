from utils.bag import Bag


class UserShoppingHistory:

    @classmethod
    def new(cls):
        return cls()

    def __init__(self):
        self.books: Bag = Bag.new()
        self.total_amount: int = 0

    def register_new_sale(self, other):
        self.books.merge(other.books)
        self.total_amount += other.total_amount
