from domain.postnet.postnet_interface import PostnetInterface
from utils.card import Card


class Postnet(PostnetInterface):

    def __init__(self):
        pass

    def return_ticket(self, card: Card, amount: int):
        return "1234"
