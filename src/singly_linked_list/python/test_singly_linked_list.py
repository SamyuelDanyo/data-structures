#!/usr/bin/env python
#################################################
""" test_singly_linked_list.py
# # Test for Singly Linked List Implementation
#   Tests:
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
# Local Application/Library Specific Imports.
import singly_linked_list as sll
##################################################
# Test
##################################################
SLLIST = sll.SinglyLinkedList(sll.SLLNode(0))
for i in range(1, 6):
    SLLIST.insert(i, i)
SLLIST.push(-1)
SLLIST.append(7)
SLLIST.insert_after(SLLIST.head.next, 100)
SLLIST.traverse()
print('='*30)
SLLIST.remove(100)
print(SLLIST)
print('='*30)
SLLIST.remove_node(3)
SLLIST.traverse()
print('='*30)
SLLIST.delete()
SLLIST.traverse()
