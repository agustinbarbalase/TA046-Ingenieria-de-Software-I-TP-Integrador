from datetime import datetime, timedelta
import sys
import os
import unittest

from utils.clock import Clock
from domain.user_session import UserSession

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class UserSessionTest(unittest.TestCase):

    def test01_usser_session_is_not_expired(self):
        clock = Clock(lambda: datetime(2023, 1, 1, 0, 0), lambda: timedelta(seconds=10))
        user_session = UserSession(catalog={}, expiration_date=clock.limit_date())
        self.assertFalse(user_session.is_expired(clock.current()))

    def test02_usser_session_is_expired(self):
        clock = Clock(lambda: datetime(2023, 1, 1, 0, 0), lambda: timedelta(seconds=10))
        user_session = UserSession(catalog={}, expiration_date=clock.limit_date())
        self.assertTrue(
            user_session.is_expired(clock.current() + timedelta(seconds=11))
        )
