class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        result: int = x
        for i in range(abs(n) - 1):
            result *= x

        if n < 0:
            return 1/result
        return result
    
print(Solution().myPow(x = 2.00000, n = -2))