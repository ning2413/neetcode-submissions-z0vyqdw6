class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        ans = []
        pacificq = collections.deque()
        atlanticq = collections.deque()
        pacific = set()
        atlantic = set()
        def bfs(q, reachable):
            while q:
                x, y = q.popleft()

                for dx, dy in directions:
                    newX, newY = x + dx, y + dy

                    if 0 <= newX < m and 0 <= newY < n:
                        if (newX, newY) not in reachable:
                            if heights[newX][newY] >= heights[x][y]:
                                q.append([newX, newY])
                                reachable.add((newX, newY))
        for i in range(m):
            pacificq.append([i, 0])
            pacific.add((i, 0))

            atlanticq.append([i, n - 1])
            atlantic.add((i, n - 1))
        for j in range(n):
            pacificq.append([0, j])
            pacific.add((0, j))

            atlanticq.append([m - 1, j])
            atlantic.add((m - 1, j))
        
        bfs(pacificq, pacific)
        bfs(atlanticq, atlantic)
        
        return list(pacific & atlantic)