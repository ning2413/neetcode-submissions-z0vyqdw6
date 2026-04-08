class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            idx = i + nums[i]
            if idx >= len(nums):
                idx = len(nums) - 1
            for j in range(idx, i, -1):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[len(nums) - 1]