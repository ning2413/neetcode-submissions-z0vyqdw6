class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)
        for r in range(n):
            while stack and heights[stack[-1]] > heights[r]:
                ind = stack.pop()
                height = heights[ind]
                l = stack[-1] if stack else -1
                width = r - l - 1
                maxArea = max(maxArea, height * width)
            stack.append(r)
        while stack:
            ind = stack.pop()
            height = heights[ind]
            l = stack[-1] if stack else -1
            width = n - l - 1
            maxArea = max(maxArea, height * width)
        return maxArea
