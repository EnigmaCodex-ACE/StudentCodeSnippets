# https://leetcode.com/problems/contains-duplicate/
# Time Complexity: O(n)
# Space Complexity: O(N)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                return True
            d[num] = i