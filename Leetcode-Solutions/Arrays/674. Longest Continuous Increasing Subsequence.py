# Easy
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

# Time Complexity : O(N)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        out = 0
        i = 0
        while i < len(nums):
            curr = 1
            if i == 0:
                out = 1
                i += 1
                continue
            while i < len(nums) and nums[i] > nums[i - 1]:
                i += 1
                curr += 1
            out = max(curr, out)
            i += 1
        return out