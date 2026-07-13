class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        [1,7,2,5,4,7,3,6]
         0,1,2,3,4,5,6,7
         l             r -> cal area-> min(1,6) * r-l = 1*(7-0) = 7
           l           r -> cal area-> min(7,6) * r-l = 6*(7-1) = 36
           l         r   -> cal area-> min(7,3) * r-l = 3*(6-1) = 15
           l       r     -> cal area-> min(7,7) * r-l = 7*(5-1) = 28
           l     r       -> cal area-> min(7,4) * r-l = 4*(4-1) = 12
           l   r         -> cal area-> min(7,5) * r-l = 5*(3-1) = 10
           l r           -> cal area-> min(7,2) * r-l = 2*(2-1) = 2
           l=r -> stop
        """
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            max_area = max(min(heights[l], heights[r]) * (r-l), max_area)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return max_area

        