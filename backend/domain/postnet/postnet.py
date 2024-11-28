import random
from utils.card import Card
from domain.postnet.postnet_interface import PostnetInterface


class Postnet(PostnetInterface):
    """Instance creation - class"""

    @classmethod
    def new(cls):
        return cls()

    """Error message - class"""

    @classmethod
    def reject_card_message_error(cls):
        return "Rejected card"

    """Initialization"""

    def __init__(self):
        pass

    """Main protocol"""

    def return_ticket(self, card: Card, amount: int):
        if card.get_number_card() == 6969696969696969:
            raise Exception(Postnet.reject_card_message_error())
        return random.randint(10000, 99999)
