class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        count = 0
        for i in range(len(nums)):
            for curr_sum, count in dp[i].items():
                n_add = curr_sum + nums[i]
                n_sub = curr_sum - nums[i]
                dp[i + 1][n_add] += count
                dp[i + 1][n_sub] += count

        return dp[len(nums)][target]