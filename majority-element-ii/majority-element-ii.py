from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 0
            counts[nums[i]] += 1

        majority_elements: List = []
        n: int = len(nums) // 3
        for k in counts:
            if counts[k] > n:
                majority_elements.append(k)
        return majority_elements


# Solution().majorityElement([5 for _ in range(5)] + [3 for _ in range(3)] + [4 for _ in range(5)])
Solution().majorityElement([3, 2, 3])
