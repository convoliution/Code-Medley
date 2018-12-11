class Node:
    def __init__(self, value, num_children):
        self.value = value
        self.children = [None]*num_children

class ListNode(Node):
    def __init__(self, value):
        super().__init__(value, 1)
        self.next = self.children[0]

class BinaryNode(Node):
    def __init__(self, value):
        super().__init__(value, 2)
        self.left = self.children[0]
        self.right = self.children[1]
