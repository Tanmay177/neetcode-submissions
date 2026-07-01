class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        for i in range(n-1):
            for j in range(i+1,n):
                maxArea = max(maxArea, min(heights[i],heights[j])*(j-i))
        return maxArea
        