from typing import List
from itertools import permutations


class Solution:
    n_min = 6
    n_hours = 4

    def get_permutations(self, turnedOn: int) -> list[int]:
        lights = [0] * 10
        for i in range(turnedOn):
            lights[i] = 1
        perms = list(set(permutations(lights)))
        return perms
    
    def translate_time(self, lights) -> str:
        minutes: int = 0
        hours: int = 0

        for i in range(self.n_min):
            if lights[i] == 1:
                minutes += 2**i
        index: int = 0
        for i in range(self.n_min, self.n_min + self.n_hours, 1):
            if lights[i] == 1:
                hours += 2**index
            index += 1
        
        if minutes > 59 or hours > 11:
            return

        if minutes < 10:
            time: str = f"{hours}:0{minutes}"
        else:
            time: str = f"{hours}:{minutes}"
        
        return time

    def translate_string(self, strTime: str) -> int:
        val: int = 0
        for char in strTime:
            if char != ':':
                val += int(char)
                val *= 10
        return val


    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        pers = self.get_permutations(turnedOn)
        times = []
        for per in pers:
            x = self.translate_time(per)
            if (x != None):
                times.append(x)
            times.sort(key=lambda x: self.translate_string(x))
        # print(times)
        return times

s = Solution()
s.readBinaryWatch(2)