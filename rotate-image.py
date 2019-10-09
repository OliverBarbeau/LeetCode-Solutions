class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n= len(matrix)
        #if pos is i,j new pos is j, n-i-1
        seen = set()
        temp = None
        for layer in range(n//2):
            first = layer
            last = n-layer-1
            for i in range(first, last):
                offset = i-first
                top = matrix[first][i]
                matrix[first][i] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[i][last]
                matrix[i][last] = top