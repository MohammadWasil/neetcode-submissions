class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        max_area = 0
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            area = w * h
            max_area = max(area, max_area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area