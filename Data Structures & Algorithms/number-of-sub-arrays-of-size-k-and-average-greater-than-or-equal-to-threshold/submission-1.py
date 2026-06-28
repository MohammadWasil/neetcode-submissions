class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = 0
        res = 0
        for r in range(len(arr)):
            current_sum += arr[r]

            if r >= k-1:
                res += int(bool((current_sum/k) >= threshold))
                current_sum -= arr[r - (k-1)]
        return res