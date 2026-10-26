class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day=prices[0]
        sell_day=prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i]<buy_day:
                buy_day=prices[i]
                sell_day=prices[i]
            elif prices[i]>sell_day:
                sell_day=prices[i]
            
            max_profit = max(max_profit, sell_day-buy_day)
        
        return max_profit

        
