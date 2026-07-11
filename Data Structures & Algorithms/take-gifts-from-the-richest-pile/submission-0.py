class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
                [-25,-64,-9,-4,-100]

                -100
            -64      -25
        -9  -4

        take the max -> 100 -> sqrt(100) -> 10 -> push

                -64
            -25     -9
        -4  -10

        repeat!
        END.

        Add all the values in the list.
        """

        gifts = [-1 * gift for gift in gifts]

        heapq.heapify(gifts)
        i=0
        while i < k:
            max_val = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(max_val)))
            i += 1
        
        return -sum(gifts)

        