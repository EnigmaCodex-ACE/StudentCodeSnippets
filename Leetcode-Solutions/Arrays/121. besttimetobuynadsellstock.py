# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

# Time Complexity: O(N) 
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import math
        mini = math.inf
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            elif prices[i] - mini > max_profit:
                max_profit = prices[i] - mini
        return max_profit