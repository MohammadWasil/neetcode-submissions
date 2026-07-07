class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        window = 3
        res
        [2, 2, 2, 2, 5, 5, 5, 8]
        initally -> window = 2+2=4
        
        [  4 + 2]     -> cal the average, and if avg > threshold -> res+1
                        else remove the first element, and add the next element
            [i x  j] -> not > threshold
               [i x  j] -> not > threshold
                  [i x  j] -> yes, res+1
                      [i x  j] -> yes, res+1
                         [i x j] -> res+1
                           [i  x  j] -> loop ends, j==len(arr)-1
        """
        window = sum(arr[:k-1])
        res = 0

        for i in range(len(arr) - k + 1): # rnun for 6 ietrations
            window += arr[i + k - 1]
            if (window/k) >= threshold:
                res += 1
            window -= arr[i]
        
        return res



