class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        
        hashmap2 = {}
        for c in t:
            hashmap2[c] = hashmap2.get(c, 0) + 1

        return hashmap == hashmap2