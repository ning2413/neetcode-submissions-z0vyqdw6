class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currSum = 0
        currMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        total = 0
        for n in nums:
            currSum = max(currSum + n, n)
            currMin = min(currMin + n, n)
            maxSum = max(maxSum, currSum)
            minSum = min(minSum, currMin)
            total += n
        return max(total - minSum, maxSum) if maxSum > 0 else maxSum