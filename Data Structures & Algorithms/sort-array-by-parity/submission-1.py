class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        1. find the odd and even num
        2. swap the values.
        [3, 1, 2, 4]
         i        j -> check if i is odd or even, if odd, swap with j value
                    the last value is odd, so decrement j, j-1
         4, 1, 2, 3
         i     j     -> check, i is even, fine, increment i+1
            i  j     -> check, i is odd, swap with j, j-1
         4, 2, 1, 1
            ij       -> when both i and j are on the same index, stop. 
        """

        i = 0
        j = len(nums) - 1

        while i != j:
            if nums[i] % 2 == 1: # odd
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
            else:
                i+=1 

        return nums

