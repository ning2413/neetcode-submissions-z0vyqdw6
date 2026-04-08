class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for x, y in points:
            distance = math.sqrt((x)**2 +(y)**2)
            heapq.heappush(closest, (distance, [x, y]))
        ans = []
        while len(closest) > (len(points) - k):
            _, pts = heapq.heappop(closest)
            ans.append(pts)
        return ans