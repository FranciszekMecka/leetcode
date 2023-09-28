from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        iter: int = 0
        for i in zip(*matrix):
            print(i)
            matrix[iter] = i[::-1]
            iter += 1


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
Solution().rotate(matrix)
print(matrix)