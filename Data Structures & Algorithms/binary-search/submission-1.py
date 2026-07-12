class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        [-1,0,2,4,6,8]
          l    m    r

          # check if target is on the left or right side
          # taregt > middle -> l=m+1   [l---r m ---X]
          # taregt < middle -> r=m-1   [X---- m l--r]
    
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r-l) // 2)

            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
            else:
                return m
        
        return -1



