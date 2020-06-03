#!/usr/bin/env python
#################################################
""" test_queue.py
# # Test for Queue(FIFO) Implementation
#   Tests:
#      - Capacity, size.
#      - Push, Pop, Peek.
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
import queue as que
##################################################
# Test
##################################################
print("==== ARRAY QUEUE IMPLEMENTATION ====")
QUEUE = que.Queue(7)
for _ in range(8):
    QUEUE.push(randint(1, 100))
print("Queue cap: {} | size: {}".format(QUEUE.capacity(), QUEUE.size()))
print(QUEUE)
print("QUEUE tail at:", QUEUE.peek())
while not QUEUE.is_empty():
    print(QUEUE.pop())
QUEUE.pop()
print("==== LIST QUEUE IMPLEMENTATION ====")
QUEUE = que.ListQueue(7)
for _ in range(8):
    QUEUE.push(randint(1, 100))
print("Queue cap: {} | size: {}".format(QUEUE.capacity(), QUEUE.size()))
print(QUEUE)
print("QUEUE tail at:", QUEUE.peek())
while not QUEUE.is_empty():
    print(QUEUE.pop())
QUEUE.pop()
