# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Runtime: 990 ms, faster than 98.04% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 86.17% of Python3 online submissions for Best Time to Buy and Sell Stock.

# 49 minutes

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        highest_price = prices[0]
        best_profit = 0

        for i in range(len(prices)):
            # If this is a new highest (update highest price)
            if(prices[i] > highest_price):
                highest_price = prices[i]
                # If these profits are the best we've seen (update best profit)
                if(highest_price - lowest_price > best_profit):
                    best_profit = highest_price - lowest_price

            # If we found a new low
            if(prices[i] < lowest_price):
                # Update new low and reset highest prices
                lowest_price = prices[i]
                highest_price = prices[i]

        return best_profit
