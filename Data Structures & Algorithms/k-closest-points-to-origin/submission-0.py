class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for x, y in points:
            distance = math.sqrt((x)**2 +(y)**2)
            heapq.heappush(closest, (-1 * distance, [x, y]))
        print(closest)

        while len(closest) > k:
            heapq.heappop(closest)
        ans = []
        for _, pts in closest:
            ans.append(pts)
        return ans