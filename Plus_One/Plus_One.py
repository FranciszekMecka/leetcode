from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] += 1
        
        i = len(digits) - 1
        while True:
            if digits[i] <= 9:
                break
            else:
                if (i == 0):
                    digits[0] %= 10
                    digits.insert(0, 1)
                    break
                digits[i - 1] += 1
                digits[i] %= 10
                i -= 1
        return digits
solution = Solution()
print(solution.plusOne([9]))