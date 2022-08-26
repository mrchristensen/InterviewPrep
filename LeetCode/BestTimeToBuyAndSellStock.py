# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Runtime: 990 ms, faster than 98.04% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 86.17% of Python3 online submissions for Best Time to Buy and Sell Stock.
    
# 49 minutes

# Time Complexity: O(n)
# Space Complexity: O(1)

import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_price = (prices[0], 0)
        highest_price = (prices[0], 0)
        best_profit = 0
        
        for i in range(len(prices)):
            if(prices[i] > highest_price[0]):
                highest_price = (prices[i], i)
                if(highest_price[0] - lowest_price[0] > best_profit):
                    best_profit = highest_price[0] - lowest_price[0]
                
            if(prices[i] < lowest_price[0]):
                lowest_price = (prices[i], i)
                highest_price = (prices[i], i)
           
            
        return best_profit
    
