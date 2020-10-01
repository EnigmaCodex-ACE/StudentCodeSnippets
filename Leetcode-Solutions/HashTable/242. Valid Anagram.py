# Easy
# https://leetcode.com/problems/valid-anagram/

# Time Complexity : O(n log n) using sorting
# class Solution:     
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# Time Complexity : O(n) 
# Space Complexity : O(n)
class Solution:     
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for letter in s: # Storing frequencies of letters in s
            d[letter] = d.get(letter, 0) + 1
        
        for letter in t: # reducing the frequencies of the letter
            if letter not in d:
                return False
            d[letter] -= 1 
        
        for key, value in d.items():
            if value != 0:
                return False
        return True