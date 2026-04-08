class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, total, numArr = 0, 0, 0
        for r in range(len(arr)):
            if r - l >= k:
                total -= arr[l]
                l += 1
            total += arr[r]
            if (r - l + 1 == k) and ((total / k) >= threshold):
                numArr += 1
        return numArr
