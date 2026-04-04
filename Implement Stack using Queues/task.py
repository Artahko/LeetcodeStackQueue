"""Task 2"""

class Node:
    """Class representing a node in Linked List"""

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    """Class implementing a queue using Linked List"""

    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    def add(self, val):
        """Pushes value to the rear of a linked list"""
        # Checks if queue is empty, than initializes it
        if self.head is None:
            self.head = Node(val)
            self.rear = self.head
            self.size += 1

            return

        self.size += 1

        new_node = Node(val)
        self.rear.next = new_node
        self.rear = new_node

    def pop(self):
        """Pops value from a head and returns it"""
        val = self.head.val
        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.rear = None

        return val

    def peek(self):
        """Returns value of a head"""
        return self.head.val

    def is_empty(self):
        """Returns True is queue is empty"""
        return self.head is None

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        while self.q1.size != 0:
            self.q2.add(self.q1.pop())

        self.q1.add(x)

        while self.q2.size != 0:
            self.q1.add(self.q2.pop())

    def pop(self) -> int:
        return self.q1.pop()

    def top(self) -> int:
        return self.q1.head.val

    def empty(self) -> bool:
        return self.q1.head is None
