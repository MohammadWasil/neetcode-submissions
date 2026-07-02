class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # list = [1, 2, 3] -> False
        # list = [1, 1, 2, 3, 3] -> True

        return len(nums) != len(set(nums))

        