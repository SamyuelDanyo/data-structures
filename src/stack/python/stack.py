#!/usr/bin/env python
#################################################
""" stack.py
# # Stack(LIFO) Implementation
#   Supports:
#      - Push.
#      - Pop.
#      - Peek.
#      - Delete_mid.
"""
#################################################
# ###  Author: Samyuel Danyo
# ###  Date: 02/06/2020
# ###  Last Edit: 02/06/2020
##################################################
# Array Implementation
##################################################
class Stack:
    """Stack(LIFO) array implementation."""
    def __init__(self, cap):
        self.cap = cap
        self.data = [None]*cap
        self.head = 0

    def __str__(self):
        return str(self.data)

    def capacity(self):
        """Get the stack capacity."""
        return self.cap

    def size(self):
        """Get the stack's current size"""
        return self.head

    def is_empty(self):
        """True if the stack is empty."""
        return self.head == 0

    def is_full(self):
        """True if the stack is full"""
        return self.size() == self.capacity()

    def push(self, value):
        """Push a value to the stack."""
        if self.is_full():
            print("ERROR:: Stack Overflow!!")
            return None
        self.data[self.head] = value
        self.head += 1
        return True

    def pop(self):
        """Pop a value off the stack."""
        if self.is_empty():
            print("ERROR: Stack Underflow!")
            return None
        self.head -= 1
        return self.data[self.head]

    def peek(self):
        """See the top(newest) value on the stack."""
        if self.is_empty():
            print("WARNING: Empty Stack!")
            return None
        return self.data[self.head-1]

    def delete_mid(self):
        """Delete the middle element of the stack."""
        size = self.size()
        if size == 0:
            return None
        mid = size//2
        temp = Stack(mid)
        for _ in range(mid):
            temp.push(self.pop())
        self.pop()
        for _ in range(mid):
            self.push(temp.pop())
        return True

class StackNode:
    """Node for a stack implementation."""
    def __init__(self, data):
        self.data = data
        self.next = None

##################################################
# List Implementation
##################################################
class ListStack:
    """Stack(LIFO) list implementation."""
    def __init__(self, cap):
        self.cap = cap
        self.num_els = 0
        self.head = None

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
        """True if the stack is empty."""
        return self.size() == 0

    def is_full(self):
        """True if the stack is full"""
        return self.size() == self.capacity()

    def push(self, value):
        """Push a value to the stack."""
        if self.is_full():
            print("ERROR:: Stack Overflow!!")
            return None
        data = StackNode(value)
        data.next = self.head
        self.head = data
        self.num_els += 1
        return True

    def pop(self):
        """Pop a value off the stack."""
        if self.is_empty():
            print("ERROR: Stack Underflow!")
            return None
        value = self.head.data
        self.head = self.head.next
        self.num_els -= 1
        return value

    def peek(self):
        """See the top(newest) value on the stack."""
        if self.is_empty():
            print("WARNING: Empty Stack!")
            return None
        return self.head.data

    def delete_mid(self):
        """Delete the middle element of the stack."""
        size = self.size()
        if size == 0:
            return None
        mid = size//2
        temp = Stack(mid)
        for _ in range(mid):
            temp.push(self.pop())
        self.pop()
        for _ in range(mid):
            self.push(temp.pop())
        return True
