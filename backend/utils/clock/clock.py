from datetime import datetime, timedelta
from utils.clock.clock_interface import ClockInterface


class Clock(ClockInterface):
    """Instance creation - class"""

    @classmethod
    def with_current_time(cls, current_time):
        return cls(current_time)

    @classmethod
    def with_time_now(cls):
        return cls(datetime.now())

    """Initialization"""

    def __init__(self, current_time):
        self.current_time = current_time

    """Main protocol"""

    def is_later_that(self, other):
        return datetime.now() > other

    def step_seconds(self, seconds: int):
        self.current_time = datetime.now() + timedelta(seconds=seconds)

    def step_to_current_time(self):
        self.current_time = datetime.now()

    def later_date_to_seconds(self, seconds):
        return datetime.now() + timedelta(seconds=seconds)
