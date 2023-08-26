class Solution:
    def reverse(self, x: int) -> int:
        if x > pow(2, 31) - 1 or x < -1 * pow(2, 31):
            return 0
        
        flag: bool = True
        if x < 0:
            x *= -1
            flag = not flag

        numbers: list = []
        while x > 0:
            numbers.append(x%10)
            x//=10
        
        numbers.reverse()
        num: int = 0
        for i in range(len(numbers)):
            num += pow(10, i) * numbers[i]

        if num < -1 * pow(2, 31) or num > pow(2, 31):
            return 0

        if flag:
            return num
        
        return -num

print(Solution().reverse(1563847412))