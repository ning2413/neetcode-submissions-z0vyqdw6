class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position = sorted(zip(position, speed), reverse=True)
        times = []

        for pos, spd in position:
            time = (target - pos) / spd
            if times and time <= times[-1]:
                continue
            times.append(time)
        return len(times)