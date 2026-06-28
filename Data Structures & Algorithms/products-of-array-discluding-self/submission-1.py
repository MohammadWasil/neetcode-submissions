class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]
        total_prod = 48

        for each elements e in arra:
            new_arra[total_prod /= e]

        prefix=1 [1,2,4,6] postfix=1

        create a prefix product, leaving the last element
        [prefix, prefix*num[0], prefix*num[1], prefix*num[2]]
        [1, 1, 2, 8]

        create a postfix product in reverse, leaving the first element
        [suffix*num[0+1], suffix*num[1+1], suffix*num[2+1], suffix]
        [1]
        [48, 24, 6, 1, ]
        Multiple suffix and prefix:
        [48, 24, 12, 8]
        """

        prefix = 1
        prefix_arr = [prefix]
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            prefix_arr.append(prefix)

        # [48, 24, 6, 1]
        postfix = 1 #6
        postfix_arr = [postfix for _ in range(len(nums))] 
        for i in range(len(nums)-1, 0, -1):
            postfix *= nums[i]
            postfix_arr[i-1] = postfix

        return [pre*post for pre,post in zip(prefix_arr, postfix_arr)]
