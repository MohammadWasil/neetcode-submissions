class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l = 0
        r = len(nums) - 1
        # Loop as long as the left pointer is less than or equal to the right pointer
        while l <= r:
            print(nums)
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return l
    