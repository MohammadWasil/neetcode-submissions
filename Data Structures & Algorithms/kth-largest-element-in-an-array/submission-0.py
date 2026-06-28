class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        k = 2 -> second largets element
        [2,3,1,5,4] -> [1, 2, 3, 4, 5]

        min_heap = []
        Limit the heap to only have k elements/nodes: k <= 2
        whenever the ehap exceeds k element, pop the minimum value

            4
        5       _

        return the min value from the heap

        [2,3,1,1,5,5,4], K = 3
        initliaze min_heap = []
        1. Add 2
        2. Add 3
        3. Add 1
        4. Add 1

                1
            1       2
        3

        5. len(heap) exceeded k > 3, so remove min value -> 1
            1
        3       2
        
        6. Add 5
                1
            3       2
        5

        7. len(heap) exceeded k > 3, so remove min value -> 1
            2
        3       5

        8. Add 5
                2
            3       5
        5

        9. len(heap) exceeded k > 3, so remove min value -> 2
            3
        5       5

        10. Add 4 -> (n * log k)
                3
            5       5
        4

        11. len(heap) exceeded k > 3, so remove min value -> 3 -> (n-k) * log k
                4
            5       5

        return heap.pop -> min value - O(1)
        
        """

        min_heap = []
        for i in nums:
            heapq.heappush(min_heap, i)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return heapq.heappop(min_heap)
