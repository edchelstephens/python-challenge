from node.node import Node

class LinkedList:
    """A list of linked nodes."""
    
    def __init__(self, items):
        """Construct linked nodes from 'items' iterable.
        
        If 'items' iterable is a string, then,
        only construct a single node list,
        containing the string value.
        """
        self.head = None
        
        if isinstance(items, str):
            self.head = Node(data=items)
        else:
            try: 
                for item in items:
                    self.head = self.insert(self.head, item)
            except TypeError:
                raise TypeError(f"Expected argument {items} to be an iterable")
    
    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return f"LinkedList(head={self.head})"

    def insert(self, head, item):
        """Inserts item at the last node of the linked list."""
        node = Node(item)

        if head is None:
            head = node
        else:
            tail = self.get_tail(head)
            tail.next = node

        return head
    
    def get_tail(self, head):
        """Get tail node of linked list from head."""
        try:
            if head is None or head.next is None:
                tail = head
            else:
                tail = self.get_tail(head.next)

            return tail
        except AttributeError:
            raise AttributeError("Object has no attribute next")

    def get_list(self, head):
        """Get the list of values from the linked list."""
        try:
            linked_list_list = []
            node = head
            while node is not None:
                linked_list_list.append(node.value)
                node = node.next

            return linked_list_list
        except TypeError as type_error:
            raise type_error
        except AttributeError as attribute_error:
            raise attribute_error

    def copy_list(self, head):
        """Return a copy of the list."""
        try:
            linked_list_items = self.get_list(head)
            list_copy = LinkedList(linked_list_items)
            
            return list_copy
        except AttributeError as attribute_error:
            raise attribute_error
        
    def reverse_list(self, head):
        """Reverse the linked list from head."""
        return head

    def sort_list(self, head):
        """Sort list by node values if values are sortable."""
        return head

    def is_empty(self, head):
        """Check if list head is pointing to an empty linked list."""
        return head is None

    def is_single_item_list(self, head):
        """Check if list only contains the head node."""
        try:
            return not self.is_empty(head) and head.next is None
        except AttributeError:
            raise AttributeError("Object has no attribute next")

    def is_homogenuous(self, head):
        """Check if list contains homogoneous values."""
        try:
            if self.is_empty(head):
                homogoneous = False
            elif self.is_single_item_list(head):
                homogoneous = True
            else:
                homogoneous = isinstance(head.next.value, type(head.value))
                if homogoneous and head.next is not None:
                    homogoneous = self.is_homogenuous(head.next)
            
            return homogoneous
        except TypeError as type_error:
            raise type_error