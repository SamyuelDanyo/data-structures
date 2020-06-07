#!/usr/bin/env python
#################################################
""" test_doubly_linked_list.py
# # Test for Doubly Linked List Implementation
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
import doubly_linked_list as dll
##################################################
# Test
##################################################
DLLIST = dll.DoublyLinkedList(dll.DLLNode(0))
for i in range(1, 6):
    DLLIST.insert(i, i)
DLLIST.push(-1)
DLLIST.append(7)
DLLIST.insert_after(DLLIST.head.next, 100)
DLLIST.insert(5, 100)
DLLIST.traverse()
print('='*30)
DLLIST.remove(100)
print(DLLIST)
print('='*30)
DLLIST.remove_node(3)
DLLIST.traverse()
print('='*30)
DLLIST.delete()
DLLIST.traverse()
