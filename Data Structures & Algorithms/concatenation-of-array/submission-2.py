class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums) * 2
        #return nums + nums
        for i in range(len(nums)):
            ans[i] = ans[i+len(nums)] = nums[i]
        return ans
        