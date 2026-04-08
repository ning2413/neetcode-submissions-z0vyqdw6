class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for i in stones:
            maxheap.append(-i)
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            x, y = heapq.heappop(maxheap), heapq.heappop(maxheap)
            x = -1 * x
            y = -1 * y
            if x == y:
                continue
            if x > y:
                heapq.heappush(maxheap, -1 * (x - y))
            else:
                heapq.heappush(maxheap, -1 * (y - x))
        
        return -1 * maxheap[0] if maxheap else 0