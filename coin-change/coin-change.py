from typing import List


class Solution:
    def check_sum(self, curr_coins: list[tuple], amount: int) -> bool:
        total: int = 0
        for x, y in curr_coins:
            total += x * y
        return total < amount

    def coinChange(self, coins: List[int], amount: int) -> int:
        curr_coins: List[tuple] = []
        while True:
            curr_coins.append((5, 5))
            curr_coins.append((3, 3))
            break
        
        print(self.check_sum(curr_coins, amount=amount))


Solution().coinChange([1, 3, 5], 11)
