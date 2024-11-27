from domain.postnet.postnet_interface import PostnetInterface
from utils.card import Card


class PostnetStub(PostnetInterface):

    def __init__(self):
        pass

    @classmethod
    def reject_card_message_error(cls):
        return "Rejected card"

    def return_ticket(self, card: Card, amount: int):
        if card.get_number_card() == 6969696969696969:
            raise Exception(PostnetStub.reject_card_message_error())
        return "1234"
