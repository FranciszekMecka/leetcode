from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs: int = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    pairs += 1

        return pairs


print(Solution().numIdenticalPairs([1, 1, 1, 1]))
print(Solution().numIdenticalPairs([1, 2, 3]))
