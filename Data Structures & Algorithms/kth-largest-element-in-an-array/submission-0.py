class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nnums = sorted(nums)
        return nnums[len(nums) - k]