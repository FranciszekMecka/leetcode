from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output_str: list = list(s)
        for x in zip(s, indices):
            output_str[x[1]] = x[0]
        return ''.join(output_str)
    
print(Solution().restoreString('codeleet', [4,5,6,7,0,2,1,3]))
print(Solution().restoreString("abc", [0,1,2]))