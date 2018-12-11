class Node:
    def __init__(self, value, num_children):
        self.value = value
        self.children = [None]*num_children

class BinaryNode(Node):
    def __init__(self, value):
        super().__init__(value, 2)
        self.left = self.children[0]
        self.right = self.children[1]

class LinkedList():
    class ListNode(Node):
        def __init__(self, value):
            super().__init__(value, 1)
            self.next = self.children[0]

    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def __str__(self):
        elements = []
        curr = self.head
        while curr is not None:
            elements.append(curr.value)
            curr = curr.next
        return str(elements)

    def __repr__(self):
        return f"LinkedList({self.__str__()})"

    def insert(self, value, pos=None):
        self_len = self.__len__()
        if pos is None:
            pos = self_len
        if not isinstance(pos, int) or pos < 0:
            raise ValueError("position must be a non-negative integer")
        if pos > self_len:
            raise ValueError("position out of range")

        new_node = self.ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            if pos == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                curr = self.head
                while pos > 1:
                    pos -= 1
                    curr = curr.next
                new_node.next = curr.next
                curr.next = new_node

    def reverse(self):
        prev_node = None
        curr = self.head
        next_node = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node
