class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max(nums[0], self.helper(nums[0:n - 1]), self.helper(nums[1:n]))
    def helper(self, nums):
        prev1, prev2 = 0, 0 
        for num in nums:
            curr = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = curr
        return prev1
        