#!/usr/bin/env python
#################################################
""" binary_search_tree.py
# # Binary Search Tree(BST) Implementation
#   Supports:
#      - Insert, remove.
#      - Size, min, max, height.
#      - Recursive traverse:
#          > {Pre, in, reverse in, post}-order, level
#      - Iterative traverse:
#          > {Pre, in, post}-order, level
"""
#################################################
# ###  Author: Samyuel Danyo
# ###  Date: 07/06/2020
# ###  Last Edit: 07/06/2020
##################################################
# Implementation
##################################################
class BSTNode:
    """Node for a Binary Search Tree(BST) implementation."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree(BST) implementation."""
    def __init__(self, root=None):
        self.root = root
        self.num_nodes = 0 + (root is not None)

    def _insert(self, root, data, feedback):
        """Utility function to insert BSTNode(data) in the tree."""
        if root is None:
            root = BSTNode(data)
            self.num_nodes += 1
            feedback.append(True)
        elif root.data == data:
            feedback.append(False)
        elif root.data > data:
            root.left = self._insert(root.left, data, feedback)
        else:
            root.right = self._insert(root.right, data, feedback)
        return root

    def insert(self, data):
        """Insert BSTNode(data) in the tree.
           Returns:
               feedback (Boolean): True if the data was not in the BST
                                   and was added, False otherwise."""
        feedback = []
        self.root = self._insert(self.root, data, feedback)
        return feedback[0]

    def size(self):
        """Get the number of nodes in the BST."""
        return self.num_nodes

    def _height(self, root):
        """Utility function for getting the height of the BST."""
        if root is None:
            return 0
        lheight = self._height(root.left)
        rheight = self._height(root.right)
        if lheight > rheight:
            return lheight+1
        return rheight+1

    def height(self):
        """Get the height of the BST."""
        return self._height(self.root)

    def _get_min(self, root):
        """Utility function for getting the minimum node in the BST."""
        if root is None:
            return None
        if root.left is None:
            return root.data
        return self._get_min(root.left)

    def get_min(self):
        """Get the minimum node in the BST."""
        return self._get_min(self.root)

    def _get_max(self, root):
        """Utility function for getting the maximum node in the BST."""
        if root is None:
            return None
        if root.right is None:
            return root.data
        return self._get_max(root.right)

    def get_max(self):
        """Get the maximum node in the BST."""
        return self._get_max(self.root)

    def _remove(self, root, data, feedback):
        """Utility function to remove <data> from the BST."""
        if root is None:
            feedback.append(False)
            return None
        if root.data == data:
            feedback.append(True)
            self.num_nodes -= 1
            if root.right and root.left:
                next_min = self._get_min(root.right)
                root.data = next_min
                root.right = self._remove(root.right, next_min, feedback)
                return root
            if root.right:
                return root.right
            return root.left
        if root.data > data:
            root.left = self._remove(root.left, data, feedback)
        else:
            root.right = self._remove(root.right, data, feedback)
        return root

    def remove(self, data):
        """Remove <data> from the BST.
           Returns:
               feedback (Boolean): True if the data was in the BST
                                   and was removed, False otherwise."""
        feedback = []
        self._remove(self.root, data, feedback)
        return feedback[0]

    def _pre_order(self, root, callback=print):
        """Utility function to pre-order(nlr) traverse the BST."""
        if root is None:
            return
        callback(root.data)
        self._pre_order(root.left, callback)
        self._pre_order(root.right, callback)

    def pre_order(self, verbose=True):
        """Pre-order(nlr, topologically-sorted) traverse the BST."""
        traversal = []
        self._pre_order(self.root, traversal.append)
        if verbose:
            print(traversal)
        return traversal

    def pre_order_iter(self, verbose=True):
        """Pre-order(nlr, topologically-sorted) traverse the BST, iterative implementation."""
        stack = []
        stack.append(self.root)
        traversal = []
        while stack:
            node = stack.pop()
            traversal.append(node.data)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        if verbose:
            print(traversal)
        return traversal

    def __str__(self):
        return "".join(str(self.pre_order(False)))

    def _in_order(self, root, callback=print):
        """Utility function to in-order(lnr, min->max sorted) traverse the BST."""
        if root is None:
            return
        self._in_order(root.left, callback)
        callback(root.data)
        self._in_order(root.right, callback)

    def in_order(self, verbose=True):
        """In-order(lnr, min->max sorted) traverse the BST."""
        traversal = []
        self._in_order(self.root, traversal.append)
        if verbose:
            print(traversal)
        return traversal

    def in_order_iter(self, verbose=True):
        """In-order(lnr, min->max sorted) traverse the BST, iterative implementation."""
        stack = []
        node = self.root
        traversal = []
        while (node is not None) or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            traversal.append(node.data)
            node = node.right
        if verbose:
            print(traversal)
        return traversal

    def _rev_in_order(self, root, callback=print):
        """Utility function to reverse in-order(lnr, max->min sorted) traverse the BST."""
        if root is None:
            return
        self._rev_in_order(root.right, callback)
        callback(root.data)
        self._rev_in_order(root.left, callback)

    def rev_in_order(self, verbose=True):
        """Reverse in-order(lnr, max->min sorted) traverse the BST."""
        traversal = []
        self._rev_in_order(self.root, traversal.append)
        if verbose:
            print(traversal)
        return traversal

    def _post_order(self, root, callback=print):
        """Utility function to post-order(lrn, leaves->root) traverse the BST."""
        if root is None:
            return
        self._post_order(root.left, callback)
        self._post_order(root.right, callback)
        callback(root.data)

    def post_order(self, verbose=True):
        """Post-order(lrn, leaves->root) traverse the BST."""
        traversal = []
        self._post_order(self.root, traversal.append)
        if verbose:
            print(traversal)
        return traversal

    def post_order_iter(self, verbose=True):
        """Post-order(lrn, leaves->root) traverse the BST, iterative implementation."""
        tmp = [self.root]
        full = []
        traversal = []
        while tmp:
            node = tmp.pop()
            full.append(node)
            if node.left is not None:
                tmp.append(node.left)
            if node.right is not None:
                tmp.append(node.right)
        while full:
            node = full.pop()
            traversal.append(node.data)
        if verbose:
            print(traversal)
        return traversal

    def _print_level(self, root, lvl):
        """Utility function for printing <lvl> level of the BST."""
        if root is None:
            return
        if lvl == 1:
            print(root.data, end=' ')
        else:
            self._print_level(root.left, lvl-1)
            self._print_level(root.right, lvl-1)

    def print_level(self, lvl):
        """Print <lvl> level of the BST."""
        print("Level {}:".format(lvl), end=" ")
        self._print_level(self.root, lvl)
        print()

    def lvl_traverse(self):
        """Level traverse the BST."""
        height = self.height()
        for lvl in range(1, height+1):
            self.print_level(lvl)

    def lvl_traverse_iter(self):
        """Level traverse the BST, iterative(BFS) implementation."""
        if self.root is None:
            return
        queue = [self.root]
        tmp = []
        lvl = 1
        print("Level {}:".format(lvl), end=" ")
        while queue:
            node = queue.pop()
            print(node.data, end=' ')
            if node.left:
                tmp.insert(0, node.left)
            if node.right:
                tmp.insert(0, node.right)
            if not queue and tmp:
                lvl += 1
                queue = tmp
                tmp = []
                print("\nLevel {}:".format(lvl), end=" ")
