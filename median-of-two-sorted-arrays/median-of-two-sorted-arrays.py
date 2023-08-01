from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_nums: List = []
        while nums1 and nums2:
            total_nums.append(min(nums1[0], nums2[0]))
            if nums1[0] < nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)
        if nums1:
            total_nums += nums1
        if nums2:
            total_nums += nums2

        print(total_nums)
        if len(total_nums)%2 == 1:
            return total_nums[len(total_nums)//2]
        else:
            return (total_nums[len(total_nums)//2] + total_nums[(len(total_nums)//2) - 1]) / 2

print(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3,4]))