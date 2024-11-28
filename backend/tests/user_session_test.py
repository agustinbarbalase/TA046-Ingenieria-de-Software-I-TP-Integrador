from datetime import datetime, timedelta
import sys
import os
import unittest

from tests.stub.clock_stub import ClockStub
from domain.user_session import UserSession

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class UserSessionTest(unittest.TestCase):

    def setUp(self):
        self.current_time = datetime(2018, 12, 9, 0, 0)
        self.clock = ClockStub.with_current_time(self.current_time)

    def test01_usser_session_is_not_expired(self):
        user_session = UserSession.with_catalog_and_expiration_date(
            catalog={}, expiration_date=self.clock.later_date_to_seconds(30)
        )

        self.clock.step_seconds(29)

        self.assertFalse(user_session.is_expired(self.clock))

    def test02_usser_session_is_expired(self):
        user_session = UserSession.with_catalog_and_expiration_date(
            catalog={}, expiration_date=self.clock.later_date_to_seconds(30)
        )

        self.clock.step_seconds(30)

        self.assertFalse(user_session.is_expired(self.clock))
