class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)
        
        q = deque()
        visit = set()
        q.append((beginWord, 1))
        visit.add(beginWord)

        while q:
            word, step = q.popleft()

            if word == endWord:
                return step

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                for nei in patterns[pattern]:
                    if nei not in visit:
                        q.append((nei, step + 1))
                        visit.add(nei)

        return 0
