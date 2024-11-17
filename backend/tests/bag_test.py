import sys
import os
import unittest

from utils.bag import Bag

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class BagTest(unittest.TestCase):

    def setUp(self):
        self.bag = Bag()
        self.book_item = "book"
        self.knife_item = "knife"

    def test01_bag_is_empty(self):
        bag = Bag()
        self.assertTrue(bag.is_empty())

    def test02_bag_can_add_item(self):
        self.bag.add(self.book_item)
        self.assertFalse(self.bag.is_empty())
        self.assertTrue(self.bag.contains(self.book_item))

    def test03_bag_does_not_contains_item(self):
        self.bag.add(self.book_item)
        self.assertFalse(self.bag.contains(self.knife_item))

    def test04_bag_returns_items_amount(self):
        self.bag.add(self.book_item)
        self.assertEqual(self.bag.amount_of(self.book_item), 1)

    def test05_add_repeted_items_counts(self):
        self.bag.add(self.book_item)
        self.bag.add(self.book_item)
        self.assertEqual(self.bag.amount_of(self.book_item), 2)
