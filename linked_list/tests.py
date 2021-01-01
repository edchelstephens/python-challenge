import unittest

from .linked_list import LinkedList
from .node.node import Node

class LinkedListTestCase(unittest.TestCase):

    def setUp(self):
        self.items = [1,2,3,4]
        self.linked_list = LinkedList(self.items)
        self.head = self.linked_list.head
    
    # Helper Functions
    def insert(self, data):
        self.insert_data = data
        self.linked_list.insert(self.head, self.insert_data)

    # Tests
    def test_instance(self):
        self.assertIsInstance(self.linked_list, LinkedList)
        self.assertIsInstance(self.head, Node)

    def test_list_is_not_empty(self):
        self.assertFalse(self.linked_list.is_empty(self.head))
    
    def test_insert(self):
        self.insert(data=5)
        self.assertIn(5, self.linked_list.get_list(self.head))
