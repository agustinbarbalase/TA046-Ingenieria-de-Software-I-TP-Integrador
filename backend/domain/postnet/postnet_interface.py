from abc import abstractmethod
from utils.card import Card


class PostnetInterface:

    def __init__(self):
        pass

    @abstractmethod
    def return_ticket(self, card: Card, amount: int):
        pass
