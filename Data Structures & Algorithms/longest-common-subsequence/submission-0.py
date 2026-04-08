class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        dp = [0] * (m + 1)

        for i in range(n):
            curr = [0] * (m + 1)
            for j in range(m):
                if text1[i] == text2[j]:
                    curr[j + 1] = 1 + dp[j]
                else:
                    curr[j + 1] = max(dp[j + 1], curr[j])
            dp = curr
        return dp[m]
