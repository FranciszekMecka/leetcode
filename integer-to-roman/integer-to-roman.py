class Solution:
    def intToRoman(self, num: int) -> str:
        rom_dict: dict = {
            "I" : 1,
            "III": 3,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XL" : 90,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }