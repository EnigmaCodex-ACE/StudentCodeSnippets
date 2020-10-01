# Easy
# https://leetcode.com/problems/valid-palindrome/

import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool"""
        d=re.sub('[\W_]+', '',s).lower()
        return d==d[::-1]

