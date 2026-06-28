class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            j = i - 1
            while j >= 0 and nums[j+1] < nums[j]:
                # swap
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp
                j-=1
        return nums