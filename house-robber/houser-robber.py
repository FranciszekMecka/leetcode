from typing import List


class Solution:  
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for i in nums:
            tmp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2


print(Solution().rob([2,7,9,3,1]))
