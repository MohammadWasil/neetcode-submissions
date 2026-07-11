class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        -> [1, 2, 3, 3]

                1
            2       3
        3   null    null    null

        """

        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
        """
                2
            3       3
        """

    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]













        
