class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
        min_l = prices[0]
        max_value = 0
     

        for num in prices:
            max_value = max(max_value, num-min_l)
            min_l = min(min_l, num)
        
        return max_value