from typing import List


class Solution:
    def removeStars(self, s: str) -> str:
        result: list = []
        for i in s:
            if i == '*' and len(result) > 0:
                result.pop()
            else:
                result.append(i)

        return ''.join(result)


print(Solution().removeStars("leet**cod*e"))
