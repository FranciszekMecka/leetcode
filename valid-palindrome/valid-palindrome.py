class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = "1234567890qwertyuiopasdfghjklzxcvbnm"
        tmp = ''
        s = s.lower()
        for chr in s:
            if chr in letters:
                tmp += chr
        return tmp == tmp[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
