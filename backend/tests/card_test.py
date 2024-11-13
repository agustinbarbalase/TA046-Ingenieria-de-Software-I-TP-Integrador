import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.card import Card
import sys
import os
import unittest
from utils.gregorian_month_of_year import GregorianMonthOfYear


class CardTest(unittest.TestCase):

    def setUp(self):
        self.number = 1234567890123456
        self.month = 12
        self.year = 2025
        self.gregorian_month_of_year = GregorianMonthOfYear(self.month, self.year)
