# Easy
# https://leetcode.com/problems/merge-sorted-array/

# Time Complexity : O(n + m) where n = number of elements in nums1 and m = no.of elements in nums2
# Space Complexity: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Algo - We are bubbling max element to the end of the nums1 at every iteration
        aindex = len(nums1) - len(nums2) - 1 # index at where nums1 max element is
        bindex = len(nums2) - 1 # index at where nums2 max element is
        merge_index = len(nums1) - 1 # last index at where we start out insertion
        
        while aindex >= 0 and bindex >= 0:
            if nums1[aindex] >= nums2[bindex]:
                nums1[merge_index] = nums1[aindex]
                aindex -= 1
            else:
                nums1[merge_index] = nums2[bindex]
                bindex -= 1
            merge_index -= 1
        
        # If b index > 0
        while bindex >= 0: 
            nums1[merge_index] = nums2[bindex]
            merge_index -= 1
            bindex -= 1