class Node:
    def __init__(self, value, num_children):
        self.value = value
        self.children = [None]*num_children

class LinkedList:
    class ListNode(Node):
        def __init__(self, value):
            super().__init__(value, 1)

        @property
        def next(self):
            return self.children[0]

        @next.setter
        def next(self, node):
            self.children[0] = node

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

class BinaryTree:
    class BinaryNode(Node):
        def __init__(self, value):
            super().__init__(value, 2)

        @property
        def left(self):
            return self.children[0]

        @left.setter
        def left(self, node):
            self.children[0] = node

        @property
        def right(self):
            return self.children[1]

        @right.setter
        def right(self, node):
            self.children[1] = node

    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.traverse("in"))

    def __repr__(self):
        return f"BinaryTree({self.__str__()})"

    def insert(self, value):
        new_node = self.BinaryNode(value)
        if self.root is None:
            self.root = new_node
        else:
            to_visit = [self.root]
            while True:
                curr = to_visit.pop(0)
                if curr.left is None:
                    curr.left = new_node
                    return
                if curr.right is None:
                    curr.right = new_node
                    return
                to_visit.extend(curr.children)

    def contains(self, value):
        if self.root is None:
            return False
        to_visit = [self.root]
        while to_visit:
            curr = to_visit.pop()
            if curr.value == value:
                return True
            to_visit.extend(reversed([child for child in curr.children if child is not None]))
        return False

    def traverse(self, order):
        if order == "pre":
            def _traverse(elements, curr):
                elements.append(curr.value)
                if curr.left is not None:
                    _traverse(elements, curr.left)
                if curr.right is not None:
                    _traverse(elements, curr.right)
        elif order == "in":
            def _traverse(elements, curr):
                if curr.left is not None:
                    _traverse(elements, curr.left)
                elements.append(curr.value)
                if curr.right is not None:
                    _traverse(elements, curr.right)
        elif order == "post":
            def _traverse(elements, curr):
                if curr.left is not None:
                    _traverse(elements, curr.left)
                if curr.right is not None:
                    _traverse(elements, curr.right)
                elements.append(curr.value)
        else:
            raise ValueError("order must be one of 'pre', 'in', or 'post'")
        elements = []
        if self.root is not None:
            _traverse(elements, self.root)
        return elements
