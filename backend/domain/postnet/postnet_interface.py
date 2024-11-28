from abc import abstractmethod
from utils.card import Card


class PostnetInterface:
    """Intialization"""

    def __init__(self):
        pass

    """Main protocol"""

    @abstractmethod
    def return_ticket(self, card: Card, amount: int):
        pass
