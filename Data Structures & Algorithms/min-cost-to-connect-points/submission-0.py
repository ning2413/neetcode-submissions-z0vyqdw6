class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minheap = []
        visited.add(0)
        for j in range(1, len(points)):
            xj, yj = points[j]
            cost = abs(points[0][0] - xj) + abs(points[0][1] - yj)
            heapq.heappush(minheap, (cost, j))

        mincost = 0
        while len(visited) < len(points):
            cost, i = heapq.heappop(minheap)

            if i in visited:
                continue
            
            visited.add(i)
            mincost += cost
            xi, yi = points[i]
            for j in range(len(points)):
                if j not in visited:
                    xj, yj = points[j]
                    ncost = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(minheap, (ncost, j))

        return mincost
