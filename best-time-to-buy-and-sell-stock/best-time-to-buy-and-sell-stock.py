from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price: int = 100000
        max_price: int = -100000
        profit: int = 0


        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
                max_price = 0
            if max_price < prices[i]:
                max_price = prices[i]
            
            profit = max(profit, max_price - min_price)


        return profit


print(Solution().maxProfit([2, 4, 1]))
