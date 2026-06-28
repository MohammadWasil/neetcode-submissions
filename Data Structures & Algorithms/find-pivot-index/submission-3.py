class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        [1,7,3,6,5,6]
         i j 
         0 27
           1 20
             9 17
               11 11 <- same
        """
        """total_length = len(nums)

        for n in range(len(nums)):
            left_sum = 0
            right_sum = 0

            for i in range(n):
                left_sum += nums[i] # 0
            for j in range(n+1, total_length):
                right_sum += nums[j]
            if left_sum == right_sum:
                return n
        return -1"""

        """
        [1,7,3,6,5,6]
        total_sum=28
        prefix = 
        [0, 1, 8, 11, 17, 22, 28]
            i=1
            ls=1
            rs=28-8=20
                
                i=2
                ls=8
                rs=28-11=17

                    i=3
                    ls=11
                    rs=28-17=11
        """
        n = len(nums)
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        for i in range(n):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[n] - prefix_sum[i+1]
            if left_sum == right_sum:
                return i
        return -1







