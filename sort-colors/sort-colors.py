from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        no_colors: List = [0, 0, 0]
        
        for x in nums:
            no_colors[x] += 1

        nums.clear()
        
        for i in range(len(no_colors)):
            nums += [i for _ in range(no_colors[i])]
        
        print(nums)

Solution().sortColors([2,0,2,1,1,0])