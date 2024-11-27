from abc import abstractmethod


class ClockInterface:
    """Initialization"""

    @abstractmethod
    def __init__(self, current_time):
        pass

    """Main protocol"""

    @abstractmethod
    def is_later_that(self, other):
        pass

    @abstractmethod
    def step_seconds(self, seconds: int):
        pass

    @abstractmethod
    def step_to_current_time(self):
        pass

    @abstractmethod
    def later_date_to_seconds(self, seconds):
        pass
