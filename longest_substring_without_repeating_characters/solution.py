class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        current = []
        max_len = 1
        for i in range(0, len(s)):
            chr = s[i]
            current.append(chr)
            for j in range(i + 1, len(s)):
                if s[j] not in current:
                    current.append(s[j])
                else:
                    break
            current = []
            max_len = max(max_len, len(current))
        return max_len
    
s = Solution()
print(s.lengthOfLongestSubstring("au"))