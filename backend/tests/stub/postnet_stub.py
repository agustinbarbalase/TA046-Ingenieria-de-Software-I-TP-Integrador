from domain.postnet.postnet_interface import PostnetInterface


class PostNetStub(PostnetInterface):
    def __init__(self):
        super().__init__()

    def return_ticket(self, cart, card):
        return "Sucessfully sell"
