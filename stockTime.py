class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1000000
        max_profit = 0 
        for price in prices:
            min_price = min(min_price,price)
            profit = price - min_price
            max_profit = max(profit,max_profit)

        return max_profit
