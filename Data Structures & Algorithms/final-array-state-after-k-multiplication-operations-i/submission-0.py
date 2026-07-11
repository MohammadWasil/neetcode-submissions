class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        res -> a second copy of the nums, to update with multiplier and 
        to preserve the location of the numbers.
        Create a min heap with (val, index).
                        (1, 0)
              (2, 1)            (3, 2)
        (5, 3)      (6, 4)

        repeat
        take the min -> (1,0) -> 1xk = 1x2 = 2 -> (2,0<- index) -> push heap
        """

        res = nums[:]

        min_heap = [(num, index) for index, num in enumerate(nums)]
        heapq.heapify(min_heap)

        for _ in range(k):
            min_val, i = heapq.heappop(min_heap)
            res[i] *= multiplier
            heapq.heappush(min_heap, (res[i], i))
        
        return res