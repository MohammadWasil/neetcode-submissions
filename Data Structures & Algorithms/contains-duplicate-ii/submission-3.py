class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        nums = [2, 1, 3, 1], k=3
                   i     j
        """
        i=0
        while i < len(nums):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
            i += 1
        return False
        