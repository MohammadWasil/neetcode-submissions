class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]

        for i in nums:
            count[i] += 1

        i = 0
        for j in range(len(count)):
            for j_index in range(count[j]):
                nums[i] = j
                i += 1

        return nums