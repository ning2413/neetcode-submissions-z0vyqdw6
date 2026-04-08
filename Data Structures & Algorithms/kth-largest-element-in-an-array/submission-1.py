class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = []
        for i in nums:
            heapq.heappush(largest, i)
            if len(largest) > k:
                heapq.heappop(largest)
        return largest[0]