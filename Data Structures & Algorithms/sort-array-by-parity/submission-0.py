class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        [3, 1, 2, 4]
         i        j

        if i is even -> i+=1
        else: swap i with j, and j-= 1
        run until i==j, index

        edge case: [0]
        """

        l = 0
        r = len(nums) - 1
        # [3, 1, 2, 4]
        #  l        r
        while l <= r: # 0,2

            if nums[l]%2 == 0: # 
                l += 1
            else:
                # swapping with the element at j
                temp = nums[l] # 3
                nums[l] = nums[r] # 4
                nums[r] = temp # [4, 1, 2, 3]
                            #     l     r

                r -= 1

        return nums





