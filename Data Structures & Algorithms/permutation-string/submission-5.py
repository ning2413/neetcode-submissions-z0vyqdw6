class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)
        for c in s1:
            freq[c] += 1
        
        count = defaultdict(int)
        l = 0
        for r, c in enumerate(s2):
            count[c] += 1
            size = r - l + 1
            if size > len(s1):
                count[s2[l]] -= 1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l += 1
            size = r - l + 1
            print(count, freq)
            if size == len(s1) and count == freq:
                return True
        return False
