class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxSubstr = 0
        freq = {}
        maxFreq = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])
            while (r - l + 1) - maxFreq > k:                
                freq[s[l]] -= 1
                l += 1
            maxSubstr = max(maxSubstr, r - l + 1)
        return maxSubstr