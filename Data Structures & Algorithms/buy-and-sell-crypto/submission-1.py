class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        max_profit = 0

        while r< len(prices):
            if prices[l]< prices[r]:
                profit = prices[r]-prices[l]
                max_profit = max(max_profit,profit)
            else:
                # move the left pointer to the right position, which is the least price till now
                l=r
            # move the right pointer every time
            r+=1

        return max_profit

