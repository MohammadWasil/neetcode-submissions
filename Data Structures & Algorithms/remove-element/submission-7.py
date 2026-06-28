class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == val:
                # perform swap
                nums[l] = nums[r]
                r -= 1 # move the right pointer to the left
            else:
                l += 1

        return l
    