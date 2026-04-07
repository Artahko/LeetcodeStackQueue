"""Task 3"""

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

class FreqStack:

    def __init__(self):
        self.values = {} # All values and number of them in FreqStack
        self.group = {} # Groups by number of values in FreqStack
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val not in self.values:
            self.values[val] = 0

        self.values[val] += 1

        freq = self.values[val]

        # Add this value to new group
        if freq > self.max_freq:
            self.max_freq = freq

        if freq not in self.group:
            self.group[freq] = Stack()

        self.group[freq].push(val)

    def pop(self) -> int:
        # Take value from highest number group
        val = self.group[self.max_freq].pop()

        self.values[val] -= 1
        if self.values[val] == 0:
            del self.values[val]

        # Check if number group is empty
        if self.group[self.max_freq].is_empty():
            del self.group[self.max_freq]
            self.max_freq -= 1

        return val
