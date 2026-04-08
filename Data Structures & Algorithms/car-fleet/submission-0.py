class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        pairs.sort()
        fleets = 0
        while pairs:
            pos, spd = pairs.pop()
            time = (target - pos) / spd
            while pairs:
                posF, spdF = pairs[-1]
                timeF = (target - posF) / spdF
                if timeF <= time:
                    pairs.pop()
                else:
                    break
            fleets += 1
        print(pairs)
        return fleets