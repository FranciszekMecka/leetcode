class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len: int = 0 if len(s) == 0 else 1

        curr: list = []
        for i in range(len(s)):
            curr.append(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in curr:
                    curr.clear()
                    break
                curr.append(s[j])
                max_len = max(max_len, len(curr))
        return max_len
    
print(Solution().lengthOfLongestSubstring(""))