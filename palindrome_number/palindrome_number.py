class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp: int = x
        digits: list = []
        while temp > 0:
            digits.append(temp%10)
            temp //= 10
        reversed_digits = list(reversed(digits))
        for i in zip(digits, reversed_digits):
            if i[0] != i[1]:
                return False
        return True

print(Solution().isPalindrome(-121))