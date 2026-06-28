class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        list = [5, 3, 6, 4], target = 7
                   i     j
        """

        i = 0
        while i >= 0:
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            i += 1

        