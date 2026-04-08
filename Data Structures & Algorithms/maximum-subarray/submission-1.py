class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxsum = float('-inf')
        for n in nums:
            if n > (curr + n):
                curr = n
            else:
                curr += n
            
            maxsum = max(maxsum, curr)
        return maxsum
