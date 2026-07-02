class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Sliding window approach:
        nums = [1, 2, 3, 1, 5], k=3
                i        j
        Keep on adding new elements in the window, until sze exceeded.
        sieze exceed -> remove the first eleemtn from the window
        => sliding window of size exceeded when j-i > k
        if the element already exist in the window, True, else false

        nums = [1, 2, 3, 7, 5], k=3
        index:  0  1  2  3  4 
                   i        j
        window = {2, 3, 7, 5}

        """

        window = set()
        i = 0

        for j in range(len(nums)):
            
            # remove th element from the window once the sliding window size exceed.
            if j - i > k:
                window.remove(nums[i])
                i += 1
            if nums[j] in window:
                return True
            window.add(nums[j])
        return False
        
        