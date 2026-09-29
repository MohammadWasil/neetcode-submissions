class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[-1]
        s = set()
        duplicate = []
        for num in nums:
            if num in s:
                duplicate.append(num)
            else:
                s.add(num)
        
        difference = set(nums) - set(duplicate)
        return sorted(difference)[-1] if len(difference) >= 1 else -1
