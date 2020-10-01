# Easy
# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(n log n) using sorting
        # Space: O(1)        
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return nums[-1] + 1

        # Time: O(n) Space: O(1) swaping in place
        # for i in range(len(nums)):
        #     temp = nums[i]
        #     while temp < len(nums) and nums[temp] != temp:
        #         nums[temp], temp = temp, nums[temp]
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return nums[-1] + 1
    
        # Efficient solution using bitmanipulation
        # Time: O(n) 
        # Space: O(1)        
        # n = len(nums)
        # for i in range(len(nums)):
        #     n ^= (i ^ nums[i])
        # return n

        # Efficient solution using sum of n natural numbers
        # Time: O(n) 
        # Space: O(1)        
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum