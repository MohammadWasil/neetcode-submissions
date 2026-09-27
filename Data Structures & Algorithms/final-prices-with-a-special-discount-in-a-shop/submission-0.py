class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        """
        Time Complexity: O(n2)
        Space Complexity: O(n)
        """

        l = 0
        
        difference = []
        while l < len(prices):
            r = l + 1
            while r < len(prices):

                if prices[l] >= prices[r]:
                    difference.append(prices[l] - prices[r])
                    # stop the inner while loop
                    break
                    #r = len(prices)
                r += 1
            
            # if we exhausted the r pointer, append the original value.
            if r == len(prices):
                difference.append(prices[l])
            l += 1
        
        return difference
                
        
