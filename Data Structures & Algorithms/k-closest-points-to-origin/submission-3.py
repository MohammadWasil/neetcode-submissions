class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for p in points:
            distance = -math.sqrt( (0-p[0])**2 + (0-p[1])**2 )

            heapq.heappush(heap, [distance, p[0], p[1]])

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while len(heap) > 0:
            distance, x, y = heapq.heappop(heap)
            res.append([x, y])
        
        return res
        