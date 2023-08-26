from typing import List
from math import floor
import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score: int = 0
        my_heap = [-x for x in nums]
        heapq.heapify(my_heap)
        for _ in range(k):
            score -= heapq.heappushpop(my_heap, my_heap[0] // 3)

        return score
            
    
print(Solution().maxKelements([10,10,10,10,10], 5))
print(Solution().maxKelements([1,10,3,3,3], 3))