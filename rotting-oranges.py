# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

# Example 1:

# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Note:

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.

import queue

class Solution:
   
    def orangesRotting(self, grid: List[List[int]]) -> int:
        size = (len(grid), len(grid[0]))
        
        def top(coords):
            if coords[0] <= 0:
                return -1
            else:
                return (coords[0]-1, coords[1])
        def bottom(coords):
            if coords[0] >= size[0]-1:
                return -1
            else:
                return (coords[0]+1, coords[1])
        def right(coords):
            if coords[1] >= size[1]-1:
                return -1
            else:
                return (coords[0], coords[1]+1)
        def left(coords):
            if coords[1] <= 0:
                return -1
            else:
                return (coords[0], coords[1]-1)
        def cardinal(coords):
            return [top(coords), bottom(coords), left(coords), right(coords)]
        q = queue.Queue()
        freshCount = 0
        for i in range(size[0]):
            for j in range(size[1]):
                item = grid[i][j]
                if item == 2:
                    coords = (i,j)
                    q.put(coords)
                elif item == 1:
                    print("Fresh fruit at:", i, j)
                    freshCount += 1
        minutes = 0
        while not q.empty():
            q2 = queue.Queue()
            while not q.empty():
                coord = q.get()
                coords = cardinal(coord)
                for coord in coords:
                    print(coord)
                    if coord != -1:
                        if grid[coord[0]][coord[1]] == 1:
                            freshCount -= 1
                            q2.put(coord)
                            grid[coord[0]][coord[1]] = 2
            q = q2
            if not q2.empty():
                minutes += 1
                
            
        
            
        if freshCount != 0:
            return -1
        else:
            return minutes