class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        hashmap = {}
        for i in range(n):
            diff = target - numbers[i]
            if diff in hashmap:
                return [hashmap.get(diff), i + 1]
            hashmap[numbers[i]] = i + 1