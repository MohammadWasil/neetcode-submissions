class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        ietarte all the values in th list
        And calculate their distances
        """

        # iterate all the values in th list: [[0,2],[2,2]]
        # And calculate their distances from the origin
        distances = []
        for p in points:
            distance = (p[0] ** 2) + (p[1] ** 2)
            # add distance in the nested list
            # [[2, 0, 2], [sqrt(8), 2, 2]]
            #  [[Distance, x, y]]
            distances.append([distance, p[0], p[1]])

        # heapify the nested list (it will be performed on the first element, distance)
        heapq.heapify(distances)

        res = []
        # pop out K elements from the heap, 
        while k > 0:
            distance, x, y = heapq.heappop(distances)
            # and get their x, y values, nested list
            res.append([x, y])

            k -= 1

        return res


        