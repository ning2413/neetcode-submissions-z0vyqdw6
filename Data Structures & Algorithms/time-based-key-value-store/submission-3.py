class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.hashmap.get(key):
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        l, r = 0, len(self.hashmap[key]) - 1
        values = self.hashmap[key]
        res = ""
        while l <= r:
            m = (l + r) // 2
            # print(l, r, m, self.hashmap[key][m][0], self.hashmap[key][m][1], timestamp)
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

        
