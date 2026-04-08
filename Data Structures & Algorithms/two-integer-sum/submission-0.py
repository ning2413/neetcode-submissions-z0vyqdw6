class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        ans = []
        for i, j in enumerate(nums):
            complement = target - j
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[j] = i
             
        