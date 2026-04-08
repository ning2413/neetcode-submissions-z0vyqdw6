class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxprofit = 0
        for i in range(len(prices)):
            profit = prices[i] - prices[l]
            maxprofit = max(maxprofit, profit)
            if prices[i] < prices[l]:
                l = i
        return maxprofit