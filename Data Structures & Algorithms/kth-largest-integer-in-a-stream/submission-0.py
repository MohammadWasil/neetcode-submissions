class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        [1, 2, 3, 3]
                1
            2       3
        3   null    null    null
        3rd largest element -> 2
        # pop the values from the heap > take out min value, which would be the Kth largest value
        # inside the heap
                2
            3       3
        null   null    null    null
        2 is the Kth (3rd) largest value
        # Make sure that heap size dos not extend more than K
        # this way the Kth lagets value would be theminimim value in the heap
        """
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)

        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)


    def add(self, val: int) -> int:
        """
        K = 3
        [1, 2, 3, 3]
                2
            3       3
        null   null    null    null

        Add: 3
        1. Push the new value
                2
            3       3
        3   null    null    null        
        2. If the heap size exceed, pop the min value to maintain the size
        3. return the min value from the heap
        """

        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        
        return self.minheap[0]
        
