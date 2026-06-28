class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        res = 1

        for i in range(len(nums)):
            max_i = min_i = nums[i]
            for j in range(i+1, len(nums)):
                min_i = min(min_i, nums[j])
                max_i = max(max_i, nums[j])
                if max_i - min_i > limit:
                    break
                res = max(res, j-i+1)
        
        return res
        