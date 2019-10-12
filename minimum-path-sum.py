# Problem #64
# https://leetcode.com/problems/minimum-path-sum/
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        #every nodes minPathSum is the min of the minPathSums of the nodes that can be traveled to + itself
        #store a dictionary of minPathSums
        #if we have seen a value before we return what is in the dictionary
        locToPathSum = {}
        def pathsArray(i, j):
            p = []
            right = None
            down = None
            if i < len(grid)-1:
                down = (i+1, j)
            if j < len(grid[0])-1:
                right = (i,j+1)
            if right is not None and down is not None and grid[down[0]][down[1]] > grid[right[0]][right[1]]:
                p.append(right)
                p.append(down)
            elif right is not None and down is not None:
                p.append(down)
                p.append(right)
            elif right is not None:
                p.append(right)
            elif down is not None:
                p.append(down)
            return p
        def minPathSum_(i,j):
            if (i,j) in locToPathSum:
                return locToPathSum[(i,j)]
            paths = pathsArray(i, j)
            if len(paths) == 0:
                locToPathSum[(i,j)] = grid[i][j]
                return locToPathSum[(i,j)]
            paths = [minPathSum_(p[0], p[1]) for p in paths]
            thisPath = grid[i][j] + min(paths)
            locToPathSum[(i,j)] = thisPath
            return thisPath
        return minPathSum_(0,0)