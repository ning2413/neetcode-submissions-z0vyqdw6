class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        l = 0
        maxLen = 0
        maxFreq = 0
        # Try to extend substr by 1 w/o it being in string
        for i in range(len(s)):
            # Check if char exists in freq
            freq[s[i]] = freq.get(s[i], 0) + 1
            maxFreq = max(freq[s[i]], maxFreq)
            while freq.get(s[i]) > 1:
                freq[s[l]] -= 1
                l += 1
            maxLen = max(i - l + 1, maxLen)

        return maxLen

