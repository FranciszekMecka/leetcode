class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)
        s = str(n)[::-1]
        for i in range(3, len(s), 4):
            s = (s[:i] + '.' + s[i:])
        
        return s[::-1]
    
print(Solution().thousandSeparator(19231923))