# Easy
# O(log n)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        mid = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            print(f"l: {low} mid: {mid} h:{high}")
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if nums[mid] < target:
            mid += 1
        return mid