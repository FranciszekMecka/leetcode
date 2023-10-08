from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i: int = 0
        j: int = 0

        while i != m and j != n:
            if nums1[i] > nums2[j]:
                for x in range(i, len(nums1) - 1):
                    nums1[x + 1], nums1[x] = nums1[x], nums1[x + 1]
                nums1[i] = nums2[j]
                j += 1
            else:
                i += 1

        print(nums1)


Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
