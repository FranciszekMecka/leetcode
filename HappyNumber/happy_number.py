class Solution:
    def isHappy(self, n: int) -> bool:
        nums = []
        history = []
        while True:
            while True:
                nums.append(n%10)
                n //= 10
                if n < 10:
                    nums.append(n)
                    break
            x = 0
            for num in nums:
                x += num * num
            if x == 1:
                return True
            elif x in history:
                return False
            history.append(x)
            n = x
            nums = []

s = Solution()
print(s.isHappy(22))