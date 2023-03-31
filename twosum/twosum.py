from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, x in enumerate(nums):
            for j, y in enumerate(nums):
                if x + y == target and index != j:
                    return [index, j]

s = Solution()
print(s.twoSum([3,3], 6))