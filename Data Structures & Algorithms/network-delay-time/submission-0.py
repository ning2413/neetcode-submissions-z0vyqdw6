class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append([v, t])
        
        distance = {}
        minheap = [(0, k)] 
        while minheap:
            time, node = heapq.heappop(minheap)
            if node in distance:
                continue
            distance[node] = time
            for nei, t in adj[node]:
                if nei not in distance:
                    heapq.heappush(minheap, (t + time, nei))
        return max(distance.values()) if len(distance) == n else -1 
            
