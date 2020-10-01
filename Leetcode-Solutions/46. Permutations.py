# Medium
# https://leetcode.com/problems/permutations/

# Time Complexity: O(n!)
# Space Complexity: O(n!)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            res = []
            for i in range(len(nums)):
                curr = nums[i]
                rem = nums[:i] + nums[i+1:]
                perms = self.permute(rem)
                for p in perms:
                    res.append([curr] + p)
            return res
