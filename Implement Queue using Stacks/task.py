"""Task 1"""

class Node:
    """Class representing a node in Linked List"""

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    """Class implementing a stack using Linked List"""

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        """Pushes value to the head of a linked list"""
        self.head = Node(val, self.head)
        self.size += 1

    def pop(self):
        """Pops value from a head and returns it"""
        self.size -= 1

        val = self.head.val
        self.head = self.head.next

        return val

    def peek(self):
        """Returns value of a head"""
        return self.head.val

    def is_empty(self):
        """Returns True is stack is empty"""
        return self.head is None

class MyQueue:

    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()

    def push(self, x: int) -> None:
        while self.st1.size != 0:
            self.st2.push(self.st1.pop())

        self.st1.push(x)

        while self.st2.size != 0:
            self.st1.push(self.st2.pop())

    def pop(self) -> int:
        return self.st1.pop()


    def peek(self) -> int:
        return self.st1.head.val


    def empty(self) -> bool:
        return self.st1.head is None
