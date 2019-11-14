#!/usr/bin/python3
import sys
from kheap import Heap

key=None
training_entries = []

# We give the value of k as arguments to reducer.
k = int(sys.argv[1])

# Keep a count of the labels.
heap_list = [Heap(k) for i in range(7)]

# Reducer takes the output of mapper from STDIN.
for lines in sys.stdin:
    lines = lines.strip()
    key, distance = lines.split('\t')
    key, distance = int(key), float(distance)
    heap_list[key-1].add(distance)

for idx,heap in enumerate(heap_list):
    print(f"{idx+1}\t{str(heap)}")
