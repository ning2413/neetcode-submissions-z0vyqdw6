class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        maxheap = []
        num = set(nums)
        for n in num:
            heapq.heappush(maxheap, [-1 * freq[n], n])
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(maxheap)[1])
        return ans