#!/usr/bin/env python
#################################################
""" queue.py
# # Queue(FIFO) Implementation
#   Supports:
#      - Push.
#      - Pop.
#      - Peek.
"""
#################################################
# ###  Author: Samyuel Danyo
# ###  Date: 02/06/2020
# ###  Last Edit: 02/06/2020
##################################################
# Array Implementation
##################################################
class Queue:
    """Queue(FIFO) array implementation."""
    def __init__(self, cap):
        self.cap = cap
        self.data = [None]*cap
        # Popping at the head
        self.head = -1
        # Pushing at the tail
        self.tail = -1

    def __str__(self):
        return str(self.data)

    def capacity(self):
        """Get the stack capacity."""
        return self.cap

    def is_empty(self):
        """True if the queue is empty."""
        return self.head == self.tail == -1

    def size(self):
        """Get the stack's current size"""
        if self.is_empty():
            return 0
        if self.tail > self.head:
            return self.tail - self.head + 1
        return self.capacity() + self.tail - self.head + 1

    def is_full(self):
        """True if the queue is full."""
        return self.size() == self.capacity()

    def push(self, value):
        """Push a value into the queue."""
        if self.is_full():
            print("ERROR:: Queue Overflow!")
            return None
        self.tail = (self.tail + 1) % self.capacity()
        if self.head == -1:
            self.head += 1
        self.data[self.tail] = value
        return True

    def pop(self):
        """Pop a value off the queue."""
        if self.is_empty():
            print("ERROR:: Queue Underflow!")
            return None
        value = self.data[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity()
        return value

    def peek(self):
        """See the end(oldest) value in the queue."""
        if self.is_empty():
            print("WARNING:: Queue Empty!")
            return None
        return self.data[self.head]

##################################################
# List Implementation
##################################################
class QueueNode:
    """Node for a queue implementation."""
    def __init__(self, data):
        self.data = data
        self.next = None

class ListQueue:
    """Queue(FIFO) list implementation."""
    def __init__(self, cap):
        self.cap = cap
        self.num_els = 0
        # Popping at the head
        self.head = None
        # Pushing at the tail
        self.tail = None

    def __str__(self):
        data = []
        node = self.head
        while node:
            data.append(str(node.data))
            node = node.next
        return "[" + ", ".join(data) + "]"

    def capacity(self):
        """Get the stack capacity."""
        return self.cap

    def size(self):
        """Get the stack's current size"""
        return self.num_els

    def is_empty(self):
        """True if the queue is empty."""
        return self.size() == 0

    def is_full(self):
        """True if the queue is full."""
        return self.size() == self.capacity()

    def push(self, value):
        """Push a value into the queue."""
        if self.is_full():
            print("ERROR:: Queue Overflow!")
            return None
        data = QueueNode(value)
        if self.num_els > 0:
            self.tail.next = data
            self.tail = self.tail.next
        else:
            self.tail = data
            self.head = self.tail
        self.num_els += 1
        return True

    def pop(self):
        """Pop a value off the queue."""
        if self.is_empty():
            print("ERROR:: Queue Underflow!")
            return None
        value = self.head.data
        self.head = self.head.next
        self.num_els -= 1
        if self.num_els == 0:
            self.tail = None
        return value

    def peek(self):
        """See the end(oldest) value in the queue."""
        if self.is_empty():
            print("WARNING:: Queue Empty!")
            return None
        return self.head.data
