from domain.user_shopping_history import UserShoppingHistory
from domain.shop_cart import ShopCart
from copy import copy


class ShopingHistoryBook:
    """Instance creation - class"""

    @classmethod
    def new(cls):
        return cls()

    """"Error messages - class"""

    @classmethod
    def invalid_user_message_error(cls):
        return "Invalid user dlasdlsad"

    """Initialization"""

    def __init__(self):
        self.users_shopping_history: dict[str, UserShoppingHistory] = dict()

    """Main protocol"""

    def register_purcharse(self, user_id, cart: ShopCart):
        self.users_shopping_history[user_id] = self.users_shopping_history.get(
            user_id, UserShoppingHistory()
        )
        self.users_shopping_history[user_id].register_purcharse_for_user(cart)

    def add_user(self, user_id):
        self.users_shopping_history[user_id] = UserShoppingHistory()

    def history_for_user(self, user_id):
        shopping_history = self.users_shopping_history.get(user_id, None)
        if shopping_history is None:
            raise Exception(ShopingHistoryBook.invalid_user_message_error())
        return shopping_history
