#!/usr/bin/env python
#################################################
""" heap.py
# # Heap Implementation
#   Supports:
#     - Basic:
#         > push, peek(find min/max), pop(extract min/max), replace, pushpop.
#     - Creation:
#         > heap, full_heapify, merge.
#     - Inspection
#         > size, is_empty, is_full, capacity, height.
#     - Inernal:
#         > parent, l/rchild, heapify, heapify_down, increase_key, decrease_key
"""
#################################################
# ###  Author: Samyuel Danyo
# ###  Date: 08/06/2020
# ###  Last Edit: 11/07/2020
##################################################
# ## imports
# Python Standard Library
import operator
##################################################
# Implementation
##################################################
class Heap:
    """Binary Heap implementation.
       Heap is partial order tree-based data structure, which is
       the maximally efficient implementation of a priority queue.
       Complexity: Heapify | Find Max | Extract Max | Increase Key
                     O(n)  |   O(1)   |   O(log(n)) |   O(log(n))
                   -----------------------------------------------
                    Insert   |   Delete   | Merge
                   O(log(n)) |  O(log(n)) | O(m+n) """
    def __init__(self, data=None, htype="min", cap=float("inf")):
        # resolve the heap's type (min/max).
        self.type = htype
        if self.type == "min":
            self.opr = operator.gt
        elif self.type == "max":
            self.opr = operator.lt
        else:
            print("WARNING: Heap Type NOT Supported. MinHeap Created!")
            self.type = "min"
            self.opr = operator.lt
        # Create and order the heap.
        if data is None:
            self.num_els = 0
            self.data = []
        else:
            self.data = data
            self.num_els = len(data)
            self.full_heapify()
        self.cap = cap

    def size(self):
        """Get the number of elements in the heap."""
        return self.num_els

    def __str__(self):
        return str(self.data)

    def is_empty(self):
        """True if the queue is empty."""
        return self.size() <= 0

    def capacity(self):
        """Get the heap's capacity."""
        return self.cap

    def is_full(self):
        """True if the queue is full."""
        return self.size() == self.cap

    def _parent(self, idx):
        """Get the parent element's index of idx
           (as per binary tree list representation)."""
        if idx == 0:
            return 0
        return (idx - 1) // 2

    def _lchild(self, idx):
        """Get the left child element's index of idx
           (as per binary tree list representation)."""
        return idx * 2 + 1

    def _rchild(self, idx):
        """Get the right child element's index of idx
           (as per binary tree list representation)."""
        return idx * 2 + 2

    def __swap(self, idx1, idx2):
        """Swap elements and idx1 & idx2."""
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]

    def heapify(self, idx):
        """Set partial order to (balance) the tree with root at idx.
           Heapify up from idx to len(heap)."""
        left = self._lchild(idx)
        if left >= self.size():
            return
        right = self._rchild(idx)
        tar_idx = idx
        if self.opr(self.data[tar_idx], self.data[left]):
            tar_idx = left
        if right < self.size() and self.opr(self.data[tar_idx], self.data[right]):
            tar_idx = right
        if tar_idx != idx:
            self.__swap(idx, tar_idx)
            self.heapify(tar_idx)

    def full_heapify(self):
        """Convert the binary tree (self.data) into a Heap data structure."""
        idx = self._parent(self.size() - 1)
        while idx >= 0:
            self.heapify(idx)
            idx -= 1

    def heapify_down(self, idx):
        """Set partial order to (balance) the tree with leaf at idx.
           Heapify down from idx to heap[0]."""
        parent = self._parent(idx)
        if self.opr(self.data[parent], self.data[idx]):
            self.__swap(idx, parent)
            self.heapify_down(parent)

    def push(self, value):
        """Add a value to the heap."""
        if self.is_full():
            print("WARNING: Heap Overflow!")
            return None
        self.data.insert(0, value)
        self.num_els += 1
        self.heapify(0)
        return True

    def peek(self):
        """Find a maximum item of a max-heap,
           or a minimum item of a min-heap, respectively."""
        if self.is_empty():
            print("WARNING: Heap Underflow!")
            return None
        return self.data[0]

    def pop(self):
        """Get the maximum value from a max heap
           [or minimum value from a min heap] and removing it from the heap."""
        if self.is_empty():
            print("WARNING: Heap Underflow!")
            return None
        lastvalue = self.data.pop()
        self.num_els -= 1
        if self.is_empty():
            return lastvalue
        value = self.data[0]
        self.data[0] = lastvalue
        self.heapify(0)
        return value

    def replace(self, value):
        """Pop root and push a new key(poppush). More efficient than
           pop followed by push, since only need to balance once."""
        if self.is_empty():
            print("WARNING: Heap Underflow!. Will Push New Value!")
            self.num_els += 1
            rvalue = None
        else:
            rvalue = self.data.pop(0)
        self.data.insert(0, value)
        self.heapify(0)
        return rvalue

    def pushpop(self, value):
        """Push a new key and pop root(reverse of repalce). More efficient than
           push followed by pop, since only need to balance once."""
        if self.size() and self.opr(value, self.data[0]):
            value, self.data[0] = self.data[0], value
            self.heapify(0)
        return value

    def merge(self, heap):
        """Union: joining two heaps to form a valid new heap containing all
           the elements of both, preserving the original heaps."""
        self.num_els += len(heap)
        self.data.extend(heap)
        self.full_heapify()

    def decrease_key(self, idx, value):
        """Update key at idx with value, where value < key."""
        if self.data[idx] <= value:
            return
        self.data[idx] = value
        if self.type == "min" and idx > 0:
            self.heapify_down(idx)
        if self.type == "max":
            self.heapify(idx)

    def increase_key(self, idx, value):
        """Update key at idx with value, where value > key."""
        if self.data[idx] >= value:
            return
        self.data[idx] = value
        if self.type == "max" and idx > 0:
            self.heapify_down(idx)
        if self.type == "min":
            self.heapify(idx)
