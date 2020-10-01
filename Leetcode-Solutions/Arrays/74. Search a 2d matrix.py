# Medium
# https://leetcode.com/problems/search-a-2d-matrix/

# Time Complexity : O(n + m)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        r = 0 
        c = len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            if target > matrix[r][c] :
                r += 1
            else:
                c -= 1
        return False