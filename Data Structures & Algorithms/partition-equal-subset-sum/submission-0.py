class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for n in nums:
            total += n
        if total % 2 == 1:
            return False
        
        total = total // 2
        n = len(nums)
        dp = [[0] * (total + 1) for _ in range(n)] 

        for i in range(total):
            if i >= nums[0]:
                dp[0][i] = nums[0]
        for i in range(1, n):
            for t in range(1, total + 1):
                skip = dp[i - 1][t]
                include = 0
                if t - nums[i] >= 0:
                    include = nums[i] + dp[i - 1][t - nums[i]]
                dp[i][t] = max(skip, include)
        return total == dp[n - 1][total]