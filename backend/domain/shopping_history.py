from domain.user_shopping_history import UserShoppingHistory
from domain.shop_cart import ShopCart
from copy import copy


class ShopingHistory:
    """Instance creation - class"""

    @classmethod
    def new(cls):
        return cls()

    """Initialization"""

    def __init__(self):
        self.users_shopping_history: dict[str, UserShoppingHistory] = dict()

    """Main protocol"""

    def register_purcharse(self, user_id, cart: ShopCart):
        self.users_shopping_history[user_id] = self.users_shopping_history.get(
            user_id, UserShoppingHistory.new()
        )

    def get_user_history(self, user_id):
        return copy(self.users_shopping_history[user_id])
