#!/usr/bin/env python
#################################################
""" test_binary_search_tree.py
# # Test for Binary Search Tree(BST) Implementation
#   Tests:
#      - Insert, remove: functionality + API.
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
# ## imports
# Python Standard Library
from random import randint

# Local Application/Library Specific Imports.
import binary_search_tree as bst
##################################################
# Test
##################################################
BST_ROOT = bst.BSTNode(2)
BST = bst.BinarySearchTree(BST_ROOT)
for data in range(5):
    print("Insert: {} | Feedback: {}"
          .format(data, BST.insert(data)))
for i in range(15):
    data = randint(-100, 100)
    print("Insert: {} | Feedback: {}"
          .format(data, BST.insert(data)))
print("--- Return(__str__) ---")
print(BST)
print("Remove: {} | Feedback: {}"
      .format(1, BST.remove(1)))
print("BST.size() =", BST.size())
print("Remove: {} | Feedback: {}"
      .format(200, BST.remove(200)))
print("--- Pre-Order Recursive ---")
BST.pre_order()
print("--- Pre-Order Iterative ---")
BST.pre_order_iter()
print("--- In-Order Recursive ---")
BST.in_order()
print("--- In-Order Iterative ---")
BST.in_order_iter()
print("--- Reverse In-Order ---")
BST.rev_in_order()
print("--- Post-Order Recursive ---")
BST.post_order()
print("--- Post-Order Iterative ---")
BST.post_order_iter()
print("BST Height: ", BST.height())
print("BST: min()={}, max()={}: ".format(BST.get_min(), BST.get_max()))
print("--- Level Traverse Recursive ---")
BST.lvl_traverse()
print("--- Level Traverse Iterative ---")
BST.lvl_traverse_iter()
