class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best, worst = 1, 1
        maxproduct = max(nums)
        for n in nums:
            if n == 0:
                best, worst = 1, 1
                continue
            tmp = best * n
            best = max(best * n, worst * n, n)
            worst = min(tmp, worst * n, n)
            maxproduct = max(maxproduct, best)
        return maxproduct