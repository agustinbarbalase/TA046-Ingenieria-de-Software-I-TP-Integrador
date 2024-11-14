from abc import abstractmethod


class PostnetInterface:

    def __init__(self):
        pass

    @abstractmethod
    def return_ticket(self, cart, card):
        pass
