# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy sell once 
        # cum max profit and update lowest price
        lowest = float('inf')
        max_profit = float('-inf')

        for i in range(len(prices)):
            if prices[i] < lowest: 
                lowest = prices[i]
            
            max_profit = max(max_profit, (prices[i] - lowest))

        return max_profit