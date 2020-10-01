# Easy
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    # Time complexity : O(n)
    #  Space complexity: O(n)
    
    # Fibonacci sequence     
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        for _ in range(1, n):
            a, b = b, a + b
        return a
        