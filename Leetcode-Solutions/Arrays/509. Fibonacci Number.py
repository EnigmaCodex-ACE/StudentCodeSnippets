# Easy
# https://leetcode.com/problems/fibonacci-number/

# Time Complexity : O(N)
# Space Complexity : O(1)
class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        for _ in range(N):
            a, b = b, a + b
        return a