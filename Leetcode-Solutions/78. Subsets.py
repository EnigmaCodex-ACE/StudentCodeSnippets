# Medium
# https://leetcode.com/problems/subsets/

# Time Complexity: O(N * 2*N)
# Space Complexity: O(2*N)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def binary(num, size):
            binary_out = ''
            while num > 0:
                binary_out += str(num % 2)
                num //= 2
            binary_out += (size - len(binary_out)) * '0'
            return binary_out[::-1]
        
        n = len(nums)
        powerset = [] 
        for i in range(2 ** n):
            binary_ = binary(i, n)
            subset = []
            for j in range(n):
                if binary_[j] == '1':
                    subset.append(nums[j])
            powerset.append(subset)
        return powerset