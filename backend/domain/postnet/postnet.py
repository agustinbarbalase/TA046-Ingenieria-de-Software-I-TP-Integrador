from domain.postnet.postnet_interface import PostnetInterface


class Postnet(PostnetInterface):
    def __init__(self):
        super().__init__()

    def return_ticket(self, cart, card):
        return "1234"
