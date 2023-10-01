from typing import List

# copies the elements of the array if and shifts the
#  'k' iterator if it doesn't find the value to be removed


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k: int = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


print(Solution().removeElement([1, 4, 5, 5, 4, 0, 5, 4, 7], 4))
