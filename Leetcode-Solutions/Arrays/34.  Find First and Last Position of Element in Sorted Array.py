# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Medium

class Solution:
#     Linear search : O(n)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        flag = 0
        for index, ele in enumerate(nums):
            if ele == target: 
                if not flag:
                    start = index
                    end = index
                    flag = 1
                else:
                    end = index
        return start, end