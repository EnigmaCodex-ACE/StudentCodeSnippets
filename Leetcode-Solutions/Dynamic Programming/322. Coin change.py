# Medium
# https://leetcode.com/problems/coin-change/

# Time Complexity : O(amount * coins)
# Space Complexity : O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import math
        arr = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            mini = math.inf
            for coin in coins:
                if coin <= i:
                    mini = min(mini, arr[i - coin] + 1)
            arr[i] = mini
        if arr[amount] == math.inf:
            return -1
        return arr[amount]