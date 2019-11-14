#!/home/ayushjain1144/anaconda3/bin/python
import sys
import heapq


class Heap():
    def __init__(self, k):
        self.k=k
        self.heap=[]

    def add(self, x):
        x=-x
        heapq.heappush(self.heap,x)
        if(len(self.heap)>self.k):
            heapq.heappop(self.heap)
    
    def get(self):
        return sorted(list(map(lambda  x: -x,self.heap)))
    
    def __str__(self):
        return ','.join(map(str,self.get()))

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
