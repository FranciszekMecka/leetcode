from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        y = len(nums)
        i = 0
        while True:
            if nums[i] == val:
                del nums[i]
            i += 1
            if i >= len(nums): break
        print(nums)

solution = Solution()
solution.removeElement([9,9,9,9,9,9,9], 9)