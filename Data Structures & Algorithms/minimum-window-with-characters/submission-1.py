class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = defaultdict(int)
        for i in t:
            freq[i] += 1
        
        have, need = 0, len(freq)
        bestL, bestR = 0, 0
        bestWin = 1000000
        l = 0
        count = defaultdict(int)

        for r, c in enumerate(s):
            count[c] += 1
            if c in freq and count[c] == freq[c]:
                have += 1
                while have == need:
                    if bestWin > r - l + 1:
                        bestL = l
                        bestR = r
                        bestWin = r - l + 1
                    count[s[l]] -= 1
                    if s[l] in freq and count[s[l]] < freq[s[l]]:
                        have -= 1
                    l += 1

        return "" if bestWin == 1000000 else s[bestL:bestR+1]

        
                    


