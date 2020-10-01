# Easy
# https://leetcode.com/problems/valid-parentheses

# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '[({':
                stack.append(char)
            elif char in '])}':
                if not stack:
                    return False
                if not stack.pop() + char in ['{}', '()', '[]']:
                    return False
        if not stack:
            return True
                        