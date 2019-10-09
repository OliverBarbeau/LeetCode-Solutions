class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first binary search through first layer for the list where target lays within
        m = len(matrix)-1
        if m == -1:
            return False
        n = len(matrix[0])-1
        if n == -1:
            return False
        mid = -1
        indexOfArray = -1
        lo, hi = 0, m
        while indexOfArray == -1 and lo <= hi:
            mid = (lo + hi) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][n]:
                indexOfArray = mid
            elif target > matrix[mid][n]:
                lo = mid + 1
            else:
                hi = mid - 1
        lo, hi = 0, n
        while indexOfArray != -1 and lo <= hi:
            mid = (lo + hi) // 2
            if target == matrix[indexOfArray][mid]:
                return True
            elif target > matrix[indexOfArray][mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        #print(matrix[indexOfArray])
        return False