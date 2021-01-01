class Node:
    """A node with value and pointer to next node."""

    def __init__(self, data):
        self.value = data
        self.next = None
    
    def __str__(self):
        return f"[{self.value}][] -> {self.next}"
    
    def __repr__(self):
        return f"Node(value={self.value}, next={self.next})"
