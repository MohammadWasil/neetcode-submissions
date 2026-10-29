class Solution:
    def trap(self, height: List[int]) -> int:
        """l = 0
        r = 1

        # keep on moving until we find r which has higher height than l
        while r < len(height)-1 and height[l] < height[r]:
            l += 1
            r += 1
        
        area = 0
        local_area = 0
        while r < len(height)-1:
            local_area += height[l] - height[r]
            r += 1

            if height[r] == height[l]:
                area += local_area
                l = r
                r += 1
                local_area = 0
            else:


        return area"""
        if not height or len(height) < 3:
            return 0
            
        l = 0
        r = 1

        # keep on moving until we find r which has higher height than l
        while r < len(height) and height[l] < height[r]:
            l += 1
            r += 1
        
        area = 0
        while l < len(height) - 1:
            r = l + 1
            max_r = r
            
            # Look ahead to find either a bar >= height[l] or the max available bar
            while r < len(height):
                if height[r] >= height[l]:
                    max_r = r
                    break
                if height[r] > height[max_r]:
                    max_r = r
                r += 1
                
            # Calculate water trapped between l and max_r
            local_area = 0
            bound = min(height[l], height[max_r])
            for i in range(l + 1, max_r):
                local_area += bound - height[i]
                
            area += local_area
            l = max_r  # Move left pointer to our new boundary
            
        return area
        