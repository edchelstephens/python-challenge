import unittest
from .node import Node

class NodeTestCase(unittest.TestCase):

    def setUp(self):
        self.data1 = 1
        self.data2 = 2

        self.node = Node(self.data1)
        self.next_node = Node(self.data2)
        self.node.next = self.next_node

    def test_instance(self):
        self.assertIsInstance(self.node, Node)
        
    def test_value(self):
        self.assertEqual(self.node.value, self.data1)
    
    def test_next(self):
        self.assertIs(self.node.next, self.next_node)

    def test_next_none(self):
        self.assertIsNone(self.next_node.next)

    def test_str(self):
        node_str_from_method = self.node.__str__()
        node_str = str(self.node)
        node_str_expected = f"[{self.data1}][] -> {self.node.next}"
        
        self.assertEqual(node_str_from_method, node_str_expected)
        self.assertEqual(node_str, node_str_expected)
        

    def test_repr(self):
        node_repr_from_method = self.node.__repr__()
        node_repr = repr(self.node)
        node_repr_expected = f"Node(value={self.node.value}, next={self.node.next})"

        self.assertEqual(node_repr_from_method, node_repr_expected)
        self.assertEqual(node_repr, node_repr_expected)