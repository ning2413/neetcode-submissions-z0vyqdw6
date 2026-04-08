class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxlen = 0
        ml, mr = 0, 0
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    ml, mr = l, r
                    maxlen = r - l + 1
                r += 1
                l -= 1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    ml, mr = l, r
                    maxlen = r - l + 1
                r += 1
                l -= 1
            
        return s[ml:mr + 1] 
