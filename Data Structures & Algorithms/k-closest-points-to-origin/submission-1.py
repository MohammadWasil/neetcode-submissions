class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        # iterate all the values in th list: [[0,2],[2,2]] -> O(n)
        # And calculate their distances from the origin
        distances = []
        for p in points:
            distance = (p[0] ** 2) + (p[1] ** 2)
            # add distance in the nested list
            # [[2, 0, 2], [sqrt(8), 2, 2]]
            #  [[Distance, x, y]]
            distances.append([distance, p[0], p[1]])

        # heapify the nested list (it will be performed on the first element, distance)
        heapq.heapify(distances) # O(n)

        res = [] # O(k) = Space complexity
        # pop out K elements from the heap, 
        while k > 0:
            distance, x, y = heapq.heappop(distances) # O(k.log n)
            # and get their x, y values, nested list
            res.append([x, y])

            k -= 1

        # TC: O(n+k*log n)
        # Space: O(n)+O(k) = O(n), since n >= k

        return res
        """
        
        # Max Heap
        max_heap = []
        # Iterate all the points
        for p in points:
            # create max heap by adding a negative infront of the distanes
            distance = -(p[0]**2 + p[1]**2)
            heapq.heappush(max_heap, [distance, p[0], p[1]])

            # in the loop, limit the heap to max k elements
            # and keep on poping elements if the len of the heap is greater than K
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Iterate the heap and keep on popping min values and adding to the list
        res = []
        while len(max_heap)>0:
            distance, x, y = heapq.heappop(max_heap)
            res.append([x, y])

        return res
