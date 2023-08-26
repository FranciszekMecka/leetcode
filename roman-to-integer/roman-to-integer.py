class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict: dict = {
            'I': 1,
            'III': 3,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD' : 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }

        curr: str = ''
        total: int = 0
        i: int = 0
        while i < len(s):
            # for i in range(len(s)):
            if i != len(s) - 1:
                curr += s[i] + s[i + 1]
            else:
                curr += s[i]

            if curr in rom_dict:
                total += rom_dict[f'{curr}']
                i += 1
            else:
                total += rom_dict[f'{s[i]}']
            curr = ''
            i += 1

        return total


print(Solution().romanToInt('MCMXCIV'))
