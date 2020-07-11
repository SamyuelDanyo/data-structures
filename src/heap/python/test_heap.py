#!/usr/bin/env python
#################################################
""" test_heap.py
# # Test for Heap Implementation
#   Tests min/max heaps:
#      - Creating a heap
#      - Push, peek, pop: functionality + API.
#      - Size, capacity, is_empty.
#      - Merge, pushpop, replace, increase/decrease_key
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
import heap
##################################################
# Test
##################################################
print("==== TEST MIN HEAP IMPLEMENTATION ====")
MIN_HEAP = heap.Heap([3, 6, 10, -3, 5], "min")
print(MIN_HEAP)
for _ in range(5):
    val = randint(-100, 100)
    print("Pushing ", val)
    MIN_HEAP.push(val)
print("MIN HEAP cap: {} | size: {}".format(MIN_HEAP.capacity(), MIN_HEAP.size()))
print(MIN_HEAP)
print("MIN_HEAP min:", MIN_HEAP.peek())
print("MIN_HEAP replace (7):", MIN_HEAP.replace(7))
print(MIN_HEAP)
print("Pop the heap.")
while not MIN_HEAP.is_empty():
    print(MIN_HEAP.pop())
MIN_HEAP.pop()
print("Merge")
MIN_HEAP.merge([1, 2, -1])
print(MIN_HEAP)
print("Merge")
MIN_HEAP.merge([-2, 6])
print(MIN_HEAP)
print("PushPop -4: ", MIN_HEAP.pushpop(-4))
print("PushPop 5: ", MIN_HEAP.pushpop(5))
print(MIN_HEAP)
print("Decrease key at 3 to -4")
MIN_HEAP.decrease_key(3, -4)
print(MIN_HEAP)
print("Decrease key at 4 to 5")
MIN_HEAP.decrease_key(4, 5)
print(MIN_HEAP)
print("Increase key at 3 to 8")
MIN_HEAP.increase_key(3, 8)
print(MIN_HEAP)
print("Increase key at 0 to 7")
MIN_HEAP.increase_key(0, 7)
print(MIN_HEAP)
print("\n==== TEST MAX HEAP IMPLEMENTATION ====")
MAX_HEAP = heap.Heap([3, 6, 10, -3, 5], "max", 9)
print(MAX_HEAP)
for _ in range(5):
    val = randint(-100, 100)
    print("Pushing ", val)
    MAX_HEAP.push(val)
print("MAX HEAP cap: {} | size: {}".format(MAX_HEAP.capacity(), MAX_HEAP.size()))
print(MAX_HEAP)
print("MAX_HEAP max:", MAX_HEAP.peek())
print("MAX_HEAP replace (7):", MAX_HEAP.replace(7))
print(MAX_HEAP)
print("Pop the heap.")
while not MAX_HEAP.is_empty():
    print(MAX_HEAP.pop())
MAX_HEAP.pop()
print("Merge")
MAX_HEAP.merge([1, 2, -1])
print(MAX_HEAP)
print("Merge")
MAX_HEAP.merge([-2, 6])
print(MAX_HEAP)
print("PushPop -4: ", MAX_HEAP.pushpop(-4))
print("PushPop 7: ", MAX_HEAP.pushpop(7))
print(MAX_HEAP)
print("Increase key at 3 to 8")
MAX_HEAP.increase_key(3, 8)
print(MAX_HEAP)
print("Increase key at 4 to 7")
MAX_HEAP.increase_key(4, 7)
print(MAX_HEAP)
print("Decrease key at 3 to -4")
MAX_HEAP.decrease_key(3, -4)
print(MAX_HEAP)
print("Decrease key at 0 to 5")
MAX_HEAP.decrease_key(0, 5)
print(MAX_HEAP)
