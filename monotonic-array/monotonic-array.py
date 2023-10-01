from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        isDescending: bool = True
        isAscending: bool = True

        for i in range(0, len(nums) - 1):
            if nums[i + 1] > nums[i]:
                isDescending = False
            if nums[i + 1] < nums[i]:
                isAscending = False

            if not isDescending and not isAscending:
                return False

        return True
            