from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point : point[0])
        print(points)
        largest: int = 0
        for i in range(len(points) - 1):
            largest = max(largest, points[i + 1][0] - points[i][0])
        
        return largest


print(Solution().maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))