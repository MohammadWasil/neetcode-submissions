class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        [1, 1, 1, 2, 3, 4]
         i  j -> check if i and j are same, if yess, move j + 1
         i     j -> move j + 1
         i        j -> i and j are not the same, move j value to i+1
        =1, 2, 1, 2, 3, 4], and then increment j
            i        j -> not the same, move j to i+1
        =1, 2, 3, 2, 3, 4
               i     j > also oncrement j
               i        j -> i and j are not same, move j value into i+1
        =1, 2, 3, 4, 3, 4
                  i     j -> j ends the list
                    return i+1 -> total number of elements.
        """

        i = 0
        j = i+1

        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        
        return i+1


