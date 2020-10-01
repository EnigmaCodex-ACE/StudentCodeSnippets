# https://leetcode.com/problems/single-number/description/#

class Solution:
# Time Complexity: O(N) 
# Space Complexity: O(N)
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for key, value in d.items():
            if value == 1:
                return key
