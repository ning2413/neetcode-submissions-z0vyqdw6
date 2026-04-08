class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(m - 1):
            curr = [1] * n
            for j in range(n - 2, -1, -1):
                curr[j] = curr[j + 1] + dp[j]
            dp = curr
        return dp[0]