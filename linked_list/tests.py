import unittest

from .linked_list import LinkedList

class LinkedListTestCase(unittest.TestCase):

    def setUp(self):
        self.items = [1,2,3,4]
        self.linked_list = LinkedList(self.items)
        self.head = self.linked_list.head
       

    def test_list_is_not_empty(self):
        self.assertFalse(self.linked_list.is_empty(self.head))