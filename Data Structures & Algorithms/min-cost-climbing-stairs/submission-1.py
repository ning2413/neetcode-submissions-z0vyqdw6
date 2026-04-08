class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float("inf")] * (len(cost) + 2)
        dp[0] = 0
        dp[1] = 0
        for i in range(len(cost)):
            c1 = min(dp[i + 1], dp[i] + cost[i])
            c2 = min(dp[i + 2], dp[i] + cost[i])
            print(c1, c2)
            dp[i+1] = c1
            dp[i+2] = c2
        print(dp)
            
        return dp[len(cost)]