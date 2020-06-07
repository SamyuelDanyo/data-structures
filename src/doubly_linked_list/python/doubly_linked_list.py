#!/usr/bin/env python
#################################################
""" doubly_linked_list.py
# # Doubly Linked List Implementation
#   Supports:
#      - Traverse.
#      - Push/Append/Insert nodes.
#      - Remove by data/index.
#      - Get tail
#      - Delete.
"""
#################################################
# ###  Author: Samyuel Danyo
# ###  Date: 31/05/2020
# ###  Last Edit: 31/05/2020
##################################################
# Implementation
##################################################
class DLLNode:
    """Doubly Linked List Node Class."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """Doubly Linked List class."""
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        data = []
        node = self.head
        while node:
            data.append(str(node.data))
            node = node.next
        return "[" + ", ".join(data) + "]"

    def traverse(self):
        """Traverse the list."""
        node = self.head
        if node is None:
            print("WARNING:: The list is empty!")
            return
        try:
            print('[', end='')
            while node.next:
                print(node.data, end=', ', flush=True)
                node = node.next
            print('{}]'.format(node.data))
        except:
            print("WARNING:: The list is empty!")

    def push(self, data):
        """Push DLLNode(data) into the list."""
        node = DLLNode(data)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_after(self, prev_node, data):
        """Insert DLLNode(data) after prev_node(list[idx])."""
        node = DLLNode(data)
        node.prev = prev_node
        node.next = prev_node.next
        prev_node.next = node
        if node.next is None:
            return
        node.next.prev = node

    def insert(self, idx, data):
        """Insert DLLNode(data) at list[idx]."""
        if idx == 0:
            self.push(data)
        else:
            i = 0
            node = self.head
            while(i+1 < idx and node.next):
                i += 1
                node = node.next
            self.insert_after(node, data)

    def append(self, data):
        """Push SLLNode(data) to the list."""
        node = self.head
        if node is None:
            self.head = DLLNode(data)
        while node.next:
            node = node.next
        node.next = DLLNode(data)
        node.next.prev = node

    def get_tail(self):
        """Get list[-1]."""
        node = self.head
        while node.next:
            node = node.next
        return node

    def remove(self, data):
        """Remove first occurence of DLLNode(data)."""
        node = self.head
        if node.data == data:
            self.head = node.next
            if self.head:
                self.head.prev = None
        else:
            while node.next:
                node = node.next
                if node.data == data:
                    node.prev.next = node.next
                    if node.next:
                        node.next.prev = node.prev
                    return

    def remove_node(self, idx):
        """Remove list[idx]."""
        if idx == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            i = 0
            node = self.head
            while(i < idx and node):
                i += 1
                node = node.next
            if node is None:
                return
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

    def delete(self):
        """Delete the list"""
        node = self.head
        while node:
            next_node = node.next
            del node.data
            node = next_node
        self.head = None
