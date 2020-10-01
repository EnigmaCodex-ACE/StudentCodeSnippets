# Medium
# https://leetcode.com/problems/pancake-sorting/
# Time Complexity: O(N^2)

class Solution:
    def flip(self, arr, k):
        arr[:k] = arr[k-1::-1]
    def pancakeSort(self, arr: List[int]) -> List[int]:
        out = []
        for i in range(len(arr) - 1, -1, -1):
            maxi = i
            for j in range(0, i):
                if arr[j] > arr[maxi]:
                    maxi = j
            out.append(maxi + 1)
            self.flip(arr, maxi + 1)
            out.append(i + 1)
            self.flip(arr, i + 1)
        return out
            
#         3 2 4 1 -> maxi = 4 - > flip(arr, maxi) -> 4 2 3 1 -> flip(arr, i)