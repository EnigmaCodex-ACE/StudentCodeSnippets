# HARD
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Time Complexity: O(log( m + n))

# As arr1 and arr2 are sorted, we can use merge sort's merge function approach over here
# We can only sort the array upto half because we are finding median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1) 
        n = len(nums2)
        i, j = 0, 0
        mid = 1 + (m + n) // 2
        new_arr = []
        while i < m and j < n and len(new_arr) < mid:
            if nums1[i] <= nums2[j]:
                new_arr.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                new_arr.append(nums2[j])
                j += 1
        while len(new_arr) < mid and i < m:
            new_arr.append(nums1[i])
            i += 1
        while len(new_arr) < mid and j < n:
            new_arr.append(nums2[j])
            j += 1
        if (m + n) % 2 == 0:
            return (new_arr[-1] + new_arr[-2]) / 2
        return new_arr[-1]