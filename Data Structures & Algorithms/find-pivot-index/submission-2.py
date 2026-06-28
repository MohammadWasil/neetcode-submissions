class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        [1,7,3,6,5,6]
         i j 
         0 27
           1 20
             9 17
               11 11 <- same
        
        #left_sum = 
        #right_sum
        """
        total_length = len(nums)

        for n in range(len(nums)):
            left_sum = 0
            right_sum = 0

            for i in range(n):
                left_sum += nums[i] # 0
            for j in range(n+1, total_length):
                right_sum += nums[j]
            if left_sum == right_sum:
                return n
        return -1
