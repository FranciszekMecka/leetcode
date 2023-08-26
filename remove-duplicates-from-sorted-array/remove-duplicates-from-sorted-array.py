from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        record: set = set()
        k: int = 0
        for i in range(len(nums)):
            if nums[i] not in record:
                record.add(nums[i])
            else:
                nums[i] = '_'
                k += 1

        test = list(set(nums))
        test = test[:len(test) - 1]
        test += ['_' for _ in range(k)]
        nums = test

        return k


print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
