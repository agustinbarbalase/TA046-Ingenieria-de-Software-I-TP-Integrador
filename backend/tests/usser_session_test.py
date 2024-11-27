from datetime import datetime, timedelta
import sys
import os
import unittest

from utils.clock import Clock
from domain.user_session import UserSession

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ClockTest(unittest.TestCase):

    # def test01_usser_session_is_expired(self):
    #     clock = Clock(lambda: datetime(2023, 1, 1, 0, 0), lambda: timedelta(seconds=10))
    #     user_session = UserSession(
    #         catalog={}, expiration_date=datetime(2023, 1, 1, 0, 0, 5)
    #     )
    #     self.assertTrue(user_session.is_expired(clock.current()))

    pass
