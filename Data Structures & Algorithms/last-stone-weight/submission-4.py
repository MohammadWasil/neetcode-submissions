class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Always postive
        1 <= stone[i] <= 100
        No empty
        constraint: 1<=len(stone)<=20
        
                [2,3,6,2,4]
        Loop len() > 1
            two largest value heapify(stones)
            heapify  -> max heap O(n)
                    6
                4          3
            2     2
            heap = [6, 4, 3, 2, 2]

            y = heap.pop() = 6 -> O(1)
            x = heap.pop = 4 -> O(1)
                3
            2       2
            OR: 3, 2, 2
            # comparison 
            if x==y -> do nothing
            if x < y: 6-4=2 => y=2 -> push y into the heap

                    3
                2       2
            2

            arr: [3, 2, 2, 2]
        return heap.pop -> the first element, or 0 if None 
        """
        # [2,3,6,2,4]
        stones = [-s for s in stones]
        # [-2,-3,-6,-2,-4]

        heapq.heapify(stones)
        # [-6, -4, -3, -2, -2]

        while len(stones) > 1: # stones = [-2, -2]
            y = heapq.heappop(stones) # -6
            x = heapq.heappop(stones) # -4

            if x > y:
                y = y - x
                heapq.heappush(stones, y)
        stones.append(0)
        return abs(stones[0]) #if len(stones) >= 1 else 0




        