class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        buckets = [[] for _ in range(n + 1)]
        for num, frequency in freq.items():
            buckets[frequency].append(num)
        
        res = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res