class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        i,j = 0, n-1
        while i < j:
            maxArea = max(maxArea, min(heights[i],heights[j])*(j-i))
            if heights[i]<heights[j]:
                i +=1
            else:
                j -=1
        return maxArea
        