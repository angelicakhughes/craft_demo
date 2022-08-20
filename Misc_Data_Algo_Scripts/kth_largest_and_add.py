
#!/usr/bin/python
from typing import List
import heapq

#how to execute a class
#Class(input)
#Input is:
# (3, [4, 5, 8, 2])

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

ob = KthLargest(3, [4, 5, 8, 2])

KthLargest(3, [4, 5, 8, 2])

# print the 3th to largest number and also add "3" to the list
print(ob.add(3))
#[4,5,8,2,3]

#more examples
print(ob.add(5))
#[4,5,8,2,5]
print(ob.add(10))
#[4,5,8,2,10]
print(ob.add(9))
#[4,5,8,2,9]
print(ob.add(4))
#[4,5,8,2,4]


