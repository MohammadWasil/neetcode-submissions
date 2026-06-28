class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # insertion sort
        #for i in range(len(nums)):
        #   j = i - 1
        #    while j >= 0 and nums[j+1] < nums[j]:
        #        # swap
        #        temp = nums[j+1]
        #        nums[j+1] = nums[j]
        #        nums[j] = temp
        #        j-=1
        #return nums
        # Time complexity: O(n.m)
        # Space complexity: O(m)

        # Merge Sort
        def merge(arr, l, m, r):
            i, j, k = l, 0, 0
            left_arr = arr[l:m+1]
            right_arr = arr[m+1:r+1]

            # iterate left and right array
            while j < len(left_arr) and k < len(right_arr): # for th pointer to not go out of bound
                if left_arr[j] < right_arr[k]:
                    arr[i] = left_arr[j]
                    j += 1
                else:
                    arr[i] = right_arr[k]
                    k += 1
                i += 1
            
            # some values can be remaining, either in left or right array
            # we dont know.
            while j < len(left_arr):
                arr[i] = left_arr[j]
                j += 1
                i += 1
            
            while j < len(right_arr):
                arr[i] = right_arr[k]
                k += 1
                i += 1 
        
        def mergeSort(arr, l, r):
            if (r - l + 1) == 1:
                return arr

            m = (l+r) // 2
            mergeSort(arr, l, m) # sorting for the left array
            mergeSort(arr, m+1, r) # sorting for the right array

            merge(arr, l, m, r)
            
            return arr

        return mergeSort(nums, 0, len(nums) - 1)
