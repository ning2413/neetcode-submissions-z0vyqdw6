class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Store indices of temperature on given day i
        temps = []
        ans = [0] * len(temperatures)
        # For subsequent days we check if the temperature is greater
        # than all the previous temperatures in the stack.
        # If so we will pop those values and append the difference
        # Between the current temp index and that one
        temps.append(0)
        for i in range(1, len(temperatures)):
            while temps and temperatures[temps[-1]] < temperatures[i]:
                ans[temps[-1]] = i - temps[-1]
                temps.pop()
            temps.append(i)
        return ans
