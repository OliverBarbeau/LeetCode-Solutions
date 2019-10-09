class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroLocations = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroLocations.append((i,j))
        for (i,j) in zeroLocations:
            for k in range(len(matrix)):
                matrix[k][j] = 0
            for l in range(len(matrix[0])):
                matrix[i][l] = 0