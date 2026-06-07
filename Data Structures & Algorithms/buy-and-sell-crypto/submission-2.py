class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        max_profit = 0

        while r < len(prices):
            buy_price = prices[l]
            sell_price = prices[r] 
            if buy_price < sell_price:
                profit = sell_price - buy_price
                max_profit = max(profit, max_profit)
            else:
                # if the right one is lower move the left to right
                l = r
            
            # increment the right pointer always
            r += 1

        
        return max_profit