#!/usr/bin/env python
#################################################
""" singly_linked_list.py
# # Singly Linked List Implementation
#   Supports:
#      - Traverse.
#      - Push/Append/Insert nodes.
#      - Remove by data/index.
#      - Delete.
"""
#################################################
# ###  Author: Samyuel Danyo
# ###  Date: 31/05/2020
# ###  Last Edit: 31/05/2020
##################################################
# Implementation
##################################################
class SLLNode:
    """Singly Linked List Node Class."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Singly Linked List Class."""
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

    def insert(self, idx, data):
        """Insert a SLLNode(data) at list[idx]."""
        i = 0
        node = self.head
        while(idx > i+1 and node.next):
            i += 1
            node = node.next

        new_node = SLLNode(data)
        if idx > 0:
            new_node.next = node.next
            node.next = new_node
        else:
            new_node.next = node
            self.head = new_node

    def push(self, data):
        """Push SLLNode(data) into the list."""
        node = SLLNode(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        """Append SLLNode(data) to the list."""
        node = self.head
        while node.next:
            node = node.next
        node.next = SLLNode(data)

    def insert_after(self, prev_node, data):
        """Insert SLLNode(data) after prev_node(list[idx])."""
        node = SLLNode(data)
        node.next = prev_node.next
        prev_node.next = node

    def remove(self, data):
        """Remove first occurence of SLLNode(data)."""
        node = self.head
        if node.data == data:
            self.head = node.next
            return
        while(node and node.data != data):
            prev = node
            node = node.next
        if node is not None:
            prev.next = node.next

    def remove_node(self, idx):
        """Remove list[idx]."""
        i = 0
        node = self.head
        if idx == 0:
            self.head = node.next
        else:
            while(idx > i+1 and node.next):
                i += 1
                node = node.next
            node.next = node.next.next

    def delete(self):
        """Delete the list"""
        node = self.head
        while node:
            next_node = node.next
            del node.data
            node = next_node
        self.head = None
