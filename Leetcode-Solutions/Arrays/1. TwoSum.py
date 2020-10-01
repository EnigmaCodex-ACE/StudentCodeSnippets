# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(N log N)
        # nums = sorted(zip(nums, range(len(nums))), key=lambda data: data[0])
        # l = 0
        # h = len(nums) - 1
        # while l < h:
        #     if nums[l][0] + nums[h][0] == target:
        #         return nums[l][1], nums[h][1]
        #     elif nums[l][0] + nums[h][0] < target:
        #         l += 1
        #     else:
        #         h -= 1
        
        # Efficient Solution: O(N)
        d = {}
        for index, num in enumerate(nums):
            n = target - num
            if n not in d:
                d[num] = index
            else:
                return [d[n], index]