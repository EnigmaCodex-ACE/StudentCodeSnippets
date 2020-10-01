# https://leetcode.com/problems/sort-colors/
# Medium

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time complexity: O(N)        
        d = {0:0, 1:0, 2:0}
        for num in nums:
            d[num] += 1
        for i in range(d[0]):
            nums[i] = 0
        for i in range(d[0], d[0] + d[1]):
            nums[i] = 1
        for i in range((d[0] + d[1]), d[0] + d[1] + d[2]):
            nums[i] = 2