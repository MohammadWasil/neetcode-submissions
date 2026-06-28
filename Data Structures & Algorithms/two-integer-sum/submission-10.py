class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Brute-Force
        #for i in range(len(nums)):
        #    for j in range(i+1, len(nums)):
        #        if nums[i] + nums[j] == target:
        #            return [i, j]
        #return []

        # hashmaps:
        hashmap = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[num] = i

        # Two pointer :
        # the below solutuon will not work when we have duplcaite values
        #index_hashmap = {k: v for v, k in enumerate(nums)}
        #nums.sort()
        #i = 0
        #j = len(nums) - 1
        #while i < j:
        #    sum_ = nums[i] + nums[j]
        #    if target < sum_:
        #        j -= 1
        #    elif target > sum_:
        #        i += 1
        #    else:
        #        return [index_hashmap[nums[i]], index_hashmap[nums[j]]]
        #        #return [i, j]
        #return []



