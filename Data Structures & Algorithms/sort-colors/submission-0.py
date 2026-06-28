class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for i in nums:
            counts[i] += 1

        i = 0
        for j in range(len(counts)):
            for _ in range(counts[j]):
                nums[i] = j
                i += 1
