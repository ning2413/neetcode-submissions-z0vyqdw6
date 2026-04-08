class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        count = {}
        for i in range(n):
            count[nums[i]] = count.get(nums[i], 0) + 1
            if count[nums[i]] > 1:
                return True

        return False
