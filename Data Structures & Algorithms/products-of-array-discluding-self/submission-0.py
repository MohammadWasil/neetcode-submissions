class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #total_product = math.prod(nums)

        #for i in range(len(nums)):
        #    if nums[i] != 0:
        #        nums[i] = int(total_product / nums[i])
        #    else:
        #        nums[i] = int(total_product)
        #return nums
        prefix_prod = 1
        prefix_prod_skip = [prefix_prod]
        for i in range(1, len(nums)):
            prefix_prod *= nums[i-1]
            prefix_prod_skip.append(prefix_prod)
        
        suffix_prod = 1
        suffix_prod_skip = [suffix_prod] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffix_prod *= nums[i+1]
            suffix_prod_skip[i] = suffix_prod

        return [a*b for a,b in zip(prefix_prod_skip,suffix_prod_skip)]








            