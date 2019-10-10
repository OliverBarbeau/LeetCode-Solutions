# Problem #74
# https://leetcode.com/problems/search-a-2d-matrix
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

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