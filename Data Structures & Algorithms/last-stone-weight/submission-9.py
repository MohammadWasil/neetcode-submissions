class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-stone for stone in stones]
        
        # This way we can create an inverse heap.
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if y == x:
                continue
            elif abs(y) > abs(x):
                heapq.heappush(stones, y-x)
        stones.append(0)
        return abs(stones[0])
