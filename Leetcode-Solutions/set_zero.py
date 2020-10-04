class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ZeroMatrix = False
        isCol = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            if matrix[i][0] == 0:
                isCol = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,R):
            for j in range(1, C):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(C):
                matrix[0][i] = 0
        if isCol:
            for i in range(R):
                matrix[i][0] = 0
