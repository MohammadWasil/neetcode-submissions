class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_value = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                difference = prices[j] - prices[i]
                if difference > max_value:
                    max_value = difference
        return max_value
        