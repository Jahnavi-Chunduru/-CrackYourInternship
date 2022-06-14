import random
from heapq import heappush, heappop

class RandomizedCollection:

    def __init__(self):
        self.h = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        self.arr.append(val)
        if val in self.h:
            heap = self.h[val]
            heappush(heap, -(len(self.arr) - 1))
            self.h[val] = heap
            return False
        else:
            heap = []
            heappush(heap, -(len(self.arr) - 1))
            self.h[val] = heap
            return True

    def remove(self, val: int) -> bool:
        if val in self.h:
            indexes_heap = self.h[val]
            last_index = -heappop(indexes_heap)
            
            if last_index == len(self.arr) - 1:
                self.arr.pop()
            else:
                last_val = self.arr[-1]
                
                self.arr[last_index] = last_val
                self.arr.pop()
                
                heappop(self.h[last_val])
                heappush(self.h[last_val], -last_index)
                
            if len(indexes_heap) == 0:
                self.h.pop(val)
            
            return True
        else:
            return False

    def getRandom(self) -> int:
        r = random.randint(0, len(self.arr)-1)
        return self.arr[r]
