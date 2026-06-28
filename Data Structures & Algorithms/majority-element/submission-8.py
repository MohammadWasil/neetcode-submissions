import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        unique_element = list(set(nums))
        unique_element.sort()
        highest_major = 0
        major_element = 0
        for i in unique_element:
            #current_major = sum([i==num for num in nums]) // 2
            current_major = sum([1 for num in nums if num == i]) #// 2
            if current_major >= highest_major:
                highest_major = current_major
                major_element = i
        return major_element
        