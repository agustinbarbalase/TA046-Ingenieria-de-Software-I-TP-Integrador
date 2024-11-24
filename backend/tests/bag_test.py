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
        bag = Bag.new()
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

    def test06_add_with_amount(self):
        self.bag.add_with_amount(self.book_item, 5)
        self.assertEqual(self.bag.amount_of(self.book_item), 5)

    def test07_list_items(self):
        self.bag.add(self.book_item)
        self.bag.add_with_amount(self.knife_item, 3)
        self.assertEqual(
            [(self.book_item, 1), (self.knife_item, 3)], self.bag.list_items()
        )
