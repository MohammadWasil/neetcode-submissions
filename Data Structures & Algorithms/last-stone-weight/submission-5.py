class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
                [-2, -3, -6, -2, -4] to create max heap.

                    -6
                -4      -3
            -2     -2
        """

        stones = [-1 * stone for stone in stones]

        heapq.heapify(stones) # max heap

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if abs(x) < abs(y): # -6 < -4
                y = y - x # -4 - -6 = 2

                heapq.heappush(stones, y)
        stones.append(0)
        return abs(stones[0])
