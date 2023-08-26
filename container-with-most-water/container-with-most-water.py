from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water: int = 0
        
        i: int = 0
        j: int = len(height) - 1

        while i != j:
            max_water = max(max_water, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_water

print(Solution().maxArea([1,1]))