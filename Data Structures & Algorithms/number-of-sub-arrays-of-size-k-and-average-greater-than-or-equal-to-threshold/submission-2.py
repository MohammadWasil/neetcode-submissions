class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        [2,2,2,2,5,5,5,8], k=3 and threshold=4
        return -> number of subarrays each of size k=3 with average value >= 4(=threshold)
        window of size k=3

        res_subarray = 0
        [2,2,2,2,5,5,5,8]
           i   j
         window=[x, x, 2, 2, 5]
        loop ->
        window = [2, 2, 2], 
        when size is exceeded, stop the window -> 
        cal the avreage -> if avg > threhsold -> res_subarray -> +1
        and update my window values -> remove the frsts element and add the next element.
        """
        res_num_subarray = 0
        
        window_sum = sum(arr[:k-1]) # initially set the sum

        for i in range(len(arr) - k + 1):
            window_sum += arr[i + k - 1]
            if (window_sum / k) >= threshold:
                res_num_subarray += 1
            window_sum -= arr[i]
            
        
        return res_num_subarray
