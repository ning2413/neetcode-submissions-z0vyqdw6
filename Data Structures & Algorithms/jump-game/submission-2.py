class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxidx = 0
        for i in range(len(nums)):
            if i <= maxidx:
                maxidx = max(maxidx, i + nums[i])
                if maxidx >= len(nums) - 1:
                    return True
        return False