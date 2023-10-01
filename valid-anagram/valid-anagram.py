class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s: dict = {}
        letters_t: dict = {}
        for n in s:
            if n not in letters_s:
                letters_s[n] = 0
            letters_s[n] += 1

        for n in t:
            if n not in letters_t:
                letters_t[n] = 0
            letters_t[n] += 1

        return letters_s == letters_t


print(Solution().isAnagram("ab", "ab"))
