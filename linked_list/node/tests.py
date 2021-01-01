import unittest

from .node import Node

class NodeTestCase(unittest.TestCase):

    def setUp(self):
        self.data = "data"
        self.node = Node(self.data)

    # Helper Functions
    def add_next_node(self, data):
        self.next_node_data = data
        self.next_node = Node(self.next_node_data)
        self.node.next = self.next_node
        
    def node_strs(self):
        return self.node.__str__(), str(self.node)

    def node_reprs(self):
        return self.node.__repr__(), repr(self.node)

    # Tests
    def test_instance(self):
        self.assertIsInstance(self.node, Node)

    def test_value(self):
        self.assertEqual(self.node.value, self.data)
    
    def test_single_list_element_next_none(self):        
        self.assertIsNone(self.node.next)

    def test_next(self):
        self.add_next_node(data="next_data")

        self.assertIsNotNone(self.node.next)
        self.assertIsInstance(self.node.next, Node)
        self.assertIs(self.node.next, self.next_node)

    def test_single_node_str(self):
        from_method, from_str = self.node_strs()
        expected = f"[{self.data}][] -> None"
        
        self.assertEqual(from_method, expected)
        self.assertEqual(from_str, expected)
    
    def test_multi_node_str(self):
        self.add_next_node(data="next_data")

        from_method, from_str = self.node_strs()
        expected = f"[{self.data}][] -> [{self.next_node_data}][] -> None"

        self.assertEqual(from_method, expected)
        self.assertEqual(from_str, expected)

    def test_single_node_repr(self):
        from_method, from_repr = self.node_reprs()
        expected = f"Node(value={self.data}, next=None)"
        
        self.assertEqual(from_method, expected)
        self.assertEqual(from_repr, expected)
    
    def test_multi_node_repr(self):
        self.add_next_node(data="next_data")
        from_method, from_repr = self.node_reprs()

        expected = f"Node(value={self.data}, next=[{self.next_node_data}][] -> None)"

        self.assertEqual(from_method, expected)
        self.assertEqual(from_repr, expected)
        
