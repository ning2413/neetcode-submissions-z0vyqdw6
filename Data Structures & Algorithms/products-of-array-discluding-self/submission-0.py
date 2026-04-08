class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * (n + 1)
        right = [1] * (n + 1)
        for i in range(n):
            left[i + 1] = nums[i] * left[i]
            right[i + 1] = nums[n - i - 1] * right[i]

        result = [1] * (n)
        for i in range(n):
            result[i] = left[i] * right[n - i - 1]
        print(left)
        print(right)
        print(result)
        return result
