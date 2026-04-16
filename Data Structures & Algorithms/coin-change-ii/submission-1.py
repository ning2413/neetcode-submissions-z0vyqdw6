class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextdp = [0] * (amount + 1)
            nextdp[0] = 1
            for j in range(1, amount + 1):
                nextdp[j] = dp[j]
                if j - coins[i] >= 0:
                    nextdp[j] += nextdp[j - coins[i]]
            dp = nextdp
        return dp[amount]

