from abc import abstractmethod


class XYZ:

    def __init__(self):
        pass

    @abstractmethod
    def return_ticket(self, cart, card):
        pass


class XYZStub(XYZ):

    def __init__(self):
        super().__init__()

    def return_ticket(self, cart, card):
        return "Sucessfully sell"
