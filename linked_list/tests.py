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

    def linked_list_strs(self):
        return self.linked_list.__str__(), str(self.linked_list)
    
    def linked_list_reprs(self):
        return self.linked_list.__repr__(), repr(self.linked_list)

    # Tests
    def test_instance(self):
        self.assertIsInstance(self.linked_list, LinkedList)
        self.assertIsInstance(self.head, Node)

    def test_str(self):
        from_method, from_str = self.linked_list_strs()
        expected = "[1][] -> [2][] -> [3][] -> [4][] -> None"       
        self.assertEqual(from_method, expected) 
        self.assertEqual(from_str, expected)

    def test_repr(self):
        from_method, from_repr = self.linked_list_reprs()
        excpected="LinkedList(head=[1][] -> [2][] -> [3][] -> [4][] -> None)"

        self.assertEqual(from_method, excpected)
        self.assertEqual(from_repr, excpected)

    def test_list_is_not_empty(self):
        self.assertFalse(self.linked_list.is_empty(self.head))

    def test_insert(self):
        self.insert(data=5)
        self.assertIn(5, self.linked_list.get_list(self.head))

    def test_get_tail(self):
        tail = self.linked_list.get_tail(self.head)

        self.assertIsNotNone(tail)
        self.assertIsInstance(tail, Node)
        self.assertEqual(self.items[-1], tail.value)
        self.assertIsNone(tail.next)

    def test_get_list(self):
        self.assertEqual(self.items, self.linked_list.get_list(self.head))

    def test_copy_list(self):
        list_copy_head = self.linked_list.copy_list(self.head)
        self.assertEqual(self.items, self.linked_list.get_list(list_copy_head))
        self.assertIsNot(self.head, list_copy_head)

    def test_reverse_list(self):
        items_copy = self.items[:]
        items_copy.reverse()
        reversed_list_head = self.linked_list.reverse_list(self.head)

        self.assertEqual(items_copy, self.linked_list.get_list(reversed_list_head))

    def test_sort(self):
        unsorted_list = [5, 0, 1]
        sorted_list = [0, 1, 5]

        unsorted_linked_list = LinkedList(unsorted_list)
        sorted_list_head = unsorted_linked_list.sort_list(unsorted_linked_list.head)
        sorted_linked_list_items = self.linked_list.get_list(sorted_list_head)
        
        self.assertEqual(sorted_list, sorted_linked_list_items)

    def test_is_homogenous(self):
        self.assertTrue(self.linked_list.is_homogenuous(self.head))
        self.insert(data="A")
        self.assertFalse(self.linked_list.is_homogenuous(self.head))

    def test_is_not_empty(self):
        self.assertFalse(self.linked_list.is_empty(self.head))

    def test_is_single_item_list(self):
        linked_list = LinkedList("single list")
        self.assertTrue(linked_list.is_single_item_list(linked_list.head))
