# Medium
# https://leetcode.com/problems/reverse-words-in-a-string/

# Time Complexity: O(N)
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])