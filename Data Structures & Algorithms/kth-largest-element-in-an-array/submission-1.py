class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for i in range(0, k):
            heapq.heappush(heap, nums[i])
        
        i = k
        while i < len(nums):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
            i+= 1
        
        return heap[0]
        