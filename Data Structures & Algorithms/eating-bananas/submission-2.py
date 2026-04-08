class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = math.inf
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / mid)
            
            if time <= h:
                r = mid - 1
                k = min(k, mid)
            elif time > h:
                l = mid + 1
        return k
