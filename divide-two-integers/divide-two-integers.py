class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n: int = 0
        result: int = 0
        flag: bool = False
        if dividend < 0 and divisor > 0:
            dividend = -dividend
            flag = not flag
        elif dividend > 0 and divisor < 0:
            divisor = -divisor
            flag = not flag
        elif dividend < 0 and divisor < 0:
            divisor = -divisor
            dividend = -dividend
        while n + divisor <= dividend:
            n += divisor
            result += 1

        if not flag:
            return result
        return -result


# print(Solution().divide(10, 3))
# print(Solution().divide(7, -3))
print(Solution().divide(-1, -1))
