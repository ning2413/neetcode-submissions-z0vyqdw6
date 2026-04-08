class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = defaultdict(list)
        for s in strs:
            index = ''.join(sorted(s))
            lists[index].append(s)
        return list(lists.values())