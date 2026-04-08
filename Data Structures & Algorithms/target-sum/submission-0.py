class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(total, i, nums, target):
            if i >= len(nums):
                return 1 if total == target else 0
            
            return dfs(total - nums[i], i + 1, nums, target) + dfs(total + nums[i], i + 1, nums, target)
        
        count = dfs(0, 0, nums, target)
        print(count)
        return count