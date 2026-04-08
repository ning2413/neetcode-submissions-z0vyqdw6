class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for n1, n2 in edges:
            n = max(n, n1, n2)

        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node):
            res = node
            while parent[res] != res:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
                
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        ans = []
        for n1, n2 in edges:
            if not union(n1, n2):
                ans.append([n1, n2])
        return ans[-1]
