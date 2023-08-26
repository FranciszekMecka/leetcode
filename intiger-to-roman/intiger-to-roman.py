class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        roman: str = ''
        while num > 0:
            for k in symbols:
                if symbols[k] <= num:
                    num -= symbols[k]
                    roman += str(k)
                    break

        return roman

print(Solution().intToRoman(9))
