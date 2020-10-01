# Medium
# https://leetcode.com/problems/product-of-array-except-self/solution/

# Time complexity : O(N)
# Space complexity : O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [nums[0]]
        r = [nums[len(nums) - 1]]
        
        for i in range(1, len(nums)):
            l.append(l[i-1] * nums[i])
            
        for i in range(len(nums)-2, -1, -1):
            r.append(r[(len(nums) - 2) - i] * nums[i])
            
        r = r[::-1]
        res = []
        for i in range(len(nums)):
            if i == len(nums) - 1:
                res.append(l[i-1])
            elif i == 0:
                res.append(r[i+1])
            else: 
                res.append(l[i-1] * r[i+1])
        return res


# Memory Limit : O(1) Solution:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        
        for i in range(1, len(nums)):
            ans.append(ans[i-1] * nums[i - 1])
        
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * r
            r *= nums[i]
            
        return ans