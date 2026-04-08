class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = defaultdict(int)
        for i in t:
            freq[i] += 1

        count = defaultdict(int)
        formed = {}
        l, bestL, bestR = 0, 0, 0
        bestWin = 1000000
        for r, c in enumerate(s):
            count[c] += 1
            if c in freq and count[c] == freq[c]:
                formed[c] = True

                while len(formed) == len(freq):
                    if bestWin > r - l + 1:
                        bestR = r
                        bestL = l
                        bestWin = r - l + 1
                    if s[l] in freq:
                        count[s[l]] -= 1

                        if count[s[l]] < freq[s[l]]:
                            del formed[s[l]]
                    l += 1
        return "" if bestWin == 1000000 else s[bestL:bestR+1]
                    


