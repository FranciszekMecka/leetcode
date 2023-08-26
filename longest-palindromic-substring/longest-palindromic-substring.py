class Solution:
    def is_palindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[-i - 1]:
                return False

        return True

    def longestPalindrome(self, s: str) -> str:
        curr: list = []
        for i in range(len(s)):
            curr.append(s[i])
            for j in range(i + 1, len(s)):
                curr.append(s[j])
                if not self.is_palindrome(curr):
                    curr.clear()
                else:
                    print(curr)

Solution().longestPalindrome("testHelloheheh")