# Medium
# https://leetcode.com/problems/set-matrix-zeroes/
# https://www.byte-by-byte.com/zeromatrix/?utm_source=optin_carrot&utm_medium=pdf&utm_campaign=50questions

class Solution: # Time Complexity : O(R * C) SPACE : O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #  Determine whether the first row or first column is true
        row_zero = False
        col_zero = False
        
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                row_zero = True
                break
        
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                col_zero = True
                break
                
        #  For each cell not in the first row/column, if it is true, set the 
        #  cell in the first row/same column and first column/same row to be 
        #  true
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
    
        # Go through the first column and set each row to true where cell in
        # the first column is true
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(1, len(matrix)):
                    matrix[row][col] = 0
    
        # Repeat for the rows
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                matrix[row] = [0] * len(matrix[row])
        
        # Set first row/column to true if necessary
        if row_zero:
            matrix[0] = [0] * len(matrix[0])
        if col_zero:
            for row in range(1, len(matrix)):
                matrix[row][0] = 0