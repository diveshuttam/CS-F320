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
