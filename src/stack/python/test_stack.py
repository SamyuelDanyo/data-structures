#!/usr/bin/env python
#################################################
""" test_stack.py
# # Test for Stack(LIFO) Implementation
#   Tests:
#      - Capacity, size.
#      - Push, Pop, Peek.
#      - Delete_mid.
"""
#################################################
# ###  Author: Samyuel Danyo
# ###  Date: 02/06/2020
# ###  Last Edit: 02/06/2020
##################################################
# ## imports
# Python Standard Library
from random import randint

# Local Application/Library Specific Imports.
import stack as st
##################################################
# Test
##################################################
print("==== ARRAY STACK IMPLEMENTATION ====")
STACK = st.Stack(7)
for idx in range(8):
    STACK.push(randint(1, 100))
print("Stack cap: {} | size: {}".format(STACK.capacity(), STACK.size()))
print(STACK)
print("Stack head at:", STACK.peek())
STACK.delete_mid()
print("Stack cap: {} | size: {}".format(STACK.capacity(), STACK.size()))
while not STACK.is_empty():
    print(STACK.pop())
print("==== LIST STACK IMPLEMENTATION ====")
STACK = st.ListStack(7)
for idx in range(8):
    STACK.push(randint(1, 100))
print("Stack cap: {} | size: {}".format(STACK.capacity(), STACK.size()))
print(STACK)
print("Stack head at:", STACK.peek())
STACK.delete_mid()
print("Stack cap: {} | size: {}".format(STACK.capacity(), STACK.size()))
while not STACK.is_empty():
    print(STACK.pop())
