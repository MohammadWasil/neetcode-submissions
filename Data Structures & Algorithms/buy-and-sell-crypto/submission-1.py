class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        max_profit = 0
        [10,1,5,6,7,1]
         l  r -> 1-10=-9 <- max_profit
         l    r -> 5-10=-5 <- max_profit
         l      r -> 6-10=-4 <- max_profit
         l         r -> 7-10=-3 <- max_profit
         l           r -> 1-10=-9 < not the max profit
         -> l r -> 5-1=4 <- max_profit
         -> l   r -> 6-1=5 <- max_profit
         -> l     r -> 7-1=6 <- max_profit
         -> l       r -> 1-1=0 <- not the max_profit
         ---> l r -> 6-5=1 <- not the max_profit
         ---> l   r -> 7-5=2 <- not the max_profit
         ---> l     r -> 1-5=-4 <- not the max_profit
         ... and so on.
         when l == r , stop the Loop!
        r-l
        """
        l = 0
        r = 1
        max_profit = 0

        
        while r < len(prices):
            if prices[l] < prices[r]:
                difference = prices[r] - prices[l]
                max_profit = max(difference, max_profit)
                #if difference > max_profit:
                #    max_profit = difference
            else:
                l = r
            r += 1
        return max_profit
