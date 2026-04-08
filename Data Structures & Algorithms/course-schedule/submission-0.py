class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for i in range(n):
            a, b = prerequisites[i]
            indegree[a] += 1
            adj[b].append(a)
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            numCourses -= 1
            for neighbors in adj[course]:
                indegree[neighbors] -= 1
                if indegree[neighbors] == 0:
                    q.append(neighbors)
        return numCourses == 0
